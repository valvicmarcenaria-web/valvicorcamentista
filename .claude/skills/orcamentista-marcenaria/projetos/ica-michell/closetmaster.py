# -*- coding: utf-8 -*-
"""ICA · CLOSET MASTER — levantamento peça por peça  [28/10/2026]

páginas 153 a 165 · SEIS detalhamentos, seis itens, cinco folhas de detalhe.

⭐⭐ UMA COR SÓ, E É BRANCA: MDF Branco Diamante - Duratex nos seis itens,
  do fundo do nicho à porta de correr. Depois da Suíte Master, com três
  padrões e dois fornecedores, este compra UM material e arredonda UMA vez.
  ⚠ Lancei no preço de COR (R$ 700 a chapa de 18, R$ 600 a de 25), que é o
    lado conservador. Branco Diamante é branco texturado como o Branco TX, e
    a dúvida 01 põe a diferença na mesa: se for cobrado como branco, são
    R$ 300 por chapa A MENOS.

⭐⭐ A CADEIA VERTICAL DOS TRÊS ARMÁRIOS É A MESMA, e ela fecha:
      3 de topo + 60 de maleiro + 3 + 30 de nicho + 3 + 193 de corpo = 292
    e o resto é a base. ⛔ A prancha ainda desenha um "53" solto no pé de
    cada ladder, que não existe no desenho — somando-o a cadeia daria 345
    contra os 300 cotados. Ignorei o 53; o 193 fecha sozinho, e no DET 02
    ele se abre em 22 + 22 + 22 + 22 + 23 + 82, que dá exatamente 193.

⭐ É O AMBIENTE DE FERRAGEM DO PROJETO: oito sapateiras corrediças, seis
  sapateiras fixas, três cabideiros, dois calceiros deslizantes, um
  gavetão de cesto de roupa e vinte gavetas. ⛔ O calceiro deslizante não
  existe na Base e sai ZERO.

⛔ O pé-direito de 300 volta: lateral, divisória e fundo dos três armários
  e do nicho passam dos 273 da chapa.
"""
from base import P, gaveta, ALT_MAX, CHAPA_C

BD18, BD15, BD6 = ('MDF Branco Diamante 18', 'MDF Branco Diamante 15',
                   'MDF Branco Diamante 6')
# ⭐⭐ A ESTRUTURA SOBE PARA 25 MM [Jonathan, 28/10/2026]
#   > "No closet master considere a estrutura em mdf de 25mm"
#   ⛔ ESTRUTURA é o que SEGURA: lateral, divisória, tampo, base e a
#     divisória do nicho — as peças de 300 de altura que carregam o closet.
#     NÃO é a caixa de gaveta, que continua em 15, nem a frente nem a
#     prateleira, que continuam em 18. Numa coluna de 3 m é a lateral que
#     empena, e é ela que o senhor está reforçando.
#   ⚠ O 25 mm não tem preço na Base. Lancei um INTERINO declarado de
#     R$ 970 — o 18 na proporção 25/18 — e ele está na caixa de dúvidas.
BD25 = 'MDF Branco Diamante 25'

I1 = 'DET 01 Nichos'
I2 = 'DET 02 Armário 01'
I3 = 'DET 03 Armário 02'
I4 = 'DET 04 Armário 03'
I5 = 'DET 05 Painel com espelho'
I6 = 'DET 06 Porta de correr'

