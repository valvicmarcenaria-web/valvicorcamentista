# -*- coding: utf-8 -*-
"""GRAN ROYALLE · CORSINO SOARES — levantamento  [11/11/2026]
Caderno de marcenaria de Jéssica Sollero Interiores, 06/11/2026, 46 pranchas A4
1/25, cotadas. "Conferir medidas no local."

Materiais da prancha (todos Arauco):
  · GRISS CHESS — rack, cristaleira, cozinha (inferiores e ilha), lavanderia, gourmet;
  · ESCARLATE (amadeirado) — painéis, prateleiras grossas, torre quente e
    superiores da cozinha, despensa, cabeceiras;
  · FRAPÊ — suítes 01, 02 e master, banhos e closet;
  · interno em BRANCO TX.
  Todas orçadas no preço da linha de cor (550 a de 15, 700 a de 18, 350 a de 6).

As três linhas da casa (Telescópica · Hettich · Blum): o levantamento lança a
HETTICH (dobradiça Novisys R$ 50, corrediça R$ 150 o par) e o precos.py troca só
corrediça e dobradiça.

⛔ PEDRA NUNCA É NOSSA: bancadas, rodabancas, ilha, frente dos sóculos, o fundo
   em Atacama Branca da adega, tampos dos banhos. Eletros, cubas, metais,
   churrasqueira, box, adega de garrafas em pé: fora.
⚠ Cada premissa vai numerada em DUVIDAS.

Peça: (nome, C, L, QTD, chave, fita m/peça) · ferragem/terceiro: (nome, QTD, chave)
· por m²: (nome, C, L, QTD, chave).
"""
ITENS = []
GC15, GC18 = 'MDF Griss Chess 15', 'MDF Griss Chess 18'
ES15, ES18 = 'MDF Escarlate 15', 'MDF Escarlate 18'
FR15, FR18 = 'MDF Frapê 15', 'MDF Frapê 18'
BR15, BR18, BR6 = 'MDF Branco TX 15', 'MDF Branco TX 18', 'MDF Branco TX 6'


def item(amb, movel, medida, linha=True):
    d = dict(amb=amb, movel=movel, medida=medida, pecas=[], ferr=[], m2=[])
    ITENS.append(d); return d


def P(it, nome, c, l, q, k, fita=None):
    if fita is None: fita = 2 * (c + l) / 100          # padrão: as quatro arestas
    it['pecas'].append((nome, c, l, q, k, fita))


def F(it, nome, q, k): it['ferr'].append((nome, q, k))
def M2(it, nome, c, l, q, k): it['m2'].append((nome, c, l, q, k))


def ndob(a): return 2 if a <= 90 else 3 if a <= 160 else 4 if a <= 200 else 5


def puxador(it, larg, tipo):
    """chanfrado e cava: usinagem por metro de frente · espaçado: nada (é a folga)"""
    if tipo in ('chanfrado', 'cava'):
        F(it, f'Puxador {tipo} usinado (m)', round(larg / 100, 2), 'Cava usinada')


def caixa(it, L, A, P_, ext, ndiv=0, base_ext=False, topo_ext=False, lat_ext=2, fundo=True):
    """Caixaria: laterais aparentes na cor, divisórias, base e teto em Branco."""
    P(it, 'Lateral aparente', A, P_, lat_ext, ext, (A + P_) / 100) if lat_ext else None
    if lat_ext < 2: P(it, 'Lateral de encosto', A, P_, 2 - lat_ext, BR15, A / 100)
    if ndiv: P(it, 'Divisória', A - 3, P_ - 1, ndiv, BR15, (A - 3) / 100)
    P(it, 'Base', L - 3, P_, 1, ext if base_ext else BR15, (L - 3) / 100)
    P(it, 'Teto', L - 3, P_, 1, ext if topo_ext else BR15, (L - 3) / 100)
    if fundo: P(it, 'Fundo', L - 2, A - 2, 1, BR6, 0)


