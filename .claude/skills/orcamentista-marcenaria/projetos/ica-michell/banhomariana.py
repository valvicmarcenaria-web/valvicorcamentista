# -*- coding: utf-8 -*-
"""ICA · BANHO MARIANA — levantamento peça por peça  [28/10/2026]

páginas 201 a 207 · três detalhamentos, três itens, duas folhas de detalhe.

⚠ AS FOLHAS DESTE AMBIENTE VÊM CARIMBADAS COMO "BANHO MASTER", e não são:
  a capa da página 201 diz BANHO MARIANA, o ambiente fica ao lado do
  Closet Mariana e o Painel do executivo conta os três itens aqui. É erro
  de carimbo, o mesmo que o Closet Mariana tem — e lá as folhas vêm
  carimbadas como "SUÍTE MARIANA". ⛔ Vale avisar a arquiteta antes que
  alguém corte pela folha errada.

⭐ TRÊS PADRÕES PARA TRÊS ITENS, e cada um tem o seu:
  · DET 01, as duas portas provençais ....... Timborana Silvestre, DURATEX
  · DET 02, a moldura do espelho ............ Sal Rosa, ARAUCO
  · DET 03, as três prateleiras ............. Sal Rosa, ARAUCO
  ⭐ A caixaria vai em BRANCO, e aqui isso não é premissa minha: a VISTA
    FRONTAL INTERNA do DET 01 escreve "Parte interna do armário em MDF
    branco" com todas as letras. É a primeira vez no executivo inteiro.

⭐ A MOLDURA DAS PORTAS É DA MESMA COR DA FRENTE, então aqui vale a regra
  que o senhor fechou em 28/10: peça inteira de 6 mm usinada na router,
  não quatro réguas. É o oposto do que acontece na Suíte Mariana ao lado,
  onde a moldura é de OUTRA cor e régua continua sendo régua.

⛔ A BANCADA É QUARTZITO BIANCO SUPERIORE, com 5 de espessura aparente —
  a mesma pedra do Banho Hóspedes. Marmoraria. A cuba é redonda de apoio.

⛔ O ESPELHO DO DET 02 É VIDRACEIRO; o que é nosso é a MOLDURA de 3 cm em
  Sal Rosa, e ela tem o topo em ARCO: a peça de cima sai de um retângulo
  cheio de 87 × 38 e o miolo é perda.
"""
from base import P, provencal, ALT_MAX, CHAPA_C, DOBRADICA

TS15, TS6 = 'MDF Timborana Silvestre 15', 'MDF Timborana Silvestre 6'
SR15, SR6 = 'MDF Sal Rosa 15', 'MDF Sal Rosa 6'
EST, FUN = 'MDF Branco TX 15', 'MDF Branco TX 6'

I1 = 'DET 01 Bancada com armário'
I2 = 'DET 02 Espelho'
I3 = 'DET 03 Prateleiras'

BANHOMARIANA = [
 # ══ ITEM 01 · BANCADA COM ARMÁRIO — 120 × 70 × 60 ════════════════════
 #  VISTA FRONTAL  60 + 60 = 120 · altura 10 de cuba + 5 de pedra + 55
 #  VISTA SUPERIOR 11 + 55 + 53 = 119 ≈ 120, bancada de 64 de profundidade
 #  VISTA FRONTAL INTERNA  "Parte interna do armário em MDF branco"
 #  ⭐ as duas portas são PROVENÇAIS e a moldura é da MESMA cor: peça
 #    inteira de 6 mm usinada na router, não quatro réguas
 P('Lateral',               I1, 55, 60, 2, EST, (1, 0),
   '⭐ "Parte interna do armário em MDF branco", como a VISTA FRONTAL '
   'INTERNA escreve com todas as letras'),
 P('Tampo e base',          I1, 117, 60, 2, EST, (1, 0),
   '⭐ tampo cheio: a pedra de 120 × 64 apoia nele inteiro'),
 P('Prateleira',            I1, 117, 60, 1, EST, (1, 0),
   'A "PRATELEIRA" que a VISTA FRONTAL INTERNA nomeia, a meia altura'),
 P('Fundo',                 I1, 120, 55, 1, FUN, (0, 0), 'Encaixe em rasgo'),
 *provencal('Frente · porta de giro', I1, 60, 55, 2, TS15, TS6,
            'Provençal · duas folhas de 60 em Timborana Silvestre · ⭐ a '
            'moldura é da MESMA cor da frente, então é peça inteira usinada '
            'na router'),

 # ══ ITEM 02 · ESPELHO — 87 × 193, moldura de 3 em Sal Rosa ═══════════
 #  VISTA FRONTAL  3 + 80 + 3 = 87 · altura 3 + 151 + 35 de arco = 193
 #  ⛔ o espelho é vidraceiro; a MOLDURA é nossa
 P('Moldura · montante',    I2, 151, 3, 2, SR15, (2, 2),
   'As duas laterais de 3 de largura'),
 P('Moldura · base',        I2, 87, 3, 1, SR15, (2, 2)),
 P('Moldura · arco',        I2, 87, 38, 1, SR15, (2, 2),
   '⛔ o arco de 35 de flecha NÃO sai de uma régua: a peça vem de um '
   'retângulo cheio de 87 × 38 e o miolo é perda de usinagem'),
 P('Fundo do espelho',      I2, 87, 193, 1, SR6, (0, 0),
   '⭐ é nele que o vidraceiro cola o espelho · ⛔ sem fita: a moldura '
   'cobre o perímetro'),

 # ══ ITEM 03 · PRATELEIRAS — três de 60 × 20 × 3 ══════════════════════
 #  DET. 03 VISTA FRONTAL 60 de largura · 174 de altura das hastes
 #          cadeia 3 + 27 + 3 + 27 + 3 · VISTA SUPERIOR 60 × 20
 #  ⭐ 3 cm de espessura = duas chapas de 15 coladas, como o nome da
 #    Suíte Mariana · LED embutido sob CADA prateleira
 P('Prateleira · camada',   I3, 60, 20, 6, SR15, (2, 2),
   '⭐ duas chapas de 15 coladas por prateleira, três prateleiras · é '
   'assim que se faz os 3 cm que a VISTA LATERAL cota'),
]

