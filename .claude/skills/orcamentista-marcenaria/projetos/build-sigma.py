# -*- coding: utf-8 -*-
"""SIGMA — proposta · sala de diretoria  [14/10/2026]

⭐ [Jonathan 14/10] "capricha no layout. É cliente recorrente. Não crie
   muita narrativa, organize bem os valores e seja ousado no design."

   → CSS PRÓPRIO, não o `css-proposta.css` da casa. A paleta sai do
     PRÓPRIO PROJETO: Grafito, Jequitibá e Lino, as três chapas da Braz.
     A proposta tem a cara do móvel que vende.
   → Pouca palavra: uma linha por móvel, o valor grande e à direita.

Números de `corte-sigma-diretoria.py`; nada digitado à mão.
⛔ Sem metragem e sem contagem. Os códigos 01…06 são da PRANCHA, não
   quantidade.
"""
import pathlib, subprocess, importlib.util, sys, io, contextlib, os, base64

P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('sg', P/'corte-sigma-diretoria.py')
sg = importlib.util.module_from_spec(spec); sys.modules['sg'] = sg
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(sg)

br = lambda v: f'{v:,.0f}'.replace(',', '.')
CLIENTE, OBRA, DATA = 'Reginaldo', 'Sigma · Belo Horizonte', '14 de outubro de 2026'
ARQ = 'Braz Arquitetura & Interiores'
PRAZO, VALIDADE, GARANTIA = '60 dias corridos', '7 dias úteis', '10 anos'
NP = 4

def uri(n):
    return ('data:image/jpeg;base64,'
            + base64.b64encode((P/'img-sigma'/n).read_bytes()).decode())
HERO, NICHOS, MESA = uri('sigma-hero.jpg'), uri('sigma-nichos.jpg'), uri('sigma-mesa.jpg')
SALA = uri('sigma-sala.jpg')

ITENS = [
 ('01', 'Aparador', 'Portas em tela de bambu, tampo e base em Grafito.',
  sg.R['PV']['01 · Aparador']),
 ('02', 'Prateleiras suspensas', 'Em Jequitibá, com luz sob cada uma.',
  sg.R['PV']['02 · Prateleiras suspensas']),
 ('03', 'Mesa do diretor', 'Tampo e pé em Jequitibá, gaveteiro em Grafito, '
  'passagem de cabos embutida.', sg.R['PV']['03 · Mesa do diretor']),
 ('05', 'Móvel do café', 'Estante de nichos iluminados, espaço para frigobar '
  'e adega, e armário fechado com gavetas.', sg.R['PV']['05 · Móvel do café']),
 ('06', 'Adorno de parede', 'Peças orgânicas em Lino, retroiluminadas, com '
  'prateleira suspensa.', sg.R['PV']['06 · Adorno de parede']),
]
MARC, LED, TOTAL = sg.R['TOT'], sg.LED_PV, sg.TOTAL
# ⛔⛔ TRAVA DE SOMA
_s = sum(v for _c, _n, _d, v in ITENS)
assert abs(_s - MARC) < 0.5, f'⛔ A TABELA NÃO FECHA: {_s:,.0f} ≠ {MARC:,.0f}'
assert abs(MARC + LED - TOTAL) < 0.5, '⛔ O TOTAL NÃO FECHA'