def giro(it, n, l, a, mat, pux='chanfrado'):
    P(it, 'Porta de giro', a, l, n, mat)
    F(it, 'Dobradiça', ndob(a) * n, 'Dobradiça Hettich')
    for _ in range(n): puxador(it, l, pux)


def gavetas(it, n, l, a, prof, frente, pux='chanfrado', nome='Gaveta'):
    li = l - 6.6
    P(it, f'{nome} · frente', l, a, n, frente)
    P(it, f'{nome} · lateral da caixa', prof - 5, a - 5, 2 * n, BR15, (prof - 5) / 100)
    P(it, f'{nome} · frente e traseira', li, a - 5, 2 * n, BR15, li / 100)
    P(it, f'{nome} · fundo', li + 1, prof - 6, n, BR6, 0)
    F(it, f'Corrediça · {nome.lower()}', n, 'Corrediça Hettich')
    for _ in range(n): puxador(it, l, pux)


def bascula_baixo(it, l, a, mat):
    P(it, 'Báscula (abre para baixo)', l, a, 1, mat)
    F(it, 'Dobradiça', 2, 'Dobradiça Hettich'); F(it, 'Pistão a gás', 2, 'Pistão com amortecimento')
    puxador(it, l, 'chanfrado')


def prat(it, n, vao, prof, k=BR15):
    P(it, 'Prateleira', vao - 0.4, prof - 3, n, k, vao / 100)
    F(it, 'Suporte de prateleira (jogo)', n, 'Suporte de prateleira')


def prat_grossa(it, n, L, prof, mat, led=True, invis=True):
    """Prateleira de 5 de espessura: duas faces de 15 + frente e topos, meia esquadria."""
    P(it, 'Prateleira grossa · face', L, prof, 2 * n, mat, 0)
    P(it, 'Prateleira grossa · frente e topos', L + 2 * prof, 5, n, mat, 2 * (L + 2 * prof) / 100)
    P(it, 'Prateleira grossa · enchimento', L, 10, n, BR15, 0)
    if invis: F(it, 'Fixação invisível (un)', n * max(2, round(L / 50)), 'Fixação invisível')
    if led:
        F(it, 'LED sob a prateleira (m)', round(n * L / 100, 2), 'LED conjunto')


def painel(it, L, A, mat, nome='Painel de parede'):
    """Painel na parede: chapa de 18 na cor + sarrafos de fixação a cada 60."""
    import math
    fl = math.ceil(L / 120)
    P(it, nome, A, L / fl, fl, mat, 2 * A / 100)
    P(it, 'Sarrafo de fixação', A, 10, math.ceil(L / 60) + 1, BR15, 0)
    F(it, 'Perfil de alumínio na base (m)', round(L / 100, 2), 'Perfil de proteção de piso')


def porta_passagem(it, l, a, mat, tipo):
    """Folha de passagem no painel: duas chapas de 18 (frente na cor, costas em
    Branco) + o kit. ⚠ PREMISSA: costas em Branco TX."""
    P(it, f'Porta {tipo} · face', a, l, 1, mat)
    P(it, f'Porta {tipo} · contraface', a, l, 1, BR18)
    F(it, 'Puxador cava (m)', round(a / 100 * 0.3, 2), 'Cava usinada')
    F(it, f'Kit de porta de {tipo} de passagem', 1,
      'Kit porta de correr de passagem' if tipo == 'correr' else 'Kit porta de giro embutida')


def soculo(it, L, prof):
    P(it, 'Sóculo · estrutura (frente é pedra)', L, 12, 2, BR15, 0)
    P(it, 'Sóculo · travessa', prof - 13, 12, max(2, round(L / 60) + 1), BR15, 0)


def gaveteiro_roupeiro(it, n, l, prof, mat, a=18):
    gavetas(it, n, l, a, prof, mat, pux='espaçado')


