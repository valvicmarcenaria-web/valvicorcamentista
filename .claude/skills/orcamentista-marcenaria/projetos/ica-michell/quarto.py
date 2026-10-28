# -*- coding: utf-8 -*-
"""ICA · QUARTO — levantamento peça por peça  [28/10/2026]

páginas 060 a 070 · seis detalhamentos, seis itens.

⭐⭐ DUAS PEÇAS DE MOBILIÁRIO QUE A CASA NUNCA FEZ: a BICAMA de solteiro,
  com leito inferior corrediço, e o BAÚ com tampo que abre. Não são
  armário — são cama e caixa, com carga, pistão e movimento. As duas
  ferragens que elas pedem estão na Base SEM PREÇO.

⭐⭐ AQUI NÃO HÁ FRENTE PROVENÇAL. Toda frente é lisa, e abre por CAVA na
  própria madeira — menos as duas portas do DET 05, que abrem por PUXADOR
  PASSANTE, um perfil que atravessa a chapa e tem acabamento nas duas
  faces. É o único ambiente do projeto com passante.

⭐⭐ TRÊS PEÇAS PASSAM DO QUE A CHAPA DÁ, e é a primeira vez no projeto
  que isso aparece em peça APARENTE:
     painel de cabeceira ...... 350 de largura, contra 275 de chapa
     lateral do guarda-roupa .. 285 de altura, contra 273 de peça inteira
     porta do guarda-roupa .... 285 de altura
  O painel já vem dividido no desenho (95 + 255) e as duas partes cabem.
  O guarda-roupa, não: ele foi desenhado do piso ao teto de 300.

Padrões: Carvalho Malva Premium (painéis, cama, baú, fechamentos) ·
Off White Suave (corpo e portas do guarda-roupa) · Branco TX (interno).
"""
from base import (P, gaveta, acabamento, ALT_MAX, CHAPA_C, CHAPA_L,
                  DOBRADICA, ALTAS)

CM18 = 'MDF Carvalho Malva 18'
OW18 = 'MDF Off White Suave 18'
EST, FUN = 'MDF Branco TX 15', 'MDF Branco TX 6'
PRAT18   = 'MDF Branco TX 18'   # ⭐ só onde o vão passa de 70 cm

I1 = 'DET 01 Painel de cabeceira'
I2 = 'DET 02 Penteadeira'
I3 = 'DET 03 Cama bicama de solteiro'
I4 = 'DET 04 Baú com tampo'
I5 = 'DET 05 Armário superior com prateleiras'
I6 = 'DET 06 Guarda-roupa'

