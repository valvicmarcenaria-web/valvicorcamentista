# -*- coding: utf-8 -*-
"""ICA · COZINHA — levantamento peça por peça  [28/10/2026]

páginas 028 a 042 · ⭐ [Jonathan 28/10] "na cozinha pode mesclar o item
2, 3 e 4" — a torre da geladeira e os dois armários superiores são um
conjunto só, na mesma parede e no mesmo padrão. Ficam TRÊS itens.

⭐⭐ TRÊS PADRÕES DE MDF NO MESMO AMBIENTE, e nenhum é o do Living:
     ilha e bancada ............. Verde Floresta · Linha Velluto
     armários, ripado e básculas  Jequitibá Rosa · Linha Essencial Wood
     divisórias e interno ....... Branco
   ⛔ São TRÊS arredondamentos de chapa, não um. Cada cor é uma compra
     separada e puxa no mínimo uma chapa, mesmo que leve uma peça só.

⚠ PUXADOR OU CAVA? A prancha desenha cava frontal usinada em toda frente.
  A Base registra "Puxador Alças Traso — ICA · toda frente da Cozinha e da
  Lavanderia", a R$ 172,71 cada. Orçado com CAVA, que é o que a prancha
  manda; a diferença para o puxador sai calculada no fim do arquivo.
"""
from base import (P, gaveta, ripado, provencal, acabamento, fita_m, ALT_MAX,
                  CHAPA_C, CHAPA_L, CHAPA_M2, APROV, PRECO, FITA_PERD,
                  CORREDICA, DOBRADICA, BASCULA, SLIM, CAVA_M, PUXADOR_128,
                  LED_M, SUPORTE, CONSUM, EMBAL, ALTAS)

# ⭐ a chave carrega a COR **e** a espessura: cada combinação é uma compra
#   separada e um arredondamento próprio
VF,  JR  = 'MDF Verde Floresta 18', 'MDF Jequitibá Rosa 18'
VF15, JR15 = 'MDF Verde Floresta 15', 'MDF Jequitibá Rosa 15'
VF6,  JR6  = 'MDF Verde Floresta 6',  'MDF Jequitibá Rosa 6'
# ⭐⭐ A CAIXARIA É BRANCO TX [Jonathan, 28/10/2026]
#   > "vc aparentemente não considerou o quantitativo de material da
#   >  estrutura que sera em branco tx"
#   Eu lançava base, topo e laterais em chapa de COR de 18 mm. A Base diz,
#   na própria tabela de espessura por aplicação, que estrutura e caixaria
#   são 15 mm — e o produto é MDF Branco TX. Fica em cor só o que se vê:
#   as frentes, a lateral aparente da ilha e o ripado.
EST, FUN = 'MDF Branco TX 15', 'MDF Branco TX 6'
PRAT18 = 'MDF Branco TX 18'   # ⭐ só onde o vão passa de 70 cm

I1 = 'DET 01 Ilha'
I2 = 'DET 02+03+04 Torre da geladeira e armários superiores'
I3 = 'DET 05 Bancada com armário'

