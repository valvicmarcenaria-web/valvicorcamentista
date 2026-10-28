# -*- coding: utf-8 -*-
"""ICA · BANHO MASTER — levantamento peça por peça  [28/10/2026]

páginas 166 a 176 · três detalhamentos, três itens, duas folhas de detalhe.

⭐ UMA COR APARENTE SÓ: Carvalho Brun — Duratex, nas ripas, nas frentes
  ripadas e no nicho inteiro. A caixaria do armário vai em Branco TX, que
  é o padrão da casa, porque ela não aparece: o móvel é fechado por quatro
  portas e coberto por uma bancada de quartzo.

⭐⭐ DUAS RIPAS DIFERENTES NO MESMO BANHEIRO, e confundi-las custaria caro:
  · a do DET 01 tem 10 × 5 de seção e 300 de altura — são QUATRO montantes
    soltos na ELEVAÇÃO 01, que dividem a parede de 360 em 100 + 80 + 60 + 80;
  · a da frente do armário é fina, ripa de 2 com vão de 1 sobre painel de
    base, e são 21 ripas em cada uma das quatro portas de 62.
  ⛔ A primeira é ESTRUTURA — um U de uma face e dois lados, encostado na
    parede de azulejo, que faz de quarto lado. A segunda é ACABAMENTO —
    duas camadas, como no Banho Gourmet.

⛔⛔ O PÉ-DIREITO É 300 E A PEÇA INTEIRA DÁ 273. Morde três vezes aqui: as
  quatro faces e os oito lados das ripas do DET 01, as duas laterais do
  nicho, e o painel de 70 × 300 do nicho — esse último nem rebaixado
  resolve, e sai em duas faixas de 150 com a emenda atrás de uma prateleira.

⚠⚠ E FICA DE FORA O MAIOR PEDAÇO DE RIPADO DO AMBIENTE. A ELEVAÇÃO 03
  desenha a parede de 360 × 300 INTEIRA ripada, com a porta de correr do
  box e a porta de passagem embutidas no mesmo ripado — e não existe
  detalhamento nenhum dela. O Painel do executivo conta TRÊS itens neste
  ambiente, e os três têm DET. Não lancei: sem largura de ripa, sem vão e
  sem saber se é nosso ou revestimento de obra, lançar seria inventar.
  ⛔ Enquanto não responderem, o custo deste banheiro é um PISO. A dúvida
    01 põe a conta na mesa.

⛔ A BANCADA É QUARTZO CINZA ESCOVADO, 250 × 60 com 5 de espessura
  aparente. Marmoraria. As duas cubas são de apoio, em concreto.
"""
from base import P, ripado, ALT_MAX, CHAPA_C, DOBRADICA

CB15, CB18 = 'MDF Carvalho Brun 15', 'MDF Carvalho Brun 18'
EST, EST18, FUN = 'MDF Branco TX 15', 'MDF Branco TX 18', 'MDF Branco TX 6'

# ⭐⭐ ITEM ÚNICO [Jonathan, 28/10/2026]: "considere apenas um item". As
#   quatro ripas de piso a teto, o armário suspenso que morre nelas e o
#   nicho de 3 m são a mesma parede do banho master — a fábrica corta a
#   mesma chapa de Carvalho Brun para os três e o montador sobe os três
#   juntos. ⛔ Cada peça guarda o DET de origem no nome.
I = 'DET 01 a 03 Conjunto do banho master'
I1 = I2 = I3 = I

# ⭐ 21 ripas de 2 com vão de 1 em cada porta de 62 — é o que o desenho em
#   1/20 mede: dezenove vãos escuros em 58 cm de frente, passo de 3.
N_RIPA, N_PORTA = 21, 4

