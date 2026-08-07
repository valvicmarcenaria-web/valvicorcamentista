# -*- coding: utf-8 -*-
# Proposta — Armário superior de cozinha (3,02 m). 3 páginas.
# Números vêm de corte-armario-superior-cozinha.py:
#   marcenaria R$ 10.550 · LED R$ 2.500 · total R$ 13.050 (MC 35%, sem RT)
import pathlib
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')

# ── elevação frontal ────────────────────────────────────────────────────────
# X(c) = 34 + c*1.9   ·   Y(h) = 34 + (260-h)*1.9
ELEV = """
<svg viewBox="0 0 640 304" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
  <defs>
    <pattern id="gl" width="7" height="7" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="7" stroke="#C3CDD2" stroke-width="1"/>
    </pattern>
  </defs>

  <!-- cota geral -->
  <text x="320" y="12" text-anchor="middle" font-size="11" font-weight="700"
        fill="#8A6B45" letter-spacing="1.5">3,02 m</text>
  <line x1="34" y1="20" x2="607.8" y2="20" stroke="#9C9587" stroke-width=".8"/>
  <line x1="34" y1="16" x2="34" y2="24" stroke="#9C9587" stroke-width=".8"/>
  <line x1="607.8" y1="16" x2="607.8" y2="24" stroke="#9C9587" stroke-width=".8"/>

  <!-- teto -->
  <line x1="18" y1="34" x2="626" y2="34" stroke="#211E1A" stroke-width="2.4"/>

  <!-- corpos -->
  <rect x="34" y="34" width="437" height="95" fill="#EFE7DA" stroke="#211E1A" stroke-width="1.8"/>
  <rect x="471" y="34" width="136.8" height="133" fill="#EFE7DA" stroke="#211E1A" stroke-width="1.8"/>
  <rect x="34" y="129" width="437" height="114" fill="#F9F6F1" stroke="#211E1A" stroke-width="1.8"/>

  <!-- divisórias de módulo -->
  <line x1="170.8" y1="34" x2="170.8" y2="243" stroke="#211E1A" stroke-width="1.8"/>
  <line x1="328.5" y1="34" x2="328.5" y2="243" stroke="#211E1A" stroke-width="1.8"/>

  <!-- juntas de porta -->
  <g stroke="#211E1A" stroke-width=".9" opacity=".55">
    <line x1="102.4" y1="34" x2="102.4" y2="129"/>
    <line x1="249.7" y1="34" x2="249.7" y2="129"/>
    <line x1="399.8" y1="34" x2="399.8" y2="129"/>
    <line x1="539.4" y1="34" x2="539.4" y2="167"/>
    <line x1="102.4" y1="129" x2="102.4" y2="243"/>
    <line x1="249.7" y1="129" x2="249.7" y2="214.5"/>
  </g>

  <!-- cristaleira: vidro + 2 prateleiras -->
  <rect x="35" y="130" width="134.8" height="112" fill="url(#gl)" opacity=".85"/>
  <rect x="35" y="130" width="134.8" height="112" fill="none" stroke="#6B8391" stroke-width="1.1"/>
  <line x1="35" y1="167" x2="169.8" y2="167" stroke="#6B8391" stroke-width="1.2"/>
  <line x1="35" y1="205" x2="169.8" y2="205" stroke="#6B8391" stroke-width="1.2"/>

  <!-- vão da coifa -->
  <rect x="171.7" y="214.5" width="156" height="28.5" fill="#fff" stroke="#211E1A" stroke-width=".9"/>
  <rect x="185" y="222" width="130" height="10" rx="2.5" fill="#B9B4AA"/>
  <text x="249.7" y="238.5" text-anchor="middle" font-size="7" fill="#9C9587">coifa · do cliente</text>

  <!-- nicho do micro -->
  <line x1="328.5" y1="176.5" x2="471" y2="176.5" stroke="#211E1A" stroke-width="1.8"/>
  <rect x="329.5" y="177.5" width="140.5" height="64.5" fill="#fff"/>
  <rect x="343" y="188" width="113" height="44" rx="3" fill="#EDEAE3" stroke="#9C9587" stroke-width="1"/>
  <line x1="428" y1="188" x2="428" y2="232" stroke="#9C9587" stroke-width=".8"/>
  <text x="399.8" y="171" text-anchor="middle" font-size="7" fill="#6B6559">báscula</text>

  <!-- geladeira do cliente (fora do escopo) -->
  <rect x="478" y="167" width="122" height="83" fill="none" stroke="#9C9587"
        stroke-width="1" stroke-dasharray="4 3"/>
  <text x="539" y="212" text-anchor="middle" font-size="7.4" fill="#9C9587">geladeira · do cliente</text>

  <!-- LED -->
  <g stroke="#C79A4E" stroke-width="3" stroke-linecap="round">
    <line x1="37" y1="132" x2="468" y2="132"/>
    <line x1="37" y1="246" x2="468" y2="246"/>
    <line x1="39" y1="170" x2="166" y2="170"/>
    <line x1="39" y1="208" x2="166" y2="208"/>
  </g>

  <!-- cotas de altura -->
  <g stroke="#9C9587" stroke-width=".8" fill="none">
    <line x1="20" y1="34" x2="20" y2="129"/><line x1="16" y1="34" x2="24" y2="34"/>
    <line x1="16" y1="129" x2="24" y2="129"/>
    <line x1="20" y1="129" x2="20" y2="243"/><line x1="16" y1="243" x2="24" y2="243"/>
    <line x1="622" y1="34" x2="622" y2="167"/><line x1="618" y1="34" x2="626" y2="34"/>
    <line x1="618" y1="167" x2="626" y2="167"/>
  </g>
  <text x="13" y="84" text-anchor="middle" font-size="8.5" fill="#6B6559"
        transform="rotate(-90 13 84)">50</text>
  <text x="13" y="188" text-anchor="middle" font-size="8.5" fill="#6B6559"
        transform="rotate(-90 13 188)">60</text>
  <text x="631" y="102" text-anchor="middle" font-size="8.5" fill="#6B6559"
        transform="rotate(-90 631 102)">70</text>


  <!-- rodapé de módulos -->
  <g stroke="#E4DFD3" stroke-width="1">
    <line x1="34" y1="256" x2="170.8" y2="256"/>
    <line x1="170.8" y1="256" x2="328.5" y2="256"/>
    <line x1="328.5" y1="256" x2="471" y2="256"/>
    <line x1="471" y1="256" x2="607.8" y2="256"/>
  </g>
  <g font-size="8.4" text-anchor="middle" fill="#211E1A" font-weight="600">
    <text x="102.4" y="268">Cristaleira</text>
    <text x="249.7" y="268">Vão da coifa</text>
    <text x="399.8" y="268">Micro-ondas</text>
    <text x="539.4" y="268">Geladeira</text>
  </g>
  <g font-size="7.4" text-anchor="middle" fill="#9C9587">
    <text x="102.4" y="278">72 cm</text>
    <text x="249.7" y="278">83 cm</text>
    <text x="399.8" y="278">75 cm</text>
    <text x="539.4" y="278">72 cm</text>
  </g>

  <!-- legenda -->
  <g font-size="7.8" fill="#6B6559">
    <rect x="34" y="292" width="11" height="9" fill="#EFE7DA" stroke="#211E1A" stroke-width=".8"/>
    <text x="50" y="299.5">profundidade 50 cm</text>
    <rect x="180" y="292" width="11" height="9" fill="#F9F6F1" stroke="#211E1A" stroke-width=".8"/>
    <text x="196" y="299.5">profundidade 35 cm</text>
    <line x1="326" y1="296.5" x2="341" y2="296.5" stroke="#C79A4E" stroke-width="3" stroke-linecap="round"/>
    <text x="346" y="299.5">fita de LED</text>
    <rect x="430" y="292" width="11" height="9" fill="#E2E9EC" stroke="#6B8391" stroke-width=".8"/>
    <text x="446" y="299.5">vidro com perfil de alumínio</text>
  </g>
</svg>"""

