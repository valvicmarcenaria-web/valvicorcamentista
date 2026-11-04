# -*- coding: utf-8 -*-
"""ICA · CLOSET MARIANA — levantamento peça por peça  [28/10/2026]

páginas 192 a 200 · dois detalhamentos, dois itens, três folhas de detalhe.

⭐⭐ É O CLOSET MASTER DE NOVO, EM MENOR: MDF Branco Diamante - Duratex do
  fechamento superior ao último fundo, armário ABERTO sem porta nenhuma,
  maleiro em cima, nicho, cabideiro, gaveta com puxador cava e sapateira
  embaixo. A cadeia vertical é a mesma em todas as colunas dos dois
  armários: 35 de fechamento + 60 de maleiro + 3 + 27 de nicho + 3, e o
  resto do pé-direito é corpo.

⛔⛔ O PÉ-DIREITO DE 300 CONTRA A PEÇA INTEIRA DE 273 morde as seis
  verticais dos dois armários, e os dois fechamentos superiores passam da
  chapa pela LARGURA: 237 cabe, 304 não — o Armário 02 sai em duas peças
  de 152.

⚠ O TÍTULO DAS PRANCHAS DIZ "SUÍTE MARIANA" em todas as folhas deste
  ambiente, mas a capa da página 192 diz CLOSET MARIANA e o Painel do
  executivo conta os dois armários aqui. É erro de carimbo, não de
  desenho — e ele se repete no Banho Mariana, cujas folhas vêm carimbadas
  como "BANHO MASTER".

⛔ O ESPELHO COM LED FRONTAL do Armário 02 é vidraceiro; o LED do
  perímetro é nosso, e são 3,8 m.
"""
from base import P, gaveta, ALT_MAX, CHAPA_C

BD18, BD15, BD6 = ('MDF Branco Diamante 18', 'MDF Branco Diamante 15',
                   'MDF Branco Diamante 6')

I1 = 'DET 01 Armário 01'
I2 = 'DET 02 Armário 02'

