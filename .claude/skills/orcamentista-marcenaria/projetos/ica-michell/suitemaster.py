# -*- coding: utf-8 -*-
"""ICA · SUÍTE MASTER — levantamento peça por peça  [28/10/2026]

páginas 141 a 152 · três detalhamentos, três itens, quatro folhas de detalhe
(o DET 03 ocupa duas).

⭐⭐ TRÊS PADRÕES NOVOS DE UMA VEZ, e um deles muda de fornecedor:
    · Carvalho Brun — Duratex · a cor do ambiente, nos três itens
    · Nazca Linha Velluto — Duratex · só o campo central do painel do DET 03
    · Beige — ARAUCO · só o rack, e é o primeiro Arauco do projeto
  ⚠ Nazca Linha Velluto é linha de TOQUE ATERVELUDADO. Lancei os três a
    R$ 700 a chapa de 18, como melamínico fosco, e a dúvida 01 pergunta.

⭐ A CABECEIRA DO DET 01 É ESTOFADA, não é marcenaria: seis módulos de
  83 × 104 em linho bege. O que é nosso ali é a BASE SUPERIOR — uma
  prateleira de 5 com testeira de 6, em Carvalho Brun, que esconde a fita
  de LED que lava a parede. O estofamento entra por m² a ZERO e denuncia.

⭐ A CAMA É UMA PLATAFORMA, não um caixão com estrado: 300 × 255 de
  footprint com rebaixo de 190 × 200 para o colchão king, mesa de
  cabeceira embutida nos 30 da cabeceira e recuo de 10 na base.

⛔ O PÉ-DIREITO AQUI TAMBÉM É 300, e o painel do DET 03 vai do chão ao
  teto. O painel do nicho, as duas ripas e a testeira do rasgo de LED
  passam dos 273 da chapa.
"""
from base import P, gaveta, ALT_MAX, CHAPA_C

CB18, CB15 = 'MDF Carvalho Brun 18', 'MDF Carvalho Brun 15'
NZ18 = 'MDF Nazca Velluto 18'
BG18, BG15 = 'MDF Beige 18', 'MDF Beige 15'
EST, FUN = 'MDF Branco TX 15', 'MDF Branco TX 6'

I1 = 'DET 01 Cabeceira'
I2 = 'DET 02 Cama'
I3 = 'DET 03 Painel com rack'