# ══ 01 · SALA ESTAR E TV ═════════════════════════════════════════════════
it = item('Sala estar e TV', 'Rack suspenso', '180 × 40 × 40')
P(it, 'Tampo e base', 180, 40, 2, GC18)
P(it, 'Fixo da ponta · arredondado R20', 40, 20, 2, GC18)
P(it, 'Divisória', 36, 38, 3, BR15, 0.36)
P(it, 'Fundo', 178, 38, 1, BR6, 0)
gavetas(it, 2, 45, 36, 38, GC15, nome='Gavetão')
P(it, 'Nicho · tampos e fundo em meia esquadria', 50, 38, 3, GC15)
F(it, 'Ponta boleada', 2, 'Canto boleado')
F(it, 'Fixação do rack suspenso (jogo)', 1, 'Fixação invisível')

# ══ 02 · SALA DE JANTAR ══════════════════════════════════════════════════
it = item('Sala de jantar', 'Cristaleira com portas de vidro', '100 × 272 × 60')
caixa(it, 100, 272, 60, GC18, base_ext=True, topo_ext=True)
P(it, 'Forro interno em Escarlate (laterais, fundo e teto)', 266, 58, 2, ES15, 0)
P(it, 'Forro interno do fundo', 266, 96, 1, ES15, 0)
gavetas(it, 3, 96, 20, 55, GC15, pux='espaçado', nome='Gaveta')
M2(it, 'Porta em vidro reflecta bronze, alumínio slim champagne', 50, 205, 2, 'Porta de vidro reflecta bronze')
F(it, 'Dobradiça para porta de alumínio', 8, 'Dobradiça Hettich')
F(it, 'Puxador Sotille champagne', 2, 'Puxador Sotille')
M2(it, 'Prateleira de vidro', 95, 55, 5, 'Prateleira de vidro')
F(it, 'LED lateral 3000K (m)', 4.2, 'LED conjunto'); F(it, 'Fonte de LED', 1, 'Fonte de LED')

it = item('Sala de jantar', 'Painel da adega com suporte de vinhos', '260 × 280')
P(it, 'Moldura · laterais em meia esquadria', 280, 12, 2, ES18)
P(it, 'Moldura · topo e base em meia esquadria', 256, 12, 2, ES18)
P(it, 'Moldura · requadro frontal', 280, 5, 4, ES18)
F(it, 'Suporte de vinhos, haste preta', 4, 'Suporte de vinhos')

it = item('Sala de jantar', 'Painel com porta de correr da despensa', '95 × 280')
painel(it, 95, 280, ES18)
porta_passagem(it, 82, 210, ES18, 'correr')

# ══ 03 · COZINHA ═════════════════════════════════════════════════════════
it = item('Cozinha', 'Ilha · armários com gavetas e porta-temperos', '190 × 72 × 60')
caixa(it, 190, 72, 58, GC15, ndiv=2, lat_ext=0)
P(it, 'Lateral de encosto', 72, 58, 2, BR15, 0.72)
gavetas(it, 8, 80, 18, 55, GC15)
P(it, 'Porta-temperos · frente', 30, 72, 1, GC15)
P(it, 'Porta-temperos · bandejas e laterais', 50, 26, 5, BR15, 0.5)
F(it, 'Corrediça · porta-temperos', 1, 'Corrediça Hettich'); puxador(it, 30, 'chanfrado')
soculo(it, 190, 58)

it = item('Cozinha', 'Inferior da pia com báscula e gavetões', '170 × 72 × 65')
caixa(it, 170, 72, 63, GC15, ndiv=1, lat_ext=0)
P(it, 'Lateral de encosto', 72, 63, 2, BR15, 0.72)
bascula_baixo(it, 100, 36, GC15)
gavetas(it, 1, 100, 36, 55, GC15, nome='Gavetão')
gavetas(it, 2, 70, 36, 55, GC15, nome='Gavetão')
soculo(it, 170, 63)

it = item('Cozinha', 'Prateleiras e fundo da pia com LED', '170 × 188')
painel(it, 170, 123, ES18, 'Fundo em Escarlate sobre a rodabanca')
prat_grossa(it, 3, 170, 35, ES15)
F(it, 'Fonte de LED', 1, 'Fonte de LED')

