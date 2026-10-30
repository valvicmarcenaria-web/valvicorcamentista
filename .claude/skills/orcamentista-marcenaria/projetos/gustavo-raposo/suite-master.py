# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO · SUÍTE MASTER — peça por peça  [30/10/2026]

pranchas 39, 40 e 41 · planta de layout, elevação A, elevação B em vista
externa e vista interna.

⭐⭐ TRÊS ITENS, e dois deles são a MESMA PAREDE vista por fora e por
  dentro. A elevação A olha a parede da cabeceira: o PAINEL de 444 com a
  PORTA PIVOTANTE embutida nele, e o armário aparece só de LADO, em corte,
  pelos 60 de profundidade. A elevação B olha o armário de frente, 131 de
  largura — e o painel aparece nela como a fatia de 4 cm ao lado.
  ⛔ O "60" da elevação A e os "131" da elevação B não são dois móveis:
    são a profundidade e a largura do MESMO armário. Foi exatamente o erro
    que custou R$ 1.266 na Lavanderia, e aqui ele valia um armário inteiro.

⭐ A CADEIA VERTICAL DO ARMÁRIO FECHA EM 275, e as duas vistas concordam:
     5 de testeira + 2 de tampo
       + 68 de maleiro + 2 + 35 + 2 + 35 + 2 + 35 + 2 + 20+20+20+20
     + 2 de base + 5 de rodapé
  ⭐ E as DUAS FOLHAS têm 265 = 275 − 5 − 5: elas cobrem o tampo e a base e
    deixam de fora só a testeira e o rodapé. Por isso a vista externa cota
    5 · 265 · 5 e a interna cota a cadeia inteira. ⛔ Um número não
    contradiz o outro — ele o explica.

⭐⭐ O PAINEL TEM 292, NÃO 275. A cota de 17 no alto da elevação A é painel
  ACIMA do forro, dentro da sanca: é o que faz a luz lavar a madeira sem
  mostrar fresta. ⛔ São 0,74 m² de Nogueira que não se veem e que alguém
  tem de pagar.

⭐ O NEGATIVO DE 22 SÃO DOIS PERFIS DE LED, não um. A elevação desenha duas
  linhas vermelhas com 22 entre elas, e a chamada diz "perfil de LED com
  abas, modelo a definir". ⛔ A fatia de 22 é PAINEL, não perfil: o que
  custa por metro são os dois perfis de 2,92, não os 22 cm de vão.

⭐ A PORTA PIVOTANTE CONTA UMA VEZ, E É AQUI. Ela aparece na suíte (lado
  Nogueira Caiena) e no closet (lado Off-White Suave) — mesma folha, duas
  caras. ⛔ No Closet Master ela entra como LINHA A ZERO, para que a
  ausência fique escrita e ninguém a compre duas vezes.

⛔ FORA: a cama Queen · as duas mesas de cabeceira de Ø60 × 40 · a poltrona
  · a penteadeira · o espelho · o tapete orgânico de 270 × 350 · o
  interruptor de 3 teclas e as duas tomadas duplas · o forro e a sanca.