COZINHA = [
 # ══ ITEM 01 · ILHA — 245 × 90 × 110 ═════════════════════════════════
 #  VISTA FRONTAL  5 + 2+60+2+69+38+2+60+2 + 5 = 245 ⭐ · altura 5 + 85 = 90
 #                 módulo de 60 fecha 18 + 18 + 52 = 88 · outro 38 + 38 = 76
 #  VISTA SUPERIOR 122 + 122 = 244 ≈ 245 ⭐ · VISTA POSTERIOR 5 + 235 = 240
 P('Lateral',               I1, 110, 85, 2, VF, (1, 0), '⭐ a lateral aparente da ilha — é o que se vê, fica em cor'),
 P('Base e tampo de apoio', I1, 235, 110, 2, EST, (1, 0), 'Caixaria em Branco TX · o tampo recebe o quartzito, a pedra não é nossa'),
 P('Divisória',             I1, 110, 85, 4, EST, (1, 0), 'Módulos de 60 · 69 · 38 · 60, com divisórias de 2'),
 P('Fundo',                 I1, 235, 85, 1, FUN, (0, 0), 'Encaixe em rasgo'),
 *provencal('Frente · gavetão',       I1, 60, 38, 2, VF15, VF6, 'Provençal · abre pelo puxador Alças Traso'),
 *provencal('Frente · gavetão alto',  I1, 60, 52, 1, VF15, VF6, 'Provençal'),
 *provencal('Frente · gaveta',        I1, 60, 18, 2, VF15, VF6, 'Provençal · ⭐ com a moldura usinada na router a altura de 18 deixou de ser problema: não há travessa para não caber'),
 *provencal('Frente · porta',         I1, 69, 85, 1, VF15, VF6, 'De giro · provençal'),
 *provencal('Frente · porta tempero', I1, 38, 85, 1, VF15, VF6, 'Provençal'),
 *gaveta(I1, 60, 100, 38, 2, 'Gavetão'),
 *gaveta(I1, 60, 100, 52, 1, 'Gavetão alto'),
 *gaveta(I1, 60, 100, 18, 2, 'Gaveta'),
 *ripado(I1, 235, 85, 3, 3, JR,
         'Vista posterior ripada em Jequitibá Rosa · ripa de 3 com vão de 3 · laminada nos dois lados'),

 # ══ ITEM 02 · TORRE E SUPERIORES ════════════════════════════════════
 #  ⭐ mesclados a pedido do Jonathan. Mesmo padrão, mesma parede.
 #  TORRE 110 × 300 × 80 · cadeia 10 + 46 + 46 + 3 + 194 = 300 ⭐
 P('Torre · lateral',       I2, 80, 300, 2, EST, (1, 0), 'Caixaria em Branco TX · ⛔ desenhada com 300: a chapa dá 273'),
 P('Torre · fundo',         I2, 104, 300, 1, FUN, (0, 0), 'Encaixe em rasgo · ⛔ 300'),
 P('Torre · base e topo',   I2, 104, 80, 2, EST, (1, 0)),
 P('Torre · tampo do nicho',I2, 104, 80, 1, EST, (1, 0), 'A 194 do chão, sobre a geladeira de 596 L'),
 P('Torre · prateleira',    I2, 104, 80, 1, PRAT18, (1, 0), '⭐ vão de 104 passa dos 70: vai em 18 mm, contra empeno'),
 P('Torre · báscula',       I2, 104, 46, 2, JR, (2, 2), 'Fecho toque · ⭐ frente LISA, não provençal'),
 #  SUPERIOR 01 · 405 × 103 × 67 · módulos 77+65+71+65+77+50 = 405 ⭐
 #                interno 2+74+2+63+2+69+2+63+2+75+2+47+2 = 405 ⭐
 P('Superior 01 · base e topo', I2, 203, 67, 4, EST, (1, 0), 'Os 405 em dois módulos de 203'),
 P('Superior 01 · lateral',     I2, 67, 103, 2, EST, (1, 0)),
 P('Superior 01 · divisória',   I2, 67, 93, 5, EST, (1, 0)),
 P('Superior 01 · prateleira',  I2, 70, 67, 6, EST, (1, 0), 'Uma por vão · 68 líquido, fica em 15 mm'),
 P('Superior 01 · báscula',     I2, 70, 46, 9, JR, (2, 2), 'Nove basculantes, fecho toque · ⭐ LISAS'),
 *provencal('Superior 01 · porta de giro', I2, 47, 103, 1, JR15, JR6, 'Módulo de 50 · provençal'),
 #  SUPERIOR 02 · 405 × 40 × 37 · mesma cadeia de módulos · com LED
 P('Superior 02 · base e topo', I2, 203, 37, 4, EST, (1, 0), 'Os 405 em dois módulos'),
 P('Superior 02 · lateral',     I2, 37, 40, 2, EST, (1, 0)),
 P('Superior 02 · divisória',   I2, 37, 40, 5, EST, (1, 0)),
 P('Superior 02 · báscula',     I2, 67, 40, 6, JR, (2, 2), 'Seis basculantes, uma por módulo · ⭐ LISAS'),

 # ══ ITEM 03 · BANCADA COM ARMÁRIO — 405 × 90 × 60 ═══════════════════
 #  ⭐ VISTA FRONTAL 215 + 62 + 128 = 405, e o 62 é o VÃO DO LAVA-LOUÇAS:
 #    de marcenaria são 343, que fecham em 95 + 35 + 85 + 68 + 60 = 343 ⭐
 #  altura 5 + 80 + 5 = 90 · frentes 40 + 40 = 80 (gavetão duplo)
 #  VISTA SUPERIOR profundidade 55 + 5 = 60
 P('Base e tampo de apoio', I3, 172, 60, 4, EST, (1, 0), 'Os 343 em dois módulos · o tampo recebe o quartzito'),
 P('Fundo',                 I3, 172, 80, 2, FUN, (0, 0), 'Encaixe em rasgo'),
 P('Lateral e divisória',   I3, 60, 80, 6, EST, (1, 0), 'Cinco módulos: 95 · 35 · 85 · 68 · 60'),
 *provencal('Frente · gavetão de 95',      I3, 95, 40, 2, VF15, VF6, 'Provençal'),
 *provencal('Frente · gavetão de 85',      I3, 85, 40, 2, VF15, VF6, 'Provençal'),
 *provencal('Frente · gavetão de 68',      I3, 68, 40, 2, VF15, VF6, 'Provençal'),
 *provencal('Frente · gavetão de lixeira', I3, 60, 80, 1, VF15, VF6, 'Módulo de 60, altura cheia · provençal'),
 *provencal('Frente · porta tempero',      I3, 35, 80, 1, VF15, VF6, 'Módulo de 35 · provençal'),
 *gaveta(I3, 95, 55, 40, 2, 'Gavetão de 95'),
 *gaveta(I3, 85, 55, 40, 2, 'Gavetão de 85'),
 *gaveta(I3, 68, 55, 40, 2, 'Gavetão de 68'),
 *gaveta(I3, 60, 55, 80, 1, 'Gavetão de lixeira'),
]

