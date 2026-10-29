# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO · COZINHA — levantamento peça por peça  [29/10/2026]

pranchas 27 a 30 · planta de layout, elevações A e B, corte AA.

⭐⭐⭐ ESTE AMBIENTE É LACA, E LACA NÃO É MELAMÍNICO. A prancha escreve, nas
  três vistas, "MDF laqueado acetinado M048, Sayerlack". Laca é **MDF CRU**
  mais **PINTURA EM CABINE** — duas linhas de custo, nunca uma.
  ⛔ Lançar a cozinha em melamínico seria repetir o erro da cômoda da
    Juliana: a proposta promete laca, o orçamento paga chapa revestida, e
    depois de assinado a casa deve a diferença. A proposta É o contrato.

⭐⭐ E TODA FRENTE TEM MOLDURA DE 5 CM — a prancha cota o "5" em cada folha.
  Moldura da MESMA cor é PROVENÇAL [regra 15]: NÃO são quatro réguas
  montadas em volta, é uma peça inteira de 6 mm usinada na router e colada
  sobre a base de 15. ⛔ A diferença não é cosmética: quatro réguas de 5 cm
  numa frente de 72 × 39 dariam 0,10 m²; a peça inteira dá 0,28 m². É quase
  três vezes mais chapa de 6 mm, e chapa se arredonda inteira.

⭐ AS CADEIAS FECHAM, e é isso que prova a leitura:
    VERTICAL (corte AA)  10 de sóculo + 78 de corpo + 2 de bancada + 65 de
                         vão + 85 de superior + 135 até o forro = 375
    HORIZONTAL (elev. A) 82 de parede + 285 de armário + 104 de geladeira = 471
    HORIZONTAL (elev. B) 2 + 60,5 + 75 de forno + 60,5 + 2 = 200
    PROFUNDIDADE (corte) 60 embaixo · 35 em cima

⛔⛔ FORA DO ESCOPO, e nesta cozinha é muita coisa:
  bancada, pés laterais, fundo e RODOBANCA em QUARTZITO TAJ MAHAL ESCOVADO ·
  o SÓCULO de 10 cm, que é ALVENARIA com frente revestida de quartzito ·
  coifa · cooktop · forno · geladeira · cuba de embutir inox · torneira ·
  lava-louças de 14 serviços.
  ⭐ O sóculo merece nota: ele aparece na elevação como se fosse do armário,
    e não é. É obra, e a frente de pedra é do marmorista.