QUARTO = [
 # ══ ITEM 01 · PAINEL DE CABECEIRA — 350 × 100 × 2 ════════════════════
 #  VISTA FRONTAL 95 + 255 = 350 ⭐ e é essa a divisão que salva a peça:
 #  350 não cabe nos 275 da chapa, 255 e 95 cabem. A faixa de LED corre
 #  sobre os 255.
 P('Painel · folha maior', I1, 255, 100, 1, CM18, (2, 2), '⭐ os 350 da prancha não cabem na chapa de 275 — o desenho já divide em 95 + 255'),
 P('Painel · folha menor', I1,  95, 100, 1, CM18, (2, 2), 'A emenda cai na divisão que a própria cota marca'),

 # ══ ITEM 02 · PENTEADEIRA — 95 × 50 × 14 ═════════════════════════════
 #  VISTA SUPERIOR 95 × 50 · VISTA FRONTAL 95 de largura e 14 de altura,
 #  sendo 2 de tampo e 12 de gaveta · VISTA LATERAL 50 de profundidade
 P('Tampo',              I2, 95, 50, 1, CM18, (2, 2), 'Suspensa · 14 de altura total, 2 de tampo e 12 de gaveta'),
 P('Lateral',            I2, 50, 12, 2, CM18, (1, 1)),
 P('Travessa de fundo',  I2, 92, 12, 1, EST, (1, 0)),
 P('Frente da gaveta',   I2, 92, 12, 1, CM18, (2, 2), 'Lisa, com cava na própria madeira'),
 *gaveta(I2, 92, 45, 10, 1, 'Gaveta da penteadeira'),

 # ══ ITEM 03 · CAMA BICAMA DE SOLTEIRO — 195 × 100 × 45 ═══════════════
 #  VISTA SUPERIOR 4 + 187 + 4 = 195 e 4 + 92 + 4 = 100 ⭐ o rebaixo do
 #  colchão tem 10 de profundidade · VISTA FRONTAL e LATERAL 15 + 30 = 45,
 #  e os 30 de baixo são o LEITO INFERIOR que corre
 P('Longarina',          I3, 195, 45, 2, CM18, (2, 2), 'Lateral da cama · 195 cabe na chapa de 275'),
 P('Cabeceira e pé',     I3,  92, 45, 2, CM18, (2, 2)),
 P('Estrado do colchão', I3, 187, 92, 1, EST, (0, 0), 'Rebaixo de 10 para o colchão de solteiro — ⛔ não aparece, sem fita'),
 P('Frente do leito inferior', I3, 195, 30, 1, CM18, (2, 2), 'Lisa, com cava · é a frente da bicama'),
 P('Leito inferior · lateral', I3,  95, 28, 2, EST, (1, 0)),
 P('Leito inferior · costas',  I3, 191, 28, 1, EST, (1, 0)),
 P('Leito inferior · estrado', I3, 191, 95, 1, EST, (0, 0), '⭐ 15 mm, não 6: este estrado carrega uma pessoa — ⛔ sem fita'),

 # ══ ITEM 04 · BAÚ COM TAMPO — 110 × 100 × 60 ═════════════════════════
 #  VISTA FRONTAL 15 + 95 = 110 ⭐ o tampo se divide em FIXO (15) e o que
 #  ABRE (95) · altura 100 · VISTA SUPERIOR profundidade 60, com faixa de
 #  3 de LED no fundo · torre de tomadas sobre o tampo fixo
 P('Lateral',          I4, 100, 60, 2, CM18, (1, 1)),
 P('Costas',           I4, 107, 100, 1, EST, (0, 0), 'Contra a parede — ⛔ sem fita'),
 P('Base',             I4, 107, 60, 1, EST, (1, 0)),
 P('Tampo fixo',       I4,  15, 60, 1, CM18, (2, 2), 'Recebe a torre de tomadas e a faixa de LED'),
 P('Tampo que abre',   I4,  95, 60, 1, CM18, (2, 2), '⭐ tampo de baú: abre e tem de ficar aberto — pede pistão'),

 # ══ ITEM 05 · ARMÁRIO SUPERIOR COM PRATELEIRAS — 110 × 200 × 43 ══════
 #  VISTA FRONTAL 55 + 55 = 110 · altura 5 + 69 + 126 = 200, e os 126 se
 #  abrem em 35 + 3 + 35 + 3 + 50 ⭐ duas prateleiras iluminadas sobre um
 #  painel · VISTA LATERAL armário com 43 e prateleira com 38
 #  VISTA FRONTAL INTERNA 31 + 2 + 31 = 64: uma prateleira dentro
 P('Armário · lateral',         I5,  69, 43, 2, EST, (1, 0)),
 P('Armário · base e topo',     I5, 106, 43, 2, EST, (1, 0)),
 P('Armário · fundo',           I5, 110, 69, 1, FUN, (0, 0), 'Encaixe em rasgo'),
 P('Armário · prateleira',      I5, 106, 41, 1, PRAT18, (1, 0), '⭐ vão de 106 passa dos 70: 18 mm contra empeno'),
 P('Fechamento superior',       I5, 110, 43, 1, CM18, (2, 2), 'Aparente, em Carvalho Malva'),
 P('Frente · porta de giro',    I5,  55, 69, 2, CM18, (2, 2), 'Lisa · abre por PUXADOR PASSANTE, o único do projeto'),
 P('Painel das prateleiras',    I5, 110, 126, 1, CM18, (2, 2), 'É nele que as duas prateleiras se fixam · os 50 de baixo são o painel à vista'),
 P('Prateleira iluminada',      I5, 110, 38, 2, CM18, (2, 2), '⚠ desenhada com 3 cm de espessura — orçada em 18 mm, ver dúvida'),

 # ══ ITEM 06 · GUARDA-ROUPA — 110 × 300 × 63 ══════════════════════════
 #  VISTA FRONTAL 55 + 55 = 110 · altura 5 + 285 + 10 = 300, do piso ao
 #  teto · a cava fica a 105 do topo e a 105 do piso, num encaixe de 10×10
 #  VISTA FRONTAL INTERNA 2 + 106 + 2 = 110 · altura 5 + 2 + 50 maleiro +
 #  2 + 129 cabideiro + 2 + 20×5 gavetas + 2 + 10 = 302 ≈ 300
 P('Lateral',              I6, 285, 63, 2, OW18, (1, 0), '⛔ 285 passa dos 273 que a chapa dá em peça inteira'),
 P('Base e topo',          I6, 106, 63, 2, EST, (1, 0)),
 P('Fundo',                I6, 110, 285, 1, FUN, (0, 0), 'Encaixe em rasgo · ⛔ 285 passa dos 273'),
 P('Fechamento superior',  I6, 110, 63, 1, CM18, (2, 2), 'Aparente, em Carvalho Malva sobre corpo Off White'),
 P('Fechamento inferior',  I6, 110, 63, 1, CM18, (2, 2), 'Aparente, em Carvalho Malva · faixa de 10 à vista'),
 P('Maleiro',              I6, 106, 61, 1, EST, (1, 0), 'Divisória do maleiro de 50, em MDF Branco'),
 P('Prateleira sobre as gavetas', I6, 106, 61, 1, PRAT18, (1, 0), '⭐ vão de 106 passa dos 70: 18 mm contra empeno'),
 P('Frente · porta de giro', I6, 55, 285, 2, OW18, (2, 2), 'Lisa, com cava de 10 × 10 em Carvalho Malva · ⛔ 285 passa dos 273'),
 *gaveta(I6, 106, 55, 20, 5, 'Gaveta do roupeiro'),
]

