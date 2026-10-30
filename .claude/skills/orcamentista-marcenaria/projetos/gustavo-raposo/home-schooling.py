# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO · ANEXO HOMESCHOOLING — peça por peça  [30/10/2026]

pranchas 72 a 75 · planta de layout, elevação A, elevação B em vista
externa e vista interna, mais o detalhe 11 do perfil de LED embutido.

⭐⭐ É O ÚNICO AMBIENTE DA CASA EM MDF CINZA FÓSSIL, Linha VELLUTO — a
  única linha de toque aveludado do projeto, e a que mais marca dedo.
  ⛔⛔ E ESTE AMBIENTE QUASE SAIU ZERO. A lista de chaves do código
    declarava `MDF Cinza Fóssil 15` e `6`, que a Base NÃO TINHA: só o 18
    estava lá. O levantamento passaria no auditor e a aba leria vazio.
    ⭐ As duas linhas entraram na Base hoje, antes de este arquivo existir.

⭐ TRÊS ITENS, e dois deles empilhados na mesma parede:
     ELEVAÇÃO A · nicho azul de 116 sobre armário cinza de 90 = 210
     ELEVAÇÃO B · armário cinza de 210, quatro portas de giro
  ⭐ Os dois chegam a 210 e param: sobram 50 de parede até o forro de 260.
    ⛔ Pé-direito de ANEXO, 260 e não 275.

⭐ O NICHO É AZUL SECRETO DENTRO DE UM AMBIENTE CINZA, e é de propósito: a
  prancha pede perfil de LED com abas em cada uma das três prateleiras, e o
  detalhe 11 escreve "Marcenaria". O azul aceso é o ponto de cor da sala.

⛔⛔ AS OITO PRATELEIRAS DA ELEVAÇÃO B TÊM 120,75 DE VÃO. Passam por 75
  centímetros do limite de 120 da casa — e por isso TODAS pedem alma de
  aço. ⭐ Uma divisória a mais no meio economizaria oito barras; sem ela,
  são R$ 400 de aço num armário de estante.

⛔ FORA: a mesa e a cadeira · a segunda mesa · o sofá-cama · o tapete
  orgânico de 170 × 235 · as duas janelas · a elétrica.
