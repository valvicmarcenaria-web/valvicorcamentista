# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO · SUÍTE 02 FILHAS — peça por peça  [30/10/2026]

pranchas 57 a 60 · planta de layout, elevação A, elevação B, detalhe da
mesa de cabeceira, detalhe da base de cama e o detalhe 10 do perfil de LED
embutido na cabeceira.

⭐⭐ É UM QUARTO SEM ARMÁRIO — e isso não é falta, é projeto: a roupa vai
  toda para o CLOSET ao lado, atrás da porta pivotante de 72. O que este
  quarto tem é PAINEL, ESTANTE, PENTEADEIRA e CAMA.

⭐ A PAREDE DA ELEVAÇÃO A FECHA EM 509:
     50 de estante + 79 de painel claro + 96 de painel escuro
     + 94 de painel claro + 96 de painel escuro + 17 + 72 de porta + 5
  ⭐ Os dois trechos de 96 são Nogueira Thar com SEIS frisos de 16 cada e
    um perfil de LED em cada aresta vertical — quatro perfis de 2,75.
    ⛔ São os painéis atrás das duas camas: a luz lava a madeira e os
      frisos dão o relevo. O resto da parede é Off-White liso.

⛔⛔ A PORTA PIVOTANTE DE 72 É DAQUI, e reaparece no Closet Suíte 02 pela
  outra cara. Como a da Suíte Master, ela conta UMA vez — e lá entra como
  ausência declarada.

⭐ A PALHINHA É O MATERIAL DESTE QUARTO: frente de gaveta com moldura de
  MDF e palhinha natural na penteadeira, nos dois armários de canto
  arredondado e na mesa de cabeceira. ⛔ Palhinha não é chapa: é m² de
  material comprado, R$ 650, e vai em cima de uma moldura que é marcenaria.

⭐ TODAS AS FRENTES DE PALHINHA ABREM POR FECHO-TOQUE — que é o PULSADOR da
  Base. ⛔ Fecho-toque não se soma a puxador nem a cava: frente de palhinha
  com puxador por cima não existe no desenho.

⛔ FORA: os dois espelhos redondos de Ø70 e o espelho de 60 × 170, todos "a
  definir" · o papel de parede · o tapete de 200 × 400 · a estrutura
  cilíndrica dourada que sustenta a penteadeira e a mesa de cabeceira · os
  colchões.
