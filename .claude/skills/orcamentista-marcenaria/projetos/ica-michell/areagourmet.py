# -*- coding: utf-8 -*-
"""ICA · ÁREA GOURMET — levantamento peça por peça  [28/10/2026]

páginas 077 a 087 · QUATRO detalhamentos, mas só TRÊS são marcenaria.

⛔⛔ O DET 04 NÃO É NOSSO. "Coifa em inox preta, friso de 2 cm, vidros nas
  laterais, *prever vidro para suportar altas temperaturas". É serralheria
  em inox mais vidro temperado especial — zero MDF. Fica fora da conta e
  dentro da caixa de dúvidas, porque alguém tem de orçar.

⭐⭐ DUAS CORES QUE NUNCA ANDARAM JUNTAS NESTE PROJETO. O DET 01 e o DET 03
  são Jequitibá Rosa Linha Essencial Wood — Duratex; o DET 02 inteiro é
  MDF Preto Ultra Premium — Duratex. Não há peça aparente em outra cor, e a
  caixaria segue o Branco TX da regra do Jonathan.
  ⛔ "MDF Preto Ultra" não existia na Base: foi lançado em 28/10 como
    melamínico fosco (700 / 550 / 350), que é a linha a que ele pertence.

⭐⭐ TREZE FRENTES DE GAVETA NO DET 02, TODAS COM CAVA NA PRÓPRIA MADEIRA, e
  a cava aqui corre a LARGURA INTEIRA da frente — o desenho mostra a faixa
  de ponta a ponta. São 8,22 m de usinagem, não treze encaixes curtos como
  no Quarto. É a diferença entre R$ 411 e R$ 10, e está na caixa de dúvidas.

⭐ A GRANDE PEÇA DO AMBIENTE É O SUPERIOR DE 319, e ele passa dos 275 da
  chapa em TRÊS peças corridas: topo, base e fundo. Divididas em duas de
  160, que é onde cai a divisória do terceiro módulo de 64 — a emenda não
  fica solta no meio do vão.

⛔ O SÓCULO, A BANCADA E O FRONTÃO SÃO GRANITO PRETO SÃO GABRIEL ESCOVADO.
  Marmoraria, não marcenaria. O sóculo tem 5 de altura (não 10, como na
  Lavanderia) e a bancada tem saia de 5.
"""
from base import (P, gaveta, acabamento, ALT_MAX, CHAPA_C, DOBRADICA, ALTAS)

# ── os padrões ──────────────────────────────────────────────────────────
JR18, JR15 = 'MDF Jequitibá Rosa 18', 'MDF Jequitibá Rosa 15'
PT18       = 'MDF Preto Ultra Premium 18'
EST, FUN   = 'MDF Branco TX 15', 'MDF Branco TX 6'
PRAT18     = 'MDF Branco TX 18'   # ⭐ só onde o vão passa de 70 cm

I1 = 'DET 01 Armário do freezer'
I2 = 'DET 02 Bancada com armário'
I3 = 'DET 03 Armário superior'

