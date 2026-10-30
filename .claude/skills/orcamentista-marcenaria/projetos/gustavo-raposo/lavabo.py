# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO · LAVABO — levantamento peça por peça  [30/10/2026]

pranchas 25 e 26 · planta de layout, elevação A e detalhe da bancada.

⛔⛔⛔ O LAVABO É **APENAS O ESPELHO** [Jonathan, 30/10/2026]:
  > "o lavabo continua considerando marcenaria.
  >  é APENAS o espelho"

  NÃO HÁ MARCENARIA NESTE AMBIENTE. Nenhuma chapa, nenhuma fita, nenhuma
  filetagem, nenhum perfil. O item é VIDRAÇARIA PURA: duas folhas de
  espelho prata, cortadas, transportadas e coladas na parede.

  ⭐ A LIÇÃO, e ela é maior que este ambiente: a prancha pede "Espelho prata
    colado em painel de MDF", e eu lancei o painel porque a prancha o
    escreveu. ⛔ Mas a prancha descreve A MONTAGEM, não o CONTRATO. Quem
    executa o substrato é quem executa a parede, e o nosso escopo começa no
    espelho. ⭐⭐ O DESENHO DIZ COMO SE MONTA; QUEM DIZ O QUE É NOSSO É O
    JONATHAN. Eu havia deixado a pergunta na caixa de dúvidas e lançado o
    painel enquanto esperava — é o avesso da regra: na dúvida de escopo, o
    item fica FORA e a dúvida fica escrita. Cobrar e depois descobrir que
    não era nosso é devolver dinheiro; não cobrar e descobrir que era é
    uma linha a somar.

⛔⛔ E O ERRO ANTERIOR, que o Jonathan pegou em duas linhas, continua valendo:
  > "no lavabo so tem espelho, nao tem armário.
  >  o espelho sao duas folhas, leia o projeto com mais atençao nas cotas."

  1. O ESPELHO SÃO DUAS FOLHAS, e eu tinha lançado UMA. A BANCADA DE 30
     CORTA A PAREDE AO MEIO NA VERTICAL: há espelho ACIMA dela, 210 de
     altura, e espelho ABAIXO dela, 60 do chão até o fundo da bancada. No
     meio, nos 30 cm da pedra, não há espelho.
  2. A ALTURA DE 300 NÃO EXISTE EM COTA NENHUMA — eu a inventei. ⭐ E o pior:
     o cabeçalho deste mesmo arquivo já trazia a cadeia certa, "75 + 210 +
     30 + 60 = 375". Eu escrevi a cadeia certa e lancei a peça errada.
     ⛔ Cadeia conferida não é cota lançada: as duas têm de sair do mesmo
     número.

⭐ A CADEIA VERTICAL, lida na prancha com posição (geo.py, eixo 790,6):
       75  do perfil de LED ao forro
      210  ESPELHO, folha de cima ............................. ⭐ nosso
       30  BANCADA em quartzito, com cuba esculpida ........... ⛔ pedra
       60  ESPELHO, folha de baixo ............................ ⭐ nosso
      ───
      375  pé-direito · fecha

⭐ A CADEIA HORIZONTAL (eixo 493,8): 65,5 + 65,5 = 131, a parede inteira.
      65,5 à esquerda · PAINEL EM QUARTZITO JADORE POLIDO ...... ⛔ pedra
      65,5 à direita  · ESPELHO PRATA ......................... ⭐ nosso
  Ao cliente é uma parede só. Ao orçamento são dois fornecedores.

⛔ FORA: o painel de quartzito · O PAINEL DE MDF do espelho e tudo que vem
  com ele (fita, filetagem, perfil de piso) · a BANCADA em Quartzito Jadore
  polido, com CUBA ESCULPIDA e bandeja removível — a cuba é talhada na
  própria pedra, é trabalho de marmorista e não existe sem ela · bacia
  sanitária marrom fosco · torneira e acionamento dourados · as duas
  arandelas e o perfil de LED.
