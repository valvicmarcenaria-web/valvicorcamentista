# -*- coding: utf-8 -*-
"""CAROL E VINÍCIUS — APRESENTAÇÃO PREMIUM, A4 paisagem, 15 páginas.

[Jonathan 19/08] "layout similar ao do Junior, um padrão mais premium".
Referência: "APRESENTAÇÃO — JUNIOR LAGOA SANTA OFICIAL.pdf" no Drive (140 pág.,
deck horizontal conduzido por imagem, uma abertura por ambiente). Este arquivo
segue essa gramática, na identidade da Valvic.

CINCO PEDIDOS DO JONATHAN, todos aplicados:
  1. garantias com glamour e vantagem  → página 13, número grande, Hettich em
     destaque escuro, e a garantia repetida na capa e no investimento
  2. sem medidas dos itens             → nenhuma cota em nenhuma das 9 páginas
  3. móveis contemplados por ambiente  → é o eixo das páginas 4 a 12
  4. gerenciamento das frentes         → página 13 inteira, oito frentes
  5. imagens do projeto no layout      → 15 perspectivas extraídas do caderno

VALORES: `corte-vinicius.py` COM RT de 10% [Jonathan 19/08], escada 30/35/38.
"""
import base64, os, subprocess

CLIENTE  = 'Carol e Vinícius'
OBRA     = 'Caderno de marcenaria · Jéssica Sollero'
DATA     = '19 de agosto de 2026'
VALIDADE = '7 dias corridos'
PRAZO    = 'Até 90 dias corridos'  # [Jonathan 21/08]
IMGDIR   = 'projetos/img-vinicius'

def img(nome):
    with open(f'{IMGDIR}/{nome}.jpg', 'rb') as f:
        return 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode()

