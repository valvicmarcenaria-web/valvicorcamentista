# -*- coding: utf-8 -*-
"""ICA · CLOSET 03 — levantamento peça por peça  [28/10/2026]

páginas 222 a 229 · dois detalhamentos, dois itens, três folhas de detalhe.

⭐ UMA COR SÓ, do rodapé ao teto: MDF BRANCO DIAMANTE — Duratex. É o mesmo
  padrão do Closet Master e do Closet Mariana, e é a TERCEIRA vez que ele
  manda num ambiente inteiro deste projeto. ⛔ Por isso a dúvida de sempre
  — branco texturado (R$ 400/350/250) ou linha de cor (R$ 700/550/350) —
  vale mais aqui do que em qualquer lugar: ela move três closets de uma
  vez, e neste sozinho são dezesseis chapas.

⭐⭐ OS DOIS ARMÁRIOS SÃO ABERTOS, SEM UMA ÚNICA PORTA. Tudo o que fecha
  são gavetas e gavetões, e todos com PUXADOR CAVA — a prancha escreve
  "puxador cava" nos dois detalhamentos, com todas as letras. ⛔ É o
  oposto da Suíte 03 ao lado, onde não há puxador desenhado em lugar
  nenhum e a resposta foi o pulsador. Aqui não há o que supor.

⛔⛔ O PÉ-DIREITO DE 300 MORDE SEIS VEZES neste ambiente só: as duas
  laterais do Armário 01 e as duas laterais mais as duas divisórias do
  Armário 02. São peças de 60 de profundidade — a emenda apareceria no
  meio do vão, e por isso elas vão para a lista de peças ALTAS em vez de
  eu emendá-las por conta própria.

⛔ E O ARMÁRIO 02 TEM 325 DE EXTENSÃO, que é mais do que a chapa dá em
  qualquer orientação: o fechamento superior, a base e o rodapé saem
  todos em duas peças. É o mesmo caso do Armário 02 do Closet Mariana,
  que tinha 304.

⚠ O CALCEIRO DESLIZANTE do vão de 70 continua SEM PREÇO na Base — é o
  segundo do projeto, depois do Closet Master.
"""
from base import P, gaveta, ALT_MAX, CHAPA_C

BD18, BD15, BD6 = ('MDF Branco Diamante 18', 'MDF Branco Diamante 15',
                   'MDF Branco Diamante 6')

I1 = 'DET 01 Armário 01'
I2 = 'DET 02 Armário 02'

