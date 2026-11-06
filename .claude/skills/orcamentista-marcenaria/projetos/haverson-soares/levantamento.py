# -*- coding: utf-8 -*-
"""HAVERSON SOARES · Cozinha e Gourmet · executivo Luiza Pacheco, Rev.00 (out/2026)
Rua Jatobás, 125 · Residencial Árvores · Alphaville · Nova Lima/MG.

Sete pranchas A3 em AutoCAD, 1/25, COTADAS: 01 a 04 Cozinha, 05 a 07 Gourmet.
A leitura completa está no README.md desta pasta.

Especificação da prancha:
  · frentes e partes aparentes em MDF AZUL A DEFINIR (melamínico de cor);
  · no gourmet: torre quente, superiores, cristaleira e nicho em MDF FREIJÓ PURO,
    linha Essencial Wood, Duratex; a colmeia de vinhos da ilha também;
  · interno em MDF BRANCO · puxador CAVA NA MARCENARIA;
  · ferragens HÄFELE, gavetas com corrediça oculta.

Premissas minhas (cada uma vai como dúvida numerada na planilha):
  · ⚠ HÄFELE NÃO ESTÁ NA BASE DE CUSTOS: dobradiça e corrediça entram pelo
    preço da linha Gold da casa (Hettich Sensys R$ 50 e Quadro V6 R$ 150), a
    cotar com o distribuidor Häfele;
  · as básculas da PIA abrem PARA BAIXO (o vértice do símbolo aponta o lado da
    pega e a pedra está logo acima): duas dobradiças e dois pistões com
    amortecimento cada · as do SUPERIOR do gourmet abrem PARA CIMA: articulador
    de báscula da casa (AVENTOS HK-XS, R$ 250), equivalente Häfele a cotar;
  · cava usinada pela largura de cada frente (R$ 50/m);
  · os superiores da cozinha têm 60 de profundidade, lidos do corte B;
  · o sóculo "em marcenaria com frente no material da bancada" é estrutura
    nossa em Branco TX; a FRENTE é pedra, logo NÃO é nossa;
  · colmeia com 40 de profundidade (a ilha tem 44, e a prancha não cota).
⛔ PEDRA NUNCA É NOSSA: bancadas e complemento de bancada, frente dos sóculos,
   frontão, ilha. Eletrodomésticos, cooktop, coifa, cubas, adegas e
   churrasqueira também ficam fora.

Cada peça: (peça, observação, C, L, QTD, chave da Base, fita em m por peça, tipo
de fita) · ferragem: (peça, observação, QTD, UN, chave) · terceirizado por m²,
sem chapa: (peça, observação, C, L, QTD, UN, chave).
"""
ITENS = []      # dicionários: amb, movel, medida, cadeia, pecas, ferr, terc

AZ15, AZ18 = 'MDF Azul 15', 'MDF Azul 18'
FR15, FR18, FR6 = 'MDF Freijó 15', 'MDF Freijó 18', 'MDF Freijó 6'
BR15, BR18, BR6 = 'MDF Branco TX 15', 'MDF Branco TX 18', 'MDF Branco TX 6'


def item(amb, movel, medida, cadeia):
    d = dict(amb=amb, movel=movel, medida=medida, cadeia=cadeia, pecas=[], ferr=[], terc=[])
    ITENS.append(d); return d


def P(it, nome, obs, c, l, qtd, chave, fita=0.0, tipo=None):
    tipo = tipo or ('Fita Branco TX' if 'Branco' in chave else 'Fita cor')
    it['pecas'].append((nome, obs, c, l, qtd, chave, fita, tipo))


def F(it, nome, obs, qtd, un, chave):
    it['ferr'].append((nome, obs, qtd, un, chave))


def T(it, nome, obs, c, l, qtd, chave):
    """Terceirizado por m² (folha pronta): não entra no plano de corte."""
    it['terc'].append((nome, obs, c, l, qtd, 'm²', chave))


def dobradicas(alt):
    return 2 if alt <= 90 else 3 if alt <= 160 else 4 if alt <= 200 else 5


def cava(it, larguras, obs='puxador cava na própria frente, pela largura'):
    F(it, 'Cava usinada', obs, round(sum(larguras) / 100, 2), 'm', 'Cava usinada')


