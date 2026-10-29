# -*- coding: utf-8 -*-
"""ICA · SUÍTE MARIANA — levantamento peça por peça  [28/10/2026]

páginas 177 a 191 · onze detalhamentos em sete folhas, e o ambiente com
MAIS ITENS do projeto inteiro.

⭐⭐ É UM QUARTO DE CRIANÇA, e isso muda o levantamento de ponta a ponta:
  casinha, cama montessoriana com bicama, escrivaninha com encaixes,
  caixa organizadora com rodinha, prateleira baixa, o nome "Mariana"
  recortado na parede. Nada aqui é um armário.

⭐⭐ TRÊS FORNECEDORES NUMA PEÇA SÓ. A frente é Palha Indiana Sextavada
  Natural (DURATEX), a moldura de 5 cm é Sal Rosa (ARAUCO) e a estrutura é
  Paris (GUARARAPES). ⛔ Três pedidos, três fretes e três arredondamentos
  num quarto de 15 m². É a primeira vez no projeto que isso acontece.

⭐ A MOLDURA DE 5 CM É DE OUTRA COR, então aqui régua continua sendo régua:
  peça inteira de Sal Rosa por cima da Palha Indiana cobriria a palha. É a
  mesma leitura do aparador da Suíte Hóspedes e da bancada do Banho
  Hóspedes — os três únicos lugares do projeto onde não vale a peça inteira
  usinada na router.

⛔⛔ OS PAINÉIS TÊM 3 CM DE ESPESSURA, e 3 cm em MDF não é chapa: é
  construção. Lancei painel de 15 mm sobre ENGRADADO DE SARRAFO, que dá os
  3 cm e custa metade de duas chapas coladas. ⚠ A alternativa — duas
  chapas de 15 coladas — dobraria a chapa de Paris do ambiente. A dúvida
  04 põe os dois números lado a lado.

⛔ 350 NÃO SAI DE UMA CHAPA. A estante do DET 01 e a casinha do DET 06 têm
  as duas 350 de largura, e as duas saem em peças de 175 — que é
  exatamente o que a VISTA SUPERIOR de cada uma desenha.

⚠ O NOME "MARIANA" da ELEVAÇÃO 04 é marcenaria e não tem DET: "Nome em
  MDF sal rosa - Arauco com espessura de 3cm". Lancei como item próprio,
  com as duas chapas coladas e a usinagem em router a zero — a Base não
  tem a linha.
"""
from base import (P, gaveta, ripado, ALT_MAX, CHAPA_C, DOBRADICA, BASCULA)

PA15, PA6 = 'MDF Paris 15', 'MDF Paris 6'
BR6 = 'MDF Branco TX 6'
SR15, SR6 = 'MDF Sal Rosa 15', 'MDF Sal Rosa 6'
PI18 = 'MDF Palha Indiana Sextavada 18'
BR15 = 'MDF Branco TX 15'

I1  = 'DET 01 Estante com armário'
I2  = 'DET 02 Caixa organizadora'
I3  = 'DET 03 Mesa com armário'
# ⭐⭐ DUAS UNIFICAÇÕES [Jonathan, 28/10/2026]: "Unifique item 4 e 5" e
#   "unfique item 7, 8, 9 e 10". Os DETs continuam escritos peça por peça
#   dentro do item — o que muda é quantas linhas o cliente confere.
I4  = 'DET 04 e 05 Painel com suporte de papel e painel de 135'
I5  = I4
I6  = 'DET 06 Casinha'
I7  = 'DET 07 a 10 Mesa lateral, painel de 330, prateleira e escrivaninha'
I8  = I7
I9  = I7
I10 = I7
I11 = 'DET 11 Cama montessoriana'
I12 = 'ELEVAÇÃO 04 Nome Mariana'

