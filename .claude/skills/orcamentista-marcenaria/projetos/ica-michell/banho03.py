# -*- coding: utf-8 -*-
"""ICA · BANHO 03 — levantamento peça por peça  [28/10/2026]

páginas 230 a 235 · dois detalhamentos, dois itens, UMA folha de detalhe —
é o ambiente mais enxuto do projeto inteiro, e o último dele.

⭐ UMA COR SÓ: MDF SAL ROSA — Arauco. É o mesmo padrão que a Suíte Mariana
  trouxe, e aqui ele faz o armário todo, as ripas das portas e as três
  prateleiras suspensas.

⭐⭐ QUASE TUDO NESTE BANHEIRO NÃO É NOSSO. A bancada é quartzito Bianco
  Superiore, a cuba é de apoio, o box vai até o teto em ferragem preta, os
  dois revestimentos Appia são da Decortiles e o NICHO É FEITO NA PRÓPRIA
  ALVENARIA — a ELEVAÇÃO 04 escreve isso com todas as letras, e é por isso
  que ele não entra na conta. ⛔ De marcenaria sobram o armário de 120 e
  as três prateleiras de 60.

⭐ AS PRATELEIRAS NÃO TÊM LATERAL NEM FUNDO: são três tábuas de 60 × 20
  penduradas em DUAS HASTES METÁLICAS pretas fixas na laje, 174 de altura,
  com LED embutido sob cada uma. É a mesma solução do Banho Mariana, e a
  haste continua SEM PREÇO na Base.

⚠ O VÃO ENTRE AS RIPAS DA PORTA NÃO VEM COTADO. A prancha escreve "ripas
  de 4cm" e para por aí. Adotei vão de 1, que é o passo que o desenho em
  1/20 mostra: treze ripas em cada porta de 60.
"""
from base import P, ripado, ALT_MAX, CHAPA_C, DOBRADICA, PERDA_RIPA

SR18, SR15, SR6 = 'MDF Sal Rosa 18', 'MDF Sal Rosa 15', 'MDF Sal Rosa 6'

I1 = 'DET 01 Bancada com armário'
I2 = 'DET 02 Prateleiras'

# ⭐ ripa de 4 com vão de 1 · treze ripas em cada porta de 60, duas portas
N_RIPA, N_PORTA = 13, 2

BANHO03 = [
 # ══ ITEM 01 · BANCADA COM ARMÁRIO — 120 × 60 × 45 ═══════════════════
 #  DET. 01 VISTA FRONTAL   60 + 60 = 120 · altura 45 do armário + 10 da
 #     pedra = 55 · duas portas ripadas iguais
 #  DET. 01 VISTA SUPERIOR  120 × 60 · cuba redonda de 30 centrada em 60
 #  DET. 01 VISTA LATERAL   60 de profundidade · 44 + 10 = 54
 #  ⛔ a bancada de quartzito e a cuba de apoio são marmoraria, não nossas
 P('Lateral',               I1, 60, 45, 2, SR15, (1, 1),
   'Aparente: o armário é suspenso e as duas pontas ficam à mostra'),
 P('Tampo e base',          I1, 117, 60, 2, SR15, (1, 0),
   '⭐ tampo cheio, não travessa: a pedra de 120 × 60 apoia nele inteiro'),
 P('Divisória central',     I1, 60, 45, 1, SR15, (1, 0),
   'A vertical entre as duas portas de 60'),
 P('Fundo',                 I1, 120, 45, 1, SR6, (0, 0), 'Encaixe em rasgo'),
 P('Frente · porta ripada · campo', I1, 60, 45, 2, SR15, (2, 2),
   '⭐ o painel que aparece no vão de 1 entre as ripas: sai na cor da '
   'frente, não em branco · duas portas de giro iguais'),
 P('Ripa de 4',             I1, 4, 45, N_RIPA*N_PORTA, SR15, (2, 2),
   f'⚠ a prancha escreve "ripas de 4cm" e não diz o vão · adotei 1, que é '
   f'o passo do desenho em 1/20 · {N_RIPA} ripas por porta, {N_PORTA} '
   'portas · laminada nos dois lados'),
 P('Ripa de 4 · perda de serra', I1,
   round(N_RIPA*4*N_PORTA*(PERDA_RIPA - 1), 1), 45, 1, SR15, (0, 0),
   '⭐ fator 1,10 da Base · a serra come chapa a cada 4 cm de ripa · ⛔ é '
   'perda, não peça: sem fita'),

 # ══ ITEM 02 · PRATELEIRAS — três de 60 × 20, suspensas a 174 ════════
 #  DET. 02 PERSPECTIVA     174 de altura de haste · 60 × 20 de tábua
 #  DET. 02 VISTA SUPERIOR  60 × 20
 #  ⭐ não há caixa: são três tábuas penduradas em duas hastes de metal
 #    preto fixas na laje, com LED embutido sob cada uma
 P('Prateleira',            I2, 60, 20, 3, SR18, (2, 2),
   '⭐ 18 mm: a tábua vence 60 de vão pendurada só pelas pontas, sem '
   'apoio nenhum embaixo · as quatro arestas aparecem, e sob cada uma '
   'corre a fita de LED embutida · ⛔ pendurada em haste, sem armário: sem suporte'),
]

