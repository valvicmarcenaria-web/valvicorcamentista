# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO · DESPENSA — levantamento peça por peça  [29/10/2026]

prancha 31 · planta de layout e elevações A e B.

⭐ O AMBIENTE MAIS SIMPLES DA CASA, e por isso o que mais engana: não há
  armário, não há porta e não há gaveta. São DOZE PRATELEIRAS de parede, em
  "L", e o que elas custam não é chapa — é FIXAÇÃO e ALMA DE AÇO.

⭐⭐ A CADEIA VERTICAL FECHA NO PÉ-DIREITO: 141 de vão livre embaixo, e
  depois seis prateleiras de 4 cm com 35 de espaço entre elas:
      141 + 6 × (35 + 4) = 141 + 234 = 375
  São os mesmos 375 de pé-direito da cozinha e da lavanderia.

⭐ A CADEIA HORIZONTAL RESOLVE O CANTO, que é onde este tipo de levantamento
  costuma contar peça a mais: a planta cota 91 + 40 + 40 + 136 = 307, e as
  elevações cotam 131 + 176 = 307. ⛔ Os DOIS 40 são peças diferentes, uma
  em cada perna do "L" — não é o mesmo canto contado duas vezes.

⚠⚠ "FIXAÇÃO INVISÍVEL" É O CUSTO DESTE AMBIENTE. A prancha escreve isso nas
  três chamadas. Prateleira de parede sem suporte à vista se pendura em
  mão-francesa oculta ou em cavilha de aço embutida — não é o jogo de quatro
  suportes de R$ 6,50 que vai dentro de armário. ⛔ A Base tem a linha de
  suporte oculto a R$ 30, mas ela é a LEGADA, de 40 em 40 cm, e o próprio
  Jonathan a tirou de prateleira de armário em 28/10. Aqui ela volta porque
  aqui ela é o que a prancha pede. Está na caixa de dúvidas.

