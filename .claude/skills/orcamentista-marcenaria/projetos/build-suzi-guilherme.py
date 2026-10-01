# -*- coding: utf-8 -*-
"""PROPOSTA — SUZI E GUILHERME · sala e escritório  [01/10/2026]

Números vêm de `corte-suzi-guilherme.py`; nada é digitado à mão aqui.

⛔⛔ NUNCA PÔR METRAGEM NEM QUANTITATIVO NA PROPOSTA
   Sem cota, sem m², sem contagem de porta, prateleira ou nicho.
   ⭐ EXCEÇÃO AUTORIZADA, pedida pelo Jonathan em 01/10: o acabamento da
   cristaleira — **MDF melamínico amadeirado** — aparece EXPLÍCITO, porque é
   o que separa esta proposta de uma em lâmina natural. Não é medida, é
   especificação: o auditor de metragem não é afetado.
⛔ Classes novas levam sufixo S: `.invS`, `.escS`, `.cndS`, `.phS`, `.itS`.
"""
import pathlib, subprocess, importlib.util, sys, io, contextlib, os

P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('sg', P/'corte-suzi-guilherme.py')
sg = importlib.util.module_from_spec(spec); sys.modules['sg'] = sg
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(sg)

br = lambda v: f'{v:,.0f}'.replace(',', '.')
CLIENTE = 'Suzi e Guilherme'
PROJETO = 'Luiza Costa'
DATA    = '1º de outubro de 2026'
PRAZO   = '60 dias corridos'
VALID   = '10 dias corridos'
NP      = 4

def img(n): return f'img-suzi-guilherme/{n}.jpg'

CSS = (open(P/'css-proposta.css', encoding='utf-8').read()
       + open(P/'css-proposta-img.css', encoding='utf-8').read() + """
/* ── proposta Suzi e Guilherme ────────────────────────────────────────── */
.phS{background:#fff;overflow:hidden;position:relative;border:1px solid var(--hair);}
.phS img{display:block;width:100%;height:100%;object-fit:cover;}
.phS img.ct{object-fit:contain;}
.parS{display:grid;grid-template-columns:1fr 1fr;gap:4mm;}
.parS .phS{height:56mm;}

.itS{margin-top:5mm;}
.itS .n{font-family:'Cormorant Garamond',Georgia,serif;font-size:14pt;
  color:var(--gold-lt);font-weight:600;line-height:1;}
.itS .t{font-size:11.4pt;font-weight:700;letter-spacing:-.01em;margin-top:.6mm;}
.itS .d{color:var(--soft);font-size:8.7pt;line-height:1.64;margin-top:1.8mm;}
.itS .d b{color:var(--ink);font-weight:600;}

.exS{display:grid;grid-template-columns:1fr 1fr;gap:4.6mm 7mm;margin-top:5mm;}
.exS > div{border-top:1.5px solid var(--line);padding-top:3mm;}
.exS .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.exS .d{color:var(--soft);font-size:8.5pt;line-height:1.58;margin-top:1.5mm;}
.exS .d b{color:var(--ink);font-weight:600;}

table.invS{width:100%;border-collapse:collapse;margin-top:4mm;font-size:9pt;}
table.invS th{font-size:6.9pt;letter-spacing:.17em;text-transform:uppercase;
  color:var(--mut);font-weight:700;padding:0 0 2.4mm;text-align:left;}
table.invS th.r,table.invS td.r{text-align:right;}
table.invS td{padding:2mm 0;border-top:1px solid var(--hair);vertical-align:top;}
table.invS td.a{font-size:6.9pt;letter-spacing:.14em;text-transform:uppercase;
  color:var(--gold-lt);font-weight:700;padding-right:4mm;width:24mm;}
table.invS td.i{font-weight:600;}
table.invS tr.sub td{border-top:1px solid var(--line);color:var(--soft);
  font-size:8.2pt;padding:1.5mm 0;}
table.invS tr.tot td{border-top:1.6px solid var(--ink);padding-top:2.4mm;
  font-family:'Cormorant Garamond',Georgia,serif;font-size:16pt;font-weight:700;}
table.invS tr.tot td.a,table.invS tr.tot td.i{font-family:inherit;font-size:9.6pt;}

.otmS{margin-top:4mm;border:1.5px solid var(--gold);border-radius:5px;
  background:var(--gold-pale);padding:3.8mm 5.2mm;display:grid;
  grid-template-columns:1fr auto;gap:2mm 7mm;align-items:start;flex:none;}
.otmS .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.otmS .t{font-size:11pt;font-weight:700;margin-top:1mm;}
.otmS .d{color:var(--soft);font-size:8.3pt;line-height:1.56;margin-top:1.8mm;
  grid-column:1/2;grid-row:2/3;}
.otmS .d b{color:var(--ink);font-weight:600;}
.otmS .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:23pt;
  font-weight:700;white-space:nowrap;grid-column:2/3;grid-row:1/3;
  align-self:center;text-align:right;line-height:1;}
.otmS .v small{display:block;font-family:'DM Sans',sans-serif;font-size:7.4pt;
  letter-spacing:.14em;text-transform:uppercase;color:var(--gold);
  font-weight:700;margin-bottom:1.4mm;}

.escS{margin-top:4mm;border:1px solid var(--line);border-radius:5px;
  overflow:hidden;flex:none;}
.escS .l{display:flex;justify-content:space-between;align-items:baseline;
  padding:2.3mm 5mm;border-bottom:1px solid var(--hair);font-size:9pt;}
.escS .l:last-child{border-bottom:none;}
.escS .l .p{font-weight:700;font-size:11pt;color:var(--gold);min-width:14mm;}
.escS .l .q{color:var(--soft);flex:1;padding-left:4mm;}
.cndS{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm 5mm;margin-top:5mm;
  flex:none;}
.cndS .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.cndS .d{color:var(--soft);font-size:8pt;margin-top:1mm;line-height:1.44;}
.cndS .d b{color:var(--ink);}
.notaS{margin-top:4.5mm;padding-left:4mm;border-left:2.5px solid var(--gold-lt);
  font-size:8pt;color:var(--soft);line-height:1.5;flex:none;}
.notaS b{color:var(--ink);}
""")

