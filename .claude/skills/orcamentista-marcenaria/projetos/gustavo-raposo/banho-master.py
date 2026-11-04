# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO · BANHEIRO SUÍTE MASTER — peça por peça  [30/10/2026]

pranchas 45, 46 e 47 · planta de layout e as quatro elevações A, B, C e D,
mais o detalhe 08 do perfil de LED embutido.

⭐⭐ QUATRO ELEVAÇÕES E **UMA** PAREDE DE MARCENARIA. A elevação A mostra a
  parede da bancada de frente; a D mostra a MESMA parede DE LADO, pelos 16
  de profundidade do armário superior e pelos 50 do inferior. B e C são o
  box e a bacia: porcelanato de cima a baixo, nada nosso.
  ⛔ A elevação D repete as três chamadas da A — armário superior, bancada,
    armário inferior — e quem lê chamada em vez de desenho compra tudo duas
    vezes. Foi o erro de R$ 1.266 da Lavanderia, e aqui ele valia o
    ambiente inteiro.

⭐ A CADEIA VERTICAL FECHA EM 275, do forro ao piso:
     30 de vão + 130 de armário superior + 38 de vão da bancada
     + 5 de Nanoglass + 52 de armário inferior + 20 de VÃO ATÉ O CHÃO
  ⭐ O gabinete é SUSPENSO: ele flutua 20 cm acima do piso. ⛔ Sem rodapé,
    sem perfil de proteção de piso — e com isso a fixação é toda na
    alvenaria, que é o que faz um gabinete de banheiro cair.

⭐ O ARMÁRIO SUPERIOR TEM 16 DE PROFUNDIDADE e três folhas de ESPELHO PRATA
  que correm. ⛔ O espelho não é nosso por acidente: aqui ele É a porta.
  São 2,15 m² de porta de espelho em alumínio, e é o item mais caro do
  banheiro.

⭐ O PERFIL DE LED É MARCENARIA, e o detalhe 08 diz isso com todas as
  letras: "Perfil de LED, modelo com abas a definir — MARCENARIA". Ele
  corre embutido por baixo do armário superior, nos 163.

⛔ FORA, e é quase tudo: a bancada em Nanoglass · as duas cubas de apoio
  50 × 40 × 13 · as torneiras e acionamentos dourados · a bacia sanitária ·
  o box de correr piso-teto · o porcelanato Anima di Marmo · os três nichos
  revestidos de 10 cm de profundidade · o chuveiro.