# ── corte lateral: os dois planos ───────────────────────────────────────────
SEC = """
<svg viewBox="0 0 132 150" xmlns="http://www.w3.org/2000/svg" style="width:34mm;height:auto;">
  <line x1="14" y1="6" x2="14" y2="140" stroke="#211E1A" stroke-width="2"/>
  <line x1="14" y1="8" x2="96" y2="8" stroke="#211E1A" stroke-width="2"/>
  <rect x="14" y="8" width="66" height="50" fill="#EFE7DA" stroke="#211E1A" stroke-width="1.4"/>
  <rect x="14" y="58" width="46" height="60" fill="#F9F6F1" stroke="#211E1A" stroke-width="1.4"/>
  <line x1="17" y1="60.5" x2="58" y2="60.5" stroke="#C79A4E" stroke-width="2.6" stroke-linecap="round"/>
  <line x1="17" y1="120.5" x2="58" y2="120.5" stroke="#C79A4E" stroke-width="2.6" stroke-linecap="round"/>
  <g stroke="#9C9587" stroke-width=".7">
    <line x1="14" y1="130" x2="80" y2="130"/><line x1="14" y1="126" x2="14" y2="134"/>
    <line x1="80" y1="126" x2="80" y2="134"/>
    <line x1="14" y1="142" x2="60" y2="142"/><line x1="60" y1="138" x2="60" y2="146"/>
  </g>
  <text x="47" y="127" text-anchor="middle" font-size="9" font-weight="700" fill="#8A6B45">50</text>
  <text x="37" y="139" text-anchor="middle" font-size="9" font-weight="700" fill="#8A6B45">35</text>
  <text x="99" y="36" font-size="7.6" fill="#6B6559">avança</text>
  <text x="64" y="92" font-size="7.6" fill="#6B6559">recua</text>
</svg>"""

