# -*- coding: utf-8 -*-
"""ICA · LAVANDERIA — levantamento peça por peça  [28/10/2026]

páginas 043 a 059 · seis detalhamentos, seis itens.

⭐⭐⭐ O AMBIENTE INTEIRO É PROVENÇAL: 31 frentes, nenhuma lisa. Com o
  método novo — peça inteira de 6 mm usinada na router, não régua —
  cada frente consome a MESMA ÁREA DUAS VEZES, uma em 15 e outra em 6.
  É isso, e não a caixaria, que decide o preço daqui.

⭐⭐ DOIS PADRÕES DE COR, E ELES NÃO SE DIVIDEM POR MÓVEL, SE DIVIDEM POR
  PEÇA. No DET 04 o corpo e o fechamento são Carvalho Malva e as FRENTES
  são Off White Suave — a prancha diz isso em letra, vista por vista.
      armários, bancadas e fechamentos ... Carvalho Malva Premium · Duratex
      superiores, nichos e as frentes do DET 04 ... Off White Suave · Duratex
      caixaria e interno ................. Branco TX  [regra do Jonathan]

⭐ A PROFUNDIDADE ESTÁ COTEADA, ao contrário do que eu havia anotado na
  primeira leitura: 67 no DET 01 (que é o que a lava e seca pede) e 60 nos
  outros cinco. Foi a leitura por VISTA que achou — no texto corrido da
  prancha esses números caíam longe do móvel a que pertencem.

⭐ NENHUMA PEÇA PRECISA SER DOBRADA. A maior é a porta de 210 do DET 04 e
  o fundo de 265 do mesmo móvel: ambos cabem na chapa de 275 × 185. Era a
  pergunta do Jonathan e aqui a resposta é não.

⛔ O SÓCULO É DE GRANITO nos seis detalhamentos, e não é marcenaria. Não
  confundir com a "base metálica de 3 cm" que aparece na mesma folha e que
  a casa resolve em MDF melamínico: aqui a prancha pede pedra, e os 10 cm
  de sóculo saem da nossa conta.
"""
from base import (P, gaveta, provencal, acabamento, ALT_MAX, CHAPA_C,
                  DOBRADICA, ALTAS)

# ── os padrões ──────────────────────────────────────────────────────────
CM15, CM6 = 'MDF Carvalho Malva 15',  'MDF Carvalho Malva 6'
OW15, OW6 = 'MDF Off White Suave 15', 'MDF Off White Suave 6'
EST, FUN  = 'MDF Branco TX 15', 'MDF Branco TX 6'
PRAT18    = 'MDF Branco TX 18'   # ⭐ só onde o vão passa de 70 cm

# ⭐⭐ ITEM ÚNICO [Jonathan, 28/10/2026]: "A precificação da lavanderia pode
#   ser unificada." Os seis detalhamentos são UM móvel contínuo que dá a
#   volta na lavanderia — a fábrica produz junto, o montador monta junto e
#   o cliente vê um conjunto só. ⛔ O levantamento continua peça a peça e o
#   DET de origem continua no texto de cada linha: o que se unifica é o
#   PREÇO, não a leitura.
I = 'DET 01 a 06 Conjunto da lavanderia'
I1 = I2 = I3 = I4 = I5 = I6 = I