CLOSETMASTER = [
 # ══ ITEM 01 · NICHOS — 80 × 300 × 40 ═════════════════════════════════
 #  VISTA FRONTAL  80 de largura · altura 2 + 43 + 2 + 48 + 2 + 48 + 2 +
 #                 48 + 2 + 48 + 2 + 48 + 5 = 300 · SEIS nichos com LED
 #  VISTA SUPERIOR 80 = 30 de curva + 50 · profundidade 40 · canto de 90°
 P('Lateral',            I1, 300, 40, 2, BD25, (1, 0),
   'Aparente · ⛔ 300 de altura contra 273 de peça inteira'),
 P('Tampo e base',       I1, 80, 40, 2, BD25, (1, 0)),
 P('Prateleira',         I1, 80, 40, 5, BD18, (2, 2),
   '⭐ 18 mm porque o vão de 80 passa dos 70 da regra · a frente é '
   'ARREDONDADA, como a VISTA SUPERIOR mostra: é peça de canto'),
 P('Fundo',              I1, 80, 273, 1, BD6, (0, 0),
   '⭐ aparece dentro do nicho, por isso sai em Branco Diamante e não em '
   'branco de caixaria · ⛔ desenhado com 300 de altura'),

 # ══ ITEM 02 · ARMÁRIO 01 — 140 × 300 × 50 ════════════════════════════
 #  VISTA FRONTAL  3 + 50 + 3 + 53 + 3 + 29 ≈ 140 · três colunas
 #                 altura 3 + 60 + 3 + 30 + 3 + 193 ≈ 300
 #                 o corpo de 193 = 22 + 22 + 22 + 22 de sapateira + 23 de
 #                 nicho + 82 de gavetão
 P('Lateral',            I2, 300, 50, 2, BD25, (1, 0), '⛔ 300 de altura'),
 P('Divisória',          I2, 300, 50, 2, BD25, (1, 0),
   'As duas verticais que fazem as colunas de 50, 53 e 29 · ⛔ 300 de altura'),
 P('Tampo e base',       I2, 134, 50, 2, BD25, (1, 0)),
 P('Prateleira do maleiro', I2, 134, 50, 1, BD18, (1, 0),
   '⭐ 18 mm: o vão corrido de 134 passa dos 70'),
 P('Prateleira do nicho', I2, 134, 50, 1, BD18, (1, 0)),
 P('Sapateira corrediça · coluna de 50', I2, 50, 50, 4, BD15, (2, 2),
   'Quatro, de 22 em 22 · corre para fora, então as quatro arestas aparecem '
   '· ⛔ CORRE em par de corrediça, que já está orçado: sem suporte'),
 P('Sapateira corrediça · coluna de 53', I2, 53, 50, 4, BD15, (2, 2),
   'Quatro, de 22 em 22 · ⛔ corre em corrediça, já orçada: sem suporte'),
 P('Prateleira do nicho baixo', I2, 50, 50, 1, BD18, (1, 0)),
 P('Prateleira do nicho baixo · coluna de 53', I2, 53, 50, 1, BD18, (1, 0)),
 P('Frente · gavetão do cesto de roupa', I2, 50, 82, 1, BD18, (2, 2),
   '⛔ NÃO É BASCULANTE [Jonathan, 28/10]: é gaveta de corrediça, como as '
   'outras · puxador cava'),
 P('Frente · gavetão',   I2, 53, 41, 2, BD18, (2, 2), 'Dois, de 41 cada · puxador cava'),
 P('Fundo',              I2, 140, 273, 1, BD6, (0, 0),
   'Encaixe em rasgo · ⛔ 300 de altura, rebaixado para os 273 da chapa'),
 *gaveta(I2, 53, 45, 41, 2, 'Gavetão', cor=BD15, fundo=BD6),
 *gaveta(I2, 50, 45, 82, 1, 'Gaveta do cesto de roupa', cor=BD15, fundo=BD6),

 # ══ ITEM 03 · ARMÁRIO 02 — 480 × 300 × 60 ════════════════════════════
 #  VISTA FRONTAL  3 + 105 + 3 + 90 + 3 + 97 + 3 + 173 ≈ 480
 #                 altura 3 + 60 + 3 + 30 + 3 + 193 ≈ 300
 #  ⭐ a coluna de 97 leva o ESPELHO COM LED FRONTAL
 P('Lateral',            I3, 300, 60, 2, BD25, (1, 0), '⛔ 300 de altura'),
 P('Divisória',          I3, 300, 60, 3, BD25, (1, 0),
   'As três verticais das quatro colunas · ⛔ 300 de altura'),
 P('Tampo e base',       I3, 237, 60, 4, BD25, (1, 0),
   'Duas peças em cada: 474 de corrida não sai de uma chapa'),
 P('Prateleira do maleiro · coluna de 105', I3, 105, 60, 1, BD18, (1, 0)),
 P('Prateleira do maleiro · coluna de 90',  I3, 90, 60, 1, BD18, (1, 0)),
 P('Prateleira do maleiro · coluna de 97',  I3, 97, 60, 1, BD18, (1, 0)),
 P('Prateleira do maleiro · coluna de 173', I3, 173, 60, 1, BD18, (1, 0)),
 P('Prateleira do nicho · coluna de 105',   I3, 105, 60, 1, BD18, (1, 0)),
 P('Prateleira do nicho · coluna de 90',    I3, 90, 60, 2, BD18, (1, 0),
   'Duas: a coluna de 90 tem DOIS níveis de nicho, de 43 cada'),
 P('Nicho · divisória vertical', I3, 65, 60, 1, BD25, (1, 0),
   'Parte a coluna de 90 em dois nichos de 43'),
 P('Prateleira do nicho · coluna de 173',   I3, 173, 60, 1, BD18, (1, 0)),
 P('Prateleira',         I3, 90, 60, 1, BD18, (1, 0),
   'A que a VISTA FRONTAL chama de "Prateleira", abaixo dos nichos'),
 P('Frente · gaveta da coluna de 90', I3, 90, 20, 4, BD18, (2, 2),
   'Quatro gavetas de 20 · puxador cava'),
 P('Painel de apoio do espelho', I3, 97, 120, 1, BD18, (2, 2),
   '⭐ o espelho é do vidraceiro, mas ele cola em alguma coisa · a '
   'iluminação é frontal, no perímetro'),
 P('Frente · gaveta sob o espelho', I3, 49, 20, 1, BD18, (2, 2), 'Puxador cava'),
 P('Frente · gaveta sob o espelho · 48', I3, 48, 20, 1, BD18, (2, 2), 'Puxador cava'),
 P('Sapateira · coluna de 173', I3, 84, 60, 3, BD18, (2, 2),
   'Três sapateiras fixas de 84, ao lado do calceiro'),
 P('Fundo',              I3, 240, 150, 4, BD6, (0, 0),
   '⛔ 480 × 300 de fundo não sai nem de duas chapas: quatro peças de '
   '240 × 150 · encaixe em rasgo, sem fita'),
 *gaveta(I3, 90, 55, 20, 4, 'Gaveta', cor=BD15, fundo=BD6),
 *gaveta(I3, 49, 55, 20, 2, 'Gaveta do espelho', cor=BD15, fundo=BD6),

 # ══ ITEM 04 · ARMÁRIO 03 — 260 × 300 × 60 ════════════════════════════
 #  VISTA FRONTAL  104 + 80 + 67 ≈ 260 com as três verticais de 3
 #                 altura 3 + 60 + 3 + 30 + 3 + 193 ≈ 300
 #  ⭐ maleiro, nicho, cabideiro, calceiro deslizante, gavetas, gavetão e
 #    sapateira — o armário mais completo dos três
 P('Lateral',            I4, 300, 60, 2, BD25, (1, 0), '⛔ 300 de altura'),
 P('Divisória',          I4, 300, 60, 2, BD25, (1, 0), '⛔ 300 de altura'),
 P('Tampo e base',       I4, 254, 60, 2, BD25, (1, 0)),
 P('Prateleira do maleiro · coluna de 104', I4, 104, 60, 1, BD18, (1, 0)),
 P('Prateleira do maleiro · coluna de 80',  I4, 80, 60, 1, BD18, (1, 0)),
 P('Prateleira do maleiro · coluna de 67',  I4, 67, 60, 1, BD18, (1, 0)),
 P('Prateleira do nicho · coluna de 104',   I4, 104, 60, 1, BD18, (1, 0)),
 P('Prateleira do nicho · coluna de 80',    I4, 80, 60, 3, BD18, (1, 0),
   'Três: a coluna do meio é toda de nichos, de 24 em 24'),
 P('Prateleira do nicho · coluna de 67',    I4, 67, 60, 1, BD18, (1, 0)),
 P('Sapateira',          I4, 27, 60, 4, BD18, (2, 2),
   '⭐ RELIDO [Jonathan, 28/10]: a sapateira é a coluna ESTREITA de 27 da '
   'VISTA FRONTAL, não os 104 inteiros · quatro prateleiras'),
 # ⭐⭐ SÃO DEZ GAVETAS, NÃO QUATRO [Jonathan, 28/10/2026]: "item 4 - sao 10
 #   gavetas". Reli a VISTA FRONTAL e ele está certo — a cadeia de baixo é
 #   27 + 78 + 43 + 39 + 3 + 67 + 3, e eu tinha lido as três colunas de
 #   gaveta como uma só de 80. São quatro gavetas de 78, quatro de 43, uma
 #   de 39 e um gavetão de 39 × 64. Dez frentes, dez pares de corrediça e
 #   dez cavas — eu contava quatro.
 P('Frente · gaveta · coluna de 78', I4, 78, 21, 4, BD18, (2, 2),
   'Quatro gavetas de 21 na coluna de 78 · puxador cava'),
 P('Frente · gaveta · coluna de 43', I4, 43, 21, 4, BD18, (2, 2),
   'Quatro gavetas de 21 na coluna de 43 · puxador cava'),
 P('Frente · gaveta · coluna de 39', I4, 39, 21, 1, BD18, (2, 2),
   'A de cima da coluna de 39 · puxador cava'),
 P('Frente · gavetão · coluna de 39', I4, 39, 64, 1, BD18, (2, 2),
   'Os 64 de altura que a VISTA FRONTAL cota embaixo · puxador cava'),

 P('Fundo',              I4, 260, 150, 2, BD6, (0, 0),
   '⛔ 260 × 300 não sai de uma chapa: duas peças de 260 × 150 · encaixe '
   'em rasgo, sem fita'),
 *gaveta(I4, 78, 55, 21, 4, 'Gaveta de 78', cor=BD15, fundo=BD6),
 *gaveta(I4, 43, 55, 21, 4, 'Gaveta de 43', cor=BD15, fundo=BD6),
 *gaveta(I4, 39, 55, 21, 1, 'Gaveta de 39', cor=BD15, fundo=BD6),
 *gaveta(I4, 39, 55, 64, 1, 'Gavetão de 39', cor=BD15, fundo=BD6),

 # ══ ITEM 05 · PAINEL COM ESPELHO — 160 × 300 ═════════════════════════
 #  VISTA FRONTAL  160 × 300 · painel em MDF com espelho e iluminação
 #                 frontal · tem vão para a porta do DET 06 correr
 P('Painel · faixa alta', I5, 160, 150, 1, BD18, (2, 2),
   '⛔ 300 de altura não sai de uma chapa: duas peças de 150, e a emenda '
   'fica atrás do espelho'),
 P('Painel · faixa baixa', I5, 160, 150, 1, BD18, (2, 2)),

 # ══ ITEM 06 · PORTA DE CORRER — 110 × 220 ════════════════════════════
 #  VISTA FRONTAL  110 × 220 · corre no vão do painel do DET 05
 P('Folha da porta de correr', I6, 110, 220, 1, BD18, (2, 2),
   'Peça inteira: 220 cabe nos 273 da chapa'),
]