def gavetas(it, n, larg, alt, prof, frente=AZ15, rotulo='Gaveta'):
    li = larg - 6.6
    P(it, f'{rotulo} · frente', '', larg, alt, n, frente, 2 * (larg + alt) / 100)
    P(it, f'{rotulo} · lateral da caixa', '', prof - 5, alt - 5, 2 * n, BR15, (prof - 5) / 100)
    P(it, f'{rotulo} · frente e traseira da caixa', '', li, alt - 5, 2 * n, BR15, li / 100)
    P(it, f'{rotulo} · fundo da caixa', 'encaixe em rasgo, sem fita', li + 1, prof - 6, n, BR6)
    F(it, 'Corrediça Häfele', f'oculta, com amortecimento · uma por {rotulo.lower()}', n, 'gaveta',
      'Corrediça Häfele')
    cava(it, [larg] * n)


def giro(it, n, larg, alt, frente=AZ15, obs='15 mm · puxador em cava'):
    nd = dobradicas(alt)
    P(it, 'Porta de giro', obs, alt, larg, n, frente, 2 * (alt + larg) / 100)
    F(it, 'Dobradiça Häfele', f'{nd} por folha de ' + f'{alt:g}'.replace('.', ',') + ' de altura',
      nd * n, 'un', 'Dobradiça Häfele')
    cava(it, [larg] * n)


def bascula_baixo(it, n, larg, alt, frente=AZ15):
    """Báscula da pia, que abre PARA BAIXO: duas dobradiças e dois pistões."""
    P(it, 'Báscula', 'abre para baixo · 15 mm', larg, alt, n, frente, 2 * (larg + alt) / 100)
    F(it, 'Dobradiça Häfele', 'duas por báscula, na aresta de baixo', 2 * n, 'un', 'Dobradiça Häfele')
    F(it, 'Pistão com amortecimento', 'dois por báscula, segura a frente aberta', 2 * n, 'un',
      'Pistão com amortecimento')
    cava(it, [larg] * n)


def prateleiras(it, n, vao, prof, chave=None, obs=''):
    chave = chave or (BR18 if vao > 70 else BR15)
    P(it, 'Prateleira', obs or f'vão de {vao:g}'.replace('.', ','), vao - 0.4, prof - 3, n, chave,
      vao / 100)
    F(it, 'Suporte de prateleira', 'jogo de 4 por prateleira interna', n, 'jogo',
      'Suporte de prateleira')


def caixa_inferior(it, modulos, alt, prof):
    """Caixa de armário inferior sob bancada: laterais em Branco, base, duas
    travessas no topo (a pedra é o tampo), fundo em 6 mm."""
    L = sum(modulos)
    pedacos = [L] if L <= 270 else [L / 2, L / 2]
    P(it, 'Lateral e divisória', 'Branco TX · fita na aresta da frente', alt, prof - 1,
      len(modulos) + 1, BR15, alt / 100)
    for x in pedacos:
        em = ' · emenda sobre a divisória' if len(pedacos) > 1 else ''
        P(it, 'Base', 'Branco TX' + em, x, prof - 1, 1, BR15, x / 100)
        P(it, 'Travessa da frente', 'sob a bancada' + em, x, 10, 1, BR15, x / 100)
        P(it, 'Travessa de trás', 'sob a bancada' + em, x, 10, 1, BR15)
        P(it, 'Fundo', 'encaixe em rasgo, sem fita' + em, x, alt, 1, BR6)


def soculo(it, L, prof, alt=12):
    """Estrutura do sóculo em Branco TX. ⛔ A FRENTE É PEDRA: não é nossa."""
    P(it, 'Sóculo · régua de frente e de trás', 'estrutura · a frente recebe a pedra, que não é nossa',
      L, alt, 2, BR15)
    P(it, 'Sóculo · travessa', 'uma a cada 60', prof - 13, alt, max(2, round(L / 60) + 1), BR15)


# ════════════════════════════════════════════════════════════════════════
# 01 · COZINHA
# ════════════════════════════════════════════════════════════════════════
it = item('Cozinha', 'Armários inferiores da pia e do cooktop', '415 × 68 × 56',
          'elevação A: 52,5 + 52,5 + 25 + 77 + 3 × 69,33 = 415 · frente de 68 sobre o sóculo '
          'existente, sob a bancada existente · prof. pela bancada')
caixa_inferior(it, [52.5, 52.5, 25, 77, 69.33, 69.33, 69.33], 68, 56)
gavetas(it, 2, 52.1, 33.6, 50, rotulo='Gavetão')                         # módulo 1
gavetas(it, 2, 52.1, 16.6, 50, rotulo='Gaveta')                          # módulo 2 · talheres
gavetas(it, 1, 52.1, 33.6, 50, rotulo='Gavetão')
P(it, 'Porta-temperos · frente', 'módulo de 25, frente inteira de 68', 24.6, 67.6, 1, AZ15,
  2 * (24.6 + 67.6) / 100)