SUITEMARIANA = [
 # ══ ITEM 01 · ESTANTE COM ARMÁRIO — 350 × 300 × 30 ═══════════════════
 #  VISTA FRONTAL  3 + 61 + 61 + 61 + 61 + 3 + 100 = 350
 #                 altura 174 do corpo + 126 das pernas = 300
 #                 armário de 100: básculas de 85 e de 37
 #  VISTA SUPERIOR 350 × 30 · VISTA LATERAL 88 + 67 + 145 = 300
 #  ⭐ as quatro portas são recortadas na linha da empena, e é por isso
 #    que a estante parece um telhado: o ripado é o que aparece por baixo
 P('Lateral',               I1, 174, 30, 2, PA15, (1, 1)),
 P('Divisória',             I1, 174, 30, 1, PA15, (1, 0),
   'A vertical que separa as quatro portas do armário de 100'),
 P('Tampo',                 I1, 175, 30, 2, PA15, (1, 1),
   '⛔ 350 não sai de uma chapa: duas peças de 175, que é o que a VISTA '
   'SUPERIOR desenha'),
 P('Base do armário de 100', I1, 100, 30, 1, PA15, (1, 0)),
 P('Prateleira do armário de 100', I1, 100, 30, 1, PA15, (1, 0),
   'Entre a báscula de 85 e a de 37'),
 P('Fundo',                 I1, 175, 174, 2, PA6, (0, 0),
   'Encaixe em rasgo · duas peças, pela mesma razão do tampo'),
 P('Perna',                 I1, 126, 30, 2, PA15, (1, 1),
   'Os dois montantes de 8 que descem até o piso, com 235 entre eles'),
 P('Painel sob o ripado',   I1, 117.5, 212, 2, SR15, (2, 2),
   '⭐ é ele que aparece no vão de 1 entre as ripas · ⛔ 235 × 212 não '
   'cabe em orientação nenhuma: duas peças de 117,5'),
 *ripado(I1, 235, 212, 3, 1, SR15,
         'Ripado da empena · ripa de 3 com vão de 1, como a prancha '
         'escreve · laminada nos dois lados'),
 P('Frente · porta de giro · campo', I1, 61, 174, 4, SR15, (0, 0),
   '⭐⭐ O CAMPO VIRA SUBSTRATO [Jonathan, 28/10/2026]: a palha indiana é '
   'PALHINHA NATURAL a R$ 650 o m², não chapa melamínica a R$ 137 · a peça '
   'continua existindo porque a palhinha precisa de fundo em que se fixar, '
   'mas sai no MDF estrutural · ⛔ sem fita: as arestas morrem sob a moldura'),
 P('Frente · báscula de 85 · campo', I1, 100, 85, 1, SR15, (0, 0),
   'Substrato da palhinha · ⛔ sem fita'),
 P('Frente · báscula de 37 · campo', I1, 100, 37, 1, SR15, (0, 0),
   'Substrato da palhinha · ⛔ sem fita'),
 P('Frente · porta · moldura · régua longa', I1, 174, 5, 8, SR15, (2, 2),
   '⛔ MOLDURA DE OUTRA COR: Sal Rosa sobre Palha Indiana · peça inteira '
   'cobriria a palha, então aqui régua é régua'),
 P('Frente · porta · moldura · régua curta', I1, 51, 5, 8, SR15, (2, 2),
   'As duas laterais de cada porta · 61 menos as duas réguas de 5'),
 P('Frente do armário de 100 · moldura · régua longa', I1, 100, 5, 4,
   SR15, (2, 2), '⛔ moldura de OUTRA COR: Sal Rosa sobre Palha Indiana'),
 P('Frente de 85 · moldura · régua curta', I1, 75, 5, 2, SR15, (2, 2)),
 P('Frente de 37 · moldura · régua curta', I1, 27, 5, 2, SR15, (2, 2)),

 # ══ ITEM 02 · CAIXA ORGANIZADORA — 50 × 35 × 46 · DUAS ═══════════════
 #  DET. 02 VISTA SUPERIOR 50 × 35 · FRONTAL 35 × 46 · LATERAL 50 × 46
 #  ⭐ a ELEVAÇÃO 01 desenha DUAS, lado a lado sob a mesa do DET 03
 P('Lateral de 50',         I2, 50, 46, 4, SR15, (2, 2),
   'Duas por caixa, duas caixas · aparente dos dois lados: a caixa corre '
   'para fora no rodízio'),
 P('Costado de 32',          I2, 32, 46, 4, SR15, (2, 2),
   '35 menos as duas chapas de 15 mm · ⭐ não é frente de móvel: '
   'a caixa é um caixote aberto, sem porta e sem puxador'),
 P('Fundo',                 I2, 47, 32, 2, SR15, (0, 0),
   'Fundo de 15 mm: a caixa corre no chão e carrega brinquedo · '
   '⛔ sem fita de propósito: fica entre os quatro costados'),

 # ══ ITEM 03 · MESA COM ARMÁRIO — 235 × 66 × 50 ═══════════════════════
 #  DET. 03 VISTA FRONTAL  123 da mesa + 112 do armário = 235
 #                         altura 66 · três gavetas de 20 e uma porta
 #  VISTA SUPERIOR e LATERAL  50 de profundidade
 P('Tampo',                 I3, 235, 50, 1, PA15, (1, 1),
   'Peça inteira: 235 cabe nos 275 da chapa'),
 P('Lateral',               I3, 64, 50, 2, PA15, (1, 1),
   'A perna da mesa à esquerda e a lateral do armário à direita'),
 P('Divisória',             I3, 64, 50, 1, PA15, (1, 0),
   'Separa a coluna das três gavetas da coluna da porta'),
 P('Base do armário',       I3, 109, 50, 1, PA15, (1, 0)),
 P('Fundo',                 I3, 112, 66, 1, PA6, (0, 0), 'Encaixe em rasgo'),
 P('Frente · gaveta · campo', I3, 53, 20, 3, SR15, (0, 0),
   'Substrato da palhinha das três gavetas · ⛔ sem fita'),
 P('Frente · porta · campo', I3, 53, 60, 1, SR15, (0, 0),
   'Substrato da palhinha da porta · ⛔ sem fita'),
 P('Frente · gaveta · moldura · régua longa', I3, 53, 5, 6, SR15, (2, 2),
   '⛔ moldura de OUTRA COR: régua é régua'),
 P('Frente · gaveta · moldura · régua curta', I3, 10, 5, 6, SR15, (2, 2)),
 P('Frente · porta · moldura · régua longa', I3, 60, 5, 2, SR15, (2, 2)),
 P('Frente · porta · moldura · régua curta', I3, 43, 5, 2, SR15, (2, 2)),
 *gaveta(I3, 53, 45, 20, 3, 'Gaveta'),

 # ══ ITEM 04 · PAINEL COM SUPORTE DE PAPEL — 105 × 145 × 19 ═══════════
 #  DET. 04 VISTA FRONTAL 105 × 145 · SUPERIOR 18 + 68 + 20, 19 de aba
 #  ⭐ são duas travessas de 19 atravessando o painel: a de cima segura o
 #    rolo, a de baixo é o apoio onde a criança desenha
 P('Painel',                I4, 105, 145, 1, PA15, (2, 2)),
 P('Travessa de 19',        I4, 105, 19, 2, PA15, (2, 2),
   'A de cima com o suporte do rolo, a de baixo de apoio'),

 # ══ ITEM 05 · PAINEL 1 — 105 × 135 × 3 ══════════════════════════════
 #  ⭐ 3 cm não é chapa, é construção: painel de 15 sobre engradado de
 #    sarrafo. Duas chapas coladas dariam o mesmo 3 cm pelo dobro.
 P('Painel',                I5, 105, 135, 1, PA15, (2, 2)),

 # ══ ITEM 06 · CASINHA — 350 × 219 × 25 ═══════════════════════════════
 #  DET. 06 VISTA FRONTAL 10 + 40 + 290 + 10 = 350 · altura 219 na cumeeira
 #                        e 126 na beirada · empenas de 190 e de 198
 #  VISTA SUPERIOR 175 + 175 = 350, 25 de profundidade
 #  ⭐ quatro NICHOS de 40 em Sal Rosa, encaixados na espessura de 25
 P('Fachada',              I6, 175, 219, 2, PA15, (2, 2),
   '⛔ 350 não sai de uma chapa: duas peças de 175, que é o que a VISTA '
   'SUPERIOR desenha · o recorte da casa é usinagem, não peça a mais'),
 P('Telhado · água de 190',  I6, 190, 25, 1, PA15, (1, 1)),
 P('Telhado · água de 198',  I6, 198, 25, 1, PA15, (1, 1)),
 P('Lateral de 145',        I6, 145, 25, 1, PA15, (1, 1)),
 P('Lateral de 126',        I6, 126, 25, 1, PA15, (1, 1)),
 P('Nicho · lateral',       I6, 145, 25, 2, SR15, (1, 0),
   'A coluna de quatro nichos de 40, em Sal Rosa'),
 P('Nicho · prateleira',    I6, 40, 25, 5, SR15, (1, 0),
   'Cinco divisórias para os quatro nichos'),
 P('Nicho · fundo',         I6, 40, 145, 1, SR6, (0, 0),
   '⭐ o fundo do nicho aparece: sai em Sal Rosa, não em branco'),
 P('Janelinha · moldura',   I6, 25, 25, 1, PA15, (2, 2),
   'Janelinha fake · a moldura em Paris'),
 P('Janelinha · vidro fake', I6, 22, 22, 1, BR15, (2, 2),
   '⭐ "MDF branco para representar vidro", como a prancha escreve'),

 # ══ ITEM 07 · MESA LATERAL — 83 × 60 × 50 ════════════════════════════
 #  DET. 07 VISTA FRONTAL 83 de largura · altura 2 + 27 + 2 + 27 + 2 = 60
 #  VISTA SUPERIOR 83 × 50 · LATERAL 50 × 60
 #  ⭐ o NICHO interno é Sal Rosa, a caixa é Paris
 # ⭐⭐ MATERIAL DUPLO [Jonathan, 28/10/2026]: "observe que são materiais
 #   duplos, ou seja, o dobro de material". A caixa é Paris por fora e o
 #   nicho é Sal Rosa por dentro, e em melamínico UMA chapa não tem duas
 #   cores: cada face da caixa é DUAS peças coladas, a de fora em Paris e a
 #   de dentro em Sal Rosa. Era o furo deste item — eu contava uma só.
 P('Lateral · pele externa', I7, 60, 50, 2, PA15, (1, 1),
   'Paris, a cor que se vê de fora'),
 P('Lateral · pele interna', I7, 60, 50, 2, SR15, (1, 1),
   '⭐ Sal Rosa, a cor que se vê DENTRO do nicho · é a segunda pele do '
   'material duplo'),
 P('Tampo e base · pele externa', I7, 80, 50, 2, PA15, (1, 1), 'Paris'),
 P('Tampo e base · pele interna', I7, 80, 50, 2, SR15, (1, 1),
   '⭐ Sal Rosa por dentro · segunda pele'),
 P('Prateleira',            I7, 80, 50, 1, SR15, (1, 0),
   'A divisória dos dois nichos de 27 · em Sal Rosa, como a prancha pede'),
 P('Fundo',                 I7, 83, 60, 1, SR6, (0, 0),
   '⭐ o fundo aparece nos dois nichos: Sal Rosa, não branco'),

 # ══ ITEM 08 · PAINEL 2 — 330 × 145 × 3 ══════════════════════════════
 P('Painel',                I8, 165, 145, 2, PA15, (2, 2),
   '⛔ 330 não sai de uma chapa: duas peças de 165 · ⭐ os 3 cm saem do '
   'engradado de MDF atrás, não de duas chapas coladas'),

 # ══ ITEM 09 · PRATELEIRA — 114 × 15 × 8 ═════════════════════════════
 #  DET. 09 VISTA SUPERIOR 3 + 109 + 3 = 114, 15 de profundidade
 #          VISTA FRONTAL 114 × 8 · LATERAL 15 × 8
 P('Fundo',                 I9, 114, 15, 1, SR15, (1, 0)),
 P('Borda de contenção',    I9, 114, 8, 1, SR15, (2, 2),
   'Os 8 de altura que a VISTA FRONTAL desenha · ⭐ é borda, não frente: a prateleira não abre'),
 P('Lateral',               I9, 15, 8, 2, SR15, (2, 2)),

 # ══ ITEM 10 · ESCRIVANINHA MONTESSORIANA — 91 × 64 × 40 ══════════════
 #  DET. 10 VISTA SUPERIOR 2 + 81 + 2 + 7 = 91, 40 de profundidade
 #          VISTA FRONTAL 2 + 83 + 7 · altura 24 + 40 = 64
 #  ⭐ o CORTE mostra a escada de encaixes: a prateleira sobe e desce com
 #    a criança, que é o que faz dela montessoriana
 P('Tampo',                 I10, 91, 40, 1, PA15, (2, 2)),
 P('Lateral',               I10, 64, 40, 2, PA15, (2, 2),
   '⭐ é nela que a escada de encaixes é usinada'),
 P('Fundo com encaixes',    I10, 88, 64, 1, PA15, (1, 1),
   '15 mm, não 6: é ele que recebe os encaixes dos nichos'),
 P('Prateleira móvel',      I10, 83, 40, 1, SR15, (2, 2),
   '⭐ Sal Rosa, e ela é MÓVEL: encaixa em qualquer altura da escada'),
 # ⭐ RIPAS LATERAIS [Jonathan, 28/10/2026]: "item 10: tem as ripas
 #   laterais". As duas faces externas da escrivaninha são ripadas, como a
 #   empena do DET 01 — ripa de 3 com vão de 1, laminada nos dois lados.
 #   ⚠ A medida do vão saiu por leitura: a prancha não cota a ripa aqui.
 *ripado(I10, 40, 64, 3, 1, SR15,
         'Ripado da lateral esquerda · ripa de 3 com vão de 1, como na '
         'empena do DET 01 · laminada nos dois lados'),
 *ripado(I10, 40, 64, 3, 1, SR15,
         'Ripado da lateral direita · ripa de 3 com vão de 1 · laminada '
         'nos dois lados'),

 # ══ ITEM 11 · CAMA MONTESSORIANA — 207 × 107 × 57 ════════════════════
 #  DET. 11 VISTA SUPERIOR 207 × 107 · FRONTAL 207, 27 de proteção + 30
 #          de corpo · LATERAL 107, mesma divisão
 #  ⭐ o corpo de 30 guarda a BICAMA, e a proteção de 27 é Palha Indiana
 #    emoldurada em Sal Rosa, como as frentes do DET 01 e do DET 03
 P('Corpo · lateral',       I11, 207, 30, 2, SR15, (1, 1)),
 P('Corpo · cabeceira e peseira', I11, 104, 30, 2, SR15, (1, 1)),
 P('Proteção · lado longo · campo', I11, 88, 27, 1, SR15, (0, 0),
   'Substrato da palhinha · ⛔ sem fita'),
 P('Proteção · cabeceira e peseira · campo', I11, 107, 27, 2, SR15, (0, 0),
   'Substrato da palhinha · ⛔ sem fita'),
 P('Proteção · moldura · régua longa de 88', I11, 88, 5, 2, SR15, (2, 2),
   '⛔ moldura de OUTRA COR: régua é régua'),
 P('Proteção · moldura · régua longa de 107', I11, 107, 5, 4, SR15, (2, 2)),
 P('Proteção · moldura · régua curta', I11, 17, 5, 6, SR15, (2, 2),
   '27 menos as duas réguas de 5'),
 P('Bicama · frente',       I11, 195, 25, 1, SR15, (2, 2)),
 P('Bicama · lateral',      I11, 98, 25, 2, SR15, (1, 0)),
 P('Bicama · costas',       I11, 192, 25, 1, SR15, (1, 0)),

 # ══ ITEM 12 · NOME MARIANA — ELEVAÇÃO 04, sem detalhamento ═══════════
 #  "Nome em MDF sal rosa - Arauco com espessura de 3cm"
 #  ⭐ 3 cm aqui é mesmo chapa dupla: letra recortada não aceita engradado
 P('Letra · camada',        I12, 73, 20, 2, SR15, (2, 2),
   '⭐ duas chapas de 15 coladas dão os 3 cm que a ELEVAÇÃO 04 escreve · '
   '⚠ a medida saiu do desenho em 1/25, que não cota o nome'),
]