"""
from base import P, gaveta, DOBRADICA, CORREDICA

NT15 = 'MDF Nogueira Thar 15'
BR18, BR6 = 'MDF branco 18', 'MDF Branco TX 6'

I1 = 'ELEVAÇÃO A Armário superior com portas de espelho'
I2 = 'ELEVAÇÃO A Gabinete suspenso sob a bancada'

LARG = 163.0          # a nossa fatia da parede de 260: 95 de box + 2 + 163
VAO  = LARG - 3.0     # 160 · entre as duas laterais de 1,5
COL  = (VAO - 3.0)/3  # 52,33 · três colunas do gabinete, duas divisórias

BANHO_MASTER = [
 # ══ ITEM 01 · ARMÁRIO SUPERIOR — 163 × 130 × 16 ═══════════════════════
 P('Lateral',       I1, 130, 16, 2, NT15, (1, 0)),
 P('Tampo e base',  I1, VAO, 16, 2, NT15, (1, 0)),
 P('Prateleira',    I1, VAO, 14, 3, BR18, (1, 0),
   '⭐ Vão de 160 sem divisória nenhuma: a elevação A desenha as três '
   'prateleiras atravessando os 163 inteiros · ⛔ passa dos 120 e cada uma '
   'pede ALMA DE AÇO'),
 P('Fundo',         I1, LARG, 130, 1, BR6, (0, 0),
   'Peça única · ⛔ sem fita'),

 # ══ ITEM 02 · GABINETE SUSPENSO — 163 × 52 × 50 ═══════════════════════
 P('Lateral e divisória vertical', I2, 52, 50, 4, NT15, (1, 0),
   '⭐ Duas laterais e duas divisórias · TRÊS colunas de 52,3: giro, duas '
   'gavetas, giro'),
 P('Tampo e base',  I2, VAO, 50, 2, NT15, (1, 0),
   '⭐ Peça única de 160: cabe deitada na chapa · o tampo some sob a '
   'Nanoglass e a base é a cara de baixo do móvel, que se vê de pé'),
 P('Prateleira',    I2, COL, 48, 2, BR18, (1, 0),
   'Uma em cada coluna de giro · as "Proj. prateleira" da elevação A'),
 P('Frente de gaveta', I2, COL, 26, 2, NT15, (2, 2),
   'Puxador tipo CAVA QUADRADA de 5 × 5'),
 *gaveta(I2, COL, 45, 24, 2, 'Caixa de gaveta'),
 P('Fundo',         I2, LARG, 52, 1, BR6, (0, 0), '⛔ sem fita'),
 P('Frente · porta de giro', I2, COL, 52, 2, NT15, (2, 2),
   'Uma em cada ponta · puxador tipo CAVA QUADRADA de 5 × 5'),
]

# ⭐ (móvel, rótulo, nº de gavetas, preço do par)
# ⛔ AQUI A PRANCHA PEDE INVISÍVEL, não telescópica — e invisível É a
#   Hettich oculta. É o único ambiente da suíte master em que a chamada e a
#   regra da casa já concordam de saída.
GAVETAS = [
 (I2, 'Duas gavetas de 52,3 × 26 na coluna do meio · ⭐ a prancha pede '
      'corrediça INVISÍVEL e é o que entra: Hettich oculta', 2, CORREDICA),
]
# ⭐ (móvel, rótulo, nº de FOLHAS, dobradiças POR FOLHA, preço)
PORTAS = [
 (I2, 'Duas folhas de giro de 52,3 × 52, uma em cada ponta', 2, 2,
  DOBRADICA),
]
# ⭐ (móvel, rótulo, nº de frentes, extensão de cava em cm por frente)
CAVA = [
 (I2, 'Cava QUADRADA de 5 × 5 nas quatro frentes — duas folhas e duas '
      'gavetas · ⛔ é MENOR que a cava de 10 × 10 do resto da suíte: a '
      'prancha cota 3 de borda e 5 de recorte', 4, 5),
]
# ⭐ (móvel, rótulo, metros de perfil)
LED = [
 (I1, 'Perfil de LED com abas EMBUTIDO NA MARCENARIA por baixo do armário '
      'superior, nos 163 · ⭐ o detalhe 08 diz "Marcenaria" com todas as '
      'letras: o perfil é nosso, não do eletricista', 1.63),
]
# ⭐ (móvel, rótulo, qtd, comprimento, largura, chave)
VIDRO = [
 (I1, 'TRÊS folhas de correr em espelho prata, de 56 × 128 · ⭐ 2,15 m² · '
      'aqui o espelho não é acabamento, É A PORTA', 3, 56, 128,
  'Porta de espelho em alumínio'),
]
PUXADORES = MOLDURA = CABIDEIROS = ALMAS = BASCULAS = SERRALHERIA = []
# ⭐ (móvel, nome, rótulo, quantidade, unidade, chave)
OUTRAS = [
 (I1, 'Sistema de correr SS-150',
  '⚠ O TRILHO DAS TRÊS FOLHAS. A Base cobra a porta de espelho por m² — '
  'moldura de alumínio e espelho — e o trilho é linha separada. ⛔ Se o '
  'fornecedor entregar o kit completo, esta linha some e saem R$ 600',
  1, 'conjunto', 'Sistema de correr SS-150'),
 (I2, 'Perfil de proteção de piso',
  '⛔ NÃO ENTRA: o gabinete é SUSPENSO, flutua 20 cm acima do piso e não '
  'toca o chão em ponto nenhum. Linha a zero para que a ausência fique '
  'escrita', 0, 'm', 'Perfil de proteção de piso'),
]

CABECA = {
 I1: ('163 × 130 × 16',
      'ELEVAÇÃO A · armário de espelheira sobre a bancada, a 30 do forro · '
      'TRÊS folhas de correr em espelho prata · três prateleiras '
      'atravessando os 160 de vão · perfil de LED com abas embutido por '
      'baixo, detalhe 08 · ⛔ a elevação D é ESTE MESMO armário visto de '
      'lado, pelos 16 de profundidade'),
 I2: ('163 × 52 × 50',
      'ELEVAÇÃO A · gabinete SUSPENSO sob a bancada de Nanoglass, 20 cm '
      'acima do piso · TRÊS colunas de 52,3: porta de giro, duas gavetas, '
      'porta de giro · interno em MDF Branco · ⛔ a elevação D é ESTE '
      'MESMO gabinete visto de lado, pelos 50 de profundidade'),
}

FOLHA = dict(
 aba='BANHEIRO SUÍTE MASTER',
 sub='Gustavo Raposo · executivo Luiza Pacheco, pranchas 45, 46 e 47 · ⭐ '
     'quatro elevações e UMA parede de marcenaria: o resto é porcelanato, '
     'Nanoglass e louça',
 chapa_txt={
  NT15: 'Nogueira Thar · Linha Design · Duratex · ⭐ o mesmo padrão das '
        'portas da Rouparia · aqui ele faz o corpo dos dois armários e as '
        'quatro frentes do gabinete',
  BR18: 'Branco · as cinco prateleiras internas · ⭐ "interno em MDF '
        'Branco" é chamada da prancha, não escolha minha',
  BR6:  'Branco TX · os dois fundos',
  'MDF Branco TX 15': 'Branco TX · a caixaria das duas gavetas',
 },
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a QUANTIDADE é '
      'a célula AMARELA no fim do painel de material, e ela sai ZERO.   '
      '⭐⭐ O ITEM MAIS CARO DESTE BANHEIRO NÃO É MADEIRA: são os 2,15 m² '
      'de porta de espelho em alumínio das três folhas de correr. Num '
      'ambiente de 1,63 m de marcenaria, o espelho é quase um terço.   '
      '⭐ O GABINETE É SUSPENSO. Não há rodapé e não há perfil de piso — '
      'e a linha do perfil está declarada a ZERO justamente para dizer '
      'isso. ⛔ Em compensação, toda a carga vai para a alvenaria: é a '
      'fixação que decide se este móvel dura.   '
      '⭐ O PERFIL DE LED É NOSSO, por escrito: o detalhe 08 o nomeia '
      '"Marcenaria".',
 duvidas=[
  '⚠ AS TRÊS PRATELEIRAS DE 160 DE VÃO. A elevação A as desenha '
  'atravessando os 163 inteiros, sem divisória nenhuma. Pela regra da casa '
  'cada uma leva ALMA DE AÇO, e lancei as três. ⛔ Mas uma prateleira de '
  '160 × 14 em armário de banheiro é muito vão para pouca profundidade: '
  'vale conferir se a arquiteta não quer duas divisórias ali, que custam '
  'menos que as três barras e resolvem melhor.',
  '⚠ O TRILHO DAS PORTAS DE ESPELHO entrou como conjunto SS-150, R$ 600. '
  'A Base cobra a porta por m² — moldura de alumínio e espelho — e não diz '
  'se o trilho vem junto. ⭐ Três folhas que correm pedem duas ou três '
  'vias, e a prancha não cota nenhuma. ⛔ Se o kit vier completo, some a '
  'linha.',
  '⚠ MDF EM BANHEIRO. Todo este ambiente é MDF comum, como o resto da '
  'casa. ⛔ Banheiro de suíte com box aberto ao lado é o pior lugar da casa '
  'para MDF cru: a aresta inferior do gabinete e o fundo do armário '
  'superior são os dois pontos que incham primeiro. ⚠ Vale decidir se '
  'entra MDF hidrófugo nestes dois móveis, ou pelo menos selagem de topo '
  'nas arestas que não levam fita. Não lancei — é decisão de projeto, não '
  'de orçamento.',
  '⚠ A PROFUNDIDADE DO GABINETE saiu da elevação D: 50. A planta cota 40,5 '
  'mas na horizontal, que ali é largura e não profundidade. ⭐ Fiquei com '
  'os 50 da vista de lado, que é a vista que mede profundidade.',
  '⚠ A LARGURA DAS FOLHAS DE ESPELHO: 56 cada, para dar sobreposição nos '
  '163. ⛔ Se forem três folhas de 54,3 sem sobrepor, elas não correm — '
  'encostam. Adotei 56, que é o mínimo para a folha do meio passar por '
  'trás das outras duas.',
 ],
 nao_marcenaria=[
  '⛔ A BANCADA EM NANOGLASS. ⭐ É pedra, e pedra não é escopo da '
  'marcenaria nesta casa. ⚠ Mas ela APOIA no nosso gabinete: a medição da '
  'pedra tem de sair depois do gabinete montado, não antes.',
  '⛔ AS DUAS CUBAS DE APOIO de 50 × 40 × 13 na cor branco, as duas '
  'torneiras de mesa bica alta e os dois acionamentos de mesa redondos, '
  'todos dourados e "a definir".',
  '⛔ A BACIA SANITÁRIA e o acabamento dourado da válvula de descarga de '
  'parede.',
  '⛔ O BOX DE CORRER PISO-TETO em vidro temperado incolor, com roldanas '
  'aparentes douradas. ⭐ É vidraçaria de box, que nesta casa não vem pela '
  'marcenaria — diferente do espelho das portas do armário, que vem.',
  '⛔ O PORCELANATO Portobello Anima di Marmo Acetinado 120 × 120 de todas '
  'as paredes, e os TRÊS NICHOS revestidos nele, de 10 cm de profundidade '
  '— o de shampoo no box e os dois da parede da bacia. ⚠ Os nichos pedem '
  '"iluminação por perfil de LED com abas": esse perfil é do gesseiro ou '
  'do eletricista, não nosso. O nosso é só o do detalhe 08, por baixo do '
  'armário superior.',
 ],
 notas=[
  '⭐ SÃO 1,63 M DE PAREDE DE MARCENARIA num banheiro de 2,60 × 1,80. '
  'Pouco móvel e muito acabamento caro em volta — é um ambiente em que o '
  'orçamento da marcenaria engana: parece grande no desenho e é pequeno '
  'na conta.',
  '⭐ O ARMÁRIO SUPERIOR TEM 16 DE PROFUNDIDADE e 130 de altura. É um '
  'armário de espelheira: cabe frasco e não cabe toalha. A profundidade '
  'está cotada na elevação D e em nenhum outro lugar.',
  '⭐ A CAVA DESTE BANHEIRO É DE 5 × 5, não de 10 × 10 como a da suíte e a '
  'do closet. Mesma casa, mesma família de puxador, recorte menor — e a '
  'prancha cota os dois, 3 de borda e 5 de recorte.',
 ],
)
