# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO · LAVANDERIA — levantamento peça por peça  [29/10/2026]

pranchas 32 a 34 · planta de layout, elevação A (vista externa e interna do
armário) e elevação B.

⭐⭐ É O AMBIENTE DE BÁSCULA DA CASA: SEIS. Quatro no armário superior da
  elevação A, uma no corpo inferior e uma na elevação B. Cada báscula é um
  articulador AVENTOS HK-XS da Blum a R$ 250 — e seis delas pesam mais que
  trinta dobradiças. ⛔ O AVENTOS é DE MOLAS, não a gás; a correção é de
  28/10 e vale para a proposta inteira.

⭐ A CADEIA VERTICAL FECHA NOS 375 DE PÉ-DIREITO, por dois caminhos:
    170 até o forro + 50 de superior + 65 de vão + 90 de bancada = 375
    170 + 50 + 55 + 10 + 2 de bancada + 78 de corpo + 10 de sóculo = 375
  ⛔ Dos 90, só os 78 são nossos: 2 é a bancada de granito e 10 é o sóculo,
    que é alvenaria com frente de porcelanato.

⭐ A CADEIA HORIZONTAL DA ELEVAÇÃO A: 60 de painel fixo + 208 de gaveteiro =
  268, mais 62 da torre = 330. A torre tem 260 de altura e abre numa folha
  só de 250 — a vista interna mostra o que ela guarda: duas prateleiras em
  cima e um nicho de 150 para vassoura e rodo.

⛔ FORA: bancada em GRANITO MARROM IMPERIAL ESCOVADO · sóculo de 10 cm com
  frente em porcelanato travertino 120 × 120 · tanque de embutir inox 50×40 ·
  torneira de parede · as duas máquinas lava e seca.
