# -*- coding: utf-8 -*-
"""ICA · HOME OFFICE — levantamento peça por peça  [28/10/2026]

páginas 094 a 103 · quatro detalhamentos, quatro itens.

⭐⭐ TRÊS CORES APARENTES NO MESMO AMBIENTE, e é a primeira vez no projeto:
      Lacca Fume · Eucatex ....... DET 01 inteiro e o tampo da mesa
      Nogueira Caiena · Duratex .. o painel e o corpo do superior
      Preto Ultra Premium ........ SÓ as quatro básculas do DET 04
  Três arredondamentos de chapa, não um. ⛔ "Lacca Fume" não está nomeado
  na Base: entrou como melamínico fosco, como o Preto Ultra Premium.

⭐⭐ DUAS PEÇAS PASSAM DOS 275 E NENHUMA DELAS É ALTURA — são CORRIDAS. O
  painel do DET 03 tem 350 de largura e o tampo da mesa tem 335. Dividi
  cada uma em duas, e no DET 04, que também tem 335, a emenda cai na
  divisória do segundo vão de 83.

⚠⚠ A MESA É UM TAMPO SOLTO DE 335 × 60 COM 7 DE ESPESSURA, e a prancha
  não desenha NENHUM apoio: sem pé, sem cavalete, sem lateral. Orcei o
  tampo como CAIXÃO — duas faces e borda — porque MDF não existe em 70 mm,
  e deixei o apoio na caixa de dúvidas. ⛔ Um tampo de 3,35 m sem apoio no
  meio não para em pé: ou é mão-francesa, ou é estrutura, ou é pé.

⭐ O DET 04 TEM O INTERIOR À VISTA NA FILEIRA DE BAIXO. São quatro nichos
  ABERTOS e iluminados, e o que se vê dentro deles sai em Nogueira Caiena,
  não em Branco TX. A fileira de cima fecha com báscula e aí a caixaria
  volta a ser branca, pela regra da casa.
"""
from base import (P, gaveta, acabamento, ALT_MAX, CHAPA_C, DOBRADICA, ALTAS)

LF18 = 'MDF Lacca Fume 18'
NC18, NC6 = 'MDF Nogueira Caiena 18', 'MDF Nogueira Caiena 6'
PT18 = 'MDF Preto Ultra Premium 18'
EST, FUN = 'MDF Branco TX 15', 'MDF Branco TX 6'
PRAT18   = 'MDF Branco TX 18'   # ⭐ só onde o vão passa de 70 cm

# ⭐⭐ ITEM ÚNICO [Jonathan, 28/10/2026]: "tbm considere o conjunto apenas
#   um item". Os quatro detalhamentos são uma parede só de home office —
#   armário embaixo, mesa, painel atrás e superior em cima, todos na mesma
#   prumada de 335/350. ⛔ Cada peça guarda o DET de origem no nome.
I = 'DET 01 a 04 Conjunto do home office'
I1 = I2 = I3 = I4 = I

