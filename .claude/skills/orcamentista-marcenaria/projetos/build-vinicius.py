# -*- coding: utf-8 -*-
"""CAROL E VINÍCIUS — PROPOSTA, 9 páginas.

Valores de `corte-vinicius.py`. Diferente da Luciana, aqui a geometria é
PEÇA A PEÇA: o caderno da Jéssica Sollero é vetorial e cotado, e as 49 pranchas
foram lidas uma a uma. O número tem o mesmo grau de confiança do Eliuton.

[Jonathan 19/08] escada 30/35/38 confirmada · chapa em COR confirmada ·
  **COM RT de 10%** para a Jéssica Sollero. Valores atualizados.
  Sem RT, para referência interna: R$ 121.800 / 141.100 / 155.900.

Esta é a versão TÉCNICA, A4 retrato, com as medidas de cada móvel. A versão
que vai ao cliente é `build-vinicius-premium.py` — deck A4 paisagem, sem cotas,
conduzido pelas perspectivas do projeto. As duas têm de bater no valor.

⚠ PRAZO e VALIDADE são premissas minhas — este projeto é maior que o da Luciana.
"""
import subprocess

CLIENTE  = 'Carol e Vinícius'
OBRA     = 'Caderno de marcenaria · Jéssica Sollero'
DATA     = '18 de agosto de 2026'
VALIDADE = '7 dias corridos'            # ⚠ premissa
PRAZO    = 'Até 90 dias corridos'       # [Jonathan 21/08]

CEN = [
    dict(n='I', nome='Intermediária', gar='5 anos',
         dobr='Dobradiça Hardt com amortecimento',
         corr='Corrediça oculta Hardt, fechamento suave',
         basc='Articulador Blum HK-xs',
         txt='A gaveta passa a correr por baixo, escondida: some o trilho '
             'lateral e o vão útil cresce. Nos seis gavetões de 70 cm do '
             'buffet da sala de estar, é o degrau que mais se sente.'),
    dict(n='II', nome='Superior', gar='10 anos',
         dobr='Dobradiça Hettich Novisys',
         corr='Corrediça oculta Hettich Quadro',
         basc='Articulador Blum HK-xs',
         txt='A corrediça Quadro tem curso mais longo, carga maior, retorno '
             'mais macio e ciclo de teste muito acima do uso doméstico. '
             'Dobra a garantia outra vez.'),
]

