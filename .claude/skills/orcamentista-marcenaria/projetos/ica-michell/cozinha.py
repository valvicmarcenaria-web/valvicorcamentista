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
from base import (P, gaveta, ripado, fita_m, ALT_MAX, CHAPA_C, CHAPA_L,
                  CHAPA_M2, APROV, PRECO, FITA_CHEIA, FITA_PERD, CORREDICA,
                  DOBRADICA, BASCULA, PULSADOR, CAVA_M, PUXADOR, LED_M,
                  SUPORTE, CONSUM, EMBAL, ALTAS)

VERDE, ROSA = 'MDF cor 18', 'MDF cor 18'     # ⚠ mesmo preço, cores distintas
BRANCO, BR6 = 'MDF branco 18', 'MDF branco 6'
# ⭐ a chave carrega a COR para o arredondamento sair certo
VF, JR = 'MDF Verde Floresta 18', 'MDF Jequitibá Rosa 18'

I1 = 'DET 01 Ilha'
I2 = 'DET 02+03+04 Torre da geladeira e armários superiores'
I3 = 'DET 05 Bancada com armário'

COZINHA = [
 # ══ ITEM 01 · ILHA — 245 × 90 × 110 ═════════════════════════════════
 #  VISTA FRONTAL  5 + 2+60+2+69+38+2+60+2 + 5 = 245 ⭐ · altura 5 + 85 = 90
 #                 módulo de 60 fecha 18 + 18 + 52 = 88 · outro 38 + 38 = 76
 #  VISTA SUPERIOR 122 + 122 = 244 ≈ 245 ⭐ · VISTA POSTERIOR 5 + 235 = 240
 P('Lateral',              I1, 110, 85, 2, VF, (1, 0), 'Verde Floresta · Velluto'),
 P('Base e tampo de apoio', I1, 235, 110, 2, VF, (1, 0), 'O tampo recebe o quartzito — a pedra não é nossa'),
 P('Divisória',            I1, 110, 85, 4, BRANCO, (1, 0), 'Módulos de 60 · 69 · 38 · 60, com divisórias de 2'),
 P('Fundo',                I1, 235, 85, 1, BR6, (0, 0), 'Encaixe em rasgo'),
 P('Frente · gavetão',     I1, 60, 38, 2, VF, (2, 2), 'Cava frontal usinada'),
 P('Frente · gavetão',     I1, 60, 52, 1, VF, (2, 2), 'Cava frontal usinada'),
 P('Frente · gaveta',      I1, 60, 18, 2, VF, (2, 2), 'Cava frontal usinada'),
 P('Frente · porta',       I1, 69, 85, 1, VF, (2, 2), 'De giro, com cava'),
 P('Frente · porta tempero', I1, 38, 85, 1, VF, (2, 2), 'Cava frontal usinada'),
 *gaveta(I1, 60, 100, 38, 2, 'Gavetão'),
 *gaveta(I1, 60, 100, 52, 1, 'Gavetão alto'),
 *gaveta(I1, 60, 100, 18, 2, 'Gaveta'),
 *ripado(I1, 235, 85, 3, 3, JR,
         'Vista posterior ripada em Jequitibá Rosa · ripa de 3 com vão de 3'),

 # ══ ITEM 02 · TORRE E SUPERIORES ════════════════════════════════════
 #  ⭐ mesclados a pedido do Jonathan. Mesmo padrão, mesma parede.
 #  TORRE 110 × 300 × 80 · cadeia 10 + 46 + 46 + 3 + 194 = 300 ⭐
 P('Torre · lateral',      I2, 80, 300, 2, JR, (1, 0), '⛔ desenhada com 300: a chapa dá 273'),
 P('Torre · fundo',        I2, 104, 300, 1, BR6, (0, 0), 'Encaixe em rasgo · ⛔ 300'),
 P('Torre · base e topo',  I2, 104, 80, 2, JR, (1, 0)),
 P('Torre · tampo do nicho', I2, 104, 80, 1, BRANCO, (1, 0), 'A 194 do chão, sobre a geladeira de 596 L'),
 P('Torre · prateleira',   I2, 104, 80, 1, BRANCO, (1, 0), 'Entre as duas básculas de 46'),
 P('Torre · báscula',      I2, 104, 46, 2, JR, (2, 2), 'Fecho toque'),
 #  SUPERIOR 01 · 405 × 103 × 67 · módulos 77+65+71+65+77+50 = 405 ⭐
 #                interno 2+74+2+63+2+69+2+63+2+75+2+47+2 = 405 ⭐
 P('Superior 01 · base e topo', I2, 203, 67, 4, JR, (1, 0), 'Os 405 em dois módulos de 203'),
 P('Superior 01 · lateral', I2, 67, 103, 2, JR, (1, 0)),
 P('Superior 01 · divisória', I2, 67, 93, 5, BRANCO, (1, 0)),
 P('Superior 01 · prateleira', I2, 70, 67, 6, BRANCO, (1, 0), 'Uma por vão'),
 P('Superior 01 · báscula', I2, 70, 46, 9, JR, (2, 2), 'Nove basculantes, fecho toque'),
 P('Superior 01 · porta de giro', I2, 47, 103, 1, JR, (2, 2), 'Módulo de 50'),
 #  SUPERIOR 02 · 405 × 40 × 37 · mesma cadeia de módulos · com LED
 P('Superior 02 · base e topo', I2, 203, 37, 4, JR, (1, 0), 'Os 405 em dois módulos'),
 P('Superior 02 · lateral', I2, 37, 40, 2, JR, (1, 0)),
 P('Superior 02 · divisória', I2, 37, 40, 5, BRANCO, (1, 0)),
 P('Superior 02 · báscula', I2, 67, 40, 6, JR, (2, 2), 'Seis basculantes, uma por módulo'),

 # ══ ITEM 03 · BANCADA COM ARMÁRIO — 405 × 90 × 60 ═══════════════════
 #  ⭐ VISTA FRONTAL 215 + 62 + 128 = 405, e o 62 é o VÃO DO LAVA-LOUÇAS:
 #    de marcenaria são 343, que fecham em 95 + 35 + 85 + 68 + 60 = 343 ⭐
 #  altura 5 + 80 + 5 = 90 · frentes 40 + 40 = 80 (gavetão duplo)
 #  VISTA SUPERIOR profundidade 55 + 5 = 60
 P('Base e tampo de apoio', I3, 172, 60, 4, VF, (1, 0), 'Os 343 em dois módulos · o tampo recebe o quartzito'),
 P('Fundo',                I3, 172, 80, 2, BR6, (0, 0), 'Encaixe em rasgo'),
 P('Lateral e divisória',  I3, 60, 80, 6, BRANCO, (1, 0), 'Cinco módulos: 95 · 35 · 85 · 68 · 60'),
 P('Frente · gavetão',     I3, 95, 40, 2, VF, (2, 2), 'Cava frontal usinada'),
 P('Frente · gavetão',     I3, 85, 40, 2, VF, (2, 2), 'Cava frontal usinada'),
 P('Frente · gavetão',     I3, 68, 40, 2, VF, (2, 2), 'Cava frontal usinada'),
 P('Frente · gavetão de lixeira', I3, 60, 80, 1, VF, (2, 2), 'Módulo de 60, altura cheia'),
 P('Frente · porta tempero', I3, 35, 80, 1, VF, (2, 2), 'Módulo de 35'),
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
CAVA    = [(I1, 'Frentes da ilha',    7, 55), (I3, 'Frentes da bancada', 8, 71)]
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
     'Verde Floresta na ilha e na bancada, Jequitibá Rosa nos armários, '
     f'Branco no interno · peça inteira até {ALT_MAX:g}, que é a chapa de '
     f'{CHAPA_C:g} menos o acerto de corte',
 chapas=[(VF,     'Linha Velluto · ilha e bancada'),
         (JR,     'Linha Essencial Wood · armários, ripado e básculas'),
         (BRANCO, 'Divisórias, prateleiras e caixa de gaveta'),
         (BR6,    'Fundos · encaixe em rasgo, sem fita')],
 nota='⛔ O FRETE ESTÁ ZERADO DE PROPÓSITO: as quatro linhas de frete da '
      'Base não têm preço ainda. Preencher lá e elas aparecem aqui sozinhas.'
      '   ⭐ QUATRO PADRÕES DE CHAPA, QUATRO ARREDONDAMENTOS: cada cor é uma '
      'compra separada e puxa no mínimo uma chapa, mesmo que leve uma peça '
      'só. Somar a fração e arredondar no fim subestima a compra — e justo '
      'os projetos de arquiteta, que misturam cor, é onde isso dói.',
 nao_marcenaria=[
  'Tampo da ilha e bancada em Quartzito Bianco Superiore — pedra, e o recorte é nosso mas a pedra não',
  'Cuba dupla inox 86 × 44, torneira monocomando e escorredor de calha úmida',
  'Coifa downdraft de bancada, forno elétrico, cooktop de indução, micro-ondas, lava-louças e torre de tomadas'],
 notas=[
  '⛔ A TORRE DA GELADEIRA FOI DESENHADA COM 300 e a chapa dá 273: lateral e '
  'fundo foram rebaixados, e sobram 27 cm abertos no topo. É a mesma decisão '
  'que o senhor fechou com o cliente para as colunas do Living — aqui ela '
  'ainda não foi tomada.',
  '⚠ PUXADOR OU CAVA? A prancha desenha cava frontal usinada em toda frente, '
  'e foi assim que orçamos. Mas a Base registra "Puxador Alças Traso 416 mm · '
  'ICA · toda frente da Cozinha e da Lavanderia", a R$ 172,71. São 15 '
  'frentes: trocar cava por puxador acrescenta R$ 2.590,65 de puxador e tira '
  'R$ 476,50 de usinagem — líquido de R$ 2.114,15 a mais.',
  '⚠ LATERAIS DE 3 CM na torre e nos superiores. MDF não existe em 30 mm: ou '
  'se colam duas chapas, e aí DOBRA a chapa dessas peças e entra laminação de '
  'topo, ou se faz caixão. Orçado como caixão, em 18 mm simples. É a decisão '
  'mais cara do projeto e aparece em quase todo ambiente.',
  '⚠ NÃO LI AS PÁGINAS 031 a 033: não estavam no cache de folhas soltas. São '
  'elevações, não detalhamentos, mas convém conferir se trazem algo que o '
  'quantitativo não pegou.'],
)