# ── ferragem, declarada item a item ─────────────────────────────────────
GAVETAS = []  # ⛔ as três gavetas foram para CORREDIÇA TOUCH, ver OUTRAS
# ⭐ DOZE DOBRADIÇAS NA ESTANTE [Jonathan, 28/10/2026]: "são 12 dobradiças
#   no total". Eu havia posto quatro por folha — 16 — porque a porta tem
#   até 174 de altura. São TRÊS por folha: 4 × 3 = 12.
PORTAS  = [(I1, 'Estante · quatro portas de giro recortadas na empena, '
            'de até 174 de altura · ⭐ três dobradiças por folha', 4, 3,
            DOBRADICA),
           (I3, 'Mesa com armário · uma porta de giro de 60', 1, 2,
            DOBRADICA)]
BASCULAS = [(I1, 'Armário de 100 da estante · duas básculas, de 85 e de 37',
             2, 'pulsador')]
CAVA    = [(I11, 'Frente da bicama', 1, 195)]
PUXADORES = []
MOLDURA = []
# ⭐ as duas fitas que a prancha escreve: "com fita de led embutido acima"
#   na empena do DET 01 e na da casinha do DET 06
LED     = [(I1, 'Embutida acima do ripado, nas duas águas da empena', 2.8),
           (I6, 'Embutida acima, nas águas de 190 e de 198 da casinha', 3.9)]
