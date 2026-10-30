# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO · BANHEIRO SUÍTE 01 FILHOS — peça por peça  [30/10/2026]

pranchas 54, 55 e 56 · planta de layout e as quatro elevações A, B, C e D.

⭐⭐ QUATRO ELEVAÇÕES E **UM** MÓVEL: o gabinete de 135 sob a bancada. A
  elevação D é a MESMA parede da A, vista de lado; B e C são porcelanato,
  nicho e box.

⛔⛔ E O NICHO DE 20 × 170 DA ELEVAÇÃO B NÃO É NOSSO, por mais que ele
  pareça estante. Ele é um RASGO NA ALVENARIA revestido de porcelanato
  Incesa Marmo Blue, com quatro PRATELEIRAS EM NANOGLASS e perfil de LED
  previsto. ⭐ Pedra não é escopo da marcenaria nesta casa, e as
  prateleiras dele são pedra. Quem faz o nicho é o pedreiro e o marmorista.

⭐ A CADEIA VERTICAL DA BANCADA FECHA EM 275:
     198 de parede + 5 de Nanoglass + 52 de gabinete + 20 de VÃO ATÉ O CHÃO
  ⭐ O gabinete é SUSPENSO, como o da suíte master. Sem rodapé, sem perfil
    de piso — e a linha do perfil sai declarada a zero para dizer isso.

⭐ É O ÚNICO AMBIENTE DA CASA EM AZUL SECRETO, Linha Essencial. Um padrão
  só, um módulo só: é o levantamento mais curto do projeto.

⛔ FORA: a bancada em Nanoglass · a cuba de apoio · a torneira e o
  acionamento dourados · a bacia · o box de correr · os dois porcelanatos ·
  o nicho de 20 × 170 com suas quatro prateleiras de Nanoglass · e o
  ESPELHO de 75 × 110 com moldura dourada, que é peça de compra, não
  espelho colado de marcenaria.