BANHOMASTER = [
 # ══ ITEM 01 · RIPAS — quatro montantes de 10 × 5 × 300 ═══════════════
 #  DET. 01 VISTA FRONTAL  10 de largura × 300 de altura
 #  DET. 01 PERSPECTIVA    10 × 5 de seção
 #  ELEVAÇÃO 01            100 + 10 + 80 + 10 + 60 + 10 + 80 + 10 = 360
 #  ⭐ seção 10 × 5 em MDF = U encostado na parede: UMA face de 10 e dois
 #    lados de 3,5 · a parede é o quarto lado, e ela é de azulejo
 P('Face de 10 · DET 01', I1, 300, 10, 4, CB15, (2, 0),
   '⭐ uma face por ripa, quatro ripas · as duas arestas verticais de cada '
   'face são o canto que aparece, e são 3 m cada · ⛔ 300 de altura'),
 P('Lado de 3,5 · DET 01', I1, 300, 3.5, 8, CB15, (0, 0),
   'Os dois lados de cada U · 5 de profundidade menos a chapa de 15 mm da '
   'face = 3,5 · a aresta de trás morre na parede, sem fita · ⛔ 300'),

 # ══ ITEM 02 · ARMÁRIO COM BANCADA — 250 × 45 × 60, suspenso a 25 ═════
 #  DET. 02 VISTA FRONTAL         62 + 62 + 62 + 62 = 248 ≈ 250 · altura 45
 #  DET. 02 VISTA FRONTAL INTERNA 2 + 122 + 2 + 122 + 2 = 250
 #                                altura 19 + 2 + 19, uma prateleira por vão
 #  DET. 02 VISTA LATERAL         60 de profundidade · 5 de pedra · 12 de cuba
 #  ELEVAÇÃO 01                   25 do piso + 50 do móvel com a pedra = 75
 P('Lateral · DET 02', I2, 45, 60, 2, CB15, (1, 1),
   'Aparente: a ponta do armário morre na ripa do DET 01 e ele é SUSPENSO, '
   'com 25 de vão até o piso'),
 P('Divisória central · DET 02', I2, 45, 60, 1, EST, (1, 0),
   'A vertical que parte os 250 em dois vãos de 122'),
 P('Tampo e base · DET 02', I2, 247, 60, 2, EST, (1, 0),
   '⭐ tampo cheio, não travessa: a pedra de 250 × 60 apoia nele inteiro'),
 P('Prateleira · DET 02', I2, 122, 60, 2, EST18, (1, 0),
   '⭐ 18 mm porque o vão de 122 passa muito dos 70 da regra · uma em cada '
   'vão, que é o que a VISTA FRONTAL INTERNA desenha com 19 + 2 + 19'),
 P('Fundo · DET 02', I2, 250, 45, 1, FUN, (0, 0), 'Encaixe em rasgo'),
 P('Frente · porta ripada · base · DET 02', I2, 62, 45, 4, CB15, (2, 2),
   '⭐ o painel de base é que aparece no vão de 1 entre as ripas: sai na '
   'cor da frente, não em branco · quatro portas de giro iguais'),
 P('Ripa de 2 · DET 02', I2, 2, 45, N_RIPA*N_PORTA, CB15, (2, 2),
   f'Vão de 1 entre as ripas · {N_RIPA} ripas em 62 · quatro portas · '
   'laminada nos dois lados, que é o que o Jonathan fechou em 28/10'),
 P('Ripa de 2 · perda de serra · DET 02', I2,
   round(N_RIPA*2*N_PORTA*0.10, 1), 45, 1, CB15, (0, 0),
   '⭐ fator 1,10 da Base · a serra come chapa a cada 2 cm de ripa · ⛔ é '
   'perda, não peça: sem fita'),

 # ══ ITEM 03 · NICHOS — 70 × 300 × 10 ═════════════════════════════════
 #  DET. 03 VISTA FRONTAL  2 + 66 + 2 = 70 de largura
 #     altura 75 + 2 + 38 + 2 + 38 + 2 + 38 + 2 + 38 + 2 + 63 = 300 exato
 #     CINCO prateleiras, um LED sob cada uma
 #  DET. 03 VISTA SUPERIOR e LATERAL  10 de profundidade
 P('Painel · faixa alta · DET 03', I3, 70, 150, 1, CB15, (2, 2),
   '⛔ 70 × 300 não sai de chapa nenhuma, em orientação nenhuma: duas '
   'faixas de 150, e a emenda fica atrás de uma prateleira'),
 P('Painel · faixa baixa · DET 03', I3, 70, 150, 1, CB15, (2, 2), '—'),
 P('Lateral · DET 03', I3, 300, 10, 2, CB15, (1, 0),
   'Os dois "2" da VISTA FRONTAL · só a aresta da frente aparece, e ela '
   'tem 3 m · ⛔ 300 de altura'),
 P('Topo e base · DET 03', I3, 66, 10, 2, CB15, (1, 0), 'Aparente'),
 P('Prateleira · DET 03', I3, 66, 10, 5, CB15, (1, 0),
   '⭐ 15 mm: o vão de 66 não chega aos 70 da regra · cinco prateleiras, '
   'quatro nichos de 38 entre elas e o de 63 embaixo'),
]

