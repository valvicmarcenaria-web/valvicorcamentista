# -*- coding: utf-8 -*-
"""SPE NOVA LIMA 1 — proposta ATUALIZADA (stand + apartamento decorado).

[Jonathan 07/08] "considere sem RT e MC de 35%. sem mexer nos valores na
proposta inicial."

O stand (MOB 01 + MOB 02) entra INALTERADO em R$ 88.200 — foi fechado a MC 40%
sem RT. O decorado (MO 03 + DET 05 + DET 06) sai a MC 35% sem RT, divisor
0,45016, de `corte-spe-decorado.py`:

  Cozinha  R$ 11.671,12 → 25.900      Quarto  R$  9.178,30 → 20.400
  Sala     R$  6.306,83 → 14.000      Suíte   R$ 10.652,57 → 23.700
  DECORADO R$ 37.808,82 → 84.000  (MC conferida 35,0%)

  TOTAL  88.200 + 84.000 = R$ 172.200   ·   MC combinada do contrato ~37,6%
"""
import pathlib
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')
CSS = open('/tmp/css_premium.txt', encoding='utf-8').read().split('CSS = """')[1].rsplit('"""', 1)[0]

STAND, DEC, TOT = 88200, 84000, 172200
AMB = [('Cozinha', 'Anis Matt · Frapé Matt',
        'Bancada em “L” com módulos de giro e a torre do forno com <b>3 gavetas</b> · '
        'aéreos em dois planos, <b>prof. 62</b> em Anis e <b>prof. 40</b> em Frapé com '
        '<b>8 básculas</b> em articulador · nicho do micro-ondas e vão da coifa de embutir · '
        'painel alto de <b>2,55 m</b> com nichos.', 25900),
       ('Sala', 'Anis Matt',
        'Painelaria de <b>7,20 m</b> de desenvolvimento por <b>2,55 m</b> de altura, em duas '
        'elevações: painel com <b>4 nichos de espelho</b> emoldurados e espelho de 1,90 m · '
        'painel com <b>3 nichos</b> e porta embutida · <b>rodapé em perfil de inox escovado</b>.', 14000),
       ('Quarto', 'Ciliegio Poro · laca Sayerlack M072',
        'Roupeiro de <b>1,54 m</b> com duas portas de correr · módulo de nichos iluminados em '
        '<b>laca brilhante</b> · cabeceira estofada, painel de TV, prateleira suspensa, '
        'bancada de trabalho e criado suspenso · cortineiro com iluminação.', 20400),
       ('Suíte', 'Anis Matt · Frapé Matt',
        'Torre de <b>5 nichos iluminados</b> em Frapé, do piso ao teto · roupeiro de '
        '<b>1,935 m</b> com duas portas de correr · <b>painel ripado</b> em perfil de madeira '
        '5×1,5 · cabeceira estofada e cortineiro com iluminação.', 23700)]
def br(v): return f'{v:,.0f}'.replace(',', '.')

