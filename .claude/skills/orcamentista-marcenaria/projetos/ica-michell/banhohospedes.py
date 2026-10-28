# -*- coding: utf-8 -*-
"""ICA · BANHO HÓSPEDES — levantamento peça por peça  [28/10/2026]

páginas 118 a 123 · dois detalhamentos, dois itens, uma folha só de detalhe.

⭐ É O BANHEIRO DA SUÍTE HÓSPEDES e usa o mesmo par de padrões: Oásis Linha
  Essencial Wood na caixa e na moldura, Palha Indiana Sextavada Natural na
  frente da gaveta. A frente repete, peça por peça, a do aparador do DET 06
  da suíte — moldura de 2 cm em OUTRA COR, e por isso quatro réguas por
  frente e não peça inteira.

⭐ A ELEVAÇÃO FECHA A ALTURA, e isso é raro neste executivo: 15 do piso ao
  móvel + 60 do móvel com a pedra + 15 da cuba de apoio = 90 na borda, que
  é a altura certa de um lavatório. O móvel é SUSPENSO, com 15 de vão.
  ⛔ Então aqui não há base metálica a lançar: não há base nenhuma.

⛔ A BANCADA É QUARTZITO BIANCO SUPERIORE, com 10 de espessura aparente.
  Marmoraria. A cuba é redonda de apoio e a torneira é de mesa, bica alta.

⚠ O NICHO É EMBUTIDO NA PAREDE. O que é nosso é a caixa de 40 × 174 × 11 e
  a fita de LED de cada um dos quatro vãos. O rasgo na alvenaria, o
  acabamento da borda e a passagem da fiação não estão nesta conta.
"""
from base import P, gaveta, ALT_MAX, CHAPA_C

OA18, OA6 = 'MDF Oásis 18', 'MDF Oásis 6'
PI18 = 'MDF Palha Indiana Sextavada 18'
EST, FUN = 'MDF Branco TX 15', 'MDF Branco TX 6'

I1 = 'DET 01 Bancada com armário'
I2 = 'DET 02 Nichos'

BANHOHOSPEDES = [
 # ══ ITEM 01 · BANCADA COM ARMÁRIO — 100 × 50 × 50 ════════════════════
 #  VISTA FRONTAL  100 de largura · altura 10 de quartzito + 25 + 25 = 60
 #  VISTA SUPERIOR 100 × 50 · ELEVAÇÃO 03 e 04  15 + 60 + 15 = 90
 #  ⭐ frente em Palha Indiana com moldura de 2 em Oásis — OUTRA COR, e
 #    por isso são QUATRO RÉGUAS por frente, não peça inteira
 P('Lateral',               I1, 50, 50, 2, OA18, (1, 1),
   'Aparente dos dois lados: é suspensa, com 15 de vão até o piso'),
 P('Base',                  I1, 96, 50, 1, OA18, (1, 0),
   'Aparente por baixo: é suspensa'),
 P('Travessa de apoio da bancada', I1, 96, 10, 2, EST, (1, 0),
   'Frente e fundo · ⭐ a pedra apoia nelas, não em tampo cheio'),
 P('Fundo',                 I1, 100, 50, 1, FUN, (0, 0), 'Encaixe em rasgo'),
 # ⭐⭐ A PALHA É PALHINHA NATURAL, NÃO CHAPA [Jonathan, 28/10/2026]: "na
 #   cabeceira vc nao considerou a palha indiana (650,00) o metro
 #   quadrado". ⛔ Eu a orçava como melamínico — R$ 700 a chapa, uns R$ 137
 #   o m² depois do aproveitamento — e ela custa R$ 650 o m². Era cinco
 #   vezes menos. O campo sai da conta de chapa e entra como material de
 #   tapeceiro, trançado dentro da moldura: 0,96 × 0,25 × 2 = 0,48 m².
 #   ⚠ A moldura continua em Oásis e continua sendo régua.

 P('Frente · gaveta · campo', I1, 96, 25, 2, EST, (0, 0),
   '⭐ Substrato da PALHINHA NATURAL [Jonathan, 28/10/2026]: a palha '
   'indiana custa R$ 650 o m² e é tapeceiro, não chapa · a peça fica '
   'porque a palhinha precisa de fundo em que se fixar, mas sai no MDF '
   'estrutural · ⛔ sem fita: as arestas morrem sob a moldura'),
 P('Frente · moldura · régua longa', I1, 96, 2, 4, OA18, (2, 2),
   '⛔ MOLDURA DE OUTRA COR: duas réguas de 2 em Oásis por frente, em cima '
   'e embaixo · peça inteira cobriria a palha, então aqui régua é régua'),
 P('Frente · moldura · régua curta', I1, 21, 2, 4, OA18, (2, 2),
   'As duas laterais de cada frente'),
 *gaveta(I1, 96, 45, 25, 2, 'Gaveta'),

 # ══ ITEM 02 · NICHOS — 40 × 174 × 11 ═════════════════════════════════
 #  DET. 02 VISTA FRONTAL  2 + 36 + 2 = 40 de largura
 #                         altura 2 + 50 + 2 + 33 + 2 + 33 + 2 + 49 + 2
 #  DET. 02 VISTA SUPERIOR profundidade 11
 #  ELEVAÇÃO 03  101 do piso + 174 do nicho + 25 = 300 de pé-direito
 P('Lateral',               I2, 174, 11, 2, OA18, (1, 0),
   '⭐ embutido na parede: só a aresta da frente aparece, e ela tem 174'),
 P('Topo e base',           I2, 36, 11, 2, OA18, (1, 0), 'Aparente'),
 P('Prateleira',            I2, 36, 11, 3, OA18, (1, 0),
   'Três divisórias para quatro nichos de 50, 33, 33 e 49'),
 P('Fundo',                 I2, 40, 174, 1, OA6, (0, 0),
   '⭐ O FUNDO APARECE: é ele que o LED lava, e por isso sai em Oásis, não '
   'em branco · 6 mm por encaixe em rasgo, sem fita'),
]

