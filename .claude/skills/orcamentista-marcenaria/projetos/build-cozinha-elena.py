# -*- coding: utf-8 -*-
# Proposta — Cozinha (consultoria Rizzi Interiores). 4 páginas.
# corte-cozinha-elena.py: custo direto R$ 15.721,49 · MC 30% · COM RT · Hardt
#   bancada inferior R$ 13.300 · demais móveis R$ 24.800 · total R$ 38.100
# A escada vai só até −3% (28,7%): a −5% e −7% a MC fura o piso de 28% da casa.
import pathlib
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')

AZ, FR, CZ, GRA = '#5D7480', '#B08856', '#E4E0D8', '#CFCCC5'

# ── elevação desdobrada · X(c)=25+c*1.45 · Y(h)=30+(270-h)*1.45 ──────────────
def X(c): return 25 + c*1.45
def Y(h): return 30 + (270-h)*1.45

def rect(x1, h1, x2, h2, fill, sw=1.6, stroke='#211E1A', extra=''):
    return (f'<rect x="{X(x1):.1f}" y="{Y(h2):.1f}" width="{(x2-x1)*1.45:.1f}" '
            f'height="{(h2-h1)*1.45:.1f}" fill="{fill}" stroke="{stroke}" '
            f'stroke-width="{sw}"{extra}/>')
def vline(c, h1, h2, sw=.9, op=.5):
    return (f'<line x1="{X(c):.1f}" y1="{Y(h2):.1f}" x2="{X(c):.1f}" y2="{Y(h1):.1f}" '
            f'stroke="#211E1A" stroke-width="{sw}" opacity="{op}"/>')
def hline(c1, c2, h, sw=.9, op=.5):
    return (f'<line x1="{X(c1):.1f}" y1="{Y(h):.1f}" x2="{X(c2):.1f}" y2="{Y(h):.1f}" '
            f'stroke="#211E1A" stroke-width="{sw}" opacity="{op}"/>')

E = ['<svg viewBox="0 0 880 492" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">']
# LEITURA CORRIGIDA: os tres volumes de 150 (bancada B, nicho freijo, aereo azul)
# sao a MESMA pilha, na parede 2. A parede 1 tem so a bancada A e a janela.
#   parede 1: bancada A 272 (+60 de canto = 332 da planta)
#   parede 2: bancada B 150 + torre 70 + geladeira 80 = 300 da planta
E.append(f'<line x1="14" y1="{Y(270):.1f}" x2="866" y2="{Y(270):.1f}" stroke="#211E1A" stroke-width="2.4"/>')
E.append(f'<line x1="14" y1="{Y(0):.1f}" x2="866" y2="{Y(0):.1f}" stroke="#211E1A" stroke-width="2.4"/>')

# ── bancadas: A (0→272, 4 modulos) e B (272→422, 2 modulos) ────────────────
for x1, x2, mods in ((0, 272, (80, 140, 200)), (272, 422, (347,))):
    E.append(rect(x1, 0, x2, 10, '#C9C4BA', 1.2))
    E.append(rect(x1, 10, x2, 87, AZ))
    E.append(rect(x1, 87, x2, 90, GRA, 1.2))
    for m in mods: E.append(vline(m, 10, 87))
E.append(hline(0, 80, 62))                                            # bascula da pia
for h in (36, 62): E.append(hline(80, 200, h))                        # 3 gavetas x 2 modulos
E.append(vline(236, 10, 87, .9, .35))                                 # 2 portas de giro
for h in (29, 48, 67): E.append(hline(272, 347, h))                   # 4 gavetas
E.append(vline(384.5, 10, 87, .9, .35))                               # 2 portas de giro