def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria</span>'
            f'<span>{CLIENTE} · projeto {PROJETO}</span><span>{n} / {NP}</span></div>')

def it(num, titulo, desc):
    return (f'<div class="itS"><div class="n serif">{num}</div>'
            f'<div class="t">{titulo}</div><div class="d">{desc}</div></div>')

# ── 1 · capa ──────────────────────────────────────────────────────────────
p1 = f"""<div class="page cover"><div class="cv2">
  <div class="txt">
    <div class="eyebrow">Proposta comercial</div>
    <div class="cv-t serif">Marcenaria<br>sob medida.</div>
    <div class="cv-nome serif" style="font-size:40pt;">Suzi<br>e Guilherme</div>
    <div class="cv-s">Sala e escritório — projeto de interiores
    {PROJETO}.</div>
    <div class="cv-meta">
      <div><div class="k">Cliente</div><div class="v">{CLIENTE}</div></div>
      <div><div class="k">Ambientes</div><div class="v">Sala e escritório</div></div>
      <div><div class="k">Projeto</div><div class="v">{PROJETO}</div></div>
      <div><div class="k">Data</div><div class="v">{DATA}</div></div>
    </div>
    <div style="margin-top:auto;"><div class="cv-brand">Valvic Marcenaria</div></div>
  </div>
  <div class="ph"><img src="{img('bar-vista')}" alt=""></div>
</div></div>"""