CLOSET03 = [
 # ══ ITEM 01 · ARMÁRIO 01 — 170 × 60 × 300 ═══════════════════════════
 #  DET. 01 VISTA FRONTAL  170 = 167 + 3 · as duas colunas são 95 + 3 + 69
 #     e embaixo viram 30 (sapateira) + 65 (gaveta) + 72 (gavetão) + 3
 #     altura 3,5 + 60 maleiro + 3 + 25 nicho + 3 + 110 cabideiro + 3 +
 #     18 + 3 + 17 + 3 + 17 + 3 + 19 + 5 ≈ 300
 #  DET. 01 VISTA SUPERIOR e LATERAL  170 × 60 · 60 de profundidade
 P('Lateral',               I1, 300, 60, 2, BD15, (1, 0),
   '⛔ 300 de pé-direito · só a aresta da frente aparece, e são 3 m'),
 P('Fechamento superior',   I1, 167, 60, 1, BD15, (1, 0),
   'O painel que fecha o armário contra a laje · a VISTA FRONTAL o cota '
   'com 3,5 de faixa aparente'),
 P('Fechamento superior · testeira', I1, 170, 5, 1, BD15, (2, 2),
   'A faixa de 3,5 que se vê de frente · ⛔ régua, filetagem manual'),
 P('Base',                  I1, 167, 60, 1, BD15, (1, 0), 'Aparente de baixo'),
 P('Rodapé',                I1, 167, 5, 1, BD15, (1, 0),
   'Os 5 do pé da VISTA FRONTAL'),
 P('Prateleira do maleiro', I1, 167, 60, 1, BD18, (1, 0),
   '⭐ 18 mm: é a única horizontal que atravessa os 167 inteiros, e é '
   'nela que o maleiro de 60 apoia'),
 P('Divisória vertical',    I1, 60, 228, 1, BD15, (1, 0),
   'A vertical que parte o armário em 95 e 69, do maleiro ao rodapé'),
 P('Prateleira · coluna do cabideiro', I1, 95, 60, 2, BD18, (1, 0),
   'A do nicho de 25 e a que fecha o cabideiro de 110 por baixo · ⭐ 18 '
   'mm, o vão de 95 passa dos 70 da regra'),
 P('Prateleira · coluna direita', I1, 69, 60, 4, BD15, (1, 0),
   '⭐ 15 mm: o vão de 69 fica abaixo dos 70 da regra · quatro nichos '
   'empilhados de 25, 35, 34 e 35'),
 P('Divisória da sapateira', I1, 60, 80, 1, BD15, (1, 0),
   'A vertical baixa que separa os 30 da sapateira dos 65 das gavetas · ⛔ é DIVISÓRIA, não sapateira: sem suporte'),
 P('Sapateira',             I1, 30, 60, 4, BD15, (1, 0),
   'Quatro prateleiras na coluna estreita de 30'),
 P('Frente da gaveta',      I1, 65, 18, 4, BD15, (2, 2),
   '⭐ a prancha escreve "puxador cava" com todas as letras · as quatro '
   'têm 18, 17, 17 e 19 na VISTA FRONTAL; lancei as quatro em 18, que é '
   'a média e é o que a chapa vê'),
 P('Frente do gavetão',     I1, 72, 40, 2, BD15, (2, 2),
   'Os dois gavetões da coluna direita, também com puxador cava'),
 *gaveta(I1, 65, 55, 14, 4, 'Caixa de gaveta', BD15, BD6),
 *gaveta(I1, 69, 55, 35, 2, 'Caixa do gavetão', BD15, BD6),
 P('Fundo',                 I1, 150, 170, 2, BD6, (0, 0),
   '⛔ 170 × 300 não sai de chapa nenhuma: duas faixas de 150, emenda '
   'atrás de prateleira · encaixe em rasgo'),

 # ══ ITEM 02 · ARMÁRIO 02 — 325 × 60 × 300 ═══════════════════════════
 #  DET. 02 VISTA FRONTAL  325 = 3 + 100 + 2 + 87 + 3 + 130, e embaixo
 #     3 + 100 + 2 + 87 + 3 + 70 (calceiro) + 2 + 58 (sapateira)
 #     altura 3,5 + 60 maleiro + 3 + 25 nicho + 3 + 193 + 5 ≈ 300
 #  DET. 02 VISTA SUPERIOR  325 × 60 · VISTA LATERAL 60 × 300
 P('Lateral',               I2, 300, 60, 2, BD15, (1, 0),
   '⛔ 300 de pé-direito'),
 P('Divisória vertical',    I2, 300, 60, 2, BD15, (1, 0),
   'As duas que partem os 325 em 100, 87 e 130 · ⛔ 300, e elas vão do '
   'fechamento superior ao rodapé'),
 P('Fechamento superior',   I2, 163, 60, 2, BD15, (1, 0),
   '⛔ 325 de extensão não sai de chapa nenhuma, em orientação nenhuma: '
   'duas peças de 163, com a emenda sobre uma divisória'),
 P('Fechamento superior · testeira', I2, 163, 5, 2, BD15, (2, 2),
   'A faixa de 3,5 aparente · ⛔ régua, filetagem manual'),
 P('Base',                  I2, 160, 60, 2, BD15, (1, 0),
   'Também em duas peças, pelo mesmo motivo'),
 P('Rodapé',                I2, 160, 5, 2, BD15, (1, 0), 'Os 5 do pé'),
 P('Prateleira do maleiro · vão de 100', I2, 100, 60, 1, BD18, (1, 0),
   '⭐ 18 mm em todas as três: os vãos de 100, 87 e 130 passam dos 70'),
 P('Prateleira do maleiro · vão de 87',  I2, 87, 60, 1, BD18, (1, 0), '—'),
 P('Prateleira do maleiro · vão de 130', I2, 130, 60, 1, BD18, (1, 0), '—'),
 P('Prateleira do nicho · vão de 100', I2, 100, 60, 1, BD18, (1, 0),
   'A do nicho de 25, logo abaixo do maleiro'),
 P('Prateleira do nicho · vão de 87',  I2, 87, 60, 1, BD18, (1, 0), '—'),
 P('Prateleira do nicho · vão de 130', I2, 130, 60, 1, BD18, (1, 0), '—'),
 P('Divisória dos nichos pareados', I2, 60, 100, 1, BD15, (1, 0),
   'Só o vão de 87 é partido ao meio na parte baixa — são seis nichos '
   'pequenos de 42, em três fileiras'),
 P('Prateleira do nicho pareado', I2, 42, 60, 4, BD15, (1, 0),
   '⭐ 15 mm: o vão de 42 é curto · duas por coluna, que fazem as três '
   'fileiras de nicho'),
 P('Prateleira cheia do vão de 87', I2, 87, 60, 2, BD18, (1, 0),
   'A que fecha os nichos pareados por baixo e a que fecha o nicho '
   'corrido sobre as quatro gavetas'),
 P('Frente da gaveta',      I2, 87, 18, 4, BD15, (2, 2),
   '⭐ "puxador cava", escrito na prancha · quatro gavetas no vão de 87'),
 *gaveta(I2, 87, 55, 14, 4, 'Caixa de gaveta', BD15, BD6),
 P('Prateleira sob o cabideiro · vão de 130', I2, 130, 60, 1, BD18, (1, 0),
   'É ela que fecha o cabideiro longo e faz o teto do bloco do calceiro '
   'e da sapateira'),
 P('Divisória do calceiro', I2, 60, 79, 1, BD15, (1, 0),
   'A vertical baixa que separa os 70 do calceiro deslizante dos 58 da '
   'sapateira'),
 P('Sapateira',             I2, 58, 60, 4, BD15, (1, 0),
   'Quatro prateleiras na coluna de 58, ao lado do calceiro'),
 P('Fundo',                 I2, 163, 150, 4, BD6, (0, 0),
   '⛔ 325 × 300 é o maior fundo do projeto inteiro: quatro faixas de '
   '163 × 150 · encaixe em rasgo'),
]