# ── parede 1: janela sobre a bancada A ─────────────────────────────────────
E.append(rect(18, 95, 168, 205, '#EAF0F3', 1.4, '#8FA6B2'))
E.append(vline(93, 95, 205, 1, .3))
E.append(f'<text x="{X(93):.1f}" y="{Y(146):.1f}" text-anchor="middle" font-size="10" fill="#7D93A0">janela</text>')
E.append(f'<text x="{X(220):.1f}" y="{Y(150):.1f}" text-anchor="middle" font-size="9" fill="#B5AEA0">parede</text>')
E.append(f'<text x="{X(220):.1f}" y="{Y(136):.1f}" text-anchor="middle" font-size="9" fill="#B5AEA0">revestida</text>')

# ── parede 2: nicho freijo + aereo azul, sobre a bancada B ─────────────────
E.append(rect(272, 90, 422, 160, FR))
E.append(f'<line x1="{X(272):.1f}" y1="{Y(125):.1f}" x2="{X(422):.1f}" y2="{Y(125):.1f}" stroke="#8A6A40" stroke-width="1.6"/>')
E.append(rect(272, 160, 422, 200, FR))
for m in (321, 370): E.append(vline(m, 160, 200))
E.append(rect(272, 200, 422, 270, AZ))
for m in (322, 372): E.append(vline(m, 200, 270, .9, .35))

# ── torre quente ───────────────────────────────────────────────────────────
E.append(rect(422, 0, 492, 10, '#C9C4BA', 1.2))
E.append(rect(422, 10, 492, 270, CZ))
for h in (50, 90, 150, 190, 230): E.append(hline(422, 492, h))
E.append(rect(430, 96, 484, 144, '#B9B4AA', 1.1, '#8C877D'))
# ── geladeira do cliente + aereo ───────────────────────────────────────────
E.append(f'<rect x="{X(492):.1f}" y="{Y(190):.1f}" width="{80*1.45:.1f}" height="{190*1.45:.1f}" '
         f'fill="none" stroke="#9C9587" stroke-width="1.2" stroke-dasharray="5 4"/>')
for i, t in enumerate(('geladeira', 'do cliente')):
    E.append(f'<text x="{X(532):.1f}" y="{Y(98-i*14):.1f}" text-anchor="middle" font-size="9.5" fill="#9C9587">{t}</text>')
E.append(rect(492, 200, 572, 270, CZ))
E.append(vline(532, 200, 270, .9, .35))

# ── o canto do "L" ─────────────────────────────────────────────────────────
E.append(f'<line x1="{X(272):.1f}" y1="{Y(270)-16:.1f}" x2="{X(272):.1f}" y2="{Y(0)+16:.1f}" '
         f'stroke="#8A6B45" stroke-width="1.4" stroke-dasharray="6 4"/>')
E.append(f'<text x="{X(272):.1f}" y="{Y(270)-22:.1f}" text-anchor="middle" font-size="9.5" '
         f'font-weight="700" fill="#8A6B45" letter-spacing="1.2">CANTO DO "L"</text>')
for c, t in ((136, 'PAREDE 1 · 332 cm'), (422, 'PAREDE 2 · 300 cm')):
    E.append(f'<text x="{X(c):.1f}" y="{Y(270)-22:.1f}" text-anchor="middle" font-size="9" '
             f'fill="#9C9587" letter-spacing="1">{t}</text>')

# ── cotas de altura ────────────────────────────────────────────────────────
for h1, h2, rot in ((0, 90, '90'), (90, 200, '110'), (200, 270, '70')):
    E.append(f'<line x1="14" y1="{Y(h2):.1f}" x2="14" y2="{Y(h1):.1f}" stroke="#9C9587" stroke-width=".8"/>')
    for h in (h1, h2):
        E.append(f'<line x1="10" y1="{Y(h):.1f}" x2="18" y2="{Y(h):.1f}" stroke="#9C9587" stroke-width=".8"/>')
    ym = (Y(h1)+Y(h2))/2
    E.append(f'<text x="7" y="{ym:.1f}" text-anchor="middle" font-size="9" fill="#6B6559" '
             f'transform="rotate(-90 7 {ym:.1f})">{rot}</text>')