# ── ferragem, declarada item a item ─────────────────────────────────────
GAVETAS = [(I2, 'Armário 01 · dois gavetões de 41 e o cesto de roupa', 3, 450),
           (I3, 'Armário 02 · quatro gavetas de 20 e duas sob o espelho',
            6, 550),
           (I4, 'Armário 03 · nove gavetas de 21 e um gavetão de 64 · '
            'DEZ, relidas em 28/10', 10, 550)]
PORTAS  = []
# ⛔⛔ NÃO EXISTE GAVETÃO BASCULANTE [Jonathan, 28/10/2026]: "item 2 - não
#   existe gaveta basculante, considere apenas a corrediça". Eu tinha lido
#   o cesto de roupa do Armário 01 como báscula que tomba para fora e
#   lancei um articulador a gás HK-XS de R$ 250 nele. Não é: é gaveta
#   comum, e o que ela leva é o par de corrediça que já estava na conta.
BASCULAS= []
#  ⭐ puxador cava em toda frente deste ambiente
CAVA    = [(I2, 'O cesto de roupa e os dois gavetões do Armário 01', 3, 52),
           (I3, 'As quatro gavetas de 90 e as duas sob o espelho', 6, 76),
           (I4, 'Quatro gavetas de 78',                   4, 78),
           (I4, 'Quatro gavetas de 43',                   4, 43),
           (I4, 'A gaveta e o gavetão da coluna de 39',   2, 39)]
