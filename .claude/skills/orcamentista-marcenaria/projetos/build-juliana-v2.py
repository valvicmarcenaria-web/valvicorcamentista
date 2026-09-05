# -*- coding: utf-8 -*-
"""KAIRON & JULIANA — VERSÃO 2 · escopo priorizado  [Jonathan 06/08/2026]

A V1 tinha 8 ambientes (Gold 123.954 / Essencial 107.121). Eles priorizaram:
  · Cozinha  · Quarto de casal  · Closet
e entra um item NOVO na cozinha: mesa de refeições com base em serralheria e
tampo em MDF, R$ 2.350 de venda (mesmo valor nas duas linhas — serralheria e
MDF não mudam de linha).

O gabinete do lavabo entra de BRINDE no fechamento (valia 2.000 Gold / 1.800
Essencial na V1).

Valores dos 3 ambientes preservados da V1 — não recalculei nada.
Condições herdadas da V1: escada padrão, prazo 45–60 dias úteis, validade 7
dias, garantia Gold 10 anos / Essencial 2 anos.
"""
import pathlib
P = pathlib.Path(__file__).resolve().parent
CSS = open(P/'css-juliana-premium.css', encoding='utf-8').read()

ITENS = [
 ('Cozinha', 'Coluna de eletros, aéreos e balcões',
  'Coluna com <b>forno e micro-ondas embutidos</b> · vão de geladeira com tamponamento · '
  'balcões inferiores com gavetões · aéreos em três faces · prateleiras flutuantes · '
  '<b>6 m de LED</b> com sensor · puxador em <b>perfil cava Rometal RM195</b>. '
  'Interno todo em <b>branco</b>.', 23000, 20400),
 ('Cozinha', 'Mesa de refeições <span class="nv">novo</span>',
  'Base em <b>serralheria</b> com tampo em <b>MDF</b>. Item acrescentado nesta versão — '
  'fecha a cozinha como ambiente de refeição, não só de preparo.', 2350, 2350),
 ('Quarto de casal', '',
  '<b>Cabeceira estofada</b> · painel · duas mesinhas suspensas com duas gavetas cada · '
  '<b>porta de passagem em sistema RO82 sem freio</b> (folha + trilho) · puxadores '
  'redondos dourados · <b>3 m de LED</b> com sensor. Interno todo em <b>branco</b>.',
  19600, 17400),
 ('Closet', 'Versão 2',
  'Armários piso-teto com portas até o forro · <b>12 gavetas e sapateiras internas</b> · '
  'cabideiros · puxador <b>Next Meia Lua 64 mm</b> · '
  '<b>cômoda de cinco gavetas em laca vermelha, com tampo de vidro</b>. '
  'Interno todo em <b>branco</b>.', 36700, 31500),
]
BRINDE = ('Lavabo', 'Gabinete suspenso',
          'Gabinete suspenso amadeirado, com o interno em branco e a cuba por '
          'conta do cliente.', 2000, 1800)

TG = sum(i[3] for i in ITENS)
TE = sum(i[4] for i in ITENS)
def br(v): return f'{v:,.0f}'.replace(',', '.')

linhas = ''.join(
  f'<tr><td class="sv"><b>{a}</b>{f"<small>{b}</small>" if b else ""}</td>'
  f'<td class="ds">{d}</td>'
  f'<td class="vl">R$ {br(g)}</td><td class="vl alt">R$ {br(e)}</td></tr>'
  for a, b, d, g, e in ITENS)

ESCADA = [('Entrada 30% + saldo em até 10× no cartão', 0.00, 'valor de tabela'),
          ('Entrada 50% + saldo em até 8× no cartão',  0.03, '−3%'),
          ('Entrada 70% + saldo em até 6× no cartão',  0.05, '−5%'),
          ('Entrada 70% + saldo via transferência',    0.07, '−7%')]
def _tr(d):
    return ' class="best"' if d == 0.07 else ''