"""
from base import P, gaveta, CORREDICA, engradado

NT18, NT15 = 'MDF Nogueira Thar 18', 'MDF Nogueira Thar 15'
OWS18, OWS15 = 'MDF Off-White Suave 18', 'MDF Off-White Suave 15'
BR6 = 'MDF Branco TX 6'

I1 = 'ELEVAÇÃO A Estante e armário de canto arredondado'
I2 = 'ELEVAÇÃO A Painéis de parede'
I3 = 'ELEVAÇÃO A Porta pivotante mimetizada'
I4 = 'ELEVAÇÃO B Penteadeira de 279'
I5 = 'ELEVAÇÃO B Dois armários de canto arredondado'
I6 = 'MESA DE CABECEIRA entre as duas camas'
I7 = 'BASE CAMA Duas bases de 196 × 96'

N_FRISO = 6                  # por painel de 96, a cada 16

SUITE_02 = [
 # ══ ITEM 01 · ESTANTE 50 × 225 × 25 + ARMÁRIO 50 × 45 × 40 ════════════
 P('Lateral da estante', I1, 225, 25, 2, NT18, (1, 0),
   '⭐ A estante é RASA: 25 de profundidade, cotado na vista de lado da '
   'elevação B · canto arredondado na aresta da frente'),
 P('Tampo da estante', I1, 47, 25, 1, NT18, (1, 0)),
 P('Prateleira', I1, 47, 25, 5, NT18, (1, 0),
   '⭐ Cinco, com vãos de 42,6 · cada uma leva perfil de LED por baixo'),
 P('Fundo da estante', I1, 225, 50, 1, BR6, (0, 0), '⛔ sem fita'),
 P('Lateral do armário', I1, 45, 40, 2, NT18, (1, 0),
   '⭐ O armário de baixo é mais FUNDO que a estante: 40 contra 25 · é o '
   'que dá base ao conjunto'),
 P('Tampo e base do armário', I1, 47, 40, 2, NT18, (1, 0)),
 P('Rodapé', I1, 50, 5, 1, NT18, (1, 0)),
 P('Frente de gaveta · moldura de palhinha', I1, 47, 21, 2, NT18, (2, 2),
   '⭐ Duas gavetas · a frente é MOLDURA de MDF com PALHINHA no miolo, e '
   'abre por FECHO-TOQUE: não leva puxador nem cava'),
 *gaveta(I1, 47, 35, 19, 2, 'Caixa de gaveta'),
 P('Fundo do armário', I1, 50, 45, 1, BR6, (0, 0), '⛔ sem fita'),

 # ══ ITEM 02 · PAINÉIS DA PAREDE DE 509 ════════════════════════════════
 P('Painel claro · trecho de 79',  I2, 275, 79, 1, OWS18, (1, 1),
   'Off-White Suave liso, sem friso'),
 P('Painel claro · trecho de 94',  I2, 275, 94, 1, OWS18, (1, 1)),
 P('Painel claro · retorno de 17 e de 5', I2, 275, 22, 1, OWS18, (1, 1),
   '⭐ Os dois pedaços estreitos que fecham a parede ao lado da porta'),
 P('Painel escuro frisado · trecho de 96', I2, 275, 96, 2, NT18, (1, 1),
   f'⭐ DOIS trechos, um atrás de cada cama · {N_FRISO} frisos de 0,5 × '
   f'0,5 a cada 16 · ⛔ 96 cabe nos 185 da chapa deitada, mas os 275 de '
   f'altura são o limite exato: peça de topo a topo, sem sobra'),
 *engradado(I2, 40.0, OWS18, 'Travessa de fixação dos painéis na parede',
            larg=7.0),

 # ══ ITEM 03 · PORTA PIVOTANTE — 72 × 210 ══════════════════════════════
 P('Porta pivotante · face da suíte',  I3, 210, 72, 1, OWS18, (2, 2),
   '⭐ Mimetizada no painel claro · puxador tipo CAVA QUADRADA de 10 × 10, '
   'a 100 do chão e a 5 da borda'),
 P('Porta pivotante · face do closet', I3, 210, 72, 1, OWS18, (2, 2),
   '⭐ As DUAS faces em Off-White Suave — ao contrário da pivotante da '
   'Suíte Master, que é de dois padrões · a tranca fica nesta face'),
 *engradado(I3, 7.0, OWS18, 'Quadro interno da folha', larg=7.0),
 P('Bandeira sobre a porta pivotante', I3, 65, 72, 1, OWS18, (1, 1),
   '⭐ Os 65 que fecham os 275 acima da folha de 210'),

 # ══ ITEM 04 · PENTEADEIRA — 279 × 50, a 75 do chão ════════════════════
 P('Tampo da penteadeira', I4, 139.5, 50, 2, NT18, (1, 1),
   '⛔ 279 não cabe na chapa de 275: sai em DUAS de 139,5 · ⭐ a emenda '
   'cai no eixo do pé cilíndrico do meio'),
 P('Saia frontal e de fundo', I4, 139.5, 12, 4, NT18, (1, 1),
   '⭐ São os 12 de altura aparente do tampo, na frente e atrás'),
 P('Frente de gaveta · moldura de palhinha', I4, 68, 12, 4, NT18, (2, 2),
   '⭐ Quatro gavetas rasas de 12 · moldura de MDF com PALHINHA no miolo · '
   'abre por FECHO-TOQUE'),
 *gaveta(I4, 68, 40, 10, 4, 'Caixa de gaveta'),

 # ══ ITEM 05 · DOIS ARMÁRIOS DE CANTO ARREDONDADO — 70 × 50 × 50 ═══════
 P('Lateral', I5, 45, 50, 4, NT18, (1, 0),
   '⭐ Duas por armário, dois armários · 45 = 50 menos os 5 do rodapé'),
 P('Tampo e base', I5, 67, 50, 4, NT18, (1, 0)),
 P('Rodapé', I5, 70, 5, 2, NT18, (1, 0)),
 P('Lateral cega de 18 · o canto arredondado', I5, 45, 18, 2, NT18,
   (1, 1),
   '⭐ A elevação B cota 18 + 52 nos 70: os 18 são a faixa cheia do canto '
   'arredondado, e as gavetas só têm 52 de boca'),
 P('Frente de gaveta pequena · moldura de palhinha', I5, 52, 14, 2, NT18,
   (2, 2), 'Uma por armário · FECHO-TOQUE'),
 P('Frente de gaveta grande · moldura de palhinha', I5, 52, 27, 2, NT18,
   (2, 2), 'Uma por armário · FECHO-TOQUE'),
 *gaveta(I5, 52, 45, 12, 2, 'Caixa de gaveta'),
 *gaveta(I5, 52, 45, 25, 2, 'Caixa de gavetão'),
 P('Fundo', I5, 70, 45, 2, BR6, (0, 0), '⛔ sem fita'),

 # ══ ITEM 06 · MESA DE CABECEIRA — 40 × 56 × 50 ════════════════════════
 P('Lateral', I6, 50, 56, 2, NT15, (1, 0)),
 P('Tampo e base', I6, 37, 56, 2, NT15, (1, 1)),
 P('Frente de gaveta · palhinha', I6, 37, 22, 2, NT15, (2, 2),
   '⭐ Duas gavetas · frente em PALHINHA · ⛔ aqui o puxador é REDONDO '
   'DOURADO, não fecho-toque: é o único móvel de palhinha do quarto com '
   'puxador à vista'),
 *gaveta(I6, 37, 50, 20, 2, 'Caixa de gaveta'),
 P('Fundo', I6, 40, 50, 1, BR6, (0, 0), '⛔ sem fita'),

 # ══ ITEM 07 · DUAS BASES DE CAMA — 196 × 96 × 45, AMBAS COM GAVETÃO ═══
 P('Lateral da base', I7, 196, 45, 4, NT18, (2, 2)),
 P('Cabeceira e pé da base', I7, 92, 45, 4, NT18, (2, 2)),
 P('Gavetão da cama auxiliar · frente', I7, 190, 30, 2, NT18, (2, 2),
   '⭐ AS DUAS bases levam gavetão aqui — na Suíte 01 só uma levava'),
 P('Gavetão da cama auxiliar · lateral', I7, 88, 28, 4, NT18, (1, 0)),
 P('Gavetão da cama auxiliar · costas',  I7, 190, 28, 2, NT18, (1, 0)),
 P('Gavetão da cama auxiliar · fundo',   I7, 190, 88, 2, BR6, (0, 0),
   '⛔ sem fita'),
]

# ⭐ (móvel, rótulo, nº de gavetas, preço do par)
GAVETAS = [
 (I1, 'Duas gavetas de 47 × 21 sob a estante · corrediça invisível', 2,
  CORREDICA),
 (I4, 'Quatro gavetas rasas de 68 × 12 na penteadeira · corrediça '
      'invisível', 4, CORREDICA),
 (I5, 'Quatro gavetas nos dois armários, de 14 e de 27 · corrediça '
      'invisível', 4, CORREDICA),
 (I6, 'Duas gavetas da mesa de cabeceira · corrediça invisível', 2,
  CORREDICA),
 (I7, 'Os DOIS gavetões de cama auxiliar · ⚠ o que eles pedem é '
      'CORREDIÇA DE CARGA, que a Base traz sem preço', 2, CORREDICA),
]
# ⭐ (móvel, rótulo, nº de frentes, extensão de cava em cm por frente)
CAVA = [
 (I3, 'Cava QUADRADA de 10 × 10 nas duas faces da folha pivotante', 2, 10),
 (I7, 'Os dois gavetões · ⚠ a prancha diz só "puxador a definir"', 4, 20),
]
# ⭐ (móvel, rótulo, metros de perfil)
LED = [
 (I1, 'CINCO perfis de 0,47 sob as cinco prateleiras da estante', 2.35),
 (I2, 'QUATRO perfis verticais de 2,75, um em cada aresta dos dois '
      'painéis escuros de 96 · ⭐ é a luz que lava a madeira frisada atrás '
      'das camas, detalhe 10', 11.00),
]
PORTAS = BASCULAS = PUXADORES = MOLDURA = CABIDEIROS = ALMAS = []
VIDRO = SERRALHERIA = []
# ⭐ (móvel, nome, rótulo, quantidade, unidade, chave)
OUTRAS = [
 (I2, 'Usinagem de friso',
  f'⭐ {N_FRISO} frisos de 0,5 × 0,5 em CADA um dos dois painéis de 96, a '
  f'cada 16, subindo os 275 · {2*N_FRISO*2.75:.2f} m de rasgo · ⛔ A '
  'COTAR: a linha da Base está sem preço', round(2*N_FRISO*2.75, 2), 'm',
  'Usinagem de friso'),
 (I1, 'Pulsador', '⭐ Fecho-toque nas duas gavetas', 2, 'un', 'Pulsador'),
 (I4, 'Pulsador', '⭐ Fecho-toque nas quatro gavetas da penteadeira', 4,
  'un', 'Pulsador'),
 (I5, 'Pulsador', '⭐ Fecho-toque nas quatro gavetas dos dois armários', 4,
  'un', 'Pulsador'),
 (I6, 'Puxador a definir',
  '⭐ Puxador REDONDO na cor DOURADO, modelo a definir · dois, um por '
  'gaveta · ⛔ A COTAR: a Base traz a linha sem preço', 2, 'un',
  'Puxador a definir'),
 (I1, 'Palhinha natural',
  '⭐ Duas frentes de 47 × 21 · 0,20 m²', 0.20, 'm²', 'Palhinha natural'),
 (I4, 'Palhinha natural',
  '⭐ Quatro frentes de 68 × 12 · 0,33 m²', 0.33, 'm²', 'Palhinha natural'),
 (I5, 'Palhinha natural',
  '⭐ Quatro frentes: duas de 52 × 14 e duas de 52 × 27 · 0,43 m²', 0.43,
  'm²', 'Palhinha natural'),
 (I6, 'Palhinha natural',
  '⭐ Duas frentes de 37 × 22 · 0,16 m²', 0.16, 'm²', 'Palhinha natural'),
 (I7, 'Estrado em metalon',
  '⭐ QUATRO quadros: dois dos leitos e dois das camas auxiliares · aqui '
  'as duas bases levam gavetão, e gavetão com colchão é cama', 4, 'quadro',
  'Estrado em metalon'),
 (I7, 'Corrediça de carga',
  '⚠ O que os dois gavetões realmente pedem · declarada a ZERO porque a '
  'Base não tem preço para ela', 2, 'par', 'Corrediça de carga'),
 (I3, 'Perfil de proteção de piso',
  '⛔ NÃO ENTRA na folha: porta não é painel. O perfil dos painéis está no '
  'item 02', 0, 'm', 'Perfil de proteção de piso'),
 (I2, 'Perfil de proteção de piso',
  'Os 387 de painel que tocam o chão', 3.87, 'm',
  'Perfil de proteção de piso'),
 (I1, 'Perfil de proteção de piso', 'O rodapé de 50 toca o chão', 0.50,
  'm', 'Perfil de proteção de piso'),
 (I5, 'Perfil de proteção de piso',
  'Os dois rodapés de 70 tocam o chão', 1.40, 'm',
  'Perfil de proteção de piso'),
]

CABECA = {
 I1: ('50 × 275 × 25 e 40',
      'ELEVAÇÃO A · estante rasa de 25 com CINCO prateleiras e perfil de '
      'LED em cada uma, sobre armário mais fundo de 40 com duas gavetas de '
      'palhinha · canto arredondado'),
 I2: ('387 × 275',
      'ELEVAÇÃO A · a parede de 509 menos a porta de 72 e a estante de 50 '
      '· DOIS trechos de 96 em Nogueira Thar com seis frisos cada e um '
      'perfil de LED em cada aresta, e o resto em Off-White liso'),
 I3: ('72 × 210 + bandeira de 65',
      'ELEVAÇÃO A · folha mimetizada no painel claro, Off-White nas DUAS '
      'faces · cava quadrada de 10 × 10 e tranca no lado do closet · '
      '⛔ ela reaparece no Closet Suíte 02 e lá entra a ZERO'),
 I4: ('279 × 50 × 12, a 75 do chão',
      'ELEVAÇÃO B · penteadeira suspensa em pé cilíndrico metálico, com '
      'quatro gavetas rasas de frente em palhinha e fecho-toque'),
 I5: ('70 × 50 × 50, duas unidades',
      'ELEVAÇÃO B · um em cada ponta da penteadeira · 18 de faixa cheia no '
      'canto arredondado e 52 de boca de gaveta · duas gavetas cada, de 14 '
      'e de 27, em palhinha com fecho-toque'),
 I6: ('40 × 56 × 50',
      'PRANCHA 58 · mesa de cabeceira entre as duas camas, sobre estrutura '
      'cilíndrica dourada · duas gavetas de palhinha com puxador REDONDO '
      'dourado — o único móvel de palhinha do quarto com puxador à vista'),
 I7: ('196 × 96 × 45, duas unidades',
      'PRANCHA 60 · as DUAS bases levam gavetão de cama auxiliar · QUATRO '
      'quadros de estrado em metalon ao todo'),
}

FOLHA = dict(
 aba='SUÍTE 02 FILHAS',
 sub='Gustavo Raposo · executivo Luiza Pacheco, pranchas 57 a 60 · ⭐ um '
     'quarto SEM ARMÁRIO: a roupa vai para o closet ao lado · painel '
     'frisado com LED, estante, penteadeira de palhinha e duas camas',
 chapa_txt={
  NT18: 'Nogueira Thar · Linha Design · Duratex · a estante, os painéis '
        'frisados de 96, a penteadeira, os dois armários de canto e as '
        'duas bases de cama',
  NT15: 'Nogueira Thar · Linha Design · Duratex · só a mesa de cabeceira',
  OWS18: 'Off-White Suave · Linha Sense · Duratex · os painéis lisos da '
         'parede, as duas faces da porta pivotante e a bandeira',
  BR6:   'Branco TX · os fundos da estante, dos armários, da mesa de '
         'cabeceira e dos dois gavetões',
  'MDF Branco TX 15': 'Branco TX · a caixaria das catorze gavetas',
 },
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a QUANTIDADE é '
      'a célula AMARELA no fim do painel de material, e ela sai ZERO.   '
      '⭐⭐ UM QUARTO SEM ARMÁRIO, e é projeto: a roupa vai para o closet '
      'atrás da porta pivotante. O que pesa aqui é PAINEL — 3,87 m de '
      'parede revestida, com quatro perfis de LED verticais.   '
      '⛔ A PORTA PIVOTANTE DE 72 É DAQUI e reaparece no Closet Suíte 02 '
      'pela outra cara. Lá ela entra a zero.   '
      '⭐ A PALHINHA É O MATERIAL DO QUARTO: catorze frentes de gaveta com '
      'moldura de MDF e palhinha no miolo, 1,12 m² ao todo. ⛔ Todas abrem '
      'por FECHO-TOQUE, menos as duas da mesa de cabeceira, que levam '
      'puxador redondo dourado.',
 duvidas=[
  '⚠ A MÃO DE OBRA DA FRENTE DE PALHINHA não está lançada. Lancei a chapa '
  'da moldura e o m² da palhinha, que são MATERIAL. ⛔ Montar moldura com '
  'palhinha esticada é serviço, e a Base não tem a linha — a de "moldura '
  'provençal" está lá, sem preço, e é outra coisa. São catorze frentes.',
  '⚠ A PROFUNDIDADE DA ESTANTE é 25 e a do armário de baixo é 40. O 25 '
  'está cotado na vista de lado da elevação B; o 40 é dedução minha, pela '
  'proporção do desenho. ⛔ Se o armário também tiver 25, saem cerca de '
  '0,6 m² de Nogueira.',
  '⚠ A MESA DE CABECEIRA tem 40 × 56 em planta e a ALTURA não está cotada '
  'em lugar nenhum. Adotei 50, que é altura de cabeceira ao lado de cama '
  'de 45 de base. ⚠ A estrutura cilíndrica dourada que a sustenta é '
  'serralheria "a definir" e NÃO está no orçamento.',
  '⚠ A ESTRUTURA CILÍNDRICA DA PENTEADEIRA também não está. São os pés '
  'metálicos dourados que seguram 2,79 m de tampo, e a prancha só diz '
  '"cor a definir". ⛔ Sem eles a penteadeira não para de pé: é um item '
  'que precisa de cotação antes de fechar o preço.',
  '⚠ OS QUATRO PERFIS DE LED VERTICAIS somam 11 m e são R$ 1.650 — o '
  'terceiro item mais caro do quarto. ⭐ Conferi no desenho: há um perfil '
  'em cada aresta de cada painel de 96, e os dois painéis são os que '
  'ficam atrás das camas.',
  '⚠ OS SEIS FRISOS POR PAINEL vêm das seis cotas de 16 que a prancha '
  'desenha sobre cada trecho de 96. São 33 m de rasgo, a ZERO: a linha de '
  'usinagem de friso entrou hoje na Base sem preço.',
 ],
 nao_marcenaria=[
  '⛔ OS DOIS ESPELHOS REDONDOS de Ø70 sobre a penteadeira e o ESPELHO de '
  '60 × 170 da outra parede — os três "a ser adquirido, modelo a definir".',
  '⛔ O PAPEL DE PAREDE da elevação B e o TAPETE de 200 × 400.',
  '⛔ A ESTRUTURA CILÍNDRICA DOURADA que sustenta a penteadeira e a mesa '
  'de cabeceira. ⚠ É serralheria e está "a definir" — mas sem ela os dois '
  'móveis não existem. Vale cobrar o modelo da arquiteta.',
  '⛔ OS COLCHÕES, inclusive os dois das camas auxiliares.',
  '⛔ A ELÉTRICA: interruptor de 4 teclas com 2 tomadas, as tomadas duplas '
  'e os dois pontos para rede atrás da penteadeira.',
 ],
 notas=[
  '⭐ SETE ITENS E NENHUM ARMÁRIO DE ROUPA. É o quarto mais decorativo da '
  'casa: painel frisado com luz, palhinha, cantos arredondados e dourado. '
  'O orçamento dele é quase todo chapa e acabamento, com pouquíssima '
  'ferragem — catorze pares de corrediça e dez pulsadores.',
  '⭐ TODOS OS CANTOS SÃO ARREDONDADOS: a estante, os dois armários da '
  'penteadeira e a própria penteadeira, com raio de 5 em planta e de 2 na '
  'elevação. ⛔ Canto arredondado em MDF é usinagem e é fita curva — a '
  'fita de topo tem de contornar o raio sem vincar, e isso é mão de obra '
  'que não aparece em metro de aresta.',
  '⭐ AS DUAS BASES DE CAMA LEVAM GAVETÃO, diferente da Suíte 01, onde só '
  'uma leva. São quatro quadros de estrado em metalon neste quarto contra '
  'três lá.',
 ],
)