amb_tb = ''.join(
  f'<tr><td class="sv">{n}<small>{c}</small></td><td class="ds">{d}</td>'
  f'<td class="vl alt">R$ {br(v)}</td></tr>' for n, c, d, v in AMB)

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

  .amb4{{border-top:1px solid var(--hair); padding:6.6mm 0;}}
  .amb4:first-child{{border-top:2px solid var(--ink);}}
  .amb4 .hd{{display:flex; justify-content:space-between; align-items:baseline;}}
  .amb4 .t{{font-family:'Cormorant Garamond',Georgia,serif; font-size:19pt; font-weight:700; line-height:1.14;}}
  .amb4 .q{{font-size:6.4pt; letter-spacing:.16em; text-transform:uppercase; color:var(--gold);
      font-weight:700; white-space:nowrap; padding-left:5mm;}}
  .amb4 .d{{font-size:9.6pt; color:var(--soft); line-height:1.64; margin-top:2mm;}}
  .amb4 .d b{{color:var(--ink);}}

  .lin{{display:flex; gap:7mm; margin-top:6mm;}}
  .lin > div{{flex:1; border:1.5px solid var(--line); border-radius:7px; padding:7mm 6.5mm;}}
  .lin > div.g{{border-color:var(--gold); background:rgba(201,169,106,.07);}}
  .lin .k{{font-size:6.4pt; letter-spacing:.18em; text-transform:uppercase; color:var(--gold); font-weight:700;}}
  .lin .t{{font-family:'Cormorant Garamond',Georgia,serif; font-size:24pt; font-weight:700;
      color:var(--ink); line-height:1.05; margin-top:1.4mm;}}
  .lin .d{{font-size:8.8pt; color:var(--soft); line-height:1.58; margin-top:2.4mm;}}
  .lin .d b{{color:var(--ink);}}

  .dual{{width:100%; border-collapse:collapse; font-size:8.6pt; margin-top:3mm;}}
  .dual th{{font-size:6.4pt; letter-spacing:.14em; text-transform:uppercase; color:var(--mut);
      font-weight:700; border-bottom:1.5px solid var(--ink); padding:0 0 2mm; text-align:left;
      vertical-align:bottom;}}
  .dual th.vh{{text-align:right; width:28mm; padding-left:3mm; color:var(--gold);}}
  .dual td{{padding:2.1mm 0; border-bottom:1px solid var(--hair); vertical-align:top;}}
  .dual td.sv{{width:32mm; font-weight:700; color:var(--ink); font-size:9pt; padding-right:3mm;}}
  .dual td.sv small{{display:block; font-weight:700; color:var(--gold); font-size:6.4pt;
      letter-spacing:.12em; text-transform:uppercase; margin-top:.5mm; line-height:1.3;}}
  .dual td.ds{{color:var(--soft); line-height:1.54; padding-right:4mm;}}
  .dual td.vl{{text-align:right; white-space:nowrap; font-weight:700;
      font-variant-numeric:tabular-nums; padding-left:3mm;}}
  .dual td.vl.alt{{color:var(--gold); background:rgba(201,169,106,.07);}}
  .dual tr.st td{{background:var(--sand);}}
  .dual tr.st td.vl{{color:var(--soft); background:var(--sand);}}
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

  .same{{display:flex; gap:0; margin-top:6mm; border-top:2px solid var(--ink);
      border-bottom:1px solid var(--line); padding:5.4mm 0;}}
  .same > div{{flex:1; padding-left:6mm; border-left:1px solid var(--line);}}
  .same > div:first-child{{padding-left:0; border-left:0;}}
  .same .k{{font-size:6.4pt; letter-spacing:.16em; text-transform:uppercase; color:var(--gold); font-weight:700;}}
  .same .d{{font-size:8.8pt; color:var(--soft); line-height:1.56; margin-top:1.4mm;}}
  .same .d b{{color:var(--ink);}}

  .cnd{{display:grid; grid-template-columns:1fr 1fr; gap:4.2mm 8mm; margin-top:5mm;
      border-top:2px solid var(--ink); padding-top:4.2mm;}}
  .cnd .k{{font-size:6.4pt; letter-spacing:.16em; text-transform:uppercase; color:var(--gold); font-weight:700;}}
  .cnd .v{{font-size:9.2pt; color:var(--soft); line-height:1.52; margin-top:.8mm;}}
  .cnd .v b{{color:var(--ink);}}
</style></head><body>

<!-- 1 · CAPA -->
<div class="page cover cover-t">
  <div class="rules"></div><div class="v2">02</div>
  <div class="inner">
    <div><div class="brand">valvic<span class="d">.</span></div><div class="bsub">MARCENARIA</div></div>
    <div class="mid">
      <div class="kick">Proposta de marcenaria · atualização</div>
      <div class="tit">SPE<br>Nova Lima 1.</div>
      <div class="sub">Stand de vendas e apartamento decorado · projeto Lodi Motta</div>
    </div>
    <div class="strip">
      <div class="c"><div class="k">Contratado</div><div class="v">Stand</div></div>
      <div class="c"><div class="k">Entra agora</div><div class="v">4 ambientes</div></div>
      <div class="c"><div class="k">Pranchas</div><div class="v">MO 03 · DET 05 · DET 06</div></div>
      <div class="c"><div class="k">Data</div><div class="v">07.08.2026</div></div>
    </div>
  </div>
</div>