"""

I1 = 'ELEVAÇÃO A Espelho da parede de 131'

# ⛔⛔ NENHUMA PEÇA DE MDF NESTE AMBIENTE [Jonathan, 30/10/2026].
#   ⭐ E a lista vazia é informação, não omissão: o item existe, tem
#     cabeçalho, tem conta e tem total — só não tem chapa. É o único
#     ambiente da casa assim.
LAVABO = []

# ⭐ sem gaveta, porta, báscula, prateleira ou ferragem de movimento:
#   não há armário aqui, e nunca houve.
GAVETAS = PORTAS = BASCULAS = PUXADORES = MOLDURA = []
LED = CABIDEIROS = ALMAS = SERRALHERIA = CAVA = []
# ⭐ nem perfil de proteção de piso: ele protege a BASE DE MDF que encosta
#   no chão, e a base saiu com o painel.
OUTRAS = []

# ⭐ (móvel, rótulo, nº de folhas, comprimento, largura, chave)
#   ⛔ ESPELHO FIXO É R$ 600/m² — não é a porta de espelho de alumínio de
#     R$ 700/m², que é outra construção. Aqui o espelho é COLADO e não abre
#     nem corre.
#   ⭐ DUAS LINHAS, UMA POR FOLHA, e de propósito: são dois cortes, dois
#     transportes e duas colagens. Somá-las numa linha só esconderia que a
#     folha de baixo existe — foi exatamente assim que ela sumiu.
VIDRO = [
 (I1, 'Folha de CIMA · acima da bancada · 65,5 × 210 = 1,38 m²', 1,
  65.5, 210, 'Espelho prata colado'),
 (I1, 'Folha de BAIXO · do chão ao fundo da bancada · 65,5 × 60 = 0,39 m²',
  1, 65.5, 60, 'Espelho prata colado'),
]

CABECA = {
 I1: ('65,5 de largura · 210 acima da bancada + 60 abaixo',
      'ELEVAÇÃO A · ⛔ VIDRAÇARIA, SEM MARCENARIA: duas folhas de espelho '
      'prata e nada mais · a parede de 131 está dividida ao meio na '
      'HORIZONTAL — 65,5 de quartzito, que não é nosso, e 65,5 de espelho, '
      'que é — e dividida outra vez na VERTICAL pela bancada: 210 de '
      'espelho acima dela, 30 de pedra, 60 de espelho abaixo · '
      '75 + 210 + 30 + 60 = 375, o pé-direito'),
}

FOLHA = dict(
 aba='LAVABO',
 sub='Gustavo Raposo · executivo Luiza Pacheco, pranchas 25 e 26 · ⛔⛔ NÃO '
     'HÁ MARCENARIA NESTE AMBIENTE: nem armário, nem porta, nem gaveta, nem '
     'prateleira, nem painel de MDF · o item é o ESPELHO, em DUAS FOLHAS de '
     '65,5 de largura — 210 acima da bancada e 60 abaixo dela · a outra '
     'metade da parede é quartzito, e a bancada com cuba esculpida é do '
     'marmorista',
 chapa_txt={},
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a QUANTIDADE é a '
      'célula AMARELA no fim do painel de material, e ela sai ZERO.   '
      '⛔⛔ ESTE AMBIENTE NÃO TEM MARCENARIA, e é o único da casa assim. Não '
      'há chapa, fita, filetagem nem ferragem: há duas folhas de espelho '
      'prata, cortadas, transportadas e coladas. ⭐ A prancha pede "espelho '
      'colado em painel de MDF", mas o painel é da obra, não nosso — o '
      'desenho diz COMO SE MONTA; quem diz O QUE É NOSSO é a Valvic.   '
      '⛔⛔ O ESPELHO SÃO DUAS FOLHAS, e a bancada é quem as separa: 210 de '
      'altura acima dela, 60 abaixo, nenhum espelho nos 30 cm da pedra. '
      'Lançar uma folha só de 300 — como eu tinha feito — inventa uma altura '
      'que não está em cota nenhuma e some com a folha de baixo.   '
      '⭐⭐ E É O MELHOR EXEMPLO DA FRONTEIRA DO ESCOPO DA CASA. A parede de '
      '131 está dividida exatamente ao meio: 65,5 de painel em Quartzito '
      'Jadore polido, que é do marmorista, e 65,5 de espelho, que é nosso. '
      'Ao cliente é uma parede só; ao orçamento são dois fornecedores, e a '
      'proposta tem de dizer qual é qual.   '
      '⛔ A CUBA É ESCULPIDA NA PRÓPRIA PEDRA, com bandeja removível. Não '
      'existe sem a bancada, não sai da nossa fábrica e não entra aqui.',
 duvidas=[
  '⭐ O PAINEL DE MDF SAIU, e a decisão é do Jonathan [30/10/2026]: "o '
  'lavabo é APENAS o espelho". ⚠ FICA UMA COMBINAÇÃO A FAZER NA OBRA: o '
  'espelho colado precisa de substrato plano e seco — se o quartzito e a '
  'alvenaria não derem essa superfície, quem fornece o painel é a obra, e '
  'isso tem de estar dito ANTES da medição final do vidraceiro.',
  '⚠ ESPELHO DE 2,10 m COLADO precisa de fita dupla-face estrutural e de '
  'película de segurança por trás — se quebrar, não cai em caco. Lancei o '
  'espelho prata a R$ 600/m², que é o preço da casa para o colado, e NÃO os '
  'R$ 700 da porta de alumínio, que é outra construção. ⛔ Confirmar se a '
  'película está no preço do vidraceiro ou se é linha à parte.',
  '⚠ AS DUAS FOLHAS SÃO CORTE DE CHAPA DE ESPELHO, e sobra. 65,5 × 210 e '
  '65,5 × 60 saem da mesma largura — o vidraceiro pode tirar as duas da '
  'mesma chapa, e o preço por m² já supõe isso. ⛔ Se ele cobrar chapa '
  'cheia, o custo muda e a linha tem de ser recotada.',
  '⚠ O ACABAMENTO DA BORDA não está na prancha. Espelho visto de lado pede '
  'lapidação; colado de topo a topo, não pede. Lancei sem lapidação. ⛔ Se '
  'alguma das quatro bordas de cada folha ficar aparente, é serviço a '
  'somar.'],
 nao_marcenaria=[
  'Painel em Quartzito Jadore polido — a outra metade da parede',
  '⛔ O PAINEL DE MDF do espelho, e com ele a fita, a filetagem e o perfil '
  'de proteção de piso — decisão do Jonathan em 30/10: o lavabo é apenas o '
  'espelho',
  'Bancada em Quartzito Jadore polido com CUBA ESCULPIDA na própria pedra e '
  'bandeja removível',
  'Bacia sanitária na cor marrom fosco',
  'Torneira de mesa bica alta e acionamento redondo, na cor dourado',
  'As duas arandelas e o perfil de LED com abas'],
 notas=[
  '⛔⛔ O ÚNICO AMBIENTE DA CASA SEM UMA ÚNICA PEÇA DE MARCENARIA. Nenhuma '
  'chapa, nenhuma fita, nenhuma ferragem: duas folhas de espelho prata, e '
  'nada mais. ⭐ A linha de chapa não está faltando — ela não existe.',
  '⭐ O CUSTO DESTE AMBIENTE É ESPELHO PURO: 1,7685 m² a R$ 600/m². Não há '
  'um centavo de chapa para diluir.',
  '⭐ A REGRA QUE ESTE AMBIENTE DEIXA, e são duas. A primeira: cadeia '
  'conferida não é cota lançada — eu havia escrito 75 + 210 + 30 + 60 e '
  'lançado uma peça de 300 que não aparece nela. A segunda, maior: a '
  'prancha descreve A MONTAGEM, não o CONTRATO. "Colado em painel de MDF" '
  'diz como o espelho se prende, não que o painel seja nosso.'],
)
