# -*- coding: utf-8 -*-
"""PROPOSTA — Nádia e Maurílio · retomada de negociação  [Jonathan 06/08/2026]

Escopo de `nadia_v3.pdf` ("Proposta especial para Nádia — reduzida versão 2").
Duas colunas de preço: COM ferragens (fornecimento Valvic) e SEM ferragens
(compra por conta da cliente).

⚠️ A linha "Lavanderia superior" vem no PDF com a descrição "Idem lavanderia" e
   a CÉLULA DE VALOR EM BRANCO. Adotei o mesmo valor do térreo (5.850 / 4.800),
   que é a leitura literal de "idem". É o único número que não veio do documento.

Renders: as 3 faixas de imagem da capa do nadia_v3.pdf, recortadas em 8 renders
(258×251 a 419×384 px). São pequenos — por isso a capa é tipográfica e os
renders entram em tamanho contido. O PDF do projeto completo no Drive tem 1 GB
e não é transferível neste ambiente.

Ferragens ilustradas em SVG desenhado, não em foto de catálogo: a política de
rede bloqueia hosts externos, e para explicar MECANISMO o desenho é melhor.
"""
import pathlib, base64
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')
CSS = open('/tmp/css_premium.txt', encoding='utf-8').read().split('CSS = """')[1].rsplit('"""',1)[0]

def uri(n):
    return 'data:image/jpeg;base64,' + base64.b64encode((P/'img'/n).read_bytes()).decode()

CLO1, CLO2 = uri('nadia-closet-1.jpg'), uri('nadia-closet-3.jpg')
COZ1, COZ2, COZ3 = (uri(f'nadia-cozinha-{i}.jpg') for i in (1, 2, 3))
LAV1, LAV2 = uri('nadia-lavanderia-1.jpg'), uri('nadia-lavanderia-2.jpg')

ITENS = [
 ('Lavanderia térreo', '',
  'Estrutura interna e acabamento externo em <b>MDF Areia Guararapes</b> · puxadores '
  'inferiores em cava e superiores passantes · fundo em MDF com <b>duplo revestimento</b>.',
  5850, 4800),
 ('Lavanderia superior', '',
  'Mesma especificação da lavanderia do térreo.', 5850, 4800),
 ('Hall dos dormitórios', '',
  'Estrutura interna e acabamento externo em <b>MDF Areia Guararapes</b> · portas de '
  '<b>espelho prata</b> em esquadria de alumínio bronze.', 6300, 5700),
 ('Cozinha', 'Ilha e geladeiras',
  'Estrutura interna e externa em <b>MDF Areia</b> · puxadores em cava com perfil · '
  '<b>ilha reduzida para 2,80 m</b>.', 15100, 11800),
 ('Cozinha', 'Cristaleira',
  'Cores conforme projeto · <b>3 portas de vidro reflecta bronze</b> em esquadria de '
  'alumínio bronze · prateleiras de vidro incolor temperado de 8 mm · puxadores em cava '
  'com perfil · iluminação de LED instalada · <b>alterada para 80 cm</b> de largura.',
  5650, 4800),
 ('Cozinha', 'Bancada',
  'Armários aéreos e inferiores com estrutura em <b>MDF Areia</b> · cores externas conforme '
  'projeto · armários com <b>básculas em MDF amadeirado</b> interno e externo · puxadores '
  'inferiores em cava com <b>perfil Rometal RM280</b> · puxadores superiores passantes · '
  'básculas com <b>articuladores Blum HK-S</b>.', 52400, 41300),
 ('Cozinha', 'Painel de TV',
  'Painel de TV em <b>MDF Itapuã</b> · iluminação de LED instalada. '
  '<i>Sem ferragem — o valor não muda entre as colunas.</i>', 2250, 2250),
 ('Suíte master', 'Closet versão 2',
  'Estrutura completa em <b>MDF Areia</b> · gavetas com puxadores espaçados · '
  '<b>cabideiros metálicos</b> · removendo a cômoda.', 36700, 31200),
]
TOT_C = sum(i[3] for i in ITENS)
TOT_S = sum(i[4] for i in ITENS)
def br(v): return f'{v:,.0f}'.replace(',', '.')
def br2(v): return f'{v:,.2f}'.replace(',', '·').replace('.', ',').replace('·', '.')

