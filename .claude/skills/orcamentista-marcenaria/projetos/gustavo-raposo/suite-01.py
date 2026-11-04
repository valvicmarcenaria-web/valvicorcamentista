# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO · SUÍTE 01 FILHOS — peça por peça  [30/10/2026]

pranchas 48 a 53 · planta de layout, elevação A, elevação B em vista
externa e interna, elevação C em vista externa e interna, planta e vista da
base de cama, mais o detalhe 09 do perfil de LED embutido na cabeceira.

⭐⭐⭐ O AMBIENTE MAIS CHEIO DA CASA: painel de cabeceira frisado, armário em
  L nas duas paredes, mesa suspensa de 2,93 m, gaveteiro com rodízios e
  DUAS bases de cama, uma delas com gavetão de cama auxiliar.

⛔⛔⛔ E O ARMÁRIO EM L TEM UM CANTO QUE APARECE DUAS VEZES. A elevação B
  cota 190 = 60 + 130; a C cota 240 = 180 + 60. Os dois "60" são O MESMO
  módulo de canto, desenhado de frente em cada uma das duas vistas — é o
  que o rótulo "cabideiro contínuo DE CANTO", repetido nas duas, diz em
  voz alta. ⭐ Somar 190 + 240 dá 430 de armário; o armário tem 370.
    190 + 240 − 60 = 370
  ⛔ Sessenta centímetros de armário de 2,75 m, com maleiro, duas
    prateleiras e DOIS cabideiros — era quase R$ 2.000 comprados em
    dobro, e nada na planilha teria acusado.
  ⭐ Por isso o canto é ITEM SEPARADO nesta aba: para que ele se veja.

⭐ A CADEIA VERTICAL DO ARMÁRIO FECHA EM 275 nas duas paredes:
     10 de rodapé + 255 de corpo + 10 de testeira
  e o 255 se abre em 62 de maleiro + 2 + 109 + 2 + 80 — ou, na coluna de
  prateleira da elevação C, em 62 + 2 + três vãos de 35 + quatro frentes
  de 20.

⭐ QUATRO PORTAS DE CORRER FLUTUANTES, duas de MDF e duas de espelho prata,
  em sistema SS-150 SEM amortecedor, com puxador NEO32 Bronze. Duas correm
  nos 130 da elevação B e duas nos 180 da C. ⛔ "Flutuante" quer dizer sem
  moldura: o espelho é COLADO na folha de MDF, não emoldurado em alumínio.

⛔ FORA: o papel de parede dos 165 acima da cabeceira · as três arandelas ·
  os dois tapetes · a mesa de cabeceira redonda a ser adquirida · a janela
  acima da mesa · os colchões.