P(it, 'Porta-temperos · lateral', 'caixa do porta-temperos', 60, 48, 2, BR15, 0.60)
P(it, 'Porta-temperos · bandeja', 'três níveis', 18, 48, 3, BR15, 0.18)
F(it, 'Corrediça Häfele', 'porta-temperos · ⚠ pede corrediça de carga lateral', 1, 'gaveta',
  'Corrediça Häfele')
cava(it, [25])
gavetas(it, 2, 76.6, 33.6, 50, rotulo='Gavetão')                         # módulo 4 · cooktop
bascula_baixo(it, 3, 68.9, 33.6)                                         # módulos 5 a 7 · pia
gavetas(it, 3, 68.9, 33.6, 50, rotulo='Gavetão')

it = item('Cozinha', 'Armários inferiores da parede da geladeira', '174 × 68 × 56',
          'elevação B: 2 módulos de 87 · frente de 68 sobre o sóculo existente')
caixa_inferior(it, [87, 87], 68, 56)
gavetas(it, 4, 86.6, 33.6, 50, rotulo='Gavetão')

it = item('Cozinha', 'Torre quente', '80 × 249 × 60',
          'elevação C: 5 + 74 + 10 + 39 + 10 + 60 + 10 + 29 + 12 = 249 · micro-ondas de 34 L '
          'e forno de 80 L de embutir')
P(it, 'Lateral aparente', 'as duas aparecem: a da porta de vidro e a do nicho da adega', 237, 58,
  2, AZ15, 2.37 + 0.58)
P(it, 'Base e teto', '', 77, 58, 2, BR15, 0.77)
P(it, 'Horizontal fixa', 'sob o armário, sob e entre os eletros', 77, 55, 3, BR15, 0.77)
P(it, 'Apoio do forno', '18 mm', 77, 55, 1, BR18, 0.77)
prateleiras(it, 1, 77, 58)
P(it, 'Fundo do armário superior', 'encaixe em rasgo', 77, 74, 1, BR6)
giro(it, 2, 39.6, 73.6)
P(it, 'Requadro horizontal', 'as faixas de 10 entre os eletros', 79.6, 10, 3, AZ15,
  2 * (79.6 + 10) / 100)
P(it, 'Requadro vertical', 'as faixas que fecham o nicho dos eletros', 99, 10, 2, AZ15,
  2 * (99 + 10) / 100)
gavetas(it, 1, 79.6, 28.6, 50, rotulo='Gavetão')
P(it, 'Acabamento superior', 'faixa de 5 até o forro', 80, 5, 1, AZ15, 0.80)
soculo(it, 77, 58)

it = item('Cozinha', 'Armários superiores sobre a bancada', '157 × 79 × 58',
          'elevação C: 74 + 5 de acabamento · duas portas em cada módulo de 78,5 · ⚠ 60 de '
          'profundidade, lida do corte B')
P(it, 'Lateral e divisória', 'Branco TX', 74, 58, 3, BR15, 0.74)
P(it, 'Base', 'Azul: é vista por baixo', 76.5, 58, 2, AZ15, 0.765)
P(it, 'Teto', '', 76.5, 58, 2, BR15, 0.765)
prateleiras(it, 2, 76.5, 58)
P(it, 'Fundo', 'encaixe em rasgo', 76.5, 74, 2, BR6)
giro(it, 4, 38.9, 73.6)
P(it, 'Acabamento superior', 'faixa de 5 até o forro', 157, 5, 1, AZ15, 1.57)

it = item('Cozinha', 'Bancada em MDF Azul, nicho da adega e armário', '157 × 90 × 60',
          'elevação C: nicho de 55 + armário de 102 · bancada de 3 a 90 do piso · sóculo de 12')
P(it, 'Bancada', 'duas de 15 coladas = 30 mm · fita na frente', 157, 60, 2, AZ15, 1.57)
P(it, 'Lateral fixa', 'a face do canto morto, entre a bancada e o superior', 80, 60, 1, AZ15,
  0.80 + 0.60)
