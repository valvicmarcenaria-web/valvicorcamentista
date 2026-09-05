# -*- coding: utf-8 -*-
# Proposta Porto Verde (Leonardo) — comercial, config única. Base visual: build-lm.py.
# Peças interpretadas a partir da referência visual enviada pelo cliente (sem projeto executivo).
import pathlib
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')

HTML = """<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8">
<style>
:root{--gold:#B8901E;--gold-soft:#D9B25A;--gold-deep:#9A6E12;--ink:#211a12;--ink-soft:#5c5344;--mut:#8b8172;
--cream:#FCF8F0;--line:#EAE0CB;--line-soft:#F0E9D9;--paper:#fff;--petrol:#2C4A5A;--petrol-tint:#F5F8F8;--petrol-line:#CBD7DB;}
@page{size:A4;margin:0;}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{margin:0;font-family:'DM Sans','Liberation Sans',Arial,sans-serif;color:var(--ink);font-size:10.5pt;line-height:1.6;}
.serif{font-family:'Cormorant Garamond','Georgia',serif;}
.page{position:relative;width:210mm;height:297mm;padding:15mm 18mm 14mm;page-break-after:always;overflow:hidden;background:var(--paper);}
.page:last-child{page-break-after:auto;}
h1,h2,h3{margin:0;font-weight:600;}
p{margin:8px 0;}
.eyebrow{letter-spacing:.34em;text-transform:uppercase;font-size:8pt;font-weight:700;color:var(--gold-deep);}
.rule{height:1.5px;width:46px;background:var(--gold-soft);border:0;margin:11px 0 13px;}
.section-h{font-family:'Cormorant Garamond','Georgia',serif;font-size:23pt;font-weight:700;color:var(--ink);line-height:1.1;}
.lead{font-family:'Cormorant Garamond','Georgia',serif;font-size:13.5pt;font-style:italic;color:var(--ink-soft);line-height:1.5;max-width:160mm;}
.pfoot{position:absolute;left:18mm;right:18mm;bottom:12mm;display:flex;justify-content:space-between;font-size:7.4pt;color:var(--mut);letter-spacing:.13em;border-top:1px solid var(--line-soft);padding-top:3mm;}
.brandline{font-family:'Cormorant Garamond','Georgia',serif;font-weight:700;letter-spacing:.12em;}.brandline .dot{color:var(--gold);}

/* CAPA */
.cover{padding:0;background:var(--cream);}
.cover .frame{position:absolute;inset:10mm;border:1px solid var(--gold-soft);pointer-events:none;}
.cover .inner{position:relative;padding:28mm 20mm 16mm;height:297mm;}
.brand{font-family:'Cormorant Garamond','Georgia',serif;font-size:30pt;font-weight:700;letter-spacing:.2em;color:var(--ink);}
.brand .dot{color:var(--gold);}
.brand-sub{letter-spacing:.52em;font-size:7.6pt;font-weight:700;color:var(--gold-deep);margin-top:3px;}
.cover .kicker{margin-top:74mm;letter-spacing:.34em;text-transform:uppercase;font-size:8.6pt;font-weight:700;color:var(--gold-deep);}
.cover .client{font-family:'Cormorant Garamond','Georgia',serif;font-size:40pt;font-weight:700;line-height:1.02;margin:5px 0 4px;color:var(--ink);}
.cover .proj{font-family:'Cormorant Garamond','Georgia',serif;font-style:italic;font-size:15pt;color:var(--ink-soft);}
.cover .meta{margin-top:9mm;display:flex;gap:7mm;flex-wrap:wrap;}
.cover .meta .m{border-left:2px solid var(--gold-soft);padding-left:4mm;}
.cover .meta .t{font-size:7pt;letter-spacing:.16em;text-transform:uppercase;color:var(--gold-deep);font-weight:700;}
.cover .meta .v{font-family:'Cormorant Garamond','Georgia',serif;font-size:12.5pt;font-weight:700;color:var(--ink);}
.cover .foot{position:absolute;left:20mm;right:20mm;bottom:16mm;display:flex;justify-content:space-between;align-items:flex-end;font-size:8.4pt;color:var(--ink-soft);}
.sparkles{font-size:11pt;color:var(--gold-soft);letter-spacing:.45em;margin-bottom:3mm;}

/* ESCOPO */
.block{margin-top:6mm;padding-left:5mm;border-left:2px solid var(--gold-soft);}
.block .nm{font-family:'Cormorant Garamond','Georgia',serif;font-size:16.5pt;font-weight:700;color:var(--ink);}
.block .sub{font-size:8pt;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-deep);font-weight:700;margin-top:1mm;}
.block ul{margin:2.5mm 0 0;padding-left:4.6mm;font-size:9.3pt;color:var(--ink-soft);}
.block li{margin:1.6mm 0;}
.block b{color:var(--ink);}
.block .pv{font-family:'Cormorant Garamond','Georgia',serif;font-size:12pt;font-weight:700;color:var(--gold-deep);margin-top:2mm;}
.highlights{display:flex;gap:6mm;margin-top:8mm;}
.hl{flex:1;border-radius:6px;padding:4.5mm 5mm;}
.hl.perg{background:var(--petrol-tint);border:1px solid var(--petrol-line);}
.hl.port{background:#FBF3E1;border:1px solid var(--line);}
.hl .t{font-family:'Cormorant Garamond','Georgia',serif;font-size:13.5pt;font-weight:700;line-height:1.1;}
.hl.perg .t{color:var(--petrol);}
.hl.port .t{color:var(--gold-deep);}
.hl ul{margin:2.5mm 0 0;padding-left:4.4mm;font-size:8.5pt;color:var(--ink-soft);line-height:1.45;}
.hl li{margin:1.4mm 0;}
.hl b{color:var(--ink);}

/* INVESTIMENTO */
.hero{margin-top:6mm;border:1px solid var(--line);border-radius:8px;padding:7mm 8mm;position:relative;background:var(--paper);}
.hero::before{content:"";position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--gold-soft);border-radius:8px 0 0 8px;}
.hero .t{letter-spacing:.2em;text-transform:uppercase;font-size:8pt;font-weight:700;color:var(--gold-deep);}
.hero .big{font-family:'Cormorant Garamond','Georgia',serif;font-size:34pt;font-weight:700;color:var(--ink);line-height:1;margin:3mm 0 1mm;}
.hero .cap{font-size:9pt;color:var(--ink-soft);}
table{width:100%;border-collapse:collapse;margin:7mm 0 2mm;font-size:9.8pt;}
thead th{background:transparent;color:var(--ink-soft);font-size:7.4pt;letter-spacing:.16em;text-transform:uppercase;font-weight:700;border:0;border-bottom:1.5px solid var(--ink);padding:0 4mm 2.2mm;text-align:left;}
td{padding:2.4mm 4mm;border-bottom:1px solid var(--line-soft);}
td.r,th.r{text-align:right;font-variant-numeric:tabular-nums;}
.nmc{font-weight:600;color:var(--ink);}
.grand td{border:0;border-top:1.5px solid var(--gold);color:var(--ink);font-weight:700;font-size:11.5pt;padding-top:3mm;}
.grand .serif{font-size:14pt;}
.split{display:flex;gap:9mm;margin-top:6mm;}.split>div{flex:1;}
h3.blk{font-family:'Cormorant Garamond','Georgia',serif;font-size:13.5pt;color:var(--ink);margin-bottom:1mm;}
.hrule{height:1px;background:var(--line);margin:2.5mm 0 3mm;}
.pay{margin:2mm 0 0;padding-left:4.6mm;}.pay li{margin:1.6mm 0;font-size:9.3pt;color:var(--ink-soft);}.pay b{color:var(--ink);}
.terms{display:flex;gap:5mm;margin-top:3mm;}
.term{flex:1;border:1px solid var(--line);border-radius:4px;padding:3.4mm 3mm;text-align:center;}
.term .t{font-size:7pt;letter-spacing:.16em;text-transform:uppercase;color:var(--gold-deep);font-weight:700;}
.term .b{font-family:'Cormorant Garamond','Georgia',serif;font-size:13pt;font-weight:700;margin-top:3px;line-height:1.12;color:var(--ink);}
.note{margin-top:7mm;padding-left:5mm;border-left:2px solid var(--gold-soft);font-size:8.5pt;color:var(--ink-soft);line-height:1.55;}
.note b{color:var(--ink);}
.note .h{font-size:7.4pt;letter-spacing:.16em;text-transform:uppercase;color:var(--gold-deep);font-weight:700;margin-bottom:2mm;}
</style></head>
<body>

<!-- CAPA -->
<div class="page cover">
  <div class="frame"></div>
  <div class="inner">
    <div><div class="brand">valvic<span class="dot">.</span></div><div class="brand-sub">MARCENARIA</div></div>
    <div class="kicker">Proposta comercial</div>
    <div class="client">Leonardo</div>
    <div class="proj">Porto Verde — escritório comercial, 40 m²</div>
    <div class="meta">
      <div class="m"><div class="t">Escopo</div><div class="v">Parede destaque · Mesas · Escritório · Copa/Lavabo</div></div>
      <div class="m"><div class="t">Ferragens</div><div class="v">Hettich (Alemanha) · Garantia 10 anos</div></div>
    </div>
    <div class="foot">
      <div><span class="sparkles">&#10022; &#10022; &#10022;</span><br>Da referência que você nos mostrou ao projeto executável, peça por peça.</div>
      <div style="text-align:right">22 de julho de 2026<br>validade 10 dias</div>
    </div>
  </div>
</div>

<!-- ESCOPO I -->
<div class="page">
  <div class="eyebrow">Como chegamos até aqui</div>
  <div class="section-h serif">A imagem virou projeto.</div>
  <hr class="rule">
  <p class="lead">Você ainda não tem o projeto executivo do Porto Verde — tem a referência certa. A partir da imagem que você compartilhou, lemos cada parede, cada material, cada proporção do ambiente, e traduzimos em uma proposta de marcenaria executável: o que entendemos ser o mais adequado e interessante para o seu espaço, peça por peça.</p>

  <div class="block">
    <div class="nm">Parede de destaque</div>
    <div class="sub">Painéis piso-teto · iluminação embutida</div>
    <ul>
      <li>Revestimento contínuo em <b>painéis piso-teto</b>, com <b>iluminação de LED instalada</b> — o plano que emoldura o ambiente do chão ao forro.</li>
    </ul>
    <div class="pv">R$ 12.800</div>
  </div>

  <div class="block">
    <div class="nm">Mesas centrais</div>
    <div class="sub">Estações de trabalho · 5 postos</div>
    <ul>
      <li>Bancada para <b>5 estações de trabalho</b>, tampo em <b>MDF Ultra</b> (linha reforçada, maior resistência à umidade).</li>
      <li><b>Calha elétrica usinada na marcenaria</b>, com infraestrutura de <b>20 pontos de tomada 10A</b> já instalada — sem fiação aparente sobre a mesa.</li>
      <li>Estrutura em serralheria, acabamento em <b>pintura eletrostática</b>.</li>
    </ul>
    <div class="pv">R$ 9.500</div>
  </div>

  <div class="pfoot"><span class="brandline">valvic<span class="dot">.</span> marcenaria</span><span>Porto Verde · Leonardo</span></div>
</div>

<!-- ESCOPO II -->
<div class="page">
  <div class="eyebrow">Escopo da marcenaria</div>
  <div class="section-h serif">Escritório principal &amp; parede de apoio</div>
  <hr class="rule">

  <div class="block">
    <div class="nm">Escritório principal</div>
    <div class="sub">Painéis laterais · porta mimetizada · teto</div>
    <ul>
      <li>Fechamento em <b>painéis laterais</b> (direita e esquerda) e <b>teto decorativo</b> em marcenaria.</li>
      <li>O painel do lado direito integra uma <b>porta mimetizada</b> — acesso discreto, sem ferragem aparente, alinhado ao painel.</li>
    </ul>
    <div class="pv">R$ 12.000</div>
  </div>

  <div class="block">
    <div class="nm">Parede de apoio</div>
    <div class="sub">Copa · balcão · torre · estante · acesso ao lavabo</div>
    <ul>
      <li><b>Balcão de até 2,70 m</b>: tampo com prateleira aérea sobre suporte oculto e iluminação de LED instalada. Composição com até <b>4 gavetas</b>, portas com prateleiras internas e puxadores em cava.</li>
      <li><b>Teto decorativo</b> + <b>torre de até 90 cm</b> de largura, com prateleiras internas e portas com puxador em cava ou touch.</li>
      <li><b>Estante em serralheria</b> (pintura eletrostática) com prateleiras em MDF.</li>
      <li><b>Painel com porta mimetizada</b> de acesso ao lavabo — mesma lógica do escritório principal: sem ferragem aparente.</li>
    </ul>
    <div class="pv">R$ 28.100</div>
  </div>

  <div class="highlights">
    <div class="hl perg">
      <div class="t">Ferragens Hettich<br>engenharia alemã</div>
      <ul>
        <li>Corrediças e dobradiças <b>Hettich</b>, fabricadas na Alemanha — abertura macia, fechamento silencioso e resistência para uso comercial intenso.</li>
        <li><b>10 anos de garantia de fábrica</b> — o dobro do padrão do mercado.</li>
      </ul>
    </div>
    <div class="hl port">
      <div class="t">A marcenaria<br>que desaparece</div>
      <ul>
        <li><b>Duas portas mimetizadas</b> — escritório principal e acesso ao lavabo — sem puxador ou ferragem aparente, alinhadas ao painel.</li>
        <li>O acesso existe, mas só quem precisa sabe onde ele está.</li>
      </ul>
    </div>
  </div>

  <div class="pfoot"><span class="brandline">valvic<span class="dot">.</span> marcenaria</span><span>Porto Verde · Leonardo</span></div>
</div>

<!-- INVESTIMENTO -->
<div class="page">
  <div class="eyebrow">Investimento</div>
  <div class="section-h serif">Uma execução, do desenho ao encaixe</div>
  <hr class="rule">

  <div class="hero">
    <div class="t">Investimento total</div>
    <div class="big serif">R$ 62.400</div>
    <div class="cap">Parede de destaque + mesas centrais + escritório principal + parede de apoio, fornecimento e instalação por equipe própria Valvic.</div>
  </div>

  <table>
    <thead><tr><th>Frente</th><th class="r">Valor</th></tr></thead>
    <tbody>
      <tr><td class="nmc">Parede de destaque — painéis piso-teto com LED</td><td class="r">R$ 12.800</td></tr>
      <tr><td class="nmc">Mesas centrais — estações de trabalho (5 postos)</td><td class="r">R$ 9.500</td></tr>
      <tr><td class="nmc">Escritório principal — painéis + porta mimetizada + teto</td><td class="r">R$ 12.000</td></tr>
      <tr><td class="nmc">Parede de apoio — balcão + torre + estante + acesso lavabo</td><td class="r">R$ 28.100</td></tr>
    </tbody>
    <tfoot><tr class="grand"><td class="serif">Total</td><td class="r serif">R$ 62.400</td></tr></tfoot>
  </table>

  <div class="split">
    <div>
      <h3 class="blk">Condições de pagamento</h3>
      <div class="hrule"></div>
      <ul class="pay">
        <li><b>40%</b> de entrada (assinatura)</li>
        <li><b>60%</b> na entrega</li>
      </ul>
    </div>
    <div>
      <h3 class="blk">Prazo &amp; garantia</h3>
      <div class="hrule"></div>
      <div class="terms">
        <div class="term"><div class="t">Entrega</div><div class="b">35 a 45<br>dias úteis</div></div>
        <div class="term"><div class="t">Garantia</div><div class="b">10 anos<br><span style="font-size:8pt;font-family:'DM Sans',sans-serif;font-weight:400;color:var(--ink-soft);">ferragens Hettich</span></div></div>
      </div>
    </div>
  </div>

  <div class="note">
    <div class="h">Premissas &amp; não inclusos</div>
    Proposta elaborada a partir da <b>leitura visual da referência</b> compartilhada por Leonardo — sem projeto executivo formalizado. Medidas, quantidades e composições descritas são a <b>interpretação técnica Valvic</b> do que é mais adequado para o espaço, sujeitas a confirmação em vistoria e ajustadas em projeto executivo antes da produção. Ferragens <b>Hettich</b> (corrediças e dobradiças) em todos os módulos com gaveta/porta. <b>Não inclusos:</b> equipamentos (impressora, cafeteira, monitores, cadeiras), pontos elétricos/hidráulicos de alimentação e serviços de obra civil (gesso, pintura, alvenaria, vidro). Prazo a partir da aprovação do projeto executivo e liberação da frente de trabalho.
  </div>

  <div class="pfoot"><span class="brandline">valvic<span class="dot">.</span> marcenaria</span><span>Porto Verde · Leonardo · 22/07/2026</span></div>
</div>

</body></html>"""
(P/'proposta-porto-verde.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-porto-verde.html', len(HTML))