HOMEOFFICE = [
 # ══ ITEM 01 · ARMÁRIO — 237 × 68 × 40 ════════════════════════════════
 #  VISTA FRONTAL  4 × 59 = 236 ≈ 237 · altura 4 + 59 + 5 = 68
 #  VISTA FRONTAL INTERNA  115 + 2 + 115 · interno 4 + 27 + 27 + 5
 #  VISTA LATERAL  profundidade 40, com recuo de 30 + 10 embaixo do LED
 P('Lateral · DET 01', I1, 59, 40, 2, EST, (1, 0)),
 P('Divisória central · DET 01', I1, 59, 40, 1, EST, (1, 0), 'Dois vãos de 115'),
 P('Base · DET 01', I1, 233, 40, 1, EST, (1, 0),
   '⭐ o recuo de 10 × 5 da VISTA LATERAL é onde corre o LED da iluminação '
   'inferior: a base não vai até a frente'),
 P('Tampo superior · DET 01', I1, 237, 40, 1, LF18, (2, 2),
   'Aparente · a prancha desenha 4 de testeira e chama de "tampo superior"'),
 P('Fundo · DET 01', I1, 237, 59, 1, FUN, (0, 0), 'Encaixe em rasgo'),
 P('Prateleira · DET 01', I1, 115, 38, 2, PRAT18, (1, 0),
   '⭐ "armário interno com prateleiras em MDF Branco" — a prancha escreve a '
   'cor · vão de 115 passa dos 70, então 18 mm contra empeno'),
 P('Frente · porta de giro · DET 01', I1, 59, 59, 4, LF18, (2, 2),
   'Lisa · "puxador cava na própria madeira", como a prancha escreve'),

 # ══ ITEM 02 · MESA — 335 × 60 × 7 ════════════════════════════════════
 #  VISTA SUPERIOR  335 × 60 · as duas torres de tomada a 80 e a 50 das pontas
 #  VISTA FRONTAL e LATERAL  espessura 7 ⚠ MDF não existe em 70 mm: caixão
 P('Tampo · face superior · DET 02', I2, 167.5, 60, 2, LF18, (2, 2),
   '⛔ 335 de corrida não cabe na chapa: duas peças de 167,5'),
 P('Tampo · face inferior · DET 02', I2, 167.5, 60, 2, EST, (1, 0),
   '⚠ em Branco TX: é a face de baixo de um tampo encostado na parede, sob '
   'o painel do DET 03 · se tiver de sair em Lacca Fume, soma chapa'),
 P('Tampo · borda longa · DET 02', I2, 167.5, 7, 4, LF18, (2, 2),
   'Frente e fundo do caixão, duas peças cada'),
 P('Tampo · borda de topo · DET 02', I2, 60, 7, 2, LF18, (2, 2), 'As duas pontas'),
 # ⛔ PINUS PROIBIDO [Jonathan, 28/10/2026]: o quadro interno do caixão do
 #   tampo era sarrafo de pinus, 11 m, e agora é TRAVESSA DE MDF tirada da
 #   própria chapa — vira peça no plano de corte em vez de metro invisível.
 P('Engradado · travessa de MDF · DET 02', I2, 273, 5, 4, EST, (0, 0),
   'Perímetro do caixão do tampo mais duas travessas · 11 m de travessa de '
   '5 cm · ⛔ sem fita: é estrutura interna e não aparece'),
 P('Tampo · recorte da torre de tomadas · DET 02', I2, 10, 10, 2, LF18, (0, 0),
   '⚠ duas torres, a 80 e a 50 das pontas · entra como PERDA de chapa, não '
   'como peça, e perda não leva fita: ⛔ sem fita · o furo sai do tampo e a torre em si não é nossa'),

 # ══ ITEM 03 · PAINEL — 350 × 169 × 3 ═════════════════════════════════
 #  VISTA FRONTAL  350 de largura × 169 de altura · espessura 3
 P('Painel · DET 03', I3, 175, 169, 2, NC18, (2, 2),
   '⛔ 350 de corrida não cabe na chapa: duas peças de 175 · ⚠ a prancha '
   'desenha 3 cm de espessura e MDF não existe em 30 mm — orçado em 18'),

 # ══ ITEM 04 · ARMÁRIO SUPERIOR — 335 × 131 × 40 ══════════════════════
 #  VISTA FRONTAL  4 × 83 = 332 ≈ 335 · altura 6 + 63 + 63 = 132 ≈ 131
 #  VISTA LATERAL  131 no total, 125 de corpo, 6 de fechamento · fundo 40
 #  ⭐ fileira de cima com báscula PRETA · fileira de baixo em nicho ABERTO
 P('Lateral e divisória · bloco de básculas · DET 04', I4, 63, 40, 5, EST, (1, 0),
   'Dois laterais e três divisórias, nos quatro vãos de 83'),
 P('Topo · DET 04', I4, 167.5, 40, 2, EST, (1, 0),
   '⛔ 335 de corrida não cabe: duas peças, com a emenda na divisória do '
   'segundo vão de 83'),
 P('Fundo · bloco de básculas · DET 04', I4, 167.5, 63, 2, FUN, (0, 0), 'Encaixe em rasgo'),
 P('Fechamento superior · DET 04', I4, 167.5, 6, 2, NC18, (2, 2),
   'A faixa de 6 de ponta a ponta · aparente, em Nogueira Caiena'),
 P('Prateleira entre os dois blocos · DET 04', I4, 167.5, 40, 2, NC18, (2, 2),
   '⭐ é o teto dos nichos abertos: vista de baixo, sai em Nogueira Caiena · '
   '⛔ é HORIZONTAL FIXA — o teto de um bloco e a base do outro, cavilhada '
   'nas divisórias: sem suporte, sem alma'),
 P('Lateral e divisória · bloco de nichos · DET 04', I4, 63, 40, 5, NC18, (1, 1),
   '⭐ nicho ABERTO: o que se vê por dentro sai na cor, não em Branco TX'),
 P('Base dos nichos · DET 04', I4, 167.5, 40, 2, NC18, (2, 2), 'Aparente'),
 P('Fundo dos nichos · DET 04', I4, 167.5, 63, 2, NC6, (0, 0),
   '⭐ fundo à vista: em Nogueira Caiena de 6 mm, não em Branco'),
 P('Frente · báscula · DET 04', I4, 83, 63, 4, PT18, (2, 2),
   'Quatro de 83 × 63 · ⭐ a ÚNICA peça Preto Ultra Premium do ambiente · '
   'fecho toque'),
]

