# -*- coding: utf-8 -*-
"""COZINHA (projeto Rizzi Interiores) — V3 · layout do orçamento da Juliana.

[Jonathan 07/08] "faça do mesmo layout do orçamento da juliana · margem 32%".

O layout da Juliana é TIPOGRÁFICO — capa escura com numeral translúcido, blocos
.amb4, tabela .dual, escada .pay-tb2, grade .cnd. Não depende de render nenhum,
que é o que resolve: os renders do projeto nunca chegaram como arquivo.

MC 32% · COM RT (10% do líquido) · Hardt → divisor 0,39216
  bancada inferior  R$  5.501,35 → R$ 14.000
  demais móveis     R$ 10.220,14 → R$ 26.100
  TOTAL             R$ 15.721,49 → R$ 40.100   (MC conferida 32,0%)

A +2 pontos a escada volta INTEIRA: o −7% cai em 29,1%, acima do piso de 28%.
A 30% ela tinha de ser truncada em −3%.
"""
import pathlib
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')
CSS = open('/tmp/css_premium.txt', encoding='utf-8').read().split('CSS = """')[1].rsplit('"""', 1)[0]

TOT, BANC, DEMAIS, SEM_BANC = 40100, 14000, 26100, 28000
def br(v): return f'{v:,.0f}'.replace(',', '.')

MOVEIS = [
 ('Armário de bancada', 'Azul Ardósia',
  '<b>77 × 272 × 60 cm</b> — módulo da pia com báscula e gavetão, dois módulos de gavetas '
  'e módulo de portas de giro. Todas as frentes <b>em cava</b>.'),
 ('Armário de bancada', 'Azul Ardósia',
  '<b>77 × 150 × 60 cm</b> — fecha o “L” com quatro gavetas e duas portas de giro. '
  'Sóculo recuado de 10 cm, como o projeto define.'),
 ('Nicho', 'Freijó',
  '<b>110 × 150 cm</b> — o volume que reveste o vão entre a bancada e o aéreo, com '
  'prateleira. É onde a madeira aparece na altura do olho.'),
 ('Aéreo de básculas', 'Freijó',
  '<b>40 × 147 × 45 cm</b> — três básculas em cava com articulador. Único volume a '
  '<b>45 cm</b> de profundidade: é o que fica na altura de trabalho.'),
 ('Aéreo', 'Azul Ardósia',
  '<b>70 × 150 × 60 cm</b> — três portas de giro em cava, com prateleira interna. '
  'Profundidade cheia, onde o alcance já não atrapalha.'),
 ('Torre quente', 'Cinza Urban',
  '<b>270 × 70 × 60 cm</b>, do piso ao teto — duas básculas, gavetas, vãos para os '
  'embutidos e <b>tomadas embutidas na lateral esquerda</b>, conforme o projeto.'),
 ('Aéreo da geladeira', 'Cinza Urban',
  '<b>70 × 80 × 60 cm</b> — duas portas de giro em cava, fechando o vão acima do '
  'eletrodoméstico e alinhando o topo com o resto da parede.'),
 ('Painel ripado', 'Freijó',
  'Ripas em freijó integrando a cozinha à sala de jantar. É o item que faz os dois '
  'ambientes lerem como um só.'),
 ('Mesa', 'Freijó',
  'Tampo em freijó com apoio na lateral esquerda, conforme o projeto.'),
]
tb_moveis = ''.join(
  f'<tr><td class="sv">{n}<small>{c}</small></td><td class="ds">{d}</td></tr>'
  for n, c, d in MOVEIS)

ESCADA = [('Entrada 30% + saldo em até 10× no cartão', 0.00, 'valor de tabela'),
          ('Entrada 50% + saldo em até 8× no cartão',  0.03, '−3%'),
          ('Entrada 70% + saldo em até 6× no cartão',  0.05, '−5%'),
          ('Entrada 70% + saldo via transferência',    0.07, '−7%')]