it = item('Cozinha', 'Torre quente com armário superior', '68 × 280 × 65')
caixa(it, 68, 280, 65, ES18, fundo=True)
P(it, 'Horizontal dos nichos dos eletros', 65, 63, 3, BR15, 0.65)
giro(it, 1, 64, 78, ES15)
prat(it, 1, 64, 63)

it = item('Cozinha', 'Armário sobre a geladeira e laterais', '99 × 280 × 65')
P(it, 'Lateral da geladeira, piso ao teto', 280, 65, 2, ES18, 3.45)
caixa(it, 99, 80, 65, ES15, lat_ext=0)
giro(it, 2, 49, 80, ES15)

it = item('Cozinha', 'Painel com porta de correr da lavanderia', '117 × 280')
painel(it, 117, 280, ES18)
porta_passagem(it, 82, 210, ES18, 'correr')

it = item('Cozinha', 'Painel da parede da escada (elevação C)', '350 × 275')
painel(it, 349.5, 275, ES18)

it = item('Cozinha', 'Painel com porta de giro do lavabo', '142 × 280')
painel(it, 142, 280, ES18)
porta_passagem(it, 82, 210, ES18, 'giro')

# ══ 04 · DESPENSA ════════════════════════════════════════════════════════
it = item('Despensa', 'Prateleiras em L com LED', '165 + 119,5 × 50 · 5 níveis')
prat_grossa(it, 5, 165, 50, ES15)
prat_grossa(it, 5, 119.5, 50, ES15)
F(it, 'Fonte de LED', 1, 'Fonte de LED')

# ══ 05 · LAVANDERIA ══════════════════════════════════════════════════════
it = item('Lavanderia', 'Armário superior com cabideiro', '200 × 75 × 35')
caixa(it, 200, 75, 35, GC15, ndiv=4, base_ext=True)
prat(it, 5, 40, 35)
giro(it, 5, 40, 75, GC15)
F(it, 'Cabideiro metálico', 2, 'Cabideiro')

it = item('Lavanderia', 'Inferior da cuba com báscula e gavetão', '65 × 72 × 61')
caixa(it, 65, 72, 61, GC15, lat_ext=1)
bascula_baixo(it, 65, 36, GC15)
gavetas(it, 1, 65, 36, 55, GC15, nome='Gavetão')
soculo(it, 65, 61)

it = item('Lavanderia', 'Torre de vassouras e utilidades', '90 × 262 × 61')
caixa(it, 90, 262, 61, GC15)
prat(it, 4, 90, 61, BR18)
giro(it, 2, 45, 262, GC15)

# ══ 06 · ESPAÇO GOURMET ══════════════════════════════════════════════════
it = item('Espaço gourmet', 'Inferior da pia com portas e gaveteiro', '220 × 72 × 65')
caixa(it, 220, 72, 63, GC15, ndiv=2, lat_ext=1)
prat(it, 2, 75, 63)
giro(it, 4, 37.5, 72, GC15)
gavetas(it, 4, 70, 18, 55, GC15)
soculo(it, 220, 63)

it = item('Espaço gourmet', 'Prateleiras com LED', '220 e 150 × 35')
prat_grossa(it, 1, 220, 35, ES15)
prat_grossa(it, 1, 150, 35, ES15)
F(it, 'Fonte de LED', 1, 'Fonte de LED')

# ══ 07 · SUÍTE 01 ════════════════════════════════════════════════════════
it = item('Suíte 01', 'Roupeiro com portas de correr em vidro reflecta', '305,5 × 280 × 60')
caixa(it, 305.5, 274, 60, FR18, ndiv=2, lat_ext=2)
P(it, 'Maleiro', 99, 57, 3, BR18, 0.99)
P(it, 'Prateleira sobre gaveteiro', 99, 57, 3, BR18, 0.99)
F(it, 'Cabideiro metálico', 4, 'Cabideiro')
P(it, 'Divisória do gaveteiro e da sapateira', 80, 55, 2, BR15, 0.8)
P(it, 'Sapateira com corrediça', 49, 45, 4, BR15, 0.49)
F(it, 'Corrediça · sapateira', 4, 'Corrediça Hettich')
gaveteiro_roupeiro(it, 8, 49.5, 55, FR15)
gaveteiro_roupeiro(it, 4, 60, 55, FR15)
M2(it, 'Porta de correr em vidro reflecta bronze, alumínio slim champagne', 100, 274, 3, 'Porta de vidro reflecta bronze')
F(it, 'Sistema de correr 3 folhas de vidro', 1, 'Sistema de correr 3 folhas')
F(it, 'Puxador Sotille champagne', 3, 'Puxador Sotille')