# ── o escopo, ambiente a ambiente ─────────────────────────────────────────
ESCOPO = [
 ('Lavabo', 'painel de 1,26 m', [
  ('Painel ripado com espelho', '126 × 148 em MDF Areal — ripas de 3 × 2 cm com '
   'espaçamento de 3 cm, espelho prata colado no miolo e fita de LED 4000 K em '
   'cima e embaixo. O ripado e o espelho são a mesma peça: o espelho nasce '
   'dentro do desenho, não colado sobre ele.'),
 ]),
 ('Sala de jantar', 'parede de 2,30 m · pé-direito 2,62 m', [
  ('Cristaleira', '230 × 114,5 × 35,5 prof em MDF Frapê — quatro portas de '
   'vidro reflecta bronze com perfil de alumínio bronze e puxador Sotille, '
   'quatro prateleiras de vidro incolor temperado e LED 3000 K por trás.'),
  ('Nicho em MDF Trevi', '230 × 66 × 35,5 prof — o único módulo do projeto '
   'nesse acabamento, com LED na parte superior.'),
  ('Armário inferior', '230 × 82 × 50 prof — quatro gavetas e quatro portas, '
   'com puxador em mármore travertino 6 × 6 nas gavetas.'),
  ('Painel e porta de giro', '120 × 262,5 em MDF Frapê, com porta de giro de '
   '76 × 210, puxador cava e perfil de alumínio na base.'),
  ('Marco do vão', '140 × 150 em MDF Areal, acabamento em meia-esquadria — '
   'o arremate que faz o vão virar moldura.'),
  ('Painel e porta de correr', '140 × 262,5 com porta de correr de 140 × 242,5, '
   'trilho embutido no gesso. De fora, o painel é contínuo: a porta some nele.'),
  ('Painel e porta de correr — elevação C', '120 × 262,5 com porta de correr de '
   '72 × 230, também com trilho embutido.'),
  ('Sapateira', '52,5 × 105 × 25 prof em MDF Areal — quatro prateleiras '
   'inclinadas, acabamento em meia-esquadria.'),
 ]),
 ('Sala de estar', 'parede de 4,43 m · painel de 2,28 m', [
  ('Buffet suspenso', '443,5 × 80 × 45 prof em MDF Frapê — seis gavetões de '
   '70 cm, LED 3000 K em cima e embaixo, puxador em mármore travertino 6 × 6 '
   'em cada gavetão. Solto do chão, o móvel devolve a linha da parede.'),
  ('Painel de TV ripado', '228 × 262,5 em MDF Areal — o painel inteiro é '
   'ripado, inclusive as seis portas do armário superior: 3 × 2 cm de ripa com '
   '3 cm de vão, do rodapé ao forro, sem interrupção. Interior em MDF Branco TX.'),
  ('Prateleiras laterais', 'oito peças de 34 × 30 prof, nas duas colunas '
   'abertas que ladeiam a TV.'),
  ('Rack', '228 × 50 × 61 prof em MDF Frapê — três gavetões de 76 cm com '
   'puxador em travertino, ventilação e passagem de cabo previstas.'),
 ]),
 ('Varanda', 'bancada de 3,00 m', [
  ('Armário superior sem fundo', '73 × 168 × 22 prof em MDF Areal — três '
   'prateleiras de vidro incolor temperado e acabamento em tubinho champagne. '
   'Sem fundo: a parede aparece através dele.'),
  ('Armário inferior', '90 × 80 × 50 prof em MDF Frapê — nicho aberto de '
   '30 × 68 para a adega e porta de 56, com puxador em travertino.'),
  ('Bancada curva', '300 × 40, cinco centímetros de espessura em MDF Areal — '
   'bordas arredondadas, fixação invisível na parede e pés chumbados em tubo '
   'champagne. A curva é desenhada, não é um retângulo com canto quebrado.'),
 ]),
 ('Quarto Rafael e Miguel', 'mezanino · pé-direito 2,80 m', [
  ('Cama suspensa com mezanino', 'estrado de 203 × 150 em MDF Areal sobre '
   'estrutura de metalon, vão com porta de acesso, guarda-corpo de corda e LED '
   '4000 K na face inferior. A estrutura metálica é dimensionada para carga de '
   'uso, não para o desenho.'),
  ('Escada', 'nove degraus de 17 cm em MDF Areal, altura total 170 — degrau e '
   'espelho no mesmo material do mezanino.'),
  ('Cama inferior', '203 × 105 com dois gavetões de 93,5 em MDF Frapê.'),
  ('Cabeceiras e nichos', 'duas cabeceiras de 146 × 35 com LED 3000 K e dois '
   'nichos de 146 × 23 com suporte em MDF Frapê e luz de leitura.'),
  ('Bancada de estudo', '113 × 46 prof em MDF Frapê — duas gavetas, puxador '
   'chanfrado, borda arredondada.'),
  ('Armário', '104,5 × 170 × 40 prof em MDF Frapê — quatro portas, duas gavetas '
   'e prateleiras, interior em MDF Branco TX.'),
  ('Envelopamento do armário existente', '204 × 280 em MDF Frapê — três portas '
   'novas com espelho prata colado. O corpo que já está lá some dentro do '
   'acabamento novo.'),
 ]),
 ('Quarto Maria Luísa', 'parede de 3,18 m · pé-direito 2,80 m', [
  ('Fechamento de cortineiro', '318,5 e 214,5 em MDF Frapê, com LED 3000 K '
   'inferior — em duas paredes, com vão para a persiana.'),
  ('Painel e teto em MDF Areal', '60 × 266 e 169,5 × 60, acabamento em '
   'meia-esquadria — a madeira desce da parede e vira forro sobre a bancada.'),
  ('Prateleiras de desenho orgânico', 'três peças de 170, 170 e 125 com retorno '
   'de canto, cinco centímetros de espessura, fixação invisível e LED inferior. '
   'A curva é usinada em duas lâminas laminadas, não recortada em chapa única.'),
  ('Cabeceira estofada em gomos', '4,14 m em duas paredes, tecido facto branco, '
   'com vão posterior para persiana e LED 3000 K superior. A marcenaria executa '
   'o quadro; o revestimento é do estofador e está no valor.'),
  ('Bancada e penteadeira em L', '172 + 167,5 × 50 prof em MDF Frapê — dois '
   'gavetões, duas gavetas, báscula a gás, báscula com espelho prata colado, '
   'divisória interna em acrílico e LED 4000 K no espelho.'),
  ('Banco-armário com assento estofado', '50 × 80 × 50 prof — gaveta interna e '
   'assento em tecido facto branco.'),
  ('Envelopamento do armário existente', '188,5 × 266 em MDF Frapê, três portas '
   'com espelho prata colado.'),
 ]),
 ('Banho social', '', [
  ('Armário superior', '140 × 120,5 × 15 prof em MDF Frapê — três portas de '
   'correr em espelho prata e doze prateleiras internas em MDF Branco TX.'),
  ('Armário inferior', '140 × 91 × 35 prof — báscula com pistão a gás, dois '
   'gavetões tulha e um gavetão, puxador chanfrado.'),
 ]),
 ('Quarto casal', 'painel de 2,72 m', [
  ('Painel da cabeceira', '272,5 × 256 em MDF Areal, acabamento em '
   'meia-esquadria, instalado acima do rodapé.'),
  ('Cabeceira estofada', '177,5 em Tecido Bouclé Elba Cor Branco Bruma — quadro '
   'de marcenaria e revestimento do estofador, dentro do valor.'),
  ('Penteadeira', '52 × 50 prof em MDF Frapê — báscula a gás, báscula com '
   'espelho prata colado, divisória interna em acrílico e LED 4000 K.'),
  ('Mesa de cabeceira', '45 × 50 prof em MDF Frapê — uma gaveta com puxador em '
   'mármore travertino.'),
  ('Cristaleira', '100,5 × 181 × 30 prof em MDF Areal — duas portas de vidro '
   'reflecta bronze com puxador Sotille, quatro prateleiras de vidro e LED '
   '3000 K por trás.'),
  ('Armário inferior da cristaleira', '100,5 × 85 × 30 prof em MDF Frapê — oito '
   'gavetas em duas colunas.'),
  ('Duas portas em MDF Areal', 'uma de giro de 97,5 × 242 e uma de correr de '
   '59 × 242, puxador cava e perfil de alumínio na base.'),
 ]),
 ('Banho casal', '', [
  ('Armário superior', '112 × 120,5 × 15 prof em MDF Frapê — duas portas de '
   'correr em espelho prata, quatro prateleiras e iluminação frontal em LED '
   '4000 K nos montantes fixos.'),
  ('Armário inferior', '112 × 91 × 51,5 prof — báscula com pistão a gás, '
   'gavetão tulha e gavetão, puxador chanfrado.'),
 ]),
]

