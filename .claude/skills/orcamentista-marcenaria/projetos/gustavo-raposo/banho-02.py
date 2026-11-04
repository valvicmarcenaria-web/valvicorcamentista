# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO · BANHEIRO SUÍTE 02 FILHAS — peça por peça  [30/10/2026]

pranchas 63, 64 e 65 · planta de layout e as quatro elevações A, B, C e D.

⭐⭐ É O GÊMEO DO BANHEIRO DA SUÍTE 01, e só muda em três coisas: a chapa é
  MDF PINOLE em vez de Azul Secreto, o gabinete tem 150 em vez de 135, e as
  três colunas aqui são IGUAIS — 48 cada — em vez de uma de 40 e duas de
  44,5. Tudo o mais é a mesma receita: suspenso a 20 do chão, bancada de
  Nanoglass em cima, duas gavetas e duas portas de giro, cava quadrada de
  5 × 5 e interno em MDF Branco.

⛔⛔ E O NICHO DA ELEVAÇÃO B TAMBÉM NÃO É NOSSO: rasgo na alvenaria
  revestido de porcelanato Ceusa Confete PK, com PRATELEIRAS EM NANOGLASS
  e perfil de LED previsto. Pedra não é escopo da marcenaria.

⭐ A CADEIA VERTICAL FECHA EM 275: 198 de parede + 5 de Nanoglass + 52 de
  gabinete + 20 de VÃO ATÉ O CHÃO.

⛔ FORA: a bancada em Nanoglass · a cuba · a torneira e o acionamento
  dourados · a bacia · o box de correr · os porcelanatos · o nicho com suas
  prateleiras de pedra · e o ESPELHO de 75 × 110 com moldura dourada, que é
  peça de compra.
