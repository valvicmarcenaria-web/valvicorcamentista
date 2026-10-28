# -*- coding: utf-8 -*-
"""ICA · SALA DE CINEMA E ATELIÊ — levantamento peça por peça  [28/10/2026]

páginas 124 a 140 · DEZ detalhamentos, dez itens, nove folhas de detalhe.
É o maior ambiente do projeto em área (49,21 m²) e em número de peças.

⭐⭐ UMA COR SÓ, do chão ao teto: MDF Nogueira Caiena - Duratex em TODOS os
  dez itens. O branco aparece só onde ninguém vê — prateleira de dentro de
  armário, divisória, fundo. É o ambiente mais simples do projeto em
  material e o mais pesado em quantidade.

⛔⛔ O PÉ-DIREITO É 300 E A CHAPA DÁ 273. Sete dos dez itens têm peça de
  300 de altura: o roupeiro, as duas divisórias, os dois painéis, a porta
  de correr. ⚠ Não é detalhe de corte — é a pergunta de projeto deste
  ambiente, e ela vale para as 24 aletas da Divisória 01 uma por uma.

⭐⭐ AS DUAS DIVISÓRIAS SÃO ALETAS SOLTAS, não ripado sobre painel. A 01
  tem 24 aletas de 7 × 20 em 398; a 02 tem 16 aletas de 3 × 15 em 243. As
  duas vão do chão à laje ("prever fixação na laje"), e as duas resolvem a
  seção de um jeito diferente:
    · 7 × 20  → CAIXÃO: duas faces de 20 mais duas testeiras de 4 (7 menos
                as duas chapas de 15 mm)
    · 3 × 15  → DUAS CHAPAS DE 15 COLADAS: 15 + 15 = 30 mm, que é o 3 cm
                do desenho, exato. Não precisa de caixão.
  ⚠ E aleta solta é ARESTA: cada uma tem quatro arestas verticais de 3 m.
    Só a Divisória 01 pede ~288 m de fita, mais que o ambiente inteiro do
    Banho Hóspedes.

⭐ O "RIPADO" DO DET 03 É RANHURA, não aleta. O DET. RIPADO desenha o corte
  de um painel de 2 cm com frisos de 3 em 1 usinados na face — é o mesmo
  tipo do "fundo ripado" do Living, e NÃO o ripado de duas camadas do Banho
  Gourmet. Por isso aqui não há ripa a contar: há usinagem.

⛔ A BASE METÁLICA DE 3 CM, QUE O PROJETO ESCREVE EM TODAS AS NOVE FOLHAS,
  ENTRA AQUI PELA PRIMEIRA VEZ. [Jonathan, 26/10] fechou que a casa faz o
  rodapé de 3 cm em MDF melamínico, e nos nove ambientes anteriores ela
  ficou de fora por falta dessa decisão estar amarrada. Lancei os 14,3 m
  que os cinco móveis de chão pedem. ⚠ Os outros nove ambientes seguem sem
  ela — é retrabalho pequeno e eu faço quando o senhor mandar.
"""
from base import (P, gaveta, ALT_MAX, CHAPA_C, DOBRADICA, CORREDICA)

NC18, NC15 = 'MDF Nogueira Caiena 18', 'MDF Nogueira Caiena 15'
EST, FUN = 'MDF Branco TX 15', 'MDF Branco TX 6'
PRAT = 'MDF Branco TX 18'

I1  = 'DET 01 Roupeiro'
I2  = 'DET 02 Divisória 01'
I3  = 'DET 03 Painel'
I4  = 'DET 04 Rack'
I5  = 'DET 05 Painel'
I6  = 'DET 06 Divisória 02'
I7  = 'DET 07 Porta de correr'
I8  = 'DET 08 Armário'
I9  = 'DET 09 Painel com nichos'
I10 = 'DET 10 Mesa'