CLOSETMARIANA = [
 # ══ ITEM 01 · ARMÁRIO 01 — 240 × 300 × 60 ════════════════════════════
 #  VISTA FRONTAL  89 + 2 + 147 + 2 = 240 · altura 35 + 60 + 3 + 27 + 3
 #                 + corpo = 300 · embaixo 28 + 2 + 59 + 2 + 73 + 2 + 72
 #  VISTA SUPERIOR 240 × 60 · VISTA LATERAL 60, com 5 de rodapé
 #  ⭐ armário ABERTO: não há uma porta sequer no ambiente
 P('Lateral',               I1, 300, 60, 2, BD15, (1, 1),
   '⛔ 300 de altura contra 273 de peça inteira'),
 P('Divisória',             I1, 300, 60, 1, BD15, (1, 0),
   'A vertical que parte os 240 em 89 e 147 · ⛔ 300 de altura'),
 P('Fechamento superior e base', I1, 237, 60, 2, BD15, (1, 1),
   '⭐ o "fechamento superior em MDF Branco Diamante" que a prancha '
   'nomeia, e a base · 237 cabe inteiro nos 275 da chapa'),
 P('Prateleira do fechamento de 35', I1, 89, 60, 1, BD18, (1, 0)),
 P('Prateleira do fechamento de 35 · coluna de 147', I1, 147, 60, 1, BD18,
   (1, 0)),
 P('Prateleira do maleiro',  I1, 89, 60, 1, BD18, (1, 0),
   '⭐ 18 mm: o vão de 89 passa dos 70 da regra'),
 P('Prateleira do maleiro · coluna de 147', I1, 147, 60, 1, BD18, (1, 0)),
 P('Prateleira do nicho',    I1, 89, 60, 1, BD18, (1, 0)),
 P('Prateleira do nicho · coluna de 147', I1, 147, 60, 1, BD18, (1, 0)),
 P('Divisória do corpo',     I1, 110, 60, 1, BD15, (1, 0),
   'Parte a coluna de 147 nas duas de 73 e 72 dos nichos'),
 P('Prateleira do nicho de 26 · coluna de 73', I1, 73, 60, 3, BD18, (1, 0),
   'Três nichos de 26, um sobre o outro'),
 P('Prateleira do nicho de 26 · coluna de 72', I1, 72, 60, 3, BD18, (1, 0)),
 P('Divisória do bloco de baixo', I1, 115, 60, 2, BD15, (1, 0),
   'Separam as quatro colunas de 28, 59, 73 e 72 que a cadeia de baixo dá'),
 P('Sapateira',             I1, 28, 60, 4, BD18, (1, 0),
   'Quatro sapateiras fixas na coluna estreita de 28'),
 P('Frente · gavetão',      I1, 59, 40, 2, BD18, (2, 2),
   'Dois gavetões de 40 · puxador cava'),
 P('Frente · gaveta · coluna de 73', I1, 73, 20, 4, BD18, (2, 2),
   'Quatro gavetas de 20 · puxador cava'),
 P('Frente · gaveta · coluna de 72', I1, 72, 20, 4, BD18, (2, 2)),
 P('Fundo',                 I1, 240, 150, 2, BD6, (0, 0),
   '⛔ 240 × 300 não sai de uma chapa: duas peças de 150 · encaixe em '
   'rasgo, sem fita'),
 *gaveta(I1, 59, 55, 40, 2, 'Gavetão', BD15, BD6),
 *gaveta(I1, 73, 55, 20, 4, 'Gaveta de 73', BD15, BD6),
 *gaveta(I1, 72, 55, 20, 4, 'Gaveta de 72', BD15, BD6),

 # ══ ITEM 02 · ARMÁRIO 02 — 310 × 300 × 60 ════════════════════════════
 #  VISTA FRONTAL  3 + 89 + 3 + 80 + 2 + 131 + 2 = 310 · embaixo
 #                 95 + 80 + 75 + 60 = 310 · altura 35 + 60 + 3 + 27 + 3
 #  ⭐ a coluna de 80 é a PENTEADEIRA: espelho com LED em cima, uma gaveta
 #    e 77 de vão livre embaixo, para a cadeira entrar
 P('Lateral',               I2, 300, 60, 2, BD15, (1, 1),
   '⛔ 300 de altura'),
 P('Divisória',             I2, 300, 60, 2, BD15, (1, 0),
   'As duas verticais que partem os 310 em 89, 80 e 131 · ⛔ 300'),
 P('Fechamento superior e base', I2, 152, 60, 4, BD15, (1, 1),
   '⛔ 304 de corrida NÃO sai da chapa de 275: duas peças de 152 em cada, '
   'e são dois — o fechamento superior e a base'),
 P('Prateleira do fechamento de 35 · coluna de 89', I2, 89, 60, 1, BD18,
   (1, 0)),
 P('Prateleira do fechamento de 35 · coluna de 80', I2, 80, 60, 1, BD18,
   (1, 0)),
 P('Prateleira do fechamento de 35 · coluna de 131', I2, 131, 60, 1, BD18,
   (1, 0)),
 P('Prateleira do maleiro · coluna de 89', I2, 89, 60, 1, BD18, (1, 0)),
 P('Prateleira do maleiro · coluna de 80', I2, 80, 60, 1, BD18, (1, 0)),
 P('Prateleira do maleiro · coluna de 131', I2, 131, 60, 1, BD18, (1, 0)),
 P('Prateleira do nicho · coluna de 89', I2, 89, 60, 1, BD18, (1, 0)),
 P('Prateleira do nicho · coluna de 80', I2, 80, 60, 1, BD18, (1, 0)),
 P('Prateleira do nicho · coluna de 131', I2, 131, 60, 1, BD18, (1, 0)),
 P('Divisória do bloco de baixo', I2, 79, 60, 1, BD15, (1, 0),
   'Parte a coluna de 131 nas de 75, do calceiro, e 60, da sapateira'),
 P('Sapateira',             I2, 60, 60, 4, BD18, (1, 0),
   'Quatro sapateiras fixas de 19, 18, 18 e 19'),
 P('Tampo da penteadeira',  I2, 80, 60, 1, BD18, (1, 1),
   '⭐ aparente por baixo: a cadeira entra sob ele, e são 77 de vão livre'),
 P('Frente · gaveta da penteadeira', I2, 80, 15, 1, BD18, (2, 2),
   'A única gaveta deste armário · puxador cava'),
 P('Fundo',                 I2, 155, 150, 4, BD6, (0, 0),
   '⛔ 310 × 300 não sai nem de duas chapas: quatro peças de 155 × 150 · '
   'encaixe em rasgo, sem fita'),
 *gaveta(I2, 80, 55, 15, 1, 'Gaveta da penteadeira', BD15, BD6),
]