SUITEMASTER = [
 # ══ ITEM 01 · CABECEIRA — 500 × 110 ══════════════════════════════════
 #  VISTA FRONTAL  6 × 83 ≈ 500 de largura · altura 6 + 104 = 110
 #  DET. CABECEIRA  prateleira de 5 contra a parede, testeira de 2 à
 #                  frente, e a fita de LED entre as duas, virada para cima
 P('Base superior · prateleira do LED', I1, 250, 5, 2, CB18, (1, 0),
   '⭐ é ela que carrega a fita · duas peças de 250 porque 500 de corrida '
   'não sai de uma chapa'),
 P('Base superior · testeira',          I1, 250, 6, 2, CB18, (2, 2),
   'A faixa de 6 que a VISTA FRONTAL mostra acima dos módulos · esconde a '
   'fita e joga a luz na parede'),

 # ══ ITEM 02 · CAMA — 300 × 255 × 45 ══════════════════════════════════
 #  VISTA SUPERIOR  300 = 55 + 190 + 55 · 255 = 30 da mesa + 225 da cama
 #                  rebaixo de 190 × 200 para o colchão king
 #  VISTA FRONTAL   altura 45 = 25 da mesa + 15 do estrado + 5 do recuo
 #  VISTA LATERAL   10 de recuo na frente · 42 + 5 no pé
 P('Plataforma · faixa lateral',   I2, 55, 225, 2, CB18, (2, 2),
   'As duas bordas de 55 que emolduram o colchão'),
 P('Plataforma · faixa do pé',     I2, 190, 25, 1, CB18, (2, 2),
   '225 menos os 200 do rebaixo'),
 # ⛔⛔ O ESTRADO DEIXOU DE SER MDF [Jonathan, 28/10/2026]: "troque o
 #   sarrafo pela estrutura de serralheria" e "Todas as camas teremos a
 #   aplicação de estrado em metalom ... o custo de cada quadro é de
 #   250,00". As duas frases dizem a mesma coisa: o que segura o colchão
 #   king não é painel de 15 mm sobre sarrafo de pinus, é quadro de
 #   metalon. Saem os dois painéis e sai o sarrafo; entram dois quadros.
 P('Saia · frente e costas',       I2, 150, 15, 4, CB18, (1, 0),
   'Duas peças em cada: 300 de corrida não sai de uma chapa'),
 P('Saia · lateral',               I2, 255, 15, 2, CB18, (1, 0)),
 P('Base recuada · frente',        I2, 140.5, 5, 2, CB18, (1, 0),
   '⭐ o recuo de 10 em cada ponta que a VISTA FRONTAL cota: a cama '
   'parece flutuar · duas peças, porque 281 de corrida passa dos 275'),
 P('Base recuada · lateral',       I2, 245, 5, 2, CB18, (1, 0)),
 P('Mesa de cabeceira · tampo',    I2, 150, 30, 2, CB18, (2, 2),
   'A faixa de 30 na cabeceira, que corre os 300 inteiros e serve de '
   'criado-mudo dos dois lados'),
 P('Mesa de cabeceira · testeira', I2, 150, 25, 2, CB18, (1, 0),
   'Os 25 que ela sobe acima do estrado'),

 # ══ ITEM 03 · PAINEL COM RACK — 400 × 300 ════════════════════════════
 #  VISTA FRONTAL  70 do nicho + 240 do painel + 90 do espelho = 400
 #                 altura 30 + 3 + 63 + 3 + 64 + 3 + 27 + 3 + 27 + 22 +
 #                 55 = 300 · QUATRO prateleiras no nicho
 #  VISTA SUPERIOR nicho 32 de profundidade, rack 45 · painel de 5
 #  VISTA LATERAL  rack suspenso a 55 do chão, 22 de altura
 P('Painel do nicho',        I3, 300, 70, 1, CB18, (2, 2),
   '⛔ 300 de altura · é o fundo escuro contra o qual as prateleiras '
   'aparecem'),
 P('Ripa vertical',          I3, 300, 8, 2, CB18, (2, 2),
   '⛔ 300 de altura · as duas ripas que carregam as prateleiras do nicho'),
 P('Prateleira do nicho',    I3, 56, 32, 4, CB18, (2, 2),
   'Borda arredondada · quatro, nos vãos de 30, 63, 64 e 27'),
 P('Painel central',         I3, 240, 150, 2, NZ18, (2, 2),
   'Nazca Linha Velluto · duas peças porque 300 de altura não sai de uma '
   'chapa · ⚠ a emenda horizontal cai no meio de um campo liso'),
 P('Testeira do rasgo de LED', I3, 300, 5, 2, CB18, (1, 1),
   '⛔ 300 de altura · é ela que forma o rasgo onde a fita corre, numa '
   'lateral e na outra'),
 P('Painel de apoio do espelho', I3, 90, 150, 2, CB18, (1, 1),
   '⭐ o espelho é do vidraceiro, mas ele cola em alguma coisa · duas '
   'peças porque 300 de altura não sai de uma chapa'),
 # ── o rack, em MDF Beige da Arauco
 P('Rack · lateral',         I3, 22, 45, 2, BG15, (1, 1), 'Aparente: é suspenso'),
 P('Rack · tampo e base',    I3, 168, 45, 4, BG15, (1, 0),
   'Duas peças em cada: 336 de corrida não sai de uma chapa'),
 P('Rack · divisória',       I3, 22, 45, 4, EST, (1, 0), 'Cinco módulos de 67'),
 P('Rack · fundo',           I3, 170, 22, 2, FUN, (0, 0), 'Encaixe em rasgo'),
 P('Rack · frente de gaveta', I3, 67, 22, 5, BG18, (2, 2),
   'Cinco gavetas de 67 · sem puxador desenhado'),
 P('Rack · tampo de correr', I3, 67, 45, 1, BG18, (2, 2),
   '⭐ "gaveta com tampo superior de correr, para esconder aparelhos e '
   'fio" · a VISTA SUPERIOR marca o módulo central com a seta'),
 *gaveta(I3, 67, 40, 22, 5, 'Gaveta'),
]