⛔ FORA: o revestimento Branco Retificado Acetinado 30 × 60 das paredes.
"""
from base import P

BD18 = 'MDF Branco Diamante 18'

I1 = 'ELEVAÇÃO A Prateleiras da parede de 131'
I2 = 'ELEVAÇÃO B Prateleiras da parede de 176'

DESPENSA = [
 # ══ ITEM 01 · PRATELEIRAS DA ELEVAÇÃO A — 131 × 40, seis níveis ═══════
 # ⭐⭐ DOZE PEÇAS PARA SEIS PRATELEIRAS [Jonathan, 30/10/2026]:
 #   > "cada prateleira com duas peças inteiras, duplamente revestindo uma
 #   >  estrutura de metalom no mesmo formato"
 #   ⭐ É um SANDUÍCHE: quadro de metalon no formato da prateleira, revestido
 #     em cima e embaixo por uma peça INTEIRA de 18 mm. Por isso a quantidade
 #     é 12 e não 6 — e as duas faces aparecem, logo as duas levam fita nas
 #     quatro arestas.
 P('Prateleira · revestimento', I1, 131, 40, 12, BD18, (2, 2),
   '⭐ DUAS peças por prateleira: seis prateleiras, doze peças · revestem o '
   'quadro de metalon em cima e embaixo · ⛔ sem alma de aço: quem resiste à '
   'flecha é o metalon, a chapa só reveste · ⛔ fixação invisível, sem '
   'lateral e sem suporte de armário'),
 # ══ ITEM 02 · PRATELEIRAS DA ELEVAÇÃO B — 176 × 40, seis níveis ═══════
 # ⛔⛔ "sem suporte" NA OBS, e ela não é enfeite [30/10/2026]: é o que
 #   tira esta prateleira da conta automática do jogo de quatro suportes de
 #   armário. Sem a marca, o ITEM 02 saía pagando a fixação DUAS vezes — o
 #   jogo de armário E o suporte oculto, R$ 39,00 de linha que não existe.
 #   ⭐ O ambiente inteiro é FIXAÇÃO INVISÍVEL: não há lateral de armário
 #     onde um suporte de prateleira possa encaixar.
 P('Prateleira · revestimento', I2, 176, 40, 12, BD18, (2, 2),
   '⭐ DUAS peças por prateleira: seis prateleiras, doze peças · 176 de vão '
   'livre, sem apoio no meio — é o quadro de metalon que vence o vão · '
   '⛔ sem alma de aço: o metalon faz esse serviço · ⛔ fixação invisível, '
   'sem lateral e sem suporte de armário'),
]

# ⭐ nada de gaveta, porta, báscula, cava, LED, vidro ou serralheria aqui.
GAVETAS = PORTAS = BASCULAS = PUXADORES = MOLDURA = []
LED = CABIDEIROS = ALMAS = VIDRO = SERRALHERIA = CAVA = []
# ⭐ (móvel, nome, rótulo, quantidade, unidade, chave)
OUTRAS = [
 # ⭐⭐ A ESTRUTURA DE METALON, UMA POR PRATELEIRA [Jonathan, 30/10/2026]:
 #   > "considere um custo de 250,00 para estrutura, sera uma em cada"
 #   ⛔⛔ E ELA SUBSTITUI DUAS LINHAS QUE SAÍRAM: o SUPORTE OCULTO de R$ 30
 #     (54 unidades, R$ 1.620) e a ALMA DE AÇO de R$ 50 por prateleira. O
 #     quadro de metalon é as duas coisas ao mesmo tempo — ele vence o vão
 #     E se fixa na alvenaria. Manter as três seria pagar o mesmo serviço
 #     três vezes, que é o erro que este ambiente já cometeu uma vez.
 #   ⚠ Está na caixa de dúvidas: se o senhor quiser o metalon SÓ como alma,
 #     com fixação por mão-francesa à parte, o suporte volta.
 (I1, 'Estrutura de metalon', '⭐ Uma por prateleira · quadro soldado no '
  'formato da prateleira de 131 × 40, revestido nas duas faces · ⛔ é ao '
  'mesmo tempo a ESTRUTURA contra a flecha e a FIXAÇÃO INVISÍVEL que a '
  'prancha pede · R$ 250 a unidade, cravado pelo Jonathan em 30/10',
  6, 'un', 'Estrutura de metalon'),
 (I2, 'Estrutura de metalon', '⭐ Uma por prateleira · quadro de 176 × 40, '
  'o vão mais exigente do ambiente · ⛔ sem apoio no meio: é o metalon que '
  'segura os 1,76 m', 6, 'un', 'Estrutura de metalon'),
]

CABECA = {
 I1: ('131 × 40 · seis níveis',
      'ELEVAÇÃO A · cadeia vertical 141 de vão livre + seis prateleiras de '
      '4 cm espaçadas 35 = 375, o pé-direito · a parede de 131 é 91 + 40 do '
      'canto'),
 I2: ('176 × 40 · seis níveis',
      'ELEVAÇÃO B · mesma cadeia vertical · a parede de 176 é 40 do canto + '
      '136 · ⛔ os dois 40 das duas elevações são peças DIFERENTES, uma em '
      'cada perna do L'),
}

FOLHA = dict(
 aba='DESPENSA',
 sub='Gustavo Raposo · executivo Luiza Pacheco, prancha 31 · doze '
     'prateleiras de parede em MDF Branco Diamante, Linha Trama, Duratex, '
     'com FIXAÇÃO INVISÍVEL · sem armário, sem porta e sem gaveta',
 chapa_txt={BD18: 'Branco Diamante · Linha Trama · Duratex · as doze '
                  'prateleiras · ⭐ 18 mm pelo vão, que passa dos 70 da '
                  'regra em todas elas'},
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a QUANTIDADE é a '
      'célula AMARELA no fim do painel de material, e ela sai ZERO.   '
      '⭐⭐⭐ CADA PRATELEIRA É UM SANDUÍCHE, e é a decisão do Jonathan de '
      '30/10: um QUADRO DE METALON no formato exato da prateleira, revestido '
      'em cima e embaixo por uma peça INTEIRA de 18 mm. Por isso são DOZE '
      'peças de chapa para seis prateleiras em cada elevação, e vinte e '
      'quatro no ambiente.   '
      '⭐⭐ E O METALON FAZ O TRABALHO DE DUAS LINHAS QUE SAÍRAM. Ele é a '
      'ESTRUTURA — quem vence o vão de 1,76 m sem apoio no meio — e é a '
      'FIXAÇÃO INVISÍVEL que a prancha pede nas três chamadas. Saíram, '
      'portanto, os 54 suportes ocultos de R$ 30 e a alma de aço de R$ 50 '
      'por prateleira: as três coisas faziam o mesmo serviço, e pagar as '
      'três seria pagar a fixação três vezes.   '
      '⭐ R$ 250 A UNIDADE, doze unidades, R$ 3.000 — metade do custo do '
      'ambiente. É serralheria, não marcenaria, e a chapa aqui é '
      'REVESTIMENTO: ela fecha o quadro e dá a cara, não sustenta nada.   '
      '⭐ AS DUAS CADEIAS FECHAM: a vertical em 141 + 6 × (35 + 4) = 375, '
      'que é o pé-direito; a horizontal em 91 + 40 + 40 + 136 = 307, que '
      'bate com 131 + 176 das elevações.',
 duvidas=[
  '⚠⚠ O QUADRO DE METALON É A FIXAÇÃO, OU SÓ A ESTRUTURA? Eu entendi as '
  'duas coisas: o quadro se chumba na alvenaria e some entre as duas chapas '
  '— é isso que faz a "fixação invisível" da prancha. ⛔ Se o quadro for '
  'apenas alma, e a fixação na parede for mão-francesa à parte, volta uma '
  'linha de fixação e o ambiente sobe. Confirmar com a serralheria.',
  '⚠ R$ 250 É O MESMO PREÇO PARA 131 E PARA 176? Lancei igual, como o '
  'senhor passou. ⛔ O quadro de 176 tem um terço mais de perímetro e vence '
  'um vão bem maior — se a serralheria cobrar por metro linear, a elevação '
  'B fica mais cara que a A. Vale uma cotação das duas medidas.',
  '⭐ A CHAPA AGORA É REVESTIMENTO, e isso muda o que ela precisa ser. Em '
  '18 mm as doze prateleiras pesam 24 peças e quase cinco chapas. ⚠ Se o '
  'metalon é quem estrutura, 15 mm bastaria para revestir e economizaria '
  'cerca de uma chapa e meia — mas a aresta de 15 + metalon + 15 fica mais '
  'fina e o desenho da prateleira muda. Decisão de aparência, não de '
  'resistência.',
  '⚠ A FITA VAI NAS DUAS PEÇAS, as quatro arestas de cada uma: 102 m de '
  'fita no ambiente. ⛔ Entre as duas chapas sobra a espessura do metalon '
  'aparente na aresta — se ele não for pintado da cor da chapa, aparece '
  'uma linha escura em volta de toda prateleira. Perguntar se a '
  'serralheria entrega pintado.',
  '⚠ A PROFUNDIDADE DE 40 saiu da planta, onde o 40 aparece como a perna '
  'do canto. Se os 40 forem a profundidade da prateleira e não o trecho de '
  'parede, as paredes passam a medir 91 e 136 — e o ambiente perde dois '
  'metros lineares de prateleira. ⭐ Mas aí as duas cadeias não fechariam '
  'em 307, e elas fecham. Fica o registro.'],
 nao_marcenaria=[
  'Revestimento Branco Retificado Acetinado 30 × 60 das paredes',
  '⚠ OS DOZE QUADROS DE METALON são SERRALHERIA, e estão na conta porque '
  'são nossos de entregar — mas não saem da nossa fábrica. R$ 250 cada, '
  'preço cravado pelo Jonathan em 30/10'],
 notas=[
  '⭐⭐ METADE DO CUSTO DESTE AMBIENTE É AÇO, NÃO MADEIRA: R$ 3.000 de '
  'metalon contra menos de R$ 3.000 de chapa, fita e corte. É o único '
  'ambiente da casa em que a marcenaria é o acabamento e não a estrutura.',
  '⭐ UM MATERIAL SÓ E UMA ESPESSURA SÓ na madeira: Branco Diamante Linha '
  'Trama em 18 mm, nas vinte e quatro peças. Uma de 176 × 40 e outra de '
  '131 × 40 saem da mesma tira, e isso faz deste o ambiente que melhor '
  'aproveita chapa.',
  '⚠ PRATELEIRA DE DESPENSA CARREGA PESO DE VERDADE: conserva, garrafa, '
  'saco de arroz. É por isso que o quadro de metalon não é luxo — é o que '
  'permite 1,76 m de vão livre sem apoio no meio e sem flecha.'],

)