it = item('Suíte 01', 'Cabeceira com brise e estofado, painel e mesa de cabeceira', '235,5 × 280')
painel(it, 235.5, 280, ES18, 'Painel de fundo da cabeceira')
P(it, 'Lâmina do brise · giro de 20°', 140, 19.5, 9, ES18)
P(it, 'Brise · requadro fixo', 140, 20, 2, ES18)
F(it, 'Pino de giro do brise', 18, 'Pino de brise')
P(it, 'Base do estofado R20', 215.5, 110, 1, BR15, 0)
M2(it, 'Estofado em linho terracota', 215.5, 110, 1, 'Estofado')
P(it, 'Mesa de cabeceira · caixa', 40, 40, 4, FR15)
gavetas(it, 2, 40, 15, 35, FR15)

# ══ 08 · BANHO SUÍTE 01 ══════════════════════════════════════════════════
it = item('Banho suíte 01', 'Gabinete suspenso', '140 × 90 × 35')
caixa(it, 140, 70, 35, FR15, ndiv=1, base_ext=True)
bascula_baixo(it, 95, 28, FR15)
gavetas(it, 1, 95, 27, 32, FR15, nome='Gavetão')
gavetas(it, 3, 45, 18, 32, FR15)
it = item('Banho suíte 01', 'Armário superior com portas de espelho e LED', '140 × 160 × 15')
caixa(it, 140, 157, 15, FR15, ndiv=1, base_ext=True)
prat(it, 10, 60, 15)
M2(it, 'Porta de espelho prata em alumínio', 40, 157, 3, 'Porta de espelho em alumínio')
F(it, 'Dobradiça', 9, 'Dobradiça Hettich')
F(it, 'LED frontal 4000K (m)', 3.2, 'LED conjunto'); F(it, 'Fonte de LED', 1, 'Fonte de LED')

# ══ 09 · SUÍTE 02 ════════════════════════════════════════════════════════
it = item('Suíte 02', 'Roupeiro com porta de correr e porta de espelho', '200 × 280 × 60')
caixa(it, 200, 274, 60, FR18, ndiv=1)
P(it, 'Maleiro', 97, 57, 2, BR18, 0.97)
P(it, 'Prateleira', 97, 57, 2, BR18, 0.97)
F(it, 'Cabideiro metálico', 3, 'Cabideiro')
P(it, 'Sapateira com corrediça', 97, 45, 3, BR15, 0.97)
F(it, 'Corrediça · sapateira', 3, 'Corrediça Hettich')
gaveteiro_roupeiro(it, 4, 48.5, 55, FR15)
P(it, 'Porta de correr em Frapê', 274, 98, 1, FR18)
F(it, 'Desempenador de porta', 2, 'Desempenador de porta')
M2(it, 'Porta de correr de espelho prata em alumínio', 98, 274, 1, 'Porta de espelho em alumínio')
F(it, 'Sistema de correr Dominus', 1, 'Sistema de correr Dominus')
F(it, 'Puxador Sotille champagne', 2, 'Puxador Sotille')

it = item('Suíte 02', 'Painel com porta de giro do banho', '350 × 280')
painel(it, 350, 280, FR18)
porta_passagem(it, 82, 210, FR18, 'giro')

it = item('Suíte 02', 'Bancada com gavetas e prateleiras', '150 × 45 · gavetas · 2 prateleiras de 155')
P(it, 'Bancada · tampo e fundo (10 de espessura)', 150, 45, 2, FR15)
P(it, 'Bancada · frente e topos', 240, 10, 1, FR15)
gavetas(it, 3, 50, 10, 40, FR15)
prat_grossa(it, 2, 155, 25, FR15, led=False)

