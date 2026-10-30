# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO · LAVABO — levantamento peça por peça  [30/10/2026]

pranchas 25 e 26 · planta de layout, elevação A e detalhe da bancada.

⛔⛔ O QUE EU TINHA ERRADO, e o Jonathan pegou em duas linhas [30/10/2026]:
  > "no lavabo so tem espelho, nao tem armário.
  >  o espelho sao duas folhas, leia o projeto com mais atençao nas cotas."

  1. O ESPELHO SÃO DUAS FOLHAS, e eu tinha lançado UMA. A BANCADA DE 30 CORTA
     A PAREDE AO MEIO NA VERTICAL: há espelho ACIMA dela, 210 de altura, e
     espelho ABAIXO dela, 60 do chão até o fundo da bancada. No meio, nos
     30 cm da pedra, não há espelho nem painel.
  2. A ALTURA DE 300 NÃO EXISTE EM COTA NENHUMA — eu a inventei. ⭐ E o pior:
     o cabeçalho deste mesmo arquivo já trazia a cadeia certa, "90 do chão à
     bancada (60 + 30) + 210 acima + 75 até o forro = 375". Eu escrevi a
     cadeia certa e lancei a peça errada. ⛔ Cadeia conferida não é cota
     lançada: as duas têm de sair do mesmo número.
  3. E a emenda que eu anotei na caixa de dúvidas era consequência do erro:
     300 não cabe nos 273 da chapa, 210 cabe folgado. ⭐ Não há emenda.

⭐ A CADEIA VERTICAL, lida na prancha com posição (geo.py, eixo 790,6):
       75  do perfil de LED ao forro
      210  ESPELHO, folha de cima ............................. ⭐ nossa
       30  BANCADA em quartzito, com cuba esculpida ........... ⛔ pedra
       60  ESPELHO, folha de baixo ............................ ⭐ nossa
      ───
      375  pé-direito · fecha

⭐ A CADEIA HORIZONTAL (eixo 493,8): 65,5 + 65,5 = 131, a parede inteira.
      65,5 à esquerda · PAINEL EM QUARTZITO JADORE POLIDO ...... ⛔ pedra
      65,5 à direita  · ESPELHO PRATA COLADO EM PAINEL DE MDF .. ⭐ nosso
  Ao cliente é uma parede só. Ao orçamento são dois fornecedores.

⭐⭐ NÃO HÁ ARMÁRIO AQUI, e nunca houve: não há porta, gaveta, prateleira
  nem ferragem de movimento. O MDF que aparece no orçamento é o SUBSTRATO
  do espelho, e quem o pede é a própria prancha, com todas as letras:
  "Espelho prata colado em painel de MDF". ⚠ Se o senhor quiser o espelho
  colado direto no quartzito, o MDF, a fita e a filetagem saem — e o ambiente
  vira vidraçaria pura. A pergunta está na caixa de dúvidas.

⛔ FORA: o painel de quartzito · a BANCADA em Quartzito Jadore polido, com
  CUBA ESCULPIDA e bandeja removível — a cuba é talhada na própria pedra, é
  trabalho de marmorista e não existe sem ela · bacia sanitária marrom fosco
  · torneira e acionamento dourados · as duas arandelas e o perfil de LED.