LAVANDERIA = [
 # ══ ITEM 01 · ARMÁRIO DA LAVA E SECA — 122 × 265 × 67 ════════════════
 #  VISTA FRONTAL  largura 60 + 62 = 122 · altura 5 + 65 + 185 + 10 = 265
 #  coluna de 62   5 + 32 + 32 + 2 + 27 + 2 + 27 + 2 + 85 + 10 + 30 + 10
 #  VISTA FRONTAL INTERNA, coluna de 60
 #                 5 +2+ 30 +2+ 30 +2+ 35 +2+ 34 +2+ 34 +2+ 34 +2+ 35 +2+ 10
 #  VISTA SUPERIOR e LATERAL  profundidade 67 ⭐ coteada
 P('Lateral · DET 01', I1, 255, 67, 2, EST, (1, 0), 'Sobre o sóculo de granito de 10, que não é nosso'),
 P('Divisória central · DET 01', I1, 255, 67, 1, EST, (1, 0), 'Separa a coluna de 60 da coluna de 62'),
 P('Base e topo · DET 01', I1, 119, 67, 2, EST, (1, 0)),
 # ⛔ PINUS PROIBIDO [Jonathan, 28/10/2026]: o reforço que segura a lava e
 #   seca cheia era sarrafo e agora é TRAVESSA DE MDF, tirada da própria
 #   chapa — mesma compra, sem fornecedor novo, e vira peça no plano de
 #   corte em vez de metro linear invisível.
 P('Engradado · travessa de MDF · DET 01', I1, 122, 8, 2, EST, (0, 0),
   'Duas travessas sob o tampo da lava e seca · ⛔ sem fita: é estrutura '
   'interna e não aparece · ⛔ substitui o sarrafo de pinus'),
 P('Fundo · DET 01', I1, 122, 255, 1, FUN, (0, 0), 'Encaixe em rasgo'),
 P('Fechamento superior · DET 01', I1, 122, 67, 1, CM15, (1, 1), '⭐ aparente, em Carvalho Malva · a prancha desenha 5 de testeira'),
 P('Prateleira interna · DET 01', I1, 57, 66, 6, EST, (1, 0), 'Coluna de 60 · sete vãos de 30·30·35·34·34·34·35, seis prateleiras'),
 P('Prateleira do nicho aberto · DET 01', I1, 59, 66, 3, CM15, (1, 1), '⭐ os dois vãos de 27 ficam à vista: prateleira em Carvalho Malva'),
 P('Divisória do módulo basculante · DET 01', I1, 59, 66, 1, EST, (1, 0), 'Separa as duas frentes basculantes de 32'),
 P('Apoio da lava e seca · DET 01', I1, 59, 66, 1, PRAT18, (1, 0), '⭐ "prever reforço para suportar lava e seca cheia": 18 mm mais sarrafo'),
 *provencal('Frente · porta de giro alta · DET 01', I1, 30,  65, 2, CM15, CM6, 'Provençal · duas folhas de 30 sobre a coluna de 60'),
 *provencal('Frente · porta de giro baixa · DET 01', I1, 30, 185, 2, CM15, CM6, 'Provençal · duas folhas de 30 · 185 de altura cabe inteira na chapa'),
 *provencal('Frente · báscula · DET 01', I1, 62,  32, 2, CM15, CM6, 'Provençal · articulador HK-XS'),
 *provencal('Frente · gaveta baixa · DET 01', I1, 62,  10, 1, CM15, CM6, 'Provençal · ⭐ 10 de altura só é possível com a moldura usinada'),
 *provencal('Frente · gavetão · DET 01', I1, 62,  30, 1, CM15, CM6, 'Provençal'),
 *gaveta(I1, 62, 55, 10, 1, 'Gaveta baixa'),
 *gaveta(I1, 62, 55, 30, 1, 'Gavetão'),

 # ══ ITEM 02 · BANCADA COM ARMÁRIO — 200 × 95 × 60 ════════════════════
 #  VISTA FRONTAL 50 + 50 + 50 + 50 = 200 · altura 5 + 80 + 10 = 95
 #  VISTA FRONTAL INTERNA 97 + 2 + 97 = 196 · interno 37 + 2 + 37 = 76
 #  VISTA SUPERIOR profundidade 60 · as duas cubas ficam na metade esquerda
 P('Lateral e divisória · DET 02', I2, 80, 60, 3, EST, (1, 0), 'Dois vãos de 97'),
 P('Base · DET 02', I2, 196, 60, 1, EST, (1, 0)),
 P('Travessa de apoio da bancada · DET 02', I2, 196, 10, 2, EST, (1, 0), 'Frente e fundo · a pedra apoia nelas, não em tampo cheio'),
 P('Fundo · DET 02', I2, 200, 80, 1, FUN, (0, 0), 'Encaixe em rasgo'),
 P('Prateleira · DET 02', I2, 97, 58, 2, PRAT18, (1, 0), '⭐ vão de 97 passa dos 70: 18 mm contra empeno · ⚠ a do vão da cuba pode esbarrar no sifão'),
 *provencal('Frente · porta de giro · DET 02', I2, 50, 80, 4, CM15, CM6, 'Provençal · quatro folhas de 50'),

 # ══ ITEM 03 · ARMÁRIO SUPERIOR 01 — 256 × 170 × 60 ═══════════════════
 #  VISTA FRONTAL largura 75 + 75 + 56 + 50 = 256 ⭐
 #                bloco de 206 com 5 + 65 · coluna de 50 com 5+65+30+71 = 171
 #                o vão de 56 se divide em duas básculas de 33
 #  VISTA LATERAL 5 + 65 + 100 = 170 · profundidade 60
 P('Bloco · lateral e divisória · DET 03', I3, 65, 60, 3, EST, (1, 0), 'Três vãos: 75 · 75 · 56'),
 P('Bloco · base e topo · DET 03', I3, 206, 60, 2, EST, (1, 0)),
 P('Coluna · lateral · DET 03', I3, 170, 60, 2, EST, (1, 0), 'A coluna de 50 desce 170, abaixo do bloco'),
 P('Coluna · base e tampos do nicho · DET 03', I3, 47, 60, 3, OW15, (1, 1), '⭐ o nicho de 30 é aberto: vai na cor'),
 P('Fechamento superior · DET 03', I3, 256, 60, 1, OW15, (1, 1), 'Aparente, em Off White Suave'),
 P('Fundo do bloco · DET 03', I3, 206, 70, 1, FUN, (0, 0), 'Encaixe em rasgo'),
 P('Fundo da coluna · DET 03', I3, 50, 170, 1, FUN, (0, 0), 'Encaixe em rasgo'),
 P('Prateleira do vão de 75 · DET 03', I3, 72, 58, 2, PRAT18, (1, 0), '⭐ vão de 72 passa dos 70: 18 mm'),
 P('Divisória do vão de 56 · DET 03', I3, 53, 58, 1, EST, (1, 0), 'Separa as duas frentes basculantes de 33'),
 P('Prateleira da coluna · DET 03', I3, 47, 58, 2, EST, (1, 0)),
 *provencal('Frente · báscula de 75 · DET 03', I3, 75, 65, 2, OW15, OW6, 'Provençal · articulador HK-XS'),
 *provencal('Frente · báscula de 56 · DET 03', I3, 56, 33, 2, OW15, OW6, 'Provençal · duas empilhadas no vão de 56'),
 *provencal('Frente · porta da coluna · DET 03', I3, 50, 65, 1, OW15, OW6, 'De giro · provençal'),
 *provencal('Frente · porta baixa da coluna · DET 03', I3, 50, 71, 1, OW15, OW6, 'De giro · provençal · abaixo do nicho aberto'),

 # ══ ITEM 04 · ARMÁRIO 02 — 130 × 265 × 60 ════════════════════════════
 #  VISTA FRONTAL largura 80 + 50 = 130 · a de 80 se divide em 40 + 40
 #                coluna de 80  10 + 210 + 40 + 5 = 265
 #                coluna de 50  25 + 55 + 140 + 40 + 5 = 265 ⭐ o nicho do
 #                robô vai ao CHÃO: não tem sóculo embaixo dele
 #  VISTA FRONTAL INTERNA 2 + 77 + 2 + 47 + 2 = 130
 #                vão de 77   6 +38+2+ 40+2+39+2+40+2+39+2+40 +10 = 265
 #                            e por dentro se divide em 38 + 2 + 38
 #                vão de 47   6 +38+2+ 138 +2+ 55 +2+ 22 = 265
 #  ⭐⭐ O CORPO É CARVALHO MALVA E AS FRENTES SÃO OFF WHITE SUAVE
 P('Lateral e divisória central · DET 04', I4, 255, 60, 3, EST, (1, 0), 'Vãos de 77 e 47'),
 P('Divisória do vão de 77 · DET 04', I4, 206, 58, 1, EST, (1, 0), 'Separa a coluna de prateleiras do vão da tábua de passar'),
 P('Base · DET 04', I4, 126, 60, 1, EST, (1, 0)),
 P('Fechamento superior · DET 04', I4, 130, 60, 1, CM15, (1, 1), '⭐ aparente, em Carvalho Malva · a frente é que vai em Off White'),
 P('Fundo · DET 04', I4, 130, 265, 1, FUN, (0, 0), 'Encaixe em rasgo · 265 cabe na chapa de 275'),
 P('Prateleira do vão de 38 · DET 04', I4, 38, 58, 4, EST, (1, 0), 'Cinco vãos de 40·39·40·39·40, quatro prateleiras'),
 P('Prateleira do vão de 77 · DET 04', I4, 77, 58, 1, PRAT18, (1, 0), '⭐ vão de 77 passa dos 70: 18 mm · fecha o compartimento da báscula'),
 P('Prateleira da coluna de 47 · DET 04', I4, 47, 58, 3, EST, (1, 0), 'Fecha o vão das vassouras, o armário e o nicho do robô'),
 *provencal('Frente · báscula de 80 · DET 04', I4, 80,  40, 1, OW15, OW6, 'Provençal em Off White · articulador HK-XS'),
 *provencal('Frente · báscula de 50 · DET 04', I4, 50,  40, 1, OW15, OW6, 'Provençal em Off White · articulador HK-XS'),
 *provencal('Frente · porta alta · DET 04', I4, 40, 210, 2, OW15, OW6, 'De giro · provençal · ⭐ 210 de altura cabe inteira na chapa de 275'),
 *provencal('Frente · porta de 140 · DET 04', I4, 50, 140, 1, OW15, OW6, 'De giro · provençal · vão das vassouras e rodos'),
 *provencal('Frente · porta de 55 · DET 04', I4, 50,  55, 1, OW15, OW6, 'De giro · provençal'),

 # ══ ITEM 05 · BANCADA COM ARMÁRIO 02 — 230 × 100 × 60 ════════════════
 #  VISTA FRONTAL 58 + 58 + 58 + 58 = 232 ≈ 230 · altura 5 + 85 + 10 = 100
 #  VISTA FRONTAL INTERNA 112 + 2 + 112 = 226 · dois vãos de 40 + 40
 #  VISTA LATERAL e SUPERIOR profundidade 60
 P('Lateral e divisória · DET 05', I5, 85, 60, 3, EST, (1, 0), 'Dois vãos de 112'),
 P('Base · DET 05', I5, 226, 60, 1, EST, (1, 0)),
 P('Travessa de apoio da bancada · DET 05', I5, 226, 10, 2, EST, (1, 0), 'Frente e fundo · a pedra apoia nelas'),
 P('Fundo · DET 05', I5, 230, 85, 1, FUN, (0, 0), 'Encaixe em rasgo'),
 P('Prateleira · DET 05', I5, 112, 58, 2, PRAT18, (1, 0), '⭐ vão de 112 passa dos 70: 18 mm contra empeno'),
 *provencal('Frente · porta de giro · DET 05', I5, 58, 85, 4, CM15, CM6, 'Provençal · quatro folhas de 58'),

 # ══ ITEM 06 · ARMÁRIO SUPERIOR 02 — 230 × 165 × 60 ═══════════════════
 #  VISTA FRONTAL largura 86 + 86 + 58 = 230 ⭐
 #                bloco de 172 com 5 + 40 = 45 · LED e cabideiro embaixo
 #                coluna de 58  5 +40+2+ 28 +2+ 27 +2+ 27 +2+ 28 +2 = 165
 #  VISTA LATERAL 45 + 120 = 165 · profundidade 60
 P('Bloco · lateral e divisória · DET 06', I6, 45, 60, 3, EST, (1, 0), 'Dois vãos de 86'),
 P('Bloco · base e topo · DET 06', I6, 172, 60, 2, EST, (1, 0)),
 P('Coluna · lateral · DET 06', I6, 165, 60, 2, EST, (1, 0)),
 P('Coluna · base e topo · DET 06', I6, 58, 60, 2, OW15, (1, 1), '⭐ a coluna é toda de nicho aberto: vai na cor'),
 P('Prateleira do nicho · DET 06', I6, 55, 58, 3, OW15, (1, 1), 'Quatro nichos abertos de 28 · 27 · 27 · 28'),
 P('Fechamento superior · DET 06', I6, 230, 60, 1, OW15, (1, 1), 'Aparente, em Off White Suave'),
 P('Fundo do bloco · DET 06', I6, 172, 45, 1, FUN, (0, 0), 'Encaixe em rasgo'),
 P('Fundo da coluna · DET 06', I6, 58, 165, 1, FUN, (0, 0), 'Encaixe em rasgo'),
 *provencal('Frente · báscula de 86 · DET 06', I6, 86, 40, 2, OW15, OW6, 'Provençal · articulador HK-XS'),
 *provencal('Frente · báscula de 58 · DET 06', I6, 58, 40, 1, OW15, OW6, 'Provençal · topo da coluna de nichos'),
]