it = item('Suíte 02', 'Cabeceira em Escarlate e mesa de cabeceira', '173 × 110 · mesa de 50')
P(it, 'Cabeceira em Escarlate, borda arredondada', 173, 110, 1, ES18)
P(it, 'Cabeceira · contraplaca', 173, 110, 1, BR15, 0)
P(it, 'Mesa de cabeceira · caixa', 50, 40, 4, FR15)
gavetas(it, 2, 50, 15, 35, FR15)

# ══ 10 · BANHO SUÍTE 02 ══════════════════════════════════════════════════
it = item('Banho suíte 02', 'Gabinete suspenso', '120 × 90 × 50')
caixa(it, 120, 70, 50, FR15, ndiv=1, base_ext=True)
bascula_baixo(it, 85, 28, FR15)
gavetas(it, 1, 85, 27, 45, FR15, nome='Gavetão')
gavetas(it, 3, 35, 18, 45, FR15)
it = item('Banho suíte 02', 'Armário superior com portas de espelho e LED', '120 × 160 × 15')
caixa(it, 120, 157, 15, FR15, ndiv=1, base_ext=True)
prat(it, 10, 50, 15)
M2(it, 'Porta de espelho prata em alumínio', 33.5, 157, 3, 'Porta de espelho em alumínio')
F(it, 'Dobradiça', 9, 'Dobradiça Hettich')
F(it, 'LED frontal 4000K (m)', 3.2, 'LED conjunto'); F(it, 'Fonte de LED', 1, 'Fonte de LED')

# ══ 11 · SUÍTE MASTER ════════════════════════════════════════════════════
it = item('Suíte master', 'Cabeceira estofada e mesas de cabeceira', '370 × 110')
P(it, 'Base do estofado', 216, 110, 1, BR15, 0)
M2(it, 'Estofado em linho', 216, 110, 1, 'Estofado')
P(it, 'Mesa de cabeceira · painel de fundo', 75, 110, 2, FR15)
P(it, 'Mesa de cabeceira · caixa', 75, 40, 4, FR15)
gavetas(it, 4, 75, 15, 35, FR15)

it = item('Suíte master', 'Painel revestido de espelho com porta de correr', '290 × 280')
painel(it, 290, 280, FR18)
porta_passagem(it, 82, 210, FR18, 'correr')
M2(it, 'Espelho colado no painel e na porta', 290, 275, 1, 'Espelho colado')

it = item('Suíte master', 'Prateleiras com pontas arredondadas', '380 e 150 × 25')
prat_grossa(it, 1, 380, 25, ES15, led=False)
prat_grossa(it, 1, 150, 25, ES15, led=False)
F(it, 'Ponta arredondada R20', 2, 'Canto boleado')

it = item('Suíte master', 'Penteadeira e gaveteiro', '100 × 50 · gaveteiro 70 × 30')
P(it, 'Penteadeira · tampo e fundo (10)', 100, 50, 2, FR15)
gavetas(it, 2, 50, 10, 45, FR15)
M2(it, 'Tampo de vidro incolor temperado', 100, 50, 1, 'Vidro temperado')
F(it, 'Divisória interna em acrílico', 2, 'Divisória de acrílico')
P(it, 'Gaveteiro · caixa, canto arredondado', 70, 45, 4, FR15)
gavetas(it, 1, 50, 30, 42, FR15, nome='Gavetão')
F(it, 'Canto arredondado', 1, 'Canto boleado')