SALACINEMA = [
 # ══ ITEM 01 · ROUPEIRO — 145 × 300 × 62 ══════════════════════════════
 #  VISTA FRONTAL  73 + 73 = 145 · altura 5 + 290 + 5 = 300
 #  VISTA FRONTAL INTERNA  2 + 141 + 2 · 5 + 56 + 2 + 55 + 2 + 55 + 2 +
 #                         55 + 2 + 56 + 5 ≈ 300 · QUATRO prateleiras
 #  VISTA SUPERIOR e LATERAL  profundidade 62
 P('Lateral',                I1, 300, 62, 2, NC15, (1, 0),
   'Aparente · ⛔ 300 de altura contra 273 de peça inteira'),
 P('Tampo e base',           I1, 141, 62, 2, EST, (1, 0),
   'Encostam no teto e na base metálica: não aparecem'),
 P('Fechamento superior e inferior', I1, 141, 5, 2, NC15, (1, 0),
   '⭐ as duas faixas de 5 que a VISTA FRONTAL mostra acima e abaixo das '
   'portas · é o que a prancha chama de fechamento'),
 P('Prateleira',             I1, 141, 62, 4, PRAT, (1, 0),
   'Armário interno com prateleiras em MDF Branco · ⭐ 18 mm porque o vão '
   'de 141 passa dos 70 da regra'),
 P('Fundo',                  I1, 145, 300, 1, FUN, (0, 0),
   'Encaixe em rasgo · ⛔ 300 de altura'),
 P('Porta de giro',          I1, 73, 290, 2, NC18, (2, 2),
   '⛔ 290 de altura, e porta é peça ÚNICA por natureza · puxador cava '
   'duplo na aresta de encontro das duas'),

 # ══ ITEM 02 · DIVISÓRIA 01 — 398 × 300, 24 aletas de 7 × 20 ══════════
 #  VISTA FRONTAL e SUPERIOR  7 + 10 + 7 + 10 ... + 7 = 398
 #                            24 aletas de 7 com vão de 10
 #  ⭐ seção 7 × 20 em MDF = CAIXÃO: duas faces de 20 e duas testeiras de 4
 P('Aleta · face de 20',     I2, 300, 20, 48, NC15, (2, 0),
   '⭐ duas faces por aleta, 24 aletas · as duas arestas verticais de cada '
   'face aparecem, e são 3 m cada · ⛔ 300 de altura'),
 P('Aleta · testeira de 4',  I2, 300, 4, 48, NC15, (0, 0),
   'Frente e costas de cada caixão · 7 menos as duas chapas de 15 mm = 4 · '
   'as arestas ficam dentro do canto, sem fita · ⛔ 300 de altura'),
 P('Base de 3 cm',           I2, 199, 3, 2, NC15, (1, 0),
   '⭐ "não instalar os painéis diretamente no chão, considerar base '
   'metálica de 3 cm" · a casa faz em MDF melamínico [Jonathan, 26/10] · '
   'duas peças de 199 porque 398 não sai de uma chapa'),

 # ══ ITEM 03 · PAINEL — 600 × 300, com vão de 80 × 210 para o rack ════
 #  VISTA FRONTAL  20 + 27 + 24 + 2 + 345 + 2 + 23 + 27 + 130 = 600
 #                 altura 300 · vão do rack 80 de largura × 210 de altura
 #  ⭐ os dois 27 são RIPADO USINADO e os dois 2 são friso: tudo na face do
 #    painel, nada de ripa solta. A divisão em campos cai nos frisos.
 P('Painel · campo esquerdo, faixa alta',  I3, 73, 245, 1, NC18, (1, 1),
   '⭐ a emenda vertical cai no friso de 2 que o desenho já tem; a '
   'horizontal, na altura de 245 em que o ripado termina'),
 P('Painel · campo esquerdo, faixa baixa', I3, 73, 55, 1, NC18, (1, 1)),
 P('Painel · campo central, faixa alta',   I3, 173.5, 245, 2, NC18, (1, 1),
   '⚠ o campo de 345 não cabe em peça inteira e NÃO tem linha de desenho '
   'onde esconder a emenda do meio'),
 P('Painel · campo central, faixa baixa',  I3, 173.5, 55, 2, NC18, (1, 1)),
 P('Painel · verga sobre o vão do rack',   I3, 180, 90, 1, NC18, (1, 1)),
 P('Painel · montante entre o ripado e o vão', I3, 70, 210, 1, NC18, (1, 1)),
 P('Painel · montante à direita do vão',   I3, 30, 210, 1, NC18, (2, 2)),
 P('Base de 3 cm',           I3, 200, 3, 3, NC15, (1, 0),
   'Rodapé de 3 cm em MDF melamínico · três peças de 200 nos 600 do painel'),

 # ══ ITEM 04 · RACK — 470 × 30 × 35 ═══════════════════════════════════
 #  VISTA FRONTAL  59 + 59 + 59 + 117 + 59 + 59 + 59 ≈ 470 · altura 30
 #  VISTA SUPERIOR 177 + 117 + 176 = 470 · profundidade 35
 #  ⭐ SETE gavetas · o módulo central de 117 leva tampo superior de correr
 P('Lateral',                I4, 30, 35, 2, NC15, (1, 1), 'Aparente: é suspenso'),
 P('Tampo e base',           I4, 233, 35, 4, NC15, (1, 0),
   'Duas peças em cada: 466 de corrida não sai de uma chapa'),
 P('Divisória',              I4, 30, 35, 6, EST, (1, 0), 'Sete módulos'),
 P('Fundo',                  I4, 235, 30, 2, FUN, (0, 0), 'Encaixe em rasgo'),
 P('Frente · gaveta',        I4, 59, 30, 6, NC18, (2, 2),
   'Seis gavetas de 59 · fecho toque, sem puxador desenhado'),
 P('Frente · gaveta central', I4, 117, 30, 1, NC18, (2, 2),
   'O módulo de 117, que esconde os aparelhos'),
 P('Tampo de correr',        I4, 117, 35, 1, NC18, (2, 2),
   '⭐ "gaveta com tampo superior de correr, para esconder aparelhos e '
   'fio" · corre sobre o módulo central'),
 *gaveta(I4, 59, 30, 30, 6, 'Gaveta'),
 *gaveta(I4, 117, 30, 30, 1, 'Gaveta central'),

 # ══ ITEM 05 · PAINEL — 40 × 300 ══════════════════════════════════════
 #  VISTA FRONTAL  40 de largura × 300 de altura · peça única
 P('Painel',                 I5, 300, 40, 1, NC18, (2, 2),
   '⛔ 300 de altura, e é um painel estreito e solto: emenda horizontal '
   'num campo de 40 de largura aparece de qualquer ângulo'),
 P('Base de 3 cm',           I5, 40, 3, 1, NC15, (1, 0),
   'Rodapé de 3 cm em MDF melamínico'),

 # ══ ITEM 06 · DIVISÓRIA 02 — 243 × 300, 16 aletas de 3 × 15 ══════════
 #  VISTA FRONTAL e SUPERIOR  3 + 13 + 3 + 13 ... + 3 = 243
 #  ⭐ seção 3 × 15: duas chapas de 15 mm coladas dão 30 mm exatos
 P('Aleta · chapa de 15',    I6, 300, 15, 32, NC15, (1, 0),
   '⭐ duas chapas coladas por aleta, 16 aletas · 15 + 15 = 30 mm, que é o '
   '3 cm do desenho · a aresta da frente aparece e a de trás também, uma '
   'em cada chapa do par · ⛔ 300 de altura'),
 P('Base de 3 cm',           I6, 243, 3, 1, NC15, (1, 0),
   'Rodapé de 3 cm em MDF melamínico'),

 # ══ ITEM 07 · PORTA DE CORRER — 246 × 300, duas folhas de 123 ════════
 #  VISTA FRONTAL  123 + 123 = 246 · altura 300 · esquadria de 7
 #  ⭐ uma folha corre e a outra é fixa · vidro reflecta bronze
 P('Esquadria · montante',   I7, 300, 7, 4, NC18, (1, 1),
   'Dois por folha · ⛔ 300 de altura num montante de 7 de largura'),
 P('Esquadria · travessa',   I7, 109, 7, 4, NC18, (1, 1),
   'Topo e base de cada folha · 123 menos os dois montantes de 7'),

 # ══ ITEM 08 · ARMÁRIO — 247 × 75 × 40 ════════════════════════════════
 #  VISTA FRONTAL  2 + 61 + 61 + 61 + 61 + 2 ≈ 247 · altura 2 + 66 + 5 + 2
 #  VISTA FRONTAL INTERNA  2 + 121 + 2 + 121 + 2 · 2 + 32 + 2 + 32 + 5 + 2
 #  VISTA SUPERIOR  profundidade 40
 P('Lateral',                I8, 75, 40, 2, NC15, (1, 1), 'Aparente: é suspenso'),
 P('Tampo e base',           I8, 243, 40, 2, NC15, (1, 0), 'Aparente'),
 P('Divisória',              I8, 71, 40, 1, EST, (1, 0), 'Dois vãos de 121'),
 P('Prateleira',             I8, 121, 40, 2, PRAT, (1, 0),
   'Armário interno com prateleiras em MDF Branco · ⭐ 18 mm porque o vão '
   'de 121 passa dos 70 da regra'),
 P('Fundo',                  I8, 247, 75, 1, FUN, (0, 0), 'Encaixe em rasgo'),
 P('Fechamento inferior',    I8, 243, 5, 1, NC15, (1, 0),
   'A faixa de 5 que a VISTA FRONTAL mostra abaixo das portas'),
 P('Porta de giro',          I8, 61, 66, 4, NC18, (2, 2),
   'Quatro portas de 61 × 66 · puxador cava'),

 # ══ ITEM 09 · PAINEL COM NICHOS — 247 × 214 × 25 ═════════════════════
 #  VISTA FRONTAL  2 + 121 + 2 + 121 + 2 ≈ 247
 #                 altura 84 do bloco de nichos + 48 + 2 de prateleira +
 #                 80 de painel com furos = 214
 #  VISTA LATERAL e SUPERIOR  profundidade 25
 P('Painel de fundo · atrás dos nichos', I9, 247, 84, 1, NC18, (2, 0),
   '⭐ a emenda do painel de fundo cai atrás da base do bloco de nichos, '
   'que é onde ninguém a vê'),
 P('Painel de fundo · faixa lisa',       I9, 247, 50, 1, NC18, (2, 0),
   'Os 48 abertos mais os 2 da prateleira'),
 P('Painel com furos',       I9, 247, 80, 1, NC18, (2, 2),
   '⚠ "painel com furos" · a furação é usinagem e NÃO tem linha na Base: '
   'está aqui a chapa, não o serviço'),
 P('Nicho · lateral',        I9, 84, 25, 2, NC18, (1, 1)),
 P('Nicho · tampo e base',   I9, 243, 25, 2, NC18, (1, 1)),
 P('Nicho · prateleira',     I9, 243, 25, 1, NC18, (1, 1),
   'A divisão horizontal dos quatro nichos de 121 × 39'),
 P('Nicho · divisória',      I9, 80, 25, 1, NC18, (1, 1), 'A divisão vertical'),
 P('Prateleira solta',       I9, 80, 25, 2, NC18, (2, 2),
   'As duas de 80 que a VISTA FRONTAL mostra sob o bloco de nichos'),

 # ══ ITEM 10 · MESA — 247 × 60 × 10 ═══════════════════════════════════
 #  VISTA FRONTAL  62 + 62 + 62 + 62 ≈ 247 · altura 10
 #  VISTA SUPERIOR 247 × 60 · ⭐ é uma lâmina suspensa com quatro gavetas
 P('Tampo',                  I10, 247, 60, 1, NC18, (2, 2), 'Aparente'),
 P('Base',                   I10, 243, 60, 1, NC15, (1, 0),
   'Aparente por baixo: é suspensa'),
 P('Lateral',                I10, 10, 60, 2, NC15, (1, 1)),
 P('Divisória',              I10, 10, 60, 3, EST, (1, 0), 'Quatro vãos de 62'),
 P('Fundo',                  I10, 247, 10, 1, FUN, (0, 0), 'Encaixe em rasgo'),
 P('Frente · gaveta',        I10, 62, 10, 4, NC18, (2, 2),
   'Quatro gavetas de 62 · puxador passante'),
 *gaveta(I10, 62, 55, 10, 4, 'Gaveta'),
]