# ── ferragem, declarada item a item ─────────────────────────────────────
#  ⭐⭐ AQUI A BÁSCULA NÃO ABRE PELO SLIM. A prancha põe "puxador Alças
#    Traso" em TODA frente, básculas inclusive — e põe em letra, folha por
#    folha. Na Cozinha o Jonathan fechou slim nas básculas; aqui o desenho
#    pede o Traso, e são onze básculas. Declarado como o desenho manda, e
#    a diferença está na caixa de dúvidas.
GAVETAS = [(I1, 'Armário da lava e seca · gaveta de 10 e gavetão de 30', 2, 550)]
#  ⭐ a régua da casa, da Base: até 90 → 2 · 90 a 160 → 3 · 160 a 200 → 4
#    · acima de 200 → 5
PORTAS  = [(I1, 'Portas de giro de 65',                2, 2, DOBRADICA),
           (I1, 'Portas de giro de 185',               2, 4, DOBRADICA),
           (I2, 'Portas de giro de 80',                4, 2, DOBRADICA),
           (I3, 'Portas da coluna · 65 e 71',          2, 2, DOBRADICA),
           (I4, 'Portas altas de 210',                 2, 5, DOBRADICA),
           (I4, 'Porta de 140',                        1, 3, DOBRADICA),
           (I4, 'Porta de 55',                         1, 2, DOBRADICA),
           (I5, 'Portas de giro de 85',                4, 2, DOBRADICA)]