# ── ferragem, declarada item a item ─────────────────────────────────────
GAVETAS = [(I2, 'Penteadeira · uma gaveta de 92 × 12',  1, 450),
           (I6, 'Guarda-roupa · cinco gavetas de 20',   5, 550)]
#  ⭐ a régua da casa: até 90 → 2 · 90 a 160 → 3 · 160 a 200 → 4 · acima
#    de 200 → 5
PORTAS  = [(I4, 'Tampo do baú · dobradiça de tampo',    1, 2, DOBRADICA),
           (I5, 'Portas de giro de 69',                 2, 2, DOBRADICA),
           (I6, 'Portas de giro de 285',                2, 5, DOBRADICA)]
BASCULAS= []
# ⭐ TODA FRENTE DESTE AMBIENTE ABRE POR CAVA, menos as duas do DET 05,
#   que abrem por passante. Não há um único puxador aparafusado aqui.
CAVA    = [(I2, 'Frente da gaveta da penteadeira',      1,  92),
           (I3, 'Frente do leito inferior',             1, 195),
           (I6, 'Portas do guarda-roupa · encaixe de 10 × 10', 2, 10)]
PUXADORES = []
MOLDURA = []
# ⭐⭐ a ferragem que a Base tem e o gerador não tinha
OUTRAS  = [(I5, 'Puxador passante', 'Perfil SP7000 · 0,55 m por folha, '
            'duas folhas · atravessa a chapa e tem acabamento nas duas faces',
            1.1, 'm', 'Puxador passante'),
           (I3, 'Corrediça de carga', 'Leito inferior da bicama · tem de '
            'suportar o peso de uma pessoa · ⛔ A COTAR, sem preço na Base',
            1, 'par', 'Corrediça de carga'),
           (I4, 'Pistão de tampo de baú', 'Dois por tampo que abre · ⛔ A '
            'COTAR, sem preço na Base', 2, 'un', 'Pistão de tampo de baú')]
LED     = [(I1, 'Topo do painel de cabeceira · sobre os 255', 2.55),
           (I4, 'Faixa de 3 no fundo do tampo',                1.10),
           (I5, 'Sob o armário e sob as duas prateleiras · 3 × 1,10', 3.30)]
CABIDEIROS = [(I6, 'Guarda-roupa · vão de cabideiro de 129', 1)]
SARRAFOS= [(I3, 'Apoio do estrado do colchão · duas de 1,87 e duas de 0,92', 5.6)]
SUPORTES= [(I5, 'Prateleira do armário e as duas iluminadas · 3 × 2', 6),
           (I6, 'Prateleira sobre as gavetas · 1 × 2',                 2)]
ALMAS   = []
VIDRO   = []
SERRALHERIA = []