linhas = ''.join(
  f'<tr><td class="sv"><b>{a}</b>{f"<small>{b}</small>" if b else ""}</td>'
  f'<td class="ds">{d}</td>'
  f'<td class="vl">R$ {br(c)}</td><td class="vl alt">R$ {br(s)}</td></tr>'
  for a, b, d, c, s in ITENS)

# ── SVG das ferragens — desenho de mecanismo, não foto de catálogo ───────────
SVG_CORR = """<svg viewBox="0 0 200 108" fill="none" xmlns="http://www.w3.org/2000/svg">
 <rect x="14" y="20" width="172" height="62" rx="2" stroke="#C9A96A" stroke-width="1.5"/>
 <rect x="26" y="30" width="128" height="42" rx="1.5" fill="#EFE7D8" stroke="#3A322A" stroke-width="1.5"/>
 <rect x="26" y="74" width="128" height="5" rx="1" fill="#C9A96A"/>
 <path d="M26 79 H154" stroke="#3A322A" stroke-width="1.2"/>
 <path d="M154 51 h26" stroke="#3A322A" stroke-width="1.2" stroke-dasharray="3 3"/>
 <path d="M172 45 l8 6 -8 6" stroke="#3A322A" stroke-width="1.2"/>
 <text x="26" y="96" font-size="8" fill="#8C7B5E" font-family="system-ui">corrediça oculta, por baixo da gaveta</text>
</svg>"""

SVG_BLUM = """<svg viewBox="0 0 200 108" fill="none" xmlns="http://www.w3.org/2000/svg">
 <path d="M20 86 H186" stroke="#C9A96A" stroke-width="1.5"/>
 <rect x="20" y="60" width="80" height="20" rx="1.5" fill="#EFE7D8" stroke="#3A322A" stroke-width="1.5"/>
 <g opacity=".38">
  <rect x="20" y="60" width="80" height="20" rx="1.5" fill="none" stroke="#3A322A"
        stroke-width="1.2" transform="rotate(-32 22 70)"/>
  <rect x="20" y="60" width="80" height="20" rx="1.5" fill="none" stroke="#3A322A"
        stroke-width="1.2" transform="rotate(-62 22 70)"/>
 </g>
 <path d="M100 70 A 52 52 0 0 0 62 20" stroke="#C9A96A" stroke-width="1.4" stroke-dasharray="4 3"/>
 <circle cx="22" cy="70" r="3.2" fill="#C9A96A"/>
 <text x="112" y="36" font-size="8" fill="#8C7B5E" font-family="system-ui">para em qualquer</text>
 <text x="112" y="47" font-size="8" fill="#8C7B5E" font-family="system-ui">ponto do curso</text>
</svg>"""

