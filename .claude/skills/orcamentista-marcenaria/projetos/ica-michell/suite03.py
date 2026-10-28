# -*- coding: utf-8 -*-
"""ICA · SUÍTE 03 — levantamento peça por peça  [28/10/2026]

páginas 208 a 221 · seis detalhamentos, seis itens, seis folhas de detalhe.
É o quarto da criança, e é o ambiente mais DESENHADO do executivo inteiro:
escada-gaveteiro, pórtico de piso a teto, beliche com rede de cordas,
estante de 3 m, fachada de casinha com telhado ripado e escrivaninha de
encaixe. Quatro elevações e nenhuma peça órfã — tudo que a elevação mostra
tem DET, o que não aconteceu no Banho Master.

⭐⭐ DUAS CORES MANDAM NO QUARTO INTEIRO, e elas se alternam de propósito:
  · MDF PARIS — Guararapes — é a ESTRUTURA e tudo que é piso de móvel:
    degraus da escada, pórtico inteiro, camas, armário da mesa e o painel
    de encaixes da escrivaninha;
  · MDF AZUL ASTRAL — Duratex — é a COR: gavetas da escada, a estante do
    DET 04 inteira, o ripado do telhado, a bicama, a prateleira móvel e
    TODA moldura de 5 cm.
  ⭐ A terceira é PALHA INDIANA SEXTAVADA — Duratex — e só aparece em
    frente: as quatro portas e as duas básculas do DET 05 e as três
    gavetas e a porta do DET 06.

⭐⭐ TODA MOLDURA DAQUI É RÉGUA, NÃO PEÇA INTEIRA. A regra da casa fecha nos
  dois sentidos: moldura da MESMA cor da frente sai em peça inteira de
  6 mm usinada na router; moldura de OUTRA cor sai em quatro réguas. Aqui
  a frente é Palha Indiana e a moldura é Azul Astral — é o mesmo caso do
  aparador da Suíte Hóspedes e da bancada do Banho Mariana. ⛔ São dez
  frentes emolduradas e quarenta réguas, com filetagem manual nas de 5 cm.

⛔⛔ O PÉ-DIREITO DE 300 MORDE QUATRO VEZES: as duas laterais do pórtico
  (resolvidas com emenda escondida na linha do recorte da escada), as duas
  laterais da estante do DET 04, os dois montantes da cama e os dois
  montantes do DET 05. ⭐ Só as do pórtico eu emendei de propósito, porque
  são painel largo e a emenda some atrás do degrau; as outras são peça
  estreita e entram na lista de peças ALTAS para o senhor decidir.

⭐ O PÓRTICO NÃO É PAINEL DE 3 CM MACIÇO, é 15 mm sobre engradado de
  sarrafo, que é o que a casa fechou na Suíte Mariana. ⛔ A diferença aqui
  é que o pórtico tem DOIS lados à vista — você atravessa o vão da porta
  dele — então as duas laterais levam pele dos dois lados, e só o painel
  superior, que morre no teto, leva uma pele só.

⚠ A REDE DE CORDAS DA CAMA NÃO É MARCENARIA, mas a furação dos montantes
  é. São dois montantes de 4 × 4 × 300 em MDF sobre alma, e a rede de 149
  de altura pendura neles — quem dimensiona a corda e o nó não somos nós.
"""
from base import (P, gaveta, ripado, ALT_MAX, CHAPA_C, DOBRADICA)

PA18, PA15, PA6 = 'MDF Paris 18', 'MDF Paris 15', 'MDF Paris 6'
AA18, AA15, AA6 = 'MDF Azul Astral 18', 'MDF Azul Astral 15', 'MDF Azul Astral 6'
PI15 = 'MDF Palha Indiana Sextavada 15'
BR15, BR6 = 'MDF Branco TX 15', 'MDF Branco TX 6'

I1 = 'DET 01 Escada com gavetas'
I2 = 'DET 02 Pórtico'
I3 = 'DET 03 Cama'
I4 = 'DET 04 Estante'
I5 = 'DET 05 Estante da casinha'
I6 = 'DET 06 Mesa'

# ⭐ ripa de 3 com vão de 1 é o ÚNICO ripado do projeto que vem COTADO na
#   prancha: "ripas de 3cm e espaçamento de 1cm", escrito no DET 05. Em
#   todos os outros ambientes a largura da ripa foi medida por mim no
#   desenho em 1/20 e virou dúvida. Aqui não há o que perguntar.
RIPA_L, RIPA_V, RIPA_W = 3.0, 1.0, 260.0