"""
from base import P, gaveta, DOBRADICA, CORREDICA

CF15, CF18 = 'MDF Cinza Fóssil 15', 'MDF Cinza Fóssil 18'
AS15, AS18 = 'MDF Azul Secreto 15', 'MDF Azul Secreto 18'
BR18, BR15, BR6 = 'MDF branco 18', 'MDF branco 15', 'MDF Branco TX 6'

I1 = 'ELEVAÇÃO A Nicho em Azul Secreto'
I2 = 'ELEVAÇÃO A Armário inferior de 210'
I3 = 'ELEVAÇÃO B Armário de 246'

LA, LB = 210.0, 246.0
CA = (LA - 7.5)/4           # 50,6 · quatro colunas na elevação A
CB = (LB - 4.5)/2           # 120,75 · duas colunas na elevação B
PROF_N, PROF = 24.0, 40.0   # o nicho é raso; os armários, não

HOME_SCHOOLING = [
 # ══ ITEM 01 · NICHO AZUL — 210 × 116 × 24 ═════════════════════════════
 P('Lateral do nicho', I1, 116, PROF_N, 2, AS18, (1, 0),
   '⭐ Azul Secreto dentro de um ambiente Cinza Fóssil — é o ponto de cor '
   'da sala'),
 P('Tampo e base do nicho', I1, 202, PROF_N, 2, AS18, (1, 0),
   '⛔ 202 de largura: cabe deitado nos 275 da chapa, mas é peça longa e '
   'rasa, das que empenam na estocagem'),
 P('Prateleira do nicho', I1, 202, PROF_N, 2, AS18, (1, 0),
   '⭐ Duas, partindo os 112 em três vãos de 36 · ⛔ 202 de vão passa MUITO '
   'dos 120: cada uma pede alma de aço'),
 P('Fundo do nicho', I1, 116, LA, 1, AS15, (0, 0),
   '⭐ Em 15 mm e não em 6: o fundo do nicho fica À VISTA, é ele que dá a '
   'cor azul de dentro · ⛔ sem fita'),

 # ══ ITEM 02 · ARMÁRIO INFERIOR — 210 × 90 × 40 ════════════════════════
 P('Lateral e divisória vertical', I2, 78, PROF, 5, CF15, (1, 0),
   '⭐ Duas laterais e três divisórias · QUATRO colunas de 50,6: duas com '
   'porta de giro e duas com três gavetas cada'),
 P('Tampo e base', I2, CA, PROF, 8, CF15, (1, 0)),
 P('Rodapé', I2, LA, 10, 1, CF15, (1, 0)),
 P('Prateleira', I2, CA, 38, 2, BR18, (1, 0),
   'Uma em cada coluna de giro · as "Proj. prateleira" da elevação A'),
 P('Frente de gaveta rasa', I2, CA, 19.5, 4, CF15, (2, 2),
   '⭐ Duas em cada coluna de gaveta · puxador tipo CAVA QUADRADA de 5 × 5'),
 P('Frente de gavetão', I2, CA, 39, 2, CF15, (2, 2),
   '⭐ Uma em cada coluna de gaveta, embaixo · CAVA QUADRADA de 5 × 5'),
 *gaveta(I2, CA, 35, 17.5, 4, 'Caixa de gaveta'),
 *gaveta(I2, CA, 35, 37, 2, 'Caixa de gavetão'),
 P('Fundo', I2, LA, 80, 1, BR6, (0, 0), '⛔ sem fita'),
 P('Frente · porta de giro', I2, CA, 78, 2, CF15, (2, 2),
   'Duas folhas de 50,6 × 78 · CAVA QUADRADA de 5 × 5'),

 # ══ ITEM 03 · ARMÁRIO DA ELEVAÇÃO B — 246 × 210 × 40 ══════════════════
 P('Lateral e divisória vertical', I3, 200, PROF, 3, CF15, (1, 0),
   '⭐ Duas laterais e UMA divisória · DUAS colunas de 120,75'),
 P('Tampo e base', I3, CB, PROF, 4, CF15, (1, 0)),
 P('Rodapé', I3, LB, 10, 1, CF15, (1, 0)),
 P('Prateleira', I3, CB, 38, 8, BR18, (1, 0),
   '⛔ Vão de 120,75 — passa dos 120 da regra por 75 milímetros, e por '
   'isso TODAS as oito pedem alma de aço · ⚠ uma divisória a mais no meio '
   'resolveria por menos'),
 P('Fundo', I3, 200, 123, 2, BR6, (0, 0),
   '⛔ 246 de largura não cabe nos 185 da chapa: sai em DUAS de 123 · a '
   'emenda cai na divisória · sem fita'),
 P('Frente · porta de giro', I3, 61.5, 200, 4, CF15, (2, 2),
   '⭐ Quatro folhas de 61,5 × 200, duas por coluna · TRÊS dobradiças '
   'cada: 2 m de folha não se segura em duas · CAVA QUADRADA de 5 × 5'),
]

GAVETAS = [
 (I2, 'Seis gavetas em duas colunas — quatro rasas de 19,5 e dois '
      'gavetões de 39 · ⭐ a prancha pede corrediça INVISÍVEL, que já é a '
      'Hettich oculta', 6, CORREDICA),
]
PORTAS = [
 (I2, 'Duas folhas de giro de 50,6 × 78', 2, 2, DOBRADICA),
 (I3, 'Quatro folhas de giro de 61,5 × 200 · ⭐ TRÊS dobradiças por folha',
  4, 3, DOBRADICA),
]
CAVA = [
 (I2, 'Cava QUADRADA de 5 × 5 nas oito frentes — seis gavetas e duas '
      'folhas', 8, 5),
 (I3, 'Cava QUADRADA de 5 × 5 nas quatro folhas', 4, 5),
]
LED = [
 (I1, 'TRÊS perfis de 2,02, um sob cada prateleira e um sob o tampo do '
      'nicho · ⭐ o detalhe 11 escreve "Marcenaria": o perfil é nosso',
  6.06),
]
BASCULAS = PUXADORES = MOLDURA = CABIDEIROS = ALMAS = []
VIDRO = SERRALHERIA = []
OUTRAS = [
 (I1, 'Perfil de proteção de piso',
  '⛔ NÃO ENTRA: o nicho começa a 92 do chão, sobre o armário inferior',
  0, 'm', 'Perfil de proteção de piso'),
 (I2, 'Perfil de proteção de piso', 'O rodapé de 210 toca o chão', 2.10,
  'm', 'Perfil de proteção de piso'),
 (I3, 'Perfil de proteção de piso', 'O rodapé de 246 toca o chão', 2.46,
  'm', 'Perfil de proteção de piso'),
]

CABECA = {
 I1: ('210 × 116 × 24',
      'ELEVAÇÃO A · nicho RASO de 24, em MDF Azul Secreto, sobre o armário '
      'cinza · três vãos de 36 entre duas prateleiras, com perfil de LED '
      'embutido em cada um · ⭐ o fundo é de 15 mm e não de 6: ele fica à '
      'vista e é o que dá a cor'),
 I2: ('210 × 90 × 40',
      'ELEVAÇÃO A · armário inferior em MDF Cinza Fóssil, Linha Velluto · '
      'QUATRO colunas de 50,6: duas com porta de giro e prateleira, duas '
      'com três gavetas cada · rodapé de 10'),
 I3: ('246 × 210 × 40',
      'ELEVAÇÃO B · armário de estante com quatro portas de giro de 200 · '
      'DUAS colunas de 120,75 com quatro prateleiras cada · ⛔ 120,75 de '
      'vão: as OITO pedem alma de aço'),
}

FOLHA = dict(
 aba='HOMESCHOOLING',
 sub='Gustavo Raposo · executivo Luiza Pacheco, pranchas 72 a 75 · ⭐ o '
     'único ambiente em MDF Cinza Fóssil, Linha Velluto, com um nicho '
     'azul aceso no meio',
 chapa_txt={
  CF15: 'Cinza Fóssil · Linha VELLUTO · Duratex · ⭐ toque aveludado, a '
        'única linha assim do projeto · ⛔ e a que mais marca dedo: as '
        'frentes deste ambiente pedem cuidado no transporte e na montagem '
        '· os dois armários inteiros saem dela',
  AS18: 'Azul Secreto · Linha Essencial · Duratex · a estrutura do nicho',
  AS15: 'Azul Secreto · Linha Essencial · Duratex · o fundo do nicho, que '
        'fica À VISTA',
  BR18: 'Branco · as dez prateleiras internas dos dois armários cinza',
  BR6:  'Branco TX · os fundos dos dois armários',
  'MDF Branco TX 15': 'Branco TX · a caixaria das seis gavetas',
 },
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a QUANTIDADE é '
      'a célula AMARELA no fim do painel de material, e ela sai ZERO.   '
      '⛔⛔ ESTE AMBIENTE QUASE SAIU ZERO. A lista de chaves do código '
      'declarava Cinza Fóssil 15 e 6, que a Base não tinha — só o 18 '
      'estava lá. O levantamento passaria no auditor e a aba leria vazio, '
      'exatamente como a laca da cozinha. As duas linhas entraram na Base '
      'hoje, antes deste arquivo existir.   '
      '⭐ A LINHA VELLUTO É TOQUE AVELUDADO e marca dedo. É decisão de '
      'projeto e é linda — mas vale avisar o cliente, porque numa sala de '
      'estudo com criança a frente é tocada o dia inteiro.   '
      '⛔ AS OITO PRATELEIRAS DE 120,75 passam do limite de 120 por 75 '
      'milímetros e levam alma de aço. São R$ 400 de aço que uma '
      'divisória a mais evitaria.',
 duvidas=[
  '⚠ AS OITO ALMAS DE AÇO DA ELEVAÇÃO B. O vão de 120,75 passa do limite '
  'da casa por 7,5 mm — é o caso mais justo do projeto inteiro. ⭐ Duas '
  'saídas: aceitar as oito barras (R$ 400) ou pôr uma divisória central, '
  'que custa cerca de R$ 160 em chapa e derruba o vão para 59. ⛔ A '
  'segunda é mais barata E mais firme; a primeira mantém a estante limpa, '
  'que foi o que a arquiteta desenhou. É decisão sua.',
  '⚠ A PROFUNDIDADE DE 40 nos dois armários não está cotada em prancha '
  'nenhuma. Adotei 40, que é profundidade de estante e de armário de sala '
  'de estudo. ⛔ Se for 60, são cerca de 4 m² de chapa a mais.',
  '⚠ O NICHO TEM 24 DE PROFUNDIDADE, cotado na elevação A, contra 40 dos '
  'armários. ⭐ Ele é mais raso de propósito: fica acima do armário e à '
  'altura dos olhos.',
  '⚠ AS DUAS PRATELEIRAS DO NICHO têm 202 de vão e levam alma de aço '
  'também. ⛔ Em 24 cm de profundidade, uma prateleira de 2 m é frágil '
  'mesmo com barra: vale conferir se a arquiteta não aceita uma divisória '
  'no meio do nicho.',
  '⚠ A LARGURA DAS COLUNAS saiu dos totais cotados: 50,6 na elevação A e '
  '120,75 na B. A prancha cota os 210 e os 246 e não as colunas.',
 ],
 nao_marcenaria=[
  '⛔ A MESA E A CADEIRA, a segunda MESA e o SOFÁ-CAMA, todos "a ser '
  'adquirido, modelo a definir".',
  '⛔ O TAPETE ORGÂNICO de 170 × 235.',
  '⛔ AS DUAS JANELAS: a de 267 da elevação A e a de 431 da elevação B.',
  '⛔ A ELÉTRICA: as tomadas duplas e o ponto para rede.',
 ],
 notas=[
  '⭐ SÃO 4,56 M DE ARMÁRIO em duas paredes de uma sala de estudo. O '
  'ambiente é simples de fabricar — sem cabideiro, sem correr, sem '
  'espelho — e o que o encarece é a quantidade de frente: quatorze.',
  '⭐ O NICHO AZUL É O ÚNICO LUGAR DA CASA ONDE O AZUL SECRETO ENCOSTA EM '
  'OUTRA COR. No banheiro da suíte 01 ele está sozinho. ⛔ Aqui as duas '
  'compras acontecem no mesmo ambiente: Cinza Fóssil e Azul Secreto são '
  'dois arredondamentos de chapa numa sala só.',
  '⭐ O PERFIL DE LED DO NICHO É MARCENARIA, por escrito no detalhe 11 — '
  'como o da cabeceira da Suíte 01 e o do armário do banho master. Os '
  'nichos de porcelanato dos banheiros, não.',
 ],
)