# ── etiquetas de modulo e legenda ──────────────────────────────────────────
E.append(f'<line x1="{X(0):.1f}" y1="{Y(0)+10:.1f}" x2="{X(572):.1f}" y2="{Y(0)+10:.1f}" stroke="#E4DFD3" stroke-width="1"/>')
for c, t, w in ((136,'Pia · cooktop · janela','272'), (347,'Bancada · nicho · aéreo','150'),
                (457,'Torre quente','70'), (532,'Geladeira','80')):
    E.append(f'<text x="{X(c):.1f}" y="{Y(0)+26:.1f}" text-anchor="middle" font-size="10" '
             f'font-weight="600" fill="#211E1A">{t}</text>')
    E.append(f'<text x="{X(c):.1f}" y="{Y(0)+38:.1f}" text-anchor="middle" font-size="8.8" fill="#9C9587">{w} cm</text>')
for x, cor, t in ((25, AZ,'Azul Ardósia'), (215, FR,'Freijó'), (350, CZ,'Cinza Urban'),
                  (510, GRA,'Granito Itaúnas · do cliente')):
    E.append(f'<rect x="{x}" y="{Y(0)+50:.1f}" width="13" height="10" fill="{cor}" stroke="#211E1A" stroke-width=".8"/>')
    E.append(f'<text x="{x+19}" y="{Y(0)+58.5:.1f}" font-size="9.2" fill="#6B6559">{t}</text>')
E.append('</svg>')
ELEV = '\n  '.join(E)