esc = ''.join(
  f'<tr{_tr(d)}><td>{n}</td><td class="r">{r}</td>'
  f'<td class="r">R$ {br(TG*(1-d))}</td><td class="r alt">R$ {br(TE*(1-d))}</td></tr>'
  for n, d, r in ESCADA)

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

  .amb4{{border-top:1px solid var(--hair); padding:7.4mm 0;}}
  .amb4:first-child{{border-top:2px solid var(--ink);}}
  .amb4 .hd{{display:flex; justify-content:space-between; align-items:baseline;}}
  .amb4 .t{{font-family:'Cormorant Garamond',Georgia,serif; font-size:19pt; font-weight:700;
      line-height:1.14;}}
  .amb4 .q{{font-size:6.4pt; letter-spacing:.16em; text-transform:uppercase; color:var(--gold);
      font-weight:700; white-space:nowrap; padding-left:5mm;}}
  .amb4 .d{{font-size:10pt; color:var(--soft); line-height:1.7; margin-top:2.2mm;}}
  .amb4 .d b{{color:var(--ink);}}
  .nv{{display:inline-block; font-family:system-ui,sans-serif; font-size:6.2pt;
      letter-spacing:.14em; text-transform:uppercase; font-weight:700; color:#fff;
      background:var(--gold); border-radius:2px; padding:.6mm 1.6mm; vertical-align:middle;
      margin-left:2mm;}}

  .lin{{display:flex; gap:7mm; margin-top:6mm;}}
  .lin > div{{flex:1; border:1.5px solid var(--line); border-radius:7px; padding:9.5mm 7.5mm;}}
  .lin > div.g{{border-color:var(--gold); background:rgba(201,169,106,.07);}}
  .lin .k{{font-size:6.4pt; letter-spacing:.18em; text-transform:uppercase; color:var(--gold);
      font-weight:700;}}
  .lin .t{{font-family:'Cormorant Garamond',Georgia,serif; font-size:26pt; font-weight:700;
      color:var(--ink); line-height:1.05; margin-top:1.4mm;}}
  .lin .d{{font-size:9pt; color:var(--soft); line-height:1.62; margin-top:2.2mm;}}
  .lin .d b{{color:var(--ink);}}
  .lin ul{{margin:3.4mm 0 0; padding-left:4.4mm; font-size:9.4pt; color:var(--soft);
      line-height:1.85;}}
  .lin ul b{{color:var(--ink);}}

  .dual{{width:100%; border-collapse:collapse; font-size:8.6pt; margin-top:3mm;}}
  .dual th{{font-size:6.4pt; letter-spacing:.14em; text-transform:uppercase; color:var(--mut);
      font-weight:700; border-bottom:1.5px solid var(--ink); padding:0 0 2mm; text-align:left;
      vertical-align:bottom;}}
  .dual th.vh{{text-align:right; width:26mm; padding-left:3mm;}}
  .dual th.vh.alt{{color:var(--gold);}}
  .dual td{{padding:2.4mm 0; border-bottom:1px solid var(--hair); vertical-align:top;}}
  .dual td.sv{{width:33mm; font-weight:700; color:var(--ink); font-size:9pt; padding-right:3mm;}}
  .dual td.sv small{{display:block; font-weight:400; color:var(--soft); font-size:7.8pt;}}
  .dual td.ds{{color:var(--soft); line-height:1.56; padding-right:4mm;}}
  .dual td.vl{{text-align:right; white-space:nowrap; font-weight:700;
      font-variant-numeric:tabular-nums; padding-left:3mm;}}
  .dual td.vl.alt{{color:var(--gold); background:rgba(201,169,106,.07);}}
  .dual tr.tot td{{border-bottom:0; border-top:2px solid var(--ink); padding-top:3.6mm;
      font-family:'Cormorant Garamond',Georgia,serif; font-size:16pt;}}
  .dual tr.tot td.ds{{font-family:system-ui,sans-serif; font-size:8.6pt;}}
  .dual tr.bri td{{background:var(--deep); color:#EFE7D8; border-bottom:0;}}
  .dual tr.bri td.sv{{color:#fff; border-radius:4px 0 0 4px;}}
  .dual tr.bri td.sv small{{color:#C6BFB2;}}
  .dual tr.bri td.ds{{color:#C6BFB2;}}
  .dual tr.bri td.vl{{color:var(--gold-lt); background:transparent;}}
  .dual tr.bri td.vl:last-child{{border-radius:0 4px 4px 0;}}
  .dual tr.bri s{{color:#8C8071; font-weight:400;}}

  .pay-tb2{{width:100%; border-collapse:collapse; font-size:9pt; margin-top:4mm;}}
  .pay-tb2 th{{font-size:6.4pt; letter-spacing:.14em; text-transform:uppercase; color:var(--mut);
      font-weight:700; border-bottom:1.5px solid var(--ink); padding:0 0 2mm; text-align:left;}}
  .pay-tb2 th.r, .pay-tb2 td.r{{text-align:right;}}
  .pay-tb2 td{{padding:2.2mm 0; border-bottom:1px solid var(--hair);
      font-variant-numeric:tabular-nums;}}
  .pay-tb2 td.r{{font-weight:700; white-space:nowrap; padding-left:4mm;}}
  .pay-tb2 td.r.alt{{color:var(--gold);}}
  .pay-tb2 tr.best td{{background:rgba(201,169,106,.12); border-bottom:0;}}
  .pay-tb2 tr.best td:first-child{{border-radius:4px 0 0 4px; font-weight:700;}}
  .pay-tb2 tr.best td:last-child{{border-radius:0 4px 4px 0;}}

  .same{{display:flex; gap:0; margin-top:11mm; border-top:2px solid var(--ink);
      border-bottom:1px solid var(--line); padding:7mm 0;}}
  .same > div{{flex:1; padding-left:6mm; border-left:1px solid var(--line);}}
  .same > div:first-child{{padding-left:0; border-left:0;}}
  .same .k{{font-size:6.4pt; letter-spacing:.16em; text-transform:uppercase; color:var(--gold);
      font-weight:700;}}
  .same .d{{font-size:9pt; color:var(--soft); line-height:1.62; margin-top:1.4mm;}}
  .same .d b{{color:var(--ink);}}

  .cnd{{display:grid; grid-template-columns:1fr 1fr; gap:5mm 8mm; margin-top:7mm;
      border-top:2px solid var(--ink); padding-top:4.6mm;}}
  .cnd .k{{font-size:6.4pt; letter-spacing:.16em; text-transform:uppercase; color:var(--gold);
      font-weight:700;}}
  .cnd .d{{font-size:9pt; color:var(--soft); line-height:1.58; margin-top:1.1mm;}}
  .cnd .d b{{color:var(--ink);}}
</style></head><body>

<!-- ══════ 1. CAPA ══════ -->
<div class="page cover cover-t">
  <div class="rules"></div><div class="v2">02</div>
  <div class="inner">
    <div><div class="brand">valvic<span class="d">.</span></div><div class="bsub">MARCENARIA</div></div>
    <div class="mid">
      <div class="kick">Proposta de marcenaria · versão 2</div>
      <div class="tit">Kairon<br>&amp; Juliana.</div>
      <div class="sub">Escopo priorizado · cozinha, quarto de casal e closet</div>
    </div>
    <div class="strip">
      <div class="c"><div class="k">Escopo</div><div class="v">3 ambientes + mesa</div></div>
      <div class="c"><div class="k">Linhas</div><div class="v">Gold e Essencial</div></div>
      <div class="c"><div class="k">Entrega</div><div class="v">45 a 60 dias úteis</div></div>
    </div>
  </div>
</div>

<!-- ══════ 2. O ESCOPO PRIORIZADO ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Versão 2 · o que entra agora</div>
  <div class="h-sec serif" style="font-size:25pt;">Três ambientes,<br><em>na ordem de vocês.</em></div>
  <hr class="rule" style="margin:8px 0 8px;">
  <p class="lead" style="margin-bottom:2mm;">Esta versão concentra o investimento nos ambientes
  que vocês priorizaram, e acrescenta à cozinha a <b>mesa de refeições</b>. Os demais ambientes
  da versão 1 continuam válidos e podem ser retomados a qualquer momento, pelos mesmos valores.</p>

  <div style="margin-top:2.5mm;">
    <div class="amb4"><div class="hd"><div class="t">Cozinha</div><div class="q">o ambiente principal</div></div>
      <div class="d">Coluna com <b>forno e micro-ondas embutidos</b>, vão de geladeira com
      tamponamento, balcões inferiores com gavetões, aéreos em três faces e prateleiras
      flutuantes. <b>6 m de LED</b> com sensor e <b>18 m de puxador em cava usinada</b> — a mão
      entra na própria frente, sem nada aplicado.</div></div>

    <div class="amb4"><div class="hd"><div class="t">Mesa de refeições <span class="nv">novo</span></div>
      <div class="q">base em serralheria</div></div>
      <div class="d">Base em <b>serralheria</b> e tampo em <b>MDF</b>, integrada à cozinha.
      É o item que transforma a cozinha em ambiente de refeição e não só de preparo — e o que
      faltava para ela funcionar sozinha, sem depender da sala.</div></div>

    <div class="amb4"><div class="hd"><div class="t">Quarto de casal</div><div class="q">com porta de passagem</div></div>
      <div class="d"><b>Cabeceira estofada</b> e painel · duas mesinhas suspensas de duas
      gavetas · <b>porta de passagem em sistema RO82 sem freio</b>, folha e trilho · puxadores
      redondos dourados · <b>3 m de LED</b> com sensor. Interno em <b>branco</b>.</div></div>

    <div class="amb4"><div class="hd"><div class="t">Closet · versão 2</div><div class="q">com cômoda lacada</div></div>
      <div class="d">Armários piso-teto com portas até o forro · <b>12 gavetas e sapateiras
      internas</b> · cabideiros metálicos · puxador <b>Next Meia Lua 64 mm</b> ·
      <b>cômoda de cinco gavetas em laca vermelha com tampo de vidro</b>, o contraponto de cor
      do ambiente. Interno em <b>branco</b>.</div></div>
  </div>

  <div class="pull" style="margin-top:9mm;">
    <div class="t">Um ambiente<br>por vez.</div>
    <div class="d">Priorizar não é reduzir o projeto — é executá-lo na ordem em que ele é usado.
    Cozinha, quarto e closet resolvem <b>o dia inteiro de vocês</b>. O resto espera sem perder
    o preço.</div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Kairon &amp; Juliana · versão 2</span></div>
</div></div>

<!-- ══════ 3. GOLD × ESSENCIAL ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">As duas linhas</div>
  <div class="h-sec serif" style="font-size:25pt;">A mesma marcenaria.<br><em>A ferragem decide.</em></div>
  <hr class="rule" style="margin:8px 0 8px;">
  <p class="lead" style="margin-bottom:1mm;">O desenho, as medidas, as chapas e o acabamento são
  <b>idênticos</b> nas duas linhas. O que muda é a ferragem — e, com ela, o tempo de garantia.</p>

  <div class="lin">
    <div class="g"><div class="k">Linha Gold</div>
      <div class="t">Hettich.</div>
      <div class="d">Ferragem alemã em todo o projeto.</div>
      <ul>
        <li><b>Corrediça oculta</b> com amortecimento, por baixo da gaveta</li>
        <li><b>Dobradiça com amortecimento integrado</b> e ajuste em 3 dimensões</li>
        <li>Regulagem que <b>mantém a fresta igual</b> anos depois da instalação</li>
        <li><b>Garantia de 10 anos</b> — estrutura <em>e</em> ferragens</li>
      </ul></div>
    <div><div class="k">Linha Essencial</div>
      <div class="t">Hardt.</div>
      <div class="d">Ferragem nacional, mesma marcenaria.</div>
      <ul>
        <li>Corrediça e abertura em <b>linha mais econômica</b></li>
        <li>Mesmo desenho, mesmas chapas, mesmo acabamento</li>
        <li>Regulagem mais simples, sem ajuste tridimensional</li>
        <li><b>Garantia de 2 anos</b></li>
      </ul></div>
  </div>

  <div class="same">
    <div><div class="k">O que não muda</div>
      <div class="d"><b>O desenho e as medidas.</b> Mesmo projeto, mesmos módulos, mesma
      distribuição interna nos dois casos.</div></div>
    <div><div class="k">Também não muda</div>
      <div class="d"><b>A chapa e o acabamento.</b> Mesmas espessuras, mesma cor, mesma
      filetagem — e o mesmo LED instalado.</div></div>
    <div><div class="k">Nem muda</div>
      <div class="d"><b>Quem faz.</b> Equipe própria do corte à instalação, e a mesma
      conferência de medida no local antes do corte.</div></div>
  </div>

  <div class="pull" style="margin-top:10mm;">
    <div class="t">Oito anos<br>de diferença.</div>
    <div class="d">Entre as duas linhas há <b>R$ {br(TG-TE)}</b> e <b>oito anos de garantia</b>.
    Num closet e numa cozinha inteiros, a ferragem é o que se aciona milhares de
    vezes — <b>é onde o móvel envelhece</b>, e é exatamente o que a linha Gold está comprando.</div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Kairon &amp; Juliana · versão 2</span></div>
</div></div>

<!-- ══════ 4. INVESTIMENTO ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="h-sec serif" style="font-size:25pt;">Versão 2.</div>
  <hr class="rule" style="margin:8px 0 8px;">

  <table class="dual">
    <thead><tr><th>Ambiente</th><th>Descrição</th>
      <th class="vh">Gold<br><span style="font-weight:400;text-transform:none;letter-spacing:0;">Hettich · 10 anos</span></th>
      <th class="vh alt">Essencial<br><span style="font-weight:400;text-transform:none;letter-spacing:0;">Hardt · 2 anos</span></th></tr></thead>
    <tbody>
      {linhas}
      <tr class="bri"><td class="sv"><b>{BRINDE[0]}</b><small>{BRINDE[1]}</small></td>
        <td class="ds">{BRINDE[2]} <b style="color:#F0E7D6;">Cortesia Valvic no fechamento.</b></td>
        <td class="vl"><s>R$ {br(BRINDE[3])}</s><br>R$ 0</td>
        <td class="vl"><s>R$ {br(BRINDE[4])}</s><br>R$ 0</td></tr>
      <tr class="tot"><td class="sv">Total</td><td class="ds"></td>
        <td class="vl">R$ {br(TG)}</td><td class="vl alt">R$ {br(TE)}</td></tr>
    </tbody>
  </table>

  <table class="pay-tb2">
    <thead><tr><th>Forma de pagamento</th><th class="r">Desconto</th>
      <th class="r">Gold</th><th class="r">Essencial</th></tr></thead>
    <tbody>{esc}</tbody>
  </table>

  <div class="cnd">
    <div><div class="k">Prazo de entrega</div><div class="d"><b>45 a 60 dias úteis</b> após a
      aprovação e a medição final no local.</div></div>
    <div><div class="k">Garantia</div><div class="d"><b>Gold: 10 anos</b> sobre estrutura e
      ferragens · <b>Essencial: 2 anos</b>.</div></div>
    <div><div class="k">Validade da proposta</div><div class="d"><b>7 dias corridos</b> a partir
      desta data.</div></div>
    <div><div class="k">Escopo Valvic</div><div class="d">Marcenaria, ferragens, vidros e espelhos
      dos móveis e LED.</div></div>
  </div>

  <div class="note" style="margin-top:4mm;"><b>Por conta do cliente:</b> tampos de pedra,
  revestimentos, forro de madeira, eletrodomésticos, cubas e torneiras. Valores do anteprojeto —
  medidas conferidas no local antes do corte.</div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Kairon &amp; Juliana · 06/08/2026</span></div>
</div></div>

</body></html>"""

(P/'proposta-juliana-v2.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-juliana-v2.html', len(HTML))
print(f'GOLD R$ {br(TG)}  ·  ESSENCIAL R$ {br(TE)}  ·  diferença R$ {br(TG-TE)}')
print(f'brinde lavabo: Gold {br(BRINDE[3])} / Essencial {br(BRINDE[4])}')