PUXADORES= []
MOLDURA = []
# ⭐ A ILUMINAÇÃO DO ESPELHO ESTAVA NO ITEM ERRADO [Jonathan, 28/10/2026]:
#   "item 5 - considere o espelho e iluminação". Ela é do DET 05, o painel
#   com espelho, e eu a tinha pendurado no DET 03. E o perímetro não é
#   4,40: o painel tem 160 × 300, logo 2 × (1,60 + 3,00) = 9,20 m de fita.
LED     = [(I1, 'Um por nicho, nos seis nichos de 80', 4.80),
           (I5, 'Iluminação frontal do espelho · perímetro do painel de '
            '160 × 300', 9.20)]
CABIDEIROS = [(I2, 'Cabideiro para vestidos, na coluna de 29', 1),
              (I3, 'Cabideiro nas colunas de 105 e de 173', 2),
              (I4, 'Cabideiro na coluna de 67', 1)]
SARRAFOS= []
SUPORTES= []
ALMAS   = []
# ⭐ O ESPELHO ENTRA NA CONTA [Jonathan, 28/10/2026]. O DET 05 é "painel em
#   MDF com espelho, com iluminação frontal" — o espelho é a peça, não o
#   acessório. 150 × 290 dentro do painel de 160 × 300.
#   ⭐ E O DA COLUNA DE 97 DO ARMÁRIO 02 ENTRA COM ELE: é a mesma regra, e
#     deixar um espelho do ambiente fora e o outro dentro seria incoerente.
#     Está na caixa de dúvidas como decisão minha, para ele desfazer se
#     quiser.
VIDRO   = [(I5, 'Espelho do painel do DET 05 · 150 × 290 dentro do painel '
            'de 160 × 300, com o LED correndo no perímetro', 1, 150, 290,
            'Espelho'),
           (I3, 'Espelho da coluna de 97 do Armário 02 · 97 × 120, colado '
            'no painel de apoio de Branco Diamante', 1, 97, 120,
            'Espelho')]