# ── o cabeçalho de cada bloco ──────────────────────────────────────────
CABECA = {
 I1: ('350 × 100 × 2',
      'VISTA FRONTAL 95 + 255 = 350 ⭐ e é essa a divisão que salva a peça: 350 não cabe nos '
      '275 da chapa, 255 e 95 cabem · a faixa de LED corre sobre os 255 · VISTA LATERAL 2 de '
      'espessura, VISTA SUPERIOR 350 de corrida'),
 I2: ('95 × 50 × 14',
      'VISTA SUPERIOR 95 × 50 · VISTA FRONTAL 95 de largura e 14 de altura, sendo 2 de tampo '
      'e 12 de gaveta · VISTA LATERAL 50 de profundidade · suspensa, com cava na própria madeira'),
 I3: ('195 × 100 × 45',
      'VISTA SUPERIOR 4 + 187 + 4 = 195 e 4 + 92 + 4 = 100 ⭐ o rebaixo do colchão tem 10 de '
      'profundidade · VISTA FRONTAL e LATERAL 15 + 30 = 45, e os 30 de baixo são o LEITO '
      'INFERIOR que corre'),
 I4: ('110 × 100 × 60',
      'VISTA FRONTAL 15 + 95 = 110 ⭐ o tampo se divide em FIXO (15) e o que ABRE (95) · '
      'altura 100 · VISTA SUPERIOR profundidade 60, com faixa de 3 de LED no fundo e torre de '
      'tomadas sobre o tampo fixo'),
 I5: ('110 × 200 × 43',
      'VISTA FRONTAL 55 + 55 = 110 · altura 5 + 69 + 126 = 200, e os 126 se abrem em '
      '35 + 3 + 35 + 3 + 50 ⭐ duas prateleiras iluminadas sobre um painel · VISTA LATERAL '
      'armário com 43 e prateleira com 38 · VISTA FRONTAL INTERNA 31 + 2 + 31: uma prateleira'),
 I6: ('110 × 300 × 63',
      'VISTA FRONTAL 55 + 55 = 110 · altura 5 + 285 + 10 = 300, do piso ao teto · a cava fica '
      'a 105 do topo e a 105 do piso, num encaixe de 10 × 10 · VISTA FRONTAL INTERNA '
      '2 + 106 + 2 = 110 e 5 + 2 + 50 maleiro + 2 + 129 cabideiro + 2 + 20×5 gavetas + 2 + 10'),
}

