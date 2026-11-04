# -*- coding: utf-8 -*-
"""PROPOSTA Lirriet — home office sob a escada. Formato ENXUTO, 2 páginas.
Capa+escopo · investimento+condições. Preços: corte-escada-lirriet.py
(2,60 m · sem ripado · melamínico tudo na cor · base de preços · MC 40%)."""
import pathlib
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')

MAIN = open('/tmp/uri_esc_main.txt').read()
DET  = open('/tmp/uri_esc_det.txt').read()
GAV  = open('/tmp/uri_esc_gav.txt').read()
CSS  = open('/tmp/css_premium.txt', encoding='utf-8').read().split('CSS = """')[1].rsplit('"""',1)[0]

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style>
<style>
  .page:last-of-type{{page-break-after:avoid; break-after:avoid;}}
  .pad{{padding:16mm 19mm 13mm;}}

  /* capa enxuta: faixa de imagem no topo, texto embaixo */
  .top-img{{margin:0 0 6mm; border-radius:6px; overflow:hidden;}}
  .top-img img{{width:100%; height:62mm; object-fit:cover; object-position:center 46%; display:block;}}
  .hd{{display:flex; justify-content:space-between; align-items:flex-end; margin-bottom:6mm;}}
  .hd .brand{{font-family:'Cormorant Garamond',Georgia,serif; font-size:17pt; font-weight:700;
      letter-spacing:.02em; color:var(--ink);}}
  .hd .brand .d{{color:var(--gold);}}
  .hd .brand small{{display:block; font-family:system-ui,sans-serif; font-size:6.6pt;
      letter-spacing:.3em; color:var(--mut); font-weight:700; margin-top:.6mm;}}
  .hd .meta{{text-align:right; font-size:7.6pt; color:var(--mut); line-height:1.6;}}
  .hd .meta b{{color:var(--ink);}}

  .esc{{margin-top:2mm;}}
  .esc .row{{display:grid; grid-template-columns:8mm 1fr; gap:0 4mm; padding:2.2mm 0;
      border-top:1px solid var(--hair);}}
  .esc .row:first-child{{border-top:2px solid var(--ink);}}
  .esc .n{{font-family:'Cormorant Garamond',Georgia,serif; font-size:12pt; font-weight:700;
      color:var(--gold); line-height:1.2;}}
  .esc .t{{font-size:9.4pt; font-weight:600; color:var(--ink); line-height:1.3;}}
  .esc .d{{font-size:8.2pt; color:var(--soft); line-height:1.5; margin-top:.8mm;}}
  .esc .d b{{color:var(--ink);}}

  .duo{{display:flex; gap:5mm; margin-top:4mm;}}
  .duo > div{{flex:1;}}
  .duo img{{width:100%; height:24mm; object-fit:cover; border-radius:5px; display:block;}}
  .duo .cap{{font-size:7pt; letter-spacing:.1em; text-transform:uppercase; color:var(--mut);
      margin-top:1.8mm;}}

  .inv{{background:var(--deep); border-radius:7px; padding:6mm 7mm; margin-top:2mm;
      position:relative; overflow:hidden; box-shadow:inset 0 0 0 1.5px rgba(201,169,106,.5);}}
  .inv .k{{font-size:6.8pt; letter-spacing:.2em; text-transform:uppercase; color:var(--gold-lt);
      font-weight:700;}}
  .inv .big{{font-family:'Cormorant Garamond',Georgia,serif; font-size:30pt; font-weight:700;
      color:#fff; line-height:1.05; margin-top:1.6mm;}}
  .inv .sub{{font-size:8.2pt; color:#C6BFB2; margin-top:1.6mm;}}
  .inv .sub b{{color:var(--gold-lt);}}

  .pay{{margin-top:5mm;}}
  .pay .r{{display:flex; justify-content:space-between; align-items:baseline;
      border-top:1px solid var(--line); padding:2.9mm 0; font-size:9pt; color:var(--soft);}}
  .pay .r:first-child{{border-top:2px solid var(--ink);}}
  .pay .r b{{color:var(--ink);}}
  .pay .v{{font-family:'Cormorant Garamond',Georgia,serif; font-size:13pt; font-weight:700;
      color:var(--ink);}}
  .pay .r.g .v{{color:var(--gold);}}
  .pay .r.g{{background:var(--gold-pale); margin:0 -3mm; padding:2.9mm 3mm;
      border-radius:4px; border-top-color:transparent;}}

  .cond{{display:grid; grid-template-columns:1fr 1fr; gap:3mm 7mm; margin-top:5mm;
      border-top:2px solid var(--ink); padding-top:3.5mm;}}
  .cond .k{{font-size:6.8pt; letter-spacing:.16em; text-transform:uppercase; color:var(--gold);
      font-weight:700;}}
  .cond .d{{font-size:8.4pt; color:var(--soft); line-height:1.5; margin-top:.7mm;}}
  .cond .d b{{color:var(--ink);}}
  .obs{{margin-top:4.5mm; padding-left:4mm; border-left:2px solid var(--gold-lt);
      font-size:7.6pt; color:var(--soft); line-height:1.6;}}
  .obs b{{color:var(--ink);}}
</style></head><body>

<!-- ══════ 1. CAPA + ESCOPO ══════ -->
<div class="page"><div class="pad">
  <div class="hd">
    <div class="brand">valvic<span class="d">.</span><small>MARCENARIA</small></div>
    <div class="meta">Proposta de marcenaria sob medida<br>
      <b>Lirriet Libório</b> · 31 de julho de 2026</div>
  </div>

  <div class="top-img"><img src="{MAIN}" alt=""></div>
  <div class="cap" style="margin-top:-5mm;margin-bottom:6mm;">Imagem de referência enviada pela cliente</div>

  <div class="h-sec serif" style="font-size:21pt;">Home office<br><em>sob a escada.</em></div>
  <hr class="rule" style="margin:8px 0 9px;">
  <p class="lead">Aproveitamento integral do vão da escada: <b>2,60 m de bancada</b>,
  prateleiras iluminadas e gaveteiro, tudo em <b>MDF melamínico na cor</b> — por fora
  e por dentro.</p>

  <div class="esc">
    <div class="row"><div class="n">01</div><div>
      <div class="t">Painel de fundo revestido</div>
      <div class="d">Todo o fundo em melamínico, acompanhando a <b>diagonal da escada</b> —
      é o que transforma o vão em ambiente e some com a parede crua.</div></div></div>
    <div class="row"><div class="n">02</div><div>
      <div class="t">Bancada de trabalho · 2,60 × 0,55 m</div>
      <div class="d">Altura de 75 cm, com <b>engrossamento de borda</b> na frente — o tampo
      ganha espessura aparente e não parece uma chapa fina apoiada.</div></div></div>
    <div class="row"><div class="n">03</div><div>
      <div class="t">Gaveteiro de 3 gavetas</div>
      <div class="d">Corrediças <b>ocultas com amortecimento</b> e <b>puxador em cava
      usinada</b> na própria frente — sem ferragem aparente.</div></div></div>
    <div class="row"><div class="n">04</div><div>
      <div class="t">Duas prateleiras escalonadas</div>
      <div class="d">Acompanham a inclinação da escada, com <b>fita de LED embutida em cava</b>
      na face inferior de cada uma: a luz aparece, a fita não.</div></div></div>
    <div class="row"><div class="n">05</div><div>
      <div class="t">Iluminação · 4,6 m de LED</div>
      <div class="d">Três linhas contínuas — sob cada prateleira e <b>sob a bancada</b>,
      que é a que faz o móvel flutuar à noite.</div></div></div>
    <div class="row"><div class="n">06</div><div>
      <div class="t">Painel frontal e lateral de fechamento</div>
      <div class="d">Fecham o vão sob a bancada e o encontro com a porta — o móvel termina
      resolvido, sem vão aberto nem tomada à mostra.</div></div></div>
  </div>

  <div class="duo">
    <div><img src="{DET}" alt=""><div class="cap">Prateleiras · LED embutido em cava</div></div>
    <div><img src="{GAV}" alt=""><div class="cap">Bancada · iluminação indireta</div></div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Home office sob a escada</span></div>
</div></div>

<!-- ══════ 2. INVESTIMENTO + CONDIÇÕES ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="h-sec serif" style="font-size:23pt;">O que está<br><em>incluído.</em></div>
  <hr class="rule" style="margin:8px 0 9px;">
  <p class="lead" style="margin-bottom:5mm;">Projeto executivo, fabricação, entrega e
  instalação — o móvel completo, pronto para usar.</p>

  <div class="inv">
    <div class="k">Investimento · valor de tabela</div>
    <div class="big">R$ 10.700</div>
    <div class="sub">Entrada de 30% + até 10× no cartão &nbsp;·&nbsp;
      <b>R$ 9.600 à vista</b></div>
  </div>

  <div class="pay">
    <div class="r"><span>Entrada 30% + até 10× no cartão</span>
      <span><b>valor de tabela</b> &nbsp; <span class="v">R$ 10.700</span></span></div>
    <div class="r"><span>Entrada 50% + até 8× no cartão &nbsp;<b>−4%</b></span>
      <span class="v">R$ 10.300</span></div>
    <div class="r"><span>Entrada 70% + até 6× no cartão &nbsp;<b>−7%</b></span>
      <span class="v">R$ 9.900</span></div>
    <div class="r g"><span><b>À vista / transferência</b> &nbsp;<b>−10%</b></span>
      <span class="v">R$ 9.600</span></div>
  </div>

  <div class="cond">
    <div><div class="k">Material</div><div class="d">MDF <b>melamínico fosco</b> 15 mm na
      estrutura e nas frentes · 6 mm nos fundos. <b>Tudo na cor</b> — inclusive a caixaria
      e o interior das gavetas.</div></div>
    <div><div class="k">Ferragens</div><div class="d">Corrediças <b>ocultas com
      amortecimento</b> nas 3 gavetas · puxador em <b>cava usinada</b>, sem ferragem
      aparente.</div></div>
    <div><div class="k">Iluminação</div><div class="d"><b>4,6 m</b> de LED em perfil,
      embutido em cava na marcenaria. Ligação ao ponto de energia existente.</div></div>
    <div><div class="k">Garantia</div><div class="d"><b>10 anos</b> em contrato sobre
      estrutura, montagem e acabamento · <b>2 anos</b> de instalação e regulagem.</div></div>
    <div><div class="k">Prazo</div><div class="d"><b>35 a 45 dias corridos</b> após a
      aprovação e a medição final no local.</div></div>
    <div><div class="k">Validade</div><div class="d"><b>15 dias corridos</b> a partir
      desta data.</div></div>
  </div>

  <div class="obs">
    <b>Medição:</b> este valor considera <b>2,60 m</b> de largura total. A medição no local
    é feita antes do corte e, se o vão for diferente, o valor é ajustado e reapresentado
    antes de qualquer produção — nada é cortado sem a sua confirmação.<br>
    <b>Não incluso:</b> cadeira, objetos de decoração, plantas · pintura das paredes ·
    pontos elétricos novos · tomada e infraestrutura de energia.
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Lirriet Libório · 31/07/2026</span></div>
</div></div>

</body></html>"""

(P/'proposta-escada-lirriet.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-escada-lirriet.html', len(HTML))