# ── os nove ambientes: imagem, móveis (SEM medidas) e o destaque ──────────
AMB = [
 dict(n='01', nome='Lavabo', foto='lavabo-1',
      tag='Painel ripado com espelho integrado',
      mv=[('Painel ripado em MDF Areal', 'régua a régua, com o espelho integrado ao desenho'),
          ('Espelho prata integrado ao painel', 'colado sobre base própria, no miolo do ripado'),
          ('Iluminação em LED', 'superior e inferior, 4000 K')],
      nota=('O espelho nasce dentro do desenho',
            'A régua não para no espelho e recomeça depois: o painel é '
            'executado como peça única, e o espelho ocupa um vão previsto '
            'nele. É a diferença entre um espelho pendurado e um espelho '
            'que pertence à parede.')),
 dict(n='02', nome='Sala de jantar', foto='jantar-1',
      tag='Cristaleira, nicho e armário inferior',
      mv=[('Cristaleira em MDF Frapê', 'portas de vidro reflecta bronze com perfil de alumínio bronze e puxador Sotille'),
          ('Prateleiras de vidro incolor temperado', 'com LED por trás'),
          ('Nicho em MDF Trevi', 'o único módulo do projeto nesse acabamento, iluminado'),
          ('Armário inferior', 'gavetas e portas, puxador em mármore travertino'),
          ('Painel com porta de giro', 'puxador cava e perfil de alumínio na base'),
          ('Marco do vão em MDF Areal', 'acabamento em meia-esquadria'),
          ('Dois painéis com porta de correr', 'trilho embutido no gesso'),
          ('Sapateira em MDF Areal', 'prateleiras inclinadas')],
      nota=('Quatro puxadores em travertino',
            'As gavetas do armário inferior recebem puxador maciço em mármore '
            'travertino — peça de marmoraria, coordenada por nós.')),
 dict(n='03', nome='Sala de estar', foto='estar-3',
      tag='Buffet suspenso e painel de TV',
      mv=[('Buffet suspenso em MDF Frapê', 'seis gavetões, LED em cima e embaixo, puxador em travertino'),
          ('Painel da TV em MDF Areal', 'painel liso, do buffet até o armário superior'),
          ('Faixa ripada sob o televisor', 'a única ripada do ambiente — ripas de 3 × 2 cm com espaçamento de 3 e LED por baixo'),
          ('Armário superior com seis portas', 'frentes lisas em MDF Areal, interior em MDF Branco TX'),
          ('Duas colunas laterais com porta', 'quatro prateleiras cada, fechadas por porta inteira'),
          ('Rack em MDF Frapê', 'três gavetões, ventilação e passagem de cabo previstas')],
      nota=('Nove puxadores em travertino',
            'Seis no buffet e três no rack. O mesmo mármore do armário da sala '
            'de jantar, para que as duas paredes conversem.')),
 dict(n='04', nome='Varanda', foto='varanda-2',
      tag='Bancada curva com pés em tubo champagne',
      mv=[('Armário superior em MDF Areal', 'sem fundo, prateleiras de vidro incolor temperado, acabamento em tubinho champagne'),
          ('Armário inferior em MDF Frapê', 'nicho aberto para a adega e porta com puxador em travertino'),
          ('Bancada curva em MDF Areal', 'bordas arredondadas, fixação invisível e pés chumbados em tubo champagne')],
      nota=('A curva pede estrutura, não só desenho',
            'A bancada segue dois raios diferentes, tem cinco centímetros de '
            'espessura e encosta na parede sem mão-francesa aparente. Isso '
            'exige <strong>estruturação especial</strong> — reforço embutido no '
            'próprio tampo e pés chumbados em tubo champagne — dimensionada e '
            'coordenada por nós junto com a serralheria. É a peça do projeto '
            'que mais depende de execução, e está no valor.')),
 dict(n='05', nome='Quarto Rafael e Miguel', foto='rafael-1',
      tag='Mezanino estruturado em metalon',
      mv=[('Cama suspensa em mezanino', 'estrado em MDF Areal sobre estrutura de metalon, com LED na face inferior'),
          ('Guarda-corpo de corda', 'com vão e porta de acesso'),
          ('Escada em MDF Areal', 'degrau e espelho no mesmo material do mezanino'),
          ('Cama inferior com dois gavetões', 'frentes em MDF Frapê'),
          ('Duas cabeceiras e dois nichos', 'iluminados, com suporte em MDF Frapê'),
          ('Bancada de estudo em MDF Frapê', 'gavetas, puxador chanfrado, borda arredondada'),
          ('Armário em MDF Frapê', 'portas, gavetas e prateleiras, interior em MDF Branco TX'),
          ('Envelopamento do armário existente', 'três portas novas com espelho prata colado')],
      nota=('A estrutura vem antes do desenho',
            'O metalon do mezanino é dimensionado para carga de uso, não para '
            'a estética. A marcenaria veste a estrutura; ela não sustenta a '
            'cama sozinha.')),
 dict(n='06', nome='Quarto Maria Luísa', foto='maria-1',
      tag='Prateleiras orgânicas e cabeceira em gomos',
      mv=[('Fechamento de cortineiro em MDF Frapê', 'em duas paredes, com LED inferior e vão para persiana'),
          ('Painel e teto em MDF Areal', 'a madeira desce da parede e vira forro sobre a bancada'),
          ('Três prateleiras de desenho orgânico', 'fixação invisível e LED inferior'),
          ('Cabeceira estofada em gomos', 'tecido facto branco, com LED superior'),
          ('Bancada e penteadeira em L', 'gavetões, báscula a gás, báscula com espelho e divisória em acrílico'),
          ('Banco-armário com assento estofado', 'gaveta interna, tecido facto branco'),
          ('Envelopamento do armário existente', 'acabamento em MDF Frapê — montantes, testeira e base, para que o armário que já está lá desapareça no ambiente novo')],
      nota=('A curva é laminada, não recortada',
            'As prateleiras têm cinco centímetros de espessura e curva livre. '
            'Saem de duas lâminas usinadas e coladas — chapa única nessa '
            'espessura empenaria.')),
 dict(n='07', nome='Banho social', foto='banho-social-2',
      tag='Armário superior com portas de espelho',
      mv=[('Armário superior em MDF Frapê', 'três portas de correr em espelho prata'),
          ('Doze prateleiras internas', 'em MDF Branco TX'),
          ('Armário inferior', 'báscula com pistão a gás, dois gavetões tulha e um gavetão')],
      nota=('Espelho que trabalha',
            'As três folhas correm sobre trilho: o espelho é a porta, e o '
            'armário inteiro desaparece atrás dele.')),
 dict(n='08', nome='Quarto casal', foto='casal-1',
      tag='Painel de cabeceira e cristaleira iluminada',
      mv=[('Painel de cabeceira em MDF Areal', 'acabamento em meia-esquadria, instalado acima do rodapé'),
          ('Cabeceira estofada', 'Tecido Bouclé Elba Cor Branco Bruma'),
          ('Penteadeira em MDF Frapê', 'báscula a gás, báscula com espelho prata e divisória em acrílico'),
          ('Mesa de cabeceira', 'puxador em mármore travertino'),
          ('Cristaleira em MDF Areal', 'portas de vidro reflecta bronze, prateleiras de vidro e LED por trás'),
          ('Armário inferior em MDF Frapê', 'oito gavetas em duas colunas'),
          ('Duas portas em MDF Areal', 'uma de giro e uma de correr, puxador cava')],
      nota=('A cristaleira acende por dentro',
            'O LED fica atrás das prateleiras de vidro, não sobre elas: a luz '
            'atravessa o vidro e some, em vez de aparecer como fita.')),
 dict(n='09', nome='Banho casal', foto='banho-casal-2',
      tag='Iluminação frontal nos montantes',
      mv=[('Armário superior em MDF Frapê', 'duas portas de correr em espelho prata'),
          ('Iluminação frontal em LED 4000 K', 'embutida nos montantes fixos, ao lado do espelho'),
          ('Armário inferior', 'báscula com pistão a gás, gavetão tulha e gavetão')],
      nota=('Luz no rosto, não no teto',
            'Os montantes iluminados ficam nas laterais do espelho, na altura '
            'do rosto. É a posição que a maquiagem e o barbear pedem.')),
]