CSS = """
:root{--ink:#211E1A;--soft:#6B6559;--mut:#9C9587;--line:#E4DFD3;--paper:#fff;
      --accent:#8A6B45;--accent-soft:#F1EAE0;}
@page{size:A4;margin:0;}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{margin:0;font-family:'DM Sans','Liberation Sans',Arial,sans-serif;color:var(--ink);
     font-size:10.5pt;line-height:1.55;}
.page{position:relative;width:210mm;height:297mm;padding:20mm 20mm 16mm;
      page-break-after:always;overflow:hidden;background:var(--paper);}
.page:last-of-type{page-break-after:avoid;}
h1,h2,h3{margin:0;font-weight:600;} p{margin:0;}
.hd{display:flex;justify-content:space-between;align-items:flex-start;
    border-bottom:1.5px solid var(--ink);padding-bottom:7mm;margin-bottom:9mm;}
.brand{font-size:15pt;font-weight:700;letter-spacing:.02em;}
.brand .dot{color:var(--accent);}
.brand-sub{font-size:7.6pt;letter-spacing:.3em;color:var(--mut);margin-top:2px;text-transform:uppercase;}
.hd .meta{text-align:right;font-size:8.6pt;color:var(--soft);line-height:1.7;}
.hd .meta b{color:var(--ink);}
.eyebrow{font-size:8pt;letter-spacing:.22em;text-transform:uppercase;color:var(--accent);font-weight:700;}
.h1{font-size:22pt;font-weight:700;line-height:1.15;margin:3mm 0 5mm;letter-spacing:-.01em;}
.lead{font-size:10.3pt;color:var(--soft);max-width:152mm;margin-bottom:7mm;}
.scope{display:flex;gap:7mm;margin-bottom:7mm;}
.scope .it{flex:1;border-top:2px solid var(--ink);padding-top:3.4mm;}
.scope .it .k{font-size:10.2pt;font-weight:700;line-height:1.25;}
.scope .it .d{font-size:8.4pt;color:var(--soft);margin-top:2mm;line-height:1.46;}
.hl-row{display:flex;gap:6mm;}
.hl{flex:1;background:var(--accent-soft);border-radius:7px;padding:5mm 5.6mm;}
.hl .t{font-size:11pt;font-weight:700;margin-bottom:2mm;}
.hl .d{font-size:8.5pt;color:var(--soft);line-height:1.5;}
.hl .d b{color:var(--ink);}
.note{margin-top:4mm;padding-top:2.6mm;border-top:1px solid var(--line);
      font-size:8.3pt;color:var(--soft);line-height:1.5;}
.note b{color:var(--ink);}
.pfoot{position:absolute;left:20mm;right:20mm;bottom:14mm;display:flex;
       justify-content:space-between;font-size:7.6pt;color:var(--mut);
       letter-spacing:.08em;padding-top:3mm;border-top:1px solid var(--line);}
.fig{border:1px solid var(--line);border-radius:8px;padding:6mm 7mm 4mm;}
.figcap{font-size:8pt;color:var(--mut);margin-top:3mm;padding-top:2.4mm;
        border-top:1px solid var(--line);line-height:1.5;}
.figcap b{color:var(--ink);}
.mv{width:100%;border-collapse:collapse;margin-top:1mm;}
.mv th{text-align:left;font-size:7.4pt;letter-spacing:.14em;text-transform:uppercase;
       color:var(--mut);font-weight:700;padding:0 0 2mm;border-bottom:1.5px solid var(--ink);}
.mv th.r,.mv td.r{text-align:right;}
.mv td{font-size:8.8pt;padding:1.9mm 0;border-bottom:1px solid var(--line);color:var(--soft);}
.mv td:first-child{color:var(--ink);font-weight:600;}
.mv td.r{font-variant-numeric:tabular-nums;white-space:nowrap;}
.spec{display:flex;gap:5mm;margin-top:5mm;}
.spec .c{flex:1;border:1px solid var(--line);border-radius:6px;padding:4mm 4.4mm;}
.spec .c .k{font-size:7.4pt;letter-spacing:.15em;text-transform:uppercase;
            color:var(--accent);font-weight:700;margin-bottom:2.4mm;}
.spec .c ul{margin:0;padding:0;list-style:none;}
.spec .c li{font-size:8.3pt;color:var(--soft);line-height:1.42;padding:.9mm 0;
            border-bottom:1px solid var(--line);}
.spec .c li:last-child{border-bottom:none;}
.spec .c li b{color:var(--ink);}
.inv-box{border:1.5px solid var(--ink);border-radius:8px;padding:5mm 8mm;}
.inv-box .t{font-size:8pt;letter-spacing:.18em;text-transform:uppercase;color:var(--mut);font-weight:700;}
.inv-box .big{font-size:30pt;font-weight:700;margin:2.6mm 0 1mm;}
.inv-box .cap{font-size:9pt;color:var(--soft);}
.comp{margin:3.4mm 0 1mm;padding-top:2.6mm;border-top:1px solid var(--line);}
.comp .r{display:flex;justify-content:space-between;gap:6mm;font-size:8.8pt;
         color:var(--soft);padding:1.3mm 0;}
.comp .r b{color:var(--ink);font-variant-numeric:tabular-nums;white-space:nowrap;}
.esc{width:100%;border-collapse:collapse;margin-top:3mm;}
.esc td{padding:1.9mm 0;border-bottom:1px solid var(--line);font-size:9pt;color:var(--soft);}
.esc td:last-child{text-align:right;font-weight:700;color:var(--ink);font-variant-numeric:tabular-nums;}
.esc td.dsc{text-align:right;font-size:8.2pt;color:var(--accent);white-space:nowrap;padding-right:5mm;}
.terms{display:flex;gap:5mm;margin-top:4mm;}
.term{flex:1;border:1px solid var(--line);border-radius:6px;padding:3.2mm 4.2mm;}
.term .k{font-size:7.4pt;letter-spacing:.14em;text-transform:uppercase;color:var(--mut);font-weight:700;}
.term .v{font-size:11.5pt;font-weight:700;margin-top:2px;}
.term .s{font-size:7.7pt;color:var(--soft);margin-top:.8mm;line-height:1.4;}
.warn{background:var(--accent-soft);border-radius:7px;padding:4.4mm 5.6mm;margin-top:4mm;}
.warn .k{font-size:7.4pt;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);
         font-weight:700;margin-bottom:1.8mm;}
.warn .d{font-size:8.6pt;color:var(--soft);line-height:1.5;}
.warn .d b{color:var(--ink);}
"""