# ══ 12 · BANHO MASTER ════════════════════════════════════════════════════
it = item('Banho master', 'Gabinete suspenso com tulhas', '120 × 90 × 45')
caixa(it, 120, 70, 45, FR15, ndiv=2, base_ext=True)
P(it, 'Tulha · frente', 35, 55, 2, FR15)
F(it, 'Kit de tulha basculante com cesto', 2, 'Kit tulha')
puxador(it, 70, 'chanfrado')
bascula_baixo(it, 50, 28, FR15)
gavetas(it, 1, 50, 27, 42, FR15, nome='Gavetão')
it = item('Banho master', 'Armário superior com portas de correr de espelho e LED', '208 × 160 × 15')
caixa(it, 208, 157, 15, FR15, ndiv=1, base_ext=True)
prat(it, 10, 91, 15)
M2(it, 'Porta de correr de espelho prata em alumínio', 94, 157, 2, 'Porta de espelho em alumínio')
F(it, 'Sistema de correr leve', 1, 'Sistema de correr leve')
F(it, 'LED frontal 4000K (m)', 3.2, 'LED conjunto'); F(it, 'Fonte de LED', 1, 'Fonte de LED')

# ══ 13 · CLOSET MASTER ═══════════════════════════════════════════════════
it = item('Closet master', 'Closet aberto em L, sem portas', '315 + 155 × 280 × 60')
caixa(it, 315, 274, 60, FR18, ndiv=3)
caixa(it, 155, 274, 60, FR18, ndiv=1, lat_ext=1)
P(it, 'Maleiro', 83, 57, 6, BR18, 0.83)
P(it, 'Prateleira', 83, 57, 3, BR18, 0.83)
F(it, 'Cabideiro metálico', 7, 'Cabideiro')
F(it, 'LED sob o maleiro (m)', 4.7, 'LED conjunto'); F(it, 'Fonte de LED', 1, 'Fonte de LED')
gaveteiro_roupeiro(it, 4, 41, 55, FR15, a=21)
gaveteiro_roupeiro(it, 4, 83, 55, FR15, a=21)
P(it, 'Sapateira com corrediça', 65, 45, 7, BR15, 0.65)
F(it, 'Corrediça · sapateira', 7, 'Corrediça Hettich')

AMBIENTES = list(dict.fromkeys(i['amb'] for i in ITENS))

DUVIDAS = [
 'Hall, varanda da master e lavabo aparecem na apresentação, mas o caderno não tem prancha de marcenaria para eles: fora desta conta.',
 'Griss Chess, Escarlate e Frapê (Arauco) orçados no preço da linha de cor (550 / 700 / 350). Se o Escarlate for linha madeirada mais cara, a conta sobe.',
 'Portas de passagem nos painéis (despensa, lavanderia, lavabo, banho da suíte 02, closet master): folha em duas chapas de 18, kit de correr R$ 700 e de giro embutida R$ 450 — A COTAR.',
 'Suporte de vinhos com haste preta: 4 hastes a R$ 450 cada — é serralheria/acessório; confirmar se é nosso ou da arquiteta.',
 'Roupeiro da suíte 01: três folhas de vidro reflecta de 100 × 274 em alumínio slim — altura grande para vidro de correr; sistema de 3 folhas a R$ 1.200, A COTAR com o vidraceiro.',
 'Painel da master: a nota diz espelho BRONZE e o desenho diz espelho PRATA. Lançado espelho colado a R$ 650 o m².',
 'Prateleiras de 5 de espessura (cozinha, despensa, gourmet, suítes): duas faces de 15 com enchimento e meia esquadria; fixação invisível a R$ 35 cada.',
 'LED: R$ 150 o metro instalado + fonte por ambiente. A despensa sozinha tem 14 metros (5 níveis em L).',
 'Puxador chanfrado lançado como usinagem por metro (R$ 50, a chave da cava). Puxador Sotille champagne a R$ 90 a peça — A COTAR.',
 'Tulha basculante com cesto no banho master: kit a R$ 250 cada; tampo de vidro temperado da penteadeira a R$ 400 o m²; divisória em acrílico a R$ 180 por gaveta.',
 'Prancha 19 a 21 (gourmet) está com o carimbo "Banho suíte 01" e a 22 a 24 (suíte 01) com "Banho master": li pelo desenho, não pelo carimbo.',
 'Brise da suíte 01 com giro de 20°: lâminas fixas no ângulo, dois pinos por lâmina.',
]
