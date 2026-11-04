# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO · CIRCULAÇÃO / ROUPARIA — peça por peça  [29/10/2026]

pranchas 35 e 36 · planta de layout e elevação A, vista externa e interna.

⭐⭐ DOIS PADRÕES NA MESMA PEÇA, e é de propósito: o CORPO sai em MDF
  Off-White Suave, Linha Sense, e as QUATRO PORTAS em MDF Nogueira Thar,
  Linha Design. O interno é Branco. ⛔ Isso são TRÊS compras e TRÊS
  arredondamentos de chapa num armário só — e cada padrão puxa no mínimo
  uma chapa inteira, mesmo que sobre.

⭐ A CADEIA VERTICAL FECHA EM 275: 2 de topo + 256 de corpo + 10 de rodapé,
  e a vista interna abre o 256 em 66 de maleiro + quatro vãos de 35 + 40
  embaixo, com as prateleiras de 2 entre eles.

⭐ A VISTA INTERNA MOSTRA DUAS COLUNAS, cinco prateleiras cada: são DEZ
  prateleiras de 113 de vão. ⛔ Todas passam de 70 — 18 mm — e todas passam
  de 1,20 m? Não: 113 fica abaixo. Nenhuma pede alma de aço, e é o único
  armário grande da casa em que isso acontece.

⭐ O PUXADOR É CAVA QUADRADA: a elevação cota o quadrinho de 10 × 10,5 em
  cada folha. ⛔ Não é cava corrida de ponta a ponta — é um recorte de
  10 cm, e isso muda o metro de cava usinada.