# ── investimento por ambiente · valores de corte-vinicius.py ──────────────
# [Jonathan 21/08] Telescópica fora · correções de escopo na sala de estar e
# no quarto Maria Luísa · o 3º degrau vira UPGRADE DE PROJETO (interior na cor).
INV = [
 ('Lavabo',                  1900,   2200),
 ('Sala de jantar',         31800,  35800),
 ('Sala de estar',          34800,  39100),
 ('Varanda',                 5800,   6500),
 ('Quarto Rafael e Miguel', 30500,  34400),
 ('Quarto Maria Luísa',     27200,  30700),
 ('Banho social',            9100,  10200),
 ('Quarto casal',           20600,  23200),
 ('Banho casal',             8500,   9600),
]
TOT = [sum(i[k] for i in INV) for k in (1, 2)]
assert TOT == [170200, 191700], TOT
UP_5, UP_10 = 9800, 10800
TOT_UP = [TOT[0] + UP_5, TOT[1] + UP_10]

PAGTO = [
    ('Entrada de 30% + saldo em até 10× no cartão', '—'),
    ('Entrada de 50% + saldo em até 8× no cartão',  '3%'),
    ('Entrada de 70% + saldo em até 6× no cartão',  '5%'),
    ('Entrada de 70% + saldo por transferência',    '7%'),
]