FOLHA = dict(
 aba='QUARTO',
 sub='Jéssica e Michell · Projeto ICA · páginas 060 a 070 · seis itens · '
     'nenhuma frente provençal: toda frente é lisa e abre por CAVA na '
     'própria madeira, menos as duas portas do DET 05, que abrem por '
     'puxador passante · Carvalho Malva nos painéis, na cama, no baú e '
     'nos fechamentos · Off White Suave no corpo e nas portas do '
     f'guarda-roupa · Branco TX no interno · peça inteira até {ALT_MAX:g}, '
     f'que é a chapa de {CHAPA_C:g} menos o acerto de corte',
 chapa_txt={CM18:  'Carvalho Malva Premium · painéis, cama, baú e fechamentos aparentes',
            OW18:  'Off White Suave · corpo e portas do guarda-roupa',
            PRAT18:'Prateleiras de vão acima de 70 cm · 18 mm contra empeno',
            EST:   'Estrutura e caixaria · o padrão da Base para caixaria',
            FUN:   'Fundos · encaixe em rasgo, sem fita'},
 nota='⛔ O FRETE ESTÁ ZERADO DE PROPÓSITO: as linhas de frete da Base não '
      'têm preço ainda. Preencher lá e elas aparecem aqui sozinhas.   '
      '⭐⭐ DUAS PEÇAS DE MOBILIÁRIO QUE A CASA NUNCA FEZ: a bicama de '
      'solteiro, com leito corrediço, e o baú com tampo que abre. As duas '
      'ferragens que elas pedem — corrediça de carga e pistão de tampo — '
      'existem na Base e estão SEM PREÇO, então saem ZERO e denunciam.   '
      '⭐⭐ TRÊS PEÇAS PASSAM DO QUE A CHAPA DÁ, e é a primeira vez que '
      'isso aparece em peça APARENTE: o painel de cabeceira com 350 de '
      'largura, e a lateral e a porta do guarda-roupa com 285 de altura. '
      'O painel já vem dividido no desenho; o guarda-roupa, não.',
 duvidas=[
  'O PAINEL DE CABECEIRA TEM 350 e a chapa dá 275. O desenho já divide em '
  '95 + 255, e as duas partes cabem — foi assim que orcei, com a emenda '
  'caindo onde a própria cota marca. ⚠ Confirmar que a emenda pode ficar '
  'aí: num painel liso de 1 m de altura ela aparece.',
  'O GUARDA-ROUPA FOI DESENHADO COM 300, do piso ao teto, e a lateral e a '
  'porta ficam com 285 — acima dos 273 que a chapa dá em peça inteira. '
  'Rebaixei, como nas colunas do Living. ⚠ Mas uma PORTA de 285 numa folha '
  'só é incomum: o normal é virar duas folhas, corpo e maleiro. Isso muda '
  'duas dobradiças e a cava. Decisão de desenho.',
  'A PRATELEIRA ILUMINADA DO DET 05 está desenhada com 3 cm de espessura. '
  'MDF não existe em 30 mm: ou se colam duas chapas, e aí dobra a chapa '
  'dessas peças e entra laminação de topo, ou se faz caixão. Orçada em '
  '18 mm simples. ⚠ É a mesma questão das colunas do Living.',
  'A CORREDIÇA DE CARGA DA BICAMA não tem preço na Base. A linha existe '
  '("precisa suportar o peso de uma pessoa") e está vazia. Sai ZERO. ⛔ Até '
  'ela existir, o custo da cama é um PISO. ⚠ É a ferragem que decide se a '
  'bicama funciona.',
  'O PISTÃO DE TAMPO DE BAÚ também não tem preço na Base — dois por tampo '
  'que abre. Sai ZERO. ⚠ Sem ele o tampo de 95 × 60 não fica aberto, e um '
  'tampo desse tamanho caindo é risco, não é detalhe.',
  'O PUXADOR PASSANTE: o PERFIL tem preço na Base (SP7000, R$ 100/m, e '
  'lancei 1,10 m para as duas folhas), mas a USINAGEM do passante está '
  '"A COTAR" — ela atravessa a chapa e tem acabamento nas duas faces. ⚠ É '
  'mão de obra que não está nesta conta.',
  'A CAVA DO GUARDA-ROUPA é um encaixe de 10 × 10 em Carvalho Malva sobre '
  'porta Off White — duas cores na mesma frente. A Base cobra cava por '
  'METRO (R$ 50/m) e por PEÇA (R$ 50 cada). Lancei por metro, o que dá '
  'R$ 10 pelas duas; por peça seriam R$ 100. ⚠ Qual vale para um encaixe '
  'curto? E quem faz o encaixe de cor?',
  '⛔ A BASE METÁLICA DE 3 CM aparece em TODA folha do projeto, inclusive '
  'nas seis daqui, e o senhor resolveu em 26/10 que a casa faz em MDF '
  'melamínico. ⚠ Ela NÃO ESTÁ LANÇADA em nenhum ambiente ainda — nem aqui, '
  'nem no Living, nem na Cozinha. São uns 3 m de rodapé por ambiente.',
  'O SUPORTE OCULTO está a 2 por prateleira em todos os ambientes, mas a '
  'Base diz "de 40 em 40 cm" — numa prateleira de 110, como as iluminadas '
  'daqui, isso pediria 4. ⚠ Mantive 2 para não divergir do que já está '
  'orçado. Qual é a regra?'],
 nao_marcenaria=[
  'Torre de tomadas sobre o tampo fixo do baú — a definir com o cliente',
  'Colchões de solteiro: o de cima no rebaixo de 187 × 92 e o do leito inferior',
  'A fixação do painel de cabeceira na parede, que é montagem e não marcenaria'],
 notas=[
  '⭐⭐ DUAS PEÇAS QUE A CASA NUNCA FEZ. A bicama de solteiro tem leito '
  'inferior corrediço e o baú tem tampo que abre — não são armário, são '
  'cama e caixa, com carga e movimento. As duas ferragens que elas pedem, '
  'corrediça de carga e pistão de tampo, existem na Base e estão sem '
  'preço. Saem ZERO e o orçamento denuncia.',
  '⭐⭐ TRÊS PEÇAS PASSAM DO QUE A CHAPA DÁ, e aqui elas são APARENTES. O '
  'painel de cabeceira tem 350 de largura contra 275 de chapa, e a lateral '
  'e a porta do guarda-roupa têm 285 contra os 273 de peça inteira. O '
  'painel já vem dividido no desenho, em 95 + 255, e as duas partes cabem; '
  'o guarda-roupa foi desenhado do piso ao teto e não vem dividido.',
  '⭐ NENHUMA FRENTE PROVENÇAL NESTE AMBIENTE. Toda frente é lisa e abre '
  'por cava na própria madeira — e as duas portas do DET 05 abrem por '
  'puxador passante, que é o único do projeto. Não há um só puxador '
  'aparafusado no Quarto.',
  '⭐ O ESTRADO DO LEITO INFERIOR saiu em 15 mm, não em 6 como fundo de '
  'gaveta: ele carrega uma pessoa. É a diferença entre uma gaveta e uma '
  'cama, e é onde o levantamento de armário erraria sozinho.',
  '⚠ A PRATELEIRA DE 3 CM do DET 05 é a mesma questão das colunas do '
  'Living: MDF não existe em 30 mm. Orçada em 18 mm simples, como lá.'],
)