"""
from base import P

BR15 = 'MDF Branco TX 15'

I1 = 'ELEVAÇÃO A Espelho da parede de 131'

LAVABO = [
 # ══ ITEM 01 · O ESPELHO, EM DUAS FOLHAS — 65,5 de largura ═════════════
 #  ⭐ O MDF aqui não aparece: ele é o SUBSTRATO do espelho, coberto de
 #    ponta a ponta. Por isso sai em Branco TX de caixaria e não num padrão
 #    de cor — seria pagar acabamento que ninguém vê.
 #  ⭐ As quatro arestas levam fita: o painel é visto de lado, entre o
 #    quartzito e o canto, e a aresta crua apareceria.
 P('Painel de apoio · folha de cima', I1, 210, 65.5, 1, BR15, (2, 2),
   '⭐ Do topo da bancada ao perfil de LED · ⭐ 210 cabe nos 273 da chapa: '
   'peça inteira, SEM EMENDA · o MDF não aparece, é substrato do espelho'),
 P('Painel de apoio · folha de baixo', I1, 60, 65.5, 1, BR15, (2, 2),
   '⭐ Do chão ao fundo da bancada · ⛔ é a folha que eu não tinha visto: a '
   'bancada de 30 corta a parede, e abaixo dela o espelho continua'),
]

# ⭐ sem gaveta, porta, báscula ou ferragem de movimento: é painel fixo.
#   ⛔⛔ NÃO HÁ ARMÁRIO NESTE AMBIENTE [Jonathan, 30/10/2026].
GAVETAS = PORTAS = BASCULAS = PUXADORES = MOLDURA = []
LED = CABIDEIROS = ALMAS = SERRALHERIA = CAVA = []
# ⭐ (móvel, rótulo, nº de folhas, comprimento, largura, chave)
#   ⛔ ESPELHO FIXO É R$ 600/m² MAIS A CHAPA — não é a porta de espelho de
#     alumínio de R$ 700/m², que é outra construção. Aqui o espelho é
#     COLADO num painel de MDF e não abre nem corre.
#   ⭐ DUAS LINHAS, UMA POR FOLHA, e de propósito: são dois cortes, dois
#     transportes e duas colagens. Somá-las numa linha só esconderia que a
#     folha de baixo existe — foi exatamente assim que ela sumiu.
VIDRO = [
 (I1, 'Folha de CIMA · acima da bancada · 65,5 × 210 = 1,38 m²', 1,
  65.5, 210, 'Espelho prata colado'),
 (I1, 'Folha de BAIXO · do chão ao fundo da bancada · 65,5 × 60 = 0,39 m²',
  1, 65.5, 60, 'Espelho prata colado'),
]
# ⭐ (móvel, nome, rótulo, quantidade, unidade, chave)
OUTRAS = [
 (I1, 'Perfil de proteção de piso', 'A folha de baixo toca o chão', 0.655,
  'm', 'Perfil de proteção de piso'),
]

CABECA = {
 I1: ('65,5 de largura · 210 acima da bancada + 60 abaixo',
      'ELEVAÇÃO A · a parede de 131 dividida ao meio na HORIZONTAL — 65,5 de '
      'quartzito, que não é nosso, e 65,5 de espelho, que é — e dividida '
      'outra vez na VERTICAL pela bancada: 210 de espelho acima dela, 30 de '
      'pedra, 60 de espelho abaixo · 75 + 210 + 30 + 60 = 375, o pé-direito'),
}

FOLHA = dict(
 aba='LAVABO',
 sub='Gustavo Raposo · executivo Luiza Pacheco, pranchas 25 e 26 · ⛔ NÃO HÁ '
     'ARMÁRIO: nem porta, nem gaveta, nem prateleira · o ambiente é o '
     'ESPELHO, em DUAS FOLHAS de 65,5 de largura — 210 acima da bancada e '
     '60 abaixo dela · a outra metade da parede é quartzito, e a bancada '
     'com cuba esculpida é do marmorista',
 chapa_txt={BR15: 'Branco TX · ⭐ o painel é SUBSTRATO do espelho e não '
                  'aparece em lugar nenhum: sai em caixaria, não em padrão '
                  'de cor — seria pagar acabamento que ninguém vê'},
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a QUANTIDADE é a '
      'célula AMARELA no fim do painel de material, e ela sai ZERO.   '
      '⛔⛔ O ESPELHO SÃO DUAS FOLHAS, e a bancada é quem as separa: 210 de '
      'altura acima dela, 60 abaixo, nenhum espelho nos 30 cm da pedra. '
      'Lançar uma folha só de 300 — como eu tinha feito — inventa uma altura '
      'que não está em cota nenhuma e some com a folha de baixo.   '
      '⭐⭐ E É O MELHOR EXEMPLO DA FRONTEIRA DO ESCOPO DA CASA. A parede de '
      '131 está dividida exatamente ao meio: 65,5 de painel em Quartzito '
      'Jadore polido, que é do marmorista, e 65,5 de espelho prata colado em '
      'painel de MDF, que é nosso. Ao cliente é uma parede só; ao orçamento '
      'são dois fornecedores, e a proposta tem de dizer qual é qual.   '
      '⛔ A CUBA É ESCULPIDA NA PRÓPRIA PEDRA, com bandeja removível. Não '
      'existe sem a bancada, não sai da nossa fábrica e não entra aqui.',
 duvidas=[
  '⚠⚠ O PAINEL DE MDF FICA OU SAI? A prancha pede, com todas as letras, '
  '"Espelho prata colado em painel de MDF", e é assim que se monta espelho '
  'de 2,10 m: colado em substrato, e o substrato preso na parede. ⛔ Mas se '
  'o senhor quiser o espelho colado DIRETO no quartzito ou na alvenaria, '
  'saem o MDF, a fita e a filetagem, e o ambiente vira vidraçaria pura. '
  '⭐ São as duas únicas linhas de marcenaria que existem aqui: a decisão '
  'muda o ambiente de dono, não só de preço.',
  '⭐ AS DUAS FOLHAS CABEM INTEIRAS NA CHAPA: 210 e 60 contra os 273 que a '
  'chapa dá. ⛔ Não há emenda em nenhuma das duas — e a emenda que eu havia '
  'anotado aqui era consequência da altura de 300 que eu tinha inventado.',
  '⚠ ESPELHO DE 2,10 m COLADO precisa de fita dupla-face estrutural e de '
  'película de segurança por trás — se quebrar, não cai em caco. Lancei o '
  'espelho prata a R$ 600/m², que é o preço da casa para o colado, e NÃO os '
  'R$ 700 da porta de alumínio, que é outra construção. ⛔ Confirmar se a '
  'película está no preço do vidraceiro ou se é linha à parte.',
  '⚠ A PRANCHA NÃO DIZ A COR DO MDF do painel. Lancei Branco TX porque o '
  'espelho o cobre inteiro. ⛔ Se sobrar borda aparente em algum lado, ela '
  'precisa ser de um padrão que converse com o quartzito ao lado.'],
 nao_marcenaria=[
  'Painel em Quartzito Jadore polido — a outra metade da parede',
  'Bancada em Quartzito Jadore polido com CUBA ESCULPIDA na própria pedra e '
  'bandeja removível',
  'Bacia sanitária na cor marrom fosco',
  'Torneira de mesa bica alta e acionamento redondo, na cor dourado',
  'As duas arandelas e o perfil de LED com abas'],
 notas=[
  '⭐ NENHUM ARMÁRIO, NENHUMA FERRAGEM DE MOVIMENTO. O ambiente inteiro são '
  'duas folhas de espelho sobre dois painéis de MDF. É o menor item de '
  'marcenaria da casa.',
  '⚠ O CUSTO DESTE AMBIENTE É QUASE TODO ESPELHO, não chapa: 1,77 m² de '
  'espelho prata contra um terço de chapa de Branco TX.',
  '⭐ A REGRA QUE ESTE AMBIENTE DEIXA: cadeia conferida não é cota lançada. '
  'Eu havia escrito a cadeia certa — 75 + 210 + 30 + 60 — e lançado uma '
  'peça de 300 que não aparece nela. Quando a cadeia e a peça divergem, é '
  'a peça que está errada.'],
)