def _best(d): return ' class="best"' if d == 0.07 else ''
esc = ''.join(
  f'<tr{_best(d)}><td>{n}</td><td class="r">{r}</td>'
  f'<td class="r alt">R$ {br(round(TOT*(1-d)/100)*100)}</td></tr>' for n, d, r in ESCADA)

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style>
<style>
  .page:last-of-type{{page-break-after:avoid; break-after:avoid;}}

  .cover-t{{background:var(--deep); position:relative; overflow:hidden;}}
  .cover-t::before{{content:""; position:absolute; inset:0;
     background:radial-gradient(120% 80% at 18% 12%, rgba(201,169,106,.16) 0%, transparent 58%),
                radial-gradient(90% 70% at 88% 96%, rgba(201,169,106,.10) 0%, transparent 60%);}}
  .cover-t .rules{{position:absolute; inset:0;
     background:repeating-linear-gradient(90deg, rgba(255,255,255,.030) 0 1px, transparent 1px 34mm);}}
  .cover-t .v2{{position:absolute; top:34mm; right:20mm; font-family:'Cormorant Garamond',Georgia,serif;
     font-size:96pt; font-weight:700; color:rgba(201,169,106,.16); line-height:1;}}

  .amb4{{border-top:1px solid var(--hair); padding:6.4mm 0;}}
  .amb4:first-child{{border-top:2px solid var(--ink);}}
  .amb4 .hd{{display:flex; justify-content:space-between; align-items:baseline;}}
  .amb4 .t{{font-family:'Cormorant Garamond',Georgia,serif; font-size:19pt; font-weight:700; line-height:1.14;}}
  .amb4 .q{{font-size:6.4pt; letter-spacing:.16em; text-transform:uppercase; color:var(--gold);
      font-weight:700; white-space:nowrap; padding-left:5mm;}}
  .amb4 .d{{font-size:9.8pt; color:var(--soft); line-height:1.66; margin-top:2mm;}}
  .amb4 .d b{{color:var(--ink);}}

  .dual{{width:100%; border-collapse:collapse; font-size:8.6pt; margin-top:3mm;}}
  .dual th{{font-size:6.4pt; letter-spacing:.14em; text-transform:uppercase; color:var(--mut);
      font-weight:700; border-bottom:1.5px solid var(--ink); padding:0 0 2mm; text-align:left;
      vertical-align:bottom;}}
  .dual th.vh{{text-align:right; width:30mm; padding-left:3mm; color:var(--gold);}}
  .dual td{{padding:2.1mm 0; border-bottom:1px solid var(--hair); vertical-align:top;}}
  .dual td.sv{{width:38mm; font-weight:700; color:var(--ink); font-size:9pt; padding-right:3mm;}}
  .dual td.sv small{{display:block; font-weight:700; color:var(--gold); font-size:6.6pt;
      letter-spacing:.13em; text-transform:uppercase; margin-top:.5mm;}}
  .dual td.ds{{color:var(--soft); line-height:1.56; padding-right:4mm;}}
  .dual td.vl{{text-align:right; white-space:nowrap; font-weight:700;
      font-variant-numeric:tabular-nums; padding-left:3mm; color:var(--gold);
      background:rgba(201,169,106,.07);}}
  .dual tr.tot td{{border-bottom:0; border-top:2px solid var(--ink); padding-top:3.4mm;
      font-family:'Cormorant Garamond',Georgia,serif; font-size:16pt;}}
  .dual tr.tot td.ds{{font-family:system-ui,sans-serif; font-size:8.6pt;}}

  .pay-tb2{{width:100%; border-collapse:collapse; font-size:9pt; margin-top:4mm;}}
  .pay-tb2 th{{font-size:6.4pt; letter-spacing:.14em; text-transform:uppercase; color:var(--mut);
      font-weight:700; border-bottom:1.5px solid var(--ink); padding:0 0 2mm; text-align:left;}}
  .pay-tb2 th.r, .pay-tb2 td.r{{text-align:right;}}
  .pay-tb2 td{{padding:2mm 0; border-bottom:1px solid var(--hair); font-variant-numeric:tabular-nums;}}
  .pay-tb2 td.r{{font-weight:700; white-space:nowrap; padding-left:4mm;}}
  .pay-tb2 td.r.alt{{color:var(--gold);}}
  .pay-tb2 tr.best td{{background:rgba(201,169,106,.12); border-bottom:0;}}
  .pay-tb2 tr.best td:first-child{{border-radius:4px 0 0 4px; font-weight:700;}}
  .pay-tb2 tr.best td:last-child{{border-radius:0 4px 4px 0;}}

  .same{{display:flex; gap:0; margin-top:7mm; border-top:2px solid var(--ink);
      border-bottom:1px solid var(--line); padding:6mm 0;}}
  .same > div{{flex:1; padding-left:6mm; border-left:1px solid var(--line);}}
  .same > div:first-child{{padding-left:0; border-left:0;}}
  .same .k{{font-size:6.4pt; letter-spacing:.16em; text-transform:uppercase; color:var(--gold); font-weight:700;}}
  .same .d{{font-size:9pt; color:var(--soft); line-height:1.6; margin-top:1.4mm;}}
  .same .d b{{color:var(--ink);}}

  .cnd{{display:grid; grid-template-columns:1fr 1fr; gap:4.4mm 8mm; margin-top:6mm;
      border-top:2px solid var(--ink); padding-top:4.4mm;}}
  .cnd .k{{font-size:6.4pt; letter-spacing:.16em; text-transform:uppercase; color:var(--gold); font-weight:700;}}
  .cnd .v{{font-size:9.4pt; color:var(--soft); line-height:1.55; margin-top:.8mm;}}
  .cnd .v b{{color:var(--ink);}}

  .cores{{display:flex; gap:7mm; margin-top:6mm;}}
  .cores .c{{flex:1; display:flex; align-items:center; gap:3.4mm;}}
  .cores .sw{{width:14mm; height:14mm; border-radius:3px; flex:none;
      box-shadow:inset 0 0 0 1px rgba(0,0,0,.14);}}
  .cores .n{{font-family:'Cormorant Garamond',Georgia,serif; font-size:13pt; font-weight:700; line-height:1.12;}}
  .cores .u{{font-size:6.8pt; letter-spacing:.13em; text-transform:uppercase; color:var(--mut);
      font-weight:700; margin-top:.8mm;}}