# ── ferragem, declarada item a item ─────────────────────────────────────
GAVETAS = [(I1, 'Quatro gavetas de 65 e dois gavetões de 72', 6, 550),
           (I2, 'Quatro gavetas do vão de 87',                4, 550)]
PORTAS  = []          # ⭐ nenhuma: os dois armários são ABERTOS
BASCULAS= []
# ⭐ a prancha escreve "puxador cava" nos dois DET, com todas as letras
CAVA    = [(I1, 'Quatro gavetas de 65',  4, 65),
           (I1, 'Dois gavetões de 72',   2, 72),
           (I2, 'Quatro gavetas de 87',  4, 87)]
PUXADORES = []
MOLDURA = []
LED     = []          # ⚠ nenhum ponto de luz desenhado neste closet
CABIDEIROS = [(I1, 'Cabideiro da coluna de 95',                   1),
              (I2, 'Cabideiro do vão de 100 e do vão de 130',     2)]
SARRAFOS= []
SUPORTES= []
ALMAS   = []
VIDRO   = []
SERRALHERIA = []
OUTRAS  = [
           (I1, 'Perfil de proteção de piso', 'Armário 01 de 170', 1.7, 'm',
            'Perfil de proteção de piso'),
           (I2, 'Perfil de proteção de piso', 'Armário 02 de 325', 3.25, 'm',
            'Perfil de proteção de piso'),
           (I2, 'Calceiro deslizante', 'O vão de 70 da VISTA FRONTAL · '
            '⛔ SEM PREÇO na Base · é o segundo do projeto, depois do '
            'Closet Master', 1, 'un', 'Calceiro deslizante')]

CABECA = {
 I1: ('170 × 60 × 300',
      'DET. 01 VISTA FRONTAL 170 = 167 + 3 · as colunas são 95 + 3 + 69 e '
      'embaixo viram 30 de sapateira + 65 de gaveta + 72 de gavetão + 3 · '
      'altura 3,5 + 60 de maleiro + 3 + 25 de nicho + 3 + 110 de cabideiro '
      '+ 18 + 17 + 17 + 19 de gaveta + 5 ≈ 300 · VISTA SUPERIOR e LATERAL '
      '60 de profundidade · ⭐ armário ABERTO, sem uma única porta'),
 I2: ('325 × 60 × 300',
      'DET. 02 VISTA FRONTAL 325 = 3 + 100 + 2 + 87 + 3 + 130, e embaixo '
      '3 + 100 + 2 + 87 + 3 + 70 de calceiro + 2 + 58 de sapateira · '
      'altura 3,5 + 60 de maleiro + 3 + 25 de nicho + 3 + 193 + 5 ≈ 300 · '
      'VISTA SUPERIOR 325 × 60 · ⛔ 325 não sai de chapa nenhuma: '
      'fechamento superior, base e rodapé em duas peças'),
}