HD = """  <div class="hd">
    <div><div class="brand">valvic<span class="dot">.</span></div><div class="brand-sub">MARCENARIA</div></div>
    <div class="meta"><b>Cozinha</b><br>Projeto Rizzi Interiores<br>7 de agosto de 2026</div>
  </div>"""
FT = ('  <div class="pfoot"><span>valvic. marcenaria</span>'
      '<span>Cozinha · projeto Rizzi Interiores · 07/08/2026</span></div>')

HTML = f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head>
<body>

<!-- 1 -->
<div class="page">
{HD}
  <div class="eyebrow">Proposta técnica</div>
  <div class="h1">Sua cozinha,<br>executada.</div>
  <p class="lead">A marcenaria dos <b>nove móveis</b> do projeto da Rizzi Interiores — as três
  cores, a torre quente do piso ao teto, o nicho em freijó e o painel ripado. Executada
  exatamente como o projeto define, com a medição final feita por nós antes do corte.</p>

  <div class="scope">
    <div class="it">
      <div class="k">O "L" da bancada<br>272 + 150 cm</div>
      <div class="d">Dois corpos em <b>Azul Ardósia</b> fechando o "L", com portas de giro e
      gavetas em cava. <b>11 gavetas</b> em corrediça oculta com amortecimento.</div>
    </div>
    <div class="it">
      <div class="k">O bloco em freijó<br>150 cm</div>
      <div class="d">Nicho de <b>110 cm</b> com prateleira, e acima dele <b>três básculas</b>
      de 49 cm — o único volume a <b>45 cm</b> de profundidade, na altura de trabalho.</div>
    </div>
    <div class="it">
      <div class="k">Torre quente<br>270 cm, piso ao teto</div>
      <div class="d">Em <b>Cinza Urban</b>, com duas básculas, gavetas, vãos para os embutidos
      e <b>tomadas embutidas na lateral esquerda</b>, como o projeto pede.</div>
    </div>
    <div class="it">
      <div class="k">Painel ripado<br>e mesa</div>
      <div class="d">Em <b>freijó</b>, integrando a cozinha à sala de jantar. A mesa apoiada
      na lateral esquerda, conforme o projeto.</div>
    </div>
  </div>

  <div class="hl-row">
    <div class="hl">
      <div class="t">Três cores nunca dividem chapa</div>
      <div class="d">Azul Ardósia, Freijó e Cinza Urban são <b>compradas e cortadas em
      separado</b> — cada cor tem seu plano de corte. É o que garante que o tom de uma porta
      seja o mesmo da porta ao lado, e é por isso que um projeto tricolor não custa o mesmo
      que um monocromático.</div>
    </div>
    <div class="hl">
      <div class="t">Branco por dentro, cor por fora</div>
      <div class="d">Toda a caixaria interna vai em <b>branco</b>: o interior fica claro e a
      busca é mais fácil. As <b>frentes, tamponamentos e o nicho</b> vão nas cores do projeto —
      é onde a cor aparece e onde ela é cobrada.</div>
    </div>
  </div>

  <div class="note">
    <b>A medição no local vem antes do corte.</b> O documento de consultoria informa que suas
    cotas foram tiradas de planta baixa e <b>não servem como referência para compra final</b>.
    Nossa medição confirma cada vão antes de qualquer chapa ser cortada — e é parte do que
    está incluso aqui.
  </div>
{FT}
</div>