# ── 2 · sala ──────────────────────────────────────────────────────────────
p2 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">A sala</div>
  <div class="h-sec serif">O bar, e as duas mesas.</div>
  <div class="rule"></div>

  <div class="parS" style="margin-top:5mm;">
    <div class="phS"><img class="ct" src="{img('bar-fechado')}" alt=""></div>
    <div class="phS"><img class="ct" src="{img('bar-aberto')}" alt=""></div>
  </div>

  {it('01', 'Cristaleira',
      'Frente inteira em <b>portas de vidro espelhado bronze</b>, com '
      '<b>puxador em perfil metálico bronze</b> — o vidro e o puxador entram '
      'no nosso fornecimento, <b>entregues instalados</b>. Por dentro, '
      'prateleiras em <b>MDF melamínico amadeirado</b> com <b>fita de LED '
      'embutida</b>, que acende o cristal através do espelhado.')}

  {it('02', 'Bar com nichos de vinho',
      'O módulo que fecha o canto, no mesmo <b>MDF melamínico amadeirado</b>: '
      '<b>nichos de vinho</b> em grade de ripas, prateleiras com LED e, na '
      'base, armário de <b>abertura por toque</b> ao lado do vão preparado '
      'para a cervejeira.')}

  {it('03', 'Mesa do café',
      'Aqui o acabamento muda: a mesa é em <b>lâmina natural</b>. O tampo é '
      '<b>marchetaria de verdade</b> — quadrados de <b>nogueira e carvalho</b> '
      'alternados, cortados e assentados um a um, prensados e envernizados. '
      'Pés e prateleira na mesma lâmina de nogueira.')}

  {it('04', 'Tampo novo da mesa de jantar',
      '<b>Tampo novo em lâmina natural</b>, acabado em <b>verniz PU de alta '
      'resistência</b>, com a aresta encorpada para ler cheia e '
      '<b>acabamento em meia-esquadria</b>. Construído em face laminada sobre '
      '<b>moldura estruturada</b> — fica leve, não sobrecarrega a estrutura '
      'existente e não barriga com o vão. A estrutura em madeira pintada de '
      'preto é existente e <b>permanece</b>.')}

  <div class="phS" style="margin-top:auto;height:50mm;">
    <img class="ct" src="{img('mesa-cafe')}" alt="">
  </div>
  {foot(2)}
</div></div>"""

# ── 3 · escritório ────────────────────────────────────────────────────────
p3 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">O escritório</div>
  <div class="h-sec serif">Uma parede inteira,<br><em>e a mesa.</em></div>
  <div class="rule"></div>

  <div class="parS" style="margin-top:5mm;">
    <div class="phS"><img class="ct" src="{img('escritorio-2')}" alt=""></div>
    <div class="phS"><img class="ct" src="{img('escritorio-1')}" alt=""></div>
  </div>

  {it('05', 'Painel e prateleiras',
      'Painel do piso ao teto em <b>MDF Nero Guararapes</b>, arrematado em '
      '<b>perfil de alumínio cinza</b>. Sobre ele, prateleiras em Nero e em '
      '<b>MDF Cinza Perfeito Guararapes</b>, e o <b>vidro leitoso branco de '
      'escrever</b> — também no nosso fornecimento, entregue instalado.')}

  {it('06', 'Mesa de trabalho',
      'Em <b>MDF Cinza Perfeito Guararapes</b>, com tampo encorpado e '
      '<b>acabamento em meia-esquadria</b> — a aresta fecha em quina viva, sem '
      'fita aparente. <b>Borracha de nivelamento nos pés</b> e passagem '
      'preparada para as tomadas de mesa.')}

  <div class="exS">
    <div><div class="k">Ferragem especificada · Hettich</div><div class="d">
      Dobradiça <b>Hettich Sensys</b>, com <b>amortecimento integrado</b> e
      regulagem nos três eixos, e <b>Hettich Push to open Silent</b> no
      armário de abertura por toque. É a ferragem que sustenta a garantia de
      dez anos.</div></div>
    <div><div class="k">Acabamento das peças em lâmina</div><div class="d">
      <b>Verniz PU de alta resistência</b> em três demãos sobre a lâmina
      natural, nas duas mesas da sala — superfície que aguenta copo, calor e
      limpeza sem marcar.</div></div>
    <div><div class="k">Dois acabamentos, de propósito</div><div class="d">
      O bar e o escritório são em <b>MDF melamínico</b> — superfície fechada,
      estável e de manutenção simples, que é o que um bar e uma mesa de
      trabalho pedem. <b>A lâmina natural fica só nas duas mesas da sala</b>,
      onde a madeira é o assunto.</div></div>
    <div><div class="k">Medição</div><div class="d">
      Medição no local <b>antes do corte</b>, nos dois ambientes. O projeto é
      de reforma e convive com peças existentes — a medida de projeto e a
      medida da parede raramente são a mesma.</div></div>
  </div>
  {foot(3)}
</div></div>"""

