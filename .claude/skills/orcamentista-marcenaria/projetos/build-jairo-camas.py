# -*- coding: utf-8 -*-
"""JAIRO — três camas · FOLHA ÚNICA  [07/10/2026]

Cliente com marcenaria JÁ EM ANDAMENTO (`2026-jairo-samuel-marcenaria.md`,
parceria com a Jéssica Sollero). Esta é uma proposta de COMPLEMENTO — não
reapresenta a casa, retoma um projeto que já corre.

Números de `calculo-jairo-camas.py`; nada digitado à mão.
A escada padrão foi copiada da própria proposta do Jairo, para não inventar
um padrão que a casa não usa.

⛔⛔ Sem metragem nem quantitativo. Exceções autorizadas aqui: espessura de
   painel (30 mm), afastador (15 mm) e o PERFIL de metalon (30 × 20), que é
   nome comercial de tubo e não cota de peça.
⛔ Classes novas levam sufixo J.
"""
import pathlib, subprocess, base64, os, importlib.util, sys, io, contextlib

P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('jc', P/'calculo-jairo-camas.py')
jc = importlib.util.module_from_spec(spec); sys.modules['jc'] = jc
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(jc)

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
br2 = lambda v: f'{v:,.2f}'.replace(',','X').replace('.',',').replace('X','.')

CLIENTE, DATA = 'Jairo Samuel', '7 de outubro de 2026'
VALIDADE = '7 dias úteis'

def uri(nome):
    return ('data:image/jpeg;base64,'
            + base64.b64encode((P/'img'/nome).read_bytes()).decode())
IMG = uri('cama-referencia.jpg')

# ── a condição especial, do motor ─────────────────────────────────────────
ESP = [x for x in jc.LINHAS if x[0].startswith('60%')][0]
ESP_BRUTO = ESP[1]                        # 7.650
ESP_ENT   = ESP_BRUTO*0.60
ESP_SLD   = ESP_BRUTO - ESP_ENT

CSS = (open(P/'css-proposta.css', encoding='utf-8').read() + """
/* ── três camas · folha única ─────────────────────────────────────────── */
/* ⛔ flex:none em TODO bloco fechado: .pad é coluna flex e um box com
      overflow:hidden ENCOLHE em silêncio quando a coluna estoura. */
.topJ{display:flex;justify-content:space-between;align-items:baseline;gap:8mm;
  padding-bottom:4.2mm;border-bottom:1px solid var(--hair);flex:none;}
.topJ .b{font-family:'Cormorant Garamond',Georgia,serif;font-size:13.5pt;
  font-weight:700;letter-spacing:.02em;}
.topJ .m{font-size:7.2pt;letter-spacing:.17em;text-transform:uppercase;
  color:var(--mut);font-weight:700;text-align:right;}

.leadJ{color:var(--soft);font-size:9.2pt;line-height:1.56;max-width:158mm;
  flex:none;}
.leadJ b{color:var(--ink);font-weight:600;}

.duoJ{display:flex;gap:7mm;align-items:flex-start;margin-top:4mm;flex:none;}
.duoJ .fig{flex:none;width:74mm;border-radius:5px;overflow:hidden;line-height:0;}
.duoJ .fig img{display:block;width:100%;height:auto;}
.duoJ .cap{line-height:1.4;font-size:7pt;color:var(--mut);margin-top:1.6mm;
  letter-spacing:.04em;}
.duoJ .txt{flex:1;}
.duoJ .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.duoJ .d{color:var(--soft);font-size:8.1pt;line-height:1.45;margin-top:1.8mm;}
.duoJ .d b{color:var(--ink);font-weight:600;}
.duoJ .d p{margin:0 0 1.5mm;}
.duoJ .d p:last-child{margin-bottom:0;}

.tresJ{display:flex;gap:4mm;margin-top:4mm;flex:none;}
.tresJ > div{flex:1;border-top:2px solid var(--gold);padding-top:2.4mm;}
.tresJ .n{font-family:'Cormorant Garamond',Georgia,serif;font-size:13pt;
  font-weight:700;line-height:1.1;}
.tresJ .s{font-size:7.8pt;color:var(--soft);margin-top:.8mm;line-height:1.4;}

.ofJ{margin-top:4mm;border:1.5px solid var(--gold);border-radius:6px;
  background:rgba(201,169,106,.07);padding:4.8mm;display:flex;gap:6mm;
  align-items:center;flex:none;}
.ofJ > div{flex:1;}
.ofJ > div + div{border-left:1px solid var(--gold-lt);padding-left:6mm;flex:1.35;}
.ofJ .k{font-size:7pt;letter-spacing:.18em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.ofJ .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:28pt;
  font-weight:700;line-height:1.05;margin-top:1.4mm;}
.ofJ .v small{font-family:'DM Sans',sans-serif;font-size:9pt;font-weight:400;
  color:var(--soft);}
.ofJ .s{font-size:8.1pt;color:var(--soft);margin-top:1.4mm;line-height:1.5;}
.ofJ .s b{color:var(--ink);font-weight:600;}
.ofJ .sel{font-family:'Cormorant Garamond',Georgia,serif;font-size:17pt;
  font-weight:700;line-height:1.15;margin-top:1.4mm;}

.escJ{margin-top:4mm;flex:none;}
.escJ .ttl{font-size:6.9pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--mut);font-weight:700;padding-bottom:1.6mm;}
.escJ .l{display:flex;justify-content:space-between;align-items:baseline;
  gap:6mm;padding:1.6mm 0;border-top:1px solid var(--hair);font-size:8.5pt;
  color:var(--soft);}
.escJ .l b{color:var(--ink);font-weight:600;}
.escJ .l .x{flex:none;font-size:8pt;letter-spacing:.1em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}

.cndJ{display:grid;grid-template-columns:repeat(4,1fr);gap:5mm;margin-top:4mm;
  padding-top:2.8mm;border-top:1px solid var(--hair);flex:none;}
.cndJ .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.cndJ .d{color:var(--soft);font-size:8pt;margin-top:1mm;line-height:1.44;}
.cndJ .d b{color:var(--ink);}
.notaJ{margin-top:3.4mm;padding-left:4mm;border-left:2.5px solid var(--gold-lt);
  font-size:7.9pt;color:var(--soft);line-height:1.5;flex:none;}
.notaJ b{color:var(--ink);}
""")

