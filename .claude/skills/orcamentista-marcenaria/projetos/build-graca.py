# -*- coding: utf-8 -*-
# Monta a proposta Graca (3 paginas, formato enxuto). Imagens do cliente embutidas em base64.
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
:root{{--gold:#B8901E;--gold-soft:#D9B25A;--gold-deep:#8f6410;--ink:#191512;--ink-soft:#4a463f;
--cream:#FBF5E9;--cream-2:#F3E8CE;--line:#E4D8B8;--line-soft:#EDE4D2;--paper:#fff;--petrol:#294351;--petrol-d:#1e323d;}}
@page{{size:A4;margin:0;}}
*{{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}}
body{{margin:0;font-family:'DM Sans','Liberation Sans',Arial,sans-serif;color:var(--ink);font-size:10.5pt;line-height:1.62;}}
.serif{{font-family:'Cormorant Garamond','Georgia',serif;}}
.page{{position:relative;width:210mm;min-height:297mm;padding:16mm 18mm;page-break-after:always;overflow:hidden;background:var(--paper);}}
.page:last-child{{page-break-after:auto;}}
h1,h2,h3{{margin:0;font-weight:600;}}
p{{margin:8px 0;}}
.eyebrow{{letter-spacing:.32em;text-transform:uppercase;font-size:8pt;font-weight:700;color:var(--gold-deep);}}
.rule{{height:2px;width:54px;background:var(--gold);border:0;margin:12px 0;}}
.section-h{{font-family:'Cormorant Garamond','Georgia',serif;font-size:24pt;font-weight:700;color:var(--ink);line-height:1.1;margin-top:4px;}}
.lead{{font-family:'Cormorant Garamond','Georgia',serif;font-size:13.5pt;font-style:italic;color:var(--ink-soft);line-height:1.5;}}
.pfoot{{position:absolute;left:18mm;right:18mm;bottom:11mm;display:flex;justify-content:space-between;font-size:7.6pt;color:#9a9080;letter-spacing:.12em;border-top:1px solid var(--line);padding-top:3mm;}}
.brandline{{font-family:'Cormorant Garamond','Georgia',serif;font-weight:700;letter-spacing:.12em;}}.brandline .dot{{color:var(--gold);}}

/* ---------- CAPA ---------- */
.cover{{padding:0;background:var(--cream);}}
.cover .frame{{position:absolute;inset:9mm;border:1px solid var(--gold-soft);pointer-events:none;}}
.cover .inner{{position:relative;padding:19mm 18mm 15mm;height:297mm;display:flex;flex-direction:column;}}
.brand{{font-family:'Cormorant Garamond','Georgia',serif;font-size:29pt;font-weight:700;letter-spacing:.18em;color:var(--ink);}}
.brand .dot{{color:var(--gold);}}
.brand-sub{{letter-spacing:.5em;font-size:8pt;font-weight:700;color:var(--gold-deep);margin-top:2px;}}
.heroimg{{width:100%;height:120mm;margin:8mm 0 7mm;border-radius:3px;background:var(--petrol) center/cover no-repeat;box-shadow:0 14px 34px rgba(30,50,61,.30);}}
.cover .cap{{letter-spacing:.2em;text-transform:uppercase;font-size:7.4pt;color:var(--gold-deep);font-weight:700;margin-bottom:8mm;}}
.cover .for{{letter-spacing:.34em;text-transform:uppercase;font-size:9pt;font-weight:700;color:var(--gold-deep);}}
.cover .client{{font-family:'Cormorant Garamond','Georgia',serif;font-size:36pt;font-weight:700;line-height:1.05;margin:3px 0 3px;color:var(--ink);}}
.cover .proj{{font-family:'Cormorant Garamond','Georgia',serif;font-style:italic;font-size:15pt;color:var(--ink-soft);}}
.cover .foot{{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;font-size:8.5pt;color:var(--ink-soft);letter-spacing:.06em;}}
.sparkles{{font-size:12pt;color:var(--gold);letter-spacing:.4em;margin-bottom:3mm;}}

/* ---------- ESCOPO ---------- */
.amb{{display:flex;gap:6mm;align-items:stretch;margin-top:6mm;}}
.amb .im{{width:52mm;flex:none;border:1px solid var(--line);border-radius:4px;background:var(--petrol) center/cover no-repeat;}}
.amb .tx{{flex:1;}}
.amb .nm{{font-family:'Cormorant Garamond','Georgia',serif;font-size:16.5pt;font-weight:700;color:var(--ink);line-height:1.05;}}
.amb .sub{{font-size:8.2pt;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-deep);font-weight:700;margin-top:1mm;}}
.amb ul{{margin:2.5mm 0 0;padding-left:4.6mm;font-size:9.2pt;color:var(--ink-soft);}}
.amb li{{margin:1.5mm 0;}}
.note{{margin-top:7mm;background:var(--cream);border:1px solid var(--line);border-left:3px solid var(--gold);border-radius:3px;padding:4.5mm 5.5mm;font-size:8.7pt;color:var(--ink-soft);}}
.note b{{color:var(--ink);}}
.note .h{{font-size:7.6pt;letter-spacing:.16em;text-transform:uppercase;color:var(--gold-deep);font-weight:700;margin-bottom:2mm;}}

/* ---------- INVESTIMENTO ---------- */
.lines{{display:flex;gap:6mm;margin-top:4mm;}}
.lineC{{flex:1;border:1px solid var(--line);border-radius:5px;padding:5mm;background:var(--paper);}}
.lineC.prem{{background:var(--petrol);color:var(--cream);border-color:var(--petrol);}}
.lineC .tag{{letter-spacing:.2em;text-transform:uppercase;font-size:7.6pt;font-weight:700;color:var(--gold-deep);}}
.lineC.prem .tag{{color:var(--gold-soft);}}
.lineC .nm{{font-family:'Cormorant Garamond','Georgia',serif;font-size:20pt;font-weight:700;margin:2px 0 1mm;}}
.lineC.prem .nm{{color:#fff;}}
.lineC .warr{{font-family:'Cormorant Garamond','Georgia',serif;font-size:14.5pt;font-weight:700;color:var(--gold-deep);}}
.lineC.prem .warr{{color:var(--gold-soft);}}
.lineC .price{{font-family:'Cormorant Garamond','Georgia',serif;font-size:24pt;font-weight:700;margin-top:2mm;line-height:1;}}
.lineC.prem .price{{color:#fff;}}
.lineC ul{{margin:3mm 0 0;padding-left:5mm;font-size:8.9pt;color:var(--ink-soft);}}
.lineC.prem ul{{color:#e9e1cd;}}
.lineC li{{margin:1.6mm 0;}}

table{{width:100%;border-collapse:collapse;margin:4mm 0 2mm;font-size:9.4pt;}}
th,td{{padding:1.6mm 4mm;text-align:left;border-bottom:1px solid var(--line-soft);}}
thead th{{background:var(--ink);color:var(--cream);font-size:7.6pt;letter-spacing:.12em;text-transform:uppercase;font-weight:700;border:0;}}
td.r,th.r{{text-align:right;font-variant-numeric:tabular-nums;}}
.amb-name{{font-weight:600;}}
.grand td{{background:var(--gold);color:#1a1a1a;font-weight:700;font-size:10.5pt;border:0;}}
.grand .serif{{font-size:12.5pt;}}
.prem-col{{background:var(--cream-2);}}

.terms{{display:flex;gap:5mm;margin-top:5mm;flex-wrap:wrap;}}
.term{{flex:1;min-width:34mm;background:var(--cream);border:1px solid var(--line);border-radius:3px;padding:4mm;text-align:center;}}
.term .t{{font-size:7.2pt;letter-spacing:.16em;text-transform:uppercase;color:var(--gold-deep);font-weight:700;}}
.term .b{{font-family:'Cormorant Garamond','Georgia',serif;font-size:13.5pt;font-weight:700;margin-top:3px;line-height:1.1;}}
.pay{{margin:3mm 0 0;padding-left:5mm;}}.pay li{{margin:1.7mm 0;font-size:9.2pt;color:var(--ink-soft);}}
.pay b{{color:var(--ink);}}
.close{{background:var(--ink);color:var(--cream);border-radius:5px;padding:5.5mm 8mm;margin-top:4mm;}}
.close .serif{{color:#fff;font-size:15pt;}}.close p{{color:#e9e1cd;margin:3px 0 0;font-size:9.2pt;}}
.split{{display:flex;gap:8mm;}}.split>div{{flex:1;}}
h3.blk{{font-family:'Cormorant Garamond','Georgia',serif;font-size:13.5pt;color:var(--ink);margin-top:5mm;}}
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
    Projeto <b>integralmente em MDF Azul Petróleo Guararapes</b> — inclusive caixaria interna e fundos (sem branco). O armário superior da despensa é <b>revestido sobre a estrutura existente</b> (não inclui refazer a caixa). <b>Não inclusos:</b> tampos de pedra e cuba/inox (bancada da despensa e armário-tanque, por conta do marmorista), máquina de lavar (eletrodoméstico do cliente) e pontos hidráulicos/elétricos de alimentação. Medidas a conferir no local, conforme nota do projeto.
  </div>
  <div class="pfoot"><span class="brandline">valvic<span class="dot">.</span> marcenaria</span><span>Proposta Graça · Projeto Lais Teles</span></div>
</div>

<!-- PAGE 3 — INVESTIMENTO + CONDICOES -->
<div class="page">
  <div class="eyebrow">Investimento</div>
  <div class="section-h serif">Duas linhas, a mesma marcenaria</div>
  <hr class="rule">
  <p class="lead">A construção, o acabamento e o desenho são idênticos. O que muda é o <b>sistema de ferragens</b> — e, com ele, a garantia.</p>

  <div class="lines">
    <div class="lineC">
      <div class="tag">Linha Essencial</div>
      <div class="nm serif">Essencial</div>
      <div class="warr">Garantia de 2 anos</div>
      <div class="price serif">R$ 20.100</div>
      <ul>
        <li>Corrediças telescópicas com amortecimento.</li>
        <li>Dobradiças com amortecimento (fechamento suave).</li>
        <li>Projeto integral em Azul Petróleo, inclusive a caixaria.</li>
      </ul>
    </div>
    <div class="lineC prem">
      <div class="tag">Linha Essencial Prime</div>
      <div class="nm serif">Essencial Prime</div>
      <div class="warr">Garantia de 5 anos</div>
      <div class="price serif">R$ 20.800</div>
      <ul>
        <li>Corrediças <b>ocultas</b> de engenharia alemã, com amortecimento e fechamento suave.</li>
        <li>Dobradiças alemãs de alta durabilidade.</li>
        <li>Maior suavidade de uso e vida útil — a mesma peça, elevada.</li>
      </ul>
    </div>
  </div>

  <table>
    <thead><tr><th>Ambiente</th><th class="r">Essencial</th><th class="r prem-col">Essencial Prime</th></tr></thead>
    <tbody>
      <tr><td class="amb-name">Despensa</td><td class="r">R$ 12.900</td><td class="r prem-col">R$ 13.400</td></tr>
      <tr><td class="amb-name">Lavanderia</td><td class="r">R$ 5.900</td><td class="r prem-col">R$ 6.100</td></tr>
      <tr><td class="amb-name">Armário-tanque</td><td class="r">R$ 1.300</td><td class="r prem-col">R$ 1.300</td></tr>
    </tbody>
    <tfoot><tr class="grand"><td class="serif">Investimento total</td><td class="r serif">R$ 20.100</td><td class="r serif">R$ 20.800</td></tr></tfoot>
  </table>

  <div class="split">
    <div>
      <h3 class="blk">Condições de pagamento</h3>
      <ul class="pay">
        <li><b>30%</b> de entrada + saldo em até <b>10× no cartão</b></li>
        <li><b>50%</b> de entrada + saldo em até 8× — <b>3% de desconto</b></li>
        <li><b>70%</b> de entrada + saldo em até 6× — <b>5% de desconto</b></li>
        <li><b>70%</b> de entrada + saldo por transferência — <b>7% de desconto</b></li>
      </ul>
    </div>
    <div>
      <h3 class="blk">Prazo &amp; garantia</h3>
      <div class="terms" style="margin-top:2mm;">
        <div class="term"><div class="t">Entrega</div><div class="b">60 a 90<br>dias corridos</div></div>
        <div class="term"><div class="t">Garantia</div><div class="b">2 a 5<br>anos</div></div>
      </div>
      <p style="font-size:8.4pt;color:var(--ink-soft);margin-top:3mm;">Prazo a partir da aprovação do executivo e definição de acabamentos. Instalação e assistência por equipe própria Valvic.</p>
    </div>
  </div>

  <div class="close">
    <div class="serif">Uma marcenaria que começa no desenho e termina no encaixe.</div>
    <p>Seguimos com o projeto executivo assim que você escolher a linha. Qualquer ajuste de escopo é revisto com você antes de produzir — nada entra em corte sem a sua aprovação.</p>
  </div>
  <div class="pfoot"><span class="brandline">valvic<span class="dot">.</span> marcenaria</span><span>Proposta Graça · Projeto Lais Teles · 16/07/2026</span></div>
</div>

</body></html>"""
(P/'proposta-graca.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-graca.html', len(HTML), 'chars')