# ── ferragem, declarada item a item ─────────────────────────────────────
GAVETAS = []
PORTAS  = [(I1, 'Quatro portas de giro de 59', 4, 2, DOBRADICA)]
BASCULAS= [(I4, 'Quatro básculas de 83 × 63 · fecho toque', 4)]
#  ⭐ a cava corre a largura inteira das quatro frentes: 4 × 59 = 236 cm
CAVA    = [(I1, 'As quatro portas do armário', 4, 59)]
PUXADORES= []
MOLDURA = []
LED     = [(I1, 'Iluminação inferior, de ponta a ponta', 2.37),
           (I4, 'Nichos iluminados · duas fileiras de 3,35', 6.70)]
CABIDEIROS = []
# ⭐ o tampo de 7 cm é caixão: sem travamento interno ele empena e afunda
SARRAFOS= []   # ⛔ pinus PROIBIDO: o quadro do tampo virou engradado de MDF
# ⭐ nada do home office toca o chão — o armário é suspenso com recuo de
#   LED, a mesa é suspensa, o painel é de parede e o superior é alto —
#   então não há perfil de proteção de piso neste ambiente.
# ⭐ SUPORTE DE PRATELEIRA: não se declara mais. Toda prateleira interna
#   leva um jogo de 4 suportes, R$ 6,50 [Jonathan, 28/10/2026], e a
#   conta sai de B.prateleiras(), das peças. Quem não leva diz
#   'sem suporte' na obs.
SUPORTES= []
ALMAS   = []
VIDRO   = []
SERRALHERIA = []
OUTRAS  = []

CABECA = {
 I: ('335 de frente · armário 237 × 68 × 40 · mesa 335 × 60 × 7 · painel '
     '350 × 169 · superior 335 × 131 × 40',
     'DET 01 armário 237 × 68 × 40, quatro portas de 59 e o recuo de 30 + 10 '
     'embaixo onde corre o LED · DET 02 mesa 335 × 60 × 7, com as duas '
     'torres de tomada a 80 e a 50 das pontas ⚠ MDF não existe em 70 mm: '
     'orçada como CAIXÃO, duas faces e borda, com ENGRADADO DE MDF por '
     'dentro — o sarrafo de pinus saiu · DET 03 painel 350 × 169 × 3, em '
     'duas peças de 175 · DET 04 superior 335 × 131 × 40, báscula em cima e '
     'nicho aberto e iluminado embaixo · ⭐ item único [Jonathan, 28/10]'),
}

