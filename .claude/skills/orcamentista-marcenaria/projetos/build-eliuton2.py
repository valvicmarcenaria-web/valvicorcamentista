# -*- coding: utf-8 -*-
"""ELIUTON · BRISAS DA PAMPULHA — 2ª FASE · proposta comercial.

[Jonathan 07/09/2026] Preço cravado item a item, cenário 2 (Hardt · 5 anos),
com RT. Total R$ 141.800. Prazo 70 dias corridos. Condição especial de
pagamento — entrada de 30% na assinatura e saldo à vista na entrega, o mesmo
desenho com que a 1ª fase fechou em 20/08 (R$ 73.000).

⛔ [Jonathan 07/09] SEM RENDER NESTA PROPOSTA. É decisão de CASO — este
   cliente já viu o deck de 31 renders; a proposta aqui é o documento
   comercial, não a apresentação do projeto. NÃO é regra nova da casa:
   proposta ilustrada segue sendo o padrão.

⛔ O PAINEL DO ESPELHO ORGÂNICO SAIU DO ESCOPO. Ele aparece nos renders do
   quarto master — por isso a proposta DIZ que ele não está incluído. Render
   que mostra o que não vendemos vira expectativa de graça.

⚠ As portas do roupeiro da filha viraram DESLIZANTES em sistema Dominus. O
  render mostra portas de abrir; a proposta descreve o que foi contratado.

Motor: `corte-eliuton2.py` · dossiê: `2026-eliuton-2a-fase.md`.
Imagens: deck de renders da Valvic, recortadas em `img-eliuton2/`.
"""
import subprocess, pathlib

P = pathlib.Path(__file__).resolve().parent
CLIENTE   = 'Eliuton Ribeiro'
OBRA      = 'Residência Brisas da Pampulha'
ARQUITETA = 'Arq. Luciana Beatriz Simplício · Núcleo SC Arquitetura'
DATA      = '07 de setembro de 2026'
VALIDADE  = '7 dias corridos a partir desta data'
PRAZO     = '70 dias corridos'
GARANTIA  = '5 anos'

# ── preço cravado item a item · espelha PRECO_ITEM de corte-eliuton2.py ───
ITENS = [
 ('Quarto master', 'Painel de cabeceira com cabeceira estofada', 'master',
  'Painel amadeirado de <b>3,60 m</b> na parede da cabeceira mais <b>1,50 m</b> '
  'de retorno na lateral, com <b>topo curvo</b> contínuo e rasgo de LED sob o '
  'forro. <b>Cabeceira estofada de 2,00 × 1,00 m</b> integrada ao painel.', 11400),
 ('Quarto master', 'Criados-mudos (2)', None,
  'Dois criados suspensos de <b>85</b> e <b>80 cm</b>, três gavetas cada, com '
  '<b>cantos arredondados</b> e frente em cava usinada. Corrediça oculta com '
  'amortecimento.', 3700),
 ('Quarto master', 'Rack suspenso de TV', 'rack',
  'Rack de <b>1,80 m</b> suspenso, quatro portas, cantos curvos e passa-cabo. '
  'Sem apoio no piso — a limpeza passa por baixo.', 2400),
 ('Closet master', 'Closet aberto · dois lados de 2,94 m', 'closet',
  'Os <b>dois lados</b> do closet, sem portas: cabideiro duplo em quatro vãos, '
  '<b>seis prateleiras superiores</b> e <b>cinco sapateiras</b>, todas com '
  '<b>LED embutido</b>, e <b>dois gaveteiros de quatro gavetas</b>. É o móvel '
  'em que o interno é a fachada — não há porta para escondê-lo.', 24000),
 ('Quarto dos pais', 'Roupeiro em L com nicho de TV', 'pais',
  'Roupeiro em L de <b>3,42 m + 2,30 m</b> do piso ao forro, <b>dez portas</b>, '
  'dez prateleiras, quatro cabideiros e <b>gaveteiro de cinco gavetas</b>. '
  '<b>Nicho de TV amadeirado embutido no corpo</b>, com reforço, passa-cabo e '
  'LED. A TV e o ponto elétrico são da obra.', 26500),
 ('Quarto da filha', 'Roupeiro com portas deslizantes Dominus', 'filha',
  'Roupeiro de <b>3,81 m</b> com <b>quatro folhas deslizantes</b> em sistema '
  '<b>Dominus (Rometal)</b> — trilhos ocultos, duplo amortecimento e '
  'desempenadores anti-empeno em todas as folhas. Dez prateleiras, quatro '
  'cabideiros e gaveteiro de quatro gavetas.', 16500),
 ('Quarto da filha', 'Bancada / penteadeira', None,
  'Bancada de <b>1,66 m</b> sob a janela, tampo em <b>25 mm</b>, duas gavetas '
  'e <b>LED sob o tampo</b>.', 2700),
 ('Quarto de visitas', 'Roupeiro de correr · 2,45 m', 'visitas',
  'Roupeiro de <b>2,45 m</b> com <b>três folhas deslizantes</b> em sistema '
  'Dominus, portas lisas sem puxador aparente. Oito prateleiras, três '
  'cabideiros e gaveteiro de quatro gavetas.', 14200),
 ('Escritório', 'Roupeiro · 2,50 m', 'escritorio',
  'Roupeiro de <b>2,50 m</b> do piso ao forro, quatro portas, oito prateleiras, '
  'três cabideiros e gaveteiro de três gavetas.', 9400),
 ('Escritório', 'Painel de TV com nichos', 'escritorio2',
  'Painel amadeirado de <b>3,00 m</b> com <b>seis nichos suspensos</b> '
  'iluminados em LED.', 5600),
 ('Escritório', 'Bancada de trabalho curva', None,
  'Bancada de <b>2,00 m</b> com <b>ponta curva</b>, tampo em <b>25 mm</b> para '
  'não fletir no vão, montante lateral e duas gavetas.', 5500),
 ('Sala de TV', 'Painel de TV · 4,00 × 2,60 m', None,
  'Painel <b>em MDF</b> ocupando a parede inteira, com rasgo horizontal de LED e '
  '<b>faixa ripada</b> de 55 réguas a passo constante. Na faixa inferior, '
  '<b>bancada suspensa de 3,20 m</b> com quatro portas em cava usinada, sem apoio '
  'no piso — a limpeza passa por baixo.', 19900),
]
TOTAL = sum(i[4] for i in ITENS)
assert TOTAL == 141800 and len(ITENS) == 12, (TOTAL, len(ITENS))