# ── ferragem, declarada item a item ─────────────────────────────────────
GAVETAS = []
PORTAS  = [(I1, 'Duas portas de giro ripadas de 45 de altura', 2, 2,
            DOBRADICA)]
BASCULAS= []
CAVA    = []
PUXADORES = []
MOLDURA = []
LED     = [(I2, 'Uma fita embutida sob cada uma das três prateleiras', 1.8)]
CABIDEIROS = []
SARRAFOS= []
SUPORTES= []
ALMAS   = []
VIDRO   = []
SERRALHERIA = []
# ⭐ MESMA LEITURA DO BANHO GOURMET E DO BANHO MASTER: a porta ripada não
#   tem puxador nenhum desenhado, e face ripada não aceita cava sem cortar
#   a ripa. Quem sobra é o pulsador.
OUTRAS  = [(I1, 'Pulsador', 'Duas portas ripadas · abre por toque, sem '
            'ferragem à vista · ⚠ a prancha não desenha puxador nenhum',
            2, 'un', 'Pulsador'),
           (I2, 'Haste metálica de prateleira', 'As duas hastes pretas de '
            '174 fixas na laje, que seguram as três prateleiras · ⛔ SEM '
            'PREÇO na Base · é a segunda do projeto, depois do Banho '
            'Mariana', 2, 'un', 'Haste metálica de prateleira')]

CABECA = {
 I1: ('120 × 60 × 45',
      'DET. 01 VISTA FRONTAL 60 + 60 = 120, duas portas ripadas iguais · '
      'altura 45 do armário mais 10 da pedra = 55 · VISTA SUPERIOR 120 × '
      '60, cuba redonda de 30 centrada nos primeiros 60 · VISTA LATERAL '
      '60 de profundidade, 44 + 10 = 54 · ⭐ armário SUSPENSO, com portas '
      'ripadas de ripa de 4 em MDF Sal Rosa'),
 I2: ('60 × 20 · três, suspensas a 174',
      'DET. 02 PERSPECTIVA 174 de altura de haste, tábua de 60 × 20 · '
      'VISTA SUPERIOR 60 × 20 · ⭐ não há caixa: são três tábuas '
      'penduradas em duas hastes de metal preto fixas na laje, com fita '
      'de LED embutida sob cada uma'),
}