AREAGOURMET = [
 # ══ ITEM 01 · ARMÁRIO DO FREEZER — 75 × 270 × 80 ═════════════════════
 #  VISTA FRONTAL  largura 75 · altura 20 + 55 + 195 = 270
 #  VISTA FRONTAL INTERNA  o vão de 55 abre em 24 + 2 + 24, uma prateleira
 #                         e os 195 de baixo são NICHO ABERTO do freezer
 #  VISTA SUPERIOR e LATERAL  profundidade 80
 P('Lateral',               I1, 270, 80, 2, JR18, (1, 0),
   'Piso ao topo · ⭐ 270 cabe inteira: fica 3 cm abaixo do limite de 273'),
 P('Topo',                  I1, 75, 80, 1, JR18, (1, 1), 'Aparente'),
 P('Base do módulo basculante', I1, 75, 80, 1, JR18, (1, 0),
   '⭐ é ela que fecha o nicho do freezer por cima, a 195 do piso'),
 P('Fundo do módulo basculante', I1, 75, 75, 1, FUN, (0, 0),
   'Encaixe em rasgo · ⛔ o nicho do freezer fica SEM fundo: o compressor '
   'precisa de ventilação'),
 P('Fechamento superior · frontal fixo', I1, 75, 20, 1, JR18, (2, 2),
   'A faixa de 20 que a prancha chama de fechamento superior · peça fixa, '
   'não abre'),
 P('Frente · báscula',      I1, 75, 55, 1, JR18, (2, 2),
   'Lisa · fecho toque · ⭐ nenhuma frente provençal neste ambiente'),
 P('Prateleira interna',    I1, 71, 78, 1, EST, (1, 0),
   '⭐ "armário interno com prateleira em MDF Branco" — a prancha escreve a '
   'cor da prateleira, e é a da caixaria'),

 # ══ ITEM 02 · BANCADA COM ARMÁRIO — 424 × 90 × 60 ════════════════════
 #  VISTA FRONTAL  50 + 80 + 48 + 85 + 51 + 100 + 10 = 424
 #                 altura 5 sóculo + 80 corpo + 5 tampo = 90
 #  as colunas de 50 e de 51 abrem em 20+20+20+20 · as de 85 e 100 em 40+40
 #  VISTA SUPERIOR  profundidade 60 · a cuba fica no trecho de 295
 P('Lateral e divisória',   I2, 80, 60, 8, EST, (1, 0),
   'Oito verticais nos sete vãos: 50, 80 do fogão, 48, 85, 51, 100 e os 10 fixos'),
 P('Base',                  I2, 212, 60, 2, EST, (1, 0),
   '⛔ 424 de corrida não cabe na chapa: duas peças de 212, com a emenda '
   'caindo numa divisória'),
 P('Travessa de apoio da bancada', I2, 212, 10, 4, EST, (1, 0),
   'Frente e fundo, duas peças cada · ⭐ a pedra apoia nelas, não em tampo cheio'),
 P('Fundo',                 I2, 212, 80, 2, FUN, (0, 0), 'Encaixe em rasgo'),
 P('Frente · gaveta',       I2, 50, 20, 4, PT18, (2, 2),
   'Coluna de 50 · lisa, com cava na própria madeira'),
 P('Frente · gaveta',       I2, 51, 20, 4, PT18, (2, 2),
   'Coluna de 51 · lisa, com cava na própria madeira'),
 P('Frente · gavetão',      I2, 85, 40, 2, PT18, (2, 2),
   'Coluna de 85 · lisa, com cava na própria madeira'),
 P('Frente · gavetão',      I2, 100, 40, 2, PT18, (2, 2),
   'Coluna de 100 · lisa, com cava na própria madeira'),
 P('Frente · gavetão para lixo', I2, 48, 80, 1, PT18, (2, 2),
   '⭐ frente única de altura inteira · a prancha escreve "gavetão para '
   'lixeira" — o suporte de lixeira em si não está na Base'),
 P('Painel fixo',           I2, 10, 80, 1, PT18, (2, 2),
   'Os 10 da ponta direita · a prancha escreve "fixo"'),
 *gaveta(I2, 50, 55, 20, 4, 'Gaveta de 50'),
 *gaveta(I2, 51, 55, 20, 4, 'Gaveta de 51'),
 *gaveta(I2, 85, 55, 40, 2, 'Gavetão de 85'),
 *gaveta(I2, 100, 55, 40, 2, 'Gavetão de 100'),
 *gaveta(I2, 48, 55, 80, 1, 'Gavetão para lixo'),

 # ══ ITEM 03 · ARMÁRIO SUPERIOR — 319 × 120 × 60 e 30 ═════════════════
 #  VISTA FRONTAL  5 × 64 = 320 ≈ 319 · altura 20 + 55 + 45 = 120
 #  VISTA LATERAL  ⭐ a profundidade MUDA: 60 no bloco de cima, 30 no de
 #                 baixo — está cotada em "30 + 30" e desenhada em degrau
 P('Bloco superior · lateral e divisória', I3, 55, 60, 6, EST, (1, 0),
   'Dois laterais e quatro divisórias, nos cinco vãos de 64'),
 P('Bloco superior · base e topo', I3, 160, 60, 4, EST, (1, 0),
   '⛔ 319 de corrida não cabe: duas peças de 160 em cada, com a emenda na '
   'divisória do terceiro vão'),
 P('Bloco superior · fundo', I3, 160, 55, 2, FUN, (0, 0), 'Encaixe em rasgo'),
 P('Fechamento superior · frontal fixo', I3, 160, 20, 2, JR18, (2, 2),
   'A faixa de 20 de ponta a ponta · aparente, em Jequitibá Rosa'),
 P('Bloco inferior · lateral e divisória', I3, 45, 30, 6, EST, (1, 0),
   '⭐ só 30 de profundidade: o bloco de baixo recua, e é embaixo dele que '
   'corre o LED'),
 P('Bloco inferior · base', I3, 160, 30, 2, EST, (1, 0),
   'O topo do bloco de baixo é a base do de cima'),
 P('Bloco inferior · fundo', I3, 160, 45, 2, FUN, (0, 0), 'Encaixe em rasgo'),
 P('Frente · báscula alta', I3, 64, 55, 5, JR18, (2, 2),
   'Cinco de 64 × 55 · lisas, fecho toque'),
 P('Frente · báscula baixa', I3, 64, 45, 5, JR18, (2, 2),
   'Cinco de 64 × 45 · lisas, fecho toque · ⭐ é esta fileira que a prancha '
   'marca "com iluminação"'),
]