FOLHA = dict(
 aba='HOME OFFICE',
 sub='Jéssica e Michell · Projeto ICA · páginas 094 a 103 · quatro itens e '
     '⭐ TRÊS cores aparentes, a primeira vez no projeto: Lacca Fume no '
     'armário e no tampo da mesa, Nogueira Caiena no painel e no corpo do '
     'superior, Preto Ultra Premium só nas quatro básculas · caixaria em '
     f'Branco TX 15 · peça inteira até {ALT_MAX:g}, que é a chapa de '
     f'{CHAPA_C:g} menos o acerto de corte',
 chapa_txt={LF18: 'Lacca Fume · Eucatex · o armário inteiro e o tampo da mesa',
            NC18: 'Nogueira Caiena · Duratex · o painel e o que se vê do superior',
            NC6:  'Nogueira Caiena · fundo dos nichos abertos, que fica à vista',
            PT18: 'Preto Ultra Premium · só as quatro básculas do DET 04',
            EST:  'Estrutura e caixaria · o padrão da Base para caixaria',
            PRAT18:'Prateleiras de vão acima de 70 cm · 18 mm contra empeno',
            FUN:  'Fundos · encaixe em rasgo, sem fita'},
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem [Jonathan, 29/10]: '
      'a QUANTIDADE é a célula AMARELA no fim do painel de material, e ela '
      'sai ZERO. Digite quantas viagens este ambiente leva e o frete '
      'aparece aqui e no Painel.   '
      '⚠⚠ A MESA NÃO TEM APOIO DESENHADO. É um tampo de 335 × 60 com 7 de '
      'espessura, e a prancha não mostra pé, cavalete nem lateral. Orcei o '
      'tampo como CAIXÃO, que é o que 7 cm de MDF obriga, e o APOIO não '
      'está nesta conta.   ⭐ TRÊS CORES APARENTES: são três arredondamentos '
      'de chapa, não um — e "Lacca Fume" não está nomeado na Base, entrou '
      'como melamínico fosco.',
 duvidas=[
  'A MESA NÃO TEM APOIO DESENHADO: 335 × 60 de tampo com 7 de espessura e '
  'nenhum pé, cavalete ou lateral na prancha. ⛔ Um tampo de 3,35 m sem apoio '
  'no meio não para em pé. ⚠ O que vai aí: mão-francesa metálica, estrutura '
  'de serralheria, dois pés ou uma lateral de marcenaria? Não está nesta '
  'conta, e muda o item inteiro.',
  'O TAMPO DA MESA TEM 7 CM e MDF não existe em 70 mm. Orcei como CAIXÃO — '
  'face de cima em Lacca Fume, face de baixo em Branco TX, borda de 7 em '
  'Lacca Fume e ENGRADADO DE MDF por dentro. ⚠ Se a face de baixo tiver de '
  'sair em Lacca Fume, são mais 2 m² da chapa cara. É a mesma questão das '
  'colunas do Living e da prateleira do Quarto, agora em 7 cm.',
  'O PAINEL DO DET 03 TEM 350 DE LARGURA e a chapa dá 275. Dividi em duas '
  'peças de 175, com a emenda no meio. ⚠ Num painel liso de 1,69 m de altura, '
  'a emenda no centro aparece — e é exatamente atrás da mesa, no campo de '
  'visão de quem entra. Confirmar se pode, ou se a emenda vai para um terço.',
  'O PAINEL DO DET 03 também está desenhado com 3 cm de espessura. ⚠ Orçado '
  'em 18 mm simples, como as colunas do Living e a prateleira do Quarto. A '
  'alternativa é colar duas chapas, e aí dobra a chapa dessa peça e entra '
  'laminação de topo.',
  'O "MDF LACCA FUME - EUCATEX" não está nomeado na Base. Lancei como '
  'melamínico fosco, R$ 700 a chapa de 18. ⚠ Lacca é linha de ALTO BRILHO em '
  'vários fabricantes, e brilho na Base é Cristallo, R$ 800. Se for brilho, '
  'são R$ 100 por chapa a mais em quatro chapas.',
  'O DET 04 TEM A FILEIRA DE BAIXO EM NICHO ABERTO, e isso muda a cor do que '
  'está dentro: pus laterais, divisórias, base, prateleira e fundo dos nichos '
  'em Nogueira Caiena, porque se vê tudo. ⚠ A fileira de cima fecha com '
  'báscula e voltei para Branco TX, que é a regra da casa. Confirmar se o '
  'desenho quer o interior fechado também na cor.',
  'A BÁSCULA DO DET 04 É PRETO ULTRA PREMIUM e o resto do móvel é Nogueira '
  'Caiena. ⚠ São 2,1 m² de Preto, que puxam uma chapa inteira de R$ 700 para '
  'quatro portas. Se o Preto puder vir de sobra de outro ambiente — a Área '
  'Gourmet usa a mesma chapa — o custo cai. ⛔ Como ambiente isolado, não há '
  'como não comprar a chapa.',
  'A ILUMINAÇÃO: são 2,37 m no DET 01 e 6,70 m no DET 04, duas fileiras de '
  '3,35. ⚠ Nove metros de LED num ambiente de 4 itens é muito, e a prancha '
  'escreve "Led" em quatro pontos diferentes. Confirmar se as duas fileiras '
  'do superior são mesmo iluminadas, ou se só a de baixo.',
  '⛔ A BASE METÁLICA DE 3 CM aparece aqui como em todo o projeto e continua '
  'NÃO LANÇADA em nenhum ambiente — sete ambientes agora.'],
 nao_marcenaria=[
  'Apoio da mesa do DET 02 — não desenhado na prancha: pé, mão-francesa ou estrutura',
  'Duas torres de tomada embutidas no tampo da mesa',
  'Cadeiras ergonômicas, persiana horizontal e quadros decorativos',
  'Pintura das paredes em tinta Decora Efeitos Especiais Velvet Recado de Amor - Coral'],
 notas=[
  '⭐⭐ TRÊS CORES APARENTES NO MESMO AMBIENTE, e é a primeira vez no projeto. '
  'Lacca Fume no DET 01 e no tampo da mesa, Nogueira Caiena no painel e no '
  'corpo do superior, Preto Ultra Premium SÓ nas quatro básculas do DET 04. '
  'São três arredondamentos de chapa, não um: cada cor é uma compra separada '
  'e puxa no mínimo uma chapa cheia.',
  '⭐⭐ DUAS PEÇAS PASSAM DOS 275 E NENHUMA DELAS É ALTURA — são CORRIDAS. O '
  'painel do DET 03 tem 350 de largura e o tampo da mesa tem 335. Até aqui o '
  'problema do projeto era peça ALTA; neste ambiente é peça LONGA, e a '
  'emenda cai onde se olha.',
  '⚠⚠ A MESA É SÓ UM TAMPO. A prancha desenha 335 × 60 × 7 e mais nada: sem '
  'pé, sem cavalete, sem lateral. Orcei o tampo como caixão e deixei o apoio '
  'fora, na caixa de dúvidas. É o item mais incompleto do projeto até agora.',
  '⭐ O INTERIOR DO DET 04 MUDA DE COR NO MEIO DO MÓVEL: a fileira de baixo é '
  'nicho ABERTO e iluminado, então laterais, divisórias, base, prateleira e '
  'fundo saem em Nogueira Caiena; a de cima fecha com báscula e volta para '
  'Branco TX, que é a regra da casa.',
  '⭐ NENHUMA DOBRADIÇA NO DET 04 E NENHUMA BÁSCULA NO DET 01. O armário de '
  'baixo abre por porta de giro com cava; o de cima, por báscula com fecho '
  'toque. São 8 dobradiças, 4 articuladores e 2,36 m de cava.'],
)
