# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO · HÓSPEDES / OFFICE — peça por peça  [29/10/2026]

pranchas 37 e 38 · planta de layout, elevação A e detalhe 07.

⭐⭐⭐ UM ÚNICO ITEM, E ELE É A USINAGEM MAIS PESADA DA CASA: o PAINEL
  MUXARABI VAZADO, 444 × 271, em MDF Nogueira Caiena, Linha Design, Duratex.

⛔⛔ MUXARABI NÃO É RIPADO, e confundir os dois erra o orçamento inteiro.
  Ripado é ripa SOLTA com vão entre elas, e se conta por ripa. O detalhe 07
  mostra outra coisa: um painel INTEIRO com FURO QUADRADO de 3,8 × 3,9 e
  ripa de 2 cm entre os furos, nos dois sentidos. O módulo é 5,9 × 5,8.
  ⭐ O que custa não é a chapa — é o METRO DE CORTE na router.

⭐ A CONTA DOS FUROS, e ela assusta:
      colunas .... 444 / 5,9 ≈ 75
      linhas ..... 271 / 5,8 ≈ 46
      furos ...... 75 × 46 = 3.450
      corte ...... 3.450 × 2 × (3,8 + 3,9) cm = 531 metros de router
  ⛔ Meio quilômetro de corte num painel só. A Base não tem a linha e ela
    sai ZERO — o custo deste ambiente é um PISO declarado.

⛔ O PAINEL SAI EM TRÊS PEÇAS, e não é escolha: 444 × 271 não cabe na chapa
  de 275 × 185 em orientação nenhuma, e nem partido ao meio cabe (222 × 271
  tem o menor lado em 222, acima dos 185). Em três, 148 × 271 entra.
  ⚠ As emendas caem entre colunas de furo, onde a ripa de 2 cm as esconde.

⚠⚠ E HÁ UMA DÚVIDA ESTRUTURAL: 43% do painel vira vazio, e o que sobra são
  ripas de 2 cm. Um painel de 4,44 × 2,71 m assim não se segura sozinho em
  MDF de 18 — ou ganha moldura perimetral, ou vai aparafusado em sarrafeado
  na parede. A prancha não diz, e isso não é detalhe: é o que decide se a
  peça chega inteira na obra.

⛔ FORA: a estante Cambota da Lider (138 × 40 × 190) · a mesa · as mesas
  laterais · o sofá-cama · o tapete orgânico 180 × 300 · as duas arandelas.
