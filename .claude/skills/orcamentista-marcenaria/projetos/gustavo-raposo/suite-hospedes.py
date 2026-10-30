# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO · ANEXO SUÍTE HÓSPEDES — peça por peça  [30/10/2026]

pranchas 66, 67 e 68 · planta de layout, elevação A e elevação B em vista
externa e vista interna do armário.

⭐⭐ UM ÚNICO MÓVEL em três pranchas: o armário de 166 × 260 × 60. A
  elevação A é papel de parede, duas arandelas e tomada — nada nosso.

⛔⛔ E O PÉ-DIREITO AQUI É 260, NÃO 275. O anexo é mais baixo que a casa, e
  isso muda a cadeia inteira: 10 de rodapé + 240 de corpo + 10 de testeira.
  ⭐ As folhas de correr têm 240 e não 255 — se alguém copiar a folha de
    outro quarto, ela não entra.

⭐ A CADEIA VERTICAL FECHA EM 260:
     10 + 47 de maleiro + 2 + 191 de miolo + 10
  e o 191 se abre em três vãos de 35 entre prateleiras na coluna da
  esquerda, e em 109 de cabideiro mais prateleira na da direita — com
  quatro frentes de 20 embaixo nas DUAS colunas.

⭐ DUAS FOLHAS DE CORRER FLUTUANTES, as duas em MDF, sistema SS-150 SEM
  amortecedor, puxador NEO32 Bronze. ⛔ Aqui não há espelho: é o único
  armário de correr da casa sem folha espelhada.

⛔ FORA: o papel de parede · a cama de casal · o rack e as mesas laterais,
  "a serem adquiridos" · o tapete orgânico de 240 × 320 · as duas
  arandelas e a elétrica.