P(it, 'Base do nicho da adega', 'a adega é do cliente', 55, 58, 1, AZ15, 0.55)
P(it, 'Lateral do nicho', 'a do armário que aparece no nicho', 75, 58, 1, AZ15, 0.75 + 0.58)
P(it, 'Lateral de encosto', '', 75, 58, 1, BR15, 0.75)
P(it, 'Base do armário', '', 99, 58, 1, BR15, 0.99)
P(it, 'Travessa', 'sob a bancada', 99, 10, 2, BR15, 0.99)
prateleiras(it, 1, 99, 58)
P(it, 'Fundo', 'encaixe em rasgo', 99, 75, 1, BR6)
giro(it, 2, 50.8, 74.6)
soculo(it, 154, 58)

it = item('Cozinha', 'Armário sobre a geladeira e máscara', '88 × 54 × 59 · máscara 59 × 195',
          'elevação B: 49 + 5 sobre a geladeira Samsung de 465 L · máscara de 2 na lateral')
P(it, 'Lateral aparente', 'a do lado da pedra', 49, 59, 1, AZ15, 0.49 + 0.59)
P(it, 'Lateral de encosto', 'contra o painel do piso ao teto', 49, 59, 1, BR15, 0.49)
P(it, 'Base', 'Azul: é vista por baixo', 84.4, 59, 1, AZ15, 0.844)
P(it, 'Teto', '', 84.4, 59, 1, BR15, 0.844)
P(it, 'Fundo', 'encaixe em rasgo', 84.4, 49, 1, BR6)
giro(it, 2, 43.8, 48.6)
P(it, 'Acabamento superior', 'faixa de 5 até o forro', 88, 5, 1, AZ15, 0.88)
P(it, 'Máscara da geladeira', '18 mm · do piso ao armário', 195, 59, 1, AZ18, 1.95 + 0.59)
F(it, 'Perfil de proteção de piso', 'na máscara, que toca o chão', 0.59, 'm',
  'Perfil de proteção de piso')

it = item('Cozinha', 'Painel fixo do piso ao teto', '72 × 249',
          'elevação C, à direita: fecha o canto morto e é a lateral do nicho da geladeira')
P(it, 'Painel', '18 mm · uma peça só: 249 cabe na chapa', 249, 72, 1, AZ18, 2 * (2.49 + 0.72))
P(it, 'Travessa de fixação', 'no alto e embaixo', 68, 10, 2, BR15)
F(it, 'Perfil de proteção de piso', 'painel que toca o chão', 0.72, 'm',
  'Perfil de proteção de piso')

it = item('Cozinha', 'Colmeia de vinhos na ilha', '91 × 64 × 40',
          'elevação D: sete por cinco nichos de 10,4 × 10,71, divisória de 2 · no vão da ilha '
          'de pedra existente · ⚠ profundidade não cotada: 40')
P(it, 'Horizontal da colmeia', 'Freijó 18 · meia-madeira nas verticais', 91, 40, 6, FR18, 0.91)
P(it, 'Vertical da colmeia', 'Freijó 18 · meia-madeira nas horizontais', 64, 40, 8, FR18, 0.64)

# ════════════════════════════════════════════════════════════════════════
# 02 · GOURMET
# ════════════════════════════════════════════════════════════════════════
it = item('Gourmet', 'Cristaleira com porta de vidro reflecta bronze', '51 × 254 × 60',
          'elevação A: 5 + 169 + 2 + 78 = 254 · 2 + 47 + 2 = 51 · nicho de 78 para a adega '
          'existente')
P(it, 'Lateral', 'Freijó 18 · do piso ao forro', 254, 60, 2, FR18, 2.54 + 0.60)
P(it, 'Teto, base da vitrine e base do nicho', '', 47, 58, 3, FR18, 0.47)
P(it, 'Acabamento superior', 'faixa de 5', 47, 5, 1, FR18, 0.47)
P(it, 'Prateleira da vitrine', 'Freijó 18 · FIXA: o LED corre por baixo', 46.6, 55, 3, FR18, 0.466)
P(it, 'Fundo da vitrine', 'Freijó 6 · o interno é Freijó', 169, 47, 1, FR6)
T(it, 'Porta de vidro reflecta bronze', 'perfil metálico bronze e puxador bronze · folha pronta',
  169, 47, 1, 'Porta de vidro reflecta bronze')
F(it, 'Dobradiça de porta de vidro', 'quatro na folha de 169', 4, 'un', 'Dobradiça vidro')
F(it, 'LED conjunto', 'perfil com abas sob o teto e sob as três prateleiras', round(4 * 0.47, 2),
  'm', 'LED conjunto')