# ── as frentes que a Valvic coordena ──────────────────────────────────────
FRENTES = [
 ('01', 'Marcenaria', 'Corte em CNC e laminação de borda em coladeira automática, '
  'na nossa fábrica. Cerca de 60 chapas em MDF Areal, Frapê, Trevi e Branco TX.'),
 ('02', 'Serralheria', 'Estrutura de metalon do mezanino, pés chumbados em tubo '
  'champagne da bancada da varanda e o tubinho de acabamento do armário.'),
 ('03', 'Vidraçaria', 'Seis portas de vidro reflecta bronze com perfil de '
  'alumínio bronze e puxador Sotille, e onze prateleiras de vidro temperado.'),
 ('04', 'Espelharia', 'Oito folhas de espelho prata: o painel do lavabo, as '
  'portas de correr dos dois banheiros, os dois envelopamentos e as básculas.'),
 ('05', 'Estofaria', 'Cabeceira em gomos do quarto Maria Luísa, cabeceira em '
  'bouclé do quarto casal e o assento do banco — quadro nosso, revestimento do estofador.'),
 ('06', 'Marmoraria', 'Quinze puxadores maciços em travertino, usinados 6 × 6, '
  'distribuídos entre sala de jantar, sala de estar, varanda e quarto casal.'),
 ('07', 'Iluminação', 'Cerca de cinquenta metros de LED em perfil de alumínio, '
  'entre 3000 K e 4000 K conforme a prancha, embutidos na marcenaria.'),
 ('08', 'Alumínio', 'Perfis de proteção na base dos painéis apoiados no chão e '
  'os sistemas deslizantes com trilho embutido no forro de gesso.'),
]

GAR = [
 dict(anos='5', nome='Intermediária', pos='',
      x='A gaveta corre por baixo, escondida: some o trilho lateral e o vão '
        'útil cresce. O articulador da báscula é o mesmo da linha superior.',
      dobr='Dobradiça Hardt com amortecimento',
      corr='Corrediça oculta Hardt, fechamento suave',
      basc='Articulador Blum HK-xs', hi=False),
 dict(anos='10', nome='Superior', pos='A escolha da casa',
      x='Curso mais longo, carga maior, retorno mais macio e ciclo de teste '
        'muito acima do uso doméstico. Dobra a garantia.',
      dobr='Dobradiça Hettich Novisys',
      corr='Corrediça oculta Hettich Quadro',
      basc='Articulador Blum HK-xs', hi=True),
]

# ── upgrade de projeto — interior na cor  [Jonathan 21/08] ──────────────
# Substitui a linha Telescópica como terceiro degrau. Não é ferragem: é
# acabamento. Valores de `corte-vinicius.py`, seção UPGRADE DE PROJETO.
UP_5, UP_10 = 9800, 10800

# ── investimento · corte-vinicius.py COM RT ───────────────────────────────
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
TOT_UP = [TOT[0] + UP_5, TOT[1] + UP_10]
assert TOT_UP == [180000, 202500], TOT_UP