# ── ferragem, declarada item a item ─────────────────────────────────────
GAVETAS = [(I3, 'Rack · cinco gavetas de 67 · abrem por toque', 5, 400, 'touch')]
PORTAS  = []
BASCULAS= []
CAVA    = []
PUXADORES= []
MOLDURA = []
#  ⭐ três fitas: a da cabeceira lava a parede, e as duas do DET 03 correm
#    nas laterais do painel e do espelho, de cima a baixo
LED     = [(I1, 'Sob a base superior, de ponta a ponta da cabeceira', 5.00),
           (I3, 'Nas duas laterais do painel · 3 m cada, do chão ao teto', 6.00)]
CABIDEIROS = []
SARRAFOS= []   # ⛔ pinus PROIBIDO · o estrado virou quadro de metalon
SUPORTES= []
ALMAS   = []
# ⭐ O ESPELHO DO DET 03 ENTRA NA CONTA [Jonathan, 28/10/2026]: "item 3 -
#   idem situação acima das gavetas, considere o espelho tbm". São os 90
#   da ponta direita do painel de 400, de piso a teto: 0,90 × 3,00 =
#   2,70 m², colados no painel de apoio que já estava na conta.
VIDRO   = [(I3, 'Espelho de 90 × 300 da ponta direita do painel · colado no '
            'painel de apoio de Carvalho Brun', 1, 90, 300, 'Espelho')]
SERRALHERIA = []
# ⭐ nada da Suíte Master toca o chão com painel: a cabeceira é parede, a
#   cama é plataforma com base recuada e o rack é suspenso. ⚠ A base de
#   3 cm recuada da plataforma segue como dúvida.
OUTRAS  = [# ⭐ O ESTOFADO TEM PREÇO [Jonathan, 28/10/2026]: "item 1 -
           #   considere o metro quadrado do estofado em 600,00". Saiu do
           #   zero e deixou de ser PISO: 5,18 m² × R$ 600 = R$ 3.108.
           (I1, 'Estofamento em linho', 'Seis módulos de 83 × 104 em linho '
            'bege · ⛔ é estofador, não marcenaria · R$ 600 o m²',
            5.18, 'm²', 'Estofamento em linho'),
           # ⭐ ESTRADO EM METALON · R$ 250 o quadro [Jonathan, 28/10/2026]
           (I2, 'Estrado em metalon', 'Dois quadros de 190 × 100 sob o '
            'colchão king · ⛔ substitui os dois painéis de MDF e o sarrafo '
            'de pinus que os apoiava: é ele a "estrutura de serralheria" '
            'que o senhor pediu no lugar do sarrafo', 2, 'quadro',
            'Estrado em metalon')]
# ⛔⛔ O PULSADOR DO RACK SAIU E ENTROU CORREDIÇA TOUCH [Jonathan,
#   28/10/2026]: "no caso de corrediças com abertura por toque, considere
#   a corrediça touch, não precisa de pulsador". As cinco gavetas do rack
#   não têm puxador desenhado e abrem por toque — quem abre é a corrediça,
#   R$ 500 o par, e o pulsador por cima seria pagar duas vezes.

