# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO · VARANDA — levantamento peça por peça  [29/10/2026]

pranchas 19 a 22 · planta de layout, elevações A, B e C.

⭐⭐ SÃO TRÊS MÓVEIS, E A PRANCHA ESCONDE ISSO. A elevação A e a elevação B
  repetem os rótulos "Gaveta Talheres · Gaveta · Gavetão · Gaveta
  Porta-temperos", e a leitura apressada conta o mesmo gaveteiro duas vezes.
  ⛔ Não é o mesmo. A seta B da planta aponta para a ILHA (100 × 180), a seta
    A aponta para a PAREDE DE 546. São móveis diferentes, em paredes
    perpendiculares, e cada um tem o seu gaveteiro. O que prova: na elevação A
    o gaveteiro está desenhado em BEGE (marcenaria desta vista) e o
    porta-temperos em BRANCO — branco é a ilha vista por trás, e ela se
    levanta na elevação B.

⭐ O QUE A PLANTA DIZ E A ELEVAÇÃO NÃO: a ilha é "Proj. alvenaria". A caixa da
  ilha é obra, a bancada e os pés são granito — ⛔ nada disso é nosso. Nosso é
  só o gaveteiro embutido dentro dela.

⛔⛔ FORA DO ESCOPO nesta varanda, pela fronteira de 29/10:
  bancada, rodobanca, pé lateral e fundo em GRANITO MARROM IMPERIAL ESCOVADO ·
  o corpo de alvenaria da ilha · cuba inox 40×50 · torneira · cooktop · forno ·
  lava-louças de 10 serviços.
⭐ NOSSO, porque está na marcenaria: as duas PORTAS DE VIDRO TEMPERADO
  INCOLOR da cristaleira. Vidro que sai no mesmo caminhão e é instalado pela
  mesma equipe é nosso.

⚠⚠ A DÚVIDA CARA DESTE AMBIENTE — A CRISTALEIRA É CURVA?
  A PLANTA desenha a cristaleira com "R72" e a silhueta arredondada; a
  ELEVAÇÃO C desenha a mesma peça como um retângulo plano de 163 × 252, e é
  ela que tem as cotas. As duas não podem estar certas ao mesmo tempo: porta
  de vidro temperado não curva, e prateleira curva de 157 é outro móvel.
  ⛔ Levantei pela ELEVAÇÃO C, que é a vista cotada, e lancei uma linha
    declarada de usinagem de peça curva a ZERO. Se a planta mandar, a peça
    muda de patamar — é a primeira pergunta a fazer ao Jonathan.