"""
from base import P, gaveta, engradado, CORREDICA

OWS15, OWS18 = 'MDF Off-White Suave 15', 'MDF Off-White Suave 18'
NT15, NT18 = 'MDF Nogueira Thar 15', 'MDF Nogueira Thar 18'
BR15, BR18, BR6 = 'MDF branco 15', 'MDF branco 18', 'MDF Branco TX 6'

I1 = 'ELEVAÇÃO A Painel de cabeceira frisado'
I2 = 'ELEVAÇÃO B Armário de 130'
I3 = 'ELEVAÇÃO C Armário de 180'
I4 = 'CANTO Módulo de canto do armário em L'
I5 = 'ELEVAÇÃO B Mesa suspensa de 293'
I6 = 'ELEVAÇÃO B Gaveteiro com rodízios'
I7 = 'BASE CAMA Duas bases de 196 × 96'

CORPO, PROF = 255.0, 60.0        # 275 − 10 de rodapé − 10 de testeira
CB, CC = 63.5, 88.5              # colunas da elevação B e da C
CANTO = 57.0                     # o vão interno do módulo de 60
N_FRISO = 27                     # a cada 14,6 nos 395 do painel

SUITE_01 = [
 # ══ ITEM 01 · PAINEL DE CABECEIRA — 395 × 110 ═════════════════════════
 P('Face do painel de cabeceira', I1, 110, 197.5, 2, NT18, (1, 1),
   f'⛔ 395 de largura não cabe na chapa: sai em DUAS de 197,5 · ⭐ a '
   f'emenda cai no meio da parede, entre duas camas, e some dentro de um '
   f'dos {N_FRISO} frisos — que é o único lugar de um painel frisado onde '
   f'uma junta não aparece'),
 *engradado(I1, 11.85, NT18, 'Travessa de fixação do painel na parede',
            larg=7.0),

 # ══ ITEM 02 · ARMÁRIO DE 130 — elevação B ═════════════════════════════
 P('Lateral e divisória vertical', I2, CORPO, PROF, 3, OWS15, (1, 0),
   '⭐ Duas laterais e uma divisória · DUAS colunas de 63,5 · ⛔ a lateral '
   'do lado do canto é compartilhada e está contada aqui, não no canto'),
 P('Tampo e base',  I2, CB, PROF, 4, OWS15, (1, 0)),
 P('Testeira superior', I2, 130, 10, 1, OWS15, (1, 0)),
 P('Rodapé',            I2, 130, 10, 1, OWS15, (1, 0)),
 P('Prateleira do maleiro', I2, CB, 58, 2, BR18, (1, 0),
   'Fecha o maleiro de 62 em cada coluna'),
 P('Prateleira', I2, CB, 58, 2, BR18, (1, 0),
   '⭐ É ela que parte o 191 em 109 em cima e 80 embaixo'),
 P('Frente de gaveta', I2, CB, 20, 4, BR15, (2, 2),
   '⭐ Quatro gavetas na coluna da direita · puxador tipo CAVA na '
   'marcenaria · interno em MDF Branco, que é a chamada da prancha'),
 *gaveta(I2, CB, 55, 18, 4, 'Caixa de gaveta'),
 P('Fundo', I2, 255, 130, 1, BR6, (0, 0), 'Peça única · ⛔ sem fita'),
 P('Frente · porta de correr em MDF', I2, 67, CORPO, 1, OWS18, (2, 2),
   '⭐ 18 mm e não 15: folha de 2,55 m que corre pendurada no trilho '
   'empena com 15 · ⛔ flutuante, sem moldura · puxador NEO32 Bronze'),
 P('Frente · porta de correr com espelho colado', I2, 67, CORPO, 1, OWS18,
   (2, 2), '⭐ A folha é de MDF e o espelho prata vai COLADO nela — é o '
   'que "flutuante" quer dizer · o m² do espelho está na linha de vidro'),

 # ══ ITEM 03 · ARMÁRIO DE 180 — elevação C ═════════════════════════════
 P('Lateral e divisória vertical', I3, CORPO, PROF, 3, OWS15, (1, 0),
   '⭐ Duas laterais e uma divisória · DUAS colunas de 88,5'),
 P('Tampo e base',  I3, CC, PROF, 4, OWS15, (1, 0)),
 P('Testeira superior', I3, 180, 10, 1, OWS15, (1, 0)),
 P('Rodapé',            I3, 180, 10, 1, OWS15, (1, 0)),
 P('Prateleira do maleiro', I3, CC, 58, 2, BR18, (1, 0)),
 P('Prateleira', I3, CC, 58, 4, BR18, (1, 0),
   '⭐ Três na coluna de prateleira, nos vãos de 35, e uma na coluna de '
   'cabideiro, partindo o 191 em 109 e 80'),
 P('Frente de gaveta', I3, CC, 20, 2, BR15, (2, 2),
   'Puxador tipo CAVA na marcenaria'),
 P('Frente da sapateira deslizante', I3, CC, 20, 2, BR15, (2, 2),
   '⭐ Mesma frente de 20 da gaveta · ⛔ sem suporte: ela corre em '
   'corrediça'),
 *gaveta(I3, CC, 55, 18, 2, 'Caixa de gaveta'),
 *gaveta(I3, CC, 55, 18, 2, 'Caixa de gaveta · bandeja da sapateira'),
 P('Fundo', I3, 255, 180, 1, BR6, (0, 0),
   '⭐ Peça única: 180 ainda cabe nos 185 da chapa · ⛔ sem fita'),
 P('Frente · porta de correr em MDF', I3, 92, CORPO, 1, OWS18, (2, 2),
   '⭐ 18 mm · flutuante, sem moldura · puxador NEO32 Bronze'),
 P('Frente · porta de correr com espelho colado', I3, 92, CORPO, 1, OWS18,
   (2, 2), 'Espelho prata colado na folha de MDF'),

 # ══ ITEM 04 · MÓDULO DE CANTO — 60 × 60, UMA VEZ SÓ ═══════════════════
 P('Tampo e base', I4, CANTO, PROF, 2, OWS15, (1, 0),
   '⛔ SEM LATERAL PRÓPRIA: os dois lados deste módulo são as laterais dos '
   'armários de 130 e de 180, já contadas lá. Contá-las aqui seria o '
   'mesmo erro do canto em dobro, um degrau abaixo'),
 P('Testeira superior', I4, 60, 10, 1, OWS15, (1, 0)),
 P('Rodapé',            I4, 60, 10, 1, OWS15, (1, 0)),
 P('Prateleira do maleiro', I4, CANTO, 58, 1, BR18, (1, 0)),
 P('Prateleira',            I4, CANTO, 58, 1, BR18, (1, 0)),
 P('Fundo', I4, 255, 60, 2, BR6, (0, 0),
   '⭐ DUAS: o canto tem duas paredes atrás de si, uma de cada arm · '
   '⛔ sem fita'),

 # ══ ITEM 05 · MESA SUSPENSA — 293 × 55 × 5, a 75 do chão ══════════════
 P('Tampo da mesa', I5, 146.5, 55, 2, NT18, (1, 1),
   '⛔ 293 não cabe na chapa de 275: sai em DUAS de 146,5 · ⭐ a emenda '
   'cai no eixo do gaveteiro, que é onde o olho não procura'),
 P('Saia frontal de 5', I5, 146.5, 5, 2, NT18, (1, 1),
   '⭐ É ela que dá os 5 cm de espessura aparente do tampo · ⛔ sem ela a '
   'mesa vira uma prateleira de 18 mm, que não é o que a elevação desenha'),
 *engradado(I5, 9.0, NT18, 'Estrutura do tampo e fixação na parede',
            larg=7.0),

 # ══ ITEM 06 · GAVETEIRO COM RODÍZIOS — 75 × 68 × 55 ═══════════════════
 P('Lateral',      I6, 60, 55, 2, NT15, (1, 0),
   '⭐ 60 = 2 de tampo + quatro gavetas de 14 + 2 de base · os 8 que '
   'faltam para os 68 são o rodízio'),
 P('Tampo e base', I6, 72, 55, 2, NT15, (1, 0)),
 P('Frente de gaveta', I6, 72, 14, 4, NT15, (2, 2),
   '⭐ Quatro frentes de 14 · puxador tipo CAVA de 35 na marcenaria'),
 *gaveta(I6, 72, 50, 12, 4, 'Caixa de gaveta'),
 P('Fundo', I6, 75, 60, 1, BR6, (0, 0), '⛔ sem fita'),

 # ══ ITEM 07 · DUAS BASES DE CAMA — 196 × 96 × 45 ══════════════════════
 P('Lateral da base',   I7, 196, 45, 4, NT18, (2, 2),
   '⭐ Duas por base, duas bases · a cota de 2 da planta é a espessura da '
   'parede da base, que é a própria chapa de 18 com fita'),
 P('Cabeceira e pé da base', I7, 92, 45, 4, NT18, (2, 2)),
 P('Gavetão da cama auxiliar · frente', I7, 190, 30, 1, NT18, (2, 2),
   '⭐ Só UMA das duas bases leva gavetão · puxador a definir, lançado '
   'como duas cavas de 20'),
 P('Gavetão da cama auxiliar · lateral', I7, 88, 28, 2, NT18, (1, 0)),
 P('Gavetão da cama auxiliar · costas',  I7, 190, 28, 1, NT18, (1, 0)),
 P('Gavetão da cama auxiliar · fundo',   I7, 190, 88, 1, BR6, (0, 0),
   '⛔ sem fita · ⭐ é ele que recebe o terceiro quadro de metalon, o da '
   'cama auxiliar'),
]

# ⭐ (móvel, rótulo, nº de gavetas, preço do par)
GAVETAS = [
 (I2, 'Quatro gavetas de 63,5 × 20 na coluna da direita · ⛔ a prancha '
      'pede TELESCÓPICA e ela sobe para a Hettich oculta, regra da casa',
  4, CORREDICA),
 (I3, 'Duas gavetas e duas sapateiras deslizantes de 88,5 × 20 · '
      '⛔ telescópica na prancha, Hettich oculta no orçamento', 4,
  CORREDICA),
 (I6, 'Quatro gavetas de 72 × 14 · ⭐ aqui a prancha pede INVISÍVEL, que '
      'já é a Hettich oculta', 4, CORREDICA),
 (I7, 'O gavetão da cama auxiliar · ⚠ lancei um par de corrediça da casa, '
      'mas o que este gavetão pede é CORREDIÇA DE CARGA — colchão de '
      'solteiro e estrado dentro dele passam de 40 kg, e a linha de carga '
      'da Base está sem preço', 1, CORREDICA),
]
# ⭐ (móvel, rótulo, nº de frentes, extensão de cava em cm por frente)
CAVA = [
 (I2, 'As quatro frentes de gaveta de 63,5', 4, CB),
 (I3, 'As quatro frentes de 88,5 — duas gavetas e duas sapateiras', 4, CC),
 (I6, 'As quatro frentes do gaveteiro · ⭐ a cava é de 35, cotada na '
      'elevação B, e não a largura inteira da frente', 4, 35),
 (I7, 'O gavetão da cama auxiliar · ⚠ a prancha diz só "puxador a '
      'definir" e desenha DOIS recortes na frente', 2, 20),
]
# ⭐ (móvel, rótulo, quantidade)
CABIDEIROS = [
 (I2, 'TRÊS: dois na coluna da esquerda, de 109 e de 80, e um de 109 '
      'sobre as quatro gavetas', 3),
 (I3, 'DOIS na coluna de cabideiro, de 109 e de 80', 2),
 (I4, 'DOIS contínuos DE CANTO, de 109 e de 80 · ⭐ é o mesmo par que as '
      'elevações B e C desenham cada uma do seu lado: eles dobram a '
      'esquina, e por isso estão aqui e não lá', 2),
]
# ⭐ (móvel, rótulo, metros de perfil)
LED = [
 (I1, 'Perfil de LED com abas EMBUTIDO NO TOPO DA CABECEIRA, nos 395 · '
      '⭐ o detalhe 09 desenha o rasgo de 2 na própria chapa e escreve '
      '"Cabeceira em MDF": o perfil é nosso', 3.95),
]
# ⭐ (móvel, rótulo, qtd, comprimento, largura, chave)
VIDRO = [
 (I2, 'Espelho prata COLADO na folha de correr de 67 × 255', 1, 67, 255,
  'Espelho prata colado'),
 (I3, 'Espelho prata COLADO na folha de correr de 92 × 255', 1, 92, 255,
  'Espelho prata colado'),
]
PORTAS = BASCULAS = PUXADORES = MOLDURA = ALMAS = SERRALHERIA = []
# ⭐⭐ DOIS MODOS DE ABRIR NO MESMO ARMÁRIO, e é o que a prancha manda: a
#   FOLHA DE CORRER abre pelo puxador NEO32 Bronze e as GAVETAS DE DENTRO
#   abrem por cava usinada. São frentes diferentes do mesmo móvel — a
#   folha fica do lado de fora, a gaveta aparece quando ela corre.
#   ⛔ A regra do auditor é por MÓVEL, não por frente, e acusaria os dois.
#     Declarar aqui é o jeito de a exceção ficar ESCRITA: não é a regra
#     que está errada, é este móvel que de fato tem as duas coisas.
ABRE_MISTO = [I2, I3]
# ⭐ (móvel, nome, rótulo, quantidade, unidade, chave)
OUTRAS = [
 (I1, 'Usinagem de friso',
  f'⭐ {N_FRISO} frisos verticais de 0,5 × 0,5, a cada 14,6 nos 395, '
  f'subindo os 110 inteiros · {N_FRISO*1.10:.2f} m de rasgo · ⛔ A COTAR: '
  'a linha entrou na Base hoje e está sem preço, de propósito',
  round(N_FRISO*1.10, 2), 'm', 'Usinagem de friso'),
 (I2, 'Sistema de correr SS-150',
  '⭐ Um conjunto para as duas folhas dos 130 · a prancha crava "sem '
  'amortecedor"', 1, 'conjunto', 'Sistema de correr SS-150'),
 (I3, 'Sistema de correr SS-150',
  '⭐ Um conjunto para as duas folhas dos 180', 1, 'conjunto',
  'Sistema de correr SS-150'),
 (I2, 'Puxador NEO32 Bronze',
  '⛔ Duas folhas · A COTAR: a Base traz a linha SEM PREÇO e ela sai zero '
  'de propósito, para gritar', 2, 'un', 'Puxador NEO32 Bronze'),
 (I3, 'Puxador NEO32 Bronze', '⛔ Duas folhas · A COTAR', 2, 'un',
  'Puxador NEO32 Bronze'),
 (I6, 'Rodízio de gaveteiro',
  '⭐ Quatro, e são eles que dão os 8 cm entre a base do gaveteiro e o '
  'chão · ⛔ A COTAR: a Base traz a linha sem preço', 4, 'un',
  'Rodízio de gaveteiro'),
 (I7, 'Estrado em metalon',
  '⭐ TRÊS quadros: um por base de cama e MAIS UM dentro do gavetão, que é '
  'cama de verdade e leva colchão · é a regra que o senhor cravou em 28/10',
  3, 'quadro', 'Estrado em metalon'),
 (I7, 'Corrediça de carga',
  '⚠ O QUE O GAVETÃO REALMENTE PEDE. Está declarada a ZERO porque a Base '
  'não tem preço para ela, e a corrediça que entrou na conta é a comum da '
  'casa. ⛔ Se a de carga custar mais, a diferença aparece aqui',
  1, 'par', 'Corrediça de carga'),
 (I1, 'Perfil de proteção de piso',
  'O painel de cabeceira de 395 toca o chão', 3.95, 'm',
  'Perfil de proteção de piso'),
 (I2, 'Perfil de proteção de piso', 'O rodapé de 130 toca o chão', 1.30,
  'm', 'Perfil de proteção de piso'),
 (I3, 'Perfil de proteção de piso', 'O rodapé de 180 toca o chão', 1.80,
  'm', 'Perfil de proteção de piso'),
 (I4, 'Perfil de proteção de piso', 'O rodapé de 60 do canto toca o chão',
  0.60, 'm', 'Perfil de proteção de piso'),
]

CABECA = {
 I1: ('395 × 110',
      'ELEVAÇÃO A · painel de cabeceira em Nogueira Thar com 27 frisos '
      'verticais de 0,5 × 0,5 · perfil de LED embutido no topo, detalhe 09 '
      '· ⭐ acima dele são 165 de PAPEL DE PAREDE, que não é nosso: a '
      'parede tem 275 e o painel só 110'),
 I2: ('130 × 275 × 60',
      'ELEVAÇÃO B · duas colunas de 63,5 · uma com dois cabideiros de 109 '
      'e 80, outra com um cabideiro de 109 sobre quatro gavetas de 20 · '
      'duas folhas de correr de 67, uma em MDF e uma com espelho colado'),
 I3: ('180 × 275 × 60',
      'ELEVAÇÃO C · duas colunas de 88,5 · uma com três vãos de 35 entre '
      'prateleiras e quatro frentes de 20 embaixo, outra com dois '
      'cabideiros · duas folhas de correr de 92'),
 I4: ('60 × 60 × 275',
      '⛔ ESTE MÓDULO APARECE NAS DUAS ELEVAÇÕES E EXISTE UMA VEZ SÓ. A '
      'elevação B o cota dentro dos seus 190 e a C dentro dos seus 240; os '
      'dois "60" são este mesmo canto. ⭐ Somar as duas elevações daria '
      '430 de armário — o armário tem 370'),
 I5: ('293 × 55 × 5, a 75 do chão',
      'ELEVAÇÃO B · tampo suspenso em Nogueira Thar, sem pé · ⭐ os 5 cm '
      'de espessura são tampo de 18 mais saia de 5 sobre engradado'),
 I6: ('75 × 68 × 55',
      'ELEVAÇÃO B · gaveteiro solto sob a mesa, sobre quatro rodízios · '
      'quatro gavetas de 14 com corrediça invisível e cava de 35'),
 I7: ('196 × 96 × 45, duas unidades',
      'PRANCHA 53 · duas bases de cama de solteiro em Nogueira Thar, '
      'parede de 2 · UMA delas leva o gavetão de cama auxiliar de 190 × 30 '
      '· ⭐ TRÊS quadros de estrado em metalon ao todo: dois dos leitos e '
      'um da cama auxiliar'),
}

FOLHA = dict(
 aba='SUÍTE 01 FILHOS',
 sub='Gustavo Raposo · executivo Luiza Pacheco, pranchas 48 a 53 · ⭐ sete '
     'itens: cabeceira frisada, armário em L nas duas paredes, mesa '
     'suspensa, gaveteiro com rodízios e duas bases de cama',
 chapa_txt={
  NT18: 'Nogueira Thar · Linha Design · Duratex · a cabeceira frisada, a '
        'mesa, as duas bases de cama e o gavetão da cama auxiliar',
  NT15: 'Nogueira Thar · Linha Design · Duratex · o gaveteiro de rodízios '
        'inteiro',
  OWS18: 'Off-White Suave · Linha Sense · Duratex · ⭐ SÓ as quatro folhas '
         'de correr · 18 mm porque folha de 2,55 m pendurada em trilho '
         'empena com 15',
  OWS15: 'Off-White Suave · Linha Sense · Duratex · a estrutura dos três '
         'trechos de armário: laterais, divisórias, tampos, bases, '
         'testeiras e rodapés',
  BR18:  'Branco · as doze prateleiras internas · ⭐ "interno em MDF '
         'Branco" é chamada da prancha',
  BR15:  'Branco · as oito frentes de gaveta e de sapateira dentro dos '
         'armários',
  BR6:   'Branco TX · os fundos dos armários e do gavetão da cama',
  'MDF Branco TX 15': 'Branco TX · a caixaria das dezesseis gavetas',
 },
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a QUANTIDADE é '
      'a célula AMARELA no fim do painel de material, e ela sai ZERO.   '
      '⛔⛔ O CANTO DO ARMÁRIO EM L É UM ITEM SEPARADO, e é de propósito. '
      'As elevações B e C desenham cada uma o mesmo módulo de 60 dentro '
      'dos seus totais: 190 + 240 = 430, e o armário tem 370. ⭐ Separar o '
      'canto é o que impede que ele seja comprado duas vezes.   '
      '⭐ SÃO SETE ITENS E QUATRO PADRÕES DE CHAPA. O quarto de criança é '
      'o ambiente mais caro da casa depois da cozinha, e a maior parte '
      'disso é armário.   '
      '⭐ TRÊS QUADROS DE ESTRADO EM METALON: dois leitos e a cama '
      'auxiliar. A regra é do senhor, 28/10.',
 duvidas=[
  '⚠ O NÚMERO DE FRISOS. A prancha repete "Friso 0,5x0,5cm" peça por peça '
  'e não cota o espaçamento. Contei 27 nos 395, que dá um a cada 14,6 — é '
  'o que o desenho mostra. ⛔ E o PREÇO não existe: a linha "Usinagem de '
  'friso" entrou hoje na Base sem valor, de propósito, e sai ZERO. São '
  '29,70 m de rasgo numa máquina que ainda não foi cotada.',
  '⚠ O ESPELHO DAS FOLHAS DE CORRER entrou como ESPELHO PRATA COLADO na '
  'folha de MDF, não como porta de espelho em alumínio. ⭐ É o que '
  '"flutuante" e "puxador NEO32" querem dizer: a folha é de madeira e o '
  'espelho vai colado nela. ⛔ Se a arquiteta quiser folha de alumínio com '
  'espelho, a conta muda e o puxador NEO32 some.',
  '⚠ O GAVETÃO DA CAMA AUXILIAR. Lancei um par de corrediça da casa, '
  'R$ 150, mas o que ele pede é CORREDIÇA DE CARGA: colchão de solteiro '
  'mais estrado passam de 40 kg e saem puxados com a mão. ⛔ A linha de '
  'carga da Base está sem preço e eu a declarei a zero ao lado. Vale '
  'cotar antes de fechar.',
  '⚠ A MESA DE 2,93 M É SUSPENSA e a elevação não desenha pé nenhum. '
  'Lancei engradado e fixação na parede. ⛔ Dois metros e noventa de '
  'balanço em parede de alvenaria é muito: se a parede for de drywall, '
  'esta mesa precisa de montante metálico atrás, e isso não está aqui.',
  '⚠ A ESPESSURA DO PAINEL DE CABECEIRA não está cotada em lugar nenhum — '
  'diferente do painel da Suíte Master, que traz os 4 cm. Montei como face '
  'de 18 sobre travessa, que é o jeito da casa. ⚠ O detalhe 09 cota só o '
  'rasgo de 2 do perfil de LED.',
  '⚠ A LARGURA DAS COLUNAS saiu por dedução dos totais cotados: 63,5 nos '
  '130 e 88,5 nos 180. ⛔ A prancha cota os trechos e não as colunas.',
 ],
 nao_marcenaria=[
  '⛔ O PAPEL DE PAREDE "a definir" dos 165 acima da cabeceira. ⭐ É ele '
  'que explica por que o painel tem 110 e não 275: o resto da parede é '
  'papel, não madeira.',
  '⛔ AS TRÊS ARANDELAS e toda a elétrica: interruptor de 4 teclas, '
  'interruptor de 3 teclas com 2 tomadas, tomadas duplas, tomada simples '
  'e os dois pontos para rede. ⚠ Os pontos de rede caem atrás da mesa '
  'suspensa: o tampo precisa de passagem de fio, e isso é nosso.',
  '⛔ O TAPETE de 200 × 400 e a MESA DE CABECEIRA redonda de Ø60, "a ser '
  'adquirida, modelo a definir".',
  '⛔ A JANELA acima da mesa, que a elevação B desenha hachurada como '
  'vidro.',
  '⛔ OS DOIS COLCHÕES de solteiro e o da cama auxiliar. ⭐ O que é nosso é '
  'a base e o estrado de metalon que os recebe.',
 ],
 notas=[
  '⭐ O ARMÁRIO EM L TEM 3,70 M DE FRENTE em duas paredes, com sete '
  'cabideiros, dezesseis gavetas e quatro folhas de correr. É o maior '
  'armário de quarto da casa.',
  '⭐ NENHUMA PRATELEIRA PEDE ALMA DE AÇO: a maior tem 88,5 de vão e a '
  'regra da casa é 120. ⛔ Quem segurou isso foram as divisórias — o mesmo '
  'que acontece no Closet Master e o contrário do armário da Suíte Master.',
  '⭐ A CAMA AUXILIAR É UMA CAMA, não uma gaveta de roupa de cama. Por '
  'isso ela leva o terceiro quadro de estrado em metalon e por isso a '
  'corrediça dela merece atenção: é o único móvel do quarto que sai do '
  'lugar com peso de gente em cima.',
 ],
)