FORA = [
    ('Pedras e marmoraria', 'As bancadas do lavabo e dos dois banheiros são '
     'fornecimento de marmoraria. Os quinze puxadores de travertino 6 × 6, '
     'esses sim, estão no valor.'),
    ('Eletrodomésticos, louças e metais', 'Adega da varanda, TV, cubas e '
     'torneiras. Prevemos o vão e a usinagem; o aparelho é do cliente — '
     'precisamos das medidas de fábrica antes do corte.'),
    ('Persianas e cortinas', 'Há vão previsto para persiana nas cabeceiras dos '
     'quartos Maria Luísa e nos cortineiros; a persiana em si não está aqui.'),
    ('Alvenaria, gesso, revestimento e pintura', 'Inclusive o rasgo no forro '
     'para os trilhos embutidos das portas de correr, que é obra de gesseiro.'),
    ('Elétrica e hidráulica', 'A iluminação embutida NA marcenaria é nossa; os '
     'pontos de energia e de água são da obra.'),
    ('Móveis soltos e decoração', 'Camas, poltronas, mesas, tapetes e o papel '
     'de parede do quarto Maria Luísa.'),
]

CSS = open('projetos/css-proposta.css', encoding='utf-8').read()

def brl(v): return f'{v:,.0f}'.replace(',', '.')
NP = 8
def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria · {CLIENTE}</span>'
            f'<span>{OBRA}</span><span>{n} / {NP}</span></div>')

def bloco(amb, sub, itens, mt='5.5mm'):
    h = (f'<div style="margin-top:{mt}"><div class="eyebrow">{amb}'
         + (f' &nbsp;·&nbsp; {sub}' if sub else '') + '</div>'
         '<div class="rule" style="margin:5px 0 3mm"></div>')
    for t, d in itens:
        h += (f'<div class="it" style="padding:2.0mm 0"><div>'
              f'<span class="it-t" style="font-size:9.6pt">{t}</span>'
              f'<span class="it-d" style="display:inline;margin-left:5px">'
              f'{d}</span></div></div>')
    return h + '</div>'

p1 = f"""<div class="page cover"><div class="pad">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div style="margin-top:auto">
    <div class="eyebrow">Proposta de marcenaria planejada para</div>
    <div class="rule"></div>
    <div class="cv-nome" style="font-size:62pt">{CLIENTE}</div>
    <div class="cv-s">Nove ambientes, do lavabo ao mezanino,<br>
    sobre o caderno de Jéssica Sollero</div>
  </div>
  <div class="cv-meta">
    <div><div class="k">Prazo de entrega</div><div class="v">{PRAZO}</div></div>
    <div><div class="k">Data</div><div class="v">{DATA}</div></div>
    <div><div class="k">Validade</div><div class="v">{VALIDADE}</div></div>
  </div>
</div></div>"""

p2 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">O que está sendo proposto</div>
  <div class="rule"></div>
  <h2 class="h-sec">Quarenta e nove pranchas,<br>lidas uma a uma.</h2>
  <p class="lead" style="margin-top:4mm">O levantamento foi feito sobre o
  caderno de marcenaria completo — planta, elevação, corte e detalhe de cada
  ambiente. São <strong>214 m² de chapa</strong> em MDF Areal e MDF Frapê da
  Arauco, com interior em MDF Branco TX e o nicho da sala de jantar em MDF
  Trevi, como pede o projeto.</p>
  {bloco(*ESCOPO[0], mt='6mm')}
  {bloco(*ESCOPO[1])}
  {foot(2)}
</div></div>"""

p3 = f"""<div class="page"><div class="pad">
  {bloco(*ESCOPO[2], mt='0')}
  {bloco(*ESCOPO[3])}
  <div class="box" style="margin-top:6mm"><div class="t">Sobre o ripado</div>
  <p>O projeto crava a régua: <strong>3 × 2 cm com 3 cm de espaçamento</strong>.
  Não é uma textura comprada pronta — é régua cortada, fitada e colada uma a
  uma sobre o painel de fundo. No painel de TV da sala de estar são mais de
  cento e cinquenta réguas, e o desenho só fecha se o passo não variar.</p></div>
  {foot(3)}