# ── ferragem, declarada item a item ─────────────────────────────────────
GAVETAS = []
PORTAS  = [(I2, 'Quatro portas de giro ripadas de 45 de altura', 4, 2,
            DOBRADICA)]
BASCULAS= []
CAVA    = []
PUXADORES= []
MOLDURA = []
# ⭐ uma fita sob cada uma das cinco prateleiras · 5 × 66 cm
LED     = [(I3, 'Uma fita sob cada uma das cinco prateleiras do nicho', 3.3)]
CABIDEIROS = []
SARRAFOS= []
SUPORTES= []
ALMAS   = []
VIDRO   = []
SERRALHERIA = []
ABRE_MISTO = [I]   # conjunto de três móveis num item só
# ⭐ MESMA LEITURA DO BANHO GOURMET: a porta ripada não tem puxador nenhum
#   desenhado, e uma face ripada não aceita cava sem cortar a ripa. Quem
#   sobra é o pulsador.
OUTRAS  = [(I, 'Perfil de proteção de piso', 'O nicho de 70 apoia no chão '
            'e as quatro ripas de 10 descem até ele: 70 + 4 × 10 = 110 cm · '
            'o armário é suspenso a 25 e não entra', 1.10, 'm',
            'Perfil de proteção de piso'),
           (I2, 'Pulsador', 'Quatro portas ripadas · abre por toque, sem '
            'ferragem à vista · ⚠ a prancha não desenha puxador nenhum',
            4, 'un', 'Pulsador')]

CABECA = {
 I: ('ripas 10 × 300 × 5, quatro  ·  armário 250 × 45 × 60  ·  nicho '
     '70 × 300 × 10',
     'DET 01 quatro ripas de 10 × 5 e 300 de altura, dividindo a parede de '
     '360 em 100 + 80 + 60 + 80 ⭐ seção de 10 × 5 em MDF encostada na '
     'parede é um U: uma face de 10 e dois lados de 3,5, com o azulejo '
     'fazendo de quarto lado · DET 02 armário com bancada 250 × 45 × 60, '
     'quatro portas ripadas, SUSPENSO a 25 do piso, com pedra de quartzo '
     'em cima · DET 03 nicho 70 × 300 × 10, cinco prateleiras e um LED sob '
     'cada uma, fechando exato nos 300 · ⭐ item único [Jonathan, 28/10]: '
     'é a mesma parede e a mesma chapa'),
}