CABIDEIROS = []
# ⭐ o engradado que dá os 3 cm dos dois painéis, sem dobrar a chapa
SARRAFOS = []  # ⛔ pinus PROIBIDO: os dois engradados viraram travessa de MDF
SUPORTES = []
ALMAS   = []
VIDRO   = []
# ⭐ ESTRUTURA DE SERRALHERIA NA CAMA [Jonathan, 28/10/2026]: "item 11:
#   considere a palha indiana e a estrutura de serralheria". A palha já
#   estava (0,82 m² de palhinha natural); a serralheria entra agora.
#   ⛔ SEM PREÇO, e de propósito: serralheria é orçamento FECHADO por peça
#     e o senhor não deu o valor desta. O banco do Living foi R$ 2.500 e a
#     mesa da Suíte Hóspedes R$ 450 — não dá para interpolar entre os dois.
#   ⚠ E fica a pergunta na caixa de dúvidas: esta estrutura SUBSTITUI os
#     dois quadros de estrado em metalon, ou se somam? Uma cama
#     montessoriana tem o colchão quase no chão, e pode ser que o quadro
#     de metalon já seja a estrutura.
SERRALHERIA = [(I11, 'Estrutura da cama montessoriana e da bicama', 0.0)]
# ⭐ as frentes emolduradas não têm puxador nenhum desenhado, e cava
#   cortaria a palha: é o pulsador que sobra, como na Suíte Hóspedes, no
#   Banho Hóspedes e no Banho Gourmet.
OUTRAS  = [
           (I1, 'Perfil de proteção de piso', 'Estante com armário de 350', 3.5, 'm',
            'Perfil de proteção de piso'),
           (I3, 'Perfil de proteção de piso', 'Mesa com armário de 235', 2.35, 'm',
            'Perfil de proteção de piso'),
           (I6, 'Perfil de proteção de piso', 'Casinha de 350', 3.5, 'm',
            'Perfil de proteção de piso'),
           (I11, 'Perfil de proteção de piso', 'Cama montessoriana de 207', 2.07, 'm',
            'Perfil de proteção de piso'),
           # ⭐⭐ A PALHA É PALHINHA NATURAL, NÃO CHAPA [Jonathan, 28/10/2026]:
           #   "a palha indiana (650,00) o metro quadrado". Eu a orçava
           #   como melamínico, uns R$ 137 o m²; ela custa R$ 650. Os
           #   campos saem da conta de chapa e entram como tapeceiro,
           #   trançados dentro das molduras de Sal Rosa.
           (I1, 'Palhinha natural', 'Campo das quatro portas de 61 × 174 e '
            'das duas básculas de 100 · 4,25 + 0,85 + 0,37', 5.47, 'm²',
            'Palhinha natural'),
           (I3, 'Palhinha natural', 'Campo das três gavetas de 53 × 20 e da '
            'porta de 53 × 60 da mesa', 0.64, 'm²', 'Palhinha natural'),
           (I11, 'Palhinha natural', 'Campo da proteção da cama '
            'montessoriana · lado longo e as duas pontas', 0.82, 'm²',
            'Palhinha natural'),
           # ⭐ ESTRADO EM METALON · R$ 250 o quadro [Jonathan, 28/10/2026]
           (I11, 'Estrado em metalon', 'Dois quadros: o do colchão de '
            '207 × 104 e o da bicama de 192 × 98 · ⛔ substitui os dois '
            'painéis de MDF', 2, 'quadro', 'Estrado em metalon'),
           (I1, 'Pulsador', 'Quatro portas e duas básculas da estante · '
            'abre por toque, sem ferragem à vista', 6, 'un', 'Pulsador'),
           (I2, 'Rodízio deslizante', 'Quatro por caixa, duas caixas · '
            '⛔ sem preço na Base', 8, 'un', 'Rodízio deslizante'),
           (I3, 'Pulsador', 'A porta de giro de 60 da mesa · abre por '
            'toque, sem ferragem à vista · ⛔ só a porta: as três gavetas '
            'foram para corrediça touch', 1, 'un', 'Pulsador'),
           (I3, 'Corrediça touch', 'Três gavetas de 20 da mesa · abre por '
            'toque · ⛔ substitui o par de corrediça e o pulsador',
            3, 'par', 'Corrediça touch'),
           (I4, 'Suporte para rolo de papel', 'Um, na travessa de cima · '
            '⛔ sem preço na Base', 1, 'un', 'Suporte para rolo de papel'),
           (I11, 'Rodízio deslizante', 'Quatro na bicama · ⛔ sem preço na '
            'Base', 4, 'un', 'Rodízio deslizante'),
           (I12, 'Usinagem de letra em router', 'Sete letras de "Mariana" '
            'em chapa dupla de 3 cm · ⛔ sem preço na Base', 7, 'un',
            'Usinagem de letra em router')]

