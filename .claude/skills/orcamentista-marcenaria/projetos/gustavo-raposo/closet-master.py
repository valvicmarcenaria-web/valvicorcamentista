# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO · CLOSET SUÍTE MASTER — peça por peça  [30/10/2026]

pranchas 42, 43 e 44 · planta de layout, elevação A e elevação B.

⭐⭐ DOIS ARMÁRIOS ABERTOS, SEM UMA ÚNICA PORTA. E a ausência é leitura, não
  esquecimento: a Suíte Master ganhou DUAS vistas da elevação B — uma
  externa com as folhas e os rótulos "Giro Giro", outra interna sem elas.
  O closet tem UMA vista por parede, e nela o miolo está à mostra. ⛔ Não
  há folha, não há dobradiça, não há cava de porta. O que fecha este closet
  é a porta pivotante da suíte.

⭐ AS DUAS CADEIAS VERTICAIS FECHAM EM 275, e são a mesma receita:
     10 de rodapé + 62 de maleiro + 2 + (191 de miolo) + 10 de testeira
  ⛔ O 191 do meio é que muda de parede para parede: na elevação A ele é um
    cabideiro inteiro numa coluna, dois cabideiros noutra e três vãos de 35
    na terceira. Na B são três vãos de 35 de um lado e um cabideiro do
    outro — e embaixo de tudo, nas duas, quatro frentes de 20.

⛔⛔ A PORTA PIVOTANTE NÃO ESTÁ NESTE ORÇAMENTO. Ela aparece na elevação B
  porque a outra cara dela dá para cá — é a MESMA folha de 75 × 210 que a
  Suíte Master já paga, com Nogueira de um lado e Off-White do outro. O que
  é daqui é a BANDEIRA de 75 × 65 por cima dela, que é a face do painel
  virada para o closet.

⭐ A SAPATEIRA DESLIZANTE É GAVETA, e por isso ela corre em corrediça. Oito
  no total — quatro na elevação A... não: DUAS na A e QUATRO na B, mais as
  gavetas. ⛔ O que ela não leva é SUPORTE de prateleira: prateleira que
  corre não se apoia em pino.

⛔ FORA: a porta de alvenaria da parede oeste · o forro · a iluminação, que
  nenhuma das três pranchas desenha.