</div></div>"""

p4 = f"""<div class="page"><div class="pad">
  {bloco(*ESCOPO[4], mt='0')}
  {bloco(*ESCOPO[5])}
  {foot(4)}
</div></div>"""

p5 = f"""<div class="page"><div class="pad">
  {bloco(*ESCOPO[6], mt='0')}
  {bloco(*ESCOPO[7])}
  {bloco(*ESCOPO[8])}
  <div class="box" style="margin-top:6mm"><div class="t">O que atravessa o projeto inteiro</div>
  <p><strong>Cinquenta metros de LED</strong> em perfil de alumínio embutido na
  marcenaria, entre 3000 K e 4000 K conforme a prancha. <strong>Quinze
  puxadores em mármore travertino 6 × 6</strong>, no buffet, no rack, no armário
  da sala de jantar, na varanda e na mesa de cabeceira do casal. E o
  <strong>veio</strong>: a nota que se repete em todas as folhas manda seguir o
  desenho da madeira nos encontros. Isso trava a rotação das peças no plano de
  corte e é a razão de o aproveitamento de chapa ser menor aqui do que num
  projeto em cor lisa. Está considerado no valor.</p></div>
  {foot(5)}
</div></div>"""

cen_html = ''.join(
    f'<div class="cen{" hi" if c["n"]=="II" else ""}">'
    f'<div class="cen-h"><div class="cen-n">{c["n"]}</div>'
    f'<div class="cen-t">{c["nome"]}</div>'
    f'<div class="cen-g">Garantia {c["gar"]}</div></div>'
    f'<div class="cen-x">{c["txt"]}</div>'
    f'<div class="cen-l">'
    f'<div><div class="k">Dobradiça</div><div class="v">{c["dobr"]}</div></div>'
    f'<div><div class="k">Corrediça</div><div class="v">{c["corr"]}</div></div>'
    f'<div><div class="k">Báscula</div><div class="v">{c["basc"]}</div></div>'
    f'</div></div>' for c in CEN)

p6 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Três configurações</div>
  <div class="rule"></div>
  <h2 class="h-sec">O que muda entre elas<br>é o movimento.</h2>
  <p class="lead" style="margin-top:4mm">O desenho, a chapa, o acabamento e o
  esquadro são <strong>os mesmos nas três</strong>. O que separa uma da outra é
  a ferragem — e ferragem se mede em ciclo de abertura, amortecimento e
  regulagem. São <strong>76 dobradiças, 39 gavetas e 6 básculas</strong> neste
  projeto: é muita coisa abrindo e fechando todo dia.</p>
  <div style="margin-top:5mm">{cen_html}</div>
  <div class="box"><div class="t">Uma observação honesta</div>
  <p>A garantia acima é <strong>garantia Valvic</strong> — nossa, escrita e
  assinada na entrega. Não é a garantia do fabricante da ferragem, que não faz
  parte do que a gente vende.</p></div>
  {foot(6)}
</div></div>"""

linhas = ''.join(
    f'<tr><td class="l">{t}</td><td>{brl(a)}</td>'
    f'<td class="hi">{brl(b)}</td></tr>' for t, a, b in INV)