# ── ferragem, declarada item a item ─────────────────────────────────────
GAVETAS = []
PORTAS  = [(I1, 'Bancada com armário · duas portas de giro provençais de '
            '55 de altura', 2, 2, DOBRADICA)]
BASCULAS = []
CAVA    = []
PUXADORES = []
# ⭐ a mão de obra da moldura provençal, por frente · ⛔ zero: a cotar
MOLDURA = [(I1, 'As duas portas provençais da bancada', 2)]
LED     = [(I3, 'Embutida sob cada uma das três prateleiras de 60', 1.8)]
CABIDEIROS = []
SARRAFOS = []
SUPORTES = []
ALMAS   = []
VIDRO   = []
SERRALHERIA = []
# ⭐ as duas portas provençais não têm puxador desenhado — a mesma leitura
#   da Suíte Hóspedes, do Banho Hóspedes e do Banho Gourmet.
OUTRAS  = [(I1, 'Pulsador', 'Duas portas provençais · abre por toque, sem '
            'ferragem à vista · ⚠ a prancha não desenha puxador nenhum',
            2, 'un', 'Pulsador'),
           (I3, 'Haste metálica de prateleira', 'Quatro hastes de 174 '
            'fixas na laje, em metal níquel escovado · ⛔ sem preço na '
            'Base', 4, 'un', 'Haste metálica de prateleira')]

CABECA = {
 I1: ('120 × 70 × 60',
      'DET. 01 VISTA FRONTAL 60 + 60 = 120 · altura 10 de cuba + 5 de '
      'quartzito + 55 de armário = 70 · VISTA SUPERIOR 11 + 55 + 53 ≈ 120 '
      'com bancada de 64 · ⭐ a VISTA FRONTAL INTERNA escreve "Parte '
      'interna do armário em MDF branco", e as duas portas são PROVENÇAIS '
      'em Timborana Silvestre, com a moldura da mesma cor'),
 I2: ('87 × 193 × 3',
      'DET. 02 VISTA FRONTAL 3 + 80 + 3 = 87 de largura · altura 3 + 151 + '
      '35 de arco = 193 · ⛔ o espelho é vidraceiro; o que é nosso é a '
      'moldura de 3 em Sal Rosa, e o arco sai de peça cheia'),
 I3: ('60 × 20 × 3  ·  três',
      'DET. 03 VISTA FRONTAL 60 de largura, hastes de 174 · cadeia 3 + 27 + '
      '3 + 27 + 3 · VISTA SUPERIOR 60 × 20 · ⭐ 3 cm é duas chapas de 15 '
      'coladas, e cada prateleira tem LED embutido por baixo'),
}

