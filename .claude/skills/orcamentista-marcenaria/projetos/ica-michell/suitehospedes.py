# -*- coding: utf-8 -*-
"""ICA · SUÍTE HÓSPEDES — levantamento peça por peça  [28/10/2026]

páginas 104 a 117 · OITO detalhamentos, oito itens. O maior ambiente do
projeto em número de móveis.

⭐⭐ QUATRO PADRÕES APARENTES, e três deles entram no projeto AGORA:
      Oásis Linha Essencial Wood · Duratex .. o fio condutor: aparece em
                                             SETE dos oito itens
      Palha Indiana Sextavada Natural ....... fundo da cabeceira e frente
                                             das gavetas do aparador
      Palha · Duratex ....................... o painel ripado do DET 07
      Verde Floresta · Duratex .............. só o painel do DET 02
  ⛔ Nenhum dos três primeiros está nomeado na Base: entraram como
    melamínico fosco, que é a linha Duratex a que pertencem.

⭐⭐ DUAS MOLDURAS, E ELAS NÃO SÃO A MESMA COISA — é a distinção que este
  ambiente obriga a fazer:
    · DET 02, painel de cabeceira: moldura NA MESMA COR, relevo corrido.
      É a frente PROVENÇAL do método novo — peça inteira de 6 mm usinada
      na router sobre a base de 15.
    · DET 06, gavetas do aparador: moldura de 2 cm em OUTRA COR, Oásis
      sobre Palha Indiana. ⛔ Essa NÃO pode ser peça inteira: cobriria a
      palha. São quatro réguas por frente, e é o único lugar do projeto
      onde régua continua sendo régua.

⛔⛔ DUAS PEÇAS DE 300 DE ALTURA, as duas aparentes e as duas acima dos 273
  que a chapa dá: os montantes do espelho do DET 05 e o painel ripado do
  DET 07 inteiro. O painel se resolve dividindo nas linhas que o próprio
  desenho tem — 225 + 25 + 50 —, mas a moldura do espelho é peça única de
  300 por natureza.

⚠ O PUXADOR DE COURO COR FENDI do DET 03 não existe na Base. Sai ZERO.
"""
from base import (P, gaveta, provencal, ripado, acabamento, ALT_MAX,
                  CHAPA_C, DOBRADICA, ALTAS)

OA18, OA15 = 'MDF Oásis 18', 'MDF Oásis 15'
PI18 = 'MDF Palha Indiana Sextavada 18'
PA18, PA15 = 'MDF Palha 18', 'MDF Palha 15'
VF15, VF6 = 'MDF Verde Floresta 15', 'MDF Verde Floresta 6'
EST, FUN = 'MDF Branco TX 15', 'MDF Branco TX 6'

I1 = 'DET 01 Cabeceira'
I2 = 'DET 02 Painel de cabeceira'
I3 = 'DET 03 Mesa de cabeceira'
I4 = 'DET 04 Cama bicama de casal'
I5 = 'DET 05 Espelho'
I6 = 'DET 06 Aparador'
I7 = 'DET 07 Painel ripado'
I8 = 'DET 08 Mesa'