"""
from base import P

OW18, OW15, OW6 = ('MDF Off-White Suave 18', 'MDF Off-White Suave 15',
                   'MDF Off-White Suave 6')
NT15 = 'MDF Nogueira Thar 15'
BR18, BR6 = 'MDF branco 18', 'MDF Branco TX 6'

I1 = 'ELEVAÇÃO A Armário da rouparia'

ROUPARIA = [
 # ══ ITEM 01 · ARMÁRIO — 230 × 275 × 50 ════════════════════════════════
 P('Lateral',              I1, 273, 50, 2, OW15, (1, 1),
   '⛔ A elevação desenha 275 de altura e a chapa dá 273: rebaixada, e a '
   'diferença some no rodapé · aparente nas duas pontas'),
 P('Divisória central',    I1, 273, 50, 1, OW15, (1, 0),
   '⭐ Uma só: é ela que faz as DUAS colunas da vista interna'),
 P('Tampo e base',         I1, 226, 50, 2, OW15, (1, 0)),
 P('Prateleira projetada', I1, 113, 48, 10, BR18, (2, 2),
   '⭐ Cinco por coluna, duas colunas · 18 mm porque o vão de 113 passa dos '
   '70 · ⭐ mas fica abaixo de 1,20 m: nenhuma pede alma de aço'),
 P('Fundo',                I1, 115, 273, 2, BR6, (0, 0),
   '⛔ DUAS peças de 115: um fundo de 230 × 273 não cabe na chapa de '
   '275 × 185 em orientação nenhuma · a emenda cai na divisória central, '
   'que é onde ela não aparece · sem fita'),
 P('Frente · porta de giro', I1, 57.5, 256, 4, NT15, (2, 2),
   '⭐ QUATRO folhas de 2,56 m em Nogueira Thar · ⛔ folha desse porte pede '
   'TRÊS dobradiças · puxador tipo cava QUADRADA, recorte de 10 × 10,5'),
 P('Rodapé',               I1, 230, 10, 1, OW15, (1, 0),
   'Recuado, em Off-White Suave como o corpo'),
]

from base import DOBRADICA

GAVETAS = BASCULAS = PUXADORES = MOLDURA = []
LED = CABIDEIROS = ALMAS = VIDRO = SERRALHERIA = []
# ⭐ (móvel, rótulo, nº de FOLHAS, dobradiças POR FOLHA, preço)
PORTAS = [
 (I1, 'Quatro folhas de 57,5 × 256 em Nogueira Thar · ⭐ TRÊS dobradiças '
      'por folha: 2,56 m não se segura em duas', 4, 3, DOBRADICA),
]
# ⭐ (móvel, rótulo, nº de frentes, extensão de cava em cm por frente)
#   ⛔ CAVA QUADRADA, não corrida: o recorte tem 10 cm, não os 57,5 da folha.
CAVA = [
 (I1, 'Cava QUADRADA de 10 × 10,5 nas quatro folhas · ⛔ não é cava corrida '
      'de ponta a ponta', 4, 10),
]
# ⭐ (móvel, nome, rótulo, quantidade, unidade, chave)
OUTRAS = [
 (I1, 'Perfil de proteção de piso', 'O rodapé de 230 toca o chão', 2.30,
  'm', 'Perfil de proteção de piso'),
]

CABECA = {
 I1: ('230 × 275 × 50',
      'ELEVAÇÃO A · cadeia vertical 2 de topo + 256 de corpo + 10 de rodapé '
      '= 275, e o 256 se abre em 66 de maleiro + quatro vãos de 35 + 40 '
      'embaixo · a vista interna mostra DUAS colunas de cinco prateleiras '
      '· quatro portas de giro de 57,5 × 256'),
}

FOLHA = dict(
 aba='CIRCULAÇÃO / ROUPARIA',
 sub='Gustavo Raposo · executivo Luiza Pacheco, pranchas 35 e 36 · ⭐ TRÊS '
     'padrões num armário só: corpo em Off-White Suave Linha Sense, portas '
     'em Nogueira Thar Linha Design e interno em MDF Branco',
 chapa_txt={OW15: 'Off-White Suave · Linha Sense · Duratex · o CORPO: '
                  'laterais, divisória, tampo, base e rodapé',
            NT15: 'Nogueira Thar · Linha Design · Duratex · ⭐ só as QUATRO '
                  'PORTAS, e é o que se vê do corredor',
            BR18: 'Branco · as dez prateleiras internas',
            BR6:  'Branco TX · o fundo'},
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a QUANTIDADE é a '
      'célula AMARELA no fim do painel de material, e ela sai ZERO.   '
      '⭐⭐ TRÊS PADRÕES NUM ARMÁRIO SÓ, e é de propósito: do corredor se vê '
      'uma parede de Nogueira Thar, e por dentro tudo é claro. ⛔ Mas três '
      'padrões são três compras e três arredondamentos de chapa, e cada um '
      'puxa no mínimo uma chapa inteira mesmo que sobre — num armário de '
      '230 isso pesa.   ⭐ AS QUATRO FOLHAS TÊM 2,56 M e levam TRÊS '
      'dobradiças cada, não duas: folha desse porte descai na segunda.   '
      '⭐ O puxador é cava QUADRADA de 10 × 10,5, não cava corrida: são 10 '
      'cm de usinagem por folha, não 57,5.',
 duvidas=[
  '⚠ A PROFUNDIDADE DE 50 NÃO ESTÁ COTADA em nenhuma das duas pranchas. '
  'Adotei 50, que é o padrão de rouparia da casa. ⛔ Se for 60, as dez '
  'prateleiras e as duas laterais crescem 20% em área, e isso é quase uma '
  'chapa a mais. Conferir na medição técnica.',
  '⭐ A ELEVAÇÃO COTA 275 DE ALTURA e a chapa dá 273. Rebaixei lateral, '
  'divisória e fundo para 273 e deixei a diferença no rodapé, que é a peça '
  'que esconde folga. ⚠ Se o pé-direito do corredor for exatamente 275, o '
  'armário entra justo e não há onde errar: medir antes de cortar.',
  'AS DEZ PRATELEIRAS SÃO DE 113 DE VÃO. ⭐ Passam dos 70 que pedem 18 mm e '
  'ficam abaixo dos 120 que pedem alma de aço — é o único armário grande da '
  'casa que não leva barra. ⚠ Mas rouparia carrega toalha e roupa de cama '
  'empilhada, que é peso concentrado. Se a fábrica achar pouco, a alma '
  'custa R$ 50 por prateleira.'],
 # ⛔ A SEÇÃO NÃO PODE FICAR VAZIA, e aqui ela quase ficou: lista vazia
 #   deixava o título "O QUE NÃO É MARCENARIA" pendurado sobre nada, e o
 #   intervalo de formato saía invertido. ⭐ E o fato é informação: este é o
 #   único ambiente da casa em que a elevação inteira é nossa.
 nao_marcenaria=[
  '⭐ NADA — e é o único ambiente da casa assim. A elevação não traz pedra, '
  'vidro, serralheria, elétrica nem alvenaria: do rodapé ao topo, os 230 × '
  '275 são marcenaria, e o que o corredor vê é só a nossa Nogueira Thar.'],
 notas=[
  '⭐ O ARMÁRIO É SÓ PRATELEIRA: dez delas, em duas colunas de cinco, mais '
  'o maleiro de 66 no topo. Não há gaveta, não há cabideiro e não há '
  'ferragem de movimento além das doze dobradiças.',
  '⭐ É O AMBIENTE MAIS BARATO POR METRO LINEAR DA CASA, e é o que mais '
  'aparece: fica no corredor, de frente para quem passa. A Nogueira Thar '
  'das portas é o que o cliente vê.'],
)