FOLHA = dict(
 aba='BANHO MARIANA',
 sub='Jéssica e Michell · Projeto ICA · páginas 201 a 207 · três itens em '
     'duas folhas de detalhe · ⚠ as folhas vêm carimbadas como "BANHO '
     'MASTER" e NÃO são: é erro de carimbo · ⭐ três padrões para três '
     'itens — Timborana Silvestre nas portas, Sal Rosa na moldura do '
     'espelho e nas prateleiras, e a caixaria em branco, que a própria '
     f'prancha manda · peça inteira até {ALT_MAX:g}, que é a chapa de '
     f'{CHAPA_C:g} menos o acerto de corte',
 chapa_txt={TS15: 'Timborana Silvestre · Duratex · a base das duas portas '
                  'provençais da bancada',
            TS6:  'Timborana Silvestre · a moldura usinada das duas portas, '
                  'peça inteira de 6 mm',
            SR15: 'Sal Rosa · Arauco · a moldura do espelho e as três '
                  'prateleiras',
            SR6:  'Sal Rosa · o fundo onde o vidraceiro cola o espelho',
            EST:  'Estrutura e caixaria · ⭐ "Parte interna do armário em '
                  'MDF branco", como a prancha escreve',
            FUN:  'Fundos · encaixe em rasgo, sem fita'},
 nota='⛔ O FRETE ESTÁ ZERADO DE PROPÓSITO: as linhas de frete da Base não '
      'têm preço ainda. Preencher lá e elas aparecem aqui sozinhas.   '
      '⚠⚠ AS FOLHAS DESTE AMBIENTE VÊM CARIMBADAS COMO "BANHO MASTER" e '
      'NÃO são: a capa da página 201 diz BANHO MARIANA. É o mesmo erro de '
      'carimbo do Closet Mariana, cujas folhas vêm como "SUÍTE MARIANA". '
      '⛔ Vale avisar a arquiteta antes que alguém corte pela folha errada. '
      '  ⭐ A CAIXARIA VAI EM BRANCO E ISSO NÃO É PREMISSA MINHA: a VISTA '
      'FRONTAL INTERNA do DET 01 escreve "Parte interna do armário em MDF '
      'branco" com todas as letras. É a primeira vez no executivo inteiro '
      'que a prancha resolve essa pergunta sozinha.   ⭐ A MOLDURA DAS '
      'PORTAS É DA MESMA COR DA FRENTE, então aqui vale a regra de 28/10: '
      'peça inteira de 6 mm usinada na router, não quatro réguas. É o '
      'oposto da Suíte Mariana ao lado.   ⛔ A BANCADA É QUARTZITO BIANCO '
      'SUPERIORE, de marmoraria, a mesma pedra do Banho Hóspedes; e o '
      'ESPELHO do DET 02 é vidraceiro — o que é nosso é a moldura.',
 duvidas=[
  'A USINAGEM DA MOLDURA PROVENÇAL continua sem preço na Base, e aqui são '
  'DUAS frentes. ⭐ A chapa das duas camadas está lançada — base de 15 e '
  'moldura inteira de 6 —, o que falta é a mão de obra da router. ⚠ É a '
  'mesma pergunta da Lavanderia, da Cozinha e da Área Gourmet, e ela já '
  'vale umas trinta e cinco frentes no projeto inteiro. ⛔ Com R$ 40 por '
  'frente seriam R$ 80 aqui; com R$ 120, R$ 240.',
  'AS DUAS PORTAS PROVENÇAIS NÃO TÊM PUXADOR DESENHADO. ⭐ Orcei PULSADOR, '
  'R$ 100 cada, pela mesma razão dos outros quatro ambientes: a moldura '
  'ocupa o perímetro da frente e cava cortaria o relevo. ⚠ As '
  'alternativas: cava usinada sairia R$ 60 pelas duas; Alças Traso 128, '
  'R$ 220.',
  'O ARCO DA MOLDURA DO ESPELHO tem 35 de flecha sobre 87 de largura, e '
  'ele NÃO sai de uma régua: a peça vem de um retângulo cheio de 87 × 38 e '
  'o miolo vira perda. ⭐ Lancei a peça cheia, que é o que vai para o plano '
  'de corte. ⚠ A usinagem do arco é router, e também não tem preço na '
  'Base. ⛔ Se a marcenaria preferir laminar o arco em tiras, muda a mão de '
  'obra mas não muda a chapa.',
  'O FUNDO DO ESPELHO de 87 × 193 em Sal Rosa 6 é PREMISSA MINHA: a '
  'prancha desenha a moldura e o espelho, e não diz em que o vidraceiro '
  'cola. ⚠ Espelho de 80 × 187 sem fundo não para em pé numa moldura de 3 '
  'cm. Se o vidraceiro entregar com o fundo dele, sai 1,7 m² de Sal Rosa 6 '
  'desta conta — e como é a única peça de 6 mm em Sal Rosa, sai a chapa '
  'inteira, R$ 350.',
  'AS QUATRO HASTES DE 174 que seguram as prateleiras do DET 03 são "em '
  'metal na cor níquel escovado", fixas na laje — serralheria, não '
  'marcenaria de verdade, e não têm preço na Base. ⚠ Haste de 1,74 m em '
  'metal escovado, feita sob medida, não é peça de catálogo. ⛔ Até existir '
  'o preço, o custo deste item é um PISO: a chapa das prateleiras são '
  'R$ 194 e a ferragem que as segura, zero.',
  'AS TRÊS PRATELEIRAS TÊM 3 CM DE ESPESSURA e eu as lancei como DUAS '
  'CHAPAS DE 15 COLADAS, porque prateleira suspensa com LED embutido por '
  'baixo precisa de corpo para esconder o perfil. ⚠ Se for chapa de 15 '
  'com borda falsa, cai metade da chapa — mas aí o LED aparece.',
  'A BANCADA TEM 64 DE PROFUNDIDADE e o armário, 60. ⭐ É o certo: a pedra '
  'avança 4 cm sobre a frente, o que dá o beiral e evita que a porta bata. '
  '⚠ É a primeira vez no projeto que o desenho faz isso — no Banho '
  'Hóspedes a pedra e o móvel tinham a mesma profundidade, e eu levantei a '
  'dúvida lá. Aqui está resolvido.',
  '⛔ A BASE METÁLICA DE 3 CM: a VISTA LATERAL desenha o armário SUSPENSO, '
  'sem rodapé e sem pé. ⚠ Então aqui não há base a lançar — mas também não '
  'há nada desenhado que segure 120 × 60 de armário mais uma pedra de '
  'quartzito. Confirmar se entra mão francesa, como no Banho Master.'],
 nao_marcenaria=[
  'Bancada em Quartzito Bianco Superiore, 120 × 64 com 5 de espessura aparente',
  'Cuba Redonda de Apoio 30 cm Branco Slim — Deca',
  'Torneira monocomando bica alta DocolKaila níquel escovado — Docol',
  'O espelho do DET 02, de uns 80 × 187 com topo em arco — vidraceiro (a moldura é nossa)',
  'Torre de tomadas da bancada',
  'Revestimentos, bacia, box e metais'],
 notas=[
  '⚠⚠ AS FOLHAS DESTE AMBIENTE VÊM CARIMBADAS COMO "BANHO MASTER", e não '
  'são: a capa da página 201 diz BANHO MARIANA, o ambiente fica ao lado do '
  'Closet Mariana e os três itens batem com o que o Painel conta aqui. É '
  'erro de carimbo, o mesmo que o Closet Mariana tem — lá as folhas vêm '
  'carimbadas como "SUÍTE MARIANA". ⛔ Vale avisar a arquiteta: duas '
  'pranchas com o carimbo errado é quanto basta para alguém cortar o '
  'móvel do banheiro errado.',
  '⭐⭐ A CAIXARIA VAI EM BRANCO E A PRANCHA É QUEM DIZ. A VISTA FRONTAL '
  'INTERNA do DET 01 escreve "Parte interna do armário em MDF branco" com '
  'todas as letras — é a primeira vez no executivo inteiro que o desenho '
  'resolve essa pergunta sozinho, e ela apareceu como dúvida em quase '
  'todos os outros ambientes.',
  '⭐ A MOLDURA DAS PORTAS É DA MESMA COR DA FRENTE, e por isso aqui vale '
  'a regra que o senhor fechou em 28/10: peça inteira de 6 mm usinada na '
  'router, não quatro réguas. ⛔ É o oposto exato da Suíte Mariana ao '
  'lado, onde a moldura é Sal Rosa sobre Palha Indiana e régua continua '
  'sendo régua. Os dois quartos são da mesma menina e têm regras opostas '
  'de moldura — vale ter isso claro na fábrica.',
  '⭐ TRÊS PADRÕES PARA TRÊS ITENS, um para cada: Timborana Silvestre nas '
  'duas portas, Sal Rosa na moldura do espelho e nas prateleiras, branco '
  'na caixaria. ⚠ O Sal Rosa é o mesmo da Suíte Mariana e do Closet, '
  'então ele não puxa compra nova — produzidos juntos, os três ambientes '
  'da Mariana dividem a mesma chapa.',
  '⚠ NENHUMA PEÇA PASSA DA CHAPA. A maior é o fundo do espelho, de 193 × '
  '87, e ele cabe inteiro nos 275 × 185. É o segundo ambiente do projeto '
  'inteiro em que isso acontece.'],
)
