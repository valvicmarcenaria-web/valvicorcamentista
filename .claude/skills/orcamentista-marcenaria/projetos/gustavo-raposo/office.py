# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO · HÓSPEDES / OFFICE — peça por peça  [30/10/2026]

pranchas 37 e 38 · planta de layout, elevação A e detalhe 07.

⭐⭐⭐ UM ÚNICO ITEM: o PAINEL MUXARABI de 444 × 271, em MDF Nogueira
  Caiena, Linha Design, Duratex.

⛔⛔⛔ E ELE NÃO É UM PAINEL FURADO — É UMA GRADE DE RÉGUAS ENCAIXADAS
  [Jonathan, 30/10/2026, com duas fotos da peça real]:
  > "no home office, o painel de muxarabi, calcule como se fosse reguas de
  >  5cm de largura fazendo encaixes entre entre elas conforme imagens"
  > "a filetagem sera manual"

  ⭐ O que as fotos mostram: réguas com RASGOS retangulares abertos numa
    aresta, espaçados, e duas réguas cruzando pelo rasgo — ENCAIXE
    MEIA-MADEIRA. Cada régua perde metade da largura no cruzamento, e as
    duas ficam niveladas. É marcenaria de grade, não usinagem de painel.

  ⛔⛔ EU TINHA LANÇADO O AVESSO: um painel INTEIRO de 18 mm com 3.450
    furos quadrados abertos na router — 531 metros de corte, e tudo isso a
    ZERO porque a Base não tem a linha. O ambiente inteiro era um piso.
    ⭐ A diferença não é de preço, é de PROCESSO: painel furado é máquina;
      grade de régua é corte, entalhe e montagem. São fábricas diferentes.

⭐⭐ AS DUAS MEDIDAS FECHAM, e é isso que prova a leitura:
     a régua tem 5 cm de LARGURA ....... vira a PROFUNDIDADE do painel
     a chapa tem 1,8 cm de ESPESSURA ... é a "ripa de 2 cm" do detalhe 07
  ⛔ Não são duas informações que brigam: são a mesma peça vista de dois
    lados. O detalhe cota o que se vê de frente; o senhor deu o que se vê
    de lado. Por isso o módulo do detalhe 07 continua valendo.

⭐ A CONTA DA GRADE:
     módulo ........ 5,9 na horizontal (2,0 de ripa + 3,9 de furo)
                     5,8 na vertical   (2,0 de ripa + 3,8 de furo)
     verticais ..... (444 + 3,9) / 5,9 = 76 réguas de 271
     horizontais ... (271 + 3,8) / 5,8 = 47 réguas de 444
     cruzamentos ... 76 × 47 = 3.572
     encaixes ...... 3.572 × 2 = 7.144  (um em cada régua do cruzamento)

⛔ A RÉGUA HORIZONTAL DE 444 NÃO CABE NA CHAPA de 275. Sai em DUAS de 222.
  ⭐ E a emenda tem onde se esconder: ela cai DENTRO de um encaixe de régua
    vertical, que é o único lugar do painel onde uma junta não aparece.

⛔ FORA: a estante Cambota da Lider (138 × 40 × 190) · a mesa · as mesas
  laterais · o sofá-cama · o tapete orgânico 180 × 300 · as duas arandelas.
