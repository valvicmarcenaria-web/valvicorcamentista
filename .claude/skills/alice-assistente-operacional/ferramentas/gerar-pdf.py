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
  páginas     quantas páginas o PDF tem. Precisa bater com o nº de .sheet do HTML.

A contagem de páginas pega o erro mais silencioso de todos: a folha mede certo na tela,
não estoura nada, e mesmo assim o PDF sai com uma página em branco depois de cada folha.
A causa é quase sempre a mesma — falta a regra que zera a margem de tela na impressão:

    @media print{ body{ background:#fff; } .sheet{ margin:0; box-shadow:none; } }

Sem ela, os 16px de margem de cada .sheet empurram a folha para além da página.

Se der estouro, o caminho é reduzir preenchimento (padding) das caixas e encurtar texto —
não diminuir a fonte, que estraga a leitura na fábrica.
"""
import json
import os
import re
import subprocess
import sys
import tempfile

def paginas_do_pdf(caminho):
    """Nº de páginas do PDF, lido do /Count do nó raiz de páginas.

    Sem dependência externa: o pdftotext some quando o contêiner é recriado, e
    esta conferência não pode depender de um binário que pode não estar lá.
    """
    try:
        with open(caminho, 'rb') as fp:
            bruto = fp.read()
    except OSError:
        return None
    contagens = [int(n) for n in re.findall(rb'/Count\s+(\d+)', bruto)]
    return max(contagens) if contagens else None


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
    medida['paginas'] = paginas_do_pdf(pdf)
    print(f'PDF gerado: {pdf}')
    print(f"  folhas ....... {medida['folhas']}")
    print(f"  páginas PDF .. {medida['paginas']}  (tem de ser igual a folhas)")
    print(f"  over_sheet ... {medida['over_sheet']}  (tem de ser 0)")
    print(f"  over_body .... {medida['over_body']}  (tem de ser 0)")
    if medida['folga'] is not None:
        print(f"  folga rodapé . {medida['folga']} px  (negativo = invadiu o rodapé)")

    if medida['over_sheet'] > 0 or medida['over_body'] > 0 or \
            (medida['folga'] is not None and medida['folga'] < 0):
        print('\n  ATENÇÃO: o conteúdo passou da folha. Reduza o padding das caixas e')
        print('  encurte os textos longos antes de imprimir — não diminua a fonte.')
    if medida['paginas'] and medida['paginas'] != medida['folhas']:
        print(f"\n  ATENÇÃO: o HTML tem {medida['folhas']} folha(s) e o PDF saiu com "
              f"{medida['paginas']} página(s).")
        print('  Quase sempre falta esta regra no CSS:')
        print('    @media print{ body{ background:#fff; } .sheet{ margin:0; box-shadow:none; } }')
    return medida


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    gerar(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
