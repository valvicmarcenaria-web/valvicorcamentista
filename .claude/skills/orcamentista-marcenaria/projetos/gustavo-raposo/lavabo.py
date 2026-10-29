# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO · LAVABO — levantamento peça por peça  [29/10/2026]

pranchas 25 e 26 · planta de layout, elevação A e detalhe da bancada.

⭐⭐ O LAVABO É A MELHOR ILUSTRAÇÃO DA FRONTEIRA DO ESCOPO DA CASA, porque a
  parede de 131 está dividida EXATAMENTE AO MEIO entre o que é nosso e o que
  não é:
      65,5 à esquerda · PAINEL EM QUARTZITO JADORE POLIDO ........ ⛔ pedra
      65,5 à direita  · ESPELHO PRATA COLADO EM PAINEL DE MDF .... ⭐ nosso
  Ao cliente é uma parede só. Ao orçamento são dois fornecedores.

⭐ A CADEIA VERTICAL FECHA NOS 375: 90 do chão à bancada (60 + 30) + 210 de
  painel acima + 75 até o forro.

⛔ FORA: o painel de quartzito · a BANCADA em Quartzito Jadore polido, com
  CUBA ESCULPIDA e bandeja removível — a cuba é talhada na própria pedra, é
  trabalho de marmorista e não existe sem ela · bacia sanitária marrom fosco
  · torneira e acionamento dourados · as duas arandelas.

⚠ O PAINEL TEM 300 DE ALTURA, e a chapa dá 273. Sai em duas peças com
  emenda horizontal — e emenda atrás de espelho de 3 m aparece se não for
  no lugar certo. É decisão de projeto, não de corte: fica anotada.
"""
from base import P

BR15 = 'MDF Branco TX 15'

I1 = 'ELEVAÇÃO A Painel com espelho'

LAVABO = [
 # ══ ITEM 01 · PAINEL COM ESPELHO — 65,5 × 300 ═════════════════════════
 #  ⭐ O MDF aqui não aparece: ele é o SUBSTRATO do espelho, coberto de
 #    ponta a ponta. Por isso sai em Branco TX de caixaria e não num padrão
 #    de cor — seria pagar acabamento que ninguém vê.
 P('Painel de apoio do espelho', I1, 273, 65.5, 1, BR15, (1, 1),
   '⭐ Primeira peça · ⛔ o painel tem 300 de altura e a chapa dá 273: sai '
   'em duas, com emenda horizontal · o MDF não aparece, é substrato'),
 P('Painel de apoio do espelho · complemento', I1, 27, 65.5, 1, BR15, (1, 1),
   'A segunda peça, que completa os 300'),
]

# ⭐ sem gaveta, porta, báscula ou ferragem de movimento: é painel fixo.
GAVETAS = PORTAS = BASCULAS = PUXADORES = MOLDURA = []
LED = CABIDEIROS = ALMAS = SERRALHERIA = CAVA = []
# ⭐ (móvel, rótulo, nº de folhas, comprimento, largura, chave)
#   ⛔ ESPELHO FIXO É R$ 600/m² MAIS A CHAPA — não é a porta de espelho de
#     alumínio de R$ 700/m², que é outra construção. Aqui o espelho é
#     COLADO num painel de MDF e não abre nem corre.
VIDRO = [
 (I1, 'Espelho prata colado no painel de MDF · 65,5 × 300 = 1,97 m²', 1,
  65.5, 300, 'Espelho prata colado'),
]
# ⭐ (móvel, nome, rótulo, quantidade, unidade, chave)
OUTRAS = [
 (I1, 'Perfil de proteção de piso', 'O painel de 65,5 toca o chão', 0.655,
  'm', 'Perfil de proteção de piso'),
]

CABECA = {
 I1: ('65,5 × 300',
      'ELEVAÇÃO A · a parede de 131 dividida ao meio: 65,5 de painel em '
      'quartzito, que não é nosso, e 65,5 de espelho prata colado em painel '
      'de MDF, que é · cadeia vertical 90 até a bancada + 210 de painel + '
      '75 até o forro = 375'),
}

FOLHA = dict(
 aba='LAVABO',
 sub='Gustavo Raposo · executivo Luiza Pacheco, pranchas 25 e 26 · ⭐ UM '
     'ÚNICO item de marcenaria: o painel de MDF com espelho prata colado, '
     'de 65,5 × 300 · a outra metade da parede é quartzito, e a bancada com '
     'cuba esculpida é do marmorista',
 chapa_txt={BR15: 'Branco TX · ⭐ o painel é SUBSTRATO do espelho e não '
                  'aparece em lugar nenhum: sai em caixaria, não em padrão '
                  'de cor — seria pagar acabamento que ninguém vê'},
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a QUANTIDADE é a '
      'célula AMARELA no fim do painel de material, e ela sai ZERO.   '
      '⭐⭐ É O MELHOR EXEMPLO DA FRONTEIRA DO ESCOPO DA CASA. A parede de '
      '131 está dividida exatamente ao meio: 65,5 de painel em Quartzito '
      'Jadore polido, que é do marmorista, e 65,5 de espelho prata colado em '
      'painel de MDF, que é nosso. Ao cliente é uma parede só; ao orçamento '
      'são dois fornecedores, e a proposta tem de dizer qual é qual.   '
      '⛔ A CUBA É ESCULPIDA NA PRÓPRIA PEDRA, com bandeja removível. Não '
      'existe sem a bancada, não sai da nossa fábrica e não entra aqui.',
 duvidas=[
  '⚠ O PAINEL TEM 300 DE ALTURA e a chapa dá 273. Lancei em duas peças, '
  '273 + 27, com emenda horizontal. ⛔ Emenda atrás de um espelho de 3 m '
  'aparece se não estiver no lugar certo — e o espelho é colado, então a '
  'emenda do substrato marca. ⭐ Vale conversar com a fábrica sobre onde '
  'pôr o corte, ou usar painel de 6 mm duplo em vez de 15.',
  'O ESPELHO VAI DO CHÃO AO FORRO, 1,97 m² colados. ⚠ Espelho colado dessa '
  'altura precisa de fita dupla-face estrutural e de película de segurança '
  'por trás — se quebrar, não cai em caco. Lancei o espelho prata a '
  'R$ 600/m², que é o preço da casa para o colado, e NÃO os R$ 700 da porta '
  'de alumínio, que é outra construção.',
  '⚠ A PRANCHA NÃO DIZ A COR DO MDF do painel. Lancei Branco TX porque o '
  'espelho o cobre inteiro. ⛔ Se sobrar borda aparente em algum lado, ela '
  'precisa ser de um padrão que converse com o quartzito ao lado.'],
 nao_marcenaria=[
  'Painel em Quartzito Jadore polido — a outra metade da parede',
  'Bancada em Quartzito Jadore polido com CUBA ESCULPIDA na própria pedra e '
  'bandeja removível',
  'Bacia sanitária na cor marrom fosco',
  'Torneira de mesa bica alta e acionamento redondo, na cor dourado',
  'As duas arandelas e o perfil de LED'],
 notas=[
  '⭐ UM ITEM SÓ, e mesmo assim o ambiente ensina a regra da casa: espelho '
  'que está NA marcenaria é nosso, pedra nunca é. Aqui os dois estão lado a '
  'lado na mesma parede.',
  '⚠ O CUSTO DESTE AMBIENTE É QUASE TODO ESPELHO, não chapa: 1,97 m² de '
  'espelho prata contra meia chapa de Branco TX.'],
)