"""
from base import P, gaveta, ALT_MAX

NC18, NC15, NC6 = ('MDF Nogueira Caiena 18', 'MDF Nogueira Caiena 15',
                   'MDF Nogueira Caiena 6')
BR15, BR6 = 'MDF Branco TX 15', 'MDF Branco TX 6'

I1 = 'ELEVAÇÃO A Armário da parede'
I2 = 'ELEVAÇÃO B Gaveteiro da ilha'
I3 = 'ELEVAÇÃO C Cristaleira'

VARANDA = [
 # ══ ITEM 01 · ARMÁRIO DA PAREDE — 446 × 68 × 60, mais 20 de rodapé ═════
 #  A parede inteira tem 546 (planta: 100 + 331 + 20 + 95). A marcenaria
 #  ocupa 446 = 95 + 20 + 164 + 50 + 117, e os 100 que sobram são a ilha.
 #  ALTURA, pela elevação: 20 de rodapé + 68 de corpo + 2 de bancada = 90.
 #  ⛔ Os 2 da bancada e os 16 da rodobanca são GRANITO: não entram.
 #  FRENTES contadas uma a uma na elevação ampliada: oito giros, um fixo e
 #  três gavetas. O vão de 50 é a lava-louças e não tem frente nossa.
 P('Lateral',              I1, 68, 60, 2, NC15, (1, 0),
   'Aparente nas duas pontas · ⛔ a de dentro morre contra a ilha'),
 P('Divisória',            I1, 68, 60, 5, BR15, (1, 0),
   'Cinco verticais: fecham os vãos de 95, 20, 164, o nicho da lava-louças '
   'e o módulo de 117 · interno em MDF Branco, como a prancha manda'),
 P('Base',                 I1, 223, 60, 2, BR15, (1, 0),
   '⛔ DUAS peças de 223: os 446 do armário passam dos 275 da chapa · a '
   'emenda cai sobre uma divisória'),
 P('Travessa de topo',     I1, 223, 10, 4, BR15, (1, 0),
   '⭐ É o que recebe a bancada de granito. A bancada é do marmorista, mas '
   'o que a sustenta é nosso — e sem isto o granito apoia no ar'),
 P('Prateleira projetada', I1, 95, 58, 2, NC18, (2, 2),
   '⭐ 18 mm: o vão de 95 passa dos 70 da regra · as duas "Proj. prateleira" '
   'da elevação'),
 P('Fundo',                I1, 223, 68, 2, BR6, (0, 0),
   'Encaixe em rasgo · ⛔ DUAS peças de 223, pelo mesmo motivo da base · '
   'sem fita'),
 P('Frente · porta de giro', I1, 47, 68, 8, NC15, (2, 2),
   'Oito folhas, contadas uma a uma na elevação ampliada · puxador tipo '
   'cava usinada na marcenaria'),
 P('Frente · painel fixo', I1, 20, 68, 1, NC15, (2, 2),
   '⭐ A elevação escreve "Fixo": é frente que não abre, fecha o vão da '
   'coluna estreita · ⛔ NÃO leva dobradiça nem cava'),
 P('Frente · gaveta de talheres', I1, 60, 14, 1, NC15, (2, 2), 'Puxador cava'),
 P('Frente · gaveta',      I1, 60, 14, 1, NC15, (2, 2), 'Puxador cava'),
 P('Frente · gavetão',     I1, 60, 40, 1, NC15, (2, 2), 'Puxador cava'),
 *gaveta(I1, 60, 55, 14, 2, 'Caixa de gaveta'),
 *gaveta(I1, 60, 55, 36, 1, 'Caixa de gavetão'),
 P('Rodapé',               I1, 223, 20, 2, NC15, (1, 0),
   '⭐ "Rodapé a definir" na prancha · recuado, em Nogueira Caiena como o '
   'resto · ⛔ DUAS peças de 223'),

 # ══ ITEM 02 · GAVETEIRO DA ILHA — 105 × 68 ════════════════════════════
 #  A ilha mede 100 × 180 em planta e é ALVENARIA. A elevação B mostra a
 #  face de 180: 60 de gaveteiro + 23,5 de porta-temperos + 73 de forno +
 #  21,5 de gaveta = 178. ⛔ Os 73 do forno são eletro: não têm frente nossa.
 #  ⭐ O que é nosso: o corpo embutido e as cinco frentes.
 P('Lateral',              I2, 68, 55, 2, BR15, (1, 0),
   '⭐ Corpo embutido dentro da alvenaria · interno em MDF Branco'),
 P('Divisória',            I2, 68, 55, 2, BR15, (1, 0),
   'Separa o gaveteiro de 60, o porta-temperos de 23,5 e a gaveta de 21,5'),
 P('Base',                 I2, 105, 55, 1, BR15, (1, 0)),
 P('Fundo',                I2, 105, 68, 1, BR6, (0, 0), '⛔ sem fita'),
 P('Frente · gaveta de talheres', I2, 60, 14, 1, NC15, (2, 2), 'Puxador cava'),
 P('Frente · gaveta',      I2, 60, 14, 1, NC15, (2, 2), 'Puxador cava'),
 P('Frente · gavetão',     I2, 60, 40, 1, NC15, (2, 2), 'Puxador cava'),
 P('Frente · gaveta porta-temperos', I2, 23.5, 68, 1, NC15, (2, 2),
   '⭐ Gaveta VERTICAL de altura cheia — o porta-temperos da elevação B'),
 P('Frente · gaveta vertical', I2, 21.5, 68, 1, NC15, (2, 2),
   'A gaveta estreita do outro lado do forno'),
 *gaveta(I2, 60, 50, 14, 2, 'Caixa de gaveta'),
 *gaveta(I2, 60, 50, 36, 1, 'Caixa de gavetão'),
 *gaveta(I2, 23.5, 50, 64, 1, 'Caixa de gaveta vertical · porta-temperos'),
 *gaveta(I2, 21.5, 50, 64, 1, 'Caixa de gaveta vertical'),

 # ══ ITEM 03 · CRISTALEIRA — 163 × 252 × 54 ════════════════════════════
 #  ELEVAÇÃO C, que é a vista cotada: 163 de largura = 3 + 157 + 3 ·
 #  252 de altura = 3 de topo + 159 de parte envidraçada + 85 de parte
 #  fechada + 5 de base. A elevação B confirma pela lateral: a mesma cadeia
 #  de 252, com as prateleiras de 38,2 / 38,3 / 38,3 / 38,3 em cima e
 #  39,5 / 39,5 embaixo.
 #  ⭐ Interno NO MESMO MDF Nogueira Caiena — a prancha diz, e isso muda a
 #    conta: não há uma peça de branco nesta peça, nem no fundo.
 P('Lateral',              I3, 252, 54, 2, NC15, (1, 1),
   'Aparente dos dois lados · ⛔ 252 de altura: cabe nos 273 da chapa, mas '
   'é peça inteira e manda no plano de corte'),
 P('Tampo e base',         I3, 157, 54, 2, NC15, (1, 1)),
 P('Horizontal fixa',      I3, 157, 54, 1, NC18, (1, 1),
   '⭐ Divide a parte de vidro da parte fechada, aos 85 do chão · 18 mm '
   'porque é ela que trava o móvel na largura · ⛔ sem suporte: é fixa, '
   'cavilhada na lateral'),
 P('Prateleira projetada', I3, 157, 52, 4, NC18, (2, 2),
   '⭐ Quatro: três na parte de vidro e uma na fechada · 18 mm, e ainda '
   'assim o vão de 157 passa de 1,20 m e pede alma de aço'),
 P('Fundo',                I3, 163, 252, 1, NC6, (0, 0),
   '⭐ Aparece por dentro do vidro, então sai em Nogueira Caiena e não em '
   'branco de caixaria · ⛔ sem fita'),
 P('Frente · porta de giro', I3, 78.5, 85, 2, NC15, (2, 2),
   'As duas folhas de baixo, em MDF · puxador redondo'),
]

# ════════════════════════════════════════════════════════════════════════
# A FERRAGEM E O QUE NÃO É CHAPA, declarados por móvel
# ════════════════════════════════════════════════════════════════════════
from base import DOBRADICA, DOBR_VIDRO, ALT_MAX, CHAPA_C

# ⭐ (móvel, rótulo, nº de gavetas, comprimento da corrediça em mm)
#   ⛔ TODA corrediça desta casa é HETTICH OCULTA [Jonathan, 29/10]. A
#     prancha da varanda já pedia invisível: aqui não houve upgrade, houve
#     confirmação.
GAVETAS = [
 (I1, 'Gaveta de talheres e gaveta, no módulo de 117',  2, 500),
 (I1, 'Gavetão, no módulo de 117',                      1, 500),
 (I2, 'Gaveta de talheres e gaveta, no módulo de 60',   2, 450),
 (I2, 'Gavetão, no módulo de 60',                       1, 450),
 (I2, 'Gavetas verticais · porta-temperos de 23,5 e gaveta de 21,5', 2, 450),
]
# ⭐ (móvel, rótulo, nº de FOLHAS, dobradiças POR FOLHA, preço)
#   ⛔⛔ A QUANTIDADE É O PRODUTO, não o terceiro elemento. Foi lendo o
#     terceiro como quantidade que a conta de ferragem do ICA errou.
PORTAS = [
 (I1, 'Oito portas de giro de 68 de altura', 8, 2, DOBRADICA),
 (I3, 'Duas portas de giro de 85 de altura', 2, 2, DOBRADICA),
 (I3, 'Duas portas de VIDRO TEMPERADO de 159 · dobradiça GV48 1011, inox, '
      '90°, fixação alvenaria/vidro · ⭐ TRÊS por folha porque a folha passa '
      'de 1,00 m e vidro temperado pesa muito mais que MDF da mesma medida '
      '· ⛔ vidro temperado não aceita dobradiça de caneco: depois de '
      'temperado não se fura', 2, 3, DOBR_VIDRO),
]
BASCULAS   = []
PUXADORES  = []
MOLDURA    = []
LED        = []
CABIDEIROS = []
ALMAS      = []
SERRALHERIA = []
# ⭐ (móvel, rótulo, nº de frentes, extensão de cava em cm por frente)
#   ⛔ O puxador desta varanda é CAVA USINADA NA MARCENARIA nos dois
#     armários — não se compra, se usina. Na cristaleira é PUXADOR REDONDO,
#     que é peça de compra e segue sem preço.
CAVA = [
 (I1, 'Oito portas de giro e três gavetas · ⛔ o painel FIXO não leva cava',
  11, 60),
 (I2, 'Cinco frentes do gaveteiro da ilha', 5, 60),
]
# ⭐⭐ VIDRO NÃO É CHAPA, e por isso ele NÃO mora em PECAS.
#   [regra 13 do quantitativo] "m² tem dois sentidos e eles não se misturam":
#   peça de MDF se paga por CHAPA, área dividida pela área útil da chapa;
#   vidro, espelho e palhinha se pagam POR m², área cheia. O discriminador é
#   a CHAVE — só `MDF …` é chapa. Pôr a folha de vidro em PECAS a mandaria
#   para o plano de corte, e não há corte nenhum: a folha vem pronta do
#   vidraceiro, sem fita e sem cava, porque o puxador é furado no vidro.
# ⭐ (móvel, rótulo, nº de folhas, comprimento, largura, chave)
VIDRO = [
 (I3, 'Portas da cristaleira · duas folhas de 78,5 × 159, puxador redondo '
  'furado no próprio vidro · ⛔ A COTAR com o vidraceiro', 2, 78.5, 159,
  'Vidro temperado incolor'),
]
# ⭐ (móvel, nome, rótulo, quantidade, unidade, chave)
OUTRAS = [
 (I1, 'Perfil de proteção de piso', 'O rodapé do armário de 446 toca o chão '
  'em toda a extensão', 4.46, 'm', 'Perfil de proteção de piso'),
 (I3, 'Perfil de proteção de piso', 'A cristaleira de 163 toca o chão',
  1.63, 'm', 'Perfil de proteção de piso'),
 (I3, 'Puxador NEO32 Bronze', '⚠ A prancha pede "puxador redondo" nas duas '
  'portas de MDF da cristaleira e não nomeia modelo · ⛔ SEM PREÇO na Base: '
  'sai ZERO e o custo deste móvel é um PISO', 2, 'un',
  'Puxador NEO32 Bronze'),
]

# ════════════════════════════════════════════════════════════════════════
CABECA = {
 I1: ('446 × 68 × 60, mais 20 de rodapé',
      'A parede inteira tem 546 (planta: 100 + 331 + 20 + 95) e a marcenaria '
      'ocupa 446 = 95 + 20 + 164 + 50 de vão da lava-louças + 117 · altura '
      '20 de rodapé + 68 de corpo + 2 de bancada = 90, e os 2 da bancada '
      'são granito · OITO portas de giro, UM painel fixo e TRÊS gavetas'),
 I2: ('105 × 68 × 55, embutido na ilha de alvenaria',
      'A ilha mede 100 × 180 em planta e é "Proj. alvenaria": a caixa é obra '
      'e a bancada é granito · a elevação B mostra a face de 180 em 60 de '
      'gaveteiro + 23,5 de porta-temperos + 73 de forno + 21,5 de gaveta · '
      '⛔ os 73 do forno são eletro e não têm frente nossa'),
 I3: ('163 × 252 × 54',
      'ELEVAÇÃO C, a vista cotada: largura 3 + 157 + 3 = 163 · altura 3 de '
      'topo + 159 de parte envidraçada + 85 de parte fechada + 5 de base = '
      '252 · a elevação B confirma pela lateral, com as prateleiras de 38,2 '
      'e 38,3 em cima e 39,5 embaixo · DUAS portas de vidro temperado em '
      'cima e DUAS de MDF embaixo'),
}

FOLHA = dict(
 aba='VARANDA',
 sub='Gustavo Raposo · Condomínio Vale dos Pinhais, Nova Lima · executivo '
     'Luiza Pacheco, pranchas 19 a 22 · TRÊS móveis: o armário da parede de '
     '546, o gaveteiro embutido na ilha de alvenaria e a cristaleira de '
     '163 × 252 com portas de vidro temperado',
 chapa_txt={NC18: 'Nogueira Caiena · Linha Design · Duratex · prateleiras e '
                  'a horizontal fixa da cristaleira',
            NC15: 'Nogueira Caiena · Linha Design · Duratex · frentes, '
                  'rodapé e toda a caixaria aparente da cristaleira',
            NC6:  'Nogueira Caiena · Linha Design · Duratex · ⭐ o fundo da '
                  'cristaleira sai NA COR, não em branco: atrás do vidro '
                  'não existe peça escondida',
            BR15: 'Branco TX · o interno dos dois armários, como a prancha '
                  'manda ("Interno em MDF Branco")',
            BR6:  'Branco TX · fundos dos dois armários'},
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a QUANTIDADE é a '
      'célula AMARELA no fim do painel de material, e ela sai ZERO. '
      '   ⭐⭐ SÃO TRÊS MÓVEIS, E A PRANCHA ESCONDE ISSO: as elevações A e B '
      'repetem os rótulos "Gaveta Talheres · Gaveta · Gavetão · Porta-'
      'temperos", e a leitura apressada conta o mesmo gaveteiro duas vezes. '
      'Não é o mesmo — a seta B da planta aponta para a ILHA e a seta A para '
      'a PAREDE DE 546. O que prova: na elevação A o gaveteiro está em bege '
      'e o porta-temperos em branco, e branco é a ilha vista por trás. '
      '   ⛔ PEDRA NÃO É NOSSA: bancada, rodobanca, pé lateral e fundo em '
      'Granito Marrom Imperial Escovado ficam fora, e o corpo da ilha é '
      'alvenaria. ⭐ MAS O VIDRO É: as duas folhas temperadas da cristaleira '
      'saem no mesmo caminhão e são instaladas pela mesma equipe.',
 duvidas=[
  '⚠⚠ A CRISTALEIRA É CURVA? A PLANTA a desenha com "R72" e silhueta '
  'arredondada; a ELEVAÇÃO C desenha a mesma peça como um retângulo plano de '
  '163 × 252, e é a elevação que tem as cotas. As duas não podem estar certas '
  'ao mesmo tempo: porta de vidro temperado não curva, e prateleira curva de '
  '157 é outro móvel. ⛔ Levantei pela elevação. Se a planta mandar, lateral, '
  'tampo, base e as quatro prateleiras viram peça curva, as folhas de vidro '
  'viram vidro curvo — que é outro fornecedor e outro patamar de preço. '
  'É a primeira pergunta deste ambiente.',
  'O PUXADOR REDONDO DA CRISTALEIRA não tem modelo na prancha nem linha na '
  'Base, e sai ZERO. São dois nas portas de MDF, mais os dois furados no '
  'próprio vidro — e furo em vidro temperado tem de ser feito ANTES da '
  'têmpera, então o modelo precisa estar fechado antes de mandar cortar.',
  'O VIDRO TEMPERADO INCOLOR segue SEM PREÇO na Base: 2,5 m² de folha saem '
  'ZERO, e enquanto isso o custo da cristaleira é um PISO. ⚠ A dobradiça já '
  'tem modelo e preço estimado (GV48 1011, R$ 95 a unidade); o vidro não.',
  '⚠ O RODAPÉ É "A DEFINIR" na prancha. Lancei 20 cm em Nogueira Caiena, '
  'como o resto do armário, porque é o que a elevação desenha. Se for '
  'rodapé metálico ou de outro material, sai da chapa e vira compra.',
  'A ILHA É ALVENARIA e só o gaveteiro é nosso. ⚠ Isso exige combinar o vão '
  'com o pedreiro ANTES: gaveta oculta Hettich não perdoa esquadro de '
  'alvenaria, e o ajuste em obra não existe para corrediça oculta.'],
 nao_marcenaria=[
  'Bancada, rodobanca, pé lateral e fundo em Granito Marrom Imperial '
  'Escovado — pedra não é escopo da marcenaria',
  'O corpo de alvenaria da ilha, que é obra civil',
  'Cuba em inox 40 × 50 e torneira',
  'Cooktop, forno e lava-louças de 10 serviços'],
 notas=[
  '⭐⭐ UM PADRÃO SÓ NO AMBIENTE INTEIRO: Nogueira Caiena, Linha Design, '
  'Duratex, nas frentes, na cristaleira e no rodapé. O interno é Branco TX '
  'nos dois armários — mas NÃO na cristaleira, que a prancha manda fazer '
  '"interno no mesmo MDF". Atrás de porta de vidro não há peça escondida.',
  '⭐ O VIDRO É NOSSO E A PEDRA NÃO, e a proposta precisa dizer as duas '
  'coisas na mesma frase: as portas de vidro saem no mesmo contrato da '
  'marcenaria, e a bancada de granito o cliente fecha com o marmorista.',
  '⚠ AS QUATRO PRATELEIRAS DA CRISTALEIRA TÊM 157 DE VÃO. Passam dos 18 mm '
  'que resolvem empeno e dos 120 cm que pedem alma de aço — as quatro levam '
  'barra. ⛔ Sem a alma, uma prateleira de 157 carregada de louça flecha no '
  'meio, e atrás de vidro isso se vê de longe.'],
)