"""
from base import P, gaveta, DOBRADICA, CORREDICA

PI15 = 'MDF Pinole 15'
BR18, BR6 = 'MDF branco 18', 'MDF Branco TX 6'

I1 = 'ELEVAÇÃO A Gabinete suspenso sob a bancada'

LARG, ALT, PROF = 150.0, 52.0, 50.0
COL = (LARG - 6.0)/3        # 48 · três colunas iguais, duas laterais e
                            #   duas divisórias de 1,5

BANHO_02 = [
 P('Lateral e divisória vertical', I1, ALT, PROF, 4, PI15, (1, 0),
   '⭐ Duas laterais e duas divisórias · TRÊS colunas IGUAIS de 48 — a '
   'diferença para o banheiro da suíte 01, onde a coluna de gaveta é mais '
   'estreita que as de porta'),
 P('Tampo e base', I1, LARG - 3, PROF, 2, PI15, (1, 0),
   '⭐ Peça única de 147 · a base é a cara de baixo do móvel, que se vê de '
   'pé porque ele flutua'),
 P('Prateleira', I1, COL, 48, 2, BR18, (1, 0),
   'Uma em cada coluna de porta · as "Proj. prateleira" da elevação A'),
 P('Frente de gaveta', I1, COL, 26, 2, PI15, (2, 2),
   'Puxador tipo CAVA QUADRADA de 5 × 5, a 3 da borda'),
 *gaveta(I1, COL, 45, 24, 2, 'Caixa de gaveta'),
 P('Fundo', I1, LARG, ALT, 1, BR6, (0, 0), '⛔ sem fita'),
 P('Frente · porta de giro', I1, COL, ALT, 2, PI15, (2, 2),
   'Duas folhas de 48 × 52 · puxador tipo CAVA QUADRADA de 5 × 5'),
]

GAVETAS = [
 (I1, 'Duas gavetas de 48 × 26 · ⭐ corrediça INVISÍVEL na prancha, que já '
      'é a Hettich oculta da casa', 2, CORREDICA),
]
PORTAS = [
 (I1, 'Duas folhas de giro de 48 × 52', 2, 2, DOBRADICA),
]
CAVA = [
 (I1, 'Cava QUADRADA de 5 × 5 nas quatro frentes — duas gavetas e duas '
      'folhas', 4, 5),
]
LED = VIDRO = PUXADORES = MOLDURA = CABIDEIROS = ALMAS = []
BASCULAS = SERRALHERIA = []
OUTRAS = [
 (I1, 'Perfil de proteção de piso',
  '⛔ NÃO ENTRA: o gabinete é SUSPENSO, flutua 20 cm acima do piso. Linha '
  'a zero para que a ausência fique escrita', 0, 'm',
  'Perfil de proteção de piso'),
]

CABECA = {
 I1: ('150 × 52 × 50',
      'ELEVAÇÃO A · gabinete SUSPENSO sob a bancada de Nanoglass, 20 cm '
      'acima do piso · TRÊS colunas iguais de 48: duas gavetas numa e uma '
      'porta de giro em cada uma das outras · MDF Pinole, Linha Essencial, '
      'interno em MDF Branco · ⛔ a elevação D é ESTE MESMO gabinete visto '
      'de lado'),
}

FOLHA = dict(
 aba='BANHEIRO SUÍTE 02 FILHAS',
 sub='Gustavo Raposo · executivo Luiza Pacheco, pranchas 63, 64 e 65 · ⭐ '
     'o gêmeo do banheiro da suíte 01, em MDF Pinole e 15 cm mais largo',
 chapa_txt={
  PI15: 'Pinole · Linha Essencial · Duratex · ⭐ o único ambiente da casa '
        'neste padrão · o corpo do gabinete e as quatro frentes',
  BR18: 'Branco · as duas prateleiras internas · "interno em MDF Branco" é '
        'chamada da prancha',
  BR6:  'Branco TX · o fundo',
  'MDF Branco TX 15': 'Branco TX · a caixaria das duas gavetas',
 },
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a QUANTIDADE é '
      'a célula AMARELA no fim do painel de material, e ela sai ZERO.   '
      '⭐⭐ É O GÊMEO DO BANHEIRO DA SUÍTE 01. Mesma receita, outra cor e '
      '15 cm a mais — e as três colunas aqui são iguais. ⛔ Fabricar os '
      'dois juntos economiza montagem, mas NÃO economiza chapa: Pinole e '
      'Azul Secreto são duas compras separadas, cada uma com o seu '
      'arredondamento.   '
      '⛔ O NICHO DA ELEVAÇÃO B PARECE ESTANTE E NÃO É NOSSO: porcelanato '
      'Ceusa Confete PK com prateleiras de NANOGLASS.   '
      '⭐ O GABINETE É SUSPENSO: sem rodapé e sem perfil de piso, e a '
      'linha do perfil está declarada a zero para dizer isso.',
 duvidas=[
  '⚠ O ESPELHO DE 75 × 110 ficou FORA, pelo mesmo motivo do banheiro da '
  'suíte 01: "cantos arredondados e MOLDURA EM DOURADO" é peça de compra, '
  'não espelho colado de marcenaria. ⭐ Se o senhor quiser que entre, são '
  '0,83 m² e cerca de R$ 500 só de espelho, mais a moldura. Uma decisão '
  'serve para os dois banheiros.',
  '⚠ A PROFUNDIDADE DE 50 veio por semelhança com os outros dois '
  'gabinetes de banheiro da casa. ⛔ Conferir na medição.',
  '⚠ AS TRÊS COLUNAS DE 48 saíram por medição no desenho — a prancha cota '
  'os 150 e não as colunas. ⭐ Aqui elas parecem iguais, ao contrário do '
  'banheiro da suíte 01, onde a de gaveta é visivelmente mais estreita.',
  '⚠ MDF EM BANHEIRO, pela terceira vez. Pinole comum, sem tratamento. ⛔ '
  'A decisão sobre MDF hidrófugo ou selagem de topo vale para os três '
  'banheiros de suíte de uma vez.',
 ],
 nao_marcenaria=[
  '⛔ O NICHO da elevação B, revestido em porcelanato Ceusa Confete PK '
  '100 × 100, com PRATELEIRAS EM NANOGLASS e perfil de LED previsto.',
  '⛔ O ESPELHO DE 75 × 110 com cantos arredondados e moldura dourada.',
  '⛔ A BANCADA EM NANOGLASS, a cuba de apoio de 50 × 40 × 13, a torneira '
  'de mesa bica alta e o acionamento redondo, dourados.',
  '⛔ A BACIA SANITÁRIA e os acabamentos de registro e de válvula de '
  'descarga.',
  '⛔ O BOX DE CORRER piso-teto em vidro temperado incolor com roldanas '
  'douradas, e o chuveiro redondo.',
  '⛔ OS PORCELANATOS: Ceusa Confete PK 100 × 100 e Portobello Anima di '
  'Marmo Acetinado 120 × 120.',
 ],
 notas=[
  '⭐ TRÊS BANHEIROS DE SUÍTE, TRÊS PADRÕES DE CHAPA: Nogueira Thar no da '
  'master, Azul Secreto no da suíte 01 e Pinole aqui. ⛔ São três compras '
  'e três arredondamentos para três móveis pequenos — é onde o '
  'aproveitamento de chapa da casa mais sofre.',
  '⭐ A CAVA DE 5 × 5 se repete nos três banheiros. O recorte pequeno é a '
  'assinatura dos banheiros desta casa; o de 10 × 10 é a dos quartos.',
  '⭐ UM MÓVEL DE 1,50 M em quatro pranchas. Como nos outros banheiros, o '
  'desenho é quase todo revestimento e louça.',
 ],
)