# ── ferragem, declarada item a item ─────────────────────────────────────
#  ⭐ "fecho toque" aqui segue o que o Jonathan fechou na Cozinha: báscula
#    com articulador a gás mais puxador slim de R$ 35, SEM pulsador Blum —
#    os dois não se somam na mesma frente.
GAVETAS = [(I2, 'Bancada · oito gavetas de 20 e quatro gavetões de 40', 12, 550),
           (I2, 'Bancada · gavetão para lixo de 80', 1, 550)]
PORTAS  = []
BASCULAS= [(I1, 'Báscula de 75 × 55 do armário do freezer', 1),
           (I3, 'Cinco básculas de 64 × 55 e cinco de 64 × 45', 10)]
#  ⭐ a cava corre a LARGURA INTEIRA de cada frente, como a prancha desenha —
#    a faixa vai de ponta a ponta em todo gavetão. ⛔ Declarada COLUNA POR
#    COLUNA, que é o formato da Base: (nº de frentes, largura em cm).
#    50×4 + 51×4 + 85×2 + 100×2 + 48×1 = 822 cm = 8,22 m
CAVA     = [(I2, 'Quatro gavetas da coluna de 50',  4,  50),
            (I2, 'Quatro gavetas da coluna de 51',  4,  51),
            (I2, 'Dois gavetões da coluna de 85',   2,  85),
            (I2, 'Dois gavetões da coluna de 100',  2, 100),
            (I2, 'Gavetão para lixo, de 48',        1,  48)]
PUXADORES= []
MOLDURA  = []
LED      = [(I3, 'Sob o bloco inferior, de ponta a ponta', 3.19)]
CABIDEIROS = []
SARRAFOS = []
SUPORTES = [(I1, 'Prateleira interna do módulo basculante · 1 × 2', 2)]
ALMAS    = []
VIDRO    = []
SERRALHERIA = []
OUTRAS   = []

# ── o cabeçalho de cada bloco: medida geral e a cadeia que fecha ────────
CABECA = {
 I1: ('75 × 270 × 80',
      'VISTA FRONTAL largura 75 · altura 20 + 55 + 195 = 270 · '
      'VISTA FRONTAL INTERNA o vão de 55 abre em 24 + 2 + 24, uma prateleira, '
      'e os 195 de baixo são NICHO ABERTO para o freezer de 594 L · '
      'VISTA SUPERIOR e LATERAL profundidade 80'),
 I2: ('424 × 90 × 60',
      'VISTA FRONTAL 50 + 80 + 48 + 85 + 51 + 100 + 10 = 424 · altura '
      '5 de sóculo + 80 de corpo + 5 de tampo = 90 · as colunas de 50 e de 51 '
      'abrem em 20 + 20 + 20 + 20 e as de 85 e 100 em 40 + 40 · o vão de 80 é '
      'o fogão e o de 10 é fixo · VISTA SUPERIOR profundidade 60, com a cuba '
      'no trecho de 295'),
 I3: ('319 × 120 × 60 e 30',
      'VISTA FRONTAL 5 × 64 = 320 ≈ 319 · altura 20 + 55 + 45 = 120 · '
      '⭐ VISTA LATERAL a profundidade MUDA: 60 no bloco de cima e 30 no de '
      'baixo, cotada em 30 + 30 e desenhada em degrau'),
}