<!-- 2 -->
<div class="page">
{HD}
  <div class="eyebrow">O desenho</div>
  <div class="h1" style="font-size:19pt;margin-bottom:5mm;">Elevação desdobrada.</div>

  <div class="fig">
  {ELEV}
    <div class="figcap"><b>As duas paredes abertas em uma só vista</b>, como no documento do
    projeto. À esquerda do traço dourado, a parede da janela (332 cm); à direita, a parede da
    torre e da geladeira (300 cm). Cotas em centímetros, <b>a confirmar na medição final</b>.</div>
  </div>

  <div class="note">
    <b>Como as alturas se encaixam.</b> O armário de bancada tem 77 cm; somados ao sóculo
    recuado de 10 e ao granito de 3, a bancada fica exatamente nos <b>90 cm</b> que o projeto
    pede. Daí sobem os 110 cm do nicho em freijó e os 70 do aéreo — fechando os <b>270 cm</b>
    de pé-direito, a mesma altura da torre quente. As três colunas do projeto fecham no mesmo
    número, e é isso que permite orçar com esta precisão antes da medição.
  </div>

  <div class="spec" style="margin-top:6mm;">
    <div class="c">
      <div class="k">A medição confirma</div>
      <ul>
        <li>Pé-direito real e nível do piso</li>
        <li>Largura exata das duas paredes</li>
        <li>Esquadro do canto do "L"</li>
        <li>Vão livre da janela</li>
      </ul>
    </div>
    <div class="c">
      <div class="k">E também</div>
      <ul>
        <li>Posição de tomadas e interruptores</li>
        <li>Ponto de água, gás e esgoto</li>
        <li>Vão real da geladeira</li>
        <li>Medidas dos embutidos escolhidos</li>
      </ul>
    </div>
    <div class="c">
      <div class="k">Por que importa</div>
      <ul>
        <li>Cada cor tem <b>plano de corte próprio</b></li>
        <li>Chapa cortada não volta atrás</li>
        <li>Ajuste na medição custa <b>zero</b></li>
        <li>Ajuste depois do corte custa chapa</li>
      </ul>
    </div>
  </div>
{FT}
</div>

<!-- 3 -->
<div class="page">
{HD}
  <div class="eyebrow">Especificação</div>
  <div class="h1" style="font-size:19pt;margin-bottom:5mm;">Os nove móveis.</div>

  <table class="mv">
    <tr><th>Móvel</th><th>Altura × Largura × Profundidade</th><th class="r">Cor</th></tr>
    <tr><td>Armário de bancada</td><td>77 × 272 × 60 cm — portas de giro e gavetas em cava</td><td class="r">Azul Ardósia</td></tr>
    <tr><td>Armário de bancada</td><td>77 × 150 × 60 cm — completa o "L"</td><td class="r">Azul Ardósia</td></tr>
    <tr><td>Nicho</td><td>110 × 150 cm — com prateleira</td><td class="r">Freijó</td></tr>
    <tr><td>Aéreo de básculas</td><td>40 × 147 × 45 cm — três básculas em cava</td><td class="r">Freijó</td></tr>
    <tr><td>Aéreo</td><td>70 × 150 × 60 cm — três portas de giro em cava</td><td class="r">Azul Ardósia</td></tr>
    <tr><td>Torre quente</td><td>270 × 70 × 60 cm — básculas, gavetas e tomadas embutidas</td><td class="r">Cinza Urban</td></tr>
    <tr><td>Aéreo da geladeira</td><td>70 × 80 × 60 cm — duas portas de giro em cava</td><td class="r">Cinza Urban</td></tr>
    <tr><td>Painel ripado</td><td>integrando a cozinha à sala de jantar</td><td class="r">Freijó</td></tr>
    <tr><td>Mesa</td><td>com apoio na lateral esquerda</td><td class="r">Freijó</td></tr>
  </table>

  <div class="spec">
    <div class="c">
      <div class="k">Estrutura</div>
      <ul>
        <li>Caixaria em <b>15 mm</b></li>
        <li>Prateleiras em <b>18 mm</b></li>
        <li>Fundos em <b>6 mm</b></li>
        <li>Frentes e acabamentos em <b>18 mm</b></li>
        <li>Fita de borda em <b>todas</b> as faces aparentes</li>
      </ul>
    </div>
    <div class="c">
      <div class="k">Ferragens</div>
      <ul>
        <li><b>18 dobradiças</b> com amortecimento</li>
        <li><b>14 corrediças ocultas</b> com amortecimento</li>
        <li><b>5 articuladores</b> de báscula</li>
        <li>Suportes metálicos de prateleira</li>
        <li>Linha <b>Hardt</b></li>
      </ul>
    </div>
    <div class="c">
      <div class="k">Não incluso</div>
      <ul>
        <li>Granito, cuba e misturador</li>
        <li>Porcelanato e revestimentos</li>
        <li>Cooktop, forno, micro e coifa</li>
        <li>Geladeira e purificador</li>
        <li>Luminária, pontos elétricos e gesso</li>
      </ul>
    </div>
  </div>

  <div class="note">
    <b>Cava em todas as frentes.</b> São <b>16,94 m</b> de cava usinada na CNC — o puxador é
    a própria frente, sem peça aplicada. Nas três cores, com o mesmo perfil.
  </div>
{FT}
</div>