BASCULAS= [(I1, 'Duas básculas de 62 × 32',            2, 'traso'),
           (I3, 'Duas de 75 × 65 e duas de 56 × 33',   4, 'traso'),
           (I4, 'Báscula de 80 e báscula de 50',       2, 'traso'),
           (I6, 'Duas de 86 × 40 e uma de 58 × 40',    3, 'traso')]
CAVA     = []
PUXADORES= [(I1, 'As oito frentes do armário',         8),
            (I2, 'As quatro portas da bancada',        4),
            (I3, 'As seis frentes do superior',        6),
            (I4, 'As seis frentes do armário 02',      6),
            (I5, 'As quatro portas da bancada 02',     4),
            (I6, 'As três básculas do superior 02',    3)]
# ⛔ a usinagem da moldura não tem preço: sai zero e denuncia
MOLDURA  = [(I1, 'Frentes do armário da lava e seca',  8),
            (I2, 'Frentes da bancada',                 4),
            (I3, 'Frentes do superior 01',             6),
            (I4, 'Frentes do armário 02',              6),
            (I5, 'Frentes da bancada 02',              4),
            (I6, 'Frentes do superior 02',             3)]
LED     = [(I6, 'Sob o bloco de 172', 1.72)]
CABIDEIROS = [(I6, 'Sob o bloco de 172, junto do LED', 1)]
# ⭐ o reforço que a prancha pede embaixo da lava e seca cheia
SARRAFOS= []   # ⛔ pinus PROIBIDO: o reforço virou engradado de MDF
# ⭐ SUPORTE DE PRATELEIRA: não se declara mais. Toda prateleira interna
#   leva um jogo de 4 suportes, R$ 6,50 [Jonathan, 28/10/2026], e a conta
#   sai de B.prateleiras(), das peças.
SUPORTES= []
ALMAS   = []
VIDRO   = []
SERRALHERIA = []
# ⭐ PERFIL DE PROTEÇÃO DE PISO [Jonathan, 28/10/2026]: todo painel que toca
#   o chão leva perfil de alumínio/inox, R$ 15 o metro linear. Tocam o chão
#   o armário da lava e seca (122), as duas bancadas (200 e 230) e o
#   armário 02 (130), cujo nicho do robô vai ao piso sem sóculo.
OUTRAS  = [(I, 'Perfil de proteção de piso', 'Armário da lava e seca 122 + '
            'bancada 200 + armário 02 130 + bancada 02 230 = 682 cm de '
            'painel tocando o chão', 6.82, 'm', 'Perfil de proteção de piso')]