# ── ferragem, declarada item a item ─────────────────────────────────────
GAVETAS = [(I1, 'Ilha · gavetões e gavetas',        5, 550),
           (I3, 'Bancada · gavetões e lixeira',     7, 550)]
PORTAS  = [(I1, 'Ilha · porta de giro e porta tempero', 2, 2, DOBRADICA),
           (I2, 'Superior 01 · porta de giro',          1, 3, DOBRADICA),
           # ⭐ achada pelo auditor: a porta tempero da bancada estava sem
           #   dobradiça nenhuma. Altura 80, então duas pela régua da casa.
           (I3, 'Bancada · porta tempero',              1, 2, DOBRADICA)]
BASCULAS= [(I2, 'Torre, Superior 01 e Superior 02 · fecho toque', 17)]
# ⭐⭐ CADA FRENTE ABRE DE UM MODO SÓ, e agora os dois estão definidos:
#   báscula ............. HK-XS + puxador slim Rometal, R$ 35  [Jonathan]
#   porta e gavetão ..... puxador Alças Traso 128 mm, R$ 110    [Jonathan]
# ⛔ A CAVA SAI. A prancha pedia o puxador Alças Traso E cava usinada na
#   mesma frente — a contradição estava anotada em nunca-orcei.md desde
#   26/10 ("um dos dois sai"). Com o puxador especificado e precificado,
#   quem sai é a cava: frente não abre de dois modos. ⚠ É a única coisa
#   aqui que eu inferi, e vale confirmar.
CAVA     = []
PUXADORES= [(I1, 'Frentes da ilha · gavetões, gavetas e portas', 7),
            (I2, 'Superior 01 · porta de giro',                  1),
            (I3, 'Frentes da bancada · gavetões e porta tempero', 8)]