ENTRADA = 42500                      # 30,0% de 141.800, redondo
SALDO   = TOTAL - ENTRADA
assert SALDO == 99300 and abs(ENTRADA/TOTAL - 0.30) < 0.002

# [Jonathan 07/09] upgrade com 20% de desconto sobre o valor de tabela
UP_CLOSET_T, UP_TUDO_T = 10000, 31600         # tabela, na MC do pacote
UP_CLOSET = round(UP_CLOSET_T*0.80/100)*100   #  8.000
UP_TUDO   = round(UP_TUDO_T*0.80/100)*100     # 25.300
assert (UP_CLOSET, UP_TUDO) == (8000, 25300)
# custo direto do upgrade, de corte-eliuton2.py — para conferir a margem
CD_UP_CLOSET, CD_UP_TUDO = 3243, 10261
BASE_MC = 1 - 0.162 - 0.88*0.043
for _p, _c in ((UP_CLOSET, CD_UP_CLOSET), (UP_TUDO, CD_UP_TUDO)):
    assert BASE_MC - _c/_p > 0.35, (_p, _c)   # o desconto não fura o piso

# roupeiros — a lista separada que o cliente pediu para olhar primeiro
ROUPEIROS = [i for i in ITENS if i[1].startswith(('Closet aberto', 'Roupeiro'))]
TOTAL_ROUP = sum(i[4] for i in ROUPEIROS)
assert len(ROUPEIROS) == 5 and TOTAL_ROUP == 90600, (len(ROUPEIROS), TOTAL_ROUP)

def brl(v): return f'{v:,.0f}'.replace(',', '.')

