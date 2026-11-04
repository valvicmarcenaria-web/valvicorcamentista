# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO · ANEXO BANHEIRO SUÍTE HÓSPEDES — peça por peça [30/10]

pranchas 69 e 70 · planta de layout, elevação A e elevação B.

⭐ UM GABINETE DE 44, e é o MENOR MÓVEL DO PROJETO INTEIRO. Duas folhas de
  giro de 21 cada sob uma bancada de Nanoglass, suspenso 20 cm do chão.

⛔ PÉ-DIREITO DE 260, como toda a suíte de hóspedes: 183 de parede + 5 de
  Nanoglass + 52 de gabinete + 20 de vão até o chão.

⛔ FORA: a bancada em Nanoglass · a cuba redonda de 30 · a torneira inox ·
  a bacia · o box de porta de giro com estrutura inox · o porcelanato · o
  nicho revestido com perfil de LED · e o ESPELHO de 35 × 85 com moldura,
  que é peça de compra.
"""
from base import P, DOBRADICA

NT15 = 'MDF Nogueira Thar 15'
BR18, BR6 = 'MDF branco 18', 'MDF Branco TX 6'

I1 = 'ELEVAÇÃO B Gabinete suspenso sob a bancada'

LARG, ALT, PROF = 44.0, 52.0, 40.0
COL = (LARG - 3.0)/2        # 20,5 · duas folhas, sem divisória no meio

BANHO_HOSPEDES = [
 P('Lateral', I1, ALT, PROF, 2, NT15, (1, 0)),
 P('Tampo e base', I1, LARG - 3, PROF, 2, NT15, (1, 0),
   '⭐ A base é a cara de baixo do móvel, que se vê de pé porque ele '
   'flutua'),
 P('Prateleira', I1, LARG - 3, 38, 1, BR18, (1, 0),
   'A "Proj. prat." da elevação B, atravessando os 41 de vão'),
 P('Fundo', I1, LARG, ALT, 1, BR6, (0, 0), '⛔ sem fita'),
 P('Frente · porta de giro', I1, COL, ALT, 2, NT15, (2, 2),
   '⭐ Duas folhas de 20,5 × 52 · ⛔ é a folha mais estreita da casa · '
   'puxador tipo CAVA QUADRADA de 5 × 5'),
]

PORTAS = [(I1, 'Duas folhas de giro de 20,5 × 52', 2, 2, DOBRADICA)]
CAVA = [(I1, 'Cava QUADRADA de 5 × 5 nas duas folhas', 2, 5)]
GAVETAS = LED = VIDRO = PUXADORES = MOLDURA = CABIDEIROS = ALMAS = []
BASCULAS = SERRALHERIA = []
OUTRAS = [
 (I1, 'Perfil de proteção de piso',
  '⛔ NÃO ENTRA: o gabinete é SUSPENSO, flutua 20 cm acima do piso. Linha '
  'a zero para que a ausência fique escrita', 0, 'm',
  'Perfil de proteção de piso'),
]

CABECA = {
 I1: ('44 × 52 × 40',
      'ELEVAÇÃO B · o MENOR móvel do projeto · gabinete SUSPENSO sob a '
      'bancada de Nanoglass, 20 cm acima do piso · duas folhas de giro de '
      '20,5 e uma prateleira · MDF Nogueira Thar, interno em MDF Branco · '
      '⛔ pé-direito de 260: o anexo é mais baixo que a casa'),
}

FOLHA = dict(
 aba='BANHEIRO SUÍTE HÓSPEDES',
 sub='Gustavo Raposo · executivo Luiza Pacheco, pranchas 69 e 70 · ⭐ um '
     'gabinete de 44 cm e mais nada',
 chapa_txt={
  NT15: 'Nogueira Thar · Linha Design · Duratex · o corpo e as duas '
        'folhas',
  BR18: 'Branco · a única prateleira',
  BR6:  'Branco TX · o fundo',
 },
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a QUANTIDADE é '
      'a célula AMARELA no fim do painel de material, e ela sai ZERO.   '
      '⛔⛔ R$ 200 DE FRETE PARA UM MÓVEL DE 44 CM. Este ambiente é o '
      'exemplo mais claro da casa de por que o frete tem de ser decidido '
      'por VIAGEM e não por ambiente: se o gabinete do banheiro social e o '
      'armário da suíte de hóspedes subirem no mesmo caminhão, é uma '
      'viagem e não três.   '
      '⭐ A FOLHA DE 20,5 É A MAIS ESTREITA DO PROJETO. Duas dobradiças '
      'cada, como qualquer folha abaixo de 1,20 m.',
 duvidas=[
  '⚠ A PROFUNDIDADE DE 40 não está cotada. Adotei 40 por ser um gabinete '
  'de 44 de largura — 50 o deixaria mais fundo que largo. ⛔ Conferir.',
  '⚠ O ESPELHO DE 35 × 85 ficou FORA: tem moldura "em cor a definir", é '
  'peça de compra. ⭐ Mesma decisão dos banheiros das filhas — uma '
  'resposta serve para os quatro.',
  '⚠ DUAS FOLHAS DE 20,5 OU UMA DE 41? A prancha desenha duas e rotula '
  '"Giro Giro". ⛔ Duas folhas de 20,5 custam duas dobradiças a mais e '
  'abrem pior que uma de 41 num móvel tão estreito. Vale conferir com a '
  'arquiteta.',
 ],
 nao_marcenaria=[
  '⛔ O ESPELHO de 35 × 85 com cantos arredondados e moldura em cor a '
  'definir.',
  '⛔ A BANCADA EM NANOGLASS, a cuba de apoio redonda de 30 e a torneira '
  'de mesa bica alta inox.',
  '⛔ A BACIA SANITÁRIA e o BOX de h = 190 com porta de giro em vidro '
  'temperado, estrutura em seção quadrada inox e puxador slim vertical.',
  '⛔ O PORCELANATO Portobello Anima di Marmo e o NICHO revestido de 10 cm '
  'com perfil de LED previsto.',
 ],
 notas=[
  '⭐ É O AMBIENTE MAIS BARATO DO PROJETO. Cinco peças de chapa, duas '
  'folhas, quatro dobradiças e 10 cm de cava.',
  '⭐ O PÉ-DIREITO DO ANEXO É 260. Não muda nada neste móvel, que é '
  'suspenso e baixo, mas muda tudo no armário da suíte ao lado.',
 ],
)