"""
from base import P, gaveta, engradado, DOBRADICA, CORREDICA
import base as B

NC18, NC15 = 'MDF Nogueira Caiena 18', 'MDF Nogueira Caiena 15'
OWS18, OWS15, OWS6 = ('MDF Off-White Suave 18', 'MDF Off-White Suave 15',
                      'MDF Off-White Suave 6')

I1 = 'ELEVAÇÃO A Painel da cabeceira'
I2 = 'ELEVAÇÃO A Porta pivotante mimetizada'
I3 = 'ELEVAÇÃO B Armário da suíte'

# ── a geometria, em centímetros ─────────────────────────────────────────
ALT_PAINEL, SANCA = 275.0, 17.0        # piso→forro e o que sobe pra dentro
T1, T2 = 128.0, 219.0                  # os dois trechos de painel
PORTA_L, PORTA_H = 75.0, 210.0         # a folha pivotante
BAND = ALT_PAINEL + SANCA - PORTA_H    # 82 · a faixa de cima, da cabeça da
                                       #   porta até o fim da sanca

SUITE_MASTER = [
 # ══ ITEM 01 · PAINEL DA CABECEIRA — 444 × 292 × 4 ═════════════════════
 # ⭐ A EMENDA HORIZONTAL CAI EM 210, que é a linha da cabeça da porta
 #   pivotante. ⛔ Uma peça de 292 não existe: a chapa tem 275. E a emenda
 #   tem de cair onde o desenho já desenha uma linha — em 210 ela some, em
 #   273 ela ficaria boiando dois centímetros abaixo do forro.
 P('Face do painel · trecho de 128, faixa de baixo', I1, PORTA_H, T1, 1,
   NC18, (1, 0),
   '⭐ A aresta vertical do lado do perfil de LED fica à VISTA no negativo '
   '· a do outro lado encosta no armário e não leva fita'),
 P('Face do painel · trecho de 128, faixa de cima',  I1, BAND, T1, 1,
   NC18, (1, 0), 'Da cabeça da porta até o fim da sanca · a mesma aresta '
   'do LED continua à vista'),
 P('Face do painel · trecho de 219, faixa de baixo', I1, PORTA_H, T2/2, 2,
   NC18, (1, 0),
   '⛔ 219 de largura NÃO CABE na chapa de 185 em orientação nenhuma: sai '
   'em DUAS de 109,5 · ⭐ a emenda do meio é topo a topo e não leva fita; '
   'as arestas que levam são a do LED e a do batente da porta'),
 P('Face do painel · trecho de 219, faixa de cima',  I1, BAND, T2/2, 2,
   NC18, (1, 0)),
 P('Bandeira sobre a porta pivotante', I1, BAND, PORTA_L, 1, NC18, (1, 1),
   '⭐ Os 82 de painel que passam POR CIMA da folha · é o que mimetiza a '
   'porta: de cima dela para o alto a parede volta a ser painel'),
 *engradado(I1, 38.60, NC18, 'Estrutura do painel de 4 cm',
            larg=7.0),

 # ══ ITEM 02 · PORTA PIVOTANTE — 75 × 210 × 4 ══════════════════════════
 # ⭐ DUAS CARAS DE MATERIAIS DIFERENTES NUMA FOLHA SÓ, e é o único móvel
 #   da casa assim: Nogueira Caiena para a suíte, Off-White Suave para o
 #   closet. ⛔ São duas compras de chapa para uma peça de 1,58 m².
 P('Porta pivotante · face externa, lado da suíte',  I2, PORTA_H, PORTA_L,
   1, NC18, (2, 2),
   '⭐ Mimetizada: sai do mesmo veio do painel · puxador tipo CAVA '
   'QUADRADA de 10 × 10, a 100 do chão e a 5 da borda'),
 P('Porta pivotante · face interna, lado do closet', I2, PORTA_H, PORTA_L,
   1, OWS18, (2, 2), 'Off-White Suave, Linha Sense · ⭐ é a face que o '
   'closet vê, e é nela que fica a tranca'),
 *engradado(I2, 7.20, NC18, 'Quadro interno da folha de 4 cm', larg=7.0),

 # ══ ITEM 03 · ARMÁRIO — 131 × 275 × 60 ════════════════════════════════
 P('Lateral', I3, 265, 60, 2, OWS15, (1, 0),
   'Do alto do rodapé ao pé da testeira · ⭐ as duas encostam em parede: '
   'só a aresta da frente leva fita'),
 P('Tampo', I3, 128, 60, 1, OWS15, (1, 0)),
 P('Base',  I3, 128, 60, 1, OWS15, (1, 0)),
 P('Prateleira do maleiro', I3, 128, 58, 1, OWS18, (1, 0),
   '⭐ É o fundo do maleiro de 68 · leva suporte e leva ALMA como as '
   'outras: o vão é o mesmo 128'),
 P('Prateleira', I3, 128, 58, 3, OWS18, (1, 0),
   '⭐ Vão de 128 · passa dos 70 que pedem 18 mm E dos 120 que pedem alma '
   'de aço'),
 P('Frente de gaveta', I3, 128, 20, 4, OWS15, (2, 2),
   '⭐ Gavetão de 128 de boca · puxador tipo CAVA na marcenaria'),
 *gaveta(I3, 128, 55, 18, 4, 'Caixa de gavetão'),
 P('Fundo', I3, 131, 265, 1, OWS6, (0, 0),
   '⭐ Peça única: 265 × 131 cabe na chapa de 275 × 185 deitada · ⛔ sem '
   'fita'),
 P('Testeira superior', I3, 131, 5, 1, NC15, (1, 0),
   '⭐ Os 5 do alto que as folhas de 265 não cobrem · é Nogueira porque é '
   'o que se vê'),
 P('Rodapé', I3, 131, 5, 1, NC15, (1, 0), 'Recuado, em Nogueira Caiena'),
 P('Frente · porta de giro', I3, 65.5, 265, 2, NC15, (2, 2),
   '⭐ Duas folhas de 2,65 m · puxador tipo CAVA QUADRADA de 10 × 10 em '
   'cada, a 100 do chão, com 5,5 entre as duas'),
]

# ⭐ (móvel, rótulo, nº de gavetas, preço do par)
# ⛔⛔ A PRANCHA PEDE TELESCÓPICA E A CASA NÃO USA. A regra já está cravada
#   na base.py desde 29/10: onde o executivo pede telescópica, SOBE para a
#   Hettich oculta. Pela regra do elo mais fraco uma telescópica comum
#   derrubaria a garantia da casa inteira de 10 anos para 2.
GAVETAS = [
 (I3, 'Quatro gavetões de 128 × 20 · ⛔ a prancha pede corrediça '
      'TELESCÓPICA e ela SOBE para a Hettich oculta: a casa inteira é '
      'Hettich e a garantia é uniforme de 10 anos', 4, CORREDICA),
]
# ⭐ (móvel, rótulo, nº de FOLHAS, dobradiças POR FOLHA, preço)
# ⛔ A PORTA PIVOTANTE NÃO ENTRA AQUI: ela gira em pivô de piso e teto, não
#   em caneco. A linha dela está em SERRALHERIA, a zero, porque a Base não
#   tem nem o pivô nem a tranca.
PORTAS = [
 (I3, 'Duas folhas de giro de 65,5 × 265 · ⭐ QUATRO dobradiças por folha: '
      'são 2,65 m e quase 20 kg de chapa pendurados na lateral', 2, 4,
  DOBRADICA),
]
# ⭐ (móvel, rótulo, nº de frentes, extensão de cava em cm por frente)
CAVA = [
 (I3, 'Cava QUADRADA de 10 × 10 nas duas folhas de giro', 2, 10),
 (I3, 'Cava CORRIDA nas quatro frentes de gaveta · ⛔ a prancha diz só '
      '"puxador tipo cava na marcenaria", sem cotar o recorte', 4, 128),
 (I2, 'Cava QUADRADA de 10 × 10 NAS DUAS FACES, a 100 do chão e a 5 da '
      'borda · ⭐ a prancha 40 a desenha do lado da suíte e a 44 do lado '
      'do closet: são duas, não uma', 2, 10),
]
# ⭐ (móvel, rótulo, metros de perfil)
LED = [
 (I1, 'DOIS perfis verticais de 2,92, um de cada lado do negativo de 22 · '
      '⭐ perfil de LED com abas, modelo a definir · ⛔ a fatia de 22 entre '
      'eles é PAINEL, não perfil', 5.84),
]
# ⭐ (móvel, rótulo, valor cheio)
SERRALHERIA = [
 (I2, 'Pivô de piso e teto + tranca do lado do closet · ⛔ A COTAR: a Base '
      'não tem linha para nenhum dos dois, e isto sai ZERO de propósito, '
      'para gritar. Uma folha de 1,58 m² e 4 cm pesa perto de 30 kg: o '
      'pivô é ferragem de carga, não dobradiça', 0.0),
]
PUXADORES = MOLDURA = CABIDEIROS = ALMAS = VIDRO = BASCULAS = []
# ⭐ (móvel, nome, rótulo, quantidade, unidade, chave)
OUTRAS = [
 (I1, 'Perfil de proteção de piso',
  '⭐ Só os 347 de MDF tocam o chão: os 22 do negativo são perfil de '
  'alumínio e os 75 da porta são folha, não painel', 3.47, 'm',
  'Perfil de proteção de piso'),
 (I3, 'Perfil de proteção de piso', 'O rodapé de 131 toca o chão', 1.31,
  'm', 'Perfil de proteção de piso'),
 (I3, 'Desempenador de porta',
  '⚠ UM POR FOLHA nas duas de 2,65 m · ⛔ ESTA REGRA É MINHA, NÃO DO '
  'SENHOR: folha de MDF acima de 2,20 m empena sozinha com o tempo, e a '
  'Base traz a linha a R$ 100. Se o senhor não quiser, são R$ 200 a menos '
  'e a garantia de 10 anos fica torcendo por sorte', 2, 'un',
  'Desempenador de porta'),
]

CABECA = {
 I1: ('444 × 292 × 4',
      'ELEVAÇÃO A · a parede da cabeceira · 128 + 22 de negativo com dois '
      'perfis de LED + 219 + 75 de porta pivotante = 444 · ⭐ 292 de '
      'altura, sendo 17 ACIMA DO FORRO, dentro da sanca · a emenda '
      'horizontal cai em 210, na linha da cabeça da porta'),
 I2: ('75 × 210 × 4',
      'ELEVAÇÃO A · folha mimetizada no painel · ⭐ lado da suíte em '
      'Nogueira Caiena, lado do closet em Off-White Suave · cava quadrada '
      'de 10 × 10 a 100 do chão e tranca no lado interno · ⛔ gira em '
      'PIVÔ, não em dobradiça'),
 I3: ('131 × 275 × 60',
      'ELEVAÇÃO B · vista externa e vista interna do MESMO armário · '
      'cadeia 5 de testeira + 2 de tampo + 68 de maleiro + três vãos de 35 '
      'entre quatro prateleiras de 2 + quatro gavetas de 20 + 2 de base + '
      '5 de rodapé = 275 · duas folhas de giro de 65,5 × 265'),
}

FOLHA = dict(
 aba='SUÍTE MASTER',
 sub='Gustavo Raposo · executivo Luiza Pacheco, pranchas 39, 40 e 41 · ⭐ '
     'a parede da cabeceira é um painel de 4,44 m com a porta do closet '
     'mimetizada dentro dele, e o armário de 131 encosta nela de lado',
 chapa_txt={
  NC18: 'Nogueira Caiena · Linha Design · Duratex · o PAINEL inteiro, a '
        'bandeira sobre a porta, a face da folha que a suíte vê e o '
        'engradado dos dois — ⭐ a travessa sai da própria chapa, que é a '
        'regra da casa: nada de sarrafo de pinus',
  NC15: 'Nogueira Caiena · Linha Design · Duratex · ⭐ só o que se vê do '
        'armário: as duas folhas de giro, a testeira e o rodapé',
  OWS18: 'Off-White Suave · Linha Sense · Duratex · as quatro prateleiras '
         'e a face da porta pivotante que o closet vê',
  OWS15: 'Off-White Suave · Linha Sense · Duratex · o corpo do armário por '
         'dentro: laterais, tampo, base e as quatro frentes de gaveta',
  OWS6:  'Off-White Suave · Linha Sense · Duratex · o fundo do armário, '
         'peça única de 265 × 131',
  B.ESTRUTURA: 'Branco TX · a CAIXARIA dos quatro gavetões · ⭐ é o padrão '
               'da casa para caixa de gaveta, e não é o "interno em '
               'Off-White" da prancha — esse é a parte do armário que se '
               'vê de porta aberta',
  B.FUNDO_CH:  'Branco TX · o fundo das quatro caixas de gaveta, por '
               'encaixe em rasgo',
 },
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a QUANTIDADE é '
      'a célula AMARELA no fim do painel de material, e ela sai ZERO.   '
      '⭐⭐ DOIS DESENHOS, TRÊS MÓVEIS — e a conta mais perigosa deste '
      'ambiente é a de não repetir nada. A elevação A mostra o armário de '
      'lado, pelos 60 de profundidade; a elevação B mostra o painel de '
      'lado, pelos 4 de espessura. Nenhum dos dois é móvel novo.   '
      '⭐ A PORTA PIVOTANTE É DAQUI. Ela reaparece no Closet Master porque '
      'a outra cara dela dá para lá — e lá ela entra a ZERO.   '
      '⭐ AS QUATRO PRATELEIRAS TÊM 128 DE VÃO: passam dos 70 que pedem 18 '
      'mm e dos 120 que pedem alma de aço. São quatro barras.',
 duvidas=[
  '⚠ O DESEMPENADOR DE PORTA É REGRA MINHA, não do senhor. Lancei um em '
  'cada folha de 2,65 m, R$ 100 cada, porque folha de MDF acima de 2,20 m '
  'empena sozinha e a Base já traz a linha. ⛔ E se a regra valer, ela vale '
  'TAMBÉM para as quatro folhas de 2,56 m da Rouparia, que estão sem. '
  'Diga sim ou não uma vez e eu aplico na casa inteira.',
  '⚠ O PIVÔ E A TRANCA NÃO EXISTEM NA BASE e saem ZERO. Não é esquecimento '
  '— é o buraco declarado. ⛔ Mas uma folha de 75 × 210 × 4 cm pesa perto '
  'de 30 kg e gira em ferragem de carga: pivô de piso com rolamento, não '
  'dobradiça. É o item deste ambiente que mais pode surpreender no preço.',
  '⚠ A CAVA DAS GAVETAS: a prancha diz "puxador tipo cava na marcenaria" e '
  'não cota o recorte. Adotei cava CORRIDA, 128 por frente — 5,12 m ao '
  'todo, R$ 256. ⭐ Se for cava QUADRADA de 10 como a das portas, caem para '
  '0,40 m e R$ 20. São R$ 236 de diferença numa palavra que a prancha não '
  'escreveu.',
  '⚠ O PAINEL DE 4 CM: a elevação B cota a espessura e eu a montei do jeito '
  'da casa — face de 18 mm sobre engradado de MDF de 18, que dá 3,6 e '
  'fecha nos 4 com a folga de montagem. ⛔ Se a estrutura for metalon, ou '
  'se o painel for maciço de 40 mm, a conta é outra.',
  '⚠ OS 17 DE SANCA: a elevação desenha o painel subindo 17 acima da linha '
  'do forro. Lancei como painel, porque é o que faz a luz lavar a madeira '
  'sem fresta. ⭐ Se o gesso fechar antes, são 0,74 m² de Nogueira a menos '
  '— cerca de R$ 100.',
  '⚠ A CAIXARIA DAS GAVETAS saiu em Branco TX, que é o padrão da casa, e '
  'não em Off-White Suave. ⭐ A prancha diz "interno em Off-White Suave" e '
  'eu li isso como o que se vê de porta aberta — laterais, prateleiras, '
  'fundo e frentes de gaveta, que estão todos em Off-White. A caixa por '
  'dentro da gaveta é outra coisa.',
 ],
 nao_marcenaria=[
  '⛔ A CAMA QUEEN e as DUAS MESAS DE CABECEIRA de Ø60 × 40 de altura. A '
  'planta as desenha e não as cota como marcenaria — e o render mostra as '
  'três soltas, com pé. ⭐ A cabeceira desta suíte é o PAINEL: não há '
  'cabeceira de marcenaria a fazer.',
  '⛔ A POLTRONA, a MESA (penteadeira) e o ESPELHO — os três com a chamada '
  '"a ser adquirido, modelo a definir".',
  '⛔ O TAPETE ORGÂNICO de 270 × 350.',
  '⛔ A ELÉTRICA: o interruptor de 3 teclas e as duas tomadas duplas que a '
  'elevação A cota a 93, a 56, a 75 e a 30. ⭐ As cotas delas são do '
  'eletricista; entram aqui só para dizer que o painel precisa de recorte '
  'nesses pontos — e o recorte é nosso.',
  '⛔ O FORRO e a SANCA de gesso onde o painel entra 17 cm. ⚠ O painel '
  'depende dela: se a sanca não estiver pronta na montagem, o painel sobe '
  'depois e volta uma viagem.',
 ],
 notas=[
  '⭐ É UM AMBIENTE DE TRÊS PEÇAS GRANDES e quase nenhuma ferragem: oito '
  'dobradiças, quatro pares de corrediça, dois desempenadores e os dois '
  'perfis de LED. O que pesa aqui é CHAPA — 4,44 m de painel de parede '
  'inteira.',
  '⭐ O ARMÁRIO NÃO TEM DIVISÓRIA: 131 de vão livre do rodapé ao topo. É o '
  'que torna as quatro prateleiras e os quatro gavetões tão largos, e é '
  'por isso que as quatro prateleiras pedem alma de aço.',
  '⭐ A PORTA PIVOTANTE MIMETIZADA é o detalhe caro deste projeto e o que '
  'mais aparece: fechada, a parede da cabeceira é uma só superfície de '
  'Nogueira de 4,44 m, sem batente e sem marco. ⛔ Ela exige que o painel e '
  'a folha saiam do MESMO lote de chapa, com o veio contínuo. Isso é '
  'compra casada: se faltar chapa no meio do caminho, não se compra "mais '
  'uma" — a emenda aparece.',
 ],
)