p7 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="rule"></div>
  <h2 class="h-sec">Ambiente a ambiente,<br>nas duas linhas.</h2>
  <table class="inv" style="margin-top:4mm">
    <tr><th class="l">Ambiente</th><th>I · 5 anos</th>
        <th class="hi">II · 10 anos</th></tr>
    {linhas}
    <tr class="tot"><td class="l">Investimento</td>
      <td>{brl(TOT[0])}</td><td class="hi">{brl(TOT[1])}</td></tr>
    <tr><td class="l" style="padding-top:2.5mm;color:var(--gold);font-weight:600">
      + Upgrade · interior na cor da estrutura externa</td>
      <td style="padding-top:2.5mm">{brl(UP_5)}</td>
      <td class="hi" style="padding-top:2.5mm">{brl(UP_10)}</td></tr>
    <tr class="tot"><td class="l">Com o upgrade</td>
      <td>{brl(TOT_UP[0])}</td><td class="hi">{brl(TOT_UP[1])}</td></tr>
  </table>
  <div class="box"><div class="t">O que está dentro do valor</div>
  <p>Projeto executivo, material, produção em CNC e coladeira automática
  próprias, e as oito frentes coordenadas — espelhos, portas de vidro,
  prateleiras temperadas, estofamento das cabeceiras, serralheria do mezanino,
  tubo champagne, puxadores de travertino e iluminação em LED. Mais transporte,
  entrega na obra e <strong>instalação e montagem por equipe própria da
  Valvic</strong>. O acompanhamento de Jéssica Sollero Design de Interiores está
  contemplado no valor, nas duas linhas.</p></div>
  <div class="box" style="border-left-color:var(--mut)">
  <div class="t" style="color:var(--mut)">Uma definição ainda em aberto</div>
  <p>A <strong>linha da chapa</strong>. O caderno nomeia MDF Areal e MDF Frapê
  da Arauco, e este valor considera as duas na faixa de cor padrão. Se a linha
  específica for de acabamento especial, o conjunto é recotado antes de
  fechar — a chapa é o maior item isolado deste orçamento.</p></div>
  {foot(7)}
</div></div>"""

p8 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Condições</div>
  <div class="rule"></div>
  <h2 class="h-sec">Prazo, pagamento<br>e fronteiras.</h2>
  <div class="two" style="margin-top:7mm">
    <div>
      <div class="term"><div class="k">Prazo de entrega</div>
        <div class="v">{PRAZO}</div>
        <div class="s">Contados da aprovação do projeto executivo e da
        definição da chapa. Nove ambientes entregues por frentes, não todos de
        uma vez.</div></div>
      <div class="term"><div class="k">Conferência de medidas</div>
        <div class="v">Visita técnica antes do corte</div>
        <div class="s">O caderno carimba "conferir medidas no local" em todas
        as folhas, e concordamos: nada vai para a CNC antes da nossa medição na
        obra.</div></div>
      <div class="term"><div class="k">Validade da proposta</div>
        <div class="v">{VALIDADE}</div></div>
      <div class="term"><div class="k">Produção e montagem</div>
        <div class="v">Fábrica e equipe próprias, do corte à instalação</div>
        <div class="s">Corte, usinagem da cava e laminação de borda na nossa CNC
        e coladeira automática; instalação e montagem pela nossa equipe. Não
        terceirizamos nem o que define o acabamento, nem quem entrega.</div></div>
      <table class="pay" style="margin-top:4mm">
        <tr><td colspan="2" style="border:none;padding-bottom:1mm">
          <span class="eyebrow">Formas de pagamento</span></td></tr>
        {''.join(f'<tr><td>{c}</td><td class="d">{d}</td></tr>' for c, d in PAGTO)}
      </table>
      <p style="color:var(--mut);font-size:7.9pt;margin-top:2.5mm">
      O desconto por transferência devolve ao cliente a taxa de máquina que
      deixamos de pagar.</p>
    </div>
    <div class="fora">
      <div class="eyebrow">Não incluso nesta proposta</div>
      <div class="rule"></div>
      <ul>{''.join(f'<li><div class="k">{k}</div><div class="v">{v}</div></li>'
                   for k, v in FORA)}</ul>
    </div>
  </div>
  <div class="sig">
    <div class="ln">Valvic Marcenaria</div>
    <div class="ln">{CLIENTE}</div>
  </div>
  {foot(8)}
</div></div>"""

HTML = (f'<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        f'<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        f'wght@400;500;600&family=DM+Sans:wght@300;400;500;600;700&display=swap" '
        f'rel="stylesheet"><style>{CSS}</style></head><body>'
        f'{p1}{p2}{p3}{p4}{p5}{p6}{p7}{p8}</body></html>')

OUT_H, OUT_P = 'projetos/proposta-vinicius.html', 'projetos/proposta-vinicius.pdf'
open(OUT_H, 'w', encoding='utf-8').write(HTML)
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
subprocess.run(['node', '/tmp/r.js', OUT_P], check=True)
print(f'{OUT_H} · {OUT_P}')
print('Total: ' + ' · '.join(brl(t) for t in TOT))