PAGTO = [
    ('Entrada de 30% + saldo em até 10× no cartão', '—'),
    ('Entrada de 50% + saldo em até 8× no cartão',  '3%'),
    ('Entrada de 70% + saldo em até 6× no cartão',  '5%'),
    ('Entrada de 70% + saldo por transferência',    '7%'),
]

FORA = [
    ('Pedras e marmoraria de bancada', 'As bancadas do lavabo e dos dois '
     'banheiros são fornecimento de marmoraria. Os quinze puxadores de '
     'travertino, esses sim, estão no valor.'),
    ('Eletrodomésticos, louças e metais', 'Adega, TV, cubas e torneiras. '
     'Prevemos o vão e a usinagem; precisamos das medidas de fábrica antes do corte.'),
    ('Persianas e cortinas', 'Há vão previsto para persiana nos cortineiros e '
     'nas cabeceiras; a persiana em si não está aqui.'),
    ('Alvenaria, gesso, revestimento e pintura', 'Inclusive o rasgo no forro '
     'para os trilhos embutidos das portas de correr.'),
    ('Elétrica e hidráulica', 'A iluminação embutida NA marcenaria é nossa; os '
     'pontos de energia e de água são da obra.'),
    ('Móveis soltos e decoração', 'Camas, poltronas, mesas, tapetes e o papel '
     'de parede do quarto Maria Luísa.'),
]

CSS = open('projetos/css-apresentacao.css', encoding='utf-8').read()
def brl(v): return f'{v:,.0f}'.replace(',', '.')
NP = 17
def foot(n, r=False):
    return (f'<div class="foot{" r" if r else ""}">'
            f'<span>Valvic&nbsp;·&nbsp;{CLIENTE}</span><span>{n} / {NP}</span></div>')

S = []

# 1 · capa
S.append(f"""<div class="slide dark"><div class="cv">
  <div class="cv-l">
    <div class="cv-brand">Valvic Marcenaria</div>
    <div style="margin-top:auto">
      <div class="eyebrow">Marcenaria planejada para</div>
      <div class="rule"></div>
      <div class="cv-nome">{CLIENTE}</div>
      <div class="cv-s">Nove ambientes, do lavabo ao mezanino —<br>
      sobre o caderno de Jéssica Sollero Design de Interiores</div>
    </div>
    <div class="cv-meta">
      <div><div class="k">Garantia Valvic</div><div class="v">Até 10 anos</div></div>
      <div><div class="k">Prazo de entrega</div><div class="v">{PRAZO}</div></div>
      <div><div class="k">Data</div><div class="v">{DATA}</div></div>
      <div><div class="k">Validade</div><div class="v">{VALIDADE}</div></div>
    </div>
  </div>
  <div class="cv-r"><img src="{img('casal-1')}"></div>
</div></div>""")

# 2 · abertura
S.append(f"""<div class="slide"><div class="pad">
  <div class="eyebrow">A proposta</div>
  <div class="rule"></div>
  <h1 class="h1">Nove ambientes executados<br>por uma só empresa.</h1>
  <p class="lead" style="margin-top:4mm">O caderno de marcenaria da Jéssica
  Sollero foi lido prancha por prancha — planta, elevação, corte e detalhe de
  cada ambiente. Desta leitura saiu o escopo das páginas seguintes: cada móvel
  contemplado, com o material que o projeto especifica. E, junto com a
  marcenaria, <strong>as sete outras frentes</strong> que este projeto exige —
  serralheria, vidraçaria, espelharia, estofaria, marmoraria, iluminação e
  alumínio — todas coordenadas por nós, num contrato só.</p>
  <div class="mos" style="grid-template-columns:repeat(4,1fr);margin-top:6mm">
    <figure><img src="{img('estar-4')}"><figcaption>Sala de estar</figcaption></figure>
    <figure><img src="{img('rafael-3')}"><figcaption>Quarto Rafael e Miguel</figcaption></figure>
    <figure><img src="{img('maria-2')}"><figcaption>Quarto Maria Luísa</figcaption></figure>
    <figure><img src="{img('varanda-1')}"><figcaption>Varanda</figcaption></figure>
  </div>
  {foot(2)}
</div></div>""")

