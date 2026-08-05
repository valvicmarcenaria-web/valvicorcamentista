# -*- coding: utf-8 -*-
"""PROPOSTA — Cristaleira 100 × 205 × 40.
3 páginas: capa · o móvel · investimento. Peça única — uma pasta de 6 seria
desproporcional. Preço FECHADO em R$ 7.500 [Jonathan 04/08] — MC implícita 20,9% no cartão,
28,1% em transferência. Ver 2026-cristaleira.md."""
import pathlib, base64
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')
CSS = open('/tmp/css_premium.txt', encoding='utf-8').read().split('CSS = """')[1].rsplit('"""',1)[0]

def uri(n):
    return 'data:image/jpeg;base64,' + base64.b64encode((P/'img'/n).read_bytes()).decode()

CAPA   = uri('cristaleira-capa.jpg')
ABERTA = uri('cristaleira-aberta.jpg')
FECHADA = uri('cristaleira-fechada.jpg')

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style>
<style>
  .page:last-of-type{{page-break-after:avoid; break-after:avoid;}}

  /* capa em faixa: o render tem 1202 px de altura — em full-bleed A4 daria
     103 dpi; na faixa de 190 mm fica em 161. */
  .cover-b{{background:var(--deep); position:relative; overflow:hidden;
      display:flex; flex-direction:column;}}
  .cover-b .band{{height:190mm; flex:none; overflow:hidden; position:relative;}}
  .cover-b .band img{{width:100%; height:100%; object-fit:cover; display:block;}}
  .cover-b .band::after{{content:""; position:absolute; left:0; right:0; bottom:0; height:26mm;
      background:linear-gradient(to bottom, rgba(26,23,20,0) 0%, var(--deep) 100%);}}
  .cover-b .low{{flex:1; padding:0 20mm 18mm; display:flex; flex-direction:column;
      justify-content:space-between; position:relative;}}
  .cover-b .brand{{font-family:'Cormorant Garamond',Georgia,serif; font-size:20pt; font-weight:700;
      color:#fff; line-height:1;}}
  .cover-b .brand .d{{color:var(--gold-lt);}}
  .cover-b .bsub{{font-size:6.6pt; letter-spacing:.34em; color:var(--gold-lt); font-weight:700;
      margin-top:1.4mm;}}
  .cover-b .kick{{font-size:7pt; letter-spacing:.2em; text-transform:uppercase; color:var(--gold-lt);
      font-weight:700;}}
  .cover-b .tit{{font-family:'Cormorant Garamond',Georgia,serif; font-size:52pt; font-weight:700;
      color:#fff; line-height:.98; margin-top:2.5mm;}}
  .cover-b .sub{{font-size:10pt; color:#C6BFB2; margin-top:2.5mm;}}
  .cover-b .strip{{display:flex; margin-top:7mm; padding-top:4.5mm;
      border-top:1px solid rgba(201,169,106,.30);}}
  .cover-b .strip .c{{flex:1; padding-left:6mm; border-left:1px solid rgba(201,169,106,.18);}}
  .cover-b .strip .c:first-child{{padding-left:0; border-left:0;}}
  .cover-b .strip .k{{font-size:6.2pt; letter-spacing:.18em; text-transform:uppercase;
      color:var(--gold-lt); font-weight:700;}}
  .cover-b .strip .v{{font-size:9.4pt; color:#EDE6D9; margin-top:1.4mm; line-height:1.35;}}

  /* pagina do movel */
  .duo{{display:flex; gap:8mm; margin-top:4mm; align-items:stretch;}}
  .duo .ph{{width:88mm; flex:none;}}
  .duo .ph img{{width:88mm; height:96mm; object-fit:cover; display:block; border-radius:4px;
      box-shadow:0 2px 10px rgba(0,0,0,.14);}}
  .duo .ph img + img{{margin-top:5mm;}}
  .duo .ph .cp{{font-size:6.4pt; letter-spacing:.14em; text-transform:uppercase; color:var(--gold);
      font-weight:700; margin-top:2.2mm; line-height:1.5;}}
  .duo .dd{{flex:1;}}
  .dl{{border-top:1px solid var(--hair); padding:6.4mm 0;}}
  .dl:first-child{{border-top:2px solid var(--ink); padding-top:2.6mm;}}
  .dl .k{{font-size:6.4pt; letter-spacing:.16em; text-transform:uppercase; color:var(--gold);
      font-weight:700;}}
  .dl .v{{font-size:10pt; color:var(--soft); line-height:1.6; margin-top:1.2mm;}}
  .dl .v b{{color:var(--ink);}}

  /* passos ate' a entrega */
  .steps{{display:flex; gap:0; margin-top:13mm; border-top:1px solid var(--line);
      border-bottom:1px solid var(--line); padding:5.5mm 0;}}
  .steps > div{{flex:1; padding-left:6mm; padding-block:1mm; border-left:1px solid var(--line);}}
  .steps > div:first-child{{padding-left:0; border-left:0;}}
  .steps .k{{font-size:6.4pt; letter-spacing:.16em; text-transform:uppercase; color:var(--gold);
      font-weight:700;}}
  .steps .t{{font-family:'Cormorant Garamond',Georgia,serif; font-size:15pt; font-weight:700;
      color:var(--ink); line-height:1.15; margin-top:1mm;}}
  .steps .d{{font-size:8.8pt; color:var(--soft); line-height:1.6; margin-top:1.4mm;}}
  .steps .d b{{color:var(--ink);}}

  /* preco fechado dentro da caixa escura */
  .inv-hero{{padding:14mm 8mm !important;}}
  .inv-hero .v{{font-size:50pt !important; margin:2.5mm 0 1.5mm !important;}}
  .inv-hero .c{{font-size:9.2pt !important;}}
  .pay2{{display:flex; margin-top:6.5mm; padding-top:5mm;
      border-top:1px solid rgba(201,169,106,.30);}}
  .pay2 > div{{flex:1; padding-left:7mm; border-left:1px solid rgba(201,169,106,.18);}}
  .pay2 > div:first-child{{padding-left:0; border-left:0;}}
  .pay2 b{{display:block; font-family:'Cormorant Garamond',Georgia,serif; font-size:26pt;
      font-weight:700; color:var(--gold-lt); line-height:1;}}
  .pay2 span{{display:block; font-size:8.8pt; color:#C6BFB2; margin-top:2mm; line-height:1.55;}}
</style></head><body>

<!-- ══════ 1. CAPA ══════ -->
<div class="page cover-b">
  <div class="band"><img src="{CAPA}" alt="Cristaleira"></div>
  <div class="low">
    <div>
      <div class="kick">Proposta de marcenaria sob medida</div>
      <div class="tit">Cristaleira.</div>
      <div class="sub">1,00 × 2,05 m · portas de vidro · quatro prateleiras e três gavetas</div>
      <div class="strip">
        <div class="c"><div class="k">Medidas</div><div class="v">100 × 205 × 40 cm</div></div>
        <div class="c"><div class="k">Acabamento</div><div class="v">MDF Arauco Moscada Matt</div></div>
        <div class="c"><div class="k">Entrega</div><div class="v">60 dias corridos</div></div>
      </div>
    </div>
    <div style="display:flex; align-items:flex-end; justify-content:space-between;">
      <div><div class="brand">valvic<span class="d">.</span></div>
        <div class="bsub">MARCENARIA</div></div>
    </div>
  </div>
</div>

<!-- ══════ 2. O MÓVEL ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">O móvel</div>
  <div class="h-sec serif" style="font-size:26pt;">Em cima o que se mostra,<br>
    <em>embaixo o que se guarda.</em></div>
  <hr class="rule" style="margin:8px 0 10px;">

  <div class="duo">
    <div class="ph">
      <img src="{ABERTA}" alt="Cristaleira aberta, com as prateleiras e as gavetas">
      <img src="{FECHADA}" alt="Cristaleira fechada, com as portas de vidro">
      <div class="cp">Aberta e fechada · quatro vãos de 26,75 cm<br>três gavetas de corrediça oculta</div>
    </div>
    <div class="dd">
      <div class="dl"><div class="k">Medidas</div>
        <div class="v"><b>100 cm</b> de largura · <b>205 cm</b> de altura ·
        <b>40 cm</b> de profundidade.</div></div>
      <div class="dl"><div class="k">A vitrine</div>
        <div class="v"><b>Quatro vãos de 26,75 cm</b> — altura que aceita taça de
        champanhe em pé, sem deitar nem encostar no vidro.</div></div>
      <div class="dl"><div class="k">As gavetas</div>
        <div class="v"><b>Três gavetas</b> de 25 cm de frente, em <b>corrediça oculta
        Hardt</b>: fecham sozinhas nos últimos centímetros e não aparecem por baixo.
        Puxador em <b>cava de 45°</b> usinada na própria frente — nada aplicado.</div></div>
      <div class="dl"><div class="k">As portas</div>
        <div class="v">Duas folhas de <b>50 cm</b> com moldura de <b>4 cm</b> e
        <b>vidro incolor</b>. Puxador <b>Ponto Italyline Ales 118</b>, cobre velho.</div></div>
      <div class="dl"><div class="k">O pé</div>
        <div class="v"><b>4 cm</b> de altura com <b>2 cm de recuo frontal</b> — a sombra
        embaixo faz o móvel parecer pousado, não apoiado.</div></div>
      <div class="dl"><div class="k">Acabamento</div>
        <div class="v"><b>MDF Arauco Moscada Matt</b> por fora e por dentro — o tom
        continua ao abrir a porta. Interior das gavetas em branco.</div></div>
    </div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Cristaleira · 100 × 205 × 40</span></div>
</div></div>

<!-- ══════ 3. INVESTIMENTO ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="h-sec serif" style="font-size:26pt;">A peça completa,<br><em>instalada.</em></div>
  <hr class="rule" style="margin:8px 0 9px;">
  <p class="lead" style="margin-bottom:4mm;">Fornecimento, ferragens, vidro, entrega e
  instalação inclusos.</p>

  <div class="inv-hero">
    <div class="k">Cristaleira · 100 × 205 × 40 cm</div>
    <div class="v">R$ 7.500</div>
    <div class="c">MDF Arauco Moscada Matt · portas de vidro incolor com moldura de 4 cm ·
      4 prateleiras · 3 gavetas em corrediça oculta · ferragens Hardt</div>
    <div class="pay2">
      <div><b>30%</b><span>na assinatura — libera a compra do material e a entrada
        na fila de produção</span></div>
      <div><b>10×</b><span>o saldo em até dez vezes no cartão, ou em transferência
        na entrega</span></div>
    </div>
  </div>


  <div class="terms" style="margin-top:12mm;">
    <div class="term"><div class="k">Prazo de entrega</div>
      <div class="v"><b>60 dias</b> corridos</div></div>
    <div class="term"><div class="k">Garantia</div>
      <div class="v"><b>5 anos</b> em contrato</div></div>
    <div class="term"><div class="k">Execução</div>
      <div class="v">Equipe <b>própria</b></div></div>
    <div class="term"><div class="k">Validade</div>
      <div class="v"><b>15 dias</b> corridos</div></div>
  </div>

  <div class="steps">
    <div><div class="k">Passo 1</div><div class="t">Aceite</div>
      <div class="d">Assinatura e a entrada. É o que reserva a data de produção.</div></div>
    <div><div class="k">Passo 2</div><div class="t">Medição</div>
      <div class="d">Visita ao local para conferir o vão e o prumo da parede,
      <b>antes de cortar</b>.</div></div>
    <div><div class="k">Passo 3</div><div class="t">Entrega</div>
      <div class="d"><b>60 dias corridos</b> · instalação, vidro assentado e portas
      reguladas no local.</div></div>
  </div>

  <div class="note" style="margin-top:7mm;"><b>Medição:</b> conferida no local antes do
  corte. Qualquer divergência entre a medida real e o projeto é reapresentada antes de
  qualquer produção — nada entra em máquina sem conferência.</div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Cristaleira · 04/08/2026</span></div>
</div></div>

</body></html>"""

(P/'proposta-cristaleira.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-cristaleira.html', len(HTML))