# ── ferragem, declarada item a item ─────────────────────────────────────
GAVETAS = [(I4, 'Rack · seis gavetas de 59 e uma de 117', 7, 300),
           (I10, 'Mesa · quatro gavetas de 62', 4, 550)]
PORTAS  = [(I1, 'Roupeiro · duas portas de giro de 290 de altura', 2, 5,
            DOBRADICA),
           (I8, 'Armário · quatro portas de giro de 66 de altura', 4, 2,
            DOBRADICA)]
BASCULAS= []
#  ⭐ a cava corre a aresta inteira da frente, e no roupeiro ela é VERTICAL:
#    o DET. PUXADOR CAVA DUPLO mostra o perfil nas duas folhas que se
#    encontram. No armário ela é horizontal, uma por porta.
CAVA    = [(I1, 'Puxador cava duplo · as duas portas, na aresta de encontro',
            2, 290),
           (I8, 'Puxador cava nas quatro portas de giro', 4, 61)]
PUXADORES= []
MOLDURA = []
LED     = [(I9, 'Sob o bloco de nichos, de ponta a ponta', 2.47)]
CABIDEIROS = []
SARRAFOS= []
SUPORTES= []
ALMAS   = []
VIDRO   = [(I7, 'Vidro reflecta bronze · as duas folhas', 2, 109, 286)]
SERRALHERIA = []
# ⛔ duas ferragens que a Base não tem: o trilho da porta de correr e o
#   pulsador do fecho toque do rack. O pulsador tem preço; o trilho, não.
OUTRAS  = [(I4, 'Pulsador', 'Sete gavetas do rack · a prancha escreve '
            '"fecho toque" e não desenha puxador nenhum', 7, 'un', 'Pulsador'),
           (I7, 'Trilho de porta de correr', 'Uma folha corre e a outra é '
            'fixa · folha de 123 × 300 em MDF com vidro pesa, e pede trilho '
            'embutido · ⛔ sem preço na Base', 1, 'jogo',
            'Trilho de porta de correr'),
           (I10, 'Puxador passante', 'Perfil SP7000 nas quatro frentes de '
            '62 da mesa', 2.48, 'm', 'Puxador passante')]