<!-- 4 -->
<div class="page">
{HD}
  <div class="eyebrow">Investimento</div>
  <div class="h1" style="font-size:19pt;margin-bottom:5mm;">A cozinha completa.</div>

  <div class="inv-box">
    <div class="t">Investimento total</div>
    <div class="big">R$ 38.100</div>
    <div class="cap">Entrada de 30% + saldo em até 10× no cartão</div>
    <div class="comp">
      <div class="r"><span>Armários inferiores da bancada — 272 + 150 cm, 11 gavetas</span><b>R$ 13.300</b></div>
      <div class="r"><span>Demais móveis — aéreos, nicho, torre quente, painel e mesa</span><b>R$ 24.800</b></div>
    </div>
  </div>

  <table class="esc">
    <tr><td>Entrada de 30% + saldo em até 10× no cartão</td><td class="dsc">—</td><td>R$ 38.100</td></tr>
    <tr><td>Entrada de 50% + saldo em até 8× no cartão</td><td class="dsc">−3%</td><td>R$ 37.000</td></tr>
  </table>

  <div class="warn">
    <div class="k">Os armários da bancada em linha própria</div>
    <div class="d">Eles aparecem separados porque são o maior bloco isolado do projeto e o mais
    fácil de faseiar. <b>Se forem executados depois</b>, o restante da cozinha fica em
    <b>R$ 26.600</b> — e não nos R$ 24.800 acima, porque chapa comprada para o conjunto não
    encolhe na mesma proporção quando o conjunto diminui, e a instalação continua sendo uma
    cozinha inteira.</div>
  </div>

  <div class="terms">
    <div class="term"><div class="k">Prazo</div><div class="v">60 dias</div>
      <div class="s">Corridos, a partir da aprovação e da medição final</div></div>
    <div class="term"><div class="k">Garantia</div><div class="v">10 anos</div>
      <div class="s">Estrutura e ferragens · 2 anos nas corrediças</div></div>
    <div class="term"><div class="k">Validade</div><div class="v">7 dias</div>
      <div class="s">Chapa e ferragem sujeitas a reajuste</div></div>
  </div>

  <div class="note">
    <b>Medição final antes do corte.</b> As medidas desta proposta vêm do documento de
    consultoria, que declara não servir como referência para compra final. Nossa medição no
    local é feita antes da liberação do corte e <b>eventuais ajustes de dimensão são acertados
    ali</b>, com a proposta revisada por escrito antes da produção começar.
  </div>
{FT}
</div>

</body></html>"""

(P/'proposta-cozinha-elena.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-cozinha-elena.html', len(HTML))