</style></head><body>

<!-- 1 · CAPA -->
<div class="page cover cover-t">
  <div class="rules"></div><div class="v2">09</div>
  <div class="inner">
    <div><div class="brand">valvic<span class="d">.</span></div><div class="bsub">MARCENARIA</div></div>
    <div class="mid">
      <div class="kick">Proposta de marcenaria</div>
      <div class="tit">Sua cozinha,<br>executada.</div>
      <div class="sub">Projeto Rizzi Interiores · nove móveis, três cores</div>
    </div>
    <div class="strip">
      <div class="c"><div class="k">Escopo</div><div class="v">9 móveis</div></div>
      <div class="c"><div class="k">Acabamento</div><div class="v">3 cores</div></div>
      <div class="c"><div class="k">Entrega</div><div class="v">60 dias corridos</div></div>
      <div class="c"><div class="k">Garantia</div><div class="v">10 anos</div></div>
    </div>
  </div>
</div>

<!-- 2 · O ESCOPO -->
<div class="page"><div class="pad">
  <div class="eyebrow">O escopo</div>
  <div class="h-sec serif" style="font-size:25pt;">Do desenho da Rizzi<br><em>para a bancada da fábrica.</em></div>
  <hr class="rule" style="margin:8px 0;">
  <p class="lead" style="margin-bottom:2mm;">O projeto já definiu cada móvel, cada cor e cada
  medida. O nosso trabalho é traduzir isso em chapa, ferragem e montagem — sem reinterpretar
  o que já foi decidido.</p>

  <div style="margin-top:2.5mm;">
    <div class="amb4"><div class="hd"><div class="t">A bancada em “L”</div>
      <div class="q">272 + 150 cm</div></div>
      <div class="d">Dois corpos em <b>Azul Ardósia</b> fechando o “L”: módulo da pia, dois
      bancos de gavetas e módulos de portas de giro. São <b>11 gavetas em corrediça oculta</b>
      com amortecimento, e sóculo recuado de 10 cm — a bancada fica exatamente nos <b>90 cm</b>
      que o projeto pede.</div></div>

    <div class="amb4"><div class="hd"><div class="t">O bloco em freijó</div>
      <div class="q">nicho + 3 básculas</div></div>
      <div class="d">Nicho de <b>110 cm</b> com prateleira e, acima dele, <b>três básculas</b>
      de 49 cm com articulador. É o único volume a <b>45 cm</b> de profundidade — o que fica na
      altura de trabalho recua, para não esbarrar em quem cozinha.</div></div>

    <div class="amb4"><div class="hd"><div class="t">Aéreos</div>
      <div class="q">150 + 80 cm</div></div>
      <div class="d">Três portas de giro em <b>Azul Ardósia</b> sobre o nicho, e duas em
      <b>Cinza Urban</b> fechando o vão da geladeira. Ambos a <b>60 cm</b> de profundidade:
      volume de guarda onde o alcance já não atrapalha.</div></div>

    <div class="amb4"><div class="hd"><div class="t">Torre quente</div>
      <div class="q">270 cm, piso ao teto</div></div>
      <div class="d">Em <b>Cinza Urban</b>, com duas básculas, gavetas, os vãos para os
      embutidos e <b>tomadas embutidas na lateral esquerda</b>, como o projeto especifica.</div></div>

    <div class="amb4"><div class="hd"><div class="t">Painel ripado e mesa</div>
      <div class="q">em freijó</div></div>
      <div class="d">As ripas e o tampo em <b>freijó</b>, com apoio na lateral esquerda. São os
      dois itens que fazem a cozinha e a sala de jantar lerem como um ambiente só.</div></div>
  </div>

  <div class="cores">
    <div class="c"><div class="sw" style="background:#5D7480;"></div>
      <div><div class="n">Azul Ardósia</div><div class="u">bancadas e aéreo</div></div></div>
    <div class="c"><div class="sw" style="background:#B08856;"></div>
      <div><div class="n">Freijó</div><div class="u">nicho · básculas · ripado</div></div></div>
    <div class="c"><div class="sw" style="background:#E4E0D8;"></div>
      <div><div class="n">Cinza Urban</div><div class="u">torre e aéreo da geladeira</div></div></div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span>
    <span>Cozinha · projeto Rizzi Interiores</span></div>