SUITE03 = [
 # ══ ITEM 01 · ESCADA COM GAVETAS — 157 × 72 × 139 ═══════════════════
 #  DET. 01 VISTA FRONTAL   72 = 4 (vão para pórtico) + 68 de corpo
 #                          altura 5 × (2 + 26) = 140 ≈ 139 · cinco gavetas
 #  DET. 01 VISTA LATERAL   157 = 5 degraus de 31 · 5 espelhos de 28
 #  DET. 01 VISTA SUPERIOR  157 × 72, os cinco degraus de 31 à vista
 #  ⭐ os 4 cm do VISTA FRONTAL são VÃO, não peça: é a folga que a lateral
 #    do pórtico ocupa. O corpo da escada tem 68, e é isso que se corta.
 P('Lateral escalonada',    I1, 157, 139, 2, AA15, (1, 1),
   '⭐ a peça é um perfil de escada, mas o corte sai de um retângulo de '
   '157 × 139 — é assim que ela ocupa a chapa, e é assim que entra no '
   'plano de corte · as duas aparecem, a de fora para o quarto e a de '
   'dentro para o vão do pórtico'),
 P('Degrau',                I1, 68, 31, 5, PA18, (2, 2),
   '⭐ 18 mm: é piso de criança, sobe e desce todo dia · os cinco degraus '
   'da VISTA SUPERIOR, 31 cada, aparecem pelas quatro arestas'),
 P('Topo e costas do degrau alto', I1, 68, 139, 1, AA15, (1, 1),
   'A face cheia do lado alto da escada, que na PERSPECTIVA é a parede '
   'azul inteira de 139 — ela fecha a escada contra a cama'),
 P('Frente da gaveta',      I1, 68, 26, 5, AA15, (2, 2),
   '⭐ cinco frentes iguais de 26, uma por espelho de degrau · a cava '
   'semicircular do desenho é o único puxador que a prancha desenha neste '
   'ambiente inteiro'),
 *gaveta(I1, 65, 28, 22, 5, 'Caixa de gaveta', BR15, BR6),

 # ══ ITEM 02 · PÓRTICO — 370 × 121 × 300 ═════════════════════════════
 #  DET. 02 VISTA FRONTAL   370 de vão, 270 de LED, pé-direito 300
 #  DET. 02 VISTA SUPERIOR  369 × 121
 #  DET. 02 VISTA LATERAL   121 × 300 · 161 cheio + recorte da escada de
 #                          3 × 28 por 33 + 22 · sobra 50 de pé embaixo
 #  DET. 02 PERSPECTIVA     vão da porta 71 × 210 · verga de 90 · pé de 50
 #  ⭐ 15 mm sobre engradado de sarrafo dá os 3 cm desenhados — não são
 #    duas chapas coladas. O painel superior morre no teto e leva UMA
 #    pele; as duas laterais têm os dois lados à vista e levam DUAS.
 P('Painel superior · pele', I2, 185, 121, 2, PA15, (1, 1),
   '⛔ 370 de vão não sai de chapa nenhuma: duas peles de 185, e a emenda '
   'fica no teto, onde ninguém olha · é a face inferior, a que se vê'),
 P('Engradado · travessa de MDF', I2, 273, 5, 17, PA15, (0, 0),
   '⛔ PINUS PROIBIDO [Jonathan, 28/10/2026]: os 45 m de engradado das '
   'três faces do pórtico eram sarrafo e agora são TRAVESSA DE MDF, '
   'tirada da própria chapa · ⛔ sem fita, é estrutura interna'),
 P('Painel superior · testeira', I2, 185, 3, 2, PA15, (1, 0),
   'A aresta de 3 cm do vão, que é a que aparece de baixo · ⛔ filetagem '
   'manual, régua não entra na coladeira'),
 P('Lateral · pele alta',   I2, 121, 161, 4, PA15, (1, 1),
   '⭐ duas peles por lateral e duas laterais = quatro peças · o corte é '
   'em 161 porque é exatamente onde começa o recorte da escada: a emenda '
   'cai na linha do degrau e some'),
 P('Lateral · pele baixa',  I2, 121, 139, 4, PA15, (1, 1),
   'A parte recortada — da linha do degrau ao piso · sai de retângulo de '
   '121 × 139 e perde o recorte da escada e o vão da porta'),
 P('Lateral · testeira',    I2, ALT_MAX, 3, 4, PA15, (1, 0),
   'As duas arestas verticais de 3 cm de cada lateral · ⛔ 300 de pé-'
   'direito, e régua de 3 não entra na coladeira: filetagem manual'),
 P('Requadro do vão de passagem', I2, 210, 3, 2, PA15, (1, 0),
   'As duas ombreiras do vão de 71 × 210 · ⛔ filetagem manual'),
 P('Verga do vão de passagem', I2, 71, 3, 1, PA15, (1, 0),
   'O topo do vão de passagem · ⛔ filetagem manual'),

 # ══ ITEM 03 · CAMA — 202 × 125 × 300 ════════════════════════════════
 #  DET. 03 VISTA FRONTAL  202 = 4 + 194 + 4 · altura 25 + 12 + 104 + 12
 #                         + 149 = 302 ≈ 300 · nicho de 178 × 22, LED
 #  DET. 03 VISTA LATERAL  125 = 121 + 4 · 25 de bicama, 116 de leito
 #                         baixo, 12 de base alta, 149 de rede de cordas
 #  DET. 03 VISTA SUPERIOR 202 × 125, a base alta inteira
 P('Montante · face',       I3, 300, 4, 8, PA15, (1, 0),
   '⭐ quatro faces por montante, dois montantes · seção de 4 × 4 e 300 '
   'de altura, com alma de aço dentro: é ele que segura a rede de cordas '
   'de 149 · ⛔ 300 não sai inteiro da chapa'),
 P('Cama alta · guarda-corpo frontal', I3, 202, 12, 1, PA18, (2, 2),
   'Os 12 da VISTA FRONTAL · é o que prende a criança lá em cima, e é a '
   'peça mais solicitada da cama: 18 mm'),
 P('Cama alta · guarda-corpo lateral', I3, 121, 12, 2, PA18, (2, 2),
   'Os dois lados da base alta'),
 P('Cama baixa · guarda-corpo frontal', I3, 202, 12, 1, PA18, (2, 2),
   'A faixa de 12 logo acima da bicama'),
 P('Cama baixa · guarda-corpo lateral', I3, 121, 12, 2, PA18, (2, 2), '—'),
 P('Painel de fundo com nicho', I3, 194, 116, 1, PA15, (2, 2),
   '⭐ é a parede do leito de baixo, e é nela que o nicho de 178 × 22 é '
   'rasgado e o LED corre · os 116 da VISTA LATERAL'),
 P('Nicho · topo e base',   I3, 178, 22, 2, PA15, (1, 0), 'Aparente'),
 P('Nicho · lateral',       I3, 22, 22, 2, PA15, (1, 0), 'Aparente'),
 P('Nicho · fundo',         I3, 178, 22, 1, PA6, (0, 0), 'Encaixe em rasgo'),
 P('Bicama · frente',       I3, 202, 25, 1, AA15, (2, 2),
   '⭐ a bicama corre no chão, em corrediça de carga, e abre pela cava — '
   'é a mesma solução da bicama de casal da Suíte Hóspedes'),
 P('Bicama · costas',       I3, 196, 25, 1, AA15, (1, 0), 'Aparente de lado'),
 P('Bicama · lateral',      I3, 118, 25, 2, AA15, (1, 0), 'Aparente'),

 # ══ ITEM 04 · ESTANTE — 93 × 50 × 300 ═══════════════════════════════
 #  DET. 04 VISTA FRONTAL  93 = 2 + 44 + 44 + 2 · altura 5 + 6 × 48 + 5
 #                         = 298 ≈ 300 · seis fileiras, três com porta
 #  DET. 04 VISTA LATERAL e SUPERIOR  50 de profundidade
 #  ⭐ a estante inteira é AZUL ASTRAL e só o FUNDO é Paris: é o que a
 #    legenda diz duas vezes, "nicho com iluminação em MDF Azul Astral,
 #    com fundo em MDF Paris".
 P('Lateral',               I4, 300, 50, 2, AA15, (1, 0),
   '⛔ 300 de pé-direito · a aresta da frente é a que aparece, e são 3 m '
   'de cada lado'),
 P('Topo e base',           I4, 90, 50, 2, AA15, (1, 0), 'Aparente'),
 P('Prateleira',            I4, 90, 50, 5, AA18, (1, 0),
   '⭐ 18 mm: o vão de 90 passa muito dos 70 da regra da casa · cinco '
   'horizontais entre as seis fileiras de 48'),
 P('Divisória vertical',    I4, 48, 50, 3, AA15, (1, 0),
   'Só as fileiras 2, 4 e 6 são partidas ao meio — as iluminadas são '
   'vãos cheios de 88, e é por isso que a divisória não é corrida'),
 P('Fundo',                 I4, 150, 93, 2, PA6, (0, 0),
   '⛔ 93 × 300 não sai de chapa nenhuma: duas faixas de 150, emenda '
   'atrás de prateleira · encaixe em rasgo'),
 P('Porta',                 I4, 44, 48, 3, AA15, (2, 2),
   'Três portas de giro iguais, nas fileiras 2, 4 e 6 · ⚠ a prancha não '
   'desenha puxador nenhum nelas'),

 # ══ ITEM 05 · ESTANTE DA CASINHA — 370 × 25 × 300 ═══════════════════
 #  DET. 05 VISTA FRONTAL  370 = 277 + 93 · 12 de testeira + 162 de caixa
 #                         + 126 de pé · quatro portas de 68 e duas
 #                         básculas de 87 × 37 · ripado de 3/1 no frontão
 #  DET. 05 VISTA SUPERIOR 370 × 25
 #  DET. 05 VISTA LATERAL  25 de profundidade · 89 da caixa das básculas
 #                         e 211 de vão livre embaixo dela
 P('Montante · face',       I5, 300, 9, 4, PA15, (1, 0),
   '⭐ os dois pés de 9 × 25 da VISTA FRONTAL, que sobem de piso a teto · '
   'frente e costas de cada caixão · ⛔ 300'),
 P('Montante · lado',       I5, 300, 22, 4, PA15, (0, 0),
   'Os dois lados de cada caixão de 9 × 25 — ⛔ sem fita: morrem contra '
   'a face e contra a parede · ⛔ 300'),
 P('Topo',                  I5, 185, 25, 2, PA15, (1, 0),
   '⛔ 370 não sai inteiro: duas peças de 185'),
 P('Testeira superior',     I5, 185, 12, 2, PA15, (2, 2),
   'A faixa de 12 que corre os 370 no alto, acima das portas'),
 P('Divisória entre portas', I5, 25, 150, 3, PA15, (1, 0),
   'As três verticais que partem os 277 em quatro portas de 68'),
 P('Módulo das básculas · lateral', I5, 25, 89, 1, PA15, (1, 0),
   'A ponta direita dos 370 · o módulo de 93 morre aqui'),
 P('Módulo das básculas · base', I5, 93, 25, 1, PA15, (1, 0), 'Aparente'),
 P('Módulo das básculas · divisória', I5, 90, 25, 1, PA15, (1, 0),
   'A horizontal entre as duas básculas de 37'),
 P('Fundo da caixa das portas', I5, 139, 162, 2, PA6, (0, 0),
   '⛔ 277 passa dos 275 da chapa por dois centímetros: duas faixas de '
   '139 · encaixe em rasgo'),
 P('Fundo do módulo das básculas', I5, 93, 89, 1, PA6, (0, 0),
   'Encaixe em rasgo'),
 P('Ripado do frontão · painel de base', I5, 260, 143, 1, AA15, (0, 0),
   '⭐ é o painel que aparece no vão de 1 entre as ripas, e por isso sai '
   'na cor da ripa, não em branco · ⛔ sem fita: as quatro arestas morrem '
   'atrás da moldura do telhado e dos dois pés'),
 *ripado(I5, RIPA_W, 95, RIPA_L, RIPA_V, AA15,
         '⭐ é o ÚNICO ripado COTADO do projeto: "ripas de 3cm e '
         'espaçamento de 1cm", escrito no DET 05 · altura média de 95, '
         'porque o frontão é um triângulo: 41 na beirada e 143 na cumeeira '
         '· laminada nos dois lados'),
 P('Frente · porta de giro externa', I5, 68, 155, 2, PA15, (2, 2),
   '⭐ as duas portas das pontas · o fundo delas acompanha a água do '
   'telhado, mas o corte sai de retângulo de 68 × 155'),
 P('Frente · porta de giro interna', I5, 68, 111, 2, PA15, (2, 2),
   'As duas portas que encostam na cumeeira, onde a água já subiu'),
 P('Frente da báscula',     I5, 87, 37, 2, PA15, (2, 2),
   'As duas do módulo direito de 93, uma sobre a outra'),
 P('Moldura · régua vertical externa', I5, 155, 5, 4, AA15, (2, 2),
   '⭐ MOLDURA DE OUTRA COR = QUATRO RÉGUAS, não peça inteira usinada: a '
   'frente é Palha Indiana e a moldura é Azul Astral · ⛔ filetagem '
   'manual, régua de 5 não entra na coladeira'),
 P('Moldura · régua vertical interna', I5, 111, 5, 4, AA15, (2, 2),
   'As verticais das duas portas de dentro · ⛔ filetagem manual'),
 P('Moldura · régua horizontal', I5, 68, 5, 4, AA15, (2, 2),
   'O topo de cada uma das quatro portas · ⛔ filetagem manual'),
 P('Moldura · régua inclinada', I5, 72, 5, 4, AA15, (2, 2),
   'A régua que acompanha a água do telhado, uma por porta · sai mais '
   'comprida que o vão porque é diagonal · ⛔ filetagem manual'),
 P('Moldura do módulo direito · régua horizontal', I5, 87, 5, 4, AA15,
   (2, 2), 'Topo e base de cada uma das duas frentes de 87 · ⛔ '
   'filetagem manual'),
 P('Moldura do módulo direito · régua vertical', I5, 37, 5, 4, AA15,
   (2, 2), 'Os dois lados de cada frente de 37 · ⛔ filetagem manual'),

 # ══ ITEM 06 · MESA — 260 × 50 × 80 ══════════════════════════════════
 #  DET. 06 VISTA FRONTAL  260 = 130 do armário + 129 da escrivaninha
 #                         armário 3 + 62 + 62 + 3 · altura 3 + 24 + 24
 #                         + 24 + 5 = 80 · três gavetas e uma porta
 #  DET. 06 VISTA LATERAL  40 × 64, o painel de encaixes
 #  DET. 06 CORTE          40 × 64 · 24 de rasgos corridos e os nichos
 #  DET. 06 PERSPECTIVA    130 e 129 de comprimento, 50 de profundidade
 P('Armário · lateral',     I6, 50, 80, 2, PA15, (1, 1), 'Aparente'),
 P('Armário · divisória central', I6, 50, 72, 1, PA15, (1, 0),
   'A vertical que parte os 130 na coluna das gavetas e na da porta'),
 P('Armário · tampo',       I6, 130, 50, 1, PA18, (2, 2),
   '⭐ 18 mm: é tampo de mesa de estudo, vão de 127 e apoio de cotovelo'),
 P('Armário · base',        I6, 127, 50, 1, PA15, (1, 0), 'Aparente de baixo'),
 P('Armário · rodapé',      I6, 127, 5, 1, PA15, (1, 0),
   'Os 5 do pé da VISTA FRONTAL'),
 P('Armário · fundo',       I6, 130, 80, 1, PA6, (0, 0), 'Encaixe em rasgo'),
 P('Frente da gaveta',      I6, 62, 24, 3, PA15, (2, 2),
   'As três gavetas de 24 da coluna esquerda'),
 P('Frente · porta de giro', I6, 62, 72, 1, PA15, (2, 2),
   'A porta da coluna direita, da altura das três gavetas somadas'),
 P('Moldura da gaveta · régua horizontal', I6, 62, 5, 6, AA15, (2, 2),
   'Topo e base de cada uma das três gavetas · ⛔ filetagem manual'),
 P('Moldura da gaveta · régua vertical', I6, 24, 5, 6, AA15, (2, 2),
   'Os dois lados de cada gaveta · ⛔ filetagem manual'),
 P('Moldura da porta · régua vertical', I6, 72, 5, 2, AA15, (2, 2),
   '⛔ filetagem manual'),
 P('Moldura da porta · régua horizontal', I6, 62, 5, 2, AA15, (2, 2),
   '⛔ filetagem manual'),
 *gaveta(I6, 62, 45, 20, 3, 'Caixa de gaveta', BR15, BR6),
 P('Escrivaninha · lateral', I6, 50, 80, 1, PA15, (1, 1),
   'A ponta direita dos 260, que é o que a VISTA LATERAL desenha'),
 P('Escrivaninha · painel de encaixes', I6, 129, 64, 1, PA15, (2, 2),
   '⭐⭐ é o coração do móvel: o painel é RASGADO de alto a baixo para a '
   'prateleira encaixar na altura que a criança quiser · o CORTE mostra '
   '24 cm de rasgos corridos e os nichos de 11 e 13 embaixo'),
 P('Escrivaninha · prateleira fixa', I6, 129, 40, 1, PA15, (1, 1),
   'A horizontal baixa dos nichos, a que o CORTE cota entre os 11 e os 13'),
 P('Prateleira móvel',      I6, 129, 40, 1, AA18, (2, 2),
   '⭐ é ela o tampo da escrivaninha, e é a única peça AZUL do DET 06 · '
   '18 mm porque vai nela o peso do estudo, e porque o vão é de 129'),
]