CSS = """
:root{
  --ink:#211E1A; --soft:#6B6559; --mut:#9C9587; --line:#E4DFD3; --paper:#fff;
  --accent:#8A6B45; --accent-soft:#F1EAE0;
}
@page{size:A4;margin:0;}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{margin:0;font-family:'DM Sans','Liberation Sans',Arial,sans-serif;color:var(--ink);
     font-size:10.5pt;line-height:1.55;}
.page{position:relative;width:210mm;height:297mm;padding:20mm 20mm 16mm;
      page-break-after:always;overflow:hidden;background:var(--paper);}
.page:last-of-type{page-break-after:avoid;}
h1,h2,h3{margin:0;font-weight:600;} p{margin:0;}

.hd{display:flex;justify-content:space-between;align-items:flex-start;
    border-bottom:1.5px solid var(--ink);padding-bottom:8mm;margin-bottom:10mm;}
.brand{font-size:15pt;font-weight:700;letter-spacing:.02em;}
.brand .dot{color:var(--accent);}
.brand-sub{font-size:7.6pt;letter-spacing:.3em;color:var(--mut);margin-top:2px;text-transform:uppercase;}
.hd .meta{text-align:right;font-size:8.6pt;color:var(--soft);line-height:1.7;}
.hd .meta b{color:var(--ink);}

.eyebrow{font-size:8pt;letter-spacing:.22em;text-transform:uppercase;color:var(--accent);font-weight:700;}
.h1{font-size:22pt;font-weight:700;line-height:1.15;margin:3mm 0 5mm;letter-spacing:-.01em;}
.lead{font-size:10.3pt;color:var(--soft);max-width:152mm;margin-bottom:8mm;}

.scope{display:flex;gap:8mm;margin-bottom:8mm;}
.scope .it{flex:1;border-top:2px solid var(--ink);padding-top:3.6mm;}
.scope .it .k{font-size:10.4pt;font-weight:700;line-height:1.25;}
.scope .it .d{font-size:8.5pt;color:var(--soft);margin-top:2mm;line-height:1.48;}

.hl-row{display:flex;gap:6mm;}
.hl{flex:1;background:var(--accent-soft);border-radius:7px;padding:5.4mm 6mm;}
.hl .t{font-size:11pt;font-weight:700;margin-bottom:2mm;}
.hl .d{font-size:8.6pt;color:var(--soft);line-height:1.52;}
.hl .d b{color:var(--ink);}
.hl.split{display:flex;gap:5mm;align-items:center;}
.hl.split .txt{flex:1;}

.note{margin-top:4mm;padding-top:2.6mm;border-top:1px solid var(--line);
      font-size:8.3pt;color:var(--soft);line-height:1.52;}
.note b{color:var(--ink);}
.pfoot{position:absolute;left:20mm;right:20mm;bottom:14mm;display:flex;
       justify-content:space-between;font-size:7.6pt;color:var(--mut);
       letter-spacing:.08em;padding-top:3mm;border-top:1px solid var(--line);}

/* p2 — desenho */
.fig{border:1px solid var(--line);border-radius:8px;padding:6mm 7mm 4mm;margin-bottom:5mm;}
.figcap{font-size:8pt;color:var(--mut);margin-top:3mm;padding-top:2.4mm;
        border-top:1px solid var(--line);line-height:1.5;}
.figcap b{color:var(--ink);}
.spec{display:flex;gap:5mm;}
.spec .c{flex:1;border:1px solid var(--line);border-radius:6px;padding:4mm 4.6mm;}
.spec .c .k{font-size:7.4pt;letter-spacing:.15em;text-transform:uppercase;
            color:var(--accent);font-weight:700;margin-bottom:2.4mm;}
.spec .c ul{margin:0;padding:0;list-style:none;}
.spec .c li{font-size:8.4pt;color:var(--soft);line-height:1.45;padding:.9mm 0;
            border-bottom:1px solid var(--line);}
.spec .c li:last-child{border-bottom:none;}
.spec .c li b{color:var(--ink);}

/* p3 — investimento */
.inv-box{border:1.5px solid var(--ink);border-radius:8px;padding:4.6mm 8mm;}
.inv-box .t{font-size:8pt;letter-spacing:.18em;text-transform:uppercase;color:var(--mut);font-weight:700;}
.inv-box .big{font-size:30pt;font-weight:700;margin:2.6mm 0 1mm;}
.inv-box .cap{font-size:9pt;color:var(--soft);}
.comp{margin:3.4mm 0 1mm;padding-top:2.6mm;border-top:1px solid var(--line);}
.comp .r{display:flex;justify-content:space-between;gap:6mm;font-size:8.8pt;
         color:var(--soft);padding:1.3mm 0;}
.comp .r b{color:var(--ink);font-variant-numeric:tabular-nums;white-space:nowrap;}
.comp .r.s{border-top:1px solid var(--line);margin-top:1.4mm;padding-top:2.4mm;}
.comp .r small{opacity:.75;}

.esc{width:100%;border-collapse:collapse;margin-top:2mm;}
.esc td{padding:1.5mm 0;border-bottom:1px solid var(--line);font-size:9pt;color:var(--soft);}
.esc td:last-child{text-align:right;font-weight:700;color:var(--ink);
                   font-variant-numeric:tabular-nums;}
.esc td.dsc{text-align:right;font-size:8.2pt;color:var(--accent);white-space:nowrap;padding-right:5mm;}
.esc tr.best td{color:var(--ink);}
.esc tr.best td:first-child{font-weight:700;}

.incl{margin:4mm 0 3.4mm;}
.incl-t{font-size:7.4pt;letter-spacing:.16em;text-transform:uppercase;color:var(--mut);
        font-weight:700;margin-bottom:2.4mm;}
.incl ul{margin:0;padding:0;list-style:none;}
.incl li{padding:1.0mm 0;border-bottom:1px solid var(--line);font-size:9pt;
         padding-left:5mm;position:relative;}
.incl li::before{content:"";position:absolute;left:0;top:50%;margin-top:-2.5px;
                 width:5px;height:5px;background:var(--accent);}
.terms{display:flex;gap:5mm;margin-top:2mm;}
.term{flex:1;border:1px solid var(--line);border-radius:6px;padding:3.1mm 4.4mm;}
.term .k{font-size:7.4pt;letter-spacing:.14em;text-transform:uppercase;color:var(--mut);font-weight:700;}
.term .v{font-size:11.5pt;font-weight:700;margin-top:2px;}
.term .s{font-size:7.7pt;color:var(--soft);margin-top:.8mm;line-height:1.4;}
"""