"""
from base import P

NC18 = 'MDF Nogueira Caiena 18'

I1 = 'ELEVAÇÃO A Painel muxarabi em grade de réguas'

# ── a grade, em centímetros ─────────────────────────────────────────────
LARG, ALT = 444.0, 271.0
REGUA   = 5.0                      # ⭐ largura da régua = profundidade do painel
ESP     = 1.8                      # a espessura da chapa = a "ripa" do detalhe
FURO_C, FURO_L = 3.9, 3.8          # o vão do detalhe 07
MOD_C, MOD_L = ESP + FURO_C + 0.2, ESP + FURO_L + 0.2   # 5,9 e 5,8
N_VERT = round((LARG + FURO_C) / MOD_C)
N_HORZ = round((ALT  + FURO_L) / MOD_L)
N_CRUZ = N_VERT * N_HORZ
N_ENC  = N_CRUZ * 2
# ⭐ o rasgo é 2,0 de largura por 2,5 de fundo — metade dos 5 cm da régua
M_ENTALHE = round(N_ENC * (2.5 + ESP + 2.5) / 100, 1)
MEIA = LARG / 2                    # 222 · a régua horizontal parte em duas
# ⛔ O PONTO É DO PYTHON, A VÍRGULA É DO ORÇAMENTO. ':g' escrevia "5.9" na
#   aba, e quem lê a planilha lê em português.
def vg(x): return f'{x:g}'.replace('.', ',')

OFFICE = [
 # ══ ITEM 01 · PAINEL MUXARABI EM GRADE — 444 × 271 × 5 ════════════════
 # ⭐ fita=(1, 2): UMA aresta longa — a que fica de frente — mais as duas
 #   pontas. A outra aresta longa encosta na parede e não se vê.
 P('Régua vertical', I1, ALT, REGUA, N_VERT, NC18, (1, 2),
   f'⭐ {N_VERT} réguas de {vg(ALT)} × {vg(REGUA)}, uma a cada {vg(MOD_C)} cm · '
   f'cabem inteiras nos 273 da chapa · cada uma leva {N_HORZ} encaixes, '
   f'um por régua horizontal que a cruza · ⛔ filetagem MANUAL: régua de '
   f'5 cm tomba na mesa da coladeira'),
 P('Régua horizontal', I1, MEIA, REGUA, N_HORZ * 2, NC18, (1, 2),
   f'⛔ {N_HORZ} réguas de {vg(LARG)} viram {N_HORZ * 2} peças de {vg(MEIA)}: '
   f'{vg(LARG)} não cabe nos 275 da chapa · ⭐ a emenda cai DENTRO de um '
   f'encaixe de régua vertical, o único lugar do painel onde uma junta não '
   f'aparece · cada régua inteira leva {N_VERT} encaixes'),
]

GAVETAS = PORTAS = BASCULAS = PUXADORES = MOLDURA = []
LED = CABIDEIROS = ALMAS = VIDRO = SERRALHERIA = CAVA = []
# ⭐ (móvel, nome, rótulo, quantidade, unidade, chave)
OUTRAS = [
 (I1, 'Usinagem de encaixe meia-madeira',
  f'⭐ {N_CRUZ} cruzamentos × 2 = {N_ENC} encaixes · rasgo de {vg(ESP)} de '
  f'largura por 2,5 de fundo, metade da régua · {vg(M_ENTALHE)} metros de '
  'corte ao todo · ⭐ mas o rasgo se faz com as réguas EMPILHADAS, várias '
  'de uma vez — não é o mesmo serviço que furar painel um furo por vez · '
  '⛔ A COTAR: a Base não tem a linha e ela sai ZERO',
  N_ENC, 'encaixe', 'Usinagem de encaixe meia-madeira'),
 (I1, 'Perfil de proteção de piso',
  'O painel de 444 corre ao longo da parede e toca o chão', 4.44, 'm',
  'Perfil de proteção de piso'),
]

CABECA = {
 I1: (f'444 × 271 × {vg(REGUA)} · {N_VERT} × {N_HORZ} réguas',
      f'ELEVAÇÃO A e DETALHE 07 · GRADE DE RÉGUAS de {vg(REGUA)} cm de '
      f'largura encaixadas em meia-madeira, não painel furado · {N_VERT} '
      f'réguas verticais de {vg(ALT)} por {N_HORZ} horizontais de {vg(LARG)}, '
      f'módulo {vg(MOD_C)} × {vg(MOD_L)} · {N_ENC} encaixes · ⭐ a régua de '
      f'{vg(REGUA)} é a PROFUNDIDADE do painel, e a espessura de {vg(ESP)} é a '
      '"ripa de 2 cm" que o detalhe cota de frente'),
}

FOLHA = dict(
 aba='HÓSPEDES / OFFICE',
 sub='Gustavo Raposo · executivo Luiza Pacheco, pranchas 37 e 38 · ⭐⭐⭐ UM '
     'ÚNICO item: o painel muxarabi de 444 × 271, em GRADE DE RÉGUAS de 5 '
     f'cm encaixadas em meia-madeira — {N_VERT} verticais por {N_HORZ} '
     f'horizontais, {N_ENC} encaixes · filetagem MANUAL',
 chapa_txt={NC18: 'Nogueira Caiena · Linha Design · Duratex · as réguas '
                  '⭐ 18 mm, e a espessura é o que se vê de frente: é ela '
                  'a "ripa de 2 cm" do detalhe 07'},
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a QUANTIDADE é a '
      'célula AMARELA no fim do painel de material, e ela sai ZERO.   '
      '⭐⭐⭐ O MUXARABI É UMA GRADE DE RÉGUAS ENCAIXADAS, não um painel '
      'furado [Jonathan, 30/10/2026, com foto da peça]. Réguas de 5 cm de '
      'largura, com rasgo retangular aberto numa aresta, cruzando umas nas '
      'outras em MEIA-MADEIRA: cada uma perde metade da largura no '
      'cruzamento e as duas ficam niveladas.   '
      '⛔⛔ EU TINHA LANÇADO O AVESSO — um painel inteiro com 3.450 furos '
      'quadrados abertos na router, 531 metros de corte, e tudo a ZERO. A '
      'diferença não é de preço, é de PROCESSO: painel furado é máquina; '
      'grade de régua é corte, entalhe e montagem.   '
      '⭐⭐ E AS DUAS MEDIDAS FECHAM: a régua tem 5 cm de LARGURA, que vira '
      'a PROFUNDIDADE do painel, e a chapa tem 1,8 cm de ESPESSURA, que é a '
      '"ripa de 2 cm" do detalhe 07. Não são duas informações que brigam — '
      'são a mesma peça vista de dois lados.   '
      f'⭐ A FILETAGEM É MANUAL nas {N_VERT + N_HORZ * 2} réguas, e é '
      'decisão do senhor: régua de 5 cm de largura tomba na mesa da '
      'coladeira. R$ 5,00 o metro contra R$ 2,50 da automática.',
 duvidas=[
  f'⛔⛔ OS {N_ENC} ENCAIXES SAEM ZERO, e é o único zero que sobrou neste '
  'ambiente — a chapa, a fita e a filetagem agora têm preço de verdade. '
  '⭐ E agora dá para cotar: o rasgo se faz com as réguas EMPILHADAS, '
  'várias de uma vez, não uma por uma. Cronometrar UM pacote de réguas na '
  'fábrica dá o preço do encaixe, e a casa ganha uma linha que serve em '
  'todo muxarabi, grade e colmeia daqui para frente.',
  f'⚠ A RÉGUA DE {vg(REGUA)} CM É A PROFUNDIDADE DO PAINEL, e foi assim que '
  'eu li: com 5 cm de fundo e furo de 3,9, o muxarabi filtra a vista em vez '
  'de deixar ver através — que é o que um muxarabi faz. ⛔ Se os 5 cm forem '
  'a largura APARENTE da régua, vista de frente, então a grade é outra: o '
  'módulo cresce, o número de réguas cai quase à metade e o painel fica com '
  '1,8 cm de fundo. ⭐ Uma linha sua resolve.',
  f'⚠⚠ O PAINEL SE SEGURA? A grade de {N_VERT} × {N_HORZ} réguas '
  'encaixadas é bem mais rígida que o painel vazado que eu tinha lançado — '
  'o encaixe meia-madeira trava os dois sentidos. ⛔ Mas 4,44 × 2,71 m é '
  'muito pano, e a prancha não diz como ele fixa: moldura perimetral, '
  'aparafusado em sarrafeado, ou autoportante. ⭐ É o que decide se a peça '
  'chega inteira na obra — e também se ela se monta na fábrica ou no local.',
  f'⚠ A FILETAGEM FOI LANÇADA NUMA ARESTA LONGA SÓ, a que fica de frente, '
  'mais as duas pontas de cada régua. ⛔ Se o painel for divisória e se ver '
  'dos DOIS lados, a filetagem e a fita dobram — são mais de 400 metros de '
  'cada, e isso é dinheiro de verdade. Conferir se ele encosta na parede.',
  f'⚠ A ALTURA DE {vg(ALT)} veio da cadeia vertical da elevação. A planta '
  'cota 275 de pé-direito na circulação; se o painel for do chão ao forro, '
  'as réguas verticais passam dos 273 da chapa e cada uma vira duas. '
  'Conferir na medição técnica.'],
 nao_marcenaria=[
  'Estante Cambota, Lider — 138 × 40 × 190, móvel de compra',
  'Mesa, mesas laterais e sofá-cama',
  'Tapete orgânico 180 × 300',
  'As duas arandelas'],
 notas=[
  '⭐⭐⭐ UM ITEM SÓ, E ELE É O AMBIENTE. Não há armário, porta, gaveta nem '
  'ferragem: o Hóspedes/Office é um painel. Mas é o mais trabalhoso da '
  'casa, e agora dá para dizer POR QUE: não é a máquina, são as '
  f'{N_VERT + N_HORZ * 2} réguas, os {N_ENC} encaixes e a montagem.',
  '⭐ A GRADE GASTA MAIS CHAPA QUE O PAINEL, e é contra a intuição: o '
  'painel furado media 12 m² de face e virava 43% serragem; a grade mede '
  'mais de 20 m² de chapa, porque cada régua tem 5 cm de fundo e as duas '
  'direções se somam. ⛔ Em compensação não há vazado a fazer, e o que '
  'sobra da chapa são tiras, que se aproveitam.',
  '⚠ A FILETAGEM MANUAL É O SEGUNDO MAIOR CUSTO DO AMBIENTE, atrás só da '
  'chapa. São mais de 400 metros de aresta à mão, a R$ 5,00. ⭐ É o preço '
  'de um painel que se vê de perto: a aresta da régua é a cara do móvel.'],
)