# ⛔ a mão de obra de moldura provençal não tem preço: sai zero e denuncia
MOLDURA  = [(I1, 'Frentes da ilha',     7),
            (I2, 'Superior 01 · porta', 1),
            (I3, 'Frentes da bancada',  8)]
LED     = [(I2, 'Superior 02 · iluminação inferior', 4.00)]
SUPORTES= [(I2, 'Prateleiras do Superior 01 · 6 × 2', 12)]
# ⛔ SEM ALMA DE AÇO: nenhuma peça da Cozinha passa de 30 mm. ⚠ A torre e os
#   superiores são desenhados com laterais de 3 cm — se a construção for
#   painel duplo e não caixote, isso vira chapa dobrada E alma. A decidir.
ALMAS   = []
VIDRO   = []

# ── o cabeçalho de cada bloco: medida geral e a cadeia que fecha ────────
CABECA = {
 I1: ('245 × 90 × 110',
      'VISTA FRONTAL 5 + 2+60+2+69+38+2+60+2 + 5 = 245 ⭐ · altura 5 + 85 = 90 · '
      'VISTA SUPERIOR 122 + 122 = 244 ≈ 245 · módulo de 60 fecha 18 + 18 + 52 = 88'),
 I2: ('torre 110 × 300 × 80 · superiores 405 × 103 × 67 e 405 × 40 × 37',
      '⭐ três detalhamentos num item só [Jonathan 28/10] · torre 10 + 46 + 46 + 3 + 194 = 300 · '
      'superiores em módulos de 77 + 65 + 71 + 65 + 77 + 50 = 405 · interno 2+74+2+63+2+69+2+63+2+75+2+47+2 = 405'),
 I3: ('405 × 90 × 60 · sendo 343 de marcenaria',
      '⭐ VISTA FRONTAL 215 + 62 + 128 = 405, e o 62 é o VÃO DO LAVA-LOUÇAS: de marcenaria '
      'são 343, que fecham em 95 + 35 + 85 + 68 + 60 = 343 · altura 5 + 80 + 5 = 90 · frentes 40 + 40 = 80'),
}