# ── 4 · investimento ──────────────────────────────────────────────────────
NOME = {'Sala · cristaleira envidraçada': 'Cristaleira',
        'Sala · bar com nichos de vinho': 'Bar com nichos de vinho',
        'Sala · mesa do café': 'Mesa do café',
        'Sala · tampo novo da mesa de jantar': 'Tampo novo da mesa de jantar',
        'Escritório · painel e prateleiras': 'Painel e prateleiras',
        'Escritório · mesa de trabalho': 'Mesa de trabalho'}
linhas, _am = '', None
for am in sg.AMBS:
    for m in sg.ITENS[am]:
        rot = am if am != _am else ''
        _am = am
        linhas += (f'<tr><td class="a">{rot}</td><td class="i">{NOME[m]}</td>'
                   f'<td class="r">R$ {br(sg.PV_IT[m])}</td></tr>')

p4 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="h-sec serif">Peça a peça.</div>
  <div class="rule"></div>

  <table class="invS">
    <thead><tr><th></th><th></th><th class="r">Investimento</th></tr></thead>
    <tbody>{linhas}
      <tr class="tot"><td class="a"></td><td class="i">Investimento item a item</td>
        <td class="r">R$ {br(sg.TOT)}</td></tr>
    </tbody>
  </table>

  <div class="otmS">
    <div><div class="k">Cenário de otimização</div>
      <div class="t">Fechamento completo</div></div>
    <div class="v"><small>−{int(sg.DESC_FECH*100)}%</small>R$ {br(sg.TOT_FECH)}</div>
    <div class="d">Todos os itens acima fechados <b>no mesmo contrato</b>:
    uma só compra de chapa, um só plano de corte, uma só produção e uma só
    montagem. O ganho volta para o cliente como <b>{int(sg.DESC_FECH*100)}% de
    desconto</b> sobre o investimento.</div>
  </div>

  <div class="escS">
    <div class="l"><span class="p">40%</span><span class="q">na assinatura — sobre o valor de fechamento</span></div>
    <div class="l"><span class="p">30%</span><span class="q">no início das montagens</span></div>
    <div class="l"><span class="p">30%</span><span class="q">na entrega final</span></div>
  </div>

  <div class="cndS">
    <div><div class="k">Prazo</div><div class="d">
      <b>{PRAZO}</b>, da assinatura, da entrada e da medição final.</div></div>
    <div><div class="k">Execução</div><div class="d">
      Do corte à instalação, com <b>equipe própria</b> da casa.</div></div>
    <div><div class="k">Validade</div><div class="d">
      <b>{VALID}</b> a partir desta data.</div></div>
    <div><div class="k">Garantia</div><div class="d">
      <b>10 anos</b> sobre estrutura e ferragens.</div></div>
  </div>

  <div class="notaS"><b>Incluso no nosso fornecimento:</b> as portas em vidro
  espelhado bronze com o puxador em perfil metálico, o vidro leitoso de
  escrever, a fita de LED e o perfil de alumínio — todos entregues
  instalados.<br>
  <b>Não inclusos:</b> mármore e demais pedras, cervejeira e
  eletrodomésticos, elétrica e luminotécnica, alvenaria, pintura, gesso,
  persianas, tapetes, estofados e os restauros de mobiliário existente.</div>

  {foot(4)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600;700&family=DM+Sans:wght@300;400;500;700&display=swap" '
        'rel="stylesheet"><style>' + CSS + '</style></head><body>'
        + p1 + p2 + p3 + p4 + '</body></html>')

(P/'proposta-suzi-guilherme.html').write_text(HTML, encoding='utf-8')
tmp = HTML.replace('src="img-suzi-guilherme/', f'src="file://{P}/img-suzi-guilherme/')
open('/tmp/in.html', 'w', encoding='utf-8').write(tmp)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-suzi-guilherme.pdf')],
               check=True, env=env)
print(f'proposta-suzi-guilherme.pdf · {NP} páginas')
print(f'  item a item          R$ {br(sg.TOT):>9}')
print(f'  fechamento completo  R$ {br(sg.TOT_FECH):>9}  (−{int(sg.DESC_FECH*100)}%)')
assert abs(sum(sg.PV_IT.values()) - sg.TOT) < 1
print('  soma confere com o total')