SUITEHOSPEDES = [
 # ══ ITEM 01 · CABECEIRA — 370 × 110 ══════════════════════════════════
 #  VISTA FRONTAL  5 + 82 + 5 + 182 + 5 + 86 + 5 = 370
 #                 altura 5 + 65 + 5 + 30 + 5 = 110
 #  ⭐ fundo em Palha Indiana, grade de réguas de 5 em Oásis por cima
 # ⭐⭐ A PALHA É PALHINHA NATURAL, NÃO CHAPA [Jonathan, 28/10/2026]: "na
 #   cabeceira vc nao considerou a palha indiana (650,00) o metro
 #   quadrado". ⛔ Eu a orçava como melamínico — uns R$ 137 o m² depois do
 #   aproveitamento — e ela custa R$ 650. Era cinco vezes menos, e era o
 #   fundo inteiro da cabeceira: 3,70 × 1,10 = 4,07 m². Sai da conta de
 #   chapa e entra como material de tapeceiro, trançado por trás da grade
 #   de réguas de Oásis.

 P('Painel de fundo', I1, 185, 110, 2, EST, (0, 0),
   '⭐ Substrato da PALHINHA NATURAL [Jonathan, 28/10/2026]: a palha '
   'indiana custa R$ 650 o m² e é tapeceiro, não chapa · a peça fica '
   'porque a palhinha precisa de fundo em que se fixar, mas sai no MDF '
   'estrutural · ⛔ sem fita: as arestas morrem sob a moldura'),
 P('Régua · travessa de topo e base', I1, 185, 5, 4, OA18, (2, 2),
   'Duas peças em cada, de ponta a ponta'),
 P('Régua · montante',      I1, 110, 5, 4, OA18, (2, 2),
   'As duas pontas mais as duas divisões internas, a 82 e a 269'),
 P('Régua · travessa interna', I1, 182, 5, 1, OA18, (2, 2),
   'Só no campo do meio, a 65 do topo — os campos de 82 e de 86 não a têm'),

 # ══ ITEM 02 · PAINEL DE CABECEIRA — 370 × 190 ════════════════════════
 #  VISTA FRONTAL  5 + 85 + 10 + 170 + 10 + 85 + 5 = 365 ≈ 370
 #                 altura 10 + 3 + 168 + 3 + 5 = 189 ≈ 190
 #  ⭐⭐ é PROVENÇAL: base de 15 mais moldura inteira de 6 usinada na router
 #  ⭐ a divisão sai nas linhas da moldura: 100 + 170 + 100, e aí a emenda
 #    cai debaixo da nervura de 10 e some
 *provencal('Painel · módulo lateral', I2, 100, 190, 2, VF15, VF6,
            'Provençal · ⭐ a emenda do painel de 370 cai debaixo da '
            'nervura de 10 da própria moldura'),
 *provencal('Painel · módulo central', I2, 170, 190, 1, VF15, VF6,
            'Provençal · o campo do meio, de 170'),

 # ══ ITEM 03 · MESA DE CABECEIRA — 56 × 50 × 45 ═══════════════════════
 #  VISTA FRONTAL  56 de largura · altura 22 + 22 + 5 = 49 ≈ 50
 #  VISTA LATERAL  45 de corpo mais 5 de recuo · profundidade 45, com 40
 #                 de base: os 5 da frente são o recuo do rodapé
 P('Lateral',               I3, 45, 45, 2, OA18, (1, 1), 'Aparente dos dois lados'),
 P('Base e topo',           I3, 52, 45, 2, OA18, (1, 1)),
 P('Fundo',                 I3, 56, 45, 1, FUN, (0, 0), 'Encaixe em rasgo'),
 P('Frente · gaveta',       I3, 56, 22, 2, OA18, (2, 2),
   'Duas de 56 × 22 · ⚠ abre por PUXADOR DE COURO cor fendi, que não '
   'existe na Base'),
 *gaveta(I3, 56, 40, 22, 2, 'Gaveta'),

 # ══ ITEM 04 · CAMA BICAMA DE CASAL — 207 × 165 × 33 ══════════════════
 #  VISTA SUPERIOR  207 × 165 · VISTA LATERAL altura 13 + 20 = 33
 #  ⭐ "rebaixo para colchão de casal" e um leito inferior corrediço
 P('Caixa · lateral',       I4, 207, 33, 2, OA18, (2, 2), 'Aparente'),
 P('Caixa · cabeceira e pé', I4, 162, 33, 2, OA18, (2, 2), 'Aparente'),
 # ⛔⛔ O ESTRADO DEIXOU DE SER MDF [Jonathan, 28/10/2026]: "Todas as camas
 #   teremos a aplicação de estrado em metalom, tanto para a superior
 #   quanto para a inferior. o custo de cada quadro é de 250,00". Saem os
 #   dois painéis de 15 mm e o sarrafo de pinus que os apoiava; entram
 #   dois quadros de metalon, que são serralheria.

 P('Leito inferior · frente', I4, 207, 20, 1, OA18, (2, 2),
   'Lisa, com cava na própria madeira'),
 P('Leito inferior · lateral', I4, 160, 20, 2, EST, (1, 0)),
 P('Leito inferior · costas', I4, 200, 20, 1, EST, (1, 0)),


 # ══ ITEM 05 · ESPELHO — 100 × 300 ════════════════════════════════════
 #  VISTA FRONTAL  10 + 80 + 10 = 100 · altura 10 + 280 + 10 = 300
 P('Moldura · montante',    I5, 300, 10, 2, OA18, (2, 2),
   '⛔ 300 de altura passa dos 273 que a chapa dá em peça inteira, e a '
   'moldura de um espelho é peça ÚNICA por natureza: emenda num montante '
   'de 10 de largura aparece'),
 P('Moldura · travessa',    I5, 80, 10, 2, OA18, (2, 2), 'Topo e base'),
 # ⭐ O PAINEL DE 6 MM ATRÁS DO ESPELHO [Jonathan, 28/10/2026]: "item 5 -
 #   considere o espelho com um painel de 6mm atras". Um espelho de 2,80 m
 #   não se cola na alvenaria: cola num painel, e o painel é que vai na
 #   parede. ⛔ 300 de altura não sai inteiro: duas faixas de 150, e a
 #   emenda fica ATRÁS do espelho, onde ninguém a vê.
 P('Painel de apoio do espelho · 6 mm', I5, 80, 150, 2, FUN, (0, 0),
   'É nele que o espelho cola · ⛔ sem fita: fica inteiramente escondido '
   'atrás do espelho e da moldura'),

 # ══ ITEM 06 · APARADOR — 165 × 25 × 52 ═══════════════════════════════
 #  VISTA FRONTAL  3 × 55 = 165 · altura 25 · VISTA LATERAL fundo 52
 #  ⭐ frente em Palha Indiana com moldura de 2 em Oásis — OUTRA COR, e
 #    por isso são QUATRO RÉGUAS por frente, não peça inteira
 P('Lateral',               I6, 25, 52, 2, OA18, (1, 1), 'Aparente: é suspenso'),
 P('Base e topo',           I6, 161, 52, 2, OA18, (1, 1), 'Aparente'),
 P('Divisória',             I6, 25, 52, 2, EST, (1, 0), 'Três vãos de 55'),
 P('Fundo',                 I6, 165, 25, 1, FUN, (0, 0), 'Encaixe em rasgo'),
 # ⭐ idem no aparador: 0,55 × 0,25 × 3 = 0,41 m² de palhinha natural,
 #   trançada dentro da moldura de 2 em Oásis

 P('Frente · gaveta · campo', I6, 55, 25, 3, EST, (0, 0),
   'Substrato da palhinha das três gavetas · ⛔ sem fita'),
 P('Frente · moldura · régua longa', I6, 55, 2, 6, OA18, (2, 2),
   '⛔ MOLDURA DE OUTRA COR: duas réguas de 2 em Oásis por frente, em cima '
   'e embaixo · peça inteira cobriria a palha, então aqui régua é régua'),
 P('Frente · moldura · régua curta', I6, 21, 2, 6, OA18, (2, 2),
   'As duas laterais de cada frente'),
 *gaveta(I6, 55, 48, 25, 3, 'Gaveta'),

 # ══ ITEM 07 · PAINEL RIPADO — 250 × 300 ══════════════════════════════
 #  VISTA FRONTAL  4 + 57 + 4 + 57 + 4 + 57 + 4 + 57 + 4 = 248 ≈ 250
 #                 altura 225 + 25 + 50 = 300 · a faixa de 25 é onde o
 #                 aparador do DET 06 encosta ("projeção aparador", 165)
 P('Painel de base · faixa alta', I7, 125, 225, 2, PA15, (2, 2),
   '⛔ 250 × 300 não cabe de jeito nenhum na chapa de 275 × 185 · dividido '
   'nas linhas que o próprio desenho tem, e a emenda vertical cai debaixo '
   'da ripa do meio'),
 P('Painel de base · faixa do aparador', I7, 250, 25, 1, PA15, (2, 2),
   'A faixa de 25 onde o aparador encosta'),
 P('Painel de base · faixa baixa', I7, 250, 50, 1, PA15, (2, 2),
   'Os 50 de baixo, abaixo do aparador'),
 *ripado(I7, 250, 225, 4, 57, PA18,
         'Faixa alta · cinco ripas de 4 com vão de 57 · laminada nos dois lados'),
 *ripado(I7, 250, 50, 4, 57, PA18,
         'Faixa baixa · cinco ripas de 4 · laminada nos dois lados'),
 P('Ripa de 4 · faixa do aparador', I7, 4, 25, 2, PA18, (2, 2),
   '⭐ só as duas das pontas: no meio, nos 165 da projeção do aparador, '
   'a ripa não existe'),

 # ══ ITEM 08 · MESA — 187 × 75 × 45 ═══════════════════════════════════
 #  VISTA FRONTAL  187 por fora, 181 por dentro · altura 5 + 70 = 75
 #  VISTA SUPERIOR  profundidade 45 · ⚠ espessura desenhada 3
 P('Tampo',                 I8, 187, 45, 1, OA18, (2, 2),
   '⚠ a prancha desenha 3 cm de espessura e MDF não existe em 30 mm — '
   'orçado em 18, como as colunas do Living'),
 P('Pé lateral',            I8, 70, 45, 2, OA18, (2, 2),
   'Mesa-ponte: dois pés inteiros, sem travessa · ⚠ 187 de vão sem apoio '
   'no meio é muito para 18 mm'),
]