# 3 · índice dos ambientes
CURTO = {'Quarto Rafael e Miguel': 'Rafael e Miguel',
         'Quarto Maria Luísa': 'Maria Luísa',
         'Quarto casal': 'Suíte do casal'}
tiles = ''.join(
    f'<figure><img src="{img(a["foto"])}">'
    f'<figcaption>{a["n"]} &nbsp; {CURTO.get(a["nome"], a["nome"])}</figcaption>'
    f'</figure>' for a in AMB)
S.append(f"""<div class="slide"><div class="pad">
  <div class="eyebrow">Os ambientes</div>
  <div class="rule"></div>
  <h2 class="h2" style="margin-bottom:5mm">Do lavabo ao mezanino.</h2>
  <div class="mos" style="grid-template-columns:repeat(3,1fr);grid-auto-rows:1fr;margin-bottom:6mm">{tiles}</div>
  {foot(3)}
</div></div>""")

# 4 a 12 · um ambiente por página
for k, a in enumerate(AMB):
    mv = ''.join(f'<div class="mv"><span class="b"></span><div>'
                 f'<span class="t">{t}</span> '
                 f'<span class="d">— {dsc}</span></div></div>' for t, dsc in a['mv'])
    S.append(f"""<div class="slide"><div class="amb">
      <div class="amb-img"><img src="{img(a['foto'])}">
        <div class="tag">{a['tag']}</div></div>
      <div class="amb-txt">
        <div class="amb-n">{a['n']}</div>
        <div class="eyebrow" style="margin-top:2mm">Móveis contemplados</div>
        <h2 class="h2" style="margin:1mm 0 4mm">{a['nome']}</h2>
        <div>{mv}</div>
        <div class="amb-nota"><div class="t">{a['nota'][0]}</div>
          <p>{a['nota'][1]}</p></div>
      </div>
    </div>{foot(4+k, r=True)}</div>""")

# 13 · frentes coordenadas
cards = ''.join(f'<div class="c"><div class="n">{n}</div>'
                f'<div class="t">{t}</div><div class="d">{d}</div></div>'
                for n, t, d in FRENTES)
S.append(f"""<div class="slide"><div class="pad">
  <div class="eyebrow">Coordenação</div>
  <div class="rule"></div>
  <h1 class="h1">Oito frentes, um interlocutor,<br>uma data de entrega.</h1>
  <p class="lead" style="margin-top:3.5mm">Neste projeto, mais de um terço do
  custo está fora da marcenaria propriamente dita. Serralheiro, vidraceiro,
  espelheiro, estofador e marmorista têm prazos, medidas e sequências próprias —
  e cada um deles depende de a marcenaria estar pronta na hora certa. <strong>A
  Valvic contrata, mede, agenda e responde por todos.</strong> O cliente trata
  com uma empresa; a obra recebe uma equipe.</p>
  <div class="fr">{cards}</div>
  {foot(13)}
</div></div>""")

# 14 · garantias — duas linhas
gc = ''.join(
  f'<div class="c{" hi" if g["hi"] else ""}" style="position:relative">'
  + (f'<div class="selo">{g["pos"]}</div>' if g['pos'] else '')
  + f'<div class="anos">{g["anos"]}</div>'
    f'<div class="unid">anos de garantia</div>'
    f'<div class="nm">{g["nome"]}</div><div class="x">{g["x"]}</div>'
    f'<div class="l">'
    f'<div class="k">Dobradiça</div><div class="v">{g["dobr"]}</div>'
    f'<div class="k">Corrediça</div><div class="v">{g["corr"]}</div>'
    f'<div class="k">Báscula</div><div class="v">{g["basc"]}</div>'
    f'</div></div>' for g in GAR)
S.append(f"""<div class="slide"><div class="pad">
  <div class="eyebrow">Garantia</div>
  <div class="rule"></div>
  <h1 class="h1">Cinco anos ou dez anos.<br>
  A diferença cabe numa gaveta.</h1>
  <p class="lead" style="margin-top:3.5mm">O desenho, a chapa, o acabamento e o
  esquadro são <strong>os mesmos nas duas</strong>. O que separa uma da outra é a
  ferragem — e ferragem se mede em ciclo de abertura. São 76 dobradiças, 39
  gavetas e 6 básculas nesta casa, abrindo e fechando todo dia. A garantia
  abaixo é <strong>garantia Valvic</strong>: nossa, escrita e assinada na
  entrega, não a do fabricante da ferragem.</p>
  <div class="gar" style="grid-template-columns:1fr 1fr;max-width:200mm">{gc}</div>
  {foot(14)}
</div></div>""")