escada = ''.join(
    f'<div class="l"><div>{rot}</div>'
    f'<div class="x">{"sem desconto" if d == 0 else f"−{d*100:.0f}%"}</div></div>'
    for rot, d, *_ in [(r, dd) for r, dd, _, _, _ in jc.PADRAO])

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>

<div class="page"><div class="pad">

  <div class="topJ">
    <div class="b">Valvic Marcenaria</div>
    <div class="m">Proposta complementar<br>{CLIENTE} · {DATA}</div>
  </div>

  <div style="margin-top:5mm;" class="eyebrow">Dormitórios</div>
  <div class="h-sec serif" style="font-size:24pt;">Três camas,<br>
    <em>o mesmo desenho.</em></div>
  <div class="rule"></div>
  <div class="leadJ">Jairo, <b>a marcenaria do apartamento já está em
  produção</b> — e as camas entram no mesmo caderno, com o mesmo Carvalho
  Hanover que atravessa a cristaleira, a cabeceira e o painel da suíte.
  Fechar agora é manter tudo numa <b>única data de instalação</b>.</div>

  <div class="duoJ">
    <div class="fig">
      <img src="{IMG}" alt="">
      <div class="cap">Base flutuante, lateral de corpo cheio — a referência
      do desenho</div>
    </div>
    <div class="txt">
      <div class="k">Como são feitas</div>
      <div class="d">
        <p>Estrutura em <b>MDF melamínico Carvalho Hanover de 30 mm</b>, a
        mesma linha e o mesmo tom do restante do apartamento.</p>
        <p>Estrado em <b>metalon 30 × 20</b> com <b>pintura
        eletrostática</b> — estrutura metálica, não ripa de madeira: é o que
        segura o colchão plano por anos sem ceder no meio.</p>
        <p>Apoios frontais <b>tubulares de aço</b>, com base protegida por
        <b>tampa plástica e feltro</b> — não marcam o piso.</p>
        <p><b>Sapatas reguláveis</b> sob a base, com afastador do chão de
        <b>15 mm</b>: nivelam em piso torto e mantêm o painel longe da
        umidade da limpeza.</p>
      </div>
    </div>
  </div>

  <div class="tresJ">
    <div><div class="n">Queen</div></div>
    <div><div class="n">Viúva</div></div>
    <div><div class="n">Solteiro</div></div>
  </div>

  <div class="ofJ">
    <div>
      <div class="k">As três camas</div>
      <div class="v">R$ {br(jc.TOTAL)}</div>
      <div class="s">Prazo de <b>{jc.PRAZO}</b>.</div>
    </div>
    <div>
      <div class="k">Condição especial · à vista</div>
      <div class="sel">R$ {br2(ESP_ENT)} na assinatura<br>
        e R$ {br2(ESP_SLD)} na entrega</div>
      <div class="s"><b>10% de desconto</b> — acima de qualquer condição da
      tabela. Total de <b>R$ {br2(ESP_BRUTO)}</b>.</div>
    </div>
  </div>

  <div class="escJ">
    <div class="ttl">Ou nas condições de sempre</div>
    {escada}
  </div>

  <div class="cndJ">
    <div><div class="k">Prazo</div><div class="d">
      <b>{jc.PRAZO}</b>, contados do aceite.</div></div>
    <div><div class="k">Garantia</div><div class="d">
      <b>10 anos</b> sobre estrutura e ferragens.</div></div>
    <div><div class="k">Execução</div><div class="d">
      Do corte à instalação, com <b>equipe própria</b>.</div></div>
    <div><div class="k">Validade</div><div class="d">
      <b>{VALIDADE}</b> a partir desta data.</div></div>
  </div>

  <div class="notaJ"><b>Não inclusos:</b> colchões, roupa de cama, cabeceiras
  estofadas e o mobiliário solto dos dormitórios.</div>

  <div class="foot"><span>Valvic Marcenaria</span>
    <span>{CLIENTE} · proposta complementar</span>
    <span>{DATA}</span></div>

</div></div>
</body></html>"""

(P/'proposta-jairo-camas.html').write_text(HTML, encoding='utf-8')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-jairo-camas.pdf')],
               check=True, env=env)
print('proposta-jairo-camas.pdf · 1 página')
print(f'  Investimento ....... R$ {br(jc.TOTAL)}')
print(f'  Especial (−10%) .... R$ {br2(ESP_ENT)} + R$ {br2(ESP_SLD)}'
      f'  = R$ {br2(ESP_BRUTO)}')
print(f'  Prazo .............. {jc.PRAZO}')
