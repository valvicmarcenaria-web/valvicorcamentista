# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO · CLOSET SUÍTE 02 FILHAS — peça por peça  [30/10/2026]

pranchas 61 e 62 · planta de layout, elevação A e elevação B.

⭐⭐ ARMÁRIO EM L, ABERTO, SEM PORTA — a mesma receita do Closet Master, e
  com o MESMO canto que aparece duas vezes. A elevação A cota 55 + 109 e a
  B cota 159 + 55: os dois "55" são o MESMO módulo de canto, o dos dois
  "cabideiros contínuos de canto".
     164 + 214 − 55 = 323 de armário, não 378.
  ⛔ Cinquenta e cinco centímetros de armário de 2,75 m comprados em dobro
    seriam cerca de R$ 1.700 — e nada na planilha acusaria.
  ⭐ Por isso o canto é ITEM SEPARADO, como na Suíte 01.

⭐ A CADEIA VERTICAL FECHA EM 275 nas duas paredes, e é a mesma do Closet
  Master: 10 de rodapé + 62 de maleiro + 2 + 191 de miolo + 10 de testeira.
  O 191 se abre em 109 + 2 + 80 onde há cabideiro, e em três vãos de 35
  mais quatro frentes de 20 na coluna de prateleira.

⛔⛔ A PORTA PIVOTANTE DE 72 NÃO ESTÁ AQUI. Ela é da Suíte 02 Filhas, onde
  está inteira — as duas faces, o quadro, o pivô e a tranca. Pagá-la aqui
  seria comprá-la duas vezes.