# ── a folha: o que é texto da aba, e só dela ────────────────────────────
FOLHA = dict(
 aba='ÁREA GOURMET',
 sub='Jéssica e Michell · Projeto ICA · páginas 077 a 087 · quatro '
     'detalhamentos, TRÊS de marcenaria: o DET 04 é coifa em inox com vidro '
     'de alta temperatura e não é nosso · duas cores aparentes, Jequitibá '
     'Rosa nos dois armários e Preto Ultra Premium na bancada · caixaria em '
     f'Branco TX 15 · peça inteira até {ALT_MAX:g}, que é a chapa de '
     f'{CHAPA_C:g} menos o acerto de corte',
 chapa_txt={JR18: 'Jequitibá Rosa Linha Essencial Wood · armário do freezer e superior',
            PT18: 'Preto Ultra Premium · a bancada inteira, corpo e frentes',
            EST:  'Estrutura e caixaria · o padrão da Base para caixaria',
            PRAT18:'Prateleiras de vão acima de 70 cm · 18 mm contra empeno',
            FUN:  'Fundos · encaixe em rasgo, sem fita'},
 nota='⛔ O FRETE ESTÁ ZERADO DE PROPÓSITO: as linhas de frete da Base não '
      'têm preço ainda. Preencher lá e elas aparecem aqui sozinhas.   '
      '⛔⛔ O DET 04 — COIFA CHURRASQUEIRA — NÃO ESTÁ NESTA CONTA. É coifa '
      'em inox preta com friso de 2 cm e vidros nas laterais, e a própria '
      'prancha pede "prever vidro para suportar altas temperaturas". Zero '
      'MDF: é serralheria em inox mais vidro temperado especial, e precisa '
      'de cotação de terceiro.   ⛔ SÓCULO, BANCADA E FRONTÃO SÃO GRANITO '
      'PRETO SÃO GABRIEL ESCOVADO, de marmoraria — 4,24 m de bancada com '
      'saia de 5 e 4,24 m de sóculo.',
 duvidas=[
  'A COIFA DO DET 04 É INOX E VIDRO, não marcenaria: 106 × 112 × 60, friso '
  'de 2 cm, vidros nas laterais e a nota "*prever vidro para suportar altas '
  'temperaturas". ⚠ Quem orça? A Base tem serralheria por metro e vidraceiro '
  'por serviço, mas nada de inox dobrado nem de vidro refratário. ⛔ É um '
  'dos quatro itens do ambiente e sai ZERO daqui.',
  'A CAVA DA BANCADA CORRE A LARGURA INTEIRA de cada uma das treze frentes — '
  'é assim que o desenho mostra a faixa, de ponta a ponta. Dá 8,22 m a '
  'R$ 50/m = R$ 411. ⚠ Se a Base cobrasse por PEÇA seriam R$ 650; se fosse '
  'encaixe curto como no Quarto, R$ 65. É a mesma dúvida do Quarto, e aqui '
  'ela vale dez vezes mais. Qual é a regra?',
  'O SÓCULO AQUI TEM 5 DE ALTURA, não 10 como na Lavanderia, e é "revestido '
  'com granito Preto São Gabriel". ⚠ Revestido quer dizer que existe uma '
  'estrutura por baixo — nossa, em MDF? Se for, são 4,24 m de sóculo que não '
  'estão nesta conta. Se a pedra se apoia sozinha, não há o que fazer.',
  'O "MDF PRETO ULTRA PREMIUM - DURATEX" não está nomeado na Base. Lancei como '
  'melamínico fosco — R$ 700 a chapa de 18, que é a linha a que ele pertence '
  'e o mesmo preço do Carvalho Malva e do Off White. ⚠ Confirmar que o Ultra '
  'Premium não é linha mais cara que o Essencial.',
  'O GAVETÃO PARA LIXEIRA tem frente de 48 × 80 e a prancha não desenha o '
  'suporte. ⚠ A Base não tem lixeira embutida — nem o aro, nem o balde. '
  'Orcei a gaveta e a corrediça; o suporte de lixeira, se houver, é item a '
  'cotar.',
  'O VÃO DO FOGÃO TEM 80 DE LARGURA e o fogão desenhado é um Electrolux de 5 '
  'bocas com 2 fornos. ⚠ Orcei as duas divisórias que cercam o vão e nenhuma '
  'base embaixo — forno embutido pede ventilação e normalmente não leva '
  'fundo nem base. Confirmar se a fábrica quer travessa de reforço ali.',
  'O DEPURADOR DE AR de 60 cm retrátil fica embutido no bloco inferior do '
  'DET 03, que tem 30 de profundidade. ⚠ Um depurador retrátil de 60 pede '
  'recorte na base e costuma precisar de mais fundo que 30. Confirmar o '
  'modelo antes do corte.',
  'O ARMÁRIO DO DET 01 ENVOLVE UM FREEZER DE 594 LITROS e o nicho tem '
  '75 × 195 × 80. ⚠ Deixei o nicho SEM FUNDO, para o compressor ventilar. '
  'Confirmar a medida real do freezer com a porta aberta: 75 de vão para um '
  'freezer de 75 não sobra folga para dobradiça nem para nivelador.',
  '⛔ A BASE METÁLICA DE 3 CM aparece nas onze folhas daqui, como em todo o '
  'projeto, e o senhor resolveu em 26/10 que a casa faz em MDF melamínico. '
  '⚠ Continua NÃO LANÇADA em nenhum ambiente — Living, Cozinha, Lavanderia, '
  'Quarto e agora Área Gourmet. São uns 3 m de rodapé por ambiente.'],
 nao_marcenaria=[
  'DET 04 · Coifa churrasqueira em inox preta, 106 × 112 × 60, friso de 2 cm, '
  'vidros nas laterais em vidro para altas temperaturas — serralheria e vidraceiro',
  'Bancada e frontão em granito Preto São Gabriel escovado, 4,24 × 0,60 com saia de 5 cm',
  'Sóculo de 5 cm revestido com granito Preto São Gabriel escovado, 4,24 m',
  'Fogão 5 bocas Electrolux Preto Experience, 2 fornos e PerfectCook360 (FE5DB)',
  'Freezer Vertical Tripla Ação 594 L Preto Imbera VZ21 MAX',
  'Depurador de Ar Electrolux 60 cm retrátil Preto Efficient com luz de LED (DE6RB)',
  'Cuba Tramontina Design Collection Quadrum 60 em aço inox acetinado e misturador '
  'monocomando de mesa Level Gourmet - Deca',
  'Churrasqueira — a definir na prancha'],
 notas=[
  '⛔⛔ UM DOS QUATRO ITENS NÃO É MARCENARIA. O DET 04 é coifa em inox preta '
  'com vidros laterais e vidro de alta temperatura: zero MDF, zero ferragem '
  'nossa. Esta aba traz TRÊS itens, e o quarto está na caixa de dúvidas '
  'esperando cotação de terceiro.',
  '⭐⭐ DUAS CORES APARENTES, E ELAS SE DIVIDEM POR MÓVEL, não por peça: '
  'Jequitibá Rosa Linha Essencial Wood no DET 01 e no DET 03, Preto Ultra '
  'Premium no DET 02 inteiro — corpo e frentes. É a primeira vez no projeto '
  'que um móvel sai todo numa cor de frente, caixaria inclusive seria o '
  'natural; mantive a caixaria em Branco TX, que é a regra da casa, e só as '
  'peças à vista em Preto.',
  '⭐ TREZE FRENTES DE GAVETA NO DET 02 e NENHUMA PORTA DE GIRO no ambiente '
  'inteiro. Tudo abre por gaveta ou por báscula: são 13 pares de corrediça e '
  '11 articuladores, e zero dobradiça. Vale conferir contra o hábito — um '
  'levantamento por olho poria dobradiça aqui.',
  '⭐ A PROFUNDIDADE DO DET 03 MUDA NO MEIO DO MÓVEL: 60 no bloco de cima e '
  '30 no de baixo. Está cotada em "30 + 30" na VISTA LATERAL e desenhada em '
  'degrau na perspectiva. Quem lê só a cota corrida orça 60 nos dois e '
  'compra chapa a mais.',
  '⭐ TRÊS PEÇAS CORRIDAS PASSAM DOS 275 DA CHAPA, todas no DET 03: topo, '
  'base e fundo de 319. Dividi em duas de 160, e a emenda cai na divisória '
  'do terceiro vão de 64 — não fica solta no meio do vão. O mesmo vale para '
  'a base e o fundo de 424 do DET 02, em duas de 212.',
  '⛔ O SÓCULO AQUI TEM 5, não 10 como na Lavanderia. É granito Preto São '
  'Gabriel escovado, e não confundir com a base metálica de 3 cm que a '
  'prancha pede em toda folha e que a casa resolve em MDF melamínico desde '
  '26/10.'],
)