FOLHA = dict(
 aba='BANHO 03',
 sub='Jéssica e Michell · Projeto ICA · páginas 230 a 235 · dois itens em '
     'UMA folha de detalhe — o ambiente mais enxuto do projeto · ⭐ uma cor '
     'só, MDF Sal Rosa Arauco · ⛔ quase tudo aqui é de outro fornecedor: '
     'a bancada é quartzito, o nicho é feito na própria alvenaria e os '
     'revestimentos são Decortiles · peça inteira até '
     f'{ALT_MAX:g}, que é a chapa de {CHAPA_C:g} menos o acerto de corte',
 chapa_txt={SR15: 'Sal Rosa · Arauco · o armário inteiro, o campo das '
                  'portas e as 26 ripas de 4',
            SR18: 'Sal Rosa 18 mm · as três prateleiras suspensas, que '
                  'vencem 60 de vão penduradas só pelas pontas',
            SR6:  'Sal Rosa 6 mm · o fundo do armário, encaixe em rasgo'},
 nota='⛔ O FRETE ESTÁ ZERADO DE PROPÓSITO: as linhas de frete da Base não '
      'têm preço ainda. Preencher lá e elas aparecem aqui sozinhas.   '
      '⭐⭐ QUASE TUDO NESTE BANHEIRO NÃO É MARCENARIA. A bancada é '
      'quartzito Bianco Superiore com 10 de espessura aparente, a cuba é '
      'redonda de apoio de 30, o box vai até o teto em ferragem preta, os '
      'dois revestimentos Appia são da Decortiles e o NICHO É FEITO NA '
      'PRÓPRIA ALVENARIA — a ELEVAÇÃO 04 escreve isso com todas as letras. '
      'De marcenaria sobram o armário de 120 e as três prateleiras de 60, '
      'e é só isso que esta aba cobra.   '
      '⭐ AS TRÊS PRATELEIRAS NÃO TÊM CAIXA. São três tábuas de 60 × 20 '
      'penduradas em DUAS HASTES METÁLICAS pretas fixas na laje, 174 de '
      'altura, com LED embutido sob cada uma. É a mesma solução do Banho '
      'Mariana, e a haste continua SEM PREÇO na Base — por isso o item 02 '
      'é um PISO.   '
      '⚠ O VÃO ENTRE AS RIPAS DA PORTA NÃO VEM COTADO: a prancha escreve '
      '"ripas de 4cm" e para por aí. Adotei vão de 1, que é o passo do '
      'desenho em 1/20 — treze ripas em cada porta de 60.',
 duvidas=[
  '⚠ A HASTE METÁLICA DAS PRATELEIRAS CONTINUA SEM PREÇO NA BASE. São '
  'duas hastes pretas de 174, fixas na laje, e são elas que seguram as '
  'três prateleiras — sem lateral, sem fundo, sem suporte oculto. ⛔ É '
  'serralheria, não ferragem de R$ 30, e é a segunda do projeto, depois '
  'do Banho Mariana. Lancei a zero para aparecer na conta sem mentir. '
  'Enquanto não tiver preço, o item 02 é um PISO.',
  'O VÃO ENTRE AS RIPAS DA PORTA É PREMISSA MINHA. A prancha escreve '
  '"ripas de 4cm" e não diz o espaçamento. ⚠ Adotei 1, que é o passo que '
  'o desenho em 1/20 mostra: treze ripas em cada porta de 60, vinte e '
  'seis ao todo. ⛔ Se for ripa de 4 colada sem vão nenhum, como a '
  'PERSPECTIVA sugere, sobem para quinze por porta e a filetagem manual '
  'sobe junto — são R$ 180 de diferença.',
  'A FRENTE RIPADA É SOBRE CAMPO FECHADO ou é ripa solta, vazada? Lancei '
  'as DUAS CAMADAS, como no Banho Gourmet e no Banho Master: campo de '
  '60 × 45 em Sal Rosa mais as ripas por cima. ⚠ A PERSPECTIVA mostra a '
  'frente como superfície contínua, que é o que me fez decidir. ⛔ Se for '
  'vazada, saem 0,54 m² de campo e o armário fica mais barato — mas aí o '
  'interior aparece e a caixaria não pode mudar de cor.',
  'AS DUAS PORTAS RIPADAS NÃO TÊM PUXADOR DESENHADO. ⭐ Orcei PULSADOR, '
  'R$ 100 cada, R$ 200 pelas duas — mesma leitura do Banho Gourmet e do '
  'Banho Master, pela mesma razão: cava cortaria a ripa e puxador '
  'aparafusado o desenho mostraria. ⚠ A alternativa é cava usinada, que '
  'sairia R$ 60 pelas duas frentes de 60. É R$ 140 de diferença.',
  'O ARMÁRIO É SUSPENSO e tem 120 × 60 de bancada de quartzito em cima — '
  'a pedra sozinha pesa uns 45 kg. ⚠ Quem segura isso não é a marcenaria: '
  'pede mão francesa ou cantoneira chumbada. A prancha não desenha '
  'nenhuma. ⛔ Não lancei serralheria, pelo mesmo critério do Banho '
  'Master. Confirmar se entra.',
  'AS PRATELEIRAS SAÍRAM EM 18 mm e não em 15. ⚠ Elas vencem 60 de vão '
  'penduradas só pelas pontas, sem nada embaixo, e ainda levam um rasgo '
  'de LED na face inferior — em 15 mm empenam. ⛔ Se o desenho quiser a '
  'tábua mais fina, é decisão de aparência contra flecha, e vale dizer '
  'que 15 mm com rasgo é pouca seção.',
  'O NICHO DO BOX É FEITO NA PRÓPRIA ALVENARIA, com revestimento Appia '
  'Osso — a ELEVAÇÃO 04 escreve. ⚠ Não entra nesta conta, e está certo. '
  '⛔ Só confirmo aqui para ninguém procurá-lo depois: é obra, não '
  'marcenaria.',
  '⛔ A BASE METÁLICA DE 3 CM: aqui ela não cabe em lugar nenhum — o '
  'armário é suspenso e as prateleiras penduram da laje. É o único '
  'ambiente do projeto em que nada toca o chão.'],
 nao_marcenaria=[
  'Bancada em quartzito Bianco Superiore, 120 × 60 com 10 de espessura aparente',
  'Cuba Redonda de Apoio 30 cm Branco Slim - Deca',
  'Espelho de 50 × 160 da ELEVAÇÃO 01',
  'Box até o teto com ferragens preto, e o chuveiro de tubo de parede Black Matte',
  'Bacia para caixa acoplada Branco Carrara, misturador de parede Duna '
  'Clássica e acabamentos de registro Black Matte Cubo - Deca',
  'Revestimentos Appia Osso 120 × 120 e Appia Bamboo Osso 60 × 120 - Decortiles',
  '⛔ O nicho do box — feito na PRÓPRIA ALVENARIA, escrito na ELEVAÇÃO 04',
  '⚠ As duas hastes metálicas pretas de 174 que seguram as prateleiras: '
  'são nossas de projeto, mas são serralheria, e estão a zero'],
 notas=[
  '⭐⭐ É O AMBIENTE MAIS ENXUTO DO PROJETO, e isso é leitura, não descuido. '
  'A prancha do Banho 03 tem seis páginas e UMA folha de detalhe, com os '
  'dois itens lado a lado. Tudo o mais que aparece nas quatro elevações '
  'tem dono: marmoraria, vidraçaria, metais Deca, revestimento Decortiles '
  'ou alvenaria. ⛔ O nicho do box é o caso mais claro: a ELEVAÇÃO 04 '
  'escreve "nicho feito na própria alvenaria".',
  '⭐ AS TRÊS PRATELEIRAS SÃO O ITEM MAIS SIMPLES DO PROJETO INTEIRO — três '
  'tábuas de 60 × 20 — e mesmo assim não fecham preço, porque a haste '
  'metálica que as segura não existe na Base. É a mesma situação do Banho '
  'Mariana. Duas hastes, 1,8 m de LED e 0,36 m² de Sal Rosa.',
  '⚠ A RIPA DE 4 É A MAIS LARGA DO PROJETO. O Banho Gourmet tem ripa de 3, '
  'o Banho Master ripa de 2, a Suíte 03 ripa de 3. Aqui são 4, escritas na '
  'prancha — mas o vão não. Adotei 1, e são 26 ripas com filetagem manual '
  'nas quatro arestas de cada uma.',
  '⭐ ESTE É O ÚLTIMO AMBIENTE DO EXECUTIVO. Com ele fecham os vinte do '
  'Painel e as 235 páginas da prancha.'],
)