CSS = (open(P/'css-proposta.css', encoding='utf-8').read() + """
/* ── memorial numerado · proposta SEM render ─────────────────────────── */
.mem{padding:4.4mm 0;border-bottom:1px solid var(--hair);}
.mem:last-child{border-bottom:none;}
.mem-h{display:flex;align-items:baseline;gap:5mm;}
.mem-n{font-family:'Cormorant Garamond',Georgia,serif;font-size:19pt;
  color:var(--gold-lt);font-weight:600;line-height:1;min-width:11mm;}
.mem-t{font-size:11.4pt;font-weight:700;letter-spacing:-.005em;}
.mem-a{margin-left:auto;font-size:6.8pt;letter-spacing:.18em;
  text-transform:uppercase;color:var(--gold);font-weight:700;
  white-space:nowrap;padding-top:1mm;}
.mem-d{color:var(--soft);font-size:8.9pt;line-height:1.58;margin:2mm 0 0 16mm;}
.mem-d b{color:var(--ink);}
.inv2{width:100%;border-collapse:collapse;font-size:8.8pt;margin-top:4mm;}
.inv2 th{font-size:6.6pt;letter-spacing:.16em;text-transform:uppercase;
  color:var(--mut);font-weight:700;border-bottom:1.5px solid var(--ink);
  padding:0 0 2mm;text-align:left;}
.inv2 th.r{text-align:right;}
.inv2 td{padding:2.1mm 0;border-bottom:1px solid var(--hair);vertical-align:top;}
.inv2 td.a{width:34mm;color:var(--gold);font-size:7.2pt;letter-spacing:.14em;
  text-transform:uppercase;font-weight:700;padding-top:2.7mm;}
.inv2 td.i{font-weight:600;}
.inv2 td.r{text-align:right;font-weight:700;white-space:nowrap;padding-left:6mm;}
.inv2 tr.tot td{border-bottom:0;border-top:2px solid var(--ink);
  padding-top:3.4mm;font-size:13pt;font-weight:700;}
.inv2 tr.tot td.r{font-family:'Cormorant Garamond',Georgia,serif;font-size:25pt;}
.up{margin-top:5mm;border:1px solid var(--gold-lt);border-radius:2px;
  background:var(--gold-pale);padding:5.5mm 6.5mm;}
.up .k{font-size:6.9pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.up .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:20pt;
  font-weight:600;margin-top:1.5mm;line-height:1.1;}
.up .d{color:var(--soft);font-size:8.6pt;margin-top:2.6mm;line-height:1.56;}
.up .d b{color:var(--ink);}
.up .l{display:grid;grid-template-columns:1fr auto;gap:4mm;
  border-top:1px solid rgba(156,122,60,.24);padding:2.6mm 0 0;margin-top:3.2mm;}
.up .l b{font-weight:700;white-space:nowrap;}
.pf{display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:6mm;}
.pf .c{border:1px solid var(--line);border-radius:2px;padding:5.5mm 6mm;}
.pf .c.hi{background:var(--deep);border-color:var(--deep);color:#F6F1E7;}
.pf .k{font-size:6.9pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.pf .c.hi .k{color:var(--gold-lt);}
.pf .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:29pt;
  line-height:1.05;font-weight:600;margin-top:2mm;}
.pf .s{color:var(--soft);font-size:8.4pt;margin-top:2.4mm;line-height:1.5;}
.pf .c.hi .s{color:#CFC6B4;}
.fr{display:grid;grid-template-columns:1fr 1fr;gap:4.5mm 8mm;margin-top:7mm;}
.fr .k{font-size:6.9pt;letter-spacing:.18em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.fr .d{color:var(--soft);font-size:8.6pt;margin-top:1.2mm;line-height:1.52;}
.fr .d b{color:var(--ink);}
.nota{margin-top:5mm;padding-left:4mm;border-left:2px solid var(--gold-lt);
  font-size:8.2pt;color:var(--soft);line-height:1.5;}
.nota b{color:var(--ink);}
""")

NP = 7
def foot(n):
    return (f'<div class="foot"><span>valvic marcenaria</span>'
            f'<span>{CLIENTE} · 2ª fase</span><span>{n} / {NP}</span></div>')

N_IT = [0]
def mem(it):
    amb, nome, _im, desc, v = it
    N_IT[0] += 1
    return (f'<div class="mem"><div class="mem-h">'
            f'<div class="mem-n serif">{N_IT[0]:02d}</div>'
            f'<div class="mem-t">{nome}</div>'
            f'<div class="mem-a">{amb}</div></div>'
            f'<div class="mem-d">{desc}</div></div>')