# ── ferragem, declarada item a item ─────────────────────────────────────
GAVETAS = [(I1, 'Armário 01 · dois gavetões de 40 e oito gavetas de 20', 10,
            550),
           (I2, 'Armário 02 · a gaveta da penteadeira', 1, 550)]
PORTAS  = []
BASCULAS = []
# ⭐ "puxador cava", escrito na prancha em toda frente dos dois armários
CAVA    = [(I1, 'Dois gavetões de 59', 2, 59),
           (I1, 'Quatro gavetas de 73', 4, 73),
           (I1, 'Quatro gavetas de 72', 4, 72),
           (I2, 'A gaveta da penteadeira', 1, 80)]
PUXADORES = []
MOLDURA = []
LED     = [(I2, 'Perímetro do espelho da penteadeira, 80 × 110 · '
            'iluminação frontal', 3.8)]
CABIDEIROS = [(I1, 'Cabideiro na coluna de 89 do Armário 01', 1),
              (I2, 'Cabideiro nas colunas de 89 e de 131 do Armário 02', 2)]
SARRAFOS = []
SUPORTES = []
ALMAS   = []
# ⭐ O ESPELHO ENTRA NA CONTA [Jonathan, 28/10/2026]: "Ambiente 15 - closet
#   mariana: Considerar o espelho". É o da penteadeira do Armário 02,
#   80 × 110, com os 3,8 m de LED do perímetro que já estavam na conta.
#   ⚠ A prancha não cota o espelho: a medida saiu da VISTA FRONTAL em 1/20.
VIDRO   = [(I2, 'Espelho da penteadeira do Armário 02, 80 × 110 · colado '
            'no painel de apoio, com LED no perímetro', 1, 80, 110,
            'Espelho')]
SERRALHERIA = []
OUTRAS  = [
           (I1, 'Perfil de proteção de piso', 'Armário 01 de 240', 2.4, 'm',
            'Perfil de proteção de piso'),
           (I2, 'Perfil de proteção de piso', 'Armário 02 de 310', 3.1, 'm',
            'Perfil de proteção de piso'),
           (I2, 'Calceiro deslizante', 'Na coluna de 75 do Armário 02 · '
            '⛔ sem preço na Base', 1, 'un', 'Calceiro deslizante')]

CABECA = {
 I1: ('240 × 300 × 60',
      'VISTA FRONTAL 89 + 2 + 147 + 2 = 240 · altura 35 de fechamento + 60 '
      'de maleiro + 3 + 27 de nicho + 3 e o corpo até 300 · embaixo 28 + 2 '
      '+ 59 + 2 + 73 + 2 + 72 + 2 = 240 · VISTA SUPERIOR 240 × 60 · ⭐ '
      'armário ABERTO: não há uma porta sequer neste ambiente'),
 I2: ('310 × 300 × 60',
      'VISTA FRONTAL 3 + 89 + 3 + 80 + 2 + 131 + 2 = 310 · embaixo 95 + 80 '
      '+ 75 + 60 = 310 · mesma cadeia vertical do Armário 01 · ⭐ a coluna '
      'de 80 é a PENTEADEIRA: espelho com LED frontal em cima, uma gaveta e '
      '77 de vão livre embaixo para a cadeira entrar'),
}