# ── ferragem, declarada item a item ─────────────────────────────────────
GAVETAS = [(I1, 'Cinco gavetas dos degraus da escada', 5, 350),
           (I6, 'Três gavetas do armário da mesa',     3, 450)]
PORTAS  = [(I4, 'Três portas de giro da estante de 300', 3, 2, DOBRADICA),
           (I5, 'Quatro portas de giro da casinha',      4, 2, DOBRADICA),
           (I6, 'Uma porta de giro do armário da mesa',  1, 2, DOBRADICA)]
# ⭐ as duas do módulo direito do DET 05 · abrem por PULSADOR, como as da
#   estante da Suíte Mariana: frente emoldurada, sem puxador desenhado
BASCULAS = [(I5, 'Duas básculas do módulo direito de 93', 2, 'pulsador')]
# ⭐ as duas únicas cavas DESENHADAS do ambiente: a meia-lua das frentes da
#   escada e a frente da bicama, que corre no chão
CAVA    = [(I1, 'Cinco frentes de gaveta da escada', 5, 68),
           (I3, 'Frente da bicama',                  1, 202)]
PUXADORES = []
MOLDURA = []          # ⛔ nenhuma provençal aqui: toda moldura é régua
LED     = [(I2, 'Faixa sob o painel superior do pórtico · os 270 cotados', 2.7),
           (I3, 'Sob a base alta, iluminando o leito de baixo e o nicho', 1.94),
           (I4, 'Uma fita em cada uma das três fileiras iluminadas', 2.64),
           (I5, 'As duas águas do telhado, por dentro da moldura',      3.3)]