# ── 1 · capa ──────────────────────────────────────────────────────────────
p1 = f"""<div class="page cover"><div class="pad">
  <div class="cv-num serif">02</div>
  <div class="cv-brand">valvic marcenaria</div>
  <div class="cv-t serif" style="margin-top:26mm;">Proposta comercial<br>2ª fase</div>
  <div class="cv-nome serif">Os quartos,<br>os closets<br>e a sala.</div>
  <div class="cv-s">Cinco roupeiros, um closet, os painéis do quarto master e da
  sala, e as bancadas do escritório e do quarto da filha.</div>
  <div class="cv-meta" style="margin-top:auto;">
    <div><div class="k">Cliente</div><div class="v">{CLIENTE}</div></div>
    <div><div class="k">Obra</div><div class="v">{OBRA}</div></div>
    <div><div class="k">Data</div><div class="v">{DATA}</div></div>
  </div>
</div></div>"""

# ── 2 · memorial · os armários ────────────────────────────────────────────
ARM = [i for i in ITENS if i[1].startswith(('Closet aberto', 'Roupeiro'))]
RESTO = [i for i in ITENS if i not in ARM]

p2 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Memorial descritivo · os armários</div>
  <div class="h-sec serif">Os roupeiros primeiro.</div>
  <div class="rule"></div>
  <p class="lead">São <b>cinco armários</b> — o coração desta fase. Todos do piso
  ao forro, com cabideiro, prateleira e gaveteiro interno, e a mesma ferragem
  <b>Hardt</b> da 1ª fase: corrediça oculta com amortecimento e dobradiça com
  regulagem em três dimensões. <b>Interno em MDF branco</b>, com a opção de
  Gianduia Trama na página 6.</p>
  {''.join(mem(i) for i in ARM)}
  {foot(2)}
</div></div>"""

# ── 3 · memorial · os demais ──────────────────────────────────────────────
p3 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Memorial descritivo · os demais</div>
  <div class="h-sec serif">O master, o escritório<br>e a sala.</div>
  <div class="rule"></div>
  {''.join(mem(i) for i in RESTO)}
  {foot(3)}
</div></div>"""

# ── 4 · técnica ───────────────────────────────────────────────────────────
p4 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Como é feito</div>
  <div class="h-sec serif">A construção.</div>
  <div class="rule"></div>
  <p class="lead">O que não aparece na descrição de cada móvel, porque vale para
  todos eles. É aqui que um armário se diferencia de outro depois de instalado —
  não no desenho, que qualquer um copia, mas <b>no que se aciona todos os
  dias</b>.</p>
  <div class="fr" style="margin-top:6mm;">
    <div><div class="k">Chapa</div><div class="d"><b>MDF de 15 e 18 mm</b> na
      estrutura e nas portas, <b>25 mm</b> nos tampos de bancada — a espessura que
      não fleta no vão. Fundo em 6 mm.</div></div>
    <div><div class="k">Borda</div><div class="d"><b>Fita de borda extra fina de
      0,4 mm</b>, colada em máquina, e <b>meia esquadria</b> nos encontros
      aparentes: o canto fecha em 45°, sem topo de chapa à vista.</div></div>
    <div><div class="k">Corrediça</div><div class="d"><b>Oculta Hardt com
      amortecimento</b>, por baixo da gaveta — não aparece na lateral e fecha
      sozinha no fim do curso.</div></div>
    <div><div class="k">Dobradiça</div><div class="d"><b>Hardt com regulagem em
      três dimensões</b>: a fresta entre portas continua igual anos depois da
      instalação.</div></div>
    <div><div class="k">Deslizante</div><div class="d">Sistema <b>Dominus
      (Rometal)</b> nos roupeiros de correr — trilhos ocultos, duplo amortecimento
      e desempenadores anti-empeno em todas as folhas.</div></div>
    <div><div class="k">Iluminação</div><div class="d"><b>Fita de LED em perfil de
      alumínio</b>, embutida na própria peça, com driver dimensionado por
      circuito.</div></div>
    <div><div class="k">Puxador</div><div class="d"><b>Cava usinada na CNC</b> no
      próprio material, onde há puxador aparente. Nos deslizantes, folha lisa sem
      puxador.</div></div>
    <div><div class="k">Montagem</div><div class="d"><b>Equipe própria da Valvic</b>,
      do corte à instalação, com a mesma conferência de medida no local antes do
      corte.</div></div>
  </div>
  <div class="pf" style="margin-top:9mm;">
    <div class="c hi"><div class="k">Garantia</div>
      <div class="v">5 anos</div>
      <div class="s">Sobre <b>estrutura e ferragens</b> — a mesma linha Hardt com
      que a 1ª fase foi contratada em agosto. Cobre corrediça, dobradiça,
      deslizante, pistão e a integridade da caixaria.</div></div>
    <div class="c"><div class="k">Por que a ferragem define o prazo</div>
      <div class="s">A chapa não se desgasta: ela é cortada, colada e fica.
      <b>O que envelhece num armário é o que se move.</b> Num closet e em cinco
      roupeiros, corrediça e dobradiça são acionadas <b>milhares de vezes</b> —
      é onde o móvel se perde, e é o que a Hardt está comprando.</div></div>
  </div>

  <div class="nota" style="margin-top:8mm;"><b>O painel do espelho orgânico não
  está nesta proposta.</b> O painel amadeirado de 1,20 m com o espelho de corte
  orgânico, na parede lateral do quarto master, ficou fora do escopo a seu
  pedido. Se voltar, orçamos à parte.</div>
  {foot(4)}