SERRALHERIA = []
# ⛔ duas ferragens de closet que a Base não tem: o calceiro deslizante e o
#   trilho da porta de correr do DET 06.
OUTRAS  = [(I2, 'Perfil de proteção de piso', 'Armário 01 de 212', 2.12,
            'm', 'Perfil de proteção de piso'),
           (I3, 'Perfil de proteção de piso', 'Armário 02 de 281', 2.81,
            'm', 'Perfil de proteção de piso'),
           (I4, 'Perfil de proteção de piso', 'Armário 03 de 260', 2.60,
            'm', 'Perfil de proteção de piso'),
           (I5, 'Perfil de proteção de piso', 'Painel com espelho de 160',
            1.60, 'm', 'Perfil de proteção de piso'),
           (I3, 'Calceiro deslizante', 'Na coluna de 173 do Armário 02 · '
            '⛔ sem preço na Base', 1, 'un', 'Calceiro deslizante'),
           (I4, 'Calceiro deslizante', 'Na coluna de 80 do Armário 03 · '
            '⛔ sem preço na Base', 1, 'un', 'Calceiro deslizante'),
           (I6, 'Trilho de porta de correr', 'Folha de 110 × 220 em MDF de '
            '18 · ⛔ sem preço na Base', 1, 'jogo',
            'Trilho de porta de correr')]