CABECA = {
 I1: ('145 × 300 × 62',
      'VISTA FRONTAL 73 + 73 = 145 · altura 5 de fechamento + 290 de porta '
      '+ 5 de fechamento = 300 · VISTA FRONTAL INTERNA quatro prateleiras '
      'em cinco vãos de 56, 55, 55, 55 e 56 · profundidade 62'),
 I2: ('398 × 300 × 20',
      'VISTA FRONTAL e SUPERIOR 7 + 10 repetidos: VINTE E QUATRO aletas de '
      '7 com vão de 10 em 398 · ⭐ seção 7 × 20 resolvida em caixão, duas '
      'faces de 20 e duas testeiras de 4 · fixação na laje'),
 I3: ('600 × 300',
      'VISTA FRONTAL 20 + 27 + 24 + 2 + 345 + 2 + 23 + 27 + 130 = 600 · '
      'altura 300 · vão de 80 × 210 para o rack · ⭐ os dois 27 são ripado '
      'USINADO e os dois 2 são friso: é ranhura na face, não ripa solta'),
 I4: ('470 × 30 × 35',
      'VISTA FRONTAL 59 + 59 + 59 + 117 + 59 + 59 + 59 ≈ 470 · altura 30 · '
      'VISTA SUPERIOR 177 + 117 + 176 · profundidade 35 · SETE gavetas, e '
      'a central de 117 leva tampo superior de correr'),
 I5: ('40 × 300',
      'VISTA FRONTAL 40 de largura × 300 de altura · peça única, solta'),
 I6: ('243 × 300 × 15',
      'VISTA FRONTAL e SUPERIOR 3 + 13 repetidos: DEZESSEIS aletas de 3 '
      'com vão de 13 em 243 · ⭐ seção 3 × 15 = duas chapas de 15 mm '
      'coladas, 30 mm exatos · fixação na laje'),
 I7: ('246 × 300',
      'VISTA FRONTAL 123 + 123 = 246 · altura 300 · esquadria de 7 em MDF '
      'e vidro reflecta bronze · uma folha corre, a outra é fixa'),
 I8: ('247 × 75 × 40',
      'VISTA FRONTAL 2 + 61 + 61 + 61 + 61 + 2 ≈ 247 · altura 2 + 66 de '
      'porta + 5 de fechamento + 2 = 75 · VISTA FRONTAL INTERNA dois vãos '
      'de 121 com uma prateleira cada · profundidade 40 · suspenso'),
 I9: ('247 × 214 × 25',
      'VISTA FRONTAL 2 + 121 + 2 + 121 + 2 ≈ 247 · altura 84 do bloco de '
      'nichos + 48 + 2 de prateleira + 80 de painel com furos = 214 · '
      'profundidade 25 · quatro nichos de 121 × 39 com LED embaixo'),
 I10: ('247 × 60 × 10',
       'VISTA FRONTAL 62 + 62 + 62 + 62 ≈ 247 · altura 10 · VISTA SUPERIOR '
       '247 × 60 · uma lâmina suspensa de 10 com quatro gavetas'),
}