</div></div>"""

# ── 5 · investimento ──────────────────────────────────────────────────────
linhas = ''
_amb = None
for amb, nome, im, desc, v in ITENS:
    a = amb if amb != _amb else ''
    _amb = amb
    linhas += (f'<tr><td class="a">{a}</td><td class="i">{nome}</td>'
               f'<td class="r">R$ {brl(v)}</td></tr>')

lroup = ''.join(f'<tr><td class="a">{a}</td><td class="i">{n}</td>'
                f'<td class="r">R$ {brl(v)}</td></tr>'
                for a, n, _i, _d, v in ROUPEIROS)

p5 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="h-sec serif">Item a item.</div>
  <div class="rule"></div>
  <table class="inv2">
    <thead><tr><th>Ambiente</th><th>Item</th><th class="r">Investimento</th></tr></thead>
    <tbody>{linhas}
      <tr class="tot"><td></td><td>Total · projeto completo</td>
        <td class="r">R$ {brl(TOTAL)}</td></tr>
    </tbody>
  </table>
  <div class="nota">Todos os itens do memorial estão neste valor, incluídos
  projeto executivo, ferragens, iluminação e a <b>montagem por equipe
  própria</b>. Na página seguinte, o recorte <b>só com os armários</b> e a opção
  de interno em Gianduia Trama.</div>
  {foot(5)}
</div></div>"""

# ── 6 · só os roupeiros + upgrade ─────────────────────────────────────────
p6 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Investimento · recorte</div>
  <div class="h-sec serif">Só os armários.</div>
  <div class="rule"></div>
  <p class="lead">Se a prioridade for guardar roupa antes de tudo, este é o
  recorte: <b>os cinco armários</b>, com a mesma ferragem, o mesmo prazo e a
  mesma garantia do projeto completo.</p>
  <table class="inv2">
    <thead><tr><th>Ambiente</th><th>Item</th><th class="r">Investimento</th></tr></thead>
    <tbody>{lroup}
      <tr class="tot"><td></td><td>Total · só os armários</td>
        <td class="r">R$ {brl(TOTAL_ROUP)}</td></tr>
    </tbody>
  </table>

  <div class="up">
    <div class="k">Opcional · vale para os dois recortes</div>
    <div class="t serif">Interno em MDF Gianduia Trama.</div>
    <div class="d">Um armário de <b>interno branco</b> é um armário. Um armário de
    <b>interno amadeirado</b> é um móvel — e a diferença aparece no único momento
    que importa: <b>quando a porta abre.</b> O branco é o fundo neutro que a
    indústria usa por ser o mais barato de produzir; ele some. O <b>Gianduia
    Trama</b> faz o contrário: dá profundidade, aquece a luz do LED e transforma
    prateleira, cabideiro e gaveta numa composição. É o detalhe que separa
    marcenaria de armário de loja — o que a visita nota sem saber explicar.
    <b>No closet aberto ele não é acabamento: é a fachada do ambiente.</b> E o que
    se percebe do móvel se transfere para a casa — interno assim é o que faz um
    imóvel ser lembrado como bem-feito, na visita, na foto e na hora de avaliar.
    O upgrade troca <b>caixaria, fundos, prateleiras e frentes de gaveteiro</b>;
    <b>as portas não mudam.</b></div>
    <div class="l"><span><b>Só o closet master</b> — o único móvel aberto</span>
      <b>+ R$ {brl(UP_CLOSET)}</b></div>
    <div class="l"><span><b>Todos os armários</b></span>
      <b>+ R$ {brl(UP_TUDO)}</b></div>
  </div>

  <table class="inv2" style="margin-top:5mm;">
    <thead><tr><th>Com o upgrade</th><th class="r">Só os armários</th>
      <th class="r">Projeto completo</th></tr></thead>
    <tbody>
      <tr><td class="i">Interno em branco</td>
        <td class="r">R$ {brl(TOTAL_ROUP)}</td>
        <td class="r">R$ {brl(TOTAL)}</td></tr>
      <tr><td class="i">+ Gianduia no closet master</td>
        <td class="r">R$ {brl(TOTAL_ROUP+UP_CLOSET)}</td>
        <td class="r">R$ {brl(TOTAL+UP_CLOSET)}</td></tr>
      <tr><td class="i">+ Gianduia em todos os armários</td>
        <td class="r">R$ {brl(TOTAL_ROUP+UP_TUDO)}</td>
        <td class="r">R$ {brl(TOTAL+UP_TUDO)}</td></tr>
    </tbody>
  </table>
  <div class="nota">Valores do upgrade sujeitos à confirmação da tabela do
  fornecedor da chapa Gianduia Trama.</div>
  {foot(6)}