SVG_ESTR = """<svg viewBox="0 0 260 132" fill="none" xmlns="http://www.w3.org/2000/svg">
 <rect x="30" y="14" width="9" height="104" fill="#3A322A"/>
 <rect x="196" y="14" width="9" height="104" fill="#3A322A"/>
 <rect x="39" y="14" width="157" height="9" fill="#3A322A"/>
 <rect x="39" y="109" width="157" height="9" fill="#3A322A"/>
 <rect x="39" y="60" width="157" height="11" fill="#C9A96A"/>
 <rect x="205" y="14" width="4" height="104" fill="#B9AC93"/>
 <rect x="213" y="10" width="11" height="112" fill="#6E6250"/>
 <text x="46" y="36" font-size="9" fill="#241E18" font-family="system-ui" font-weight="700">15 mm</text>
 <text x="46" y="48" font-size="8" fill="#8C7B5E" font-family="system-ui">caixaria interna</text>
 <text x="82" y="69" font-size="8" fill="#241E18" font-family="system-ui" font-weight="700">18 mm · prateleira</text>
 <text x="46" y="103" font-size="8" fill="#8C7B5E" font-family="system-ui">base 15 mm</text>
 <path d="M209 128 H205" stroke="#8C7B5E"/><text x="150" y="130" font-size="7.5" fill="#8C7B5E" font-family="system-ui">fundo 6 mm →</text>
 <text x="228" y="66" font-size="8" fill="#241E18" font-family="system-ui" font-weight="700">18 mm</text>
 <text x="228" y="77" font-size="7.5" fill="#8C7B5E" font-family="system-ui">porta</text>
</svg>"""