FOLHA = dict(
 aba='SALA DE CINEMA E ATELIÊ',
 sub='Jéssica e Michell · Projeto ICA · páginas 124 a 140 · DEZ itens, o '
     'maior ambiente do projeto · ⭐ uma cor aparente só, Nogueira Caiena '
     'Duratex, nos dez itens · caixaria em Branco TX 15 · ⛔ pé-direito de '
     f'300 contra peça inteira de {ALT_MAX:g}, que é a chapa de {CHAPA_C:g} '
     'menos o acerto de corte',
 chapa_txt={NC18: 'Nogueira Caiena · Duratex · frentes, painéis, nichos e tampos',
            NC15: 'Nogueira Caiena · Duratex · laterais, aletas das duas '
                  'divisórias e o rodapé de 3 cm',
            EST:  'Estrutura e caixaria · o padrão da Base para caixaria',
            PRAT: '⭐ 18 mm por regra: prateleira de vão acima de 70 cm',
            FUN:  'Fundos · encaixe em rasgo, sem fita'},
 nota='⛔ O FRETE ESTÁ ZERADO DE PROPÓSITO: as linhas de frete da Base não '
      'têm preço ainda. Preencher lá e elas aparecem aqui sozinhas.   '
      '⛔⛔ O PÉ-DIREITO É 300 E A CHAPA DÁ 273. Sete dos dez itens têm '
      'peça de 300: o roupeiro, as duas divisórias, os dois painéis e a '
      'porta de correr. Todas aparecem marcadas na auditoria e nenhuma tem '
      'onde esconder a emenda — é decisão de projeto, não de corte.   '
      '⭐⭐ AS DUAS DIVISÓRIAS SÃO ALETAS SOLTAS: 24 de 7 × 20 na 01 e 16 '
      'de 3 × 15 na 02. Aleta é ARESTA, e só a Divisória 01 pede uns 288 m '
      'de fita — mais que o Banho Hóspedes inteiro.   ⭐ A BASE METÁLICA '
      'DE 3 CM entra aqui pela primeira vez no projeto, em MDF melamínico '
      'como o senhor fechou em 26/10: são 14,3 m nos cinco móveis de chão.',
 duvidas=[
  'AS 24 ALETAS DA DIVISÓRIA 01 TÊM 7 × 20 DE SEÇÃO e 300 de altura. ⭐ '
  'Resolvi em CAIXÃO de MDF: duas faces de 20 mais duas testeiras de 4. ⚠ '
  'Isso dá 1,4 m² de chapa POR ALETA e nenhuma peça cabe inteira — são 24 '
  'emendas horizontais a 273 do chão, todas à vista. ⛔ As alternativas '
  'mudam o preço de verdade: miolo de pinus revestido sai mais leve, mais '
  'barato e sem emenda de chapa; chapa de 300 sob encomenda resolve a '
  'emenda e encarece. É a maior pergunta deste ambiente.',
  'O PÉ-DIREITO É 300 E A PEÇA INTEIRA DÁ 273. Além das aletas, têm 300 de '
  'altura: as laterais e o fundo do roupeiro, a porta de 290, o painel de '
  '40 do DET 05, os montantes de 7 da porta de correr e as 16 aletas da '
  'Divisória 02. ⚠ Em alguns dá para esconder — o fundo do roupeiro fica '
  'atrás das prateleiras. Em outros não: um montante de 7 de largura com '
  'emenda a 273 do chão é o primeiro lugar onde o olho vai. ⛔ Confirmar '
  'se a casa compra chapa de 300 para este ambiente.',
  'O "RIPADO" DO DET 03 É USINAGEM, não ripa. O DET. RIPADO desenha o '
  'corte de um painel de 2 cm com frisos de 3 em 1 na face. ⚠ Lancei a '
  'chapa do painel e NÃO lancei o serviço: a Base traz "Painel ripado · R$ '
  '180/m²" e não diz se esse valor já inclui a chapa. São 1,5 m² de banda '
  'ripada aqui. ⛔ É a mesma pergunta do Banho Gourmet, e ela volta em '
  'todo ripado do projeto.',
  'O "PAINEL COM FUROS" DO DET 09 é um pegboard de 247 × 80 em Nogueira '
  'Caiena. ⚠ Lancei a chapa; a FURAÇÃO não tem linha na Base e não entrou. '
  'São uns 1.500 furos numa chapa de 18 mm — é hora de CNC, não de '
  'furadeira. Pedir preço de usinagem por m² ao terceirizado.',
  'O TRILHO DA PORTA DE CORRER DO DET 07 não existe na Base e sai ZERO. ⚠ '
  'A folha tem 123 × 300 em MDF de 18 mm com vidro reflecta: passa fácil '
  'de 60 kg. Isso é trilho embutido de carga, não corrediça — costuma '
  'custar de R$ 400 a R$ 1.200 o jogo. ⛔ Até existir, o custo deste item '
  'é um PISO.',
  'O VIDRO REFLECTA BRONZE da porta de correr segue SEM PREÇO na Base, '
  'como o reflecta champagne do Living. ⚠ São 6,2 m² em duas folhas de '
  '109 × 286 — e vidro de 2,86 m de altura é peça especial, não é '
  'prateleira de cristaleira. ⛔ Sai ZERO e denuncia.',
  'O RACK TEM "FECHO TOQUE" NAS SETE GAVETAS e nenhum puxador desenhado. '
  '⭐ Orcei PULSADOR, R$ 100 cada, R$ 700 pelos sete. ⚠ Não é o caso das '
  'básculas da Cozinha, onde o senhor tirou o pulsador porque a frente '
  'abre pelo puxador slim: aqui não há slim nenhum, e gaveta de fecho '
  'toque abre por pulsador ou por corrediça com push-to-open. Se a '
  'corrediça já vier com push, os R$ 700 saem da conta.',
  'A BASE METÁLICA DE 3 CM ENTROU AQUI, E SÓ AQUI. A prancha escreve "não '
  'instalar os painéis diretamente no chão, considerar base metálica de 3 '
  'cm" nas NOVE folhas de detalhe, e o senhor fechou em 26/10 que a casa '
  'faz esse rodapé em MDF melamínico. Lancei os 14,3 m dos cinco móveis de '
  'chão. ⚠ Os outros nove ambientes do projeto seguem sem ela — são uns 25 '
  'm somados, pouco mais de meia chapa. Eu volto e lanço quando o senhor '
  'mandar.',
  'O CAMPO CENTRAL DO PAINEL DO DET 03 TEM 345 DE LARGURA e não cabe em '
  'peça inteira. ⚠ Os outros campos eu dividi nos frisos de 2 cm que o '
  'próprio desenho tem, e a emenda some. Esse não tem linha nenhuma: '
  'dividi ao meio, 173,5 + 173,5, e a emenda fica no centro do campo. ⛔ '
  'Se o desenho puder ganhar um terceiro friso, ela some também.',
  'A MESA DO DET 10 TEM 247 DE VÃO COM 10 DE ALTURA e é suspensa. ⚠ Uma '
  'lâmina de 2,47 m apoiada só nas pontas, com quatro gavetas dentro, '
  'empena. A prancha não desenha pé, nem mão-francesa, nem fixação. É a '
  'mesma pergunta da mesa do Home Office e da mesa da Suíte Hóspedes — '
  'três mesas do projeto, a mesma lacuna.',
  'O CORRIMÃO DE FERRO FORJADO "com apoio em madeira" da planta é '
  'serralheria, não marcenaria. ⚠ Mas o "apoio em madeira" pode ser nosso. '
  'A prancha não detalha nem cota. Confirmar de quem é.'],
 nao_marcenaria=[
  'Vidro reflecta bronze das duas folhas da porta de correr — vidraceiro '
  '(a esquadria de MDF é nossa)',
  'Corrimão de ferro forjado clássico com apoio em madeira — serralheria',
  'TV 85", torre de tomadas do rack e toda a parte elétrica',
  'Sofá modular, mesa de centro Paola, cadeira Cover, abajur de chão e tapete',
  'Cortina em linho branco com blackout, pedra Atacama Branca e pintura'],
 notas=[
  '⭐⭐ UMA COR SÓ NO AMBIENTE INTEIRO: Nogueira Caiena Duratex nos dez '
  'itens. O branco só aparece onde ninguém vê — prateleira de dentro de '
  'armário, divisória e fundo. Depois de ambientes com quatro padrões '
  'aparentes, este compra chapa de uma cor e arredonda uma vez.',
  '⭐⭐ ALETA É ARESTA, e é onde o dinheiro deste ambiente se esconde. Cada '
  'aleta da Divisória 01 tem quatro arestas verticais de 3 m: são 12 m de '
  'fita por aleta e 288 m nas 24. A Divisória 02 resolve melhor — as duas '
  'chapas coladas deixam só duas arestas por aleta, 96 m nas 16.',
  '⭐ AS DUAS DIVISÓRIAS RESOLVEM A SEÇÃO DE JEITOS DIFERENTES, e não é '
  'capricho: 3 cm é exatamente duas chapas de 15 mm coladas, então a '
  'Divisória 02 não precisa de caixão. 7 cm não é múltiplo de nada, então '
  'a 01 precisa.',
  '⭐ O RIPADO DESTE AMBIENTE NÃO É O DO BANHO GOURMET. Lá o DET. RIPADO '
  'em 1/10 mostrava ripa solta sobre painel de base, em duas camadas. Aqui '
  'o DET. RIPADO mostra friso usinado na face de um painel de 2 cm — é '
  'ranhura, como o fundo ripado do Living. Mesma palavra, outro serviço.',
  '⚠ A PORTA DE CORRER TEM 300 DE ALTURA E ESQUADRIA DE 7 DE LARGURA. Um '
  'montante de 7 × 300 em MDF de 18 mm é esbelto para carregar 3 m² de '
  'vidro: na prática pede alma de aço ou perfil de alumínio embutido. A '
  'prancha não desenha nenhum dos dois e eu não lancei — está na dúvida 05 '
  'junto com o trilho.'],
)