FOLHA = dict(
 aba='CLOSET 03',
 sub='Jéssica e Michell · Projeto ICA · páginas 222 a 229 · dois itens em '
     'três folhas de detalhe · ⭐ uma cor só, MDF Branco Diamante Duratex, '
     'do rodapé ao teto · ⭐ os dois armários são ABERTOS, sem uma única '
     'porta: tudo que fecha é gaveta, e toda gaveta tem PUXADOR CAVA, '
     f'escrito na prancha · peça inteira até {ALT_MAX:g}, que é a chapa de '
     f'{CHAPA_C:g} menos o acerto de corte',
 chapa_txt={BD15: 'Branco Diamante · Duratex · caixaria, laterais, '
                  'divisórias, sapateiras e todas as frentes de gaveta',
            BD18: 'Branco Diamante 18 mm · toda prateleira de vão acima de '
                  '70 cm — maleiros, nichos largos e a sob o cabideiro',
            BD6:  'Branco Diamante 6 mm · fundos, encaixe em rasgo'},
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem [Jonathan, 29/10]: '
      'a QUANTIDADE é a célula AMARELA no fim do painel de material, e ela '
      'sai ZERO. Digite quantas viagens este ambiente leva e o frete '
      'aparece aqui e no Painel.   '
      '⛔⛔ A DÚVIDA DO BRANCO DIAMANTE VALE MAIS AQUI DO QUE EM QUALQUER '
      'LUGAR. Lancei no preço de COR, R$ 700 / 550 / 350 a chapa, que é '
      'como a Base o traz e é o lado conservador. ⚠ Mas Branco Diamante é '
      'um branco texturado, irmão do Branco TX: se a Duratex cobrar como '
      'branco — R$ 400 / 350 / 250 —, este ambiente, que é de uma cor só, '
      'CAI quase 40%. ⭐ E ela não move só este closet: move o Closet '
      'Master e o Closet Mariana também, que são do mesmo padrão. É a '
      'pergunta mais cara do projeto.   '
      '⭐⭐ NENHUMA PORTA, NENHUM PULSADOR. Os dois armários são abertos, e '
      'tudo que fecha é gaveta ou gavetão com PUXADOR CAVA — a prancha '
      'escreve a palavra nos dois detalhamentos. É o oposto da Suíte 03 ao '
      'lado, onde não há puxador desenhado em lugar nenhum.   '
      '⛔⛔ O PÉ-DIREITO DE 300 MORDE SEIS VEZES: as duas laterais do '
      'Armário 01 e as duas laterais mais as duas divisórias do Armário 02. '
      'São peças de 60 de profundidade, em que a emenda apareceria no meio '
      'do vão — por isso elas estão na lista de peças ALTAS, para o senhor '
      'decidir, e não emendadas por mim.',
 duvidas=[
  '⛔⛔ BRANCO DIAMANTE É BRANCO OU É COR? Lancei no preço de COR — R$ 700 '
  'o 18, R$ 550 o 15, R$ 350 o 6 —, que é como a Base o traz e é o lado '
  'conservador, exatamente como no Closet Master e no Closet Mariana. '
  '⚠ Mas Branco Diamante é um branco TEXTURADO, irmão do Branco TX da '
  'caixaria: se a Duratex cobrar como branco — R$ 400 / 350 / 250 —, este '
  'ambiente, que é de uma cor só do rodapé ao teto, CAI quase 40%. ⛔ E a '
  'resposta não move só este closet: o Closet Master e o Closet Mariana '
  'são do mesmo padrão e caem junto. É a pergunta mais cara do projeto '
  'inteiro, e é a terceira vez que eu a faço — uma resposta fecha as três.',
  'AS SEIS PEÇAS DE 300 DE ALTURA — quatro laterais e duas divisórias — '
  'NÃO SAEM INTEIRAS DA CHAPA, que dá 273. ⚠ Não as emendei por conta '
  'própria porque são painéis de 60 de profundidade: a emenda cairia no '
  'meio do vão aberto, bem à vista, e não tem prateleira que a esconda. '
  '⛔ As três saídas são: emenda assumida com testeira, chapa especial de '
  '3 m sob encomenda, ou rebaixar os armários para 273 e fechar o resto '
  'com um painel de gesso. Decisão de projeto, não de corte.',
  'O ARMÁRIO 02 TEM 325 DE EXTENSÃO e isso passa dos 275 da chapa em '
  'qualquer orientação. ⚠ O fechamento superior, a base e o rodapé saem '
  'em duas peças cada, com a emenda sobre uma das divisórias — é o mesmo '
  'que fiz no Armário 02 do Closet Mariana, que tinha 304. ⛔ Vale '
  'confirmar com o montador se ele prefere a emenda sobre a divisória de '
  '103 ou sobre a de 192.',
  'A ALTURA DAS QUATRO GAVETAS DO ARMÁRIO 01 VARIA — 18, 17, 17 e 19 na '
  'VISTA FRONTAL. ⚠ Lancei as quatro em 18, que é a média e é o que a '
  'chapa enxerga. ⛔ Para a bancada isso importa: são quatro frentes de '
  'medidas diferentes, não quatro iguais. A fábrica tem de cortar pela '
  'prancha, não por esta linha.',
  '⚠ O CALCEIRO DESLIZANTE DO VÃO DE 70 CONTINUA SEM PREÇO NA BASE. É o '
  'segundo do projeto, depois do Closet Master. Lancei a zero para '
  'aparecer na conta sem mentir. ⛔ Enquanto não tiver preço, o Armário '
  '02 é um PISO.',
  'NÃO HÁ UM ÚNICO PONTO DE LUZ DESENHADO NESTE CLOSET, e isso é raro no '
  'projeto: o Closet Master tem LED em prateleira, o Closet Mariana '
  'também. ⚠ Aqui a prancha não desenha nenhum, e não lancei nenhum. Se '
  'a intenção era iluminar o maleiro e os nichos como nos outros dois, '
  'são uns 6 m de fita, R$ 900.',
  'OS DOIS ARMÁRIOS SÃO ABERTOS, SEM PORTA NENHUMA. ⚠ Li exatamente o '
  'que a prancha desenha. ⛔ Mas vale a pergunta: em closet de criança, '
  'armário aberto é decisão de projeto ou faltou desenhar a porta? Se '
  'entrarem portas, são uns 10 m² de frente, mais umas três chapas e as '
  'dobradiças — perto de R$ 3.000.',
  'A PROFUNDIDADE É 60 NOS DOIS ARMÁRIOS e o cabideiro vai embutido. ⚠ '
  'Com 60 de caixa e cabideiro no sentido da largura, a roupa cabe '
  'folgada — está certo. ⛔ Só confirmar que o cabideiro é barra '
  'transversal, e não cabideiro extensível, que é outra ferragem e outro '
  'preço.',
  '⛔ A BASE METÁLICA DE 3 CM: aqui os dois armários tocam o chão em toda '
  'a extensão, 495 cm de rodapé somados. ⚠ Fica para a passada única, '
  'junto com os outros ambientes.'],
 nao_marcenaria=[
  'Paredes emassadas e pintadas com tinta toque de seda na cor Algodão '
  'Egípcio - Suvinil, das elevações 01 e 02',
  '⚠ A iluminação do ambiente — a prancha não desenha ponto nenhum'],
 notas=[
  '⭐⭐ É O TERCEIRO CLOSET DO MESMO PADRÃO. Closet Master, Closet Mariana '
  'e Closet 03 são os três inteiros em MDF Branco Diamante da Duratex, e '
  'os três dependem da mesma resposta: branco texturado ou linha de cor. '
  'Juntos são mais de cinquenta chapas, e a diferença entre as duas '
  'leituras passa de R$ 10.000. É a pergunta mais cara do projeto.',
  '⭐ AQUI NÃO HOUVE NADA A SUPOR SOBRE PUXADOR, e isso é raro neste '
  'executivo. A prancha escreve "puxador cava" nos dois detalhamentos, '
  'com todas as letras, e os dois armários são abertos — não há porta, '
  'não há báscula, não há pulsador. São dez frentes de gaveta e 5,0 m de '
  'cava usinada.',
  '⛔⛔ SEIS PEÇAS DE 300 E UM ARMÁRIO DE 325. O pé-direito morde as '
  'quatro laterais e as duas divisórias; a extensão morde o fechamento '
  'superior, a base e o rodapé do Armário 02. ⭐ A diferença é que a '
  'extensão eu resolvi — duas peças com a emenda sobre a divisória, que '
  'some — e a altura não: em painel de 60 de profundidade a emenda fica '
  'no meio do vão aberto, e isso é decisão do senhor.',
  '⚠ ZERO PONTOS DE LUZ. Os outros dois closets do projeto têm LED em '
  'prateleira; este não desenha nenhum. Não inventei — mas deixei a '
  'conta na dúvida 06, porque seis metros de fita são R$ 900 e é o tipo '
  'de coisa que aparece na obra.'],
)