<!-- 2 · O QUE MUDA -->
<div class="page"><div class="pad">
  <div class="eyebrow">A atualização</div>
  <div class="h-sec serif" style="font-size:25pt;">O stand segue como está.<br><em>O decorado entra somado.</em></div>
  <hr class="rule" style="margin:8px 0;">
  <p class="lead" style="margin-bottom:2mm;">As três pranchas executivas emitidas em 05 e 06 de
  agosto detalham o apartamento decorado. Conferimos item a item: <b>não há sobreposição</b>
  com o que já foi contratado.</p>

  <div class="lin">
    <div>
      <div class="k">Já contratado</div>
      <div class="t">R$ {br(STAND)}</div>
      <div class="d">Painelaria, pérgola e mobiliário das <b>áreas comerciais</b> —
      MOB 01 (painel dos corretores e pilar) e MOB 02 (painel e pérgula do gourmet-lounge).
      <br><br><b>Nenhum valor desta etapa foi alterado.</b> As condições permanecem
      exatamente como aprovadas.</div>
    </div>
    <div class="g">
      <div class="k">Entra agora</div>
      <div class="t">R$ {br(DEC)}</div>
      <div class="d">O <b>apartamento decorado</b> completo: cozinha, sala, quarto e suíte.
      <br><br>São <b>145,9 m² de chapa</b> em quatro acabamentos — Anis Matt, Frapé Matt,
      Ciliegio Poro e laca brilhante Sayerlack — mais espelhos, cabeceiras estofadas,
      rodapé em inox e iluminação embutida.</div>
    </div>
  </div>

  <div class="same">
    <div><div class="k">Do executivo, não do croqui</div>
      <div class="d">As três pranchas são <b>executivas e cotadas</b>. O levantamento saiu das
      elevações, não de estimativa por metro quadrado.</div></div>
    <div><div class="k">Quatro acabamentos</div>
      <div class="d">Cada cor tem <b>plano de corte próprio</b> e nunca divide chapa com outra.
      É o que garante a uniformidade de tom entre peças vizinhas.</div></div>
    <div><div class="k">Coordenação dos terceiros</div>
      <div class="d">Espelho, laca, estofado e rodapé de inox são <b>coordenados pela
      Valvic</b> e entregues instalados, dentro do valor.</div></div>
  </div>

  <table class="dual" style="margin-top:7mm;">
    <tr><th>O decorado em números</th><th>Composição</th></tr>
    <tr><td class="sv">Chapa<small>45 chapas · 145,9 m²</small></td>
      <td class="ds"><b>Anis Matt</b> e <b>Frapé Matt</b> na sala, cozinha e suíte ·
      <b>Ciliegio Poro</b> no quarto · branco na caixaria interna. Quatro planos de corte
      independentes.</td></tr>
    <tr><td class="sv">Ferragens<small>Hardt</small></td>
      <td class="ds"><b>22 dobradiças</b> com amortecimento · <b>8 articuladores</b> de báscula ·
      <b>3 conjuntos</b> de porta de correr · corrediças ocultas na torre do forno ·
      <b>8,95 m</b> de cava usinada.</td></tr>
    <tr><td class="sv">Terceiros<small>coordenados pela Valvic</small></td>
      <td class="ds">Espelho prata com perfil <b>5,34 m²</b> · laca brilhante Sayerlack M072
      <b>3,16 m²</b> · duas cabeceiras estofadas <b>3,64 m²</b> · rodapé em inox escovado
      <b>10,6 m</b> · fita de LED com perfil <b>9,9 m</b>.</td></tr>
  </table>

  <div class="note"><b>Fora do escopo:</b> caixa de gypsum, forro, pintura de paredes e teto,
  cortinas, tapetes, eletrodomésticos, bancadas de pedra, cubas e metais — todos indicados nas
  pranchas como fornecimento de outras frentes.</div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span>
    <span>SPE Nova Lima 1 · atualização</span></div>
</div></div>