CABECA = {
 I1: ('500 × 110 × 5',
      'VISTA FRONTAL seis módulos de 83 ≈ 500 · altura 6 da base superior '
      'mais 104 do estofado = 110 · DET. CABECEIRA prateleira de 5 contra '
      'a parede, testeira de 2 à frente e a fita de LED entre as duas'),
 I2: ('300 × 255 × 45',
      'VISTA SUPERIOR 55 + 190 + 55 = 300 · 30 da mesa de cabeceira mais '
      '225 da cama = 255 · rebaixo de 190 × 200 para o colchão king · '
      'VISTA FRONTAL altura 25 + 15 + 5 = 45 · VISTA LATERAL recuo de 10'),
 I3: ('400 × 300 × 45',
      'VISTA FRONTAL 70 do nicho + 240 do painel + 90 do espelho = 400 · '
      'altura 300 em quatro prateleiras e cinco vãos · VISTA SUPERIOR '
      'nicho de 32 e rack de 45 · VISTA LATERAL rack suspenso a 55 do '
      'chão, com 22 de altura'),
}

FOLHA = dict(
 aba='SUÍTE MASTER',
 sub='Jéssica e Michell · Projeto ICA · páginas 141 a 152 · três itens em '
     'quatro folhas de detalhe · ⭐ TRÊS padrões novos de uma vez, e um '
     'deles é ARAUCO, outro fornecedor · caixaria em Branco TX 15 · '
     f'⛔ pé-direito de 300 contra peça inteira de {ALT_MAX:g}, que é a '
     f'chapa de {CHAPA_C:g} menos o acerto de corte',
 chapa_txt={CB18: 'Carvalho Brun · Duratex · a cor do ambiente, nos três itens',
            CB15: 'Carvalho Brun · Duratex · peças de estrutura aparente',
            NZ18: '⚠ Nazca Linha Velluto · Duratex · toque ateveludado, só '
                  'o campo central do painel do DET 03',
            BG18: 'Beige · ARAUCO · as frentes e o tampo de correr do rack',
            BG15: 'Beige · ARAUCO · a caixa do rack',
            EST:  'Estrutura e caixaria · o padrão da Base para caixaria',
            FUN:  'Fundos · encaixe em rasgo, sem fita'},
 nota='⛔ O FRETE ESTÁ ZERADO DE PROPÓSITO: as linhas de frete da Base não '
      'têm preço ainda. Preencher lá e elas aparecem aqui sozinhas.   '
      '⭐ A CABECEIRA DO DET 01 É ESTOFADA e não é nossa: seis módulos de '
      '83 × 104 em linho bege, 5,18 m². O que é marcenaria ali é a base '
      'superior que esconde o LED. O estofamento entra por m² a ZERO.   '
      '⛔ O PÉ-DIREITO É 300 e o painel do DET 03 vai do chão ao teto: o '
      'painel do nicho, as duas ripas e as duas testeiras do rasgo de LED '
      'passam dos 273 que a chapa dá em peça inteira.   ⚠ TRÊS PADRÕES '
      'NOVOS, lançados a R$ 700 a chapa de 18 como melamínico fosco — e o '
      'Nazca Linha Velluto é linha de toque ateveludado, que costuma '
      'custar mais.',
 duvidas=[
  'TRÊS PADRÕES NOVOS DE UMA VEZ: Carvalho Brun e Nazca Linha Velluto, da '
  'Duratex, e Beige, da ARAUCO. ⚠ Lancei os três a R$ 700 a chapa de 18, '
  'como melamínico fosco. ⛔ O Nazca Linha VELLUTO é linha de toque '
  'ateveludado — não é fosco comum, e costuma sair mais caro. E o Beige é '
  'o PRIMEIRO ARAUCO do projeto: a Base não distingue fornecedor, só '
  'espessura. Confirmar os três preços.',
  'A CABECEIRA DO DET 01 É ESTOFADA EM LINHO BEGE, seis módulos de 83 × '
  '104. ⛔ Isso é estofador, não marcenaria, e a Base não tem a linha: sai '
  'ZERO. São 5,18 m² de estofado com espuma e tecido. ⚠ Confirmar se a '
  'Valvic fornece ou se o cliente contrata direto — e, se fornecemos, se o '
  'compensado de base é nosso ou do estofador. Hoje a conta tem só a base '
  'superior de Carvalho Brun, que é a parte que é certa.',
  'O ESPELHO DE 90 × 300 do DET 03 é vidraceiro. ⚠ Mas ele cola em alguma '
  'coisa: lancei um painel de apoio em Carvalho Brun de 90 × 300, em duas '
  'peças. ⛔ Se o espelho for colado direto na alvenaria, esse painel sai '
  'da conta e com ele 0,5 chapa. E espelho de 3 m de altura com LED na '
  'lateral é peça especial — confirmar quem mede e quem instala.',
  'O PAINEL CENTRAL DE NAZCA VELLUTO TEM 240 × 300 e não sai de uma chapa: '
  'dividi em duas peças de 240 × 150 e a emenda cai no MEIO de um campo '
  'liso, sem linha de desenho onde se esconder. ⚠ Num acabamento de toque '
  'ateveludado a emenda horizontal aparece mais, não menos. ⛔ Ou o '
  'desenho ganha uma ranhura na altura da emenda, ou a casa compra chapa '
  'de 300 para este painel.',
  'O RACK DO DET 03 NÃO TEM PUXADOR DESENHADO nas cinco gavetas. ⭐ Orcei '
  'PULSADOR, R$ 100 cada, R$ 500 pelos cinco — é o mesmo que fiz no rack '
  'da Sala de Cinema, que tem a mesma solução de tampo de correr. ⚠ Se a '
  'corrediça já vier com push-to-open, os R$ 500 saem.',
  'O "TAMPO SUPERIOR DE CORRER" aparece aqui e na Sala de Cinema, com a '
  'mesma nota e a mesma imagem de referência. ⚠ Lancei a chapa do tampo, '
  'mas a FERRAGEM que o faz correr não está na Base e não entrou. É '
  'corrediça de tampo, não de gaveta. ⛔ Dois ambientes esperam esse '
  'preço.',
  '⛔ A BASE METÁLICA DE 3 CM não está lançada aqui. A cama e o painel do '
  'DET 03 tocam o chão, e a prancha da Sala de Cinema escreve a regra em '
  'todas as folhas. ⚠ Lancei a base na Sala de Cinema e deixei os outros '
  'ambientes para uma passada só, quando o senhor mandar.'],
 nao_marcenaria=[
  'Cabeceira com módulos estofados em linho bege — 5,18 m² de estofamento',
  'Espelho de 90 × 300 do DET 03 — vidraceiro (o painel de apoio é nosso)',
  'Colchão king size 190 × 200',
  'TV, aparelhos e a torre de tomadas escondida no rack'],
 notas=[
  '⭐⭐ TRÊS PADRÕES NOVOS E UM FORNECEDOR NOVO. Carvalho Brun é a cor do '
  'ambiente e aparece nos três itens; Nazca Linha Velluto só no campo '
  'central do painel; Beige, da Arauco, só no rack. ⚠ Cada padrão é um '
  'arredondamento próprio, e o Beige existe para UM móvel de 340 × 22.',
  '⭐ A CABECEIRA É DE OUTRO OFÍCIO. O DET. CABECEIRA desenha o corte com '
  'clareza: prateleira de 5 contra a parede, fita de LED virada para cima, '
  'testeira de 2 escondendo a fita, e o módulo estofado abaixo. A '
  'marcenaria faz a prateleira e a testeira; o estofador faz o resto.',
  '⭐ A CAMA É UMA PLATAFORMA. Não tem lateral de caixão nem estrado '
  'solto: é uma moldura de 55 em volta de um rebaixo de 190 × 200, com a '
  'mesa de cabeceira embutida nos 30 da cabeceira e um recuo de 10 na '
  'base, que a faz flutuar. O estrado interno é Branco TX 15, como no '
  'Quarto e na Suíte Hóspedes.',
  '⚠ O RACK SE REPETE. Este e o da Sala de Cinema são o mesmo móvel em '
  'outra medida: gavetas rasas, tampo superior de correr para esconder '
  'aparelhos, nenhum puxador desenhado. A mesma dúvida vale para os dois.'],
)