# ⭐ MODO MISTO DENTRO DO MESMO MÓVEL [Jonathan, 28/10/2026]. A regra da
#   casa é uma abertura por frente, e aqui há DUAS espécies de frente no
#   mesmo móvel: as GAVETAS, que desde 28/10 abrem por CORREDIÇA TOUCH, e
#   a PORTA de giro, que não tem corrediça nenhuma e abre por PULSADOR.
#   ⛔ Não é pagar duas vezes: são frentes diferentes. Fica declarado para
#     a auditoria não confundir soma de modos com soma de custo.
ABRE_MISTO = [I3]

CABECA = {
 I1: ('350 × 300 × 30',
      'VISTA FRONTAL 3 + 61 + 61 + 61 + 61 + 3 + 100 = 350 · altura 174 do '
      'corpo mais 126 das pernas = 300 · armário de 100 com básculas de 85 '
      'e de 37 · VISTA SUPERIOR 350 × 30 · ⭐ as quatro portas são '
      'RECORTADAS na linha da empena, e o ripado de 3 com vão de 1 é o que '
      'aparece por baixo delas'),
 I2: ('50 × 46 × 35  ·  duas',
      'DET. 02 VISTA SUPERIOR 50 × 35 · FRONTAL 35 × 46 · LATERAL 50 × 46 · '
      '⭐ a ELEVAÇÃO 01 desenha DUAS, lado a lado sob a mesa do DET 03 · '
      'MDF Sal Rosa com rodinhas deslizantes'),
 I3: ('235 × 66 × 50',
      'DET. 03 VISTA FRONTAL 123 da mesa mais 112 do armário = 235 · altura '
      '66 · três gavetas de 20 e uma porta · VISTA SUPERIOR e LATERAL 50 de '
      'profundidade · frentes em Palha Indiana com moldura de 5 em Sal Rosa'),
 I4: ('105 × 145 × 19',
      'DET. 04 VISTA FRONTAL 105 × 145 · VISTA SUPERIOR 18 + 68 + 20 com 19 '
      'de aba · duas travessas de 19 atravessam o painel: a de cima segura '
      'o rolo de papel, a de baixo é o apoio'),
 I5: ('105 × 135 × 3',
      'DET. 05 VISTA FRONTAL 105 × 135, com 3 de espessura · ⭐ 3 cm em MDF '
      'não é chapa, é construção: painel de 15 sobre engradado de MDF'),
 I6: ('350 × 219 × 25',
      'DET. 06 VISTA FRONTAL 10 + 40 + 290 + 10 = 350 · altura 219 na '
      'cumeeira e 126 na beirada · águas de 190 e de 198 · VISTA SUPERIOR '
      '175 + 175 = 350 com 25 de profundidade · quatro NICHOS de 40 em Sal '
      'Rosa na espessura, janelinha fake e LED embutido na empena'),
 I7: ('83 × 60 × 50',
      'DET. 07 VISTA FRONTAL 83 de largura · altura 2 + 27 + 2 + 27 + 2 = '
      '60 · VISTA SUPERIOR 83 × 50 · ⭐ a caixa é Paris e o nicho interno é '
      'Sal Rosa, que é o que a prancha escreve'),
 I8: ('330 × 145 × 3',
      'DET. 08 VISTA FRONTAL 330 × 145, com 3 de espessura · ⛔ 330 não sai '
      'de uma chapa: duas peças de 165 · os 3 cm saem do engradado'),
 I9: ('114 × 15 × 8',
      'DET. 09 VISTA SUPERIOR 3 + 109 + 3 = 114 com 15 de profundidade · '
      'VISTA FRONTAL 114 × 8 · prateleira baixa, com borda de contenção'),
 I10: ('91 × 64 × 40',
       'DET. 10 VISTA SUPERIOR 2 + 81 + 2 + 7 = 91 com 40 de profundidade · '
       'VISTA FRONTAL 2 + 83 + 7, altura 24 + 40 = 64 · ⭐ o CORTE mostra a '
       'escada de encaixes: a prateleira sobe e desce com a criança'),
 I11: ('207 × 107 × 57',
       'DET. 11 VISTA SUPERIOR 207 × 107 · FRONTAL 207 com 27 de proteção e '
       '30 de corpo · ⭐ o corpo de 30 guarda a BICAMA, e a proteção é '
       'Palha Indiana emoldurada em Sal Rosa, como as frentes do DET 01'),
 I12: ('73 × 20 × 3',
       'ELEVAÇÃO 04, em letra e SEM detalhamento: "Nome em MDF sal rosa - '
       'Arauco com espessura de 3cm" · ⚠ a medida saiu do desenho em 1/25 · '
       '⭐ aqui os 3 cm são mesmo chapa dupla: letra recortada não aceita '
       'engradado'),
}