SVG_ROME = """<svg viewBox="0 0 200 108" fill="none" xmlns="http://www.w3.org/2000/svg">
 <rect x="18" y="34" width="150" height="40" fill="#EFE7D8" stroke="#3A322A" stroke-width="1.5"/>
 <path d="M168 34 h14 v11 h-9 v18 h9 v11 h-14 z" fill="#C9A96A" stroke="#3A322A" stroke-width="1.2"/>
 <path d="M175 50 h-9" stroke="#3A322A" stroke-width="1" stroke-dasharray="2 2"/>
 <path d="M182 24 v-8" stroke="#8C7B5E"/>
 <text x="120" y="14" font-size="8" fill="#8C7B5E" font-family="system-ui">perfil embutido</text>
 <text x="20" y="92" font-size="8" fill="#8C7B5E" font-family="system-ui">a mão entra no perfil — nada aplicado</text>
</svg>"""

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style>
<style>
  .page:last-of-type{{page-break-after:avoid; break-after:avoid;}}

  .cover-t{{background:var(--deep); position:relative; overflow:hidden;}}
  .cover-t::before{{content:""; position:absolute; inset:0;
     background:radial-gradient(120% 80% at 16% 10%, rgba(201,169,106,.17) 0%, transparent 58%),
                radial-gradient(90% 70% at 90% 96%, rgba(201,169,106,.11) 0%, transparent 60%);}}
  .cover-t .rules{{position:absolute; inset:0;
     background:repeating-linear-gradient(90deg, rgba(255,255,255,.030) 0 1px, transparent 1px 34mm);}}

  .amb3{{border-top:1px solid var(--hair); padding:5.4mm 0;}}
  .amb3:first-child{{border-top:2px solid var(--ink);}}
  .amb3 .hd{{display:flex; justify-content:space-between; align-items:baseline;}}
  .amb3 .t{{font-family:'Cormorant Garamond',Georgia,serif; font-size:16pt; font-weight:700;
      line-height:1.15;}}
  .amb3 .q{{font-size:6.4pt; letter-spacing:.16em; text-transform:uppercase; color:var(--gold);
      font-weight:700; white-space:nowrap; padding-left:5mm;}}
  .amb3 .d{{font-size:9.6pt; color:var(--soft); line-height:1.66; margin-top:1.8mm;}}
  .amb3 .d b{{color:var(--ink);}}

  .rend3{{display:flex; gap:5mm; margin-top:8mm;}}
  .rend3 > div{{flex:1;}}
  .rend3 img{{width:100%; height:52mm; object-fit:cover; display:block; border-radius:4px;
      box-shadow:0 1px 6px rgba(0,0,0,.12);}}
  .rend3 .cp{{font-size:6.2pt; letter-spacing:.13em; text-transform:uppercase; color:var(--gold);
      font-weight:700; margin-top:1.8mm;}}

  /* ferragens */
  .fer{{display:flex; gap:8mm; margin-top:7mm; border-top:1px solid var(--line);
      padding-top:7.5mm; align-items:center;}}
  .fer:first-of-type{{border-top:2px solid var(--ink);}}
  .fer .art{{width:74mm; flex:none; background:var(--panel-2,#F4EEE1); border-radius:6px;
      padding:5mm 5.5mm;}}
  .fer .art svg{{width:100%; height:auto; display:block;}}
  .fer .tx{{flex:1;}}
  .fer .k{{font-size:6.4pt; letter-spacing:.17em; text-transform:uppercase; color:var(--gold);
      font-weight:700;}}
  .fer .t{{font-family:'Cormorant Garamond',Georgia,serif; font-size:19pt; font-weight:700;
      color:var(--ink); line-height:1.14; margin-top:1mm;}}
  .fer .d{{font-size:9.6pt; color:var(--soft); line-height:1.68; margin-top:2.4mm;}}
  .fer .d b{{color:var(--ink);}}

  /* estrutura */
  .estr{{display:flex; gap:8mm; margin-top:4mm; align-items:center;}}
  .estr .dw{{width:96mm; flex:none; background:var(--panel-2,#F4EEE1); border-radius:6px;
      padding:9mm 6mm 6mm;}}
  .estr .dw .cp{{font-size:6.4pt; letter-spacing:.14em; text-transform:uppercase;
      color:var(--gold); font-weight:700; text-align:center; margin-top:4mm; line-height:1.5;}}
  .estr .dw svg{{width:100%; height:auto; display:block;}}
  .esl{{border-top:1px solid var(--hair); padding:5.6mm 0;}}
  .esl:first-child{{border-top:2px solid var(--ink); padding-top:2.4mm;}}
  .esl .n{{font-family:'Cormorant Garamond',Georgia,serif; font-size:20pt; font-weight:700;
      color:var(--gold); line-height:1;}}
  .esl .d{{font-size:9.4pt; color:var(--soft); line-height:1.62; margin-top:1.5mm;}}
  .esl .d b{{color:var(--ink);}}

  /* tabela de duas colunas */
  .dual{{width:100%; border-collapse:collapse; font-size:8.4pt; margin-top:3mm;}}
  .dual th{{font-size:6.4pt; letter-spacing:.14em; text-transform:uppercase; color:var(--mut);
      font-weight:700; border-bottom:1.5px solid var(--ink); padding:0 0 2mm; text-align:left;
      vertical-align:bottom;}}
  .dual th.vh{{text-align:right; width:26mm; padding-left:3mm;}}
  .dual th.vh.alt{{color:var(--gold);}}
  .dual td{{padding:2.4mm 0; border-bottom:1px solid var(--hair); vertical-align:top;}}
  .dual td.sv{{width:34mm; font-weight:700; color:var(--ink); font-size:8.8pt; padding-right:3mm;}}
  .dual td.sv small{{display:block; font-weight:400; color:var(--soft); font-size:7.8pt;}}
  .dual td.ds{{color:var(--soft); line-height:1.55; padding-right:4mm;}}
  .dual td.vl{{text-align:right; white-space:nowrap; font-weight:700; font-variant-numeric:tabular-nums;
      padding-left:3mm;}}
  .dual td.vl.alt{{color:var(--gold); background:rgba(201,169,106,.07);}}
  .dual tr.tot td{{border-bottom:0; border-top:2px solid var(--ink); padding-top:3.4mm;
      font-family:'Cormorant Garamond',Georgia,serif; font-size:15pt;}}
  .dual tr.tot td.ds{{font-family:system-ui,sans-serif; font-size:8.4pt;}}

  .resp{{margin-top:5mm; background:var(--deep); border-left:3px solid var(--gold-lt);
      border-radius:0 5px 5px 0; padding:6.5mm 7.5mm;}}
  .resp .k{{font-size:6.6pt; letter-spacing:.2em; text-transform:uppercase; color:var(--gold-lt);
      font-weight:700;}}
  .resp .t{{font-family:'Cormorant Garamond',Georgia,serif; font-size:17pt; font-weight:700;
      color:#fff; line-height:1.15; margin-top:1.4mm;}}
  .resp .d{{font-size:8.6pt; color:#C6BFB2; line-height:1.62; margin-top:2mm;}}
  .resp .d b{{color:#F0E7D6;}}
  .resp ul{{margin:2mm 0 0; padding-left:4.5mm; font-size:8.6pt; color:#C6BFB2; line-height:1.62;}}
  .resp ul b{{color:#F0E7D6;}}

  /* pagamento */
  .pgto{{display:flex; gap:6mm; margin-top:7mm;}}
  .pgto > div{{flex:1; border:1.5px solid var(--line); border-radius:7px; padding:8mm 7mm;}}
  .pgto > div.best{{border-color:var(--gold); background:rgba(201,169,106,.07);}}
  .pgto .k{{font-size:6.4pt; letter-spacing:.16em; text-transform:uppercase; color:var(--gold);
      font-weight:700;}}
  .pgto .big{{font-family:'Cormorant Garamond',Georgia,serif; font-size:30pt; font-weight:700;
      color:var(--ink); line-height:1.05; margin-top:1.6mm;}}
  .pgto .sub{{font-size:8.4pt; color:var(--soft); line-height:1.55; margin-top:1.6mm;}}
  .pgto .sub b{{color:var(--ink);}}
  .pgto .sec{{margin-top:3mm; padding-top:2.6mm; border-top:1px solid var(--line);
      font-size:8.4pt; color:var(--soft); line-height:1.5;}}
  .pgto .sec b{{color:var(--gold); font-size:10pt;}}

  .cnd{{display:grid; grid-template-columns:1fr 1fr; gap:5mm 8mm; margin-top:7mm;
      border-top:2px solid var(--ink); padding-top:4.6mm;}}
  .cnd .k{{font-size:6.4pt; letter-spacing:.16em; text-transform:uppercase; color:var(--gold);
      font-weight:700;}}
  .cnd .d{{font-size:9pt; color:var(--soft); line-height:1.58; margin-top:1.1mm;}}
  .cnd .d b{{color:var(--ink);}}
</style></head><body>

<!-- ══════ 1. CAPA ══════ -->
<div class="page cover cover-t">
  <div class="rules"></div>
  <div class="inner">
    <div><div class="brand">valvic<span class="d">.</span></div><div class="bsub">MARCENARIA</div></div>
    <div class="mid">
      <div class="kick">Proposta de marcenaria sob medida</div>
      <div class="tit">Nádia<br>&amp; Maurílio.</div>
      <div class="sub">Cozinha · suíte master · lavanderias · hall dos dormitórios</div>
    </div>
    <div class="strip">
      <div class="c"><div class="k">Escopo</div><div class="v">8 conjuntos · 5 ambientes</div></div>
      <div class="c"><div class="k">Ferragens</div><div class="v">Hettich · Blum · Rometal</div></div>
      <div class="c"><div class="k">Entrega</div><div class="v">80 a 90 dias corridos</div></div>
    </div>
  </div>
</div>

<!-- ══════ 2. O ESCOPO ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">O que será executado</div>
  <div class="h-sec serif" style="font-size:25pt;">Cinco ambientes,<br><em>o mesmo padrão.</em></div>
  <hr class="rule" style="margin:8px 0 8px;">
  <p class="lead" style="margin-bottom:2mm;">Fornecimento, entrega e instalação, conforme o projeto
  de marcenaria. Estrutura em <b>MDF Areia Guararapes</b>, com as cores externas do projeto.</p>

  <div style="margin-top:2.5mm;">
    <div class="amb3"><div class="hd"><div class="t">Cozinha</div><div class="q">4 conjuntos</div></div>
      <div class="d"><b>Ilha e geladeiras</b> com a ilha reduzida para 2,80 m · <b>bancada</b> com
      aéreos e inferiores, básculas em MDF amadeirado por dentro e por fora · <b>cristaleira</b> de
      80 cm com 3 portas de vidro reflecta bronze e prateleiras de vidro temperado · <b>painel de TV</b>
      em MDF Itapuã. LED instalado na cristaleira e no painel.</div></div>
    <div class="amb3"><div class="hd"><div class="t">Suíte master · closet</div><div class="q">versão 2</div></div>
      <div class="d">Estrutura completa em MDF Areia, <b>gavetas com puxadores espaçados</b> e
      <b>cabideiros metálicos</b>. Versão 2 — sem a cômoda.</div></div>
    <div class="amb3"><div class="hd"><div class="t">Lavanderias</div><div class="q">térreo + superior</div></div>
      <div class="d">Duas lavanderias na mesma especificação: puxadores inferiores em cava,
      superiores passantes, e <b>fundo em MDF com duplo revestimento</b> — a face de dentro acabada
      como a de fora, onde a umidade é rotina.</div></div>
    <div class="amb3"><div class="hd"><div class="t">Hall dos dormitórios</div><div class="q">espelho</div></div>
      <div class="d"><b>Portas de espelho prata</b> em esquadria de alumínio bronze, sobre a mesma
      caixaria em MDF Areia.</div></div>
  </div>

  <div class="rend3">
    <div><img src="{COZ2}" alt=""><div class="cp">Cozinha · ilha</div></div>
    <div><img src="{CLO1}" alt=""><div class="cp">Closet</div></div>
    <div><img src="{LAV1}" alt=""><div class="cp">Lavanderia</div></div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Nádia &amp; Maurílio</span></div>
</div></div>

<!-- ══════ 3. ESTRUTURA ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Estrutura do móvel</div>
  <div class="h-sec serif" style="font-size:25pt;">A espessura certa<br><em>em cada peça.</em></div>
  <hr class="rule" style="margin:8px 0 9px;">
  <p class="lead" style="margin-bottom:2mm;">Um móvel não empena por acaso: empena onde a chapa é
  fina demais para o vão que ela vence. Cada peça deste projeto recebe a espessura da função que
  cumpre — e não uma espessura única para tudo.</p>

  <div class="estr">
    <div class="dw">{SVG_ESTR}<div class="cp">Corte da caixaria<br>as quatro espessuras do projeto</div></div>
    <div style="flex:1;">
      <div class="esl"><div class="n">15 mm</div>
        <div class="d"><b>Caixaria interna.</b> Laterais, base e tampo. É a estrutura que não
        aparece e que segura tudo o que aparece.</div></div>
      <div class="esl"><div class="n">18 mm</div>
        <div class="d"><b>Prateleiras.</b> A peça que mais sofre: recebe carga distribuída no meio
        do vão. Em 15 mm ela cede com o tempo — <b>é a barriga que aparece no segundo verão</b>.
        Em 18 não.</div></div>
      <div class="esl"><div class="n">6 mm</div>
        <div class="d"><b>Fundos.</b> Encaixados em ranhura na caixaria, travando o esquadro do
        móvel. Nas lavanderias, com <b>duplo revestimento</b>.</div></div>
      <div class="esl"><div class="n">18 mm</div>
        <div class="d"><b>Portas e acabamentos.</b> A folha precisa de massa para não torcer e
        para receber dobradiça com firmeza — e é o que se toca todo dia.</div></div>
    </div>
  </div>

  <div class="pull" style="margin-top:9mm;">
    <div class="t">O que sustenta<br>não é o que se vê.</div>
    <div class="d">A diferença entre 15 e 18 mm numa prateleira não aparece na entrega. Aparece
    três anos depois, quando uma cede e a outra não. <b>É por isso que a espessura está escrita
    nesta proposta</b> — para poder ser cobrada.</div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Nádia &amp; Maurílio</span></div>
</div></div>

<!-- ══════ 4. FERRAGENS ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Ferragens especificadas</div>
  <div class="h-sec serif" style="font-size:25pt;">Onde o móvel<br><em>é usado todo dia.</em></div>
  <hr class="rule" style="margin:8px 0 8px;">

  <div class="fer">
    <div class="art">{SVG_CORR}</div>
    <div class="tx"><div class="k">Hettich · Alemanha</div>
      <div class="t">Corrediças e dobradiças.</div>
      <div class="d"><b>Corrediça oculta</b> sob a gaveta — não aparece pela lateral e fecha sozinha
      no fim do curso. <b>Dobradiça com amortecimento integrado</b>, dentro do corpo da própria peça:
      a porta desacelera e encosta macia em qualquer velocidade, com ajuste em <b>três dimensões</b>
      para a fresta continuar igual anos depois da instalação.</div></div>
  </div>

  <div class="fer">
    <div class="art">{SVG_BLUM}</div>
    <div class="tx"><div class="k">Blum · Áustria</div>
      <div class="t">Articulador HK-S.</div>
      <div class="d">Nas <b>básculas dos aéreos da cozinha</b>. A folha sobe e <b>para exatamente
      onde é solta</b> — em qualquer ponto do curso, não só aberta ou fechada. Desce amortecida,
      sem risco de cair na cabeça de quem está na bancada. É a ferragem que decide se o armário
      alto é confortável ou se vira aquele que ninguém abre.</div></div>
  </div>

  <div class="fer">
    <div class="art">{SVG_ROME}</div>
    <div class="tx"><div class="k">Rometal · perfil RM280</div>
      <div class="t">Puxador em cava.</div>
      <div class="d">Perfil <b>embutido na própria frente</b> nos armários inferiores — a mão entra
      no rebaixo e não há nada aplicado para esbarrar, prender pano de prato ou marcar a linha do
      móvel. Nos superiores, <b>puxador passante</b>. A frente fica limpa e a leitura do conjunto,
      contínua.</div></div>
  </div>

  <div class="note" style="margin-top:5.5mm;">Todas as ferragens são <b>especificadas por linha e
  modelo</b> nesta proposta — não por categoria. É o que permite conferir na entrega exatamente o
  que foi contratado.</div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Nádia &amp; Maurílio</span></div>
</div></div>

<!-- ══════ 5. INVESTIMENTO — DUAS COLUNAS ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="h-sec serif" style="font-size:25pt;">Duas formas<br><em>de contratar.</em></div>
  <hr class="rule" style="margin:8px 0 8px;">
  <p class="lead" style="margin-bottom:1mm;">A coluna da esquerda é a contratação completa, com as
  ferragens fornecidas pela Valvic. A da direita é a mesma marcenaria <b>sem o fornecimento das
  ferragens</b> — leia a condição da página seguinte antes de optar.</p>

  <table class="dual">
    <thead><tr><th>Serviço</th><th>Descrição</th>
      <th class="vh">Com ferragens<br><span style="font-weight:400;text-transform:none;letter-spacing:0;">fornecimento Valvic</span></th>
      <th class="vh alt">Sem ferragens<br><span style="font-weight:400;text-transform:none;letter-spacing:0;">compra da cliente</span></th></tr></thead>
    <tbody>
      {linhas}
      <tr class="tot"><td class="sv">Total</td><td class="ds"></td>
        <td class="vl">R$ {br(TOT_C)}</td><td class="vl alt">R$ {br(TOT_S)}</td></tr>
    </tbody>
  </table>

  <div class="note" style="margin-top:4mm;">A diferença entre as colunas é de
  <b>R$ {br(TOT_C-TOT_S)}</b> — o custo das ferragens especificadas nas páginas anteriores,
  com o fornecimento, a conferência e a garantia sob nossa responsabilidade.</div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Nádia &amp; Maurílio</span></div>
</div></div>

<!-- ══════ 6. CONDIÇÕES ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Condições</div>
  <div class="h-sec serif" style="font-size:25pt;">Como fechamos.</div>
  <hr class="rule" style="margin:8px 0 8px;">

  <div class="resp">
    <div class="k">Se a opção for “sem ferragens”</div>
    <div class="t">O fornecimento passa a ser<br>da contratante.</div>
    <div class="d">A Valvic executa a marcenaria e faz a instalação. <b>Todo o processo de aquisição
    das ferragens passa a ser de inteira responsabilidade da contratante</b>, incluindo:</div>
    <ul>
      <li><b>Pedido e especificação</b> — modelo, linha e quantidade exatos, conforme esta proposta.</li>
      <li><b>Notas fiscais</b> e a relação comercial direta com o fornecedor.</li>
      <li><b>Logística</b> — prazo de compra, transporte e entrega das peças na data da montagem.</li>
      <li><b>Ocorrências</b> — falta, atraso, peça errada, avaria no transporte, defeito de fábrica,
          troca e garantia junto ao fabricante.</li>
    </ul>
    <div class="d"><b>Efeito no prazo e na garantia:</b> a instalação só ocorre com as ferragens
    disponíveis no local — atraso na entrega delas desloca o cronograma. A garantia Valvic
    permanece integral sobre a marcenaria, <b>e não alcança as ferragens fornecidas por
    terceiros</b> nem os desdobramentos de uma ferragem inadequada sobre a peça.</div>
  </div>

  <div class="pgto">
    <div><div class="k">4× no boleto · −5%</div>
      <div class="big">R$ {br(TOT_C*0.95)}</div>
      <div class="sub">com ferragens · <b>4 parcelas de R$ {br2(TOT_C*0.95/4)}</b>,
        primeiro boleto para <b>60 dias</b>.</div>
      <div class="sec">sem ferragens <b>R$ {br2(TOT_S*0.95)}</b><br>
        4 × R$ {br2(TOT_S*0.95/4)}</div></div>
    <div class="best"><div class="k">À vista · −10%</div>
      <div class="big">R$ {br(TOT_C*0.90)}</div>
      <div class="sub">com ferragens · <b>70% de entrada</b> (R$ {br2(TOT_C*0.90*0.7)})
        e o saldo na entrega final.</div>
      <div class="sec">sem ferragens <b>R$ {br(TOT_S*0.90)}</b><br>
        entrada de R$ {br2(TOT_S*0.90*0.7)}</div></div>
  </div>

  <div class="cnd" style="margin-top:9mm;">
    <div><div class="k">Prazo de entrega</div><div class="d"><b>80 a 90 dias corridos</b> a partir
      do pagamento.</div></div>
    <div><div class="k">Conferência técnica</div><div class="d">Precisa ocorrer em <b>até 60 dias
      antes</b> do prazo de entrega — é ela que libera o corte.</div></div>
    <div><div class="k">Garantia</div><div class="d"><b>5 anos</b> em contrato — estrutura, montagem,
      acabamento e instalação.</div></div>
    <div><div class="k">Validade da proposta</div><div class="d"><b>7 dias corridos</b> a partir
      desta data.</div></div>
  </div>

  <div class="note" style="margin-top:5mm;"><b>Não incluso:</b> eletrodomésticos, cubas, torneiras,
  tampos de pedra, pontos elétricos e hidráulicos, alvenaria, gesso e pintura do ambiente.
  <b>Medição:</b> conferida no local antes do corte — nada entra em máquina sem conferência.</div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Nádia &amp; Maurílio · 06/08/2026</span></div>
</div></div>

</body></html>"""

(P/'proposta-nadia.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-nadia.html', len(HTML))
print(f'COM R$ {br(TOT_C)} · SEM R$ {br(TOT_S)} · diferença R$ {br(TOT_C-TOT_S)}')