"""
from base import P

NC18 = 'MDF Nogueira Caiena 18'

I1 = 'ELEVAÇÃO A Painel muxarabi vazado'

# ── a grelha do detalhe 07, em centímetros ──────────────────────────────
FURO_C, FURO_L, RIPA = 3.9, 3.8, 2.0
LARG, ALT = 444.0, 271.0
N_COL = int(LARG // (FURO_C + RIPA))
N_LIN = int(ALT  // (FURO_L + RIPA))
N_FUROS = N_COL * N_LIN
M_CORTE = round(N_FUROS * 2 * (FURO_C + FURO_L) / 100, 1)

OFFICE = [
 # ══ ITEM 01 · PAINEL MUXARABI VAZADO — 444 × 271 ══════════════════════
 P('Painel muxarabi vazado', I1, 148, 271, 3, NC18, (2, 2),
   f'⛔ TRÊS peças de 148 × 271: o painel de 444 × 271 não cabe na chapa de '
   f'275 × 185 em orientação nenhuma, e nem partido ao meio · as emendas '
   f'caem entre colunas de furo, onde a ripa de 2 cm as esconde · ⭐ cada '
   f'peça leva {N_FUROS // 3} furos quadrados de {FURO_C:g} × {FURO_L:g}'),
]

GAVETAS = PORTAS = BASCULAS = PUXADORES = MOLDURA = []
LED = CABIDEIROS = ALMAS = VIDRO = SERRALHERIA = CAVA = []
# ⭐ (móvel, nome, rótulo, quantidade, unidade, chave)
OUTRAS = [
 (I1, 'Usinagem de muxarabi vazado',
  f'⭐ {N_FUROS} furos quadrados de {FURO_C:g} × {FURO_L:g}, com ripa de '
  f'{RIPA:g} cm entre eles · {M_CORTE:g} METROS de corte na router · ⛔ a '
  'Base não tem a linha e ela sai ZERO: o custo deste ambiente é um PISO',
  M_CORTE, 'm', 'Usinagem de muxarabi vazado'),
 (I1, 'Perfil de proteção de piso',
  'O painel de 444 corre ao longo da parede e toca o chão', 4.44, 'm',
  'Perfil de proteção de piso'),
]

CABECA = {
 I1: (f'444 × 271 · {N_FUROS} furos',
      f'ELEVAÇÃO A e DETALHE 07 · grelha de furo quadrado {FURO_C:g} × '
      f'{FURO_L:g} com ripa de {RIPA:g} cm, módulo {FURO_C + RIPA:g} × '
      f'{FURO_L + RIPA:g} · {N_COL} colunas por {N_LIN} linhas · ⛔ sai em '
      'três peças de 148, porque 444 × 271 não cabe na chapa'),
}

FOLHA = dict(
 aba='HÓSPEDES / OFFICE',
 sub='Gustavo Raposo · executivo Luiza Pacheco, pranchas 37 e 38 · ⭐⭐⭐ UM '
     'ÚNICO item, e é a usinagem mais pesada da casa: o painel muxarabi '
     f'vazado de 444 × 271, com {N_FUROS} furos quadrados e {M_CORTE:g} '
     'metros de corte na router',
 chapa_txt={NC18: 'Nogueira Caiena · Linha Design · Duratex · ⭐ 18 mm e '
                  'não 15: com 43% do painel virando vazio, o que sobra são '
                  'ripas de 2 cm, e em 15 mm elas não se sustentam'},
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a QUANTIDADE é a '
      'célula AMARELA no fim do painel de material, e ela sai ZERO.   '
      '⛔⛔ MUXARABI NÃO É RIPADO. Ripado é ripa solta com vão, e se conta '
      'por ripa. O detalhe 07 mostra um painel INTEIRO com furo quadrado de '
      f'{FURO_C:g} × {FURO_L:g} e ripa de {RIPA:g} cm entre os furos, nos '
      'dois sentidos. O que custa não é a chapa — é o metro de corte.   '
      f'⭐ E a conta assusta: {N_COL} colunas por {N_LIN} linhas dão '
      f'{N_FUROS} furos, e {M_CORTE:g} metros de router. Meio quilômetro de '
      'corte num painel só.   ⛔ A linha de usinagem sai ZERO porque a Base '
      'não a tem: o custo deste ambiente é um PISO declarado, não um preço.',
 duvidas=[
  f'⛔⛔ OS {M_CORTE:g} METROS DE USINAGEM SAEM ZERO e são o ambiente '
  'inteiro. A Base não tem linha para corte de router por metro. ⚠ Cronometrar '
  'UMA peça de 148 × 271 na fábrica resolve: multiplicando por três sai o '
  'painel, e a casa ganha uma linha que vai servir em todo projeto com '
  'vazado, ripado ou perfurado daqui para frente.',
  '⚠⚠ O PAINEL SE SEGURA? Com 43% virando vazio, o que sobra são ripas de '
  '2 cm cruzadas, num painel de 4,44 × 2,71 m. Lancei 18 mm em vez de 15 '
  'justamente por isso. ⛔ Mesmo assim, a prancha não diz como ele fixa: se '
  'vai em moldura perimetral, se vai aparafusado em sarrafeado na parede, '
  'ou se é autoportante. ⭐ Não é detalhe de acabamento — é o que decide se '
  'a peça chega inteira na obra.',
  '⚠ A EMENDA DAS TRÊS PEÇAS. Pus os cortes entre colunas de furo, onde a '
  'ripa de 2 cm os esconde. ⛔ Mas em 444 de largura, três peças de 148 dão '
  'duas emendas verticais de 2,71 m de altura, e se o módulo de 5,9 não '
  'fechar exato nos 148 a emenda cai no meio de um furo. ⭐ Vale a fábrica '
  'ajustar as três larguras para que cada corte caia em ripa cheia.',
  f'⚠ A ALTURA DE {ALT:g} veio da cadeia vertical da elevação. A planta '
  'cota 275 de pé-direito na circulação; se o painel for do chão ao forro, '
  'ele passa a 275 e não cabe nem em três peças na vertical. Conferir na '
  'medição técnica.'],
 nao_marcenaria=[
  'Estante Cambota, Lider — 138 × 40 × 190, móvel de compra',
  'Mesa, mesas laterais e sofá-cama',
  'Tapete orgânico 180 × 300',
  'As duas arandelas'],
 notas=[
  '⭐⭐⭐ UM ITEM SÓ, E ELE É O AMBIENTE. Não há armário, porta, gaveta nem '
  'ferragem: o Hóspedes/Office é um painel. Mas é o painel mais trabalhoso '
  'da casa, e o único cujo custo mora inteiro na máquina e não no material.',
  f'⭐ A CHAPA É POUCA: três peças de 148 × 271 dão 12 m², pouco mais de '
  'duas chapas. ⚠ E ainda assim 43% dela vira serragem — o vazado não '
  'devolve material, ele vira pó.',
  '⚠ ESTE É O ITEM MAIS ARRISCADO DO ORÇAMENTO INTEIRO. O preço depende de '
  'uma linha que não existe, a estrutura depende de uma definição que a '
  'prancha não dá, e a peça é grande demais para errar barato.'],
)