"""
from base import P, gaveta, CORREDICA

OWS18, OWS15 = 'MDF Off-White Suave 18', 'MDF Off-White Suave 15'
BR18, BR15, BR6 = 'MDF branco 18', 'MDF branco 15', 'MDF Branco TX 6'

I1 = 'ELEVAÇÃO B Armário de 166'

LARG, ALT, PROF = 166.0, 260.0, 60.0
CORPO = ALT - 20.0            # 240 · entre o rodapé e a testeira, ambos 10
COL = (LARG - 4.5)/2          # 80,75 · duas colunas, duas laterais e uma
                              #   divisória de 1,5

SUITE_HOSPEDES = [
 P('Lateral e divisória vertical', I1, CORPO, PROF, 3, OWS15, (1, 0),
   '⭐ Duas laterais e uma divisória · DUAS colunas de 80,75 · ⛔ 240 de '
   'altura, não 255: o anexo tem pé-direito de 260'),
 P('Tampo e base', I1, COL, PROF, 4, OWS15, (1, 0)),
 P('Testeira superior', I1, LARG, 10, 1, OWS15, (1, 0),
   '⭐ Peça única: 166 deitada cabe nos 275 da chapa'),
 P('Rodapé',            I1, LARG, 10, 1, OWS15, (1, 0)),
 P('Prateleira do maleiro', I1, COL, 58, 2, BR18, (1, 0),
   '⭐ O maleiro aqui tem 47 e não 62: o armário é 15 cm mais baixo'),
 P('Prateleira', I1, COL, 58, 4, BR18, (1, 0),
   '⭐ Três na coluna da esquerda, nos vãos de 35, e uma na da direita, '
   'fechando o cabideiro de 109'),
 P('Frente de gaveta', I1, COL, 20, 4, BR15, (2, 2),
   '⭐ Duas em cada coluna · puxador tipo CAVA na marcenaria · interno em '
   'MDF Branco, que é a chamada da prancha'),
 P('Frente da sapateira deslizante', I1, COL, 20, 4, BR15, (2, 2),
   '⭐ Duas em cada coluna · ⛔ sem suporte: ela corre em corrediça'),
 *gaveta(I1, COL, 55, 18, 4, 'Caixa de gaveta'),
 *gaveta(I1, COL, 55, 18, 4, 'Caixa de gaveta · bandeja da sapateira'),
 P('Fundo', I1, CORPO, 83, 2, BR6, (0, 0),
   '⛔ 166 de largura não cabe nos 185 da chapa junto com os 240 de '
   'altura: sai em DUAS de 83 · a emenda cai na divisória · sem fita'),
 P('Frente · porta de correr', I1, 85, CORPO, 2, OWS18, (2, 2),
   '⭐ Duas folhas de 85 × 240, com 4 de sobreposição nos 166 · 18 mm '
   'porque folha de 2,40 m pendurada em trilho empena com 15 · '
   '⛔ flutuante, sem moldura · puxador NEO32 Bronze'),
]

GAVETAS = [
 (I1, 'Quatro gavetas e quatro sapateiras deslizantes de 80,75 × 20 · '
      '⛔ a prancha pede TELESCÓPICA e ela sobe para a Hettich oculta, '
      'que é a regra da casa', 8, CORREDICA),
]
CAVA = [
 (I1, 'As oito frentes de 80,75 — quatro gavetas e quatro sapateiras',
  8, COL),
]
CABIDEIROS = [
 (I1, 'UM, de 109, na coluna da direita', 1),
]
PORTAS = BASCULAS = PUXADORES = MOLDURA = ALMAS = []
LED = VIDRO = SERRALHERIA = []
# ⭐⭐ DOIS MODOS DE ABRIR NO MESMO MÓVEL: a folha de correr abre pelo
#   NEO32 e as gavetas de dentro por cava. São frentes diferentes.
ABRE_MISTO = [I1]
OUTRAS = [
 (I1, 'Sistema de correr SS-150',
  '⭐ Um conjunto para as duas folhas · a prancha crava "sem '
  'amortecedor"', 1, 'conjunto', 'Sistema de correr SS-150'),
 (I1, 'Puxador NEO32 Bronze',
  '⛔ Duas folhas · A COTAR: a Base traz a linha SEM PREÇO e ela sai zero '
  'de propósito, para gritar', 2, 'un', 'Puxador NEO32 Bronze'),
 (I1, 'Perfil de proteção de piso', 'O rodapé de 166 toca o chão', 1.66,
  'm', 'Perfil de proteção de piso'),
]

CABECA = {
 I1: ('166 × 260 × 60',
      'ELEVAÇÃO B · ⛔ PÉ-DIREITO DE 260, não 275: o anexo é mais baixo '
      'que a casa · 10 de rodapé + 47 de maleiro + 2 + 191 de miolo + 10 '
      'de testeira · DUAS colunas de 80,75, uma com três vãos de '
      'prateleira e outra com cabideiro de 109 · quatro frentes de 20 '
      'embaixo em cada uma · duas folhas de correr de 85 × 240'),
}

FOLHA = dict(
 aba='SUÍTE HÓSPEDES',
 sub='Gustavo Raposo · executivo Luiza Pacheco, pranchas 66, 67 e 68 · ⭐ '
     'um armário e mais nada: a elevação A é papel de parede',
 chapa_txt={
  OWS18: 'Off-White Suave · Linha Sense · Duratex · ⭐ SÓ as duas folhas '
         'de correr · 18 mm porque folha de 2,40 m pendurada em trilho '
         'empena com 15',
  OWS15: 'Off-White Suave · Linha Sense · Duratex · a estrutura: '
         'laterais, divisória, tampos, bases, testeira e rodapé',
  BR18:  'Branco · as seis prateleiras internas · "interno em MDF Branco" '
         'é chamada da prancha',
  BR15:  'Branco · as oito frentes de 20',
  BR6:   'Branco TX · o fundo, em duas peças',
  'MDF Branco TX 15': 'Branco TX · a caixaria das oito gavetas e bandejas',
 },
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a QUANTIDADE é '
      'a célula AMARELA no fim do painel de material, e ela sai ZERO.   '
      '⛔⛔ O PÉ-DIREITO DO ANEXO É 260, NÃO 275. Toda a cadeia muda com '
      'isso: maleiro de 47 em vez de 62, folha de 240 em vez de 255. ⭐ Na '
      'fábrica é a diferença entre cortar a folha deste armário junto com '
      'as dos quartos ou não — e não pode.   '
      '⭐ É O ÚNICO ARMÁRIO DE CORRER DA CASA SEM ESPELHO: as duas folhas '
      'são de MDF. Nos quartos dos filhos, metade das folhas é espelhada.   '
      '⭐ OITO FRENTES DE 20 em dois metros de armário: quatro gavetas e '
      'quatro sapateiras, todas em corrediça.',
 duvidas=[
  '⚠ A PROFUNDIDADE DE 60 não está cotada em nenhuma das três pranchas. '
  'Adotei 60, que é o padrão de armário de quarto desta casa. ⛔ Se for '
  '55, saem cerca de 1,4 m² de chapa — perto de R$ 250.',
  '⚠ A LARGURA DAS FOLHAS DE CORRER: 85 cada, para dar 4 cm de '
  'sobreposição nos 166. ⛔ Duas folhas de 83 sem sobrepor encostam e não '
  'correm.',
  '⚠ O TRILHO SS-150 entrou como UM conjunto para as duas folhas. ⭐ É '
  'como lancei na Suíte 01, onde há dois trechos e dois conjuntos. ⛔ Se o '
  'fornecedor cobrar por folha, dobra.',
  '⚠ O ARMÁRIO NÃO TEM ILUMINAÇÃO DESENHADA e as folhas de correr deixam '
  'metade do interior no escuro o tempo todo. É o mesmo silêncio dos dois '
  'closets.',
 ],
 nao_marcenaria=[
  '⛔ O PAPEL DE PAREDE "a definir" da elevação A, que ocupa a parede '
  'inteira.',
  '⛔ A CAMA DE CASAL, o RACK e as MESAS LATERAIS, todos "a serem '
  'adquiridos, modelo a definir".',
  '⛔ O TAPETE ORGÂNICO de 240 × 320.',
  '⛔ A ELÉTRICA: dois pontos de arandela, interruptor de 2 teclas e '
  'tomada dupla.',
 ],
 notas=[
  '⭐ UM MÓVEL SÓ, E É O MAIS SIMPLES DE TODOS OS ARMÁRIOS DA CASA: duas '
  'colunas iguais, um cabideiro, seis prateleiras e oito frentes. Sem '
  'canto, sem espelho, sem padrão misto.',
  '⭐ NENHUMA PRATELEIRA PEDE ALMA DE AÇO: 80,75 de vão contra os 120 da '
  'regra.',
  '⛔ É O ÚNICO AMBIENTE DO PROJETO COM PÉ-DIREITO DIFERENTE. Vale '
  'destacar isso na ordem de corte: um armário de 260 no meio de uma casa '
  'de 275 é o tipo de peça que sai errada por hábito.',
 ],
)