# ── ferragem, declarada item a item ─────────────────────────────────────
GAVETAS = [(I1, 'Bancada com armário · duas gavetas de 25', 2, 450)]
PORTAS  = []
BASCULAS= []
CAVA    = []
PUXADORES= []
MOLDURA = []
#  ⭐ uma fita por nicho, no topo de cada um · 4 × 36 cm
LED     = [(I2, 'Uma fita no topo de cada um dos quatro nichos', 1.44)]
CABIDEIROS = []
SARRAFOS= []
SUPORTES= []
ALMAS   = []
# ⭐ O ESPELHO ENTRA NA CONTA [Jonathan, 28/10/2026]: "considerar o espelho
#   e a palinha natural". O oval de 60 × 150 estava em NÃO É MARCENARIA e
#   não devia estar: quem compra e instala é a casa. 0,90 m² pelo
#   retângulo que o contém — oval se corta de chapa retangular.
VIDRO   = [(I1, 'Espelho oval de 60 × 150 da ELEVAÇÃO 04 · medido pelo '
            'retângulo que o contém, que é como o vidraceiro corta',
            1, 60, 150, 'Espelho')]
SERRALHERIA = []
# ⭐ as duas gavetas não têm puxador nenhum desenhado, e a frente é Palha
#   Indiana emoldurada: cava cortaria a palha. Mesma leitura do aparador da
#   Suíte Hóspedes e da porta ripada do Banho Gourmet.
OUTRAS  = [(I1, 'Pulsador', 'Duas gavetas da bancada · abre por toque, sem '
            'ferragem à vista · ⚠ a prancha não desenha puxador nenhum',
            2, 'un', 'Pulsador'),
           # ⭐ PALHINHA NATURAL · R$ 650 o m² [Jonathan, 28/10/2026]
           (I1, 'Palhinha natural', 'O campo das duas frentes de gaveta, '
            '96 × 25 cada · trançado dentro da moldura de Oásis · ⛔ é '
            'tapeceiro, não chapa: saiu da conta de MDF', 0.48, 'm²',
            'Palhinha natural')]
# ⭐ nada neste banheiro toca o chão: a bancada é suspensa com 15 de vão e
#   o nicho começa a 101 do piso — não há perfil de proteção de piso.

CABECA = {
 I1: ('100 × 50 × 50',
      'VISTA FRONTAL 100 de largura · altura 10 de quartzito mais 25 + 25 '
      'de gaveta = 60 · VISTA SUPERIOR e LATERAL profundidade 50 · ELEVAÇÃO '
      '03 e 04 dão 15 do piso + 60 + 15 da cuba = 90 na borda · ⭐ frente '
      'em Palha Indiana Sextavada com moldura de 2 em Oásis, que é OUTRA '
      'COR e por isso sai em quatro réguas'),
 I2: ('40 × 174 × 11',
      'DET. 02 VISTA FRONTAL 2 + 36 + 2 = 40 · altura 2 + 50 + 2 + 33 + 2 + '
      '33 + 2 + 49 + 2 ≈ 174 · VISTA SUPERIOR profundidade 11 · quatro '
      'nichos, cada um com a sua fita de LED no topo'),
}