⛔ FORA: o forro e a iluminação, que nenhuma das duas pranchas desenha.
"""
from base import P, gaveta, CORREDICA

OWS18, OWS15, OWS6 = ('MDF Off-White Suave 18', 'MDF Off-White Suave 15',
                      'MDF Off-White Suave 6')

I1 = 'ELEVAÇÃO A Armário de 109'
I2 = 'ELEVAÇÃO B Armário de 159'
I3 = 'CANTO Módulo de canto do armário em L'

PROF, CORPO = 55.0, 255.0
CA = 52.5                  # as duas colunas da elevação A
CP, CC = 105.0, 50.0       # na B: a coluna de prateleira e a de cabideiro
CANTO = 52.0               # vão interno do módulo de 55

CLOSET_02 = [
 # ══ ITEM 01 · ARMÁRIO DA ELEVAÇÃO A — 109 × 275 × 55 ══════════════════
 P('Lateral e divisória vertical', I1, CORPO, PROF, 2, OWS15, (1, 0),
   '⭐ Uma lateral e uma divisória · a outra lateral é a do módulo de '
   'canto e está contada lá · DUAS colunas de 52,5'),
 P('Tampo e base', I1, CA, PROF, 4, OWS15, (1, 0)),
 P('Testeira superior', I1, 109, 10, 1, OWS15, (1, 0)),
 P('Rodapé',            I1, 109, 10, 1, OWS15, (1, 0)),
 P('Prateleira do maleiro', I1, CA, 53, 2, OWS18, (1, 0)),
 P('Prateleira', I1, CA, 53, 2, OWS18, (1, 0),
   '⭐ É ela que parte o 191 em 109 de cabideiro longo e 80 de curto'),
 P('Fundo', I1, CORPO, 109, 1, OWS6, (0, 0), 'Peça única · ⛔ sem fita'),

 # ══ ITEM 02 · ARMÁRIO DA ELEVAÇÃO B — 159 × 275 × 55 ══════════════════
 P('Lateral e divisória vertical', I2, CORPO, PROF, 3, OWS15, (1, 0),
   '⭐ Duas laterais e uma divisória · a coluna de 105 com prateleiras e '
   'frentes, a de 50 com dois cabideiros'),
 P('Tampo e base · coluna de 105', I2, CP, PROF, 2, OWS15, (1, 0)),
 P('Tampo e base · coluna de 50',  I2, CC, PROF, 2, OWS15, (1, 0)),
 P('Testeira superior', I2, 159, 10, 1, OWS15, (1, 0),
   '⭐ Peça única: 159 deitada cabe nos 275 da chapa'),
 P('Rodapé',            I2, 159, 10, 1, OWS15, (1, 0)),
 P('Prateleira do maleiro · coluna de 105', I2, CP, 53, 1, OWS18, (1, 0)),
 P('Prateleira do maleiro · coluna de 50',  I2, CC, 53, 1, OWS18, (1, 0)),
 P('Divisória da coluna de 105', I2, 109, PROF, 1, OWS15, (1, 0),
   '⭐ É ela que faz os dois 51,5 cotados · vai do maleiro ao topo das '
   'gavetas e PARA ali'),
 P('Prateleira', I2, 51.5, 53, 6, OWS18, (1, 0),
   '⭐ Três níveis de 35 × duas meias-colunas de 51,5'),
 P('Prateleira entre os dois cabideiros', I2, CC, 53, 1, OWS18, (1, 0)),
 P('Frente de gaveta', I2, CP, 20, 2, OWS15, (2, 2),
   'Puxador tipo CAVA na marcenaria'),
 P('Frente da sapateira deslizante', I2, CP, 20, 2, OWS15, (2, 2),
   '⛔ sem suporte: ela corre em corrediça'),
 *gaveta(I2, CP, 50, 18, 2, 'Caixa de gaveta'),
 *gaveta(I2, CP, 50, 18, 2, 'Caixa de gaveta · bandeja da sapateira'),
 P('Fundo', I2, CORPO, 79.5, 2, OWS6, (0, 0),
   '⛔ 159 de largura não cabe nos 185 da chapa junto com os 255 de '
   'altura: sai em DUAS de 79,5 · a emenda cai na divisória · sem fita'),

 # ══ ITEM 03 · MÓDULO DE CANTO — 55 × 55, UMA VEZ SÓ ═══════════════════
 P('Lateral do canto', I3, CORPO, PROF, 1, OWS15, (1, 0),
   '⭐ UMA só: do outro lado o canto encosta no armário de 159, cuja '
   'lateral já está contada lá'),
 P('Tampo e base', I3, CANTO, PROF, 2, OWS15, (1, 0)),
 P('Testeira superior', I3, 55, 10, 1, OWS15, (1, 0)),
 P('Rodapé',            I3, 55, 10, 1, OWS15, (1, 0)),
 P('Prateleira do maleiro', I3, CANTO, 53, 1, OWS18, (1, 0)),
 P('Prateleira',            I3, CANTO, 53, 1, OWS18, (1, 0)),
 P('Fundo', I3, CORPO, 55, 2, OWS6, (0, 0),
   '⭐ DUAS: o canto tem duas paredes atrás de si · ⛔ sem fita'),
]

# ⭐ (móvel, rótulo, nº de gavetas, preço do par)
GAVETAS = [
 (I2, 'Duas gavetas e duas sapateiras deslizantes de 105 × 20 · ⛔ a '
      'prancha pede TELESCÓPICA e ela sobe para a Hettich oculta', 4,
  CORREDICA),
]
# ⭐ (móvel, rótulo, nº de frentes, extensão de cava em cm por frente)
CAVA = [
 (I2, 'As quatro frentes de 105 — duas gavetas e duas sapateiras', 4, CP),
]
# ⭐ (móvel, rótulo, quantidade)
CABIDEIROS = [
 (I1, 'QUATRO: dois em cada coluna de 52,5, de 109 e de 80', 4),
 (I2, 'DOIS na coluna de 50, de 109 e de 80', 2),
 (I3, 'DOIS contínuos DE CANTO, de 109 e de 80 · ⭐ é o mesmo par que as '
      'elevações A e B desenham cada uma do seu lado', 2),
]
PORTAS = BASCULAS = PUXADORES = MOLDURA = ALMAS = []
LED = VIDRO = SERRALHERIA = []
# ⭐ (móvel, nome, rótulo, quantidade, unidade, chave)
OUTRAS = [
 (I1, 'Perfil de proteção de piso', 'O rodapé de 109 toca o chão', 1.09,
  'm', 'Perfil de proteção de piso'),
 (I2, 'Perfil de proteção de piso', 'O rodapé de 159 toca o chão', 1.59,
  'm', 'Perfil de proteção de piso'),
 (I3, 'Perfil de proteção de piso', 'O rodapé de 55 do canto toca o chão',
  0.55, 'm', 'Perfil de proteção de piso'),
]

CABECA = {
 I1: ('109 × 275 × 55',
      'ELEVAÇÃO A · armário ABERTO, sem porta · DUAS colunas de 52,5, cada '
      'uma com maleiro de 62 e dois cabideiros de 109 e 80'),
 I2: ('159 × 275 × 55',
      'ELEVAÇÃO B · armário ABERTO · coluna de 105 com seis prateleiras de '
      '51,5 e quatro frentes de 20, e coluna de 50 com dois cabideiros'),
 I3: ('55 × 55 × 275',
      '⛔ ESTE MÓDULO APARECE NAS DUAS ELEVAÇÕES E EXISTE UMA VEZ SÓ. A '
      'elevação A o cota ao lado dos seus 109 e a B ao lado dos seus 159. '
      '⭐ Somar as duas daria 378 de armário — o armário tem 323'),
}

FOLHA = dict(
 aba='CLOSET SUÍTE 02 FILHAS',
 sub='Gustavo Raposo · executivo Luiza Pacheco, pranchas 61 e 62 · ⭐ '
     'armário em L aberto em Off-White Suave, 3,23 m de frente, oito '
     'cabideiros e nenhuma porta',
 chapa_txt={
  OWS18: 'Off-White Suave · Linha Sense · Duratex · as catorze '
         'prateleiras e maleiros',
  OWS15: 'Off-White Suave · Linha Sense · Duratex · a estrutura inteira e '
         'as quatro frentes de 20',
  OWS6:  'Off-White Suave · Linha Sense · Duratex · os fundos dos três '
         'trechos',
  'MDF Branco TX 15': 'Branco TX · a caixaria das quatro gavetas e '
                      'bandejas',
 },
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a QUANTIDADE é '
      'a célula AMARELA no fim do painel de material, e ela sai ZERO.   '
      '⛔⛔ O CANTO É UM ITEM SEPARADO, e é de propósito: as duas '
      'elevações desenham o mesmo módulo de 55 dentro dos seus totais. '
      '164 + 214 = 378, e o armário tem 323.   '
      '⛔ A PORTA PIVOTANTE DE 72 NÃO ESTÁ AQUI: ela é da Suíte 02 Filhas, '
      'onde está inteira.   '
      '⭐ UM PADRÃO DE CHAPA SÓ, como no Closet Master: tudo Off-White '
      'Suave, Linha Sense.',
 duvidas=[
  '⚠ A PROFUNDIDADE DE 55 veio por semelhança com o Closet Master, cuja '
  'planta a cota. ⛔ A planta deste closet não a traz no corte que eu li. '
  'Conferir na medição: cada 5 cm mudam cerca de 0,9 m² de chapa.',
  '⚠ OS QUATRO CABIDEIROS DA ELEVAÇÃO A. A prancha desenha a barra '
  'atravessando as duas colunas de 52,5 nos dois níveis e rotula uma vez '
  'só. Lancei dois por coluna. ⛔ Se for barra única atravessando as duas, '
  'são dois cabideiros e não quatro — R$ 240 a menos.',
  '⚠ A LARGURA DAS COLUNAS saiu das cotas da prancha: 52,5 na elevação A, '
  '105 e 50 na B, 55 no canto. ⭐ Aqui a prancha cota as colunas uma a '
  'uma, o que é raro neste executivo.',
  '⚠ O CLOSET NÃO TEM ILUMINAÇÃO DESENHADA — nem fita, nem perfil, nem '
  'spot. É o mesmo silêncio do Closet Master. Num armário aberto de 3,23 m '
  'isso chama atenção; vale perguntar antes de o gesso fechar.',
 ],
 nao_marcenaria=[
  '⛔ A PORTA PIVOTANTE de 72 × 210 — e não por não ser marcenaria, mas '
  'por já estar PAGA na Suíte 02 Filhas. ⭐ Está escrita aqui para que '
  'ninguém a some duas vezes.',
  '⛔ O FORRO e a ILUMINAÇÃO, que as duas pranchas não desenham.',
 ],
 notas=[
  '⭐ É O GÊMEO MENOR DO CLOSET MASTER: mesma cadeia vertical, mesmo '
  'padrão de chapa, mesma ausência de porta e o mesmo canto em L. ⛔ A '
  'diferença é o tamanho — 3,23 m contra 4,97 m — e o número de frentes: '
  'quatro contra doze.',
  '⭐ NENHUMA PRATELEIRA PEDE ALMA DE AÇO: a maior tem 105 de vão e a '
  'regra da casa é 120. ⭐ A de 105 passou raspando.',
  '⭐ OITO CABIDEIROS E QUATRO PARES DE CORREDIÇA. É um closet de '
  'pendurar, não de guardar dobrado — e isso é coerente com o quarto ao '
  'lado, que não tem armário nenhum.',
 ],
)