</div></div>"""

# ── 7 · prazo, pagamento, garantia e fronteiras ───────────────────────────
p7 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Condições</div>
  <div class="h-sec serif">Prazo, pagamento<br>e fronteiras.</div>
  <div class="rule"></div>

  <div class="pf">
    <div class="c hi"><div class="k">Condição especial</div>
      <div class="v">R$ {brl(ENTRADA)}</div>
      <div class="s">Entrada na assinatura — 30% do total. Libera a compra de
      material e a entrada do projeto na fila de produção.</div></div>
    <div class="c"><div class="k">Saldo à vista, na entrega</div>
      <div class="v">R$ {brl(SALDO)}</div>
      <div class="s">Pago após a instalação concluída e conferida na obra.
      <b>Não há parcela durante a produção.</b></div></div>
  </div>

  <div class="fr" style="margin-top:7mm;">
    <div><div class="k">Prazo de entrega</div><div class="d"><b>{PRAZO}</b>,
      contados da assinatura, do pagamento da entrada e da medição final no
      local.</div></div>
    <div><div class="k">Garantia</div><div class="d"><b>{GARANTIA}</b> sobre
      estrutura e ferragens — a mesma linha Hardt com que a 1ª fase foi
      contratada.</div></div>
    <div><div class="k">Validade da proposta</div><div class="d">{VALIDADE}.</div></div>
    <div><div class="k">Escopo Valvic</div><div class="d">Projeto executivo,
      chapas, ferragens, iluminação em LED com driver, sistemas deslizantes,
      transporte e <b>montagem por equipe própria</b>.</div></div>
  </div>

  <div class="nota" style="margin-top:7mm;"><b>Medidas.</b> Os valores acima partem da planta cotada da
  arquiteta e do projeto de renders. <b>As medidas são conferidas no local antes
  do corte</b> — se alguma diferir do projeto, avisamos antes de produzir.</div>

  <div style="margin-top:auto;padding-top:8mm;border-top:1px solid var(--hair);">
    <div class="eyebrow">{ARQUITETA}</div>
  </div>
  {foot(7)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600;700&family=DM+Sans:wght@300;400;500;700&display=swap" '
        f'rel="stylesheet"><style>{CSS}</style></head><body>'
        f'{p1}{p2}{p3}{p4}{p5}{p6}{p7}</body></html>')

assert 'img-eliuton2' not in HTML and '<img' not in HTML   # proposta SEM render
(P/'proposta-eliuton2.html').write_text(HTML, encoding='utf-8')
pathlib.Path('/tmp/in.html').write_text(HTML, encoding='utf-8')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-eliuton2.pdf')], check=True)
print(f'proposta-eliuton2.pdf · total R$ {brl(TOTAL)} · '
      f'entrada {brl(ENTRADA)} + saldo {brl(SALDO)} · prazo {PRAZO}')
print(f'upgrade Gianduia: closet +{brl(UP_CLOSET)} · tudo +{brl(UP_TUDO)}')