FOLHA = dict(
 aba='BANHO HÓSPEDES',
 sub='Jéssica e Michell · Projeto ICA · páginas 118 a 123 · dois itens, uma '
     'folha só de detalhe · ⭐ o mesmo par de padrões da suíte ao lado: '
     'Oásis Linha Essencial Wood na caixa e na moldura, Palha Indiana '
     'Sextavada na frente · caixaria em Branco TX 15 · peça inteira até '
     f'{ALT_MAX:g}, que é a chapa de {CHAPA_C:g} menos o acerto de corte',
 chapa_txt={OA18: 'Oásis Linha Essencial Wood · Duratex · caixa da bancada, '
                  'moldura das frentes e o nicho inteiro',
            OA6:  'Oásis · o fundo dos nichos, que é o que o LED lava',
            PI18: 'Palha Indiana Sextavada Natural · o campo das duas frentes',
            EST:  'Estrutura e caixaria · o padrão da Base para caixaria',
            FUN:  'Fundos · encaixe em rasgo, sem fita'},
 nota='⛔ O FRETE ESTÁ ZERADO DE PROPÓSITO: as linhas de frete da Base não '
      'têm preço ainda. Preencher lá e elas aparecem aqui sozinhas.   '
      '⛔ A BANCADA É QUARTZITO BIANCO SUPERIORE, com 10 de espessura '
      'aparente: é marmoraria, e o que está nesta conta é só a caixa que a '
      'sustenta.   ⚠ O NICHO DO DET 02 É EMBUTIDO NA PAREDE. O que é nosso '
      'é a caixa de 40 × 174 × 11 e as quatro fitas de LED; o rasgo na '
      'alvenaria, o acabamento da borda e a passagem da fiação, não.   '
      '⭐ A ELEVAÇÃO FECHA A ALTURA, o que é raro neste executivo: 15 do '
      'piso + 60 do móvel com a pedra + 15 da cuba de apoio = 90 na borda. '
      'O móvel é SUSPENSO, e por isso aqui não há base metálica a lançar.   '
      '⭐⭐ CINCO PADRÕES PARA CATORZE PEÇAS: a regra de ferro cobra CINCO '
      'chapas cheias, R$ 2.350, para 5,7 m² de peça. É o ambiente onde o '
      'arredondamento mais pesa no projeto inteiro — e QUATRO desses cinco '
      'padrões são os mesmos da Suíte Hóspedes ao lado.',
 duvidas=[
  'AS DUAS GAVETAS NÃO TÊM PUXADOR DESENHADO, e a prancha não escreve cava, '
  'não escreve puxador e não escreve fecho toque. ⭐ Orcei PULSADOR, R$ 100 '
  'cada, R$ 200 pelos dois — é o mesmo que fiz no aparador da Suíte '
  'Hóspedes, pela mesma razão: a frente é Palha Indiana emoldurada e cava '
  'cortaria a palha. ⚠ As alternativas: cava usinada sairia R$ 96 pelas '
  'duas frentes de 96; Alças Traso 128, R$ 220. Decisão de desenho, e vale '
  'R$ 104 para baixo ou R$ 20 para cima.',
  'O FUNDO DO NICHO saiu em Oásis 6 mm, não em branco. ⚠ São quatro nichos '
  'com LED no topo de cada um: o fundo é justamente a superfície que a luz '
  'lava, e é ele que se vê de frente. Se o desenho quiser o fundo em outro '
  'padrão — espelho, pedra, laca — muda a chapa e muda o preço. A '
  'perspectiva do DET 02 desenha fundo e laterais na mesma madeira.',
  'O NICHO É EMBUTIDO NA PAREDE e tem 11 de profundidade. ⚠ Quem abre o '
  'rasgo na alvenaria, quem acaba a borda e quem passa a fiação do LED não '
  'está dito. Orcei a caixa de marcenaria, que é a parte que é nossa. ⛔ Se '
  'o rasgo for nosso, é serviço de obra e não cabe em quantitativo de '
  'marcenaria — tem de ir para a proposta como item à parte.',
  'A CAIXA DA BANCADA TEM 50 DE PROFUNDIDADE, igual à pedra. ⚠ O normal é '
  'o armário ser 3 a 5 cm mais raso que o tampo, para a pedra ter beiral e '
  'a frente não bater na porta de correr do box. A VISTA LATERAL do DET 01 '
  'não cota a profundidade do móvel, só a da pedra. Confirmar antes do '
  'corte: cada 5 cm aqui são 0,3 m² de chapa.',
  'A FRENTE DA GAVETA É PALHA INDIANA SEXTAVADA NATURAL e a Base ainda não '
  'tem esse padrão cotado de verdade: lancei R$ 700 a chapa de 18, como '
  'melamínico fosco. ⚠ É a mesma pergunta da dúvida 05 da Suíte Hóspedes, e '
  'a resposta vale para os dois ambientes de uma vez.',
  'O ESPELHO OVAL DE 60 × 150 da ELEVAÇÃO 04 não é nosso: é vidraceiro. ⚠ '
  'Mas espelho oval costuma pedir moldura ou um sarrafo de apoio, e a '
  'prancha não desenha nenhum dos dois. Confirmar quem fixa.'],
 nao_marcenaria=[
  'Bancada em Quartzito Bianco Superiore, 100 × 50 com 10 de espessura aparente',
  'Cuba Redonda de Apoio 30 cm Branco Slim e Torneira de Mesa Bica Alta '
  'Corten Unic — Deca',
  'Espelho oval de 60 × 150 da ELEVAÇÃO 04',
  'Bacia para caixa acoplada, papeleira, box até o teto e revestimentos'],
 notas=[
  '⭐ A FRENTE DAQUI É A MESMA DO APARADOR DA SUÍTE HÓSPEDES, peça por '
  'peça: campo em Palha Indiana Sextavada e moldura de 2 cm em Oásis. Como '
  'a moldura é de OUTRA COR, peça inteira cobriria a palha — então são '
  'quatro réguas por frente, e este é o segundo dos dois únicos lugares do '
  'projeto onde régua continua sendo régua.',
  '⭐ A ELEVAÇÃO FECHA A ALTURA: 15 do piso ao móvel, 60 do móvel com a '
  'pedra, 15 da cuba de apoio — 90 na borda, que é a altura certa de um '
  'lavatório. É a primeira vez neste executivo que a elevação resolve a '
  'altura que o detalhamento não cota. ⛔ E resolve de um jeito que apaga '
  'uma pergunta: móvel suspenso não tem base metálica.',
  '⭐ O NICHO INTEIRO É APARENTE, dos dois lados e no fundo, e mesmo assim '
  'gasta pouco: 40 × 174 × 11 dá 0,8 m² de Oásis 18 mais 0,7 m² de Oásis 6. '
  'O que pesa nele é o LED — 1,44 m de fita a R$ 150 o metro.',
  '⚠ NENHUMA PEÇA PASSA DA CHAPA. A maior é a lateral do nicho, de 174 × '
  '11, e o fundo de 174 × 40 — os dois cabem inteiros nos 275 × 185.',
  '⭐⭐ AQUI O ARREDONDAMENTO É A CONTA. São 5,7 m² de peça e CINCO padrões '
  'de chapa, um para cada: a regra de ferro cobra cinco chapas cheias, '
  '20,4 m² úteis comprados para 5,7 m² usados. R$ 2.350 de MDF num móvel '
  'que tem 1,8 m² de frente. É o pior arredondamento do projeto, e não é '
  'erro de conta — é o que custa um banheiro pequeno com cinco materiais.',
  '⭐⭐ E ELE TEM CONSERTO NA PRODUÇÃO: QUATRO dos cinco padrões daqui são '
  'os mesmos da Suíte Hóspedes ao lado — Oásis 18, Palha Indiana Sextavada '
  '18, Branco TX 15 e Branco TX 6. Produzidos juntos, as peças deste '
  'banheiro saem da SOBRA da suíte, e o que resta de compra própria é só a '
  'chapa de Oásis 6 do fundo do nicho. ⚠ No orçamento cada ambiente fecha '
  'em chapa cheia, que é o certo para precificar; na fábrica, não. Se o '
  'senhor quiser, eu fecho um arredondamento CONJUNTO dos dois ambientes '
  'na versão enxuta da proposta. ⭐ Conferi a conta: os dois juntos dão '
  'R$ 8.750 de MDF contra R$ 10.750 separados — as quatro chapas comuns '
  'absorvem o banheiro inteiro sem puxar nenhuma a mais. São R$ 2.000.'],
)