CABIDEIROS = []
SARRAFOS= []   # ⛔ pinus PROIBIDO · engradado virou MDF, estrado virou metalon
SUPORTES= []
ALMAS   = [(I3, 'Montantes da cama · caixão de 40 × 40 mm e 300 de altura', 2),
           (I5, 'Pés da casinha · caixão de 90 × 250 mm e 300 de altura', 2)]
VIDRO   = []
SERRALHERIA = []
OUTRAS  = [# ⭐⭐ A PALHA É PALHINHA NATURAL [Jonathan, 28/10/2026]: R$ 650 o
           #   m², tapeceiro, não chapa. As frentes passam a ser substrato
           #   de MDF Paris com a palhinha trançada dentro da moldura.
           (I5, 'Palhinha natural', 'Campo das quatro portas de giro e das '
            'duas básculas da casinha · 2,11 + 1,51 + 0,64', 4.26, 'm²',
            'Palhinha natural'),
           (I6, 'Palhinha natural', 'Campo das três gavetas e da porta do '
            'armário da mesa · 0,45 + 0,45', 0.90, 'm²', 'Palhinha natural'),
           # ⭐ ESTRADO EM METALON · R$ 250 o quadro [Jonathan, 28/10/2026]
           (I3, 'Estrado em metalon', 'TRÊS quadros: cama alta 194 × 121, '
            'cama baixa 194 × 121 e bicama 196 × 118 · ⛔ substitui os três '
            'painéis de MDF e o sarrafo que os apoiava', 3, 'quadro',
            'Estrado em metalon'),
           # ⭐ PERFIL DE PROTEÇÃO DE PISO · R$ 15 o metro linear
           (I1, 'Perfil de proteção de piso', 'Escada de 157 de extensão',
            1.57, 'm', 'Perfil de proteção de piso'),
           (I2, 'Perfil de proteção de piso', 'As duas laterais do pórtico, '
            '121 cada', 2.42, 'm', 'Perfil de proteção de piso'),
           (I4, 'Perfil de proteção de piso', 'Estante de 93', 0.93, 'm',
            'Perfil de proteção de piso'),
           (I5, 'Perfil de proteção de piso', 'Os dois pés de 9 da casinha',
            0.18, 'm', 'Perfil de proteção de piso'),
           (I6, 'Perfil de proteção de piso', 'Armário da mesa, 130',
            1.30, 'm', 'Perfil de proteção de piso'),
           (I3, 'Corrediça de carga', 'Bicama de solteiro que corre no '
            'chão · ⛔ a Base não tem a linha', 1, 'un', 'Corrediça de carga'),
           (I4, 'Pulsador', 'Três portas lisas de 44 × 48 · a prancha não '
            'desenha puxador nenhum', 3, 'un', 'Pulsador'),
           (I5, 'Pulsador', 'Quatro portas de giro e duas básculas, todas '
            'emolduradas e sem puxador desenhado', 6, 'un', 'Pulsador'),
           (I6, 'Pulsador', 'Três gavetas e uma porta, todas emolduradas e '
            'sem puxador desenhado', 4, 'un', 'Pulsador'),
           (I6, 'Usinagem de encaixe de prateleira', 'Painel de encaixes da '
            'escrivaninha · 129 de largura por 64 de altura de rasgo '
            'corrido · ⛔ SEM PREÇO na Base', 1.29, 'm', 
            'Usinagem de encaixe de prateleira')]

