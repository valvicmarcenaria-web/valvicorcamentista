# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO · ANEXO BANHEIRO SOCIAL — peça por peça  [30/10/2026]

prancha 71 · planta de layout e elevação A na mesma folha.

⭐ UM GABINETE DE 88 sob bancada de Nanoglass com cuba semi-encaixe. Duas
  folhas de giro, uma divisória no meio e uma prateleira em cada coluna.

⛔ A BANCADA AQUI TEM 15, não 5. É cuba SEMI-ENCAIXE: a pedra precisa de
  espessura para receber o recorte, e isso empurra o gabinete para baixo.
     174 de parede + 15 de Nanoglass + 51 de gabinete + 20 de vão = 260
  ⭐ E o gabinete tem 51 de altura, não 52 como os outros três banheiros.

⛔ FORA: a bancada em Nanoglass com a cuba semi-encaixe de 40 × 40 · a
  torneira misturador inox · a bacia com caixa acoplada · o box de h = 190
  · o porcelanato · o nicho revestido · e o ESPELHO de 60 × 110 com
  moldura, que é peça de compra.
"""
from base import P, DOBRADICA

NT15 = 'MDF Nogueira Thar 15'
BR18, BR6 = 'MDF branco 18', 'MDF Branco TX 6'

I1 = 'ELEVAÇÃO A Gabinete suspenso sob a bancada'

LARG, ALT, PROF = 88.0, 51.0, 40.0
COL = (LARG - 4.5)/2        # 41,75 · duas colunas com divisória no meio

BANHO_SOCIAL = [
 P('Lateral e divisória vertical', I1, ALT, PROF, 3, NT15, (1, 0),
   '⭐ Duas laterais e uma divisória · DUAS colunas de 41,75'),
 P('Tampo e base', I1, COL, PROF, 4, NT15, (1, 0)),
 P('Prateleira', I1, COL, 38, 2, BR18, (1, 0),
   'Uma em cada coluna · as "Proj. prateleira" da elevação A'),
 P('Fundo', I1, LARG, ALT, 1, BR6, (0, 0), '⛔ sem fita'),
 P('Frente · porta de giro', I1, COL, ALT, 2, NT15, (2, 2),
   'Duas folhas de 41,75 × 51 · puxador tipo CAVA QUADRADA de 5 × 5'),
]

PORTAS = [(I1, 'Duas folhas de giro de 41,75 × 51', 2, 2, DOBRADICA)]
CAVA = [(I1, 'Cava QUADRADA de 5 × 5 nas duas folhas', 2, 5)]
GAVETAS = LED = VIDRO = PUXADORES = MOLDURA = CABIDEIROS = ALMAS = []
BASCULAS = SERRALHERIA = []
OUTRAS = [
 (I1, 'Perfil de proteção de piso',
  '⛔ NÃO ENTRA: o gabinete é SUSPENSO, flutua 20 cm acima do piso. Linha '
  'a zero para que a ausência fique escrita', 0, 'm',
  'Perfil de proteção de piso'),
]

CABECA = {
 I1: ('88 × 51 × 40',
      'ELEVAÇÃO A · gabinete SUSPENSO sob bancada de Nanoglass de 15 com '
      'cuba SEMI-ENCAIXE · duas colunas de 41,75, uma folha de giro e uma '
      'prateleira em cada · MDF Nogueira Thar, interno em MDF Branco · '
      '⛔ pé-direito de 260, como todo o anexo'),
}

FOLHA = dict(
 aba='BANHEIRO SOCIAL',
 sub='Gustavo Raposo · executivo Luiza Pacheco, prancha 71 · ⭐ um '
     'gabinete de 88 cm, o segundo menor ambiente do projeto',
 chapa_txt={
  NT15: 'Nogueira Thar · Linha Design · Duratex · o corpo e as duas '
        'folhas',
  BR18: 'Branco · as duas prateleiras',
  BR6:  'Branco TX · o fundo',
 },
 nota='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a QUANTIDADE é '
      'a célula AMARELA no fim do painel de material, e ela sai ZERO.   '
      '⛔⛔ A BANCADA AQUI TEM 15 E NÃO 5, e isso é informação de '
      'fabricação: a cuba é SEMI-ENCAIXE e a pedra precisa de espessura '
      'para receber o recorte. ⭐ O gabinete desceu para 51 de altura por '
      'causa disso — é o único dos quatro banheiros com essa medida, e '
      'quem copiar os 52 dos outros vai sobrar 1 cm.   '
      '⭐ MESMO PADRÃO DO BANHEIRO DA SUÍTE DE HÓSPEDES: Nogueira Thar, '
      'interno em MDF Branco, cava quadrada de 5 × 5. Os dois do anexo '
      'são irmãos e devem sair na mesma compra de chapa.',
 duvidas=[
  '⚠ A PROFUNDIDADE DE 40 não está cotada. Adotei 40, o mesmo do banheiro '
  'de hóspedes.',
  '⚠ O ESPELHO DE 60 × 110 ficou FORA: moldura "a definir", peça de '
  'compra. ⭐ Mesma decisão dos outros três banheiros.',
  '⚠ A DIVISÓRIA DO MEIO. A elevação desenha uma linha vertical no centro '
  'dos 88 e a "Proj. prateleira" atravessa os dois lados. Li como '
  'divisória com uma prateleira de cada lado. ⛔ Se for prateleira única '
  'de 85 atravessando, sai uma peça e entra o risco de flecha — 85 ainda '
  'está abaixo dos 120 da regra, mas em 18 mm com peso de banheiro é '
  'justo.',
 ],
 nao_marcenaria=[
  '⛔ O ESPELHO de 60 × 110 com cantos arredondados e moldura a definir.',
  '⛔ A BANCADA EM NANOGLASS de 15 com a CUBA SEMI-ENCAIXE quadrada de '
  '40 × 40 e a torneira misturador de mesa inox. ⚠ A cuba semi-encaixe '
  'exige recorte na pedra E folga no nosso tampo: a medição da pedra tem '
  'de sair depois do gabinete montado.',
  '⛔ A BACIA com caixa acoplada e o BOX de h = 190 com porta de giro em '
  'vidro temperado, estrutura inox e puxador slim vertical.',
  '⛔ O PORCELANATO Portobello Anima di Marmo e o NICHO revestido de '
  '10 cm com perfil de LED previsto.',
 ],
 notas=[
  '⭐ CINCO LINHAS DE PEÇA E QUATRO DOBRADIÇAS. Com o banheiro de '
  'hóspedes, são os dois ambientes mais simples do projeto.',
  '⭐ OS DOIS BANHEIROS DO ANEXO SÃO IRMÃOS: mesmo padrão de chapa, mesma '
  'cava, mesmo pé-direito de 260. Devem sair juntos no plano de corte e '
  'subir no mesmo caminhão.',
 ],
)