"""
from base import P, gaveta, CORREDICA

OWS18, OWS15, OWS6 = ('MDF Off-White Suave 18', 'MDF Off-White Suave 15',
                      'MDF Off-White Suave 6')

I1 = 'ELEVAÇÃO A Armário de 286'
I2 = 'ELEVAÇÃO B Armário de 211'
I3 = 'ELEVAÇÃO B Bandeira sobre a porta pivotante'

PROF, CORPO = 55.0, 255.0        # 275 − 10 de rodapé − 10 de testeira
# as colunas, apuradas das cotas: a de 92 vem dos dois 45,3 da elevação A,
# a de 102 vem dos dois 50,3 da B, e o resto se divide no que sobra
C1A, C2A = 92.1, 94.0            # elevação A · 1,5 + 92,1 + 1,5 + 94 + 1,5 + 94 + 1,5
C1B, C2B = 104.4, 102.1          # elevação B · 1,5 + 104,4 + 1,5 + 102,1 + 1,5

CLOSET_MASTER = [
 # ══ ITEM 01 · ARMÁRIO DA ELEVAÇÃO A — 286 × 275 × 55 ══════════════════
 P('Lateral e divisória vertical', I1, CORPO, PROF, 4, OWS15, (1, 0),
   '⭐ Duas laterais e duas divisórias, iguais · TRÊS colunas: 92,1 + 94 + '
   '94 · só a aresta da frente leva fita'),
 P('Tampo e base · coluna de 92',   I1, C1A, PROF, 2, OWS15, (1, 0)),
 P('Tampo e base · colunas de 94',  I1, C2A, PROF, 4, OWS15, (1, 0)),
 P('Testeira superior', I1, 143, 10, 2, OWS15, (1, 0),
   '⛔ 286 não cabe na chapa de 275: sai em DUAS de 143 · a emenda cai '
   'numa divisória'),
 P('Rodapé',           I1, 143, 10, 2, OWS15, (1, 0),
   '⛔ Mesma emenda do testeira, pelo mesmo motivo'),
 P('Prateleira do maleiro · coluna de 92',  I1, C1A, 53, 1, OWS18, (1, 0),
   '⭐ Fecha o maleiro de 62'),
 P('Prateleira do maleiro · colunas de 94', I1, C2A, 53, 2, OWS18, (1, 0)),
 P('Divisória da coluna de 92', I1, 109, PROF, 1, OWS15, (1, 0),
   '⭐ É ela que faz os dois 45,3 cotados · vai do maleiro ao topo das '
   'gavetas e PARA ali: embaixo as frentes são inteiras'),
 P('Prateleira', I1, 45.3, 53, 6, OWS18, (1, 0),
   '⭐ Três níveis de 35 × duas meias-colunas de 45,3'),
 P('Prateleira entre os dois cabideiros', I1, C2A, 53, 1, OWS18, (1, 0),
   '⭐ É ela que parte o 191 da coluna do meio em 109 de cabideiro longo e '
   '80 de cabideiro curto'),
 P('Frente de gaveta', I1, C1A, 20, 2, OWS15, (2, 2),
   'Puxador tipo CAVA na marcenaria'),
 P('Frente da sapateira deslizante', I1, C1A, 20, 2, OWS15, (2, 2),
   '⭐ Mesma frente de 20 da gaveta · ⛔ sem suporte: ela corre em '
   'corrediça, não se apoia em pino'),
 *gaveta(I1, C1A, 50, 18, 2, 'Caixa de gaveta'),
 *gaveta(I1, C1A, 50, 18, 2, 'Caixa de gaveta · bandeja da sapateira'),
 P('Fundo', I1, 143, CORPO, 2, OWS6, (0, 0),
   '⛔ Em duas peças, pelo mesmo 286 que não cabe · sem fita'),

 # ══ ITEM 02 · ARMÁRIO DA ELEVAÇÃO B — 211 × 275 × 55 ══════════════════
 P('Lateral e divisória vertical', I2, CORPO, PROF, 3, OWS15, (1, 0),
   '⭐ Duas laterais e UMA divisória · DUAS colunas: 104,4 e 102,1'),
 P('Tampo e base · coluna de 104',  I2, C1B, PROF, 2, OWS15, (1, 0)),
 P('Tampo e base · coluna de 102',  I2, C2B, PROF, 2, OWS15, (1, 0)),
 P('Testeira superior', I2, 211, 10, 1, OWS15, (1, 0),
   '⭐ Peça única: 211 deitada cabe nos 275 da chapa'),
 P('Rodapé',           I2, 211, 10, 1, OWS15, (1, 0)),
 P('Prateleira do maleiro · coluna de 104', I2, C1B, 53, 1, OWS18, (1, 0)),
 P('Prateleira do maleiro · coluna de 102', I2, C2B, 53, 1, OWS18, (1, 0)),
 P('Divisória da coluna de 102', I2, 109, PROF, 1, OWS15, (1, 0),
   '⭐ É ela que faz os dois 50,3 cotados'),
 P('Prateleira', I2, 50.3, 53, 6, OWS18, (1, 0),
   '⭐ Três níveis de 35 × duas meias-colunas de 50,3'),
 P('Frente de gaveta', I2, C1B, 20, 2, OWS15, (2, 2),
   'Puxador tipo CAVA na marcenaria'),
 P('Frente de gaveta · coluna de 102', I2, C2B, 20, 2, OWS15, (2, 2),
   'Puxador tipo CAVA na marcenaria'),
 P('Frente da sapateira deslizante', I2, C1B, 20, 2, OWS15, (2, 2),
   '⛔ sem suporte: ela corre em corrediça'),
 P('Frente da sapateira deslizante · coluna de 102', I2, C2B, 20, 2, OWS15,
   (2, 2), '⛔ sem suporte: ela corre em corrediça'),
 *gaveta(I2, C1B, 50, 18, 2, 'Caixa de gaveta'),
 *gaveta(I2, C2B, 50, 18, 2, 'Caixa de gaveta da coluna de 102'),
 *gaveta(I2, C1B, 50, 18, 2, 'Caixa de gaveta · bandeja da sapateira'),
 *gaveta(I2, C2B, 50, 18, 2,
         'Caixa de gaveta · bandeja da sapateira de 102'),
 P('Fundo', I2, 105.5, CORPO, 2, OWS6, (0, 0),
   '⛔ 211 de largura não cabe na chapa de 185: sai em DUAS de 105,5 · a '
   'emenda cai na divisória · sem fita'),

 # ══ ITEM 03 · BANDEIRA SOBRE A PORTA PIVOTANTE — 75 × 65 ══════════════
 P('Bandeira sobre a porta · face do closet', I3, 65, 75, 1, OWS18, (1, 1),
   '⭐ É a face Off-White do painel de 4 cm cuja outra cara, em Nogueira, '
   'está na Suíte Master · ⛔ o engradado dos 4 cm JÁ ESTÁ LÁ: aqui entra '
   'só a chapa desta face, senão a estrutura é paga duas vezes'),
]

# ⭐ (móvel, rótulo, nº de gavetas, preço do par)
# ⛔ A SAPATEIRA DESLIZANTE CONTA COMO GAVETA: ela corre, e o que faz uma
#   prateleira correr é o mesmo par de corrediça da gaveta.
GAVETAS = [
 (I1, 'Duas gavetas e duas sapateiras deslizantes, todas de 92,1 × 20 · '
      '⛔ a prancha pede corrediça TELESCÓPICA e ela SOBE para a Hettich '
      'oculta, que é a regra da casa', 4, CORREDICA),
 (I2, 'Quatro gavetas e quatro sapateiras deslizantes, de 104,4 e de '
      '102,1 · ⛔ telescópica na prancha, Hettich oculta no orçamento',
  8, CORREDICA),
]
# ⭐ (móvel, rótulo, nº de frentes, extensão de cava em cm por frente)
CAVA = [
 (I1, 'As quatro frentes de 92,1 — duas gavetas e duas sapateiras', 4,
  C1A),
 (I2, 'As quatro frentes de 104,4', 4, C1B),
 (I2, 'As quatro frentes de 102,1', 4, C2B),
]
# ⭐ (móvel, rótulo, quantidade)
CABIDEIROS = [
 (I1, 'TRÊS: dois na coluna do meio, de 109 e de 80, e um inteiro de 191 '
      'na coluna da direita', 3),
 (I2, 'UM, de 109, na coluna de 104,4', 1),
]
PORTAS = BASCULAS = PUXADORES = MOLDURA = []
LED = ALMAS = VIDRO = SERRALHERIA = []
# ⭐ (móvel, nome, rótulo, quantidade, unidade, chave)
OUTRAS = [
 (I1, 'Perfil de proteção de piso', 'O rodapé de 286 toca o chão', 2.86,
  'm', 'Perfil de proteção de piso'),
 (I2, 'Perfil de proteção de piso', 'O rodapé de 211 toca o chão', 2.11,
  'm', 'Perfil de proteção de piso'),
]

CABECA = {
 I1: ('286 × 275 × 55',
      'ELEVAÇÃO A · armário ABERTO, sem porta · TRÊS colunas de 92,1 + 94 '
      '+ 94 · cadeia 10 de rodapé + 62 de maleiro + 2 + 191 de miolo + 10 '
      'de testeira = 275 · a coluna de 92 leva seis prateleiras de 45,3, '
      'duas gavetas e duas sapateiras; a do meio, dois cabideiros de 109 e '
      '80; a da direita, um cabideiro inteiro de 191'),
 I2: ('211 × 275 × 55',
      'ELEVAÇÃO B · armário ABERTO · DUAS colunas de 104,4 e 102,1 · a de '
      '104 leva um cabideiro de 109 e quatro frentes de 20; a de 102, seis '
      'prateleiras de 50,3 e mais quatro frentes de 20'),
 I3: ('75 × 65',
      '⛔ A PORTA PIVOTANTE DE 75 × 210 NÃO ESTÁ NESTE ITEM nem neste '
      'ambiente: ela é a MESMA folha que a Suíte Master já paga, com '
      'Nogueira de um lado e Off-White do outro, e pagá-la aqui seria '
      'comprá-la duas vezes. ⭐ O que é daqui é só a BANDEIRA de 75 × 65 '
      'por cima dela — a face do painel virada para o closet'),
}

FOLHA = dict(
 aba='CLOSET SUÍTE MASTER',
 sub='Gustavo Raposo · executivo Luiza Pacheco, pranchas 42, 43 e 44 · ⭐ '
     'dois armários abertos em Off-White Suave, 286 numa parede e 211 na '
     'outra, e nenhuma porta: quem fecha o closet é a pivotante da suíte',
 chapa_txt={
  OWS18: 'Off-White Suave · Linha Sense · Duratex · as prateleiras, os '
         'maleiros e a bandeira sobre a porta — 18 mm onde o vão passa de '
         '70',
  OWS15: 'Off-White Suave · Linha Sense · Duratex · a estrutura inteira: '
         'laterais, divisórias, tampos, bases, testeiras, rodapés e as '
         'doze frentes de 20',
  OWS6:  'Off-White Suave · Linha Sense · Duratex · os fundos dos dois '
         'armários',
  'MDF Branco TX 15': 'Branco TX · a caixaria das doze gavetas e bandejas '
                      '· ⭐ é o padrão da casa para caixa de gaveta',
  'MDF Branco TX 6':  'Branco TX · o fundo das doze caixas, por encaixe '
                      'em rasgo',
 },
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a QUANTIDADE é '
      'a célula AMARELA no fim do painel de material, e ela sai ZERO.   '
      '⭐⭐ UM PADRÃO SÓ NA CASA INTEIRA DO CLOSET: tudo Off-White Suave, '
      'Linha Sense. É um arredondamento de chapa só por espessura, e por '
      'isso o aproveitamento aqui é o melhor do projeto.   '
      '⛔⛔ A PORTA PIVOTANTE NÃO ESTÁ AQUI. Ela é da Suíte Master, onde '
      'está inteira — as duas faces, o engradado, o pivô e a tranca. Nesta '
      'aba entra só a bandeira de 75 × 65 por cima dela.   '
      '⭐ DOZE FRENTES DE 20 E NENHUMA PORTA: o orçamento deste ambiente é '
      'doze pares de corrediça e quatro cabideiros. Dobradiça, ZERO.',
 duvidas=[
  '⚠ A LARGURA DAS COLUNAS saiu por dedução. A prancha cota os dois 45,3 '
  'da elevação A e os dois 50,3 da B, e o resto eu reparti no que sobra: '
  '92,1 + 94 + 94 numa parede e 104,4 + 102,1 na outra, com laterais e '
  'divisórias de 1,5. ⛔ Se a medição de obra devolver 284 ou 288 em vez de '
  '286, as colunas mudam e as prateleiras mudam com elas — mas a conta de '
  'chapa quase não se move, porque a área é a mesma.',
  '⚠ A PROFUNDIDADE DE 55 vem da planta, não das elevações, e é 5 cm menor '
  'que a dos armários da suíte. ⭐ Confirmei nas duas faixas de 55 da '
  'planta de layout. ⛔ Se na obra virar 60, as vinte e seis peças '
  'horizontais crescem 9% — cerca de uma chapa.',
  '⚠ A SAPATEIRA DESLIZANTE entrou como GAVETA: frente de 20, caixa e par '
  'de corrediça. ⭐ É o que "deslizante" quer dizer, e é o que a cava na '
  'frente confirma. ⛔ Se o senhor a quiser como bandeja inclinada de '
  'sapato, com aba baixa em vez de caixa, cai material e cai preço — mas '
  'a corrediça fica.',
  '⚠ OS FUNDOS: lancei fundo de 6 mm nos dois armários. A elevação não os '
  'desenha porque elevação não desenha fundo. ⛔ Se os armários forem '
  'montados direto contra a alvenaria, sem fundo, saem 7,3 m² de 6 mm — '
  'cerca de R$ 500. ⚠ Mas armário aberto sem fundo mostra a parede, e aqui '
  'o miolo fica todo à vista.',
 ],
 nao_marcenaria=[
  '⛔ A PORTA PIVOTANTE de 75 × 210 — e não por não ser marcenaria, mas '
  'por já estar PAGA na Suíte Master. ⭐ É o único item do projeto que '
  'aparece em duas abas, e esta é a razão de ele estar escrito aqui: para '
  'que ninguém o some duas vezes.',
  '⛔ A PORTA DE ALVENARIA da parede oeste, que a planta desenha com o '
  'arco de abertura.',
  '⛔ O FORRO e a ILUMINAÇÃO. ⚠ Nenhuma das três pranchas desenha luz '
  'dentro do closet — nem fita, nem perfil, nem spot. Num closet aberto de '
  '4,97 m de armário isso chama atenção: vale perguntar à arquiteta antes '
  'de a obra fechar o gesso.',
 ],
 notas=[
  '⭐ É O AMBIENTE MAIS SIMPLES DE FABRICAR DA CASA e um dos maiores: '
  '4,97 m de armário, um padrão só de chapa, nenhuma porta e nenhuma '
  'ferragem de giro. O que ele tem de caro é CORREDIÇA — doze pares.',
  '⭐ NENHUMA PRATELEIRA PEDE ALMA DE AÇO. A maior tem 50,3 de vão, e a '
  'regra da casa é 120. ⛔ É o contrário do armário da suíte, onde as '
  'quatro prateleiras de 128 pedem barra. Quem divide a coluna ao meio '
  'compra divisória e economiza alma.',
  '⭐ OS MALEIROS DE 62 SÃO CINCO, um por coluna, e todos levam suporte e '
  'prateleira de 18 mm como qualquer outra — a palavra "maleiro" só diz '
  'onde ela está, não o que ela é.',
 ],
)