# ── o cabeçalho de cada bloco: medida geral e a cadeia que fecha ────────
CABECA = {
 I: ('seis módulos · 122 + 200 + 256 + 130 + 230 + 230 de frente',
     'DET 01 armário da lava e seca 122 × 265 × 67 · DET 02 bancada com '
     'armário 200 × 95 × 60 · DET 03 superior 01 256 × 170 × 60 · DET 04 '
     'armário 02 130 × 265 × 60, com o nicho do robô indo ao CHÃO · DET 05 '
     'bancada com armário 02 230 × 100 × 60 · DET 06 superior 02 230 × 165 '
     '× 60, com LED e cabideiro sob o bloco de 172 · ⭐ item único por '
     'decisão de preço [Jonathan, 28/10]: é um móvel contínuo que dá a '
     'volta no ambiente, e a fábrica o produz junto'),
}

# ── a folha: o que é texto da aba, e só dela ────────────────────────────
FOLHA = dict(
 aba='LAVANDERIA',
 sub='Jéssica e Michell · Projeto ICA · páginas 043 a 059 · seis itens · '
     'o ambiente inteiro é provençal: 31 frentes, nenhuma lisa · dois '
     'padrões de cor, Carvalho Malva nos armários e bancadas e Off White '
     'Suave nos superiores, nos nichos e nas frentes do DET 04 · caixaria '
     f'em Branco TX 15 · peça inteira até {ALT_MAX:g}, que é a chapa de '
     f'{CHAPA_C:g} menos o acerto de corte — e aqui nenhuma peça passa disso',
 chapa_txt={CM15:  'Carvalho Malva Premium · base das frentes e fechamentos aparentes',
            CM6:   'Carvalho Malva Premium · moldura usinada, peça inteira sobre a base',
            OW15:  'Off White Suave · base das frentes, nichos e fechamentos',
            OW6:   'Off White Suave · moldura usinada, peça inteira sobre a base',
            EST:   'Estrutura e caixaria · o padrão da Base para caixaria',
            PRAT18:'Prateleiras de vão acima de 70 cm · 18 mm contra empeno',
            FUN:   'Fundos · encaixe em rasgo, sem fita'},
 nota='⛔ O FRETE ESTÁ ZERADO DE PROPÓSITO: as linhas de frete da Base não '
      'têm preço ainda. Preencher lá e elas aparecem aqui sozinhas.   '
      '⭐⭐ TRINTA E UMA FRENTES PROVENÇAIS, E CADA UMA CONSOME A MESMA '
      'ÁREA DUAS VEZES — uma em 15 mm de base e outra em 6 mm de moldura, '
      'que é peça inteira usinada na router, não régua. É a frente, e não '
      'a caixaria, que decide o preço deste ambiente: a chapa de 6 mm nas '
      'duas cores sozinha já é uma linha de orçamento.   ⭐ NENHUMA PEÇA '
      'PRECISA SER DOBRADA: a maior é a porta de 210 do DET 04 e o fundo '
      'de 265 do mesmo móvel, e ambos cabem inteiros na chapa.',
 duvidas=[
  'O SÓCULO DE GRANITO BRANCO ITAÚNAS aparece nos SEIS detalhamentos, 10 cm '
  'de altura, e NÃO ENTROU nesta conta — é pedra, é marmoraria. ⚠ Quem '
  'fornece e instala? E a marcenaria precisa deixar alguma estrutura embaixo '
  'para a pedra apoiar, ou ela se resolve sozinha? São uns 12 m de sóculo.',
  'A BÁSCULA AQUI ABRE PELO ALÇAS TRASO, não pelo slim. A prancha escreve '
  '"puxador Alças Traso" em toda frente, básculas inclusive, folha por '
  'folha — e na Cozinha o senhor fechou slim de R$ 35 nas básculas. '
  'Orcei como o desenho manda. ⚠ São 11 básculas: manter o Traso ou passar '
  'para o slim vale R$ 825.',
  'OS NICHOS ABERTOS MOSTRAM A CAIXARIA. No DET 01 são dois vãos de 27 mais '
  'o da lava e seca, no DET 03 um nicho de 30, no DET 06 quatro nichos. '
  'Pus na cor só o que se vê de frente — prateleiras, tampos e fechamentos '
  '— e mantive a estrutura em Branco TX, que é a regra que o senhor fixou. '
  '⚠ Se o interior do nicho tem de ser todo na cor, soma chapa.',
  'A USINAGEM DA MOLDURA PROVENÇAL não tem preço na Base e aqui são 31 '
  'frentes — quase o dobro da Cozinha. Sai ZERO e o orçamento denuncia. '
  '⛔ Até esse preço existir, o custo deste ambiente é um PISO. ⚠ Vale '
  'cronometrar uma na router antes de fechar.',
  'O VÃO DA TÁBUA DE PASSAR, no DET 04, é só um VÃO de 38 × 206 — a prancha '
  'não desenha tábua embutida. ⚠ Se o cliente quiser a tábua dobrável '
  'deslizante, a Base traz R$ 480 de ferragem que não estão aqui.',
  '"PREVER SUPORTES" para vassouras e rodos, no vão de 138 do DET 04. A '
  'Base não tem esse item — o suporte oculto que ela traz é de prateleira, '
  'não de cabo de vassoura. ⚠ O que vai aí: gancho, pinça de mola, barra?',
  'O REFORÇO DA LAVA E SECA: a prancha pede "prever reforço para suportar '
  'lava e seca cheia". Subi o apoio para 18 mm e lancei 2,5 m de sarrafo de '
  'pinus por baixo. ⚠ Uma lava e seca cheia passa de 100 kg — confirmar se '
  'a fábrica quer sarrafo, cantoneira metálica ou painel duplo.',
  'A BANCADA EM GRANITO e as duas cubas não são nossas: bancada de 200 × 60 '
  'no DET 02 e de 230 × 60 no DET 05, dois tanques Tramontina Hera de 34 L '
  'em inox 50 × 40 e duas torneiras monocomando. ⚠ Só confirmar que o '
  'recorte da pedra é da marmoraria, não nosso.',
  'A PRATELEIRA DO VÃO DA CUBA, no DET 02, está desenhada a 37 do topo — e '
  'o tanque de 34 L desce com sifão. ⚠ Pode não caber. Se sair, são 18 mm '
  'a menos de chapa e dois suportes.'],
 nao_marcenaria=[
  'Sóculo revestido com Granito Branco Itaúnas nos seis móveis — 10 cm de altura, serviço de marmoraria',
  'Bancada em Granito Branco Itaúnas: 200 × 60 no DET 02 e 230 × 60 no DET 05',
  'Dois tanques de encaixe Tramontina Hera 34 L em aço inox escovado 50 × 40 e duas torneiras monocomando bica alta',
  'Máquina de lava e seca, robô aspirador e torre de tomadas — todos a definir com o cliente'],
 notas=[
  '⭐⭐ O AMBIENTE INTEIRO É PROVENÇAL: 31 frentes, nenhuma lisa, e com a '
  'moldura usinada na router cada frente consome a MESMA ÁREA DUAS VEZES — '
  'uma em 15 mm e outra em 6 mm. É a frente, e não a caixaria, que decide o '
  'preço daqui. A chapa de 6 mm nas duas cores é, sozinha, uma linha de '
  'orçamento.',
  '⭐ A PROFUNDIDADE ESTÁ COTEADA, ao contrário do que a primeira leitura '
  'dizia: 67 no DET 01, que é o que a lava e seca pede, e 60 nos outros '
  'cinco. Quem achou foi a leitura por VISTA — no texto corrido da prancha '
  'esses números caem longe do móvel a que pertencem, e foi assim que eu '
  'errei antes.',
  '⭐ NENHUMA PEÇA PRECISA SER DOBRADA. A maior é a porta de 210 do DET 04 e '
  'o fundo de 265 do mesmo móvel: ambos cabem inteiros na chapa de 275 × 185. '
  'Era a pergunta, e aqui a resposta é não.',
  '⭐⭐ NO DET 04 O CORPO E AS FRENTES SÃO DE COR DIFERENTE: armário e '
  'fechamento superior em Carvalho Malva, portas e básculas em Off White '
  'Suave. Está escrito em letra na VISTA FRONTAL e na LATERAL, e não é '
  'descuido do desenho — é o único móvel do ambiente assim.',
  '⭐ O NICHO DO ROBÔ ASPIRADOR, no DET 04, vai até o CHÃO: os 25 cm de baixo '
  'não têm sóculo embaixo, senão o robô não entra. A cadeia de cota fecha os '
  '265 pela coluna de 50 sem os 10 do sóculo, e é isso que a prancha quer '
  'dizer com "espaço para robô aspirador — confirmar modelo".',
  '⛔ O SÓCULO DE GRANITO NÃO É MARCENARIA, e não confundir com a "base '
  'metálica de 3 cm" que aparece na mesma folha: essa a casa resolve em MDF '
  'melamínico desde 26/10. Aqui a prancha pede pedra, nos seis móveis.',
  '⚠ ONZE BÁSCULAS COM PUXADOR ALÇAS TRASO, não com o slim. É o que a prancha '
  'escreve, folha por folha. Na Cozinha o senhor fechou o slim de R$ 35 para '
  'báscula; manter o Traso aqui custa R$ 825 a mais e é decisão de desenho, '
  'não de ferragem.'],
)