# ── ferragem, declarada item a item ─────────────────────────────────────
GAVETAS = [(I3, 'Mesa de cabeceira · duas gavetas de 22', 2, 400),
           (I6, 'Aparador · três gavetas de 25', 3, 450)]
PORTAS  = []
BASCULAS= []
#  ⭐ a cava corre a largura da frente do leito corrediço
CAVA    = [(I4, 'Frente do leito inferior da bicama', 1, 207)]
MOLDURA = [(I2, 'Os três módulos provençais do painel de cabeceira', 3)]
LED     = []
CABIDEIROS = []
SARRAFOS= []   # ⛔ pinus PROIBIDO · o estrado virou quadro de metalon
SUPORTES= []
ALMAS   = []
# ⭐ O ESPELHO ENTRA NA CONTA [Jonathan, 28/10/2026]. Estava em NÃO É
#   MARCENARIA, como vidraçaria de terceiro, e não devia: quem compra,
#   mede e instala é a casa. 80 × 280 = 2,24 m².
VIDRO   = [(I5, 'Espelho de 80 × 280 do DET 05 · colado no painel de 6 mm',
            1, 80, 280, 'Espelho')]
# ⭐ A MESA DO DET 08 PEDE SERRALHERIA [Jonathan, 28/10/2026]: "item 8 -
#   considere uma estrutura de serralheria para estruturar a mesa - custo
#   de 450". Era uma das dúvidas em aberto do ambiente — o tampo não se
#   sustentava sozinho — e agora tem resposta e tem preço.
SERRALHERIA = [(I8, 'Estrutura da mesa do DET 08', 450.0)]
# ⛔ o puxador de couro não existe na Base, e a corrediça de carga da bicama
#   existe mas está sem preço. As duas saem ZERO e denunciam.
OUTRAS  = [# ⭐ ESTRADO EM METALON · R$ 250 o quadro [Jonathan, 28/10/2026]
           (I4, 'Estrado em metalon', 'Dois quadros: o do colchão de casal '
            'de 204 × 162 e o do leito inferior de 200 × 160 · ⛔ substitui '
            'os dois painéis de MDF e o sarrafo que os apoiava', 2, 'quadro',
            'Estrado em metalon'),
           (I3, 'Puxador de couro', 'Cor fendi · duas gavetas da mesa de '
            'cabeceira · ⛔ A COTAR, não existe na Base', 2, 'un',
            'Puxador de couro'),
           (I4, 'Corrediça de carga', 'Leito inferior da bicama de casal · '
            '⛔ sem preço na Base', 1, 'par', 'Corrediça de carga'),
           # ⭐ PALHINHA NATURAL · R$ 650 o m² [Jonathan, 28/10/2026]
           (I1, 'Palhinha natural', 'O fundo inteiro da cabeceira, 370 × '
            '110 · trançada por trás da grade de réguas de 5 em Oásis · ⛔ '
            'é tapeceiro, não chapa: saiu da conta de MDF', 4.07, 'm²',
            'Palhinha natural'),
           (I6, 'Palhinha natural', 'O campo das três frentes de gaveta do '
            'aparador, 55 × 25 cada · trançada dentro da moldura de 2 em '
            'Oásis', 0.41, 'm²', 'Palhinha natural')]