F(it, 'Fonte de LED', '', 1, 'un', 'Fonte de LED')
F(it, 'Perfil de proteção de piso', 'nas duas laterais', 1.20, 'm', 'Perfil de proteção de piso')

it = item('Gourmet', 'Armários inferiores da área molhada e da churrasqueira', '246 × 70 × 56',
          'elevação A: 4 × 61,5 = 246 · frente de 70 · sóculo de 10 · sob a bancada existente')
caixa_inferior(it, [61.5] * 4, 70, 56)
bascula_baixo(it, 3, 61.1, 34.6)
gavetas(it, 4, 61.1, 34.6, 50, rotulo='Gavetão')
gavetas(it, 2, 61.1, 17.1, 50, rotulo='Gaveta')
soculo(it, 246, 56, 10)

it = item('Gourmet', 'Armários inferiores da parede da torre', '132 × 70 × 40',
          'elevação B: 2 × 66 · frente de 70 · prof. pela bancada de 42')
caixa_inferior(it, [66, 66], 70, 40)
gavetas(it, 4, 65.6, 34.6, 35, rotulo='Gavetão')
soculo(it, 132, 40, 10)

it = item('Gourmet', 'Nicho e armário superior com básculas', '192 × 94 × 30',
          'elevação B: nicho de 60 + armário de 132 · 89 + 5 de acabamento · prof. 30')
P(it, 'Lateral de ponta', 'Freijó 18', 89, 30, 2, FR18, 0.89 + 0.30)
P(it, 'Divisória do nicho', 'Freijó 18', 85.4, 30, 1, FR18, 0.854)
P(it, 'Nicho · base, teto e prateleira', 'Freijó 18', 56.4, 30, 3, FR18, 0.564)
P(it, 'Nicho · fundo', 'Freijó 6', 85.4, 56.4, 1, FR6)
P(it, 'Armário · base', 'Freijó: é vista por baixo', 128.4, 30, 1, FR18, 1.284)
P(it, 'Armário · horizontal do meio', 'Freijó: aparece entre as básculas', 128.4, 28, 1, FR18, 1.284)
P(it, 'Armário · teto', '', 128.4, 30, 1, BR15, 1.284)
P(it, 'Armário · divisória', '', 85.4, 28, 1, BR15, 0.854)
P(it, 'Armário · fundo', 'encaixe em rasgo', 128.4, 85.4, 1, BR6)
P(it, 'Báscula', 'abre para cima · Freijó 15', 65.8, 41.3, 4, FR15, 2 * (65.8 + 41.3) / 100)
F(it, 'Articulador de báscula', 'um por frente · equivalente Häfele a cotar', 4, 'un',
  'Báscula HK-XS')
cava(it, [65.8] * 4)
P(it, 'Acabamento superior', 'faixa de 5 até o forro', 192, 5, 1, FR15, 1.92)

it = item('Gourmet', 'Torre quente', '95 × 254 × 60',
          'elevação B: 5 + 75 + 10 + 39 + 10 + 60 + 10 + 35 + 10 = 254 · requadros de 17,5 nas '
          'laterais dos eletros')
P(it, 'Lateral aparente', 'Freijó 15', 239, 58, 1, FR15, 2.39 + 0.58)
P(it, 'Lateral de parede', '', 239, 58, 1, BR15, 2.39)
P(it, 'Base e teto', '', 92, 58, 2, BR15, 0.92)
P(it, 'Horizontal fixa', 'sob o armário, sob e entre os eletros', 92, 55, 3, BR15, 0.92)
P(it, 'Apoio do forno', '18 mm', 92, 55, 1, BR18, 0.92)
prateleiras(it, 1, 92, 58)
P(it, 'Fundo do armário superior', 'encaixe em rasgo', 92, 75, 1, BR6)
giro(it, 2, 47.3, 74.6, frente=FR15)
P(it, 'Requadro horizontal', 'as faixas de 10 entre os eletros', 94.6, 10, 3, FR15,
  2 * (94.6 + 10) / 100)
P(it, 'Requadro vertical', 'as faixas de 17,5 dos lados dos eletros', 109, 17.5, 2, FR15,
  2 * (109 + 17.5) / 100)
gavetas(it, 1, 94.6, 34.6, 50, frente=FR15, rotulo='Gavetão')
P(it, 'Acabamento superior', 'faixa de 5 até o forro', 95, 5, 1, FR15, 0.95)
soculo(it, 92, 58, 10)

AMBIENTES = ['Cozinha', 'Gourmet']