CABECA = {
 I1: ('157 × 72 × 139',
      'DET. 01 VISTA FRONTAL 72 = 4 de vão para o pórtico + 68 de corpo · '
      'altura 5 × (2 + 26) ≈ 139, cinco gavetas · VISTA LATERAL 157 = '
      'cinco degraus de 31, cinco espelhos de 28 · VISTA SUPERIOR 157 × 72 '
      '· ⭐ os 4 cm não são peça, são folga para a lateral do pórtico'),
 I2: ('370 × 121 × 300',
      'DET. 02 VISTA FRONTAL 370 de vão, 270 de LED, pé-direito 300 · '
      'VISTA SUPERIOR 369 × 121 · VISTA LATERAL 121 × 300, 161 cheio mais '
      'o recorte da escada de três degraus de 28 × 33 · PERSPECTIVA vão da '
      'porta de 71 × 210, verga de 90, pé de 50 · ⭐ 15 mm sobre engradado '
      'de sarrafo, não chapa maciça de 3 cm'),
 I3: ('202 × 125 × 300',
      'DET. 03 VISTA FRONTAL 202 = 4 + 194 + 4 · altura 25 de bicama + 12 '
      '+ 104 + 12 + 149 de rede ≈ 300 · nicho de 178 × 22 com LED · VISTA '
      'LATERAL 125 = 121 + 4, 116 de leito baixo · VISTA SUPERIOR 202 × '
      '125 · ⚠ a rede de cordas não é marcenaria; a furação é'),
 I4: ('93 × 50 × 300',
      'DET. 04 VISTA FRONTAL 93 = 2 + 44 + 44 + 2 · altura 5 + seis '
      'fileiras de 48 + 5 = 298 ≈ 300 · três fileiras cheias e '
      'iluminadas, três partidas ao meio com porta · VISTA LATERAL e '
      'SUPERIOR 50 de profundidade · ⭐ tudo Azul Astral, só o fundo Paris'),
 I5: ('370 × 25 × 300',
      'DET. 05 VISTA FRONTAL 370 = 277 + 93 · 12 de testeira, 162 de '
      'caixa, 126 de pé · quatro portas de 68 com água de telhado e duas '
      'básculas de 87 × 37 · frontão ripado de 3 com vão de 1, COTADO na '
      'prancha · VISTA SUPERIOR 370 × 25 · VISTA LATERAL 89 da caixa das '
      'básculas e 211 de vão livre embaixo'),
 I6: ('260 × 50 × 80',
      'DET. 06 VISTA FRONTAL 260 = 130 de armário + 129 de escrivaninha · '
      'armário 3 + 62 + 62 + 3, altura 3 + 24 + 24 + 24 + 5 = 80, três '
      'gavetas e uma porta · VISTA LATERAL 40 × 64 · CORTE 24 cm de '
      'rasgos corridos e os nichos de 11 e 13 · ⭐ o tampo da '
      'escrivaninha é a PRATELEIRA MÓVEL, que encaixa onde a criança quiser'),
}