"""
from base import P, gaveta

BD18, BD15, BD6 = ('MDF Branco Diamante 18', 'MDF Branco Diamante 15',
                   'MDF Branco Diamante 6')
BR15, BR6 = 'MDF Branco TX 15', 'MDF Branco TX 6'

I1 = 'ELEVAÇÃO A Armário superior'
I2 = 'ELEVAÇÃO A Armário inferior'
I3 = 'ELEVAÇÃO A Torre de vassouras'
I4 = 'ELEVAÇÃO B Armário superior e inferior'

LAVANDERIA = [
 # ══ ITEM 01 · ARMÁRIO SUPERIOR DA ELEVAÇÃO A — 268 × 50 × 35 ══════════
 #  QUATRO básculas de 67 de largura, lado a lado.
 P('Lateral',              I1, 50, 35, 2, BD15, (1, 1)),
 P('Divisória',            I1, 50, 35, 3, BR15, (1, 0), 'Fazem os quatro vãos de 67'),
 P('Tampo e base',         I1, 264, 35, 2, BD15, (1, 1)),
 P('Fundo',                I1, 268, 50, 1, BR6, (0, 0), '⛔ sem fita'),
 P('Frente · báscula',     I1, 67, 50, 4, BD15, (2, 2),
   'Quatro · articulador AVENTOS HK-XS da Blum, DE MOLAS · puxador tipo '
   'cava usinada na marcenaria'),

 # ══ ITEM 02 · ARMÁRIO INFERIOR DA ELEVAÇÃO A — 268 × 78 × 60 ══════════
 #  60 de painel FIXO (é onde fica o tanque) + 208 em três colunas de 69.
 #  Na fileira de cima: gavetão, báscula, gavetão. Na de baixo: três gavetões.
 P('Lateral',              I2, 78, 60, 2, BD15, (1, 1)),
 P('Divisória',            I2, 78, 60, 3, BR15, (1, 0),
   'Separam o painel fixo de 60 e as três colunas de 69'),
 P('Base',                 I2, 268, 60, 1, BR15, (1, 0)),
 P('Travessa de topo',     I2, 268, 10, 2, BR15, (1, 0),
   '⭐ Recebe a bancada de granito, que é do marmorista'),
 P('Fundo',                I2, 268, 78, 1, BR6, (0, 0), '⛔ sem fita'),
 P('Frente · painel fixo', I2, 60, 78, 1, BD15, (2, 2),
   '⭐ A elevação escreve "Fixo": fecha o vão do tanque e não abre · '
   '⛔ sem dobradiça e sem cava'),
 P('Frente · gavetão',     I2, 69, 39, 5, BD15, (2, 2),
   'Cinco: dois na fileira de cima e três na de baixo · puxador cava'),
 P('Frente · báscula',     I2, 69, 39, 1, BD15, (2, 2),
   'Uma, no meio da fileira de cima · AVENTOS HK-XS'),
 *gaveta(I2, 69, 55, 36, 5, 'Caixa de gavetão'),

 # ══ ITEM 03 · TORRE DE VASSOURAS — 62 × 260 × 60 ══════════════════════
 #  Uma folha só, de 250. A vista interna cota 2 + 46 + 2 + 46 + 2 + 150 +
 #  2 + 10 = 260: duas prateleiras em cima e um nicho de 150 embaixo.
 P('Lateral',              I3, 260, 60, 2, BD15, (1, 1),
   '⛔ 260 de altura: cabe nos 273 da chapa, mas é peça inteira e manda no '
   'plano de corte'),
 P('Tampo e base',         I3, 58, 60, 2, BD15, (1, 1)),
 P('Prateleira projetada', I3, 58, 58, 2, BD18, (2, 2),
   'As duas do topo, nos vãos de 46 · ⭐ vão de 58 abaixo dos 70, mas 18 mm '
   'porque a torre é alta e a peça trabalha'),
 P('Fundo',                I3, 62, 260, 1, BR6, (0, 0), '⛔ sem fita'),
 P('Frente · porta de giro', I3, 62, 250, 1, BD15, (2, 2),
   '⭐ UMA FOLHA SÓ, de 2,50 m · ⛔ folha desse porte pede TRÊS dobradiças, '
   'não duas · puxador tipo cava usinada'),

 # ══ ITEM 04 · ARMÁRIO DA ELEVAÇÃO B — 60 × 78 × 60 e 35 × 50 × 35 ═════
 #  A parede de 214 é 154 das duas máquinas lava e seca mais 60 de armário.
 #  Em cima, um aéreo estreito de 35 com UMA báscula.
 P('Lateral · superior',   I4, 50, 35, 2, BD15, (1, 1)),
 P('Tampo e base · superior', I4, 31, 35, 2, BD15, (1, 1)),
 P('Fundo · superior',     I4, 35, 50, 1, BR6, (0, 0), '⛔ sem fita'),
 P('Frente · báscula',     I4, 35, 50, 1, BD15, (2, 2), 'AVENTOS HK-XS'),
 P('Lateral · inferior',   I4, 78, 60, 2, BD15, (1, 1)),
 P('Base · inferior',      I4, 56, 60, 1, BR15, (1, 0)),
 P('Travessa de topo · inferior', I4, 56, 10, 2, BR15, (1, 0),
   'Recebe a bancada de granito'),
 P('Fundo · inferior',     I4, 60, 78, 1, BR6, (0, 0), '⛔ sem fita'),
 P('Frente · gavetão',     I4, 60, 39, 2, BD15, (2, 2),
   'Dois · puxador tipo cava usinada'),
 *gaveta(I4, 60, 55, 36, 2, 'Caixa de gavetão'),
]

# ════════════════════════════════════════════════════════════════════════
from base import DOBRADICA

# ⭐ (móvel, rótulo, nº de gavetas, comprimento da corrediça em mm)
#   ⛔ "Gavetões com corrediças invisíveis" — HETTICH OCULTA.
GAVETAS = [
 (I2, 'Cinco gavetões de 69 × 39', 5, 500),
 (I4, 'Dois gavetões de 60 × 39', 2, 500),
]
# ⭐ (móvel, rótulo, nº de FOLHAS, dobradiças POR FOLHA, preço)
PORTAS = [
 (I3, 'A folha única da torre, de 62 × 250 · ⭐ TRÊS dobradiças: folha de '
      '2,50 m não se segura em duas', 1, 3, DOBRADICA),
]
# ⭐ (móvel, rótulo, quantidade, puxador)
#   ⛔ O puxador desta lavanderia é CAVA USINADA em toda frente, básculas
#     inclusive — a prancha diz "puxador tipo cava NA MARCENARIA". Por isso
#     o quarto elemento NÃO é 'slim': slim e cava não se somam na mesma folha.
BASCULAS = [
 (I1, 'Quatro básculas do armário superior', 4, 'cava'),
 (I2, 'A báscula do meio da fileira de cima', 1, 'cava'),
 (I4, 'A báscula do aéreo de 35', 1, 'cava'),
]
PUXADORES = MOLDURA = LED = CABIDEIROS = ALMAS = VIDRO = SERRALHERIA = []
# ⭐ (móvel, rótulo, nº de frentes, extensão de cava em cm por frente)
CAVA = [
 (I1, 'As quatro básculas do superior', 4, 67),
 (I2, 'Cinco gavetões e uma báscula · ⛔ o painel FIXO não leva cava',
  6, 69),
 (I3, 'A folha da torre', 1, 62),
 (I4, 'Dois gavetões e a báscula do aéreo', 3, 60),
]
# ⭐ (móvel, nome, rótulo, quantidade, unidade, chave)
OUTRAS = [
 (I3, 'Perfil de proteção de piso', 'A torre de 62 toca o chão', 0.62, 'm',
  'Perfil de proteção de piso'),
 (I2, 'Perfil de proteção de piso', '⛔ NÃO ENTRA no armário inferior: ele '
  'assenta sobre o sóculo de 10 cm, que é alvenaria com frente de '
  'porcelanato. Linha a zero para que a ausência fique escrita', 0, 'm',
  'Perfil de proteção de piso'),
]

CABECA = {
 I1: ('268 × 50 × 35',
      'ELEVAÇÃO A · quatro básculas de 67 lado a lado, sobre a bancada · '
      'cadeia vertical 170 até o forro + 50 deste armário + 65 de vão + 90 '
      'da bancada = 375'),
 I2: ('268 × 78 × 60',
      'ELEVAÇÃO A · 60 de painel FIXO, onde fica o tanque, mais 208 em três '
      'colunas de 69 · em cima gavetão, báscula e gavetão; embaixo três '
      'gavetões · ⛔ assenta sobre sóculo de alvenaria'),
 I3: ('62 × 260 × 60',
      'ELEVAÇÃO A · a torre de vassouras, numa folha só de 250 · a vista '
      'interna cota 2 + 46 + 2 + 46 + 2 + 150 + 2 + 10 = 260: duas '
      'prateleiras em cima e o nicho de 150 para vassoura e rodo embaixo'),
 I4: ('214 de parede · armário de 60 × 78 e aéreo de 35 × 50',
      'ELEVAÇÃO B · 154 das duas máquinas lava e seca mais 60 de armário '
      'com dois gavetões · em cima, um aéreo estreito de 35 com uma báscula'),
}

FOLHA = dict(
 aba='LAVANDERIA',
 sub='Gustavo Raposo · executivo Luiza Pacheco, pranchas 32 a 34 · MDF '
     'Branco Diamante, Linha Trama, Duratex · ⭐⭐ o ambiente de BÁSCULA da '
     'casa: seis articuladores AVENTOS HK-XS, e puxador tipo cava usinada '
     'na marcenaria em toda frente',
 chapa_txt={BD15: 'Branco Diamante · Linha Trama · Duratex · frentes, '
                  'laterais, tampos e bases',
            BD18: 'Branco Diamante · Linha Trama · Duratex · as duas '
                  'prateleiras do topo da torre',
            BR15: 'Branco TX · divisórias, bases e travessas internas',
            BR6:  'Branco TX · fundos'},
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a QUANTIDADE é a '
      'célula AMARELA no fim do painel de material, e ela sai ZERO.   '
      '⭐⭐ SEIS BÁSCULAS, e elas mandam no custo da ferragem: quatro no '
      'aéreo da elevação A, uma no corpo inferior e uma na elevação B. Cada '
      'uma é um articulador AVENTOS HK-XS da Blum a R$ 250 — seis pesam '
      'mais que trinta dobradiças. ⛔ E o AVENTOS é DE MOLAS, não a gás.   '
      '⭐ O PUXADOR É CAVA USINADA em toda frente, básculas inclusive: a '
      'prancha diz "puxador tipo cava NA MARCENARIA". ⛔ Por isso não entra '
      'puxador slim em báscula nenhuma — slim e cava não se somam na mesma '
      'folha.   ⛔ O SÓCULO DE 10 CM NÃO É NOSSO: é alvenaria com frente '
      'revestida de porcelanato travertino.',
 duvidas=[
  'A FOLHA DA TORRE TEM 2,50 M DE ALTURA e 62 de largura. ⭐ Lancei TRÊS '
  'dobradiças, não duas — folha desse porte descai na segunda. ⚠ Confirmar '
  'com a fábrica se não pede quatro: 2,50 m em MDF de 15 é peça pesada, e a '
  'cava usinada na borda tira material justamente onde a dobradiça fixa.',
  'A BÁSCULA DO MEIO DA FILEIRA DE CIMA do armário inferior é estranha: '
  'báscula costuma ser aérea, e esta está a 50 cm do chão. ⚠ Confirmar se a '
  'arquiteta quis báscula mesmo, ou se é um gavetão desenhado com abertura '
  'para cima. Muda R$ 250 e muda o jeito de usar.',
  '⚠ O PAINEL "FIXO" DE 60 fecha o vão do tanque. Lancei como frente que '
  'não abre, sem dobradiça e sem cava. ⛔ Mas se for painel removível para '
  'manutenção do sifão, ele precisa de alguma fixação de desmonte — e isso '
  'não está em nenhuma linha.',
  'A PRANCHA PEDE "PREVER REFORÇO PARA SUPORTAR LAVA E SECA CHEIA" em '
  'projetos deste tipo, e aqui as duas máquinas ficam sob a bancada de '
  'granito, não dentro de móvel nosso. ⭐ Por isso não lancei reforço. ⚠ Se '
  'alguma delas for embutir em módulo de marcenaria, o apoio sobe para '
  '18 mm e ganha engradado de MDF.'],
 nao_marcenaria=[
  'Bancada em Granito Marrom Imperial escovado — pedra não é escopo da '
  'marcenaria',
  'Sóculo de 10 cm com frente revestida em porcelanato travertino 120 × 120',
  'Tanque de embutir em inox 50 × 40 e torneira de parede',
  'As duas máquinas lava e seca'],
 notas=[
  '⭐⭐ A FERRAGEM PESA MAIS QUE A CHAPA AQUI. Seis básculas, sete gavetões '
  'em corrediça oculta Hettich e uma folha de 2,50 m com três dobradiças. '
  'É um ambiente pequeno em metro quadrado e caro em ferragem.',
  '⭐ A TORRE DE VASSOURAS É O MÓVEL MAIS ALTO DA LAVANDERIA e o mais '
  'simples: 260 de altura, uma folha só, duas prateleiras no topo e 150 de '
  'nicho livre embaixo. O que ela custa é a lateral inteira de 260.',
  '⛔ DOIS ITENS DA ELEVAÇÃO NÃO SÃO NOSSOS e o cliente vê um móvel só: a '
  'bancada de granito e o sóculo de alvenaria revestido. A proposta tem de '
  'dizer isso por escrito.'],
)