# 15 · upgrade de projeto — interior na cor
S.append(f"""<div class="slide"><div class="amb">
  <div class="amb-img"><img src="{img('estar-4')}">
    <div class="tag">O interior, como o projeto especifica hoje</div></div>
  <div class="amb-txt">
    <div class="amb-n">+</div>
    <div class="eyebrow" style="margin-top:2mm">Upgrade de projeto</div>
    <h2 class="h2" style="margin:1mm 0 4mm">O interior na cor<br>da estrutura externa</h2>
    <p style="color:var(--soft);font-size:8.9pt">O caderno especifica o interior
    dos armários em <strong>MDF Branco TX</strong> — é o que a perspectiva ao
    lado mostra quando as portas abrem: fora em madeira, dentro em branco.</p>
    <p style="color:var(--soft);font-size:8.9pt;margin-top:3mm">O upgrade troca
    esse interior pela <strong>mesma cor da frente</strong>. O armário de MDF
    Areal fica Areal por dentro; o de MDF Frapê, Frapê. São
    <strong>104 m² de caixaria</strong> que deixam de ser brancos — prateleiras,
    laterais, fundos e o miolo das colunas.</p>
    <div class="fr" style="grid-template-columns:1fr 1fr;margin-top:5mm">
      <div class="c"><div class="n">5</div><div class="t">anos</div>
        <div class="d">R$ {brl(TOT[0])} &nbsp;→&nbsp;
        <strong style="color:var(--ink)">R$ {brl(TOT_UP[0])}</strong><br>
        upgrade de R$ {brl(UP_5)}</div></div>
      <div class="c"><div class="n">10</div><div class="t">anos</div>
        <div class="d">R$ {brl(TOT[1])} &nbsp;→&nbsp;
        <strong style="color:var(--ink)">R$ {brl(TOT_UP[1])}</strong><br>
        upgrade de R$ {brl(UP_10)}</div></div>
    </div>
    <div class="amb-nota" style="margin-top:5mm">
      <div class="t">Onde ele aparece</div>
      <p>O upgrade cobre <strong>o que se vê ao abrir a porta</strong>: caixaria,
      prateleiras e fundos. A caixa das gavetas segue em Branco TX nas duas
      configurações — é padrão mesmo em projeto premium, e trocá-la encareceria
      sem aparecer.</p></div>
  </div>
</div>{foot(15, r=True)}</div>""")

# 16 · investimento
linhas = ''.join(f'<tr><td class="l">{t}</td><td>{brl(a)}</td>'
                 f'<td class="hi">{brl(b)}</td></tr>' for t, a, b in INV)
S.append(f"""<div class="slide"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="rule"></div>
  <h2 class="h2" style="margin-bottom:4mm">Ambiente a ambiente, nas duas linhas.</h2>
  <div style="display:grid;grid-template-columns:1.35fr 1fr;gap:11mm;flex:1;min-height:0">
    <div>
      <table class="inv">
        <tr><th class="l">Ambiente</th><th>5 anos</th><th class="hi">10 anos</th></tr>
        {linhas}
        <tr class="tot"><td class="l">Investimento</td>
          <td>{brl(TOT[0])}</td><td class="hi">{brl(TOT[1])}</td></tr>
        <tr><td class="l" style="padding-top:3mm;color:var(--gold);font-weight:600">
          + Upgrade · interior na cor</td>
          <td style="padding-top:3mm">{brl(UP_5)}</td>
          <td class="hi" style="padding-top:3mm">{brl(UP_10)}</td></tr>
        <tr class="tot"><td class="l">Com o upgrade</td>
          <td>{brl(TOT_UP[0])}</td><td class="hi">{brl(TOT_UP[1])}</td></tr>
      </table>
    </div>
    <div style="display:flex;flex-direction:column">
      <div class="box" style="margin-top:0"><div class="t">O que está dentro do valor</div>
      <p>Projeto executivo, material, produção em CNC e coladeira automática
      próprias, <strong>e as oito frentes coordenadas</strong> — espelhos,
      portas de vidro, prateleiras temperadas, estofamento das cabeceiras,
      serralheria do mezanino, tubo champagne, puxadores de travertino e
      iluminação em LED. Mais transporte, entrega na obra e
      <strong>instalação e montagem por equipe própria da Valvic</strong>.</p></div>
      <div class="box"><div class="t">Coordenação de projeto</div>
      <p>O acompanhamento de Jéssica Sollero Design de Interiores está
      contemplado no valor, nas duas linhas.</p></div>
      <div class="box" style="border-left-color:var(--mut)">
      <div class="t" style="color:var(--mut)">Uma definição em aberto</div>
      <p>A <strong>linha da chapa</strong>. O caderno nomeia MDF Areal e MDF
      Frapê da Arauco, e este valor considera as duas na faixa de cor padrão.
      Se a linha específica for de acabamento especial, o conjunto é recotado
      antes de fechar.</p></div>
    </div>
  </div>
  <div class="mos" style="grid-template-columns:repeat(3,1fr);flex:none;
       height:25mm;margin-top:8mm">
    <figure><img src="{img('jantar-4')}"></figure>
    <figure><img src="{img('casal-4')}"></figure>
    <figure><img src="{img('rafael-6')}"></figure>
  </div>
  {foot(16)}
</div></div>""")