# ⛔⛔ O PULSADOR DO APARADOR SAIU [Jonathan, 28/10/2026]: "item 6 - nao
#   considerou a palhinha e o projeto nao especifica abertura por toque".
#   Eu tinha suposto pulsador porque a frente é emoldurada e cava cortaria
#   a palha — mas supor abertura por toque onde a prancha não a desenha é
#   inventar ferragem. Entra o puxador que a casa usa quando o desenho não
#   manda outro, e a pergunta fica na caixa de dúvidas, onde devia estar.
PUXADORES = [(I6, 'Três gavetas do aparador · ⚠ a prancha não desenha '
              'puxador e não especifica toque', 3)]
# ⭐ nada da Suíte Hóspedes toca o chão: a cabeceira e o aparador são
#   suspensos, a cama apoia em pé recuado e o espelho vai na parede.

CABECA = {
 I1: ('370 × 110',
      'VISTA FRONTAL 5 + 82 + 5 + 182 + 5 + 86 + 5 = 370 · altura '
      '5 + 65 + 5 + 30 + 5 = 110 · ⭐ fundo em Palha Indiana Sextavada com '
      'uma grade de réguas de 5 em Oásis por cima'),
 I2: ('370 × 190',
      'VISTA FRONTAL 5 + 85 + 10 + 170 + 10 + 85 + 5 ≈ 370 · altura '
      '10 + 3 + 168 + 3 + 5 ≈ 190 · ⭐⭐ é PROVENÇAL: base de 15 mais '
      'moldura inteira de 6 usinada na router · dividido em 100 + 170 + 100, '
      'com a emenda debaixo da nervura'),
 I3: ('56 × 50 × 45',
      'VISTA FRONTAL 56 de largura · altura 22 + 22 + 5 ≈ 50 · VISTA '
      'LATERAL profundidade 45, com recuo de 5 na frente da base'),
 I4: ('207 × 165 × 33',
      'VISTA SUPERIOR 207 × 165, com rebaixo para colchão de casal · VISTA '
      'LATERAL altura 13 + 20 = 33, e os 20 são o leito inferior corrediço'),
 I5: ('100 × 300',
      'VISTA FRONTAL 10 + 80 + 10 = 100 · altura 10 + 280 + 10 = 300 · '
      '⛔ os montantes da moldura têm 300 e a chapa dá 273 em peça inteira'),
 I6: ('165 × 25 × 52',
      'VISTA FRONTAL 3 × 55 = 165 · altura 25 · VISTA LATERAL profundidade '
      '52 · ⭐ frente em Palha Indiana com moldura de 2 em Oásis, que é '
      'OUTRA COR e por isso sai em quatro réguas'),
 I7: ('250 × 300',
      'VISTA FRONTAL 4 + 57 + 4 + 57 + 4 + 57 + 4 + 57 + 4 ≈ 250 · altura '
      '225 + 25 + 50 = 300 · a faixa de 25 é onde o aparador do DET 06 '
      'encosta, e a prancha a marca como "projeção aparador", 165 de largura'),
 I8: ('187 × 75 × 45',
      'VISTA FRONTAL 187 por fora e 181 por dentro · altura 5 + 70 = 75 · '
      'VISTA SUPERIOR profundidade 45 · ⚠ espessura desenhada 3'),
}