</div></div>

<!-- 3 · ESPECIFICAÇÃO -->
<div class="page"><div class="pad">
  <div class="eyebrow">Especificação</div>
  <div class="h-sec serif" style="font-size:25pt;">Os <em>nove móveis</em>,<br>um a um.</div>
  <hr class="rule" style="margin:8px 0;">

  <table class="dual">
    <tr><th>Móvel</th><th>Medidas e configuração</th></tr>
    {tb_moveis}
  </table>

  <div class="same">
    <div><div class="k">Estrutura</div>
      <div class="d">Caixaria em <b>15 mm</b>, prateleiras e frentes em <b>18 mm</b>, fundos em
      <b>6 mm</b>. Fita de borda em <b>todas</b> as faces aparentes — inclusive as que só
      aparecem com a porta aberta.</div></div>
    <div><div class="k">Ferragens · Hardt</div>
      <div class="d"><b>18 dobradiças</b> e <b>14 corrediças ocultas</b>, todas com
      amortecimento. <b>5 articuladores</b> de báscula e suportes metálicos de prateleira.</div></div>
    <div><div class="k">Puxador</div>
      <div class="d"><b>16,94 m</b> de cava usinada na CNC. O puxador é a própria frente: nada
      aplicado, nada para desalinhar com o tempo. Nas três cores, com o mesmo perfil.</div></div>
  </div>

  <div class="pull" style="margin-top:6mm;">
    <div class="t">Três cores nunca dividem chapa.</div>
    <div class="d">Azul Ardósia, Freijó e Cinza Urban são compradas e cortadas em separado —
    cada cor tem seu próprio plano de corte. É o que garante que o tom de uma porta seja
    exatamente o da porta ao lado, e é por isso que um projeto tricolor não custa o mesmo que
    um monocromático.</div>
  </div>

  <div class="note" style="margin-top:5mm;"><b>Não incluso:</b> granito, cuba e misturador;
  porcelanato e demais revestimentos; cooktop, forno, micro-ondas, coifa, geladeira,
  purificador e luminária; pontos elétricos e hidráulicos; rebaixo de gesso.</div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span>
    <span>Cozinha · projeto Rizzi Interiores</span></div>