# 16 · condições
S.append(f"""<div class="slide"><div class="pad">
  <div class="eyebrow">Condições</div>
  <div class="rule"></div>
  <h2 class="h2" style="margin-bottom:2mm">Prazo, pagamento e fronteiras.</h2>
  <div class="three">
    <div>
      <div class="term"><div class="k">Prazo de entrega</div>
        <div class="v">{PRAZO}</div>
        <div class="s">Contados da aprovação do projeto executivo e da
        definição da chapa. Nove ambientes entregues por frentes, não todos de
        uma vez.</div></div>
      <div class="term"><div class="k">Conferência de medidas</div>
        <div class="v">Visita técnica antes do corte</div>
        <div class="s">O caderno carimba "conferir medidas no local" em todas as
        folhas, e concordamos: nada vai para a CNC antes da nossa medição na
        obra.</div></div>
      <div class="term"><div class="k">Validade da proposta</div>
        <div class="v">{VALIDADE}</div></div>
      <div class="term"><div class="k">Produção e montagem</div>
        <div class="v">Fábrica e equipe próprias</div>
        <div class="s">Corte, usinagem e laminação de borda na nossa CNC e
        coladeira; instalação e montagem pela nossa equipe. Não terceirizamos
        nem o que define o acabamento, nem quem entrega.</div></div>
    </div>
    <div>
      <table class="pay">
        <tr><td colspan="2" style="border:none;padding-bottom:1.4mm">
          <span class="eyebrow">Formas de pagamento</span></td></tr>
        {''.join(f'<tr><td>{c}</td><td class="d">{d}</td></tr>' for c, d in PAGTO)}
      </table>
      <p style="color:var(--mut);font-size:7.6pt;margin-top:2.5mm">
      O desconto por transferência devolve ao cliente a taxa de máquina que
      deixamos de pagar.</p>
      <div class="box"><div class="t">Garantia Valvic</div>
      <p>Até <strong>dez anos</strong> na linha Superior — escrita e assinada na
      entrega, cobrindo estrutura, ferragem e acabamento.</p></div>
    </div>
    <div class="fora">
      <div class="eyebrow">Não incluso</div>
      <div class="rule"></div>
      <ul>{''.join(f'<li><div class="k">{k}</div><div class="v">{v}</div></li>'
                   for k, v in FORA)}</ul>
    </div>
  </div>
  <div class="sig">
    <div class="ln">Valvic Marcenaria</div>
    <div class="ln">{CLIENTE}</div>
  </div>
  {foot(17)}
</div></div>""")

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600&family=DM+Sans:wght@300;400;500;600;700&display=swap" '
        f'rel="stylesheet"><style>{CSS}</style></head><body>{"".join(S)}</body></html>')

OUT_H = 'projetos/apresentacao-vinicius.html'
OUT_P = 'projetos/apresentacao-vinicius.pdf'
open(OUT_H, 'w', encoding='utf-8').write(HTML)
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
subprocess.run(['node', '/tmp/r2.js', OUT_P], check=True)
print(f'{OUT_H} · {OUT_P}  ({os.path.getsize(OUT_P)//1024} KB)')
print('Total: ' + ' · '.join(brl(t) for t in TOT))