FOLHA = dict(
 aba='SUÍTE HÓSPEDES',
 sub='Jéssica e Michell · Projeto ICA · páginas 104 a 117 · OITO itens, o '
     'maior ambiente do projeto em número de móveis · ⭐ quatro padrões '
     'aparentes, com o Oásis Linha Essencial Wood em sete dos oito · '
     f'caixaria em Branco TX 15 · peça inteira até {ALT_MAX:g}, que é a '
     f'chapa de {CHAPA_C:g} menos o acerto de corte',
 chapa_txt={OA18: 'Oásis Linha Essencial Wood · Duratex · o fio condutor: sete dos oito itens',
            PI18: 'Palha Indiana Sextavada Natural · fundo da cabeceira e frente das gavetas',
            PA18: 'Palha · Duratex · as ripas de 4 do painel do DET 07',
            PA15: 'Palha · Duratex · o painel de base atrás das ripas',
            VF15: 'Verde Floresta · base das frentes provençais do DET 02',
            VF6:  'Verde Floresta · moldura usinada, peça inteira sobre a base',
            EST:  'Estrutura e caixaria · o padrão da Base para caixaria',
            FUN:  'Fundos · encaixe em rasgo, sem fita'},
 nota='⛔ O FRETE ESTÁ ZERADO DE PROPÓSITO: as linhas de frete da Base não '
      'têm preço ainda. Preencher lá e elas aparecem aqui sozinhas.   '
      '⭐⭐ DUAS MOLDURAS, E ELAS NÃO SÃO A MESMA COISA. No DET 02 a moldura '
      'é na MESMA COR e sai como PROVENÇAL — peça inteira de 6 mm usinada '
      'na router sobre a base de 15. Nas gavetas do DET 06 ela é de 2 cm em '
      'OUTRA COR, Oásis sobre Palha Indiana, e aí peça inteira cobriria a '
      'palha: são quatro réguas por frente, e é o ÚNICO lugar do projeto '
      'onde régua continua sendo régua.   ⛔ DUAS PEÇAS DE 300 DE ALTURA, as '
      'duas aparentes: os montantes do espelho do DET 05 e o painel do '
      'DET 07. O painel se resolve nas linhas do próprio desenho; a moldura '
      'do espelho, não.',
 duvidas=[
  'A MOLDURA DO ESPELHO TEM 300 DE ALTURA e a chapa dá 273 em peça inteira. '
  '⛔ Uma moldura de espelho é peça ÚNICA por natureza, e emenda num montante '
  'de 10 de largura APARECE. ⚠ As saídas: espelho de 273, moldura em duas '
  'peças com a emenda assumida, ou moldura em madeira maciça, que não é '
  'chapa e não está nesta conta. Decisão de desenho.',
  'O PAINEL DO DET 07 TEM 250 × 300 e não cabe na chapa de nenhum jeito. '
  'Dividi nas linhas que o próprio desenho tem — 225 de campo, 25 da '
  'projeção do aparador e 50 de baixo — e a emenda vertical da faixa alta '
  'cai debaixo da ripa do meio. ⚠ Confirmar que as duas emendas horizontais '
  'podem ficar onde estão: a de cima fica a 75 do chão, atrás do aparador.',
  'O PUXADOR DE COURO COR FENDI das gavetas da mesa de cabeceira NÃO EXISTE '
  'na Base. Sai ZERO. ⚠ Puxador de couro é item de ferragem fina, costuma '
  'custar de R$ 40 a R$ 120 a unidade, e são dois. ⛔ Até existir, o custo '
  'da mesa de cabeceira é um PISO.',
  'A CORREDIÇA DE CARGA DA BICAMA DE CASAL é a mesma do Quarto: a linha '
  'existe na Base e está sem preço. Sai ZERO. ⚠ E aqui o leito é de CASAL, '
  '200 × 160, bem mais pesado que o de solteiro do Quarto.',
  'TRÊS PADRÕES NOVOS DE CHAPA, e nenhum nomeado na Base: Oásis Linha '
  'Essencial Wood, Palha Indiana Sextavada Natural e Palha, todos Duratex. '
  'Lancei os três como melamínico fosco, R$ 700 a chapa de 18. ⚠ Confirmar '
  '— padrão de palha costuma ser linha especial e pode custar mais.',
  'A "PALHA INDIANA SEXTAVADA NATURAL" e a "PALHA" são dois padrões '
  'diferentes na prancha: a primeira no DET 01 e no DET 06, a segunda no '
  'DET 07. ⚠ Se forem a mesma chapa, são duas compras que viram uma e o '
  'arredondamento cai. Se forem diferentes mesmo, estão certas como estão.',
  'A MESA DO DET 08 É UMA PONTE DE 187 DE VÃO, sem travessa e sem apoio no '
  'meio, desenhada com 3 cm de espessura. ⚠ Orçada em 18 mm, e 18 mm não '
  'vence 1,87 m de vão sem empenar. Ou vai a 25 mm, ou leva travessa, ou é '
  'caixão como o tampo do Home Office. É decisão estrutural.',
  'O APARADOR DO DET 06 NÃO TEM PUXADOR DESENHADO nas três gavetas, e a '
  'prancha não escreve cava nem puxador. ⚠ Orcei só a corrediça. É a mesma '
  'lacuna da porta ripada do Banho Gourmet.',
  'O ESPELHO DE 80 × 280 do DET 05 não é nosso: é vidraceiro. ⚠ A moldura '
  'é, e ela precisa de rebaixo para o espelho encaixar. Confirmar quem mede '
  'e quem instala — um espelho de 2,80 m não sobe sozinho.',
  '⛔ A BASE METÁLICA DE 3 CM aparece nas quinze folhas daqui e continua NÃO '
  'LANÇADA em nenhum ambiente — oito ambientes agora.'],
 nao_marcenaria=[
  'Espelho de 80 × 280 do DET 05 — vidraceiro',
  'Colchão de casal do DET 04 e colchão do leito inferior',
  'Puxador de couro cor fendi — item de ferragem fina, a cotar',
  'Roupa de cama, luminárias e decoração'],
 notas=[
  '⭐⭐ DUAS MOLDURAS, E ELAS NÃO SÃO A MESMA COISA. No DET 02 a moldura é na '
  'MESMA COR e corrida: é a frente PROVENÇAL do método novo, peça inteira de '
  '6 mm usinada na router sobre a base de 15. Nas gavetas do DET 06 a '
  'moldura tem 2 cm e é de OUTRA COR — Oásis sobre Palha Indiana. Peça '
  'inteira cobriria a palha, então ali são quatro réguas por frente. É o '
  'único lugar do projeto onde régua continua sendo régua.',
  '⭐⭐ QUATRO PADRÕES APARENTES NUM AMBIENTE SÓ, e o Oásis Linha Essencial '
  'Wood aparece em SETE dos oito itens — é o fio condutor da suíte. Os '
  'outros três entram em um ou dois móveis cada, e cada um puxa no mínimo '
  'uma chapa cheia.',
  '⛔ DUAS PEÇAS DE 300 DE ALTURA, as duas aparentes: os montantes do '
  'espelho do DET 05 e o painel ripado do DET 07. O painel se resolve nas '
  'linhas que o desenho já tem; a moldura do espelho é peça única por '
  'natureza e não tem divisão que não apareça.',
  '⭐ O ESTRADO DA BICAMA DE CASAL saiu em 15 mm, como no Quarto: carrega '
  'duas pessoas, não é fundo de gaveta. E aqui ele cabe inteiro na chapa — '
  '204 × 162 contra 275 × 185 — o que no Quarto não acontecia.',
  '⭐ O PAINEL DO DET 02 FOI DIVIDIDO EM 100 + 170 + 100, não em duas peças '
  'de 185. A divisão sai nas linhas da própria moldura, e aí a emenda cai '
  'debaixo da nervura de 10 e some. Dividir pelo meio poria a emenda no '
  'centro do campo de 170.'],
)