CABECA = {
 I1: ('80 × 300 × 40',
      'VISTA FRONTAL 80 de largura · altura 2 + 43 + 2 + 48 + 2 + 48 + 2 + '
      '48 + 2 + 48 + 2 + 48 + 5 = 300 · SEIS nichos, um LED em cada · '
      'VISTA SUPERIOR 30 de curva mais 50, profundidade 40, canto de 90°'),
 I2: ('140 × 300 × 50',
      'VISTA FRONTAL 3 + 50 + 3 + 53 + 3 + 29 ≈ 140 · altura 3 + 60 de '
      'maleiro + 3 + 30 de nicho + 3 + 193 de corpo ≈ 300 · o corpo de 193 '
      'se abre em 22 + 22 + 22 + 22 de sapateira + 23 de nicho + 82 de '
      'gavetão, que fecha exato'),
 I3: ('480 × 300 × 60',
      'VISTA FRONTAL 3 + 105 + 3 + 90 + 3 + 97 + 3 + 173 ≈ 480 · altura 3 '
      '+ 60 + 3 + 30 + 3 + 193 ≈ 300 · quatro colunas, e a de 97 leva o '
      'espelho com LED frontal'),
 I4: ('260 × 300 × 60',
      'VISTA FRONTAL 104 + 80 + 67 ≈ 260 · altura 3 + 60 + 3 + 30 + 3 + '
      '193 ≈ 300 · três colunas com maleiro, nicho, cabideiro, calceiro '
      'deslizante, gavetas, gavetão e sapateira'),
 I5: ('160 × 300',
      'VISTA FRONTAL 160 × 300 · painel em MDF com espelho e iluminação '
      'frontal · tem vão para a porta do DET 06 correr'),
 I6: ('110 × 220',
      'VISTA FRONTAL 110 × 220 · corre no vão do painel do DET 05'),
}