"""
from base import P, gaveta, provencal, ALT_MAX

CRU18, CRU15, CRU6 = 'MDF Cru 18', 'MDF Cru 15', 'MDF Cru 6'
BR15, BR6 = 'MDF Branco TX 15', 'MDF Branco TX 6'

I1 = 'ELEVAÇÃO A Armário superior'
I2 = 'ELEVAÇÃO A Nicho sobre a geladeira'
I3 = 'ELEVAÇÃO A Armário inferior'
I4 = 'ELEVAÇÃO B Armário da bancada do cooktop'

COZINHA = [
 # ══ ITEM 01 · ARMÁRIO SUPERIOR — 285 × 85 × 35 ════════════════════════
 #  QUATRO portas de giro de 85 de altura, uma prateleira por vão, e o
 #  perfil de LED com abas correndo por baixo (detalhe 06 do corte).
 P('Lateral',              I1, 85, 35, 2, CRU15, (1, 1),
   '⭐ Aparente nas duas pontas, e em laca as duas faces se pintam'),
 P('Divisória',            I1, 85, 35, 3, BR15, (1, 0),
   'Três verticais fazem os quatro vãos de 69 · ⛔ interno em MDF BRANCO, '
   'como a prancha manda: só a frente e o que aparece é laca'),
 P('Tampo e base',         I1, 140.5, 35, 4, CRU15, (1, 1),
   '⛔ QUATRO peças de 140,5: os 281 do armário passam dos 275 da chapa, '
   'então tampo e base saem partidos ao meio'),
 P('Prateleira projetada', I1, 69, 33, 4, BR18 := 'MDF branco 18', (2, 2),
   'Uma por vão · 18 mm, e o vão de 69 fica no limite dos 70 da regra'),
 P('Fundo',                I1, 142.5, 85, 2, BR6, (0, 0),
   '⛔ DUAS peças de 142,5 · sem fita'),
 *provencal('Frente · porta de giro', I1, 69, 85, 4, CRU15, CRU6,
            'Quatro folhas · moldura de 5 cm usinada na router · puxador '
            'dourado a definir'),

 # ══ ITEM 02 · NICHO SOBRE A GELADEIRA — 104 × 40 × 35 ═════════════════
 #  ⭐ Aberto, sem porta: por dentro TUDO aparece, e por isso o nicho
 #    inteiro é laca, inclusive o fundo.
 P('Lateral',              I2, 40, 35, 2, CRU15, (1, 1)),
 P('Tampo e base',         I2, 104, 35, 2, CRU15, (1, 1),
   'Cadeia da elevação: 2 + 36 de vão + 2 = 40'),
 P('Fundo',                I2, 104, 40, 1, CRU6, (1, 1),
   '⭐ Sai em CRU e vai à cabine junto: nicho aberto não tem peça escondida'),

 # ══ ITEM 03 · ARMÁRIO INFERIOR — 285 × 78 × 60 ════════════════════════
 #  A cadeia da elevação A: 2 + 216 de frentes + 2 + 65 de lava-louças = 285.
 #  As 216 se abrem em três colunas de 72, e cada coluna tem duas frentes de
 #  39: em cima um gavetão e duas básculas, embaixo três gavetões.
 P('Lateral',              I3, 78, 60, 2, CRU15, (1, 1)),
 P('Divisória',            I3, 78, 60, 3, BR15, (1, 0),
   'Três verticais: fecham as colunas de 72 e o nicho da lava-louças'),
 P('Base',                 I3, 142.5, 60, 2, BR15, (1, 0),
   '⛔ DUAS peças de 142,5: os 285 passam dos 275 da chapa'),
 P('Travessa de topo',     I3, 142.5, 10, 4, BR15, (1, 0),
   '⭐ É o que recebe a bancada de quartzito. A pedra é do marmorista, mas '
   'o que a sustenta é nosso — sem isto ela apoia no ar'),
 P('Fundo',                I3, 142.5, 78, 2, BR6, (0, 0),
   '⛔ DUAS peças de 142,5 · sem fita'),
 *provencal('Frente · gavetão', I3, 72, 39, 4, CRU15, CRU6,
            'Quatro: um na fileira de cima e três na de baixo · moldura de '
            '5 cm na router · puxador dourado'),
 *provencal('Frente · báscula', I3, 72, 39, 2, CRU15, CRU6,
            'Duas, na fileira de cima · ⭐ articulador AVENTOS HK-XS da '
            'Blum, que é DE MOLAS, não a gás · moldura de 5 cm'),
 *gaveta(I3, 72, 55, 36, 4, 'Caixa de gavetão'),

 # ══ ITEM 04 · ARMÁRIO DA BANCADA DO COOKTOP — 200 × 78 × 60 ═══════════
 #  Cadeia da elevação B: 2 + 60,5 de gaveteiro + 75 de forno + 60,5 de
 #  armário + 2 = 200. ⛔ Os 75 do forno são eletro: o nicho é nosso, a
 #  frente não existe.
 P('Lateral',              I4, 78, 60, 2, CRU15, (1, 1),
   'Aparentes: a bancada é solta e se vê dos dois lados'),
 P('Divisória',            I4, 78, 60, 2, BR15, (1, 0),
   'Fecham o nicho do forno entre o gaveteiro e o armário'),
 P('Base',                 I4, 200, 60, 1, BR15, (1, 0)),
 P('Travessa de topo',     I4, 200, 10, 2, BR15, (1, 0), 'Recebe o quartzito'),
 P('Prateleira projetada', I4, 60.5, 58, 1, BR18, (2, 2),
   'A "Proj. prateleira" da coluna da direita'),
 P('Fundo',                I4, 200, 78, 1, BR6, (0, 0), '⛔ sem fita'),
 *provencal('Frente · gaveta de talheres', I4, 60.5, 17, 1, CRU15, CRU6,
            'Moldura de 5 cm · puxador dourado'),
 *provencal('Frente · gaveta', I4, 60.5, 17, 1, CRU15, CRU6, 'Moldura de 5 cm'),
 *provencal('Frente · gavetão', I4, 60.5, 44, 1, CRU15, CRU6, 'Moldura de 5 cm'),
 *provencal('Frente · porta de giro', I4, 60.5, 78, 1, CRU15, CRU6,
            'A folha da coluna da direita · moldura de 5 cm'),
 *gaveta(I4, 60.5, 55, 15, 2, 'Caixa de gaveta'),
 *gaveta(I4, 60.5, 55, 41, 1, 'Caixa de gavetão'),
]

# ════════════════════════════════════════════════════════════════════════
# ⭐⭐ A LACA, CONTADA DAS PEÇAS — não digitada
# ════════════════════════════════════════════════════════════════════════
#   Como o suporte de prateleira e a alma de aço, a laca é REGRA e não
#   lista: toda peça que sai em MDF Cru vai para a cabine, e esquecer uma
#   é esquecer a mais cara. Então ela se conta.
#
#   ⭐ DUAS FACES, E ISSO NÃO É CONSERVADORISMO: peça lacada de um lado só
#     EMPENA. A cabine pinta frente e verso, sempre.
#   ⛔ A MOLDURA DE 6 MM NÃO SOMA. Ela é colada sobre a base de 15 e as duas
#     viram uma peça de 21 mm antes de ir para a cabine — contar as duas
#     seria pintar a mesma superfície duas vezes. Quem vai à cabine é o
#     conjunto, e a área dele é a da base.
#   ⚠ O preço de R$ 650/m² é o da peça LISA. A frente aqui tem relevo de
#     moldura usinado na router, e relevo pinta mais devagar. Está na caixa
#     de dúvidas.
def _laca_m2(pecas, movel=None):
    t = 0.0
    for p in pecas:
        if movel and p['movel'] != movel: continue
        if not p['chave'].startswith('MDF Cru'): continue
        if 'moldura' in p['nome'].lower(): continue
        t += p['c'] * p['l'] * p['qtd'] / 10000 * 2
    return round(t, 2)

MOV_COZ = list(dict.fromkeys(p['movel'] for p in COZINHA))

# ════════════════════════════════════════════════════════════════════════
# A FERRAGEM, declarada por móvel
# ════════════════════════════════════════════════════════════════════════
from base import DOBRADICA, BASCULA, ALT_MAX, CHAPA_C

# ⭐ (móvel, rótulo, nº de gavetas, comprimento da corrediça em mm)
#   ⛔ "Gavetas com corrediças invisíveis" nas duas elevações — HETTICH
#     OCULTA, como a casa inteira.
GAVETAS = [
 (I3, 'Quatro gavetões de 72 × 39', 4, 500),
 (I4, 'Gaveta de talheres e gaveta do módulo de 60,5', 2, 500),
 (I4, 'Gavetão do módulo de 60,5', 1, 500),
]
# ⭐ (móvel, rótulo, nº de FOLHAS, dobradiças POR FOLHA, preço)
PORTAS = [
 (I1, 'Quatro portas de giro de 85 de altura', 4, 2, DOBRADICA),
 (I4, 'Porta de giro de 78 de altura', 1, 2, DOBRADICA),
]
# ⭐ (móvel, rótulo, quantidade, puxador)
#   ⛔ O ARTICULADOR AVENTOS É DE MOLAS, NÃO A GÁS — a correção de 28/10.
#   ⭐ O quarto elemento diz que NÃO leva puxador slim: aqui a prancha manda
#     "puxador a definir na cor dourado" em toda frente, básculas inclusive,
#     e slim mais puxador não se somam na mesma folha.
BASCULAS = [(I3, 'Duas básculas de 72 × 39, na fileira de cima', 2, 'dourado')]
PUXADORES  = []
# ⭐ (móvel, rótulo, nº de frentes com moldura usinada)
#   ⛔ É a MÃO DE OBRA da moldura provençal — a usinagem do relevo na
#     router, por frente. A chapa de 6 mm já está nas peças; o que falta é
#     o tempo de máquina. ⚠ A Base NÃO TEM PREÇO para ela e a linha sai
#     ZERO: o custo desta cozinha é um PISO enquanto a fábrica não
#     cronometrar uma frente.
MOLDURA = [
 (I1, 'Quatro portas de giro de 69 × 85', 4),
 (I3, 'Quatro gavetões e duas básculas de 72 × 39', 6),
 (I4, 'Gaveta de talheres, gaveta, gavetão e porta de giro', 4),
]
CABIDEIROS = []
ALMAS      = []
SERRALHERIA = []
VIDRO      = []
# ⛔ SEM CAVA NESTA COZINHA. O puxador é peça de compra, "a definir na cor
#   dourado" — não é a cava usinada da varanda e dos quartos.
CAVA = []
# ⭐ (móvel, rótulo, metros de perfil de LED)
LED = [(I1, 'Perfil de LED com abas por baixo do armário superior, em toda '
        'a extensão de 285 · detalhe 06 do corte', 2.85)]
# ⭐ (móvel, nome, rótulo, quantidade, unidade, chave)
OUTRAS = [
 *[(mv, 'Laca Sayerlack M048 acetinada',
    f'{_laca_m2(COZINHA, mv):g} m² de peça em MDF cru, pintada NAS DUAS '
    'FACES · ⛔ peça lacada de um lado só empena · a moldura de 6 mm não '
    'soma: ela é colada sobre a base e as duas vão à cabine como uma peça '
    'só · ⚠ R$ 650/m² é o preço da peça LISA, e esta tem relevo de router',
    _laca_m2(COZINHA, mv), 'm²', 'Laca Sayerlack M048 acetinada')
   for mv in MOV_COZ if _laca_m2(COZINHA, mv) > 0],
 (I1, 'Puxador NEO32 Bronze', '⚠ "Puxador a definir na cor DOURADO" nas '
  'quatro portas do superior · ⛔ a prancha não nomeia modelo e a Base não '
  'tem a linha: sai ZERO', 4, 'un', 'Puxador NEO32 Bronze'),
 (I3, 'Puxador NEO32 Bronze', 'Seis frentes do inferior, básculas inclusive '
  '· ⛔ sem modelo e sem preço: sai ZERO', 6, 'un', 'Puxador NEO32 Bronze'),
 (I4, 'Puxador NEO32 Bronze', 'Quatro frentes da bancada do cooktop · ⛔ sem '
  'modelo e sem preço: sai ZERO', 4, 'un', 'Puxador NEO32 Bronze'),
 (I3, 'Perfil de proteção de piso', '⛔ NÃO ENTRA: o armário inferior não '
  'toca o chão, ele assenta sobre o sóculo de 10 cm, que é ALVENARIA com '
  'frente de quartzito — obra, não marcenaria. Linha a zero para que a '
  'ausência fique escrita', 0, 'm', 'Perfil de proteção de piso'),
]

# ════════════════════════════════════════════════════════════════════════
CABECA = {
 I1: ('285 × 85 × 35',
      'ELEVAÇÃO A · quatro portas de giro de 69 × 85 com moldura de 5 cm, '
      'uma prateleira por vão e o perfil de LED com abas correndo por baixo '
      '· ⛔ toda a frente é laca M048 Sayerlack sobre MDF cru'),
 I2: ('104 × 40 × 35',
      'ELEVAÇÃO A · nicho ABERTO sobre a geladeira, cadeia 2 + 36 + 2 = 40 '
      '· ⭐ sem porta: por dentro tudo aparece, e por isso o nicho inteiro '
      'vai à cabine, fundo incluído'),
 I3: ('285 × 78 × 60',
      'ELEVAÇÃO A · cadeia 2 + 216 de frentes + 2 + 65 de lava-louças = 285 '
      '· as 216 se abrem em três colunas de 72, cada uma com duas frentes '
      'de 39: em cima um gavetão e duas básculas, embaixo três gavetões · '
      '⛔ assenta sobre sóculo de 10 cm em ALVENARIA, que não é nosso'),
 I4: ('200 × 78 × 60',
      'ELEVAÇÃO B · cadeia 2 + 60,5 de gaveteiro + 75 de forno + 60,5 de '
      'armário + 2 = 200 · ⛔ os 75 do forno são eletro: o nicho é nosso, a '
      'frente não existe'),
}

FOLHA = dict(
 aba='COZINHA',
 sub='Gustavo Raposo · executivo Luiza Pacheco, pranchas 27 a 30 · ⭐⭐ O '
     'AMBIENTE DE LACA DA CASA: MDF laqueado acetinado M048, Sayerlack, '
     'nos quatro móveis, com moldura de 5 cm em toda frente · pé-direito '
     'de 375, armário inferior de 60 de profundidade e superior de 35',
 chapa_txt={CRU15: '⭐ MDF CRU · a base de toda peça lacada — frentes, '
                   'laterais aparentes, tampos e bases · ⚠ preço DERIVADO '
                   'da razão cru/fosco de 0,76 da Base antiga, não lido',
            CRU18: 'MDF CRU · peças de 18 mm que vão à cabine',
            CRU6:  '⭐ MDF CRU · a MOLDURA PROVENÇAL: peça inteira de 6 mm, '
                   'mesma medida da frente, relevo usinado na router e '
                   'colada sobre a base de 15',
            BR15:  'Branco TX · divisórias, bases e travessas — "Interno em '
                   'MDF Branco", como a prancha manda',
            BR18:  'Branco · prateleiras internas',
            BR6:   'Branco TX · fundos dos armários fechados'},
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a QUANTIDADE é a '
      'célula AMARELA no fim do painel de material, e ela sai ZERO.   '
      '⭐⭐⭐ LACA NÃO É MELAMÍNICO, e esta é a linha que mais pesa aqui: a '
      'chapa sai CRUA e a pintura é um terceirizado por metro quadrado, a '
      'R$ 650. São duas linhas, nunca uma — e a área conta as DUAS FACES, '
      'porque peça lacada de um lado só empena.   ⭐⭐ TODA FRENTE TEM '
      'MOLDURA DE 5 CM, e moldura da mesma cor é PROVENÇAL: não são quatro '
      'réguas em volta, é uma peça inteira de 6 mm usinada na router e '
      'colada sobre a base. Numa frente de 72 × 39 isso é 0,28 m² de chapa '
      'de 6 contra os 0,10 m² que as réguas dariam.   ⛔ O SÓCULO DE 10 CM '
      'NÃO É NOSSO: a elevação o desenha como se fosse do armário, e ele é '
      'ALVENARIA com frente revestida de quartzito. Obra e marmorista.',
 duvidas=[
  '⚠⚠ O PREÇO DO MDF CRU É DERIVADO, NÃO LIDO. A Base de hoje não tem linha '
  'de cru; a Base antiga trazia a razão cru/fosco em 95/125 = 0,76, e eu a '
  'apliquei sobre os 700 / 550 / 350 de cor — dando 530 / 410 / 255. ⛔ É a '
  'chapa de toda a cozinha: se a razão estiver errada, o ambiente inteiro '
  'se move. Confirmar com o fornecedor.',
  '⚠ R$ 650/m² É O PREÇO DA LACA EM PEÇA LISA. Toda frente desta cozinha '
  'tem relevo de moldura usinado na router, e relevo pinta mais devagar: '
  'mais demãos, mais lixa entre demãos, mais tempo de cabine. ⭐ Perguntar '
  'ao pintor o acréscimo da frente usinada — pode ser de 20% a 40%.',
  'O PUXADOR DOURADO não tem modelo na prancha ("a definir na cor dourado") '
  'nem linha na Base, e os CATORZE saem ZERO. ⛔ Enquanto isso o custo desta '
  'cozinha é um PISO. ⚠ Puxador dourado de linha boa custa de R$ 80 a '
  'R$ 250 a unidade: em catorze frentes isso é de R$ 1.100 a R$ 3.500.',
  'AS DUAS BÁSCULAS ESTÃO NO ARMÁRIO INFERIOR, na fileira de cima, e isso é '
  'incomum — báscula costuma ser aérea. ⭐ Lancei o AVENTOS HK-XS da Blum, '
  'que é a báscula da casa e é DE MOLAS, não a gás. ⚠ Confirmar se a '
  'arquiteta quis báscula mesmo ou se é gaveta desenhada com abertura '
  'para cima.',
  'O NICHO SOBRE A GELADEIRA tem 40 de altura e 104 de largura, e a prancha '
  'não diz se leva LED. ⭐ Lancei o LED só no armário superior, onde o '
  'detalhe 06 o desenha. ⚠ Nicho de laca escura sobre geladeira sem luz '
  'fica cego — vale perguntar.'],
 nao_marcenaria=[
  'Bancada, pés laterais, fundo e rodobanca em Quartzito Taj Mahal '
  'Escovado — pedra não é escopo da marcenaria',
  'O sóculo de 10 cm, que é alvenaria com frente revestida de quartzito',
  'Coifa, cooktop, forno, geladeira e lava-louças de 14 serviços',
  'Cuba de embutir em inox e torneira de bancada'],
 notas=[
  '⭐⭐⭐ É A COZINHA DE LACA, e ela é o ambiente mais caro por metro '
  'quadrado da casa. Três coisas se somam: a chapa sai crua e precisa de '
  'pintura em cabine, a pintura é por metro quadrado nas duas faces, e toda '
  'frente leva uma segunda peça inteira de 6 mm usinada na router.',
  '⭐ O INTERNO É BRANCO, e isso segura o custo. A prancha manda "Interno '
  'em MDF Branco" nos dois armários: divisória, prateleira e fundo saem em '
  'Branco TX e NÃO vão à cabine. Só vai à cabine o que aparece.',
  '⚠ O NICHO É A EXCEÇÃO: aberto, sem porta, com tudo à vista — nele até o '
  'fundo sai em cru e vai à cabine.',
  '⛔ MUITA COISA DESTA ELEVAÇÃO NÃO É NOSSA. A bancada, os pés laterais, o '
  'fundo e a rodobanca são quartzito; o sóculo é alvenaria; e cinco '
  'equipamentos são do cliente. A proposta tem de dizer isso por escrito, '
  'porque a elevação desenha tudo junto e o cliente vê um móvel só.'],
)