# ── a folha: o que é texto da aba, e só dela ────────────────────────────
FOLHA = dict(
 aba='COZINHA',
 sub='Jéssica e Michell · Projeto ICA · páginas 028 a 042 · três itens · '
     'caixaria em Branco TX 15, e em cor só o que se vê: as frentes, a '
     'lateral aparente da ilha e o ripado · 16 portas e gavetões '
     'provençais, 15 mm de base com moldura de 6 mm · 17 básculas lisas '
     f'· peça inteira até {ALT_MAX:g}, que é a chapa de {CHAPA_C:g} menos '
     'o acerto de corte',
 # ⭐ só o TEXTO de cada padrão. A LISTA sai das peças, em aba.py: assim um
 #   padrão novo (e a frente provençal criou quatro) nunca fica de fora da
 #   compra por eu ter esquecido de acrescentar uma linha aqui.
 chapa_txt={VF:   'Linha Velluto · lateral aparente da ilha',
            VF15: 'Linha Velluto · base das frentes provençais',
            VF6:  'Linha Velluto · moldura usinada, peça inteira sobre a base',
            JR:   'Linha Essencial Wood · básculas e ripado',
            JR15: 'Linha Essencial Wood · base da porta de giro',
            JR6:  'Linha Essencial Wood · moldura usinada, peça inteira',
            EST:  'Estrutura e caixaria · o padrão da Base para caixaria',
            PRAT18:'Prateleira da torre · vão de 104, 18 mm contra empeno',
            FUN:  'Fundos · encaixe em rasgo, sem fita'},
 nota='⛔ O FRETE ESTÁ ZERADO DE PROPÓSITO: as linhas de frete da Base não '
      'têm preço ainda. Preencher lá e elas aparecem aqui sozinhas.   '
      '⭐⭐ NOVE PADRÕES DE CHAPA, NOVE ARREDONDAMENTOS: cada cor × '
      'espessura é uma compra separada e puxa no mínimo uma chapa, mesmo '
      'que leve uma peça só. A frente provençal criou quatro padrões novos '
      '(15 mm de base e 6 mm de moldura, em duas cores), e QUATRO dos nove '
      'padrões levam uma chapa inteira para menos de 1,9 m² de peça: são '
      'R$ 2.000 de chapa para 3,66 m² cortados. ⚠ É onde a mistura de cor '
      'fica mais cara que a peça — vale olhar junto com a Lavanderia, que '
      'é inteira provençal e pode dividir a sobra.',
 duvidas=[
  'A TORRE DA GELADEIRA foi desenhada com 300 e a chapa dá 273. Rebaixei '
  'lateral e fundo, e sobram 27 cm abertos no topo. É a mesma decisão que o '
  'senhor fechou para as colunas do Living, mas aqui ela ainda não foi '
  'tomada. ⚠ Rebaixa, emenda, ou fecha com arremate?',
  'A CAVA SAIU quando o puxador entrou, e essa parte eu INFERI. A prancha '
  'pede puxador Alças Traso E cava frontal usinada na mesma frente; frente '
  'não abre de dois modos, então tirei a cava. ⚠ Confirmar — se a cava '
  'voltar, somam R$ 476,50.',
  'O ACABAMENTO DO ALÇAS TRASO 128 mm decide R$ 860. A busca de varejo achou '
  'de R$ 44,92 a R$ 109,22: preto por volta de R$ 54 a 62, dourado R$ 84,54, '
  'níquel velho R$ 109,22. Os R$ 110 que o senhor passou caem no níquel '
  'velho. ⚠ Qual acabamento vai?',
  'A USINAGEM DA MOLDURA PROVENÇAL não tem preço na Base e são 16 frentes '
  'aqui, mais 31 na Lavanderia. Sai ZERO e o orçamento denuncia. ⛔ Até ela '
  'existir este custo é um PISO. ⚠ Agora o que se cronometra é o tempo de ROUTER por frente, não a montagem de travessa.',
  'UMA PORTA CUSTA R$ 900 DE CHAPA. A porta de giro do Superior 01 é a única '
  'peça nos padrões Jequitibá Rosa 15 e 6, e cada um puxa uma chapa inteira: '
  'R$ 550 mais R$ 350 para 0,67 m² de peça. ⚠ Se ela virar lisa como as '
  'básculas ao lado, esses R$ 900 saem. É decisão de desenho.',
  'LATERAIS DE 3 CM na torre e nos superiores. MDF não existe em 30 mm: ou se '
  'colam duas chapas, e aí DOBRA a chapa dessas peças e entra laminação de '
  'topo, ou se faz caixão. Orcei como CAIXÃO em 18 mm simples. ⚠ É a decisão '
  'mais cara do projeto e aparece em quase todo ambiente.',
  'NÃO LI AS PÁGINAS 031 a 033 — não estavam no cache de folhas soltas. São '
  'elevações, não detalhamentos, mas convém conferir se trazem algo que o '
  'quantitativo não pegou.'],
 nao_marcenaria=[
  'Tampo da ilha e bancada em Quartzito Bianco Superiore — pedra, e o recorte é nosso mas a pedra não',
  'Cuba dupla inox 86 × 44, torneira monocomando e escorredor de calha úmida',
  'Coifa downdraft de bancada, forno elétrico, cooktop de indução, micro-ondas, lava-louças e torre de tomadas'],
 notas=[
  '⭐⭐ A MOLDURA PROVENÇAL É PEÇA INTEIRA USINADA, NÃO RÉGUA COLADA. '
  '[Jonathan, 28/10/2026] "nao considere reguas, considere outra peça de '
  'igual tamanho pois é retirada uma peça inteira e feito a usinagem na '
  'router". Eu montava a moldura com quatro travessas de 7 cm em volta da '
  'frente; a fábrica tira um RETÂNGULO CHEIO de 6 mm, do tamanho da frente, '
  'e usina o relevo. Três coisas mudaram: a chapa de 6 mm subiu (na frente '
  'de 60 × 85 eram 0,20 m² de régua e agora são 0,51 m² de peça), a '
  'FILETAGEM MANUAL SUMIU das frentes (o 6 vai colado sobre o 15 e o '
  'conjunto de 21 mm entra na coladeira no automático) e a premissa da '
  'largura da travessa deixou de existir. Líquido: a Cozinha caiu de '
  'R$ 21.473,93 para R$ 21.090,35 de custo direto.',
  '⛔ A TORRE DA GELADEIRA FOI DESENHADA COM 300 e a chapa dá 273: lateral e '
  'fundo foram rebaixados, e sobram 27 cm abertos no topo. É a mesma decisão '
  'que o senhor fechou com o cliente para as colunas do Living — aqui ela '
  'ainda não foi tomada.',
  '⭐ RESOLVIDO O PUXADOR, E A CAVA SAIU. [Jonathan, 28/10/2026] Cada frente '
  'abre de um modo só: báscula com articulador HK-XS Blum mais puxador slim '
  'Rometal de R$ 35 — sem pulsador, que não se soma ao slim —, e porta ou '
  'gavetão com puxador Alças Traso de 128 mm a R$ 110. A prancha pedia o '
  'puxador E a cava usinada na mesma frente; com o puxador precificado, quem '
  'sai é a cava. ⚠ Essa última parte eu inferi, e vale confirmar.',
  '⚠ O PREÇO DO PUXADOR, CONFERIDO NO VAREJO HOJE: o Alças Traso 128 mm '
  'aparece de R$ 44,92 a R$ 109,22, conforme acabamento e loja — preto por '
  'volta de R$ 54 a R$ 62, dourado R$ 84,54, níquel velho R$ 109,22. Os '
  'R$ 110 adotados são o topo da faixa, que é onde cai o níquel velho; a '
  'Base trazia R$ 56,69, que é a média do PRETO. ⭐ Não é divergência, é '
  'outro acabamento — mas em 16 frentes a escolha vale R$ 860.',
  '⛔ A MÃO DE OBRA DE MOLDURA PROVENÇAL NÃO TEM PREÇO, e são 16 frentes. A '
  'linha existe na Base ("Moldura provençal na frente", por frente) e está '
  'vazia de propósito: o orçamento mostra zero e denuncia. Enquanto isso '
  'este custo é um PISO. A meia hora de marceneiro por frente, a R$ 36 a '
  'hora, seriam R$ 288; a uma hora, R$ 576. ⭐ Vale cronometrar uma na '
  'fábrica antes de a Lavanderia chegar, que tem 31 frentes dessas.',
  '⚠ UMA PORTA EM JEQUITIBÁ ROSA CUSTA R$ 900 DE CHAPA. A porta de giro do '
  'Superior 01 é a única peça nos padrões Jequitibá Rosa 15 e 6, e cada um '
  'puxa uma chapa inteira: R$ 550 mais R$ 350 para 0,67 m² de peça. Se ela '
  'virar lisa, como as básculas ao lado, esses R$ 900 saem. A decisão é de '
  'desenho, não de corte.',
  '⚠ LATERAIS DE 3 CM na torre e nos superiores. MDF não existe em 30 mm: ou '
  'se colam duas chapas, e aí DOBRA a chapa dessas peças e entra laminação de '
  'topo, ou se faz caixão. Orçado como caixão, em 18 mm simples. É a decisão '
  'mais cara do projeto e aparece em quase todo ambiente.',
  '⚠ NÃO LI AS PÁGINAS 031 a 033: não estavam no cache de folhas soltas. São '
  'elevações, não detalhamentos, mas convém conferir se trazem algo que o '
  'quantitativo não pegou.'],
)