CSS = """
:root{
  --graf:#33373A; --graf-d:#212426; --jeq:#B07C44; --jeq-lt:#D9B482;
  --lino:#F3ECE4; --ink:#1B1A18; --soft:#5E5A54; --mut:#948D83;
  --hair:#E8E1D8; --line:#D8CFC3; --paper:#fff;
}
@page{size:A4;margin:0;}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{margin:0;font-family:'DM Sans',Arial,sans-serif;color:var(--ink);
     font-size:9.5pt;line-height:1.6;}
.serif{font-family:'Cormorant Garamond',Georgia,serif;}
.page{position:relative;width:210mm;height:297mm;overflow:hidden;
      background:var(--paper);page-break-after:always;}
.page:last-of-type{page-break-after:avoid;}
.pad{padding:18mm 19mm 14mm;height:100%;display:flex;flex-direction:column;}
.foot{margin-top:auto;padding-top:7mm;border-top:1px solid var(--hair);
      display:flex;justify-content:space-between;font-size:7pt;
      letter-spacing:.18em;text-transform:uppercase;color:var(--mut);flex:none;}

/* ── CAPA: faixa escura à esquerda, imagem sangrando à direita ───────── */
.cv{display:grid;grid-template-columns:97mm 113mm;height:297mm;}
.cv .L{background:var(--graf);color:#F4EFE8;padding:20mm 14mm 14mm 19mm;
  display:flex;flex-direction:column;}
.cv .R{background:#000;overflow:hidden;line-height:0;}
.cv .R img{width:100%;height:100%;object-fit:cover;opacity:.95;}
.cv .mark{font-size:8.4pt;letter-spacing:.42em;text-transform:uppercase;
  color:#EDE4D5;font-weight:700;}
.cv .kick{margin-top:auto;font-size:7pt;letter-spacing:.3em;
  text-transform:uppercase;color:var(--jeq-lt);font-weight:700;}
.cv h1{font-family:'Cormorant Garamond',Georgia,serif;font-size:40pt;
  line-height:1.02;font-weight:600;letter-spacing:-.02em;margin:4mm 0 0;}
.cv .sub{font-size:10.5pt;color:#C9C2B6;margin-top:4mm;font-weight:300;}
.cv .big{margin-top:10mm;padding-top:0;border-top:1px solid rgba(255,255,255,.18);}
.cv .big .k{font-size:6.8pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--jeq-lt);font-weight:700;}
.cv .big .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:40pt;
  font-weight:700;line-height:1.05;margin-top:1mm;letter-spacing:-.02em;}
.cv .meta{margin-top:8mm;display:grid;grid-template-columns:1fr 1fr;gap:6mm 5mm;}
.cv .meta .k{font-size:6.4pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--jeq-lt);font-weight:700;}
.cv .meta .v{font-size:10pt;color:#E7E0D4;margin-top:1mm;}
.cv .ft{margin-top:7mm;font-size:6.8pt;letter-spacing:.16em;
  text-transform:uppercase;color:#8F8779;}

/* ── página de valores ──────────────────────────────────────────────── */
.hd{display:flex;justify-content:space-between;align-items:baseline;
  border-bottom:1.6px solid var(--ink);padding-bottom:3.4mm;flex:none;}
.hd .b{font-size:8pt;letter-spacing:.4em;text-transform:uppercase;font-weight:700;}
.hd .m{font-size:7pt;letter-spacing:.16em;text-transform:uppercase;
  color:var(--mut);font-weight:700;}
.eye{font-size:7pt;letter-spacing:.3em;text-transform:uppercase;
  color:var(--jeq);font-weight:700;margin-top:8mm;flex:none;}
.h1{font-family:'Cormorant Garamond',Georgia,serif;font-size:30pt;
  line-height:1.05;font-weight:600;letter-spacing:-.02em;margin-top:2mm;flex:none;}

.rows{margin-top:7mm;flex:none;}
.row{display:grid;grid-template-columns:16mm 1fr 34mm;gap:5mm;align-items:start;
  padding:4.6mm 0;border-top:1px solid var(--line);}
.row:first-child{border-top:1.6px solid var(--ink);}
.row .n{font-family:'Cormorant Garamond',Georgia,serif;font-size:27pt;
  line-height:.85;color:var(--jeq);font-weight:700;}
.row .t{font-size:12.5pt;font-weight:600;letter-spacing:-.01em;}
.row .d{color:var(--soft);font-size:8.6pt;line-height:1.46;margin-top:1.2mm;
  max-width:92mm;}
.row .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:19pt;
  font-weight:700;text-align:right;line-height:1;padding-top:1mm;
  font-variant-numeric:tabular-nums;}

.band{margin-top:7mm;background:var(--graf);color:#F4EFE8;border-radius:3px;
  padding:7mm 8mm;flex:none;}
.band .l{display:flex;justify-content:space-between;align-items:baseline;
  padding:2.2mm 0;font-size:9.4pt;color:#D3CCC0;}
.band .l.sep{border-top:1px solid rgba(255,255,255,.16);margin-top:2mm;
  padding-top:5mm;}
.band .l .big{font-family:'Cormorant Garamond',Georgia,serif;font-size:34pt;
  font-weight:700;color:#fff;line-height:1;letter-spacing:-.02em;}
.band .l .lab{font-size:7.4pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--jeq-lt);font-weight:700;}
.band .v{font-variant-numeric:tabular-nums;}

/* ── página de valor ────────────────────────────────────────────────── */
.vw{position:relative;height:106mm;overflow:hidden;line-height:0;flex:none;
  margin:0 -19mm;}
.vw img{width:100%;height:106mm;object-fit:cover;object-position:center 58%;}
.vw .ov{position:absolute;inset:0;
  background:linear-gradient(to top,rgba(33,36,38,.92) 0%,
             rgba(33,36,38,.45) 38%,rgba(33,36,38,0) 72%);}
.vw .cap{position:absolute;left:19mm;right:19mm;bottom:9mm;color:#F4EFE8;
  line-height:1.15;}
.vw .cap .k{font-size:6.8pt;letter-spacing:.3em;text-transform:uppercase;
  color:var(--jeq-lt);font-weight:700;}
.vw .cap .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:26pt;
  font-weight:600;letter-spacing:-.01em;margin-top:2.4mm;}
.vrow{display:grid;grid-template-columns:38mm 1fr;gap:7mm;align-items:baseline;
  padding:6mm 0;border-top:1px solid var(--line);flex:none;}
.vrow:first-of-type{border-top:1.6px solid var(--ink);margin-top:9mm;}
.vrow .k{font-size:7pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--jeq);font-weight:700;padding-top:2.4mm;}
.vrow .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:23pt;
  font-weight:600;line-height:1.05;letter-spacing:-.01em;}
.vrow .d{color:var(--soft);font-size:9pt;line-height:1.55;margin-top:2mm;
  max-width:118mm;}
.vrow .d b{color:var(--ink);font-weight:600;}

.strip{margin-top:6mm;display:grid;grid-template-columns:1fr 1fr;gap:3mm;
  flex:none;}
.strip .ph{border-radius:3px;overflow:hidden;line-height:0;}
.strip .ph img{width:100%;height:40mm;object-fit:cover;display:block;}

/* ── condições ──────────────────────────────────────────────────────── */
.pay{margin-top:6mm;flex:none;}
.pay .r{display:flex;justify-content:space-between;align-items:baseline;gap:6mm;
  padding:3mm 0;border-top:1px solid var(--line);font-size:9.4pt;color:var(--soft);}
.pay .r:first-child{border-top:1.6px solid var(--ink);}
.pay .r b{color:var(--ink);font-weight:600;}
.pay .r .x{flex:none;font-size:9pt;letter-spacing:.08em;text-transform:uppercase;
  color:var(--jeq);font-weight:700;}
.four{display:grid;grid-template-columns:repeat(4,1fr);gap:6mm;margin-top:6.5mm;
  padding-top:5mm;border-top:1.6px solid var(--ink);flex:none;}
.four .k{font-size:6.8pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--jeq);font-weight:700;}
.four .v{font-size:11.5pt;font-weight:600;margin-top:1.4mm;}
.four .s{color:var(--soft);font-size:8pt;margin-top:.8mm;line-height:1.4;}
.fora{margin-top:6mm;background:var(--lino);border-radius:3px;padding:6mm 7mm;
  flex:none;}
.fora .k{font-size:6.8pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--jeq);font-weight:700;}
.fora .d{color:var(--soft);font-size:8.5pt;line-height:1.55;margin-top:2mm;}
.fora .d b{color:var(--ink);font-weight:600;}
"""

