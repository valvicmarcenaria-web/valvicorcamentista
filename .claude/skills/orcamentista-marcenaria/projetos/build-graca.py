# -*- coding: utf-8 -*-
# Monta a proposta Graca (3 paginas, layout leve/editorial). Imagens do cliente em base64.
import base64, pathlib
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')
def b64(name):
    return 'data:image/png;base64,' + base64.b64encode((P/name).read_bytes()).decode()
IMG_DESP = b64('img-graca-despensa.png')
IMG_LAV  = b64('img-graca-lavanderia.png')
IMG_TAN  = b64('img-graca-tanque.png')

HTML = f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8">
<style>
:root{{--gold:#B8901E;--gold-soft:#D9B25A;--gold-deep:#9A6E12;--ink:#211a12;--ink-soft:#5c5344;--mut:#8b8172;
--cream:#FCF8F0;--cream-2:#F5EEDE;--line:#EAE0CB;--line-soft:#F0E9D9;--paper:#fff;--petrol:#2C4A5A;--petrol-soft:#5C7686;--petrol-tint:#F5F8F8;--petrol-line:#CBD7DB;}}
@page{{size:A4;margin:0;}}
*{{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}}
body{{margin:0;font-family:'DM Sans','Liberation Sans',Arial,sans-serif;color:var(--ink);font-size:10.5pt;line-height:1.65;}}
.serif{{font-family:'Cormorant Garamond','Georgia',serif;}}
.page{{position:relative;width:210mm;height:297mm;padding:14mm 18mm 13mm;page-break-after:always;overflow:hidden;background:var(--paper);}}
.page:last-child{{page-break-after:auto;}}
h1,h2,h3{{margin:0;font-weight:600;}}
p{{margin:8px 0;}}
.eyebrow{{letter-spacing:.34em;text-transform:uppercase;font-size:8pt;font-weight:700;color:var(--gold-deep);}}
.rule{{height:1.5px;width:46px;background:var(--gold-soft);border:0;margin:10px 0 11px;}}
.section-h{{font-family:'Cormorant Garamond','Georgia',serif;font-size:22.5pt;font-weight:700;color:var(--ink);line-height:1.1;letter-spacing:.01em;}}
.lead{{font-family:'Cormorant Garamond','Georgia',serif;font-size:13.5pt;font-style:italic;color:var(--ink-soft);line-height:1.5;max-width:158mm;}}
.pfoot{{position:absolute;left:19mm;right:19mm;bottom:12mm;display:flex;justify-content:space-between;font-size:7.4pt;color:var(--mut);letter-spacing:.13em;border-top:1px solid var(--line-soft);padding-top:3mm;}}
.brandline{{font-family:'Cormorant Garamond','Georgia',serif;font-weight:700;letter-spacing:.12em;}}.brandline .dot{{color:var(--gold);}}

/* ---------- CAPA ---------- */
.cover{{padding:0;background:var(--cream);}}
.cover .frame{{position:absolute;inset:10mm;border:1px solid var(--gold-soft);pointer-events:none;}}
.cover .inner{{position:relative;padding:20mm 19mm 16mm;height:297mm;display:flex;flex-direction:column;}}
.brand{{font-family:'Cormorant Garamond','Georgia',serif;font-size:28pt;font-weight:700;letter-spacing:.2em;color:var(--ink);}}
.brand .dot{{color:var(--gold);}}
.brand-sub{{letter-spacing:.52em;font-size:7.6pt;font-weight:700;color:var(--gold-deep);margin-top:3px;}}
.heroimg{{width:100%;height:119mm;margin:9mm 0 8mm;border-radius:2px;background:var(--petrol-tint) center/cover no-repeat;border:1px solid var(--line);box-shadow:0 10px 26px rgba(44,74,90,.16);}}
.cover .cap{{letter-spacing:.22em;text-transform:uppercase;font-size:7.2pt;color:var(--gold-deep);font-weight:700;margin-bottom:9mm;}}
.cover .for{{letter-spacing:.36em;text-transform:uppercase;font-size:8.6pt;font-weight:700;color:var(--gold-deep);}}
.cover .client{{font-family:'Cormorant Garamond','Georgia',serif;font-size:37pt;font-weight:700;line-height:1.02;margin:4px 0 4px;color:var(--ink);}}
.cover .proj{{font-family:'Cormorant Garamond','Georgia',serif;font-style:italic;font-size:14.5pt;color:var(--ink-soft);}}
.cover .foot{{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;font-size:8.4pt;color:var(--ink-soft);letter-spacing:.05em;}}
.sparkles{{font-size:11pt;color:var(--gold-soft);letter-spacing:.45em;margin-bottom:3mm;}}

/* ---------- ESCOPO ---------- */
.amb{{display:flex;gap:7mm;align-items:stretch;margin-top:4mm;}}
.amb .im{{width:53mm;flex:none;border:1px solid var(--line);border-radius:3px;background:var(--petrol-tint) center/cover no-repeat;box-shadow:0 4px 12px rgba(44,74,90,.09);}}
.amb .tx{{flex:1;padding-top:1mm;}}
.amb .nm{{font-family:'Cormorant Garamond','Georgia',serif;font-size:17pt;font-weight:700;color:var(--ink);line-height:1.02;}}
.amb .sub{{font-size:8pt;letter-spacing:.15em;text-transform:uppercase;color:var(--gold-deep);font-weight:700;margin-top:1.5mm;}}
.amb ul{{margin:3mm 0 0;padding-left:4.6mm;font-size:9.2pt;color:var(--ink-soft);}}
.amb li{{margin:1.8mm 0;}}
.note{{margin-top:3.5mm;padding:0 0 0 5mm;border-left:2px solid var(--gold-soft);font-size:8.6pt;color:var(--ink-soft);line-height:1.5;}}
.note b{{color:var(--ink);}}
.note .h{{font-size:7.4pt;letter-spacing:.17em;text-transform:uppercase;color:var(--gold-deep);font-weight:700;margin-bottom:2.2mm;}}

/* ---------- INVESTIMENTO ---------- */
.lines{{display:flex;gap:7mm;margin-top:5mm;align-items:stretch;}}
.lineC{{flex:1;border:1px solid var(--line);border-radius:7px;padding:4.5mm 6mm;background:var(--paper);position:relative;}}
.lineC::before{{content:"";position:absolute;left:0;right:0;top:0;height:2.5px;background:var(--gold-soft);border-radius:7px 7px 0 0;}}
.lineC.prem{{background:var(--petrol-tint);border-color:var(--petrol-line);}}
.lineC.prem::before{{background:var(--petrol);}}
.recom{{position:absolute;top:-2.8mm;right:5.5mm;background:var(--gold);color:#fff;font-size:6.6pt;letter-spacing:.15em;text-transform:uppercase;font-weight:700;padding:1.4mm 3mm;border-radius:20px;box-shadow:0 2px 6px rgba(184,144,30,.28);}}
.lineC .tag{{letter-spacing:.2em;text-transform:uppercase;font-size:7.4pt;font-weight:700;color:var(--gold-deep);}}
.lineC.prem .tag{{color:var(--petrol);}}
.lineC .nm{{font-family:'Cormorant Garamond','Georgia',serif;font-size:19pt;font-weight:700;margin:3px 0 1mm;color:var(--ink);}}
.lineC .warr{{font-family:'Cormorant Garamond','Georgia',serif;font-size:13.5pt;font-weight:600;color:var(--gold-deep);}}
.lineC.prem .warr{{color:var(--petrol);}}
.lineC .price{{font-family:'Cormorant Garamond','Georgia',serif;font-size:22pt;font-weight:700;margin-top:2.5mm;line-height:1;color:var(--ink);}}
.lineC .plab{{font-size:7.4pt;letter-spacing:.14em;text-transform:uppercase;color:var(--mut);margin-top:1.5mm;}}
.lineC ul{{margin:2.8mm 0 0;padding-left:5mm;font-size:8.9pt;color:var(--ink-soft);}}
.lineC li{{margin:1.4mm 0;}}

table{{width:100%;border-collapse:collapse;margin:4.5mm 0 2mm;font-size:9.6pt;}}
thead th{{background:transparent;color:var(--ink-soft);font-size:7.4pt;letter-spacing:.16em;text-transform:uppercase;font-weight:700;border:0;border-bottom:1.5px solid var(--ink);padding:0 4mm 2.2mm;}}
td{{padding:1.5mm 4mm;text-align:left;border-bottom:1px solid var(--line-soft);}}
td.r,th.r{{text-align:right;font-variant-numeric:tabular-nums;}}
.amb-name{{font-weight:600;color:var(--ink);}}
.prem-col{{background:rgba(44,74,90,.045);}}
.grand td{{background:transparent;border:0;border-top:1.5px solid var(--gold);color:var(--ink);font-weight:700;font-size:11pt;padding-top:2.6mm;}}
.grand .serif{{font-size:13.5pt;}}
.grand .prem-col{{background:rgba(44,74,90,.045);}}
.tcap{{font-size:7.8pt;color:var(--mut);margin-top:2.5mm;font-style:italic;}}

.split{{display:flex;gap:9mm;margin-top:2.5mm;}}.split>div{{flex:1;}}
h3.blk{{font-family:'Cormorant Garamond','Georgia',serif;font-size:14pt;color:var(--ink);margin-bottom:1mm;}}
.hrule{{height:1px;background:var(--line);margin:2.5mm 0 3mm;}}
.pay{{margin:2mm 0 0;padding-left:4.6mm;}}.pay li{{margin:1.6mm 0;font-size:9pt;line-height:1.4;color:var(--ink-soft);}}
.pay b{{color:var(--ink);}}
.terms{{display:flex;gap:5mm;margin-top:3mm;}}
.term{{flex:1;border:1px solid var(--line);border-radius:4px;padding:3.2mm 3mm;text-align:center;background:var(--paper);}}
.term .t{{font-size:7pt;letter-spacing:.16em;text-transform:uppercase;color:var(--gold-deep);font-weight:700;}}
.term .b{{font-family:'Cormorant Garamond','Georgia',serif;font-size:13.5pt;font-weight:700;margin-top:3px;line-height:1.12;color:var(--ink);}}
.signoff{{position:absolute;left:18mm;right:18mm;bottom:22mm;text-align:center;font-size:14pt;font-style:italic;color:var(--ink-soft);border-top:1px solid var(--line);padding-top:4.5mm;}}
</style></head>
<body>

<!-- PAGE 1 — CAPA -->
<div class="page cover">
  <div class="frame"></div>
  <div class="inner">
    <div><div class="brand">valvic<span class="dot">.</span></div><div class="brand-sub">MARCENARIA</div></div>
    <div class="heroimg" style="background-image:url('{IMG_DESP}');"></div>
    <div class="cap">Marcenaria sob medida · MDF Azul Petróleo Guararapes</div>
    <div class="for">Proposta para</div>
    <div class="client">Graça</div>
    <div class="proj">Despensa · Lavanderia · Armário-tanque — projeto arq. Lais Teles</div>
    <div class="foot">
      <div><span class="sparkles">✦ ✦ ✦</span><br>Feito à mão, medido no milímetro.</div>
      <div style="text-align:right">Proposta comercial<br>16 de julho de 2026 · validade 15 dias</div>
    </div>
  </div>
</div>

<!-- PAGE 2 — ESCOPO -->
<div class="page">
  <div class="eyebrow">O que será executado</div>
  <div class="section-h serif">Três ambientes, um acabamento só</div>
  <hr class="rule">
  <p class="lead">Todo o conjunto em MDF Azul Petróleo Guararapes, com o rigor de leitura do seu projeto — cada cota conferida peça a peça.</p>

  <div class="amb">
    <div class="im" style="background-image:url('{IMG_DESP}');"></div>
    <div class="tx">
      <div class="nm">Despensa</div>
      <div class="sub">Armário superior + bancada em “L”</div>
      <ul>
        <li>Armário superior (163 × 247 cm) revestido em Azul Petróleo: novas frentes de giro, laterais aparentes, 4 prateleiras e coluna-nicho com 2 pistões a gás.</li>
        <li>Bancada inferior em “L” (154 cm) com 2 gavetões, nichos e coluna de <b>3 cestos aramados</b> para frutas e legumes.</li>
        <li>Perfil de LED de embutir <b>3000 K</b> centralizado.</li>
      </ul>
    </div>
  </div>

  <div class="amb">
    <div class="im" style="background-image:url('{IMG_LAV}');"></div>
    <div class="tx">
      <div class="nm">Lavanderia</div>
      <div class="sub">Torre da máquina de lavar</div>
      <ul>
        <li>Torre (84 × 152 × 67 cm) com vão embutido para a máquina e bancada de apoio.</li>
        <li>Gaveteiro para produtos de limpeza, gavetão para roupas e apoio extraível.</li>
        <li>Puxador em cava/perfil passante, sem ferragem aparente.</li>
      </ul>
    </div>
  </div>

  <div class="amb">
    <div class="im" style="background-image:url('{IMG_TAN}');"></div>
    <div class="tx">
      <div class="nm">Armário-tanque</div>
      <div class="sub">Balcão de apoio</div>
      <ul>
        <li>Balcão (50 × 65 × 48 cm) com 2 portas de giro, base para o tanque e prateleira interna.</li>
        <li>Preparado para receber tampo de pedra e cuba (fornecidos pelo marmorista).</li>
      </ul>
    </div>
  </div>

  <div class="note">
    <div class="h">Premissas &amp; itens não inclusos</div>
    Projeto <b>integralmente em MDF Azul Petróleo Guararapes</b> — inclusive caixaria e fundos. O armário superior da despensa é <b>revestido sobre a estrutura existente</b>. <b>Não inclusos:</b> tampos de pedra e cuba/inox (marmorista), máquina de lavar e pontos hidráulicos/elétricos de alimentação.
  </div>
  <div class="pfoot"><span class="brandline">valvic<span class="dot">.</span> marcenaria</span><span>Proposta Graça · Projeto Lais Teles</span></div>
</div>

<!-- PAGE 3 — INVESTIMENTO + CONDICOES -->
<div class="page">
  <div class="eyebrow">Investimento</div>
  <div class="section-h serif">Duas linhas, a mesma marcenaria</div>
  <hr class="rule">
  <p class="lead">O que muda entre as linhas é o <b>sistema de ferragens</b> — e, com ele, a garantia.</p>

  <div class="lines">
    <div class="lineC">
      <div class="tag">Linha Essencial</div>
      <div class="nm serif">Essencial</div>
      <div class="warr">Garantia de 2 anos</div>
      <div class="price serif">R$ 20.100</div>
      <div class="plab">Investimento total</div>
      <ul>
        <li>Corrediças telescópicas com amortecimento.</li>
        <li>Dobradiças com amortecimento (fechamento suave).</li>
        <li>Projeto integral em Azul Petróleo, inclusive a caixaria.</li>
      </ul>
    </div>
    <div class="lineC prem">
      <div class="recom">Recomendada</div>
      <div class="tag">Linha Essencial Prime</div>
      <div class="nm serif">Essencial Prime</div>
      <div class="warr">Garantia de 5 anos</div>
      <div class="price serif">R$ 24.000</div>
      <div class="plab">Investimento total</div>
      <ul>
        <li>Corrediças <b>ocultas</b> de engenharia alemã, com fechamento suave.</li>
        <li>Dobradiças alemãs de alta durabilidade.</li>
        <li>Mais suavidade de uso e vida útil — a mesma peça, elevada.</li>
      </ul>
    </div>
  </div>

  <table>
    <thead><tr><th>Ambiente</th><th class="r">Essencial</th><th class="r prem-col">Essencial Prime</th></tr></thead>
    <tbody>
      <tr><td class="amb-name">Despensa</td><td class="r">R$ 12.900</td><td class="r prem-col">R$ 15.400</td></tr>
      <tr><td class="amb-name">Lavanderia</td><td class="r">R$ 5.900</td><td class="r prem-col">R$ 7.000</td></tr>
      <tr><td class="amb-name">Armário-tanque</td><td class="r">R$ 1.300</td><td class="r prem-col">R$ 1.600</td></tr>
    </tbody>
  </table>
  <div class="tcap">Detalhamento por ambiente · o total de cada linha é o investimento indicado acima.</div>

  <div class="split">
    <div>
      <h3 class="blk">Condições de pagamento</h3>
      <div class="hrule"></div>
      <ul class="pay">
        <li><b>30%</b> de entrada + saldo em até <b>10× no cartão</b></li>
        <li><b>50%</b> de entrada + saldo em 8× — <b>3% de desconto</b></li>
        <li><b>70%</b> de entrada + saldo em 6× — <b>5% de desconto</b></li>
        <li><b>70%</b> de entrada + transferência — <b>7% de desconto</b></li>
      </ul>
    </div>
    <div>
      <h3 class="blk">Prazo &amp; garantia</h3>
      <div class="hrule"></div>
      <div class="terms">
        <div class="term"><div class="t">Entrega</div><div class="b">60 a 90<br>dias corridos</div></div>
        <div class="term"><div class="t">Garantia</div><div class="b">2 a 5<br>anos</div></div>
      </div>
      <p style="font-size:8.4pt;color:var(--ink-soft);margin-top:3.5mm;">A partir da aprovação do executivo. Instalação e assistência por equipe própria Valvic.</p>
    </div>
  </div>

  <div class="pfoot"><span class="brandline">valvic<span class="dot">.</span> marcenaria</span><span>Proposta Graça · Projeto Lais Teles · 16/07/2026</span></div>
</div>

</body></html>"""
(P/'proposta-graca.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-graca.html', len(HTML), 'chars')