HD = """  <div class="hd">
    <div><div class="brand">valvic<span class="dot">.</span></div><div class="brand-sub">MARCENARIA</div></div>
    <div class="meta"><b>Cozinha</b><br>Armário superior · 3,02 m<br>7 de agosto de 2026</div>
  </div>"""
FT = ('  <div class="pfoot"><span>valvic. marcenaria</span>'
      '<span>Armário superior · cozinha · 07/08/2026</span></div>')

HTML = f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head>
<body>

<!-- PÁGINA 1 -->
<div class="page">
{HD}
  <div class="eyebrow">Proposta técnica</div>
  <div class="h1">Armário superior<br>para a cozinha.</div>
  <p class="lead">Os <b>3,02 m</b> da parede resolvidos em <b>dois planos de profundidade</b>:
  um corpo de 50 cm que corre a parede inteira por cima, e um corpo de 35 cm no plano de
  trabalho — que libera a bancada e recua onde a geladeira entra.</p>

  <div class="scope">
    <div class="it">
      <div class="k">Corpo superior<br>230 × 50 cm</div>
      <div class="d">Seis portas em três módulos, com prateleira interna. É o volume de guarda
      do conjunto — profundidade cheia onde o alcance não atrapalha.</div>
    </div>
    <div class="it">
      <div class="k">Módulo da<br>geladeira · 72 cm</div>
      <div class="d">Duas portas, 70 cm de altura, na mesma profundidade de 50. Fecha o vão
      acima do eletrodoméstico e alinha o topo com o resto da parede.</div>
    </div>
    <div class="it">
      <div class="k">Cristaleira<br>72 cm</div>
      <div class="d">Duas portas de vidro com perfil de alumínio e <b>duas prateleiras</b>,
      com <b>LED interno</b> banhando cada nível.</div>
    </div>
    <div class="it">
      <div class="k">Coifa e<br>micro-ondas</div>
      <div class="d">Vão de <b>83 cm</b> preparado para a coifa, com duas portas acima; e nicho
      de <b>75 cm</b> para o micro, com báscula em pistão a gás por cima.</div>
    </div>
  </div>

  <div class="hl-row">
    <div class="hl split">
      <div class="txt">
        <div class="t">Dois planos, uma razão</div>
        <div class="d">O corpo de cima <b>avança para 50 cm</b> porque ali o alcance já é de
        escada — profundidade vira volume de guarda sem custo de uso. O de baixo <b>recua para
        35 cm</b> porque é altura de cabeça e de trabalho: libera a bancada, não esbarra em quem
        cozinha e deixa a luz chegar no plano de apoio.</div>
      </div>
      {SEC}
    </div>
  </div>

  <div class="hl-row" style="margin-top:5mm;">
    <div class="hl">
      <div class="t">Puxador passante</div>
      <div class="d">Perfil embutido em <b>usinagem passante</b>, correndo a linha inteira de
      cada módulo. Não é peça aplicada: o puxador <b>faz parte da porta</b>, some na frontal e
      dá um risco horizontal contínuo em vez de doze peças soltas na fachada.</div>
    </div>
    <div class="hl">
      <div class="t">Branco por dentro, cor por fora</div>
      <div class="d">A caixaria vai em <b>branco</b> — o interior fica claro, a busca é mais
      fácil e o LED rende mais. As <b>portas, tamponamentos e testeiras</b> vão na cor
      escolhida. É onde a cor aparece, e onde ela custa.</div>
    </div>
  </div>

  <div class="note">
    <b>Não incluso:</b> coifa, micro-ondas, geladeira e demais eletrodomésticos; pontos
    elétricos e hidráulicos; bancada e revestimento. <b>Medidas a confirmar no local</b> antes
    da liberação do corte.
  </div>
{FT}
</div>