def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria</span>'
            f'<span>{CLIENTE} · sala de diretoria</span><span>{n} / {NP}</span></div>')

p1 = f"""<div class="page"><div class="cv">
  <div class="L">
    <div class="mark">Valvic Marcenaria</div>
    <div class="kick" style="margin-top:34mm;">Proposta comercial</div>
    <h1>Sala de<br>Diretoria</h1>
    <div class="sub">{OBRA}<br>Projeto {ARQ}</div>
    <div class="big"></div>
    <div class="meta">
      <div><div class="k">Prazo</div><div class="v">{PRAZO}</div></div>
      <div><div class="k">Garantia</div><div class="v">{GARANTIA}</div></div>
      <div><div class="k">Execução</div><div class="v">Equipe própria</div></div>
      <div><div class="k">Validade</div><div class="v">{VALIDADE}</div></div>
    </div>
    <div class="ft">{CLIENTE} · {DATA}</div>
  </div>
  <div class="R"><img src="{HERO}" alt=""></div>
</div></div>"""

pv = f"""<div class="page"><div class="pad">
  <div class="hd"><div class="b">Valvic Marcenaria</div>
    <div class="m">{CLIENTE} · {DATA}</div></div>

  <div class="vw" style="margin-top:8mm;">
    <img src="{NICHOS}" alt="">
    <div class="ov"></div>
    <div class="cap">
      <div class="k">O que vai junto com o móvel</div>
      <div class="t">Três coisas que não aparecem<br>no desenho — e decidem
        o resultado.</div>
    </div>
  </div>

  <div class="vrow">
    <div class="k">Garantia</div>
    <div><div class="t serif">Dez anos.</div>
      <div class="d">Estrutura e ferragens dos cinco móveis. Não é selo de
      catálogo: é o prazo em que respondemos pelo que entregamos, com
      <b>equipe própria</b>, do corte à instalação.</div></div>
  </div>
  <div class="vrow">
    <div class="k">Ferragem</div>
    <div><div class="t serif">Hettich, alemã.</div>
      <div class="d"><b>Corrediça oculta</b> nas gavetas — o trilho some por
      baixo, a gaveta abre inteira e fecha com amortecimento. <b>Dobradiça
      com amortecedor</b> nas portas. É a ferragem que define se o móvel
      ainda fecha bem no décimo ano.</div></div>
  </div>
  <div class="vrow">
    <div class="k">Iluminação</div>
    <div><div class="t serif">Entregue acesa.</div>
      <div class="d">Fita e perfil <b>usinados dentro da própria peça</b>,
      não aparafusados depois. A marcenaria chega iluminada e alinhada —
      <b>a nossa parte vem instalada</b>, e a obra só liga o circuito.</div></div>
  </div>
  {foot(2)}
</div></div>"""