<!-- 3 · O DECORADO -->
<div class="page"><div class="pad">
  <div class="eyebrow">O decorado</div>
  <div class="h-sec serif" style="font-size:25pt;">Quatro ambientes,<br><em>ambiente a ambiente.</em></div>
  <hr class="rule" style="margin:8px 0;">

  <div style="margin-top:3mm;">
    <div class="amb4"><div class="hd"><div class="t">Cozinha</div>
      <div class="q">MO 03 · Anis + Frapé</div></div>
      <div class="d">Bancada em “L” com módulos de giro e a torre do forno com <b>3 gavetas</b>.
      Aéreos em <b>dois planos de profundidade</b> — 62 cm em Anis Matt e 40 cm em Frapé Matt,
      com <b>8 básculas</b> em articulador. Nicho do micro-ondas, vão da coifa de embutir e
      painel alto de <b>2,55 m</b> com nichos. Puxador em <b>cava</b>, conforme o DET.03.</div></div>

    <div class="amb4"><div class="hd"><div class="t">Sala</div>
      <div class="q">MO 03 · 7,20 m de painelaria</div></div>
      <div class="d">Duas elevações de painel a <b>2,55 m</b> de altura: uma com <b>quatro
      nichos de espelho</b> emoldurados e espelho de 1,90 m; outra com <b>três nichos</b> e a
      porta embutida no painel. <b>Rodapé em perfil de inox escovado</b> 5×0,5 correndo a base.</div></div>

    <div class="amb4"><div class="hd"><div class="t">Quarto</div>
      <div class="q">DET 05 · Ciliegio + laca</div></div>
      <div class="d">Roupeiro de <b>1,54 m</b> com duas portas de correr e módulo lateral de
      <b>nichos iluminados em laca brilhante</b> Sayerlack M072. Cabeceira estofada, painel de
      TV, prateleira suspensa, bancada de trabalho e criado suspenso. Cortineiro com
      iluminação embutida.</div></div>

    <div class="amb4"><div class="hd"><div class="t">Suíte</div>
      <div class="q">DET 06 · Anis + Frapé</div></div>
      <div class="d">Torre de <b>cinco nichos iluminados</b> em Frapé Matt, do piso ao teto ·
      roupeiro de <b>1,935 m</b> com duas portas de correr · <b>painel ripado</b> em perfil de
      madeira 5×1,5 · cabeceira estofada e cortineiro com iluminação.</div></div>
  </div>

  <div class="pull" style="margin-top:6mm;">
    <div class="t">Medição antes do corte.</div>
    <div class="d">As pranchas trazem a observação <i>“conferir medidas na obra”</i>. Nossa
    medição é feita no local antes da liberação do corte — e é ela que trava as dimensões
    finais de cada peça.</div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span>
    <span>SPE Nova Lima 1 · atualização</span></div>
</div></div>

<!-- 4 · INVESTIMENTO -->
<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="h-sec serif" style="font-size:25pt;">O contrato <em>atualizado</em>.</div>
  <hr class="rule" style="margin:8px 0;">

  <table class="dual" style="margin-top:4mm;">
    <tr><th>Etapa</th><th>Escopo</th><th class="vh">Investimento</th></tr>
    <tr class="st"><td class="sv">Stand de vendas<small>já contratado</small></td>
      <td class="ds">MOB 01 e MOB 02 — painel dos corretores, pilar, painel e pérgula do
      gourmet-lounge, móvel do lounge e armário gourmet. <b>Valor inalterado.</b></td>
      <td class="vl">R$ {br(STAND)}</td></tr>
    {amb_tb}
    <tr class="tot"><td class="sv">Total</td>
      <td class="ds">Projeto, medição, produção, terceiros coordenados, entrega e instalação
      pela equipe própria Valvic.</td>
      <td class="vl alt">R$ {br(TOT)}</td></tr>
  </table>

  <table class="pay-tb2">
    <tr><th>Forma de pagamento</th><th class="r">Condição</th><th class="r">Investimento</th></tr>
    {esc}
  </table>

  <div class="cnd">
    <div><div class="k">Prazo de entrega</div>
      <div class="v"><b>60 a 75 dias úteis</b> para o decorado, a alinhar com a data de
      inauguração do stand.</div></div>
    <div><div class="k">Garantia</div>
      <div class="v"><b>2 anos</b>, mesma condição da etapa já contratada.</div></div>
    <div><div class="k">Medição</div>
      <div class="v">Feita por nós <b>antes da liberação do corte</b>, conforme a observação
      das próprias pranchas.</div></div>
    <div><div class="k">Validade</div>
      <div class="v"><b>7 dias</b>. Chapa e ferragem sujeitas a reajuste após o prazo.</div></div>
  </div>

  <div class="note" style="margin-top:4mm;"><b>Fora do escopo:</b> caixa de gypsum, forro,
  pintura de paredes e teto, cortinas, tapetes, eletrodomésticos, bancadas de pedra, cubas e
  metais.</div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span>
    <span>SPE Nova Lima 1 · 07/08/2026</span></div>
</div></div>

</body></html>"""

(P/'proposta-spe-nova-lima.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-spe-nova-lima.html', len(HTML))