FOLHA = dict(
 aba='CLOSET MASTER',
 sub='Jéssica e Michell · Projeto ICA · páginas 153 a 165 · SEIS itens em '
     'cinco folhas de detalhe · ⭐ UMA COR SÓ e ela é branca: Branco '
     'Diamante Duratex nos seis itens · ⛔ pé-direito de 300 contra peça '
     f'inteira de {ALT_MAX:g}, que é a chapa de {CHAPA_C:g} menos o acerto '
     'de corte',
 chapa_txt={BD18: 'Branco Diamante · Duratex · prateleiras, frentes, '
                  'sapateiras e painéis',
            BD15: 'Branco Diamante · Duratex · laterais, divisórias, '
                  'sapateiras corrediças e caixas de gaveta',
            BD25: 'Branco Diamante · Duratex · ⭐ A ESTRUTURA DOS TRÊS '
                  'ARMÁRIOS [Jonathan, 28/10]: laterais, divisórias, tampos '
                  'e bases · ⚠ R$ 600 a chapa, ABAIXO do 18 mm',
            BD6:  'Branco Diamante · Duratex · fundos · ⭐ sai na cor e não '
                  'em branco de caixaria, porque dentro de closet aberto '
                  'TUDO aparece'},
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem [Jonathan, 29/10]: '
      'a QUANTIDADE é a célula AMARELA no fim do painel de material, e ela '
      'sai ZERO. Digite quantas viagens este ambiente leva e o frete '
      'aparece aqui e no Painel.   '
      '⭐⭐ UMA COR SÓ NO AMBIENTE INTEIRO, e ela é branca. Branco Diamante '
      'Duratex nos seis itens, inclusive nos fundos — dentro de closet '
      'aberto não existe peça que não apareça. ⚠ Lancei no preço de COR '
      '(R$ 700 a chapa de 18, R$ 600 a de 25), que é o lado conservador; se '
      'a Duratex cobrar como branco são R$ 300 a MENOS por chapa.   ⭐ A '
      'CADEIA VERTICAL DOS TRÊS ARMÁRIOS '
      'FECHA: 3 + 60 de maleiro + 3 + 30 de nicho + 3 + 193 de corpo = 292, '
      'e o resto é base. ⛔ O "53" solto no pé de cada ladder da prancha '
      'não existe no desenho — somando-o a cadeia daria 345 contra os 300 '
      'cotados.   ⭐ É O AMBIENTE DE FERRAGEM DO PROJETO: oito sapateiras '
      'corrediças, sete fixas, quatro cabideiros, dois calceiros '
      'deslizantes, um gavetão de cesto de roupa e vinte gavetas.',
 duvidas=[
  'BRANCO DIAMANTE É BRANCO OU É COR? Lancei no preço de COR — R$ 700 a '
  'chapa de 18, R$ 550 a de 15, R$ 350 a de 6 e R$ 600 a de 25 —, que é o '
  'lado conservador. ⚠ Mas Branco Diamante é um branco texturado, irmão do '
  'Branco TX que a casa já usa em toda a caixaria: se a Duratex cobrar como '
  'branco (R$ 400 / 350 / 250), este ambiente CAI quase 40%. ⛔ É a '
  'pergunta que mais vale dinheiro nesta aba, e ela se responde com uma '
  'ligação.',
  '⚠ O MDF DE 25 MM CUSTA MENOS QUE O DE 18 NA MESMA COR: R$ 600 contra '
  'R$ 700, pelo preço que o senhor passou em 29/10. ⭐ Lancei como o senhor '
  'disse, e a estrutura dos três armários saiu nele, como pedido em 28/10 '
  '— laterais, divisórias, tampos e bases. ⛔ Chapa mais grossa saindo mais '
  'barata é incomum; se o fornecedor confirmar, melhor para nós, porque é '
  'justamente a chapa que mais aparece em metro quadrado aqui.',
  'O CALCEIRO DESLIZANTE não existe na Base e sai ZERO. São dois, um no '
  'Armário 02 e outro no Armário 03. ⚠ Calceiro deslizante de closet custa '
  'de R$ 150 a R$ 400 a unidade conforme a largura e o acabamento. ⛔ Até '
  'existir, o custo dos dois armários é um PISO.',
  'O TRILHO DA PORTA DE CORRER DO DET 06 também não existe na Base. ⚠ A '
  'folha é pequena — 110 × 220 em MDF de 18 — então é trilho leve, não o de '
  'carga da Sala de Cinema. Mesmo assim, sem preço.',
  'A PRANCHA DESENHA UM "53" SOLTO no pé da cadeia vertical dos três '
  'armários. Somando-o, a cadeia dá 345 contra os 300 que o próprio '
  'desenho cota. ⭐ Ignorei o 53: sem ele, 3 + 60 + 3 + 30 + 3 + 193 = 292 '
  'e o 193 do DET 02 se abre em 22 + 22 + 22 + 22 + 23 + 82, que fecha '
  'exato. ⚠ Confirmar, porque 45 cm de altura em três armários de 300 é '
  'meia chapa por armário.',
  'AS SAPATEIRAS CORREDIÇAS DO ARMÁRIO 01 — oito, de 22 em 22 — levam '
  'corrediça por par, e eu as contei como gaveta sem caixa: a sapateira é '
  'uma prateleira que corre, não um gavetão. ⚠ Orcei a corrediça de 450 mm '
  'em cada, mas NÃO orcei caixa nem frente, porque a prancha desenha '
  'prateleira nua. Confirmar se levam borda de contenção.',
  'O ESPELHO DO PAINEL DO DET 05 É NOSSO desde 28/10 e entrou no '
  'levantamento — 4,35 m² de 150 × 290 dentro do painel de 160 × 300, com os '
  '4,4 m de LED do perímetro. ⛔ A linha "Espelho" da Base segue SEM PREÇO, '
  'então ele soma ZERO: o custo deste ambiente é um piso enquanto ela não '
  'tiver valor. ⚠ A prancha não cota o espelho — tirei a medida do desenho '
  'em 1/20, descontando 5 cm de painel aparente em volta.',
  'O ESPELHO DA COLUNA DE 97 DO ARMÁRIO 02 TAMBÉM ENTROU, e essa foi '
  'decisão minha. ⚠ O senhor nomeou o espelho do DET 05; este é o segundo '
  'do mesmo ambiente, e deixar um dentro e o outro fora não se sustenta na '
  'proposta. São 1,16 m² de 97 × 120, colados no painel de apoio em Branco '
  'Diamante que já estava orçado. ⛔ Como a linha "Espelho" da Base não tem '
  'preço, ele soma ZERO — entrar ou sair não move o custo de hoje, move '
  'quando o preço do vidro chegar. A prancha não cota: tirei 97 × 120 do '
  'desenho em 1/20.',
  'O CESTO DE ROUPA DO ARMÁRIO 01 DEIXOU DE SER BASCULANTE [Jonathan, '
  '28/10]: "não tem gaveta basculante". ⭐ Virou gaveta de corrediça de '
  '450 mm, como as outras duas da coluna, e o articulador HK-XS de R$ 250 '
  'saiu da conta. ⚠ Fica o registro de que é cesto de roupa: se o cliente '
  'quiser o cesto removível de aramado, isso é ferragem de terceiro e não '
  'está em nenhuma linha da Base.',
  '⛔ A BASE METÁLICA DE 3 CM não está lançada aqui. Os três armários e o '
  'nicho tocam o chão. ⚠ Fica para a passada única, junto com os outros '
  'dezoito ambientes.'],
 nao_marcenaria=[
  'Cabides, caixas organizadoras e tudo que o cliente põe dentro'],
 notas=[
  '⭐⭐ UMA COR SÓ, E ELA É BRANCA. Branco Diamante Duratex nos seis itens, '
  'do fundo do nicho à porta de correr. Depois da Suíte Master, com três '
  'padrões e dois fornecedores, este ambiente compra um material e '
  'arredonda uma vez — é o oposto do Banho Hóspedes.',
  '⭐ O FUNDO SAI NA COR, não em branco de caixaria. Dentro de closet '
  'aberto não existe peça escondida: o fundo do nicho é a superfície que '
  'se vê de frente, e em três armários de 300 de altura isso é bastante '
  'metro quadrado.',
  '⭐ A CADEIA VERTICAL É A MESMA NOS TRÊS ARMÁRIOS: 3 de topo, 60 de '
  'maleiro, 3, 30 de nicho, 3, e 193 de corpo. Só o que vai dentro do 193 '
  'muda — sapateira corrediça e gavetão no 01, gaveta e espelho no 02, '
  'calceiro e sapateira no 03. Isso facilita o corte: as laterais e as '
  'divisórias dos três são a mesma peça.',
  '⚠ É O AMBIENTE DE FERRAGEM DO PROJETO. Oito sapateiras corrediças, sete '
  'fixas, quatro cabideiros, dois calceiros deslizantes, um gavetão '
  'de cesto de roupa e vinte gavetas. A ferragem pesa mais que a chapa aqui, e '
  'dois itens dela saem ZERO porque a Base não os tem.'],
)