FOLHA = dict(
 aba='SUÍTE MARIANA',
 sub='Jéssica e Michell · Projeto ICA · páginas 177 a 191 · DOZE itens em '
     'sete folhas de detalhe, o ambiente com mais itens do projeto · ⭐ três '
     'fornecedores numa peça só: frente em Palha Indiana Sextavada '
     '(Duratex), moldura de 5 cm em Sal Rosa (Arauco), estrutura em Paris '
     f'(Guararapes) · peça inteira até {ALT_MAX:g}, que é a chapa de '
     f'{CHAPA_C:g} menos o acerto de corte',
 chapa_txt={PA15: 'Paris · Guararapes · a estrutura de tudo: estante, mesa, '
                  'casinha, painéis, mesa lateral e escrivaninha',
            PA6:  'Paris · fundos de encaixe em rasgo, sem fita',
            SR15: 'Sal Rosa · Arauco · ripado, molduras de 5 cm, nichos, '
                  'caixas organizadoras, prateleira, cama e o nome',
            SR6:  'Sal Rosa · os fundos que APARECEM dentro dos nichos',
            PI18: 'Palha Indiana Sextavada Natural · Duratex · o campo de '
                  'todas as frentes e das proteções da cama',
            BR15: 'Branco TX · só a janelinha fake da casinha, que a '
                  'prancha manda fazer em branco para representar vidro',
            BR6:  'Branco TX · o fundo das três caixas de gaveta da mesa, '
                  'que fica escondido dentro da gaveta'},
 nota='⛔ O FRETE ESTÁ ZERADO DE PROPÓSITO: as linhas de frete da Base não '
      'têm preço ainda. Preencher lá e elas aparecem aqui sozinhas.   '
      '⭐⭐ TRÊS FORNECEDORES NUMA PEÇA SÓ, e isso é novo no projeto: a '
      'frente é Palha Indiana Sextavada da DURATEX, a moldura de 5 cm é Sal '
      'Rosa da ARAUCO e a estrutura é Paris da GUARARAPES. São três '
      'pedidos, três fretes e três arredondamentos num quarto só.   '
      '⭐ A MOLDURA É DE OUTRA COR, então aqui régua continua sendo régua — '
      'peça inteira de Sal Rosa cobriria a palha. É o terceiro e último '
      'lugar do projeto onde isso vale.   ⛔⛔ OS PAINÉIS TÊM 3 CM: lancei '
      'painel de 15 sobre ENGRADADO DE SARRAFO, não duas chapas coladas. '
      'A dúvida 04 traz os dois números.   ⚠ O NOME "MARIANA" da ELEVAÇÃO '
      '04 é marcenaria, está escrito em letra e não tem DET: entrou como '
      'item 12, com a usinagem em router a zero.',
 duvidas=[
  'A LARGURA DAS QUATRO PORTAS DA ESTANTE eu li como 61 cada, pela cadeia '
  '3 + 61 + 61 + 61 + 61 + 3 + 100 = 350 da VISTA FRONTAL. ⚠ Mas elas são '
  'RECORTADAS na linha da empena, e a prancha não cota a altura de cada '
  'uma: lancei as quatro no retângulo cheio de 61 × 174, que é de onde a '
  'peça sai. ⛔ Para o CORTE está certo; para a FITA está por cima, porque '
  'a aresta inclinada é mais curta que a soma dos dois catetos. Confirmar '
  'se o senhor quer que eu refaça a fita pela diagonal real.',
  'O RIPADO DA EMPENA DO DET 01 tem 235 de largura por 212 de altura, com '
  'ripa de 3 e vão de 1 — isso a prancha escreve, e é a primeira vez no '
  'projeto que ela escreve. ⚠ São 59 ripas de 3 × 212, e a filetagem delas '
  'é MANUAL, R$ 5,00. ⛔ A mão de obra do ripado (R$ 180/m² na Base) '
  'continua FORA, pela mesma razão do Banho Gourmet: a Base não diz se '
  'esse valor já inclui a chapa. São 5 m² aqui.',
  'A ALTURA DO RIPADO eu tirei do 212 da VISTA FRONTAL, mas a mesma vista '
  'traz 174 + 126 = 300 e um 66 solto no pé. ⚠ Se o ripado parar nos 174 '
  'do corpo, são 38 cm a menos de altura em 59 ripas — quase uma chapa de '
  'Sal Rosa. É a segunda cota mais cara desta aba.',
  'OS PAINÉIS DO DET 05 E DO DET 08 TÊM 3 CM DE ESPESSURA. ⭐ Lancei painel '
  'de 15 mm sobre ENGRADADO DE MDF: dá os 3 cm, é como se faz, e a travessa '
  'sai da própria chapa. ⚠ A alternativa literal — duas chapas de 15 coladas '
  '— acrescentaria 6,2 m² de Paris, que são DUAS chapas e R$ 1.400. ⛔ '
  'Confirmar, porque é a diferença entre um painel e um painel caro.',
  'O NOME "MARIANA" DA ELEVAÇÃO 04 está em letra e não tem detalhamento: '
  '"Nome em MDF sal rosa - Arauco com espessura de 3cm". ⭐ Lancei como '
  'item 12, duas chapas de 15 coladas e sete letras. ⚠ A medida — 73 × 20 '
  '— saiu do desenho em 1/25, que não cota o nome; e a USINAGEM EM ROUTER '
  'não tem preço na Base. Letra recortada em MDF de 3 cm é serviço de CNC '
  'e costuma sair de R$ 40 a R$ 120 por letra.',
  'A BICAMA DO DET 11 aparece escrita na VISTA FRONTAL e desenhada em '
  'corte, mas sem cota própria. ⚠ Tirei 195 × 98 × 25 do corpo de 207 × '
  '107 × 30 e lancei quatro rodízios, que também não têm preço na Base. '
  'Confirmar se a bicama leva colchão nosso ou do cliente.',
  'AS FRENTES EMOLDURADAS NÃO TÊM PUXADOR DESENHADO — nem as quatro portas '
  'e duas básculas da estante, nem as três gavetas e a porta da mesa. ⭐ '
  'Orcei PULSADOR em todas as dez, R$ 1.000, pela mesma razão dos outros '
  'três ambientes: cava cortaria a palha e puxador aparafusado o desenho '
  'mostraria. ⚠ Alternativa: Alças Traso 128 saem R$ 1.100.',
  'A CAIXA ORGANIZADORA DO DET 02 tem "rodinhas deslizantes" e eu contei '
  'DUAS caixas, que é o que a ELEVAÇÃO 01 desenha sob a mesa. ⚠ O rodízio '
  'não tem preço na Base — são oito. E a caixa não tem tampo nem puxador '
  'desenhado: é caixote aberto, do jeito que a perspectiva mostra.',
  'A ESCRIVANINHA DO DET 10 TEM ENCAIXES usinados na lateral, para a '
  'prateleira subir e descer. ⚠ Isso é usinagem de router linha a linha, '
  'não corte: o CORTE desenha uma escada de uns vinte encaixes. Não lancei '
  'mão de obra de usinagem — a Base não tem a linha, e é o mesmo buraco da '
  'moldura provençal.',
  'A PRATELEIRA DO DET 09 aparece na ELEVAÇÃO 03 e na 04, e eu contei UMA: '
  'as duas elevações mostram o mesmo canto, acima da escrivaninha. ⚠ Se '
  'forem duas, é só dobrar a linha — são R$ 60 de chapa.',
  '⛔ A BASE METÁLICA DE 3 CM não está lançada aqui. Tocam o chão a '
  'estante, a mesa, a casinha, a mesa lateral e a cama. ⚠ São uns 10 m de '
  'rodapé neste ambiente, o maior do projeto. Fica para a passada única.',
  'A CABECEIRA ESTOFADA ROSA aparece com DUAS medidas: 205 × 100 na '
  'ELEVAÇÃO 03 e 187 × 100 na ELEVAÇÃO 04. ⚠ Não é nossa — é estofador — '
  'mas a diferença de 18 cm sugere que uma das duas elevações está '
  'desatualizada, e vale avisar a arquiteta.'],
 nao_marcenaria=[
  'Cabeceira estofada rosa — ⚠ 205 × 100 na ELEVAÇÃO 03 e 187 × 100 na 04',
  'Puff estofado na cor rosa 100 × 60 e cadeira infantil borboleta rosa',
  'Abajur de linho com estrutura na cor rosa',
  'Painel de porcelana jardim terrosos e o papel de parede de folhagem',
  'Persiana romana de linho',
  'Colchão da cama e colchão da bicama',
  'TV 32" da estante do DET 01'],
 notas=[
  '⭐⭐ É O AMBIENTE COM MAIS ITENS DO PROJETO: doze, contra dez da Sala de '
  'Cinema e oito do Living. E nenhum deles é um armário — casinha, cama '
  'montessoriana com bicama, escrivaninha com encaixes, caixa '
  'organizadora com rodinha, prateleira baixa, o nome recortado na parede. '
  'Quarto de criança se orça peça a peça, não módulo a módulo.',
  '⭐⭐ TRÊS FORNECEDORES NUMA PEÇA SÓ, e isso não tinha acontecido ainda: '
  'a frente da porta é Palha Indiana Sextavada da DURATEX, a moldura de 5 '
  'cm que a contorna é Sal Rosa da ARAUCO, e a caixa atrás é Paris da '
  'GUARARAPES. ⚠ Três pedidos, três fretes e três arredondamentos de chapa '
  'cheia num quarto de 15 m². Vale perguntar à arquiteta se há equivalente '
  'de Sal Rosa na Duratex — juntaria duas compras em uma.',
  '⭐ A MOLDURA DE 5 CM É DE OUTRA COR, e por isso aqui régua continua '
  'sendo régua. Peça inteira de Sal Rosa por cima da Palha Indiana '
  'cobriria justamente o que se quer ver. É o terceiro e último lugar do '
  'projeto onde a regra da peça inteira usinada na router não vale — os '
  'outros dois são o aparador da Suíte Hóspedes e a bancada do Banho '
  'Hóspedes, e os três têm a mesma frente.',
  '⛔ 350 NÃO SAI DE UMA CHAPA, e as duas peças de 350 do ambiente — a '
  'estante do DET 01 e a casinha do DET 06 — já vêm desenhadas em duas '
  'metades de 175 na VISTA SUPERIOR. É a primeira vez neste executivo que '
  'o desenho antecipa o plano de corte.',
  '⭐ OS 3 CM DOS PAINÉIS SAEM DO ENGRADADO, não de duas chapas coladas. '
  'Painel de 15 mm sobre travessa de MDF de 5 cm dá a mesma espessura por '
  'uma fração do que custa a chapa a mais. ⛔ A exceção é o nome "Mariana": letra '
  'recortada não aceita engradado, e ali os 3 cm são mesmo chapa dupla.',
  '⚠ DUAS FITAS DE LED, e as duas a prancha escreve com a mesma frase: '
  '"com fita de led embutido acima". Uma na empena do ripado da estante, '
  'outra na empena da casinha — 6,7 m somadas, R$ 1.005.'],
)