<!-- PÁGINA 2 -->
<div class="page">
{HD}
  <div class="eyebrow">O desenho</div>
  <div class="h1" style="font-size:19pt;margin-bottom:6mm;">Elevação frontal.</div>

  <div class="fig">
    {ELEV}
    <div class="figcap"><b>Vista de frente, da parede de 3,02 m.</b> Em tom mais escuro o plano
    de 50 cm, que corre do teto e passa por cima da geladeira; em tom claro o plano de 35 cm,
    que para onde a geladeira começa. As linhas douradas são as <b>fitas de LED</b>. Cotas em
    centímetros — <b>a confirmar na medição final</b>.</div>
  </div>

  <div class="spec">
    <div class="c">
      <div class="k">Estrutura</div>
      <ul>
        <li>Caixaria em <b>15 mm</b></li>
        <li>Prateleiras em <b>18 mm</b> — não fletem no vão</li>
        <li>Fundos em <b>6 mm</b></li>
        <li>Portas e acabamentos em <b>18 mm</b></li>
        <li>Fita de borda em <b>todas</b> as faces aparentes</li>
      </ul>
    </div>
    <div class="c">
      <div class="k">Acabamento</div>
      <ul>
        <li>Interno em <b>branco</b></li>
        <li>Externo <b>na cor escolhida</b></li>
        <li>Portas de vidro com <b>perfil de alumínio</b></li>
        <li><b>Puxador passante</b> em perfil, usinado</li>
        <li>Tamponamento lateral na cor</li>
      </ul>
    </div>
    <div class="c">
      <div class="k">Ferragens</div>
      <ul>
        <li><b>22 dobradiças</b> com amortecimento</li>
        <li>Dobradiça específica para a porta de alumínio</li>
        <li><b>Pistão a gás</b> na báscula do micro</li>
        <li>Suportes metálicos de prateleira</li>
        <li>Linha <b>Hardt</b></li>
      </ul>
    </div>
  </div>

  <div class="note">
    A cristaleira leva <b>vidro com perfil de alumínio</b> nas duas folhas. É o item mais caro
    da lista de ferragens — se a preferência for por portas cegas na cor, o conjunto fica
    <b>R$ 1.300 mais barato</b>, e a decisão pode ser tomada até a liberação do corte.
  </div>
{FT}
</div>