rows = ''.join(
    f'<div class="row"><div class="n">{c}</div>'
    f'<div><div class="t">{n}</div><div class="d">{d}</div></div>'
    f'<div class="v">{br(v)}</div></div>' for c, n, d, v in ITENS)

p2 = f"""<div class="page"><div class="pad">
  <div class="hd"><div class="b">Valvic Marcenaria</div>
    <div class="m">{CLIENTE} · {DATA}</div></div>
  <div class="eye">Peça a peça</div>
  <div class="h1 serif">O que entra,<br>e quanto é.</div>
  <div class="rows">{rows}</div>
  <div class="band">
    <div class="l"><span>Marcenaria</span><span class="v">R$ {br(MARC)}</span></div>
    <div class="l"><span>Iluminação de marcenaria</span>
      <span class="v">R$ {br(LED)}</span></div>
    <div class="l sep"><span class="lab">Investimento total</span>
      <span class="big">R$ {br(TOTAL)}</span></div>
  </div>
  {foot(3)}
</div></div>"""

p3 = f"""<div class="page"><div class="pad">
  <div class="hd"><div class="b">Valvic Marcenaria</div>
    <div class="m">{CLIENTE} · {DATA}</div></div>
  <div class="eye">Condições</div>
  <div class="h1 serif">Como fechamos.</div>

  <div class="strip">
    <div class="ph"><img src="{MESA}" alt=""></div>
    <div class="ph"><img src="{NICHOS}" alt=""></div>
  </div>

  <div class="pay">
    <div class="r"><div><b>30%</b> de entrada + restante em até 10× no cartão</div>
      <div class="x">R$ {br(TOTAL)}</div></div>
    <div class="r"><div><b>50%</b> de entrada + restante em até 8× no cartão</div>
      <div class="x">−3%</div></div>
    <div class="r"><div><b>70%</b> de entrada + restante em até 6× no cartão</div>
      <div class="x">−5%</div></div>
    <div class="r"><div><b>70%</b> de entrada + saldo por transferência</div>
      <div class="x">−7%</div></div>
  </div>

  <div class="four">
    <div><div class="k">Prazo</div><div class="v">{PRAZO}</div>
      <div class="s">Do aceite e da medição no local.</div></div>
    <div><div class="k">Garantia</div><div class="v">{GARANTIA}</div>
      <div class="s">Estrutura e ferragens.</div></div>
    <div><div class="k">Execução</div><div class="v">Equipe própria</div>
      <div class="s">Do corte à instalação.</div></div>
    <div><div class="k">Validade</div><div class="v">{VALIDADE}</div>
      <div class="s">A partir desta data.</div></div>
  </div>

  <div class="fora">
    <div class="k">O que não está incluso</div>
    <div class="d">A <b>mesa redonda e as cadeiras</b>, indicadas no projeto
    como modelo a definir; as <b>poltronas</b>, o <b>tapete</b> e a
    <b>cortina</b>; o <b>frigobar</b>, a <b>adega</b> e o <b>cofre</b> —
    fazemos o espaço, o equipamento é de vocês; a <b>fonte, o driver, o
    circuito e o interruptor</b> da iluminação, que são elétrica de obra;
    o <b>piso</b>, a <b>pintura</b> e as <b>luminárias de teto</b>.</div>
  </div>

  <div class="fora" style="background:#fff;border:1px solid var(--line);">
    <div class="k">A confirmar antes da produção</div>
    <div class="d">A prancha pede <b>conferir todas as medidas e o
    pé-direito no local</b> — fazemos a medição antes do corte, e é ela que
    fecha a altura do móvel do café. O <b>acabamento das portas do aparador
    em tela de bambu</b> depende de amostra aprovada por vocês e pela
    arquiteta.</div>
  </div>
  {foot(4)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600;700&family=DM+Sans:wght@300;400;500;600;700&display=swap" '
        'rel="stylesheet"><style>' + CSS + '</style></head><body>'
        + p1 + pv + p2 + p3 + '</body></html>')

(P/'proposta-sigma.html').write_text(HTML, encoding='utf-8')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-sigma.pdf')], check=True, env=env)
print(f'proposta-sigma.pdf · {NP} páginas')
for c, n, _d, v in ITENS: print(f'  {c} · {n:<26} R$ {br(v):>7}')
print(f'  {"":<4}  {"marcenaria":<26} R$ {br(MARC):>7}')
print(f'  {"":<4}  {"iluminação":<26} R$ {br(LED):>7}')
print(f'  {"":<4}  {"INVESTIMENTO":<26} R$ {br(TOTAL):>7}')
