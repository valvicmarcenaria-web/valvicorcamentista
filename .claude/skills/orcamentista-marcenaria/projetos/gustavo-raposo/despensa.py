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
      '⭐⭐ O AMBIENTE MAIS SIMPLES DA CASA É O QUE MAIS ENGANA. Não há '
      'armário, porta nem gaveta: são doze prateleiras de parede em L. O '
      'que elas custam não é chapa — é a FIXAÇÃO INVISÍVEL que a prancha '
      'pede e a ALMA DE AÇO que o vão exige. Doze prateleiras de 131 e 176 '
      'sem apoio no meio flecham sozinhas, e prateleira de despensa carrega '
      'peso de verdade.   ⭐ AS DUAS CADEIAS FECHAM: a vertical em 141 + 6 × '
      '(35 + 4) = 375, que é o pé-direito; a horizontal em 91 + 40 + 40 + '
      '136 = 307, que bate com 131 + 176 das elevações.',
 duvidas=[
  '⚠⚠ O QUE É "FIXAÇÃO INVISÍVEL" AQUI? Pode ser mão-francesa oculta '
  'parafusada na alvenaria, cavilha de aço embutida, ou perfil contínuo. '
  'Lancei o SUPORTE OCULTO da Base — R$ 30, de 40 em 40 cm —, que é a linha '
  'legada que o Jonathan tirou de prateleira de ARMÁRIO em 28/10 mas que '
  'aqui é exatamente o que a prancha pede. ⛔ É o maior item deste ambiente: '
  '54 suportes. Se for perfil contínuo ou mão-francesa de chapa, o número '
  'muda inteiro.',
  'A ALMA DE AÇO NÃO ESTÁ LANÇADA À MÃO porque o motor a conta sozinho: '
  'toda prateleira de vão acima de 1,20 m leva barra, e as doze passam. ⚠ '
  'Mas prateleira PENDURADA é caso diferente de prateleira apoiada em '
  'lateral: se a fixação invisível já for um perfil estrutural, a alma pode '
  'ser redundante. Confirmar com a fábrica.',
  '⚠ A PROFUNDIDADE DE 40 saiu da planta, onde o 40 aparece como a perna do '
  'canto. Se os 40 forem a profundidade da prateleira e não o trecho de '
  'parede, as paredes passam a medir 91 e 136 — e o ambiente perde dois '
  'metros lineares de prateleira. ⭐ Mas aí as duas cadeias não fechariam '
  'em 307, e elas fecham. Fica o registro.'],
 nao_marcenaria=[
  'Revestimento Branco Retificado Acetinado 30 × 60 das paredes'],
 notas=[
  '⭐ UM MATERIAL SÓ E UMA ESPESSURA SÓ: Branco Diamante Linha Trama em '
  '18 mm, nas doze peças. É o ambiente que menos pesa no corte e o que '
  'melhor aproveita chapa — uma prateleira de 176 × 40 e outra de 131 × 40 '
  'saem da mesma tira.',
  '⚠ PRATELEIRA DE DESPENSA CARREGA PESO DE VERDADE: conserva, garrafa, '
  'saco de arroz. É por isso que o vão manda aqui mais do que em qualquer '
  'outro ambiente da casa, e por isso a alma de aço não é preciosismo.'],
)