<!-- PÁGINA 3 -->
<div class="page">
{HD}
  <div class="eyebrow">Investimento</div>
  <div class="h1" style="font-size:18pt;margin-bottom:4mm;">Marcenaria e iluminação,<br>em linhas separadas.</div>

  <div class="inv-box">
    <div class="t">Investimento total</div>
    <div class="big">R$ 13.050</div>
    <div class="cap">Entrada de 30% + saldo em até 10× no cartão</div>
    <div class="comp">
      <div class="r"><span>Marcenaria — 5 módulos, 3,02 m de parede</span><b>R$ 10.550</b></div>
      <div class="r"><span>Iluminação LED — 7 m de fita com perfil, 2 fontes e sensor</span><b>R$ 2.500</b></div>
    </div>
  </div>

  <div class="note" style="margin-top:4mm;">
    <b>Por que o LED aparece sozinho.</b> São <b>7 m</b> de fita com perfil e difusor — 2,30 m
    sob cada corpo e 2,10 m dentro da cristaleira — mais duas fontes e o sensor. É a única
    linha que pode ser reduzida ou adiada <b>sem mexer na marcenaria</b>. Sem o trecho da
    cristaleira, cai para <b>R$ 1.900</b>.
  </div>

  <table class="esc">
    <tr><td>Entrada de 30% + até 10× no cartão</td><td class="dsc">—</td><td>R$ 13.050</td></tr>
    <tr><td>Entrada de 50% + até 8× no cartão</td><td class="dsc">−3%</td><td>R$ 12.650</td></tr>
    <tr><td>Entrada de 70% + até 6× no cartão</td><td class="dsc">−5%</td><td>R$ 12.400</td></tr>
    <tr class="best"><td>Entrada de 70% + saldo em transferência</td><td class="dsc">−7%</td><td>R$ 12.150</td></tr>
  </table>

  <div class="incl">
    <div class="incl-t">O que está incluso</div>
    <ul>
      <li><b>Corpo superior</b> 230 × 50 cm — 6 portas, 3 prateleiras · <b>módulo da geladeira</b> 72 × 70 cm — 2 portas</li>
      <li><b>Cristaleira</b> 72 cm — 2 portas de vidro com perfil de alumínio, 2 prateleiras</li>
      <li><b>Vão da coifa</b> 83 cm — 2 portas · <b>nicho do micro</b> 75 cm — báscula com pistão a gás</li>
      <li><b>Puxador passante</b> em perfil usinado em toda a frontal</li>
      <li>Interno em branco · externo na cor · fita de borda em todas as faces aparentes</li>
      <li>Ferragens Hardt com amortecimento · projeto, entrega e instalação pela equipe Valvic</li>
    </ul>
  </div>

  <div class="terms">
    <div class="term"><div class="k">Prazo</div><div class="v">45 dias</div>
      <div class="s">Corridos, após aprovação e medição</div></div>
    <div class="term"><div class="k">Garantia</div><div class="v">10 anos</div>
      <div class="s">Estrutura e ferragens · visita em 3 dias úteis</div></div>
    <div class="term"><div class="k">Validade</div><div class="v">7 dias</div>
      <div class="s">Chapa e ferragem sujeitas a reajuste</div></div>
  </div>

{FT}
</div>

</body></html>"""

(P/'proposta-armario-superior-cozinha.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-armario-superior-cozinha.html', len(HTML))