</div></div>

<!-- 4 · INVESTIMENTO -->
<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="h-sec serif" style="font-size:25pt;">A cozinha <em>completa</em>.</div>
  <hr class="rule" style="margin:8px 0;">

  <table class="dual" style="margin-top:5mm;">
    <tr><th>Linha</th><th>O que entra</th><th class="vh">Investimento</th></tr>
    <tr><td class="sv">Armários inferiores da bancada<small>Azul Ardósia</small></td>
      <td class="ds">Os dois corpos que fecham o “L” — <b>272 + 150 cm</b> — com 11 gavetas em
      corrediça oculta, portas de giro e sóculo recuado.</td>
      <td class="vl">R$ {br(BANC)}</td></tr>
    <tr><td class="sv">Demais móveis<small>três cores</small></td>
      <td class="ds">Nicho e básculas em freijó, os dois aéreos, a torre quente do piso ao teto,
      o painel ripado e a mesa.</td>
      <td class="vl">R$ {br(DEMAIS)}</td></tr>
    <tr class="tot"><td class="sv">Total</td>
      <td class="ds">Projeto, medição, produção, entrega e instalação pela equipe própria Valvic.</td>
      <td class="vl">R$ {br(TOT)}</td></tr>
  </table>

  <table class="pay-tb2">
    <tr><th>Forma de pagamento</th><th class="r">Condição</th><th class="r">Investimento</th></tr>
    {esc}
  </table>

  <div class="pull" style="margin-top:6mm;">
    <div class="t">Os armários da bancada em linha própria.</div>
    <div class="d">Eles aparecem separados porque são o maior bloco isolado do projeto e o mais
    fácil de faseiar. <b>Se forem executados depois</b>, o restante da cozinha fica em
    <b>R$ {br(SEM_BANC)}</b> — e não nos R$ {br(DEMAIS)} acima: chapa comprada para o conjunto não
    encolhe na mesma proporção quando o conjunto diminui, e a instalação continua sendo uma
    cozinha inteira.</div>
  </div>

  <div class="cnd">
    <div><div class="k">Prazo de entrega</div>
      <div class="v"><b>60 dias corridos</b>, a partir da aprovação e da medição final.</div></div>
    <div><div class="k">Garantia</div>
      <div class="v"><b>10 anos</b> em estrutura e ferragens · <b>2 anos</b> nas corrediças.</div></div>
    <div><div class="k">Medição</div>
      <div class="v">Feita por nós <b>antes da liberação do corte</b>. As cotas desta proposta
      vêm do documento de consultoria, que declara não servir como referência para compra
      final — eventuais ajustes são acertados na medição, com a proposta revisada por escrito
      antes de a produção começar.</div></div>
    <div><div class="k">Validade</div>
      <div class="v"><b>7 dias</b>. Chapa e ferragem sujeitas a reajuste após o prazo.</div></div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span>
    <span>Cozinha · projeto Rizzi Interiores · 07/08/2026</span></div>
</div></div>

</body></html>"""

(P/'proposta-cozinha-elena-v3.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-cozinha-elena-v3.html', len(HTML))
