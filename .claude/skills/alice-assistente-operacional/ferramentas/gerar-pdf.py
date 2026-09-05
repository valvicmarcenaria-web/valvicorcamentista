#!/usr/bin/env python3
"""
Gera o PDF de um documento HTML da Valvic e confere se o conteúdo estourou a página.

    python3 gerar-pdf.py caminho/documento.html [caminho/saida.pdf]

Sem o segundo argumento, o PDF sai ao lado do HTML com o mesmo nome.

Por que existe: todo documento da casa (ficha, painel, checklist, termo) é escrito em HTML
com medida exata de folha e vira PDF para impressão. O erro mais comum não é o PDF falhar —
é o conteúdo passar do rodapé sem ninguém notar, e só se descobrir na impressora. Este
script mede três coisas antes de entregar:

  over_sheet  quanto o conteúdo passou da altura da folha (.sheet). Tem de ser 0.
  over_body   quanto a página inteira passou. Tem de ser 0.
  folga       espaço entre o último elemento e o rodapé, em px. Negativo = invadiu.

Se der estouro, o caminho é reduzir preenchimento (padding) das caixas e encurtar texto —
não diminuir a fonte, que estraga a leitura na fábrica.
"""
import json
import os
import subprocess
import sys
import tempfile

NODE = '/opt/node22/bin/node'
NODE_PATH = '/opt/node22/lib/node_modules'
CHROMIUM = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'

JS = r"""
const {chromium} = require('playwright');
(async () => {
  const [htmlPath, pdfPath] = process.argv.slice(2);
  const browser = await chromium.launch({executablePath: CHROMIUM_PATH, args: ['--no-sandbox']});
  const page = await browser.newPage();
  await page.goto('file://' + htmlPath, {waitUntil: 'networkidle'});
  const medida = await page.evaluate(() => {
    const folhas = [...document.querySelectorAll('.sheet, .folha, .page')];
    const rodape = document.querySelector('.rodape, .rf, footer');
    let overSheet = 0;
    for (const f of folhas) overSheet = Math.max(overSheet, f.scrollHeight - f.clientHeight);
    let folga = null;
    if (rodape) {
      const irmaos = [...rodape.parentElement.children].filter(e => e !== rodape);
      const ultimo = irmaos[irmaos.length - 1];
      if (ultimo) folga = Math.round(rodape.getBoundingClientRect().top - ultimo.getBoundingClientRect().bottom);
    }
    return {
      folhas: folhas.length,
      over_sheet: overSheet,
      over_body: document.body.scrollHeight - document.body.clientHeight,
      folga: folga,
    };
  });
  await page.pdf({path: pdfPath, printBackground: true, preferCSSPageSize: true});
  await browser.close();
  console.log(JSON.stringify(medida));
})();
"""


def gerar(html, pdf=None):
    html = os.path.abspath(html)
    if not os.path.exists(html):
        raise SystemExit(f'não encontrei o HTML: {html}')
    pdf = os.path.abspath(pdf) if pdf else os.path.splitext(html)[0] + '.pdf'

    with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False) as f:
        f.write(JS.replace('CHROMIUM_PATH', json.dumps(CHROMIUM)))
        script = f.name
    try:
        env = dict(os.environ, NODE_PATH=NODE_PATH)
        saida = subprocess.run([NODE, script, html, pdf], env=env,
                               capture_output=True, text=True)
    finally:
        os.unlink(script)

    if saida.returncode != 0:
        raise SystemExit('falhou ao gerar o PDF:\n' + (saida.stderr or saida.stdout))

    medida = json.loads(saida.stdout.strip().splitlines()[-1])
    print(f'PDF gerado: {pdf}')
    print(f"  folhas ....... {medida['folhas']}")
    print(f"  over_sheet ... {medida['over_sheet']}  (tem de ser 0)")
    print(f"  over_body .... {medida['over_body']}  (tem de ser 0)")
    if medida['folga'] is not None:
        print(f"  folga rodapé . {medida['folga']} px  (negativo = invadiu o rodapé)")

    problema = medida['over_sheet'] > 0 or medida['over_body'] > 0 or \
        (medida['folga'] is not None and medida['folga'] < 0)
    if problema:
        print('\n  ATENÇÃO: o conteúdo passou da folha. Reduza o padding das caixas e')
        print('  encurte os textos longos antes de imprimir — não diminua a fonte.')
    return medida


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    gerar(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