FOLHA = dict(
 aba='SUÍTE 03',
 sub='Jéssica e Michell · Projeto ICA · páginas 208 a 221 · seis itens em '
     'seis folhas de detalhe · ⭐ três cores: Paris Guararapes na '
     'estrutura, Azul Astral Duratex na cor e em toda moldura, Palha '
     'Indiana Sextavada Duratex só em frente · ⭐ nenhuma peça órfã: as '
     'quatro elevações só mostram o que tem DET · peça inteira até '
     f'{ALT_MAX:g}, que é a chapa de {CHAPA_C:g} menos o acerto de corte',
 chapa_txt={PA15: 'Paris · Guararapes · estrutura: pórtico, camas, armário '
                  'da mesa e o painel de encaixes da escrivaninha',
            PA18: 'Paris 18 mm · degraus da escada, guarda-corpos das duas '
                  'camas e o tampo do armário — tudo que recebe peso',
            PA6:  'Paris 6 mm · fundos de encaixe em rasgo, sem fita',
            AA15: 'Azul Astral · Duratex · a cor do quarto: gavetas da '
                  'escada, estante do DET 04, ripado do frontão, bicama e '
                  'TODAS as quarenta réguas de moldura',
            AA18: 'Azul Astral 18 mm · prateleiras da estante de 300 e a '
                  'prateleira móvel da escrivaninha',
            PI15: 'Palha Indiana Sextavada · Duratex · só frente: as quatro '
                  'portas e as duas básculas do DET 05, as três gavetas e '
                  'a porta do DET 06',
            BR15: 'Caixaria de gaveta · o padrão da Base, não aparece',
            BR6:  'Fundos de caixa de gaveta · encaixe em rasgo'},
 nota='⛔ O FRETE ESTÁ ZERADO DE PROPÓSITO: as linhas de frete da Base não '
      'têm preço ainda. Preencher lá e elas aparecem aqui sozinhas.   '
      '⭐⭐ TODA MOLDURA DESTE AMBIENTE É RÉGUA, NÃO PEÇA INTEIRA. São dez '
      'frentes emolduradas e quarenta réguas de 5 cm, e a regra da casa é '
      'clara nos dois sentidos: moldura da MESMA cor da frente sai em peça '
      'inteira de 6 mm usinada na router; moldura de OUTRA cor sai em '
      'quatro réguas. Aqui a frente é Palha Indiana e a moldura é Azul '
      'Astral. ⛔ Régua não entra na coladeira: a filetagem das quarenta é '
      'MANUAL, R$ 5,00 o metro.   '
      '⛔⛔ O PÉ-DIREITO DE 300 MORDE QUATRO VEZES: as duas laterais do '
      'pórtico, as duas da estante do DET 04, os dois montantes da cama e '
      'os dois pés da casinha. Só as do pórtico eu emendei de propósito, '
      'porque são painel largo e a emenda some na linha do degrau. As '
      'outras estão na lista de peças ALTAS.   '
      '⭐ O PÓRTICO É 15 mm SOBRE ENGRADADO DE SARRAFO, que é o que a casa '
      'fechou na Suíte Mariana — não são duas chapas coladas. A diferença '
      'aqui é que ele tem dois lados à vista, porque se atravessa o vão de '
      'passagem: as duas laterais levam pele dos dois lados, e só o painel '
      'superior, que morre no teto, leva uma pele só.   '
      '⚠ A REDE DE CORDAS DA CAMA, O PAPEL DE PAREDE, A PERSIANA, O TAPETE '
      'E A TV DE 32" NÃO ESTÃO NESTA CONTA: não são marcenaria.',
 duvidas=[
  '⛔⛔ O PAINEL DE ENCAIXES DA ESCRIVANINHA NÃO TEM PREÇO. São 129 de '
  'largura por 64 de altura de rasgo corrido na router, para a prateleira '
  'móvel encaixar na altura que a criança quiser — o CORTE do DET 06 '
  'desenha 24 cm de rasgos e os nichos de 11 e 13 embaixo. ⚠ Não é furo '
  'de suporte oculto (R$ 30 cada) e não é ripa: é usinagem corrida, e a '
  'Base não tem a linha. É irmã da furação do pegboard do Home Office, '
  'que também está em aberto. Lancei a zero para aparecer na conta sem '
  'mentir. ⛔ Enquanto não tiver preço, este item é um PISO.',
  '⛔ A LARGURA DA RIPA DO FRONTÃO É A ÚNICA DO PROJETO QUE VEM ESCRITA: '
  '"ripas de 3cm e espaçamento de 1cm", no DET 05. ⭐ Não há o que '
  'perguntar aqui — são 66 ripas em 260. ⚠ O que FICA em aberto é a '
  'ALTURA: o frontão é um triângulo, 41 na beirada e 143 na cumeeira, e '
  'cada ripa tem uma altura diferente. Adotei 95 de média, que é a conta '
  'honesta da área. Se a fábrica quiser cortar todas em 143 e aparar, '
  'sobe meia chapa de Azul Astral.',
  'OS MONTANTES DE 4 × 4 × 300 DA CAMA SÃO O PONTO FRÁGIL DO AMBIENTE. '
  'Eles sobem do piso ao teto, seguram a base alta a 141 e ainda a rede '
  'de cordas de 149 acima dela. ⚠ Em MDF, 4 × 4 é caixão de quatro faces '
  'sobre alma de aço — foi como lancei, R$ 50 por alma. ⛔ Mas 300 não '
  'sai inteiro da chapa: ou o montante leva emenda à vista no meio, ou '
  'ele sai em madeira maciça, que é o que eu faria. Decisão do senhor, e '
  'é decisão de SEGURANÇA, não de preço.',
  'A REDE DE CORDAS DE PROTEÇÃO NÃO É MARCENARIA, mas a FURAÇÃO DOS '
  'MONTANTES É. São 149 de altura de rede entre os dois montantes, e a '
  'prancha desenha a malha mas não diz a corda, o passo do furo nem o nó. '
  '⚠ Não lancei nada: sem o passo, furar é inventar. ⛔ É item de '
  'segurança de cama infantil alta — vale confirmar com a arquiteta antes '
  'de a cama ir para a fábrica.',
  'AS TRÊS PORTAS DO DET 04 NÃO TÊM PUXADOR DESENHADO. ⭐ Orcei PULSADOR, '
  'R$ 100 cada, R$ 300 pelas três. ⚠ Diferente do DET 05 e do DET 06, '
  'aqui a frente é LISA, em Azul Astral — cava usinada caberia '
  'perfeitamente e sairia R$ 66 pelas três frentes de 44. É R$ 234 de '
  'diferença, e é só decisão de desenho.',
  'AS DEZ FRENTES EMOLDURADAS DO DET 05 E DO DET 06 TAMBÉM NÃO TÊM '
  'PUXADOR. ⭐ Orcei PULSADOR nas dez, R$ 1.000 — mesma leitura da estante '
  'da Suíte Mariana e das portas ripadas do Banho Gourmet: a moldura de 5 '
  'cm não deixa cava, e puxador aparafusado o desenho mostraria. ⚠ A '
  'alternativa é Alças Traso 128 a R$ 110, que daria R$ 1.100 — quase o '
  'mesmo. Então aqui o pulsador não é economia, é leitura de desenho.',
  'O PÓRTICO TEM 370 DE VÃO E 121 DE PROFUNDIDADE, e eu o construí como a '
  'casa construiu os painéis de 3 cm da Suíte Mariana: 15 mm sobre '
  'engradado de sarrafo. ⚠ A diferença é que aqui são DOIS lados à vista '
  'nas laterais, porque se atravessa o vão de passagem de 71 × 210 — '
  'são quatro peles por lateral em vez de duas. ⛔ Se o senhor ler o '
  'desenho como chapa maciça de 3 cm, são mais quatro chapas de Paris, '
  'uns R$ 2.200 a mais. E se a lateral esquerda encostar na parede, cai '
  'uma pele e economiza R$ 550.',
  'O RECORTE DA ESCADA NA LATERAL DO PÓRTICO É DE 33 EM 33, mas os '
  'degraus da escada do DET 01 são de 31. ⚠ Dois centímetros de folga por '
  'degrau, três degraus. Pode ser folga de montagem de propósito, pode '
  'ser cota que não bate. ⛔ Quem monta no local resolve, mas vale avisar: '
  'a escada e o pórtico se tocam, e os dois são peça cortada em fábrica.',
  'A ESCADA TEM 157 DE EXTENSÃO E 139 DE ALTURA, e a base alta da cama '
  'está a 141. ⚠ Fecha com 2 cm de degrau para o último passo, o que é '
  'correto. ⛔ Mas as duas laterais escalonadas saem de retângulo de 157 '
  '× 139 e o recorte vira sobra: são 2,2 m² de Azul Astral que viram '
  'retalho por lateral. Se a fábrica conseguir encaixar o perfil de uma '
  'na sobra da outra, cai uma chapa.',
  'OS DOIS PÉS DA CASINHA DO DET 05 TÊM 9 × 25 DE SEÇÃO E 300 DE ALTURA. '
  '⚠ Lancei como caixão de quatro peças sobre alma de aço, igual às '
  'colunas do Living. ⛔ Mesmo problema dos montantes da cama: 300 não '
  'sai inteiro. Aqui a emenda incomoda menos, porque o pé fica atrás do '
  'ripado em boa parte da altura — mas é bom o senhor saber que ela '
  'existe.',
  'AS QUATRO PORTAS DO DET 05 ACOMPANHAM A ÁGUA DO TELHADO e por isso '
  'não são retângulos: o fundo de cada uma é inclinado. ⚠ Cortei pelo '
  'retângulo que as contém — 68 × 155 nas duas de fora, 68 × 111 nas duas '
  'de dentro —, que é o que elas ocupam na chapa. ⛔ A moldura inclinada '
  'de cada porta eu lancei com 72 em vez de 68, porque régua diagonal sai '
  'mais comprida que o vão. É pouco, mas é o tipo de coisa que falta '
  'quando chega na bancada.',
  '⛔ A BASE METÁLICA DE 3 CM: aqui ela caberia na estante do DET 04, no '
  'armário da mesa e nos pés do DET 05 e do pórtico — tudo que toca o '
  'chão. São uns 8 m de rodapé. ⚠ Fica para a passada única, junto com '
  'os outros ambientes.'],
 nao_marcenaria=[
  'Rede de cordas de proteção da cama alta, 194 × 149 — e a corda, o passo '
  'do furo e o nó, que a prancha não especifica',
  'Papel de Parede Listrado Jelly - Stickdecor, nas elevações 01 e 04',
  'Persiana romana branca da ELEVAÇÃO 02',
  'Tapete Infantil Orgânico Ah Mar Aquamarine',
  'TV de 32" da ELEVAÇÃO 03, sobre o frontão ripado',
  'Os três colchões de solteiro: o da cama alta, o da baixa e o da bicama'],
 notas=[
  '⭐⭐ TODA MOLDURA DAQUI É RÉGUA, e é a regra da casa funcionando nos '
  'dois sentidos. Moldura da MESMA cor da frente sai em peça inteira de '
  '6 mm usinada na router — foi o que o senhor fechou em 28/10. Moldura '
  'de OUTRA cor sai em quatro réguas, porque régua continua sendo régua. '
  'Aqui a frente é Palha Indiana Sextavada e a moldura é Azul Astral: são '
  'dez frentes, quarenta réguas de 5 cm, e a filetagem delas é MANUAL.',
  '⭐ O RIPADO DO FRONTÃO É O ÚNICO COTADO DO PROJETO INTEIRO. Em todos os '
  'outros ambientes — Banho Gourmet, Banho Master, Área Gourmet — a '
  'largura da ripa foi medida por mim no desenho em 1/20 e virou dúvida. '
  'Aqui o DET 05 escreve: "ripas de 3cm e espaçamento de 1cm". São 66 '
  'ripas em 260, e a perda de serra entra como linha própria, pelo fator '
  '1,10 da Base.',
  '⛔⛔ O PÉ-DIREITO DE 300 MORDE QUATRO VEZES, e só uma delas eu resolvi '
  'por conta própria: as duas laterais do pórtico saem em duas peles cada, '
  'com a emenda na linha de 161 — que é exatamente onde começa o recorte '
  'da escada, então ela some atrás do degrau. As duas laterais da estante '
  'do DET 04, os dois montantes da cama e os dois pés da casinha estão na '
  'lista de peças ALTAS, porque em peça estreita a emenda aparece e a '
  'decisão é de projeto.',
  '⭐ A ESCADA É UM GAVETEIRO DISFARÇADO. Cinco degraus, cinco gavetas de '
  '68 × 26, e é o único móvel do ambiente em que a prancha DESENHA o '
  'puxador: a meia-lua da cava, em cada frente. Em todo o resto do quarto '
  'não há puxador nenhum desenhado, e é por isso que há dez pulsadores '
  'nesta conta.',
  '⚠ OS TRÊS COLCHÕES NÃO SÃO NOSSOS, mas os três estrados são, e os três '
  'são peça grande: 194 × 121 duas vezes e 196 × 118 uma. Saem em Paris '
  'os dois de cima, que ficam à vista por baixo, e em Branco TX o da '
  'bicama, que corre no chão e ninguém vê. São 6,9 m² que não aparecem '
  'no desenho e que a fábrica tem de cortar.'],
)