"""
from base import P, gaveta, DOBRADICA, CORREDICA

AS15 = 'MDF Azul Secreto 15'
BR18, BR6 = 'MDF branco 18', 'MDF Branco TX 6'

I1 = 'ELEVAÇÃO A Gabinete suspenso sob a bancada'

LARG, ALT, PROF = 135.0, 52.0, 50.0
CG, CP = 40.0, 44.5          # coluna das gavetas e as duas de porta

BANHO_01 = [
 P('Lateral e divisória vertical', I1, ALT, PROF, 4, AS15, (1, 0),
   '⭐ Duas laterais e duas divisórias · TRÊS colunas: 40 de gaveta e duas '
   'de 44,5 com porta de giro'),
 P('Tampo e base', I1, LARG - 3, PROF, 2, AS15, (1, 0),
   '⭐ Peça única de 132 · o tampo some sob a Nanoglass e a base é a cara '
   'de baixo do móvel, que se vê de pé porque ele flutua'),
 P('Prateleira', I1, CP, 48, 2, BR18, (1, 0),
   'Uma em cada coluna de porta · as "Proj. prateleira" da elevação A'),
 P('Frente de gaveta', I1, CG, 26, 2, AS15, (2, 2),
   'Puxador tipo CAVA QUADRADA de 5 × 5, a 3 da borda'),
 *gaveta(I1, CG, 45, 24, 2, 'Caixa de gaveta'),
 P('Fundo', I1, LARG, ALT, 1, BR6, (0, 0), '⛔ sem fita'),
 P('Frente · porta de giro', I1, CP, ALT, 2, AS15, (2, 2),
   'Duas folhas de 44,5 × 52 · puxador tipo CAVA QUADRADA de 5 × 5'),
]

# ⭐ (móvel, rótulo, nº de gavetas, preço do par)
GAVETAS = [
 (I1, 'Duas gavetas de 40 × 26 · ⭐ a prancha pede corrediça INVISÍVEL, '
      'que já é a Hettich oculta da casa', 2, CORREDICA),
]
# ⭐ (móvel, rótulo, nº de FOLHAS, dobradiças POR FOLHA, preço)
PORTAS = [
 (I1, 'Duas folhas de giro de 44,5 × 52', 2, 2, DOBRADICA),
]
# ⭐ (móvel, rótulo, nº de frentes, extensão de cava em cm por frente)
CAVA = [
 (I1, 'Cava QUADRADA de 5 × 5 nas quatro frentes — duas gavetas e duas '
      'folhas · ⭐ o mesmo recorte do banheiro da suíte master', 4, 5),
]
LED = VIDRO = PUXADORES = MOLDURA = CABIDEIROS = ALMAS = []
BASCULAS = SERRALHERIA = []
# ⭐ (móvel, nome, rótulo, quantidade, unidade, chave)
OUTRAS = [
 (I1, 'Perfil de proteção de piso',
  '⛔ NÃO ENTRA: o gabinete é SUSPENSO, flutua 20 cm acima do piso. Linha '
  'a zero para que a ausência fique escrita', 0, 'm',
  'Perfil de proteção de piso'),
]

CABECA = {
 I1: ('135 × 52 × 50',
      'ELEVAÇÃO A · gabinete SUSPENSO sob a bancada de Nanoglass, 20 cm '
      'acima do piso · TRÊS colunas: duas gavetas de 40 e duas portas de '
      'giro de 44,5, cada uma com sua prateleira · MDF Azul Secreto, Linha '
      'Essencial, interno em MDF Branco · ⛔ a elevação D é ESTE MESMO '
      'gabinete visto de lado'),
}

FOLHA = dict(
 aba='BANHEIRO SUÍTE 01 FILHOS',
 sub='Gustavo Raposo · executivo Luiza Pacheco, pranchas 54, 55 e 56 · ⭐ '
     'quatro elevações e UM módulo de 1,35 m — o levantamento mais curto '
     'do projeto',
 chapa_txt={
  AS15: 'Azul Secreto · Linha Essencial · Duratex · ⭐ o único ambiente da '
        'casa neste padrão · o corpo do gabinete e as quatro frentes',
  BR18: 'Branco · as duas prateleiras internas · "interno em MDF Branco" é '
        'chamada da prancha',
  BR6:  'Branco TX · o fundo',
  'MDF Branco TX 15': 'Branco TX · a caixaria das duas gavetas',
 },
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a QUANTIDADE é '
      'a célula AMARELA no fim do painel de material, e ela sai ZERO.   '
      '⛔⛔ O NICHO DE 20 × 170 DA ELEVAÇÃO B PARECE ESTANTE E NÃO É '
      'NOSSO: é rasgo na alvenaria revestido de porcelanato, com quatro '
      'prateleiras de NANOGLASS. Pedra não é escopo da marcenaria.   '
      '⭐ O GABINETE É SUSPENSO, 20 cm acima do piso: sem rodapé e sem '
      'perfil de proteção, e a linha do perfil está declarada a zero para '
      'dizer isso.   '
      '⭐ UM PADRÃO DE CHAPA SÓ no corpo e nas frentes. É o ambiente com '
      'menos arredondamento de chapa da casa.',
 duvidas=[
  '⚠ O ESPELHO DE 75 × 110 ficou FORA. A prancha o descreve como "espelho '
  'prata com cantos arredondados e MOLDURA EM DOURADO" — isso é peça de '
  'compra, pendurada na parede, não espelho colado de marcenaria como o do '
  'Lavabo. ⭐ Se o senhor quiser que ele entre pela Valvic, são 0,83 m² e '
  'cerca de R$ 500 só de espelho, mais a moldura dourada, que não está em '
  'base de preço nenhuma. Diga e eu lanço.',
  '⚠ A PROFUNDIDADE DE 50 veio por semelhança com o gabinete do banheiro '
  'da suíte master, que a elevação D de lá cota. ⛔ Aqui a elevação D '
  'mostra o gabinete de lado mas a cota ficou fora do corte que eu li. '
  'Conferir na medição: cada 5 cm de profundidade são cerca de R$ 90.',
  '⚠ A LARGURA DAS COLUNAS saiu por medição no desenho: 40 para as '
  'gavetas e 44,5 para cada porta. A prancha cota os 135 e não as colunas.',
  '⚠ MDF EM BANHEIRO, de novo. Azul Secreto comum, sem tratamento. ⛔ Este '
  'gabinete é suspenso, o que já o protege do pior — mas a face de baixo '
  'fica exposta e é a que recebe respingo. Vale decidir se entra selagem '
  'de topo nas arestas que não levam fita.',
 ],
 nao_marcenaria=[
  '⛔ O NICHO DE 20 × 170 DA ELEVAÇÃO B, com suas QUATRO PRATELEIRAS EM '
  'NANOGLASS e o perfil de LED previsto em cada uma. ⭐ É rasgo de '
  'alvenaria revestido em porcelanato Incesa Marmo Blue: pedreiro e '
  'marmorista, não marcenaria.',
  '⛔ O ESPELHO DE 75 × 110 com cantos arredondados e moldura dourada.',
  '⛔ A BANCADA EM NANOGLASS, a cuba de apoio de 50 × 40 × 13, a torneira '
  'de mesa bica alta e o acionamento redondo, todos dourados.',
  '⛔ A BACIA SANITÁRIA, o acabamento de registro e o da válvula de '
  'descarga de parede.',
  '⛔ O BOX DE CORRER piso-teto em vidro temperado incolor com roldanas '
  'douradas, e o chuveiro redondo.',
  '⛔ OS DOIS PORCELANATOS: Incesa Marmo Blue 60 × 120 e Portobello Anima '
  'di Marmo Acetinado 120 × 120.',
 ],
 notas=[
  '⭐ UM MÓVEL DE 1,35 M em quatro pranchas de banheiro. A proporção entre '
  'desenho e marcenaria é a menor da casa — e é normal: banheiro é '
  'revestimento, louça e metal, com um gabinete no meio.',
  '⭐ O AZUL SECRETO É LINHA ESSENCIAL, não Design nem Sense. Terceira '
  'linha da Duratex neste projeto, e o preço de chapa é o mesmo dos outros '
  'padrões coloridos.',
  '⭐ A CAVA DE 5 × 5 É A MESMA DO BANHEIRO DA SUÍTE MASTER. Os dois '
  'banheiros de suíte usam o recorte pequeno; a suíte, o closet e a '
  'rouparia usam o de 10.',
 ],
)