FOLHA = dict(
 aba='CLOSET MARIANA',
 sub='Jéssica e Michell · Projeto ICA · páginas 192 a 200 · dois itens em '
     'três folhas de detalhe · ⭐ UMA COR SÓ e ela é a mesma do Closet '
     'Master: Branco Diamante Duratex, do fechamento superior ao último '
     'fundo · armário ABERTO, sem uma porta sequer · peça inteira até '
     f'{ALT_MAX:g}, que é a chapa de {CHAPA_C:g} menos o acerto de corte',
 chapa_txt={BD18: 'Branco Diamante · Duratex · prateleiras, frentes, '
                  'sapateiras e o tampo da penteadeira',
            BD15: 'Branco Diamante · laterais, divisórias, fechamentos e as '
                  'caixas de gaveta',
            BD6:  'Branco Diamante · fundos · ⭐ sai na cor e não em branco '
                  'de caixaria, porque dentro de closet aberto tudo aparece'},
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem [Jonathan, 29/10]: '
      'a QUANTIDADE é a célula AMARELA no fim do painel de material, e ela '
      'sai ZERO. Digite quantas viagens este ambiente leva e o frete '
      'aparece aqui e no Painel.   '
      '⭐⭐ É O CLOSET MASTER DE NOVO, EM MENOR, e isso é bom para o preço: '
      'mesmo padrão, mesma cadeia vertical, mesma ferragem. Branco Diamante '
      'Duratex nos dois armários, armário ABERTO sem uma porta sequer, e a '
      'cadeia 35 de fechamento + 60 de maleiro + 3 + 27 de nicho + 3 se '
      'repete em todas as colunas dos dois.   ⛔⛔ O PÉ-DIREITO DE 300 morde '
      'as seis verticais, e o fechamento superior do Armário 02 passa da '
      'chapa pela LARGURA: 304 de corrida não sai dos 275, e ele vira duas '
      'peças de 152.   ⭐ A PENTEADEIRA É O ÚNICO MÓVEL DIFERENTE DO '
      'AMBIENTE: espelho com LED frontal, uma gaveta e 77 de vão livre para '
      'a cadeira. ⭐ O ESPELHO É NOSSO desde 28/10, e os 3,8 m de LED do '
      'perímetro também — mas a linha "Espelho" da Base não tem preço, '
      'então ele soma ZERO.   ⚠ O CARIMBO DAS FOLHAS DIZ "SUÍTE MARIANA", mas a capa da '
      'página 192 diz CLOSET MARIANA. É erro de carimbo, e ele se repete no '
      'Banho Mariana.',
 duvidas=[
  'BRANCO DIAMANTE É BRANCO OU É COR? Lancei no preço de COR — R$ 700 a '
  'chapa de 18, R$ 550 a de 15 e R$ 350 a de 6 —, exatamente como no '
  'Closet Master, porque é o mesmo padrão, e é o lado conservador. ⚠ Mas '
  'Branco Diamante é um branco texturado, irmão do Branco TX da caixaria: '
  'se a Duratex cobrar como branco (R$ 400 / 350 / 250), os dois ambientes '
  'CAEM juntos quase 40%. ⛔ É a mesma pergunta da dúvida 01 do Closet '
  'Master, e a resposta vale para os dois de uma vez.',
  'O CALCEIRO DESLIZANTE da coluna de 75 do Armário 02 não existe na Base e '
  'sai ZERO. ⚠ É o terceiro do projeto — dois no Closet Master, um aqui. '
  'Calceiro deslizante de closet custa de R$ 150 a R$ 400 a unidade. ⛔ Até '
  'existir, o custo deste armário é um PISO.',
  'A PENTEADEIRA DO ARMÁRIO 02 tem UMA gaveta só, e eu a tirei do desenho: '
  'a prancha escreve "Penteadeira com gavetas", no plural, mas desenha uma '
  'gaveta na coluna de 80 e nada mais. ⚠ Lancei uma, de 80 × 15. Se forem '
  'duas ou três, cada uma a mais custa uns R$ 180 entre frente, caixa, '
  'corrediça e cava.',
  'O ESPELHO COM LED FRONTAL da penteadeira É NOSSO desde 28/10 e entrou '
  'no levantamento — 0,88 m², mais os 3,8 m de LED do perímetro, R$ 570. '
  '⛔ A linha "Espelho" da Base segue SEM PREÇO, então o vidro soma ZERO e '
  'o custo deste ambiente é um piso. ⚠ A prancha NÃO cota o espelho: tirei '
  '80 × 110 da VISTA FRONTAL em 1/20 — confirmar antes de pedir o vidro.',
  'AS QUATRO SAPATEIRAS DE CADA ARMÁRIO são prateleiras FIXAS, de 19, 18, '
  '18 e 19 — não corrediças. ⚠ É diferente do Armário 01 do Closet Master, '
  'onde oito sapateiras correm para fora e levam corrediça por par. Aqui a '
  'prancha desenha prateleira nua, e foi assim que orcei.',
  'A COLUNA DE 28 DO ARMÁRIO 01 tem quatro sapateiras de 60 de '
  'profundidade e 28 de largura. ⚠ Vinte e oito centímetros é estreito até '
  'para sapato de criança, e a cadeia de baixo — 28 + 2 + 59 + 2 + 73 + 2 + '
  '72 + 2 = 240 — fecha exato, então a cota está certa no desenho. Vale '
  'confirmar se não era 38.',
  '⛔ A BASE METÁLICA DE 3 CM não está lançada aqui. ⚠ A VISTA LATERAL do '
  'DET 01 desenha 5 de rodapé sob o armário, o que sugere base de 5 e não '
  'de 3. São 5,5 m de rodapé nos dois armários. Fica para a passada única, '
  'junto com os outros ambientes.'],
 nao_marcenaria=[
  'Cadeira ou banqueta da penteadeira',
  'Cabides, caixas organizadoras e tudo que o cliente põe dentro',
  'Revestimentos, forro e iluminação de teto'],
 notas=[
  '⭐⭐ É O CLOSET MASTER DE NOVO, EM MENOR, e isso é bom para o preço: '
  'mesmo Branco Diamante Duratex, mesma cadeia vertical de 35 + 60 + 3 + 27 '
  '+ 3, mesma ferragem de cava usinada e corrediça. Produzidos na mesma '
  'leva, os dois closets compram chapa junta e o arredondamento cai.',
  '⭐ ARMÁRIO ABERTO, SEM UMA PORTA SEQUER nos dois itens — e por isso não '
  'há dobradiça, não há báscula e não há pulsador neste ambiente. A única '
  'ferragem de frente é a CAVA USINADA das onze gavetas, que a prancha '
  'escreve em letra: "puxador cava".',
  '⛔⛔ O PÉ-DIREITO DE 300 morde as seis verticais dos dois armários, e o '
  'Armário 02 ainda passa da chapa pela LARGURA: 304 de fechamento superior '
  'não sai dos 275, e ele vira duas peças de 152. É a primeira vez no '
  'projeto que a largura, e não a altura, parte uma peça.',
  '⭐ A PENTEADEIRA É O ÚNICO MÓVEL DIFERENTE DO AMBIENTE: espelho com LED '
  'frontal, uma gaveta de 80 e 77 de vão livre embaixo para a cadeira '
  'entrar. O tampo é aparente por baixo e por isso leva fita nos dois '
  'lados.',
  '⚠ O CARIMBO DAS FOLHAS DIZ "SUÍTE MARIANA" nas três folhas deste '
  'ambiente, mas a capa da página 192 diz CLOSET MARIANA. É erro de '
  'carimbo, não de desenho — e ele se repete no Banho Mariana, cujas folhas '
  'vêm carimbadas como "BANHO MASTER". Vale avisar a arquiteta antes que '
  'alguém corte pela folha errada.'],
)