FOLHA = dict(
 aba='BANHO MASTER',
 sub='Jéssica e Michell · Projeto ICA · páginas 166 a 176 · três itens em '
     'duas folhas de detalhe · ⭐ uma cor aparente só, Carvalho Brun '
     'Duratex, e caixaria em Branco TX · ⚠ a parede ripada da ELEVAÇÃO 03 '
     'NÃO está nesta conta: não tem detalhamento · peça inteira até '
     f'{ALT_MAX:g}, que é a chapa de {CHAPA_C:g} menos o acerto de corte',
 chapa_txt={CB15: 'Carvalho Brun · Duratex · as quatro ripas do DET 01, as '
                  'frentes ripadas, as laterais do armário e o nicho inteiro',
            EST:  'Estrutura e caixaria · o padrão da Base para caixaria',
            EST18: 'Prateleiras do armário · 18 mm porque o vão é de 122',
            FUN:  'Fundos · encaixe em rasgo, sem fita'},
 nota='⛔ O FRETE ESTÁ ZERADO DE PROPÓSITO: as linhas de frete da Base não '
      'têm preço ainda. Preencher lá e elas aparecem aqui sozinhas.   '
      '⚠⚠ A PAREDE RIPADA DA ELEVAÇÃO 03 NÃO ESTÁ NESTA CONTA. São 360 × '
      '300 de parede inteira ripada, com a porta do box e a porta de '
      'passagem embutidas no mesmo ripado, e ela não tem detalhamento '
      'nenhum. O executivo conta TRÊS itens neste ambiente e os três têm '
      'DET. ⛔ Até alguém dizer se é nossa, o custo deste banheiro é um '
      'PISO — a dúvida 01 põe a conta na mesa.   '
      '⭐⭐ DUAS RIPAS DIFERENTES NO MESMO BANHEIRO: a do DET 01 tem 10 × 5 '
      'de seção e 300 de altura, e é ESTRUTURA — quatro montantes '
      'que dividem a parede de 360. A da frente do armário é fina, ripa de '
      '2 com vão de 1 sobre painel de base, e é ACABAMENTO — 84 ripas nas '
      'quatro portas.   ⛔ A BANCADA É QUARTZO CINZA ESCOVADO, 250 × 60 com '
      '5 de espessura aparente, e as duas cubas são de concreto, de apoio: '
      'é marmoraria, não marcenaria.',
 duvidas=[
  '⛔⛔ A PAREDE RIPADA DA ELEVAÇÃO 03 É NOSSA? A elevação desenha os 360 × '
  '300 da parede do box INTEIROS ripados, com a porta de correr de vidro '
  'canelado e a porta de passagem embutidas no mesmo ripado — e não existe '
  'DET nenhum dela. O executivo conta três itens neste ambiente e os três '
  'têm detalhamento, então ou a parede é revestimento de obra, ou faltou '
  'uma folha. ⚠ A conta de ordem de grandeza: descontando o nicho e os '
  'vãos das duas portas sobram uns 8 m² de ripado. Pelo mesmo método do '
  'Banho Gourmet — painel de base mais ripa, nas duas camadas — são umas '
  'quatro chapas de Carvalho Brun, R$ 2.200 de material, sem a mão de obra '
  'de ripado. ⛔ É de longe a pergunta mais cara deste ambiente.',
  'A LARGURA DA RIPA DA FRENTE DO ARMÁRIO É PREMISSA MINHA. A prancha não '
  'traz DET RIPADO como o Banho Gourmet trouxe: medi no desenho em 1/20 e '
  'contei dezenove vãos em 58 cm de frente, o que dá passo de 3 — ripa de '
  '2 com vão de 1, 21 ripas por porta. ⚠ Se forem ripa de 3 com vão de 3, '
  'como no Banho Gourmet, caem para 11 por porta e a filetagem manual cai '
  'quase pela metade. Confirmar: são 84 ripas contra 44.',
  'A FRENTE RIPADA É SOBRE PAINEL DE BASE ou é ripa solta, vazada? Lancei '
  'as DUAS CAMADAS, como no Banho Gourmet: painel de 62 × 45 em Carvalho '
  'Brun mais as ripas por cima. ⚠ A PERSPECTIVA do DET 02 mostra a frente '
  'como superfície contínua e fechada, que é o que me fez decidir — mas a '
  'VISTA FRONTAL deixa passar luz entre algumas ripas. Se for vazada, '
  'saem 1,1 m² de painel de base e o armário fica mais barato — mas aí '
  'o interior aparece, e a caixaria não pode continuar branca.',
  'AS QUATRO PORTAS RIPADAS NÃO TÊM PUXADOR DESENHADO. ⭐ Orcei PULSADOR, '
  'R$ 100 cada, R$ 400 pelas quatro — mesma leitura do Banho Gourmet, pela '
  'mesma razão: cava cortaria a ripa e puxador aparafusado o desenho '
  'mostraria. ⚠ As alternativas: cava usinada sairia R$ 124 pelas quatro '
  'frentes de 62; Alças Traso 128, R$ 440. Decisão de desenho, e vale '
  'R$ 276 para baixo ou R$ 40 para cima.',
  'O ARMÁRIO É SUSPENSO A 25 DO PISO e tem 250 × 60 de bancada de quartzo '
  'em cima — a pedra sozinha pesa uns 90 kg. ⚠ Quem segura isso não é a '
  'marcenaria: pede mão francesa ou cantoneira estrutural chumbada na '
  'parede. A prancha não desenha nenhuma. ⛔ Não lancei serralheria: no '
  'banco suspenso do Living o senhor deu o valor fechado de R$ 2.500, e '
  'aqui ninguém deu nada. Confirmar se entra.',
  'A BANCADA FICA A 75 DO PISO — 25 de vão mais 45 de armário mais 5 de '
  'pedra. ⚠ É baixo para um lavatório: com a cuba de apoio de 12 a borda '
  'vai a 87, e o normal é 85 a 90, então fecha na borda. A ELEVAÇÃO 01 '
  'confirma os 87. Está certo, mas é bom o senhor saber que o tampo é '
  'baixo de propósito, por causa da cuba de apoio.',
  'A CAIXARIA DO ARMÁRIO SAIU EM BRANCO TX e as laterais em Carvalho Brun. '
  '⚠ As quatro portas fecham o móvel inteiro e a pedra cobre o tampo, '
  'então o branco não aparece — mas se o desenho quiser o interior na cor, '
  'são 3,2 m² que mudam de R$ 350 para R$ 550 a chapa. A VISTA FRONTAL '
  'INTERNA desenha o interior claro, que foi como li.',
  'O NICHO TEM 10 DE PROFUNDIDADE e 300 de altura, encostado na parede '
  'oeste. ⚠ Com 10 cm de base e 3 m de altura ele não para em pé sozinho: '
  'vai preso na alvenaria. A prancha não diz como. Orcei a caixa, que é a '
  'parte que é nossa.',
  'OS DOIS ESPELHOS DE 70 × 187 da ELEVAÇÃO 01 são vidraceiro. ⚠ Eles '
  'ficam entre as ripas do DET 01, encostados nelas — quem os fixa e se '
  'levam sarrafo de apoio atrás, a prancha não diz.',
  '⛔ A BASE METÁLICA DE 3 CM: aqui ela só caberia no nicho, que é a única '
  'peça que toca o chão — o armário é suspenso e as ripas do DET 01 vão de '
  'piso a teto. ⚠ São 0,7 m de rodapé. Fica para a passada única, junto '
  'com os outros ambientes.'],
 nao_marcenaria=[
  'Bancada em quartzo cinza escovado, 250 × 60 com 5 de espessura aparente',
  'Duas Cubas de Banheiro Concreto Apoio Elipse 55 cm (Lotus Florest) — Bela metais',
  'Dois espelhos de 70 × 187 da ELEVAÇÃO 01',
  'Porta de correr com vidro canelado do box e a persiana zebrada bege clara',
  'Hidromassagem 180 × 120 a definir, e o revestimento de madeira em volta dela',
  'Bacia Vogue, misturadores, chuveiro, toalheiro térmico e revestimentos',
  '⚠ A parede ripada da ELEVAÇÃO 03 — desenhada, sem detalhamento, e em aberto'],
 notas=[
  '⭐⭐ DUAS RIPAS DIFERENTES NO MESMO BANHEIRO, e trocá-las custaria caro. '
  'A do DET 01 tem 10 × 5 de seção e 300 de altura: são quatro montantes '
  'que dividem a parede de 360 em 100 + 80 + 60 + 80, e em MDF uma seção '
  'dessas, encostada na parede, é um U — uma face de 10 e dois lados de '
  '3,5, com o azulejo fazendo de quarto lado. A da frente '
  'do armário é fina, ripa de 2 com vão de 1 sobre painel de base, em duas '
  'camadas, como no Banho Gourmet. Uma é estrutura, a outra é acabamento.',
  '⭐ A SERRA COME CHAPA nas ripas finas, e isso está na conta como linha '
  'própria: o fator 1,10 da Base sobre 168 cm de ripa dá uma faixa de 16,8 '
  'cm de perda. São 84 ripas de 2 nas quatro portas, e cada uma tem quatro '
  'arestas — a filetagem delas é MANUAL, R$ 5,00, porque ripa não entra na '
  'coladeira.',
  '⛔⛔ O PÉ-DIREITO DE 300 MORDE TRÊS VEZES: as quatro faces e os oito '
  'lados das ripas do DET 01, as duas laterais do nicho, e o painel de '
  '70 × 300 do nicho. Esse último não cabe nem deitado — 70 passa dos 185 '
  'de largura útil só quando o outro lado é 300 — e sai em duas faixas de '
  '150, com a emenda escondida atrás de uma prateleira.',
  '⭐ O NICHO FECHA EXATO, o que é raro neste executivo: 75 + 2 + 38 + 2 + '
  '38 + 2 + 38 + 2 + 38 + 2 + 63 = 300, sem sobra e sem folga. Cinco '
  'prateleiras, quatro nichos de 38 e um de 63 embaixo, cada um com a sua '
  'fita de LED. São 3,3 m de LED, que é o que mais pesa no item.',
  '⚠⚠ E FICA DE FORA O MAIOR PEDAÇO DE RIPADO DO AMBIENTE. A ELEVAÇÃO 03 '
  'desenha a parede de 360 × 300 inteira ripada e não tem detalhamento '
  'nenhum. Uns 8 m², umas quatro chapas de Carvalho Brun, R$ 2.200 de '
  'material. ⛔ Não lancei, e por isso este ambiente é um PISO.'],
)
