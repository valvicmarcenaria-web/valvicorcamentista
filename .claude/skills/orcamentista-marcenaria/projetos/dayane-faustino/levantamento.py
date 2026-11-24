# -*- coding: utf-8 -*-
"""DAYANE FAUSTINO — suíte (quarto e banheiro) · levantamento  [24/11/2026]
Projeto executivo da designer Rubia Nascimento, 10/2026: quarto em 8 pranchas, banheiro em 5. Belo Horizonte.
Tudo em MDF Nogueira Âmbar (Guararapes), no preço da linha de cor. Palha sextavada com fundo em MDF nas portas
de baixo do roupeiro e nas gavetas das mesas laterais. Puxador ponto dourado / latão.
⛔ Fora: granito da bancada, cuba, metais, box, espelho, revestimentos, pintura, móveis e decoração de loja.
"""
ITENS = []
BR15, BR18, BR6 = 'MDF Branco TX 15', 'MDF Branco TX 18', 'MDF Branco TX 6'
NA15, NA18 = 'MDF Nogueira Âmbar 15', 'MDF Nogueira Âmbar 18'


def pux(it, n, k='Puxador Zen Design'): F(it, 'Puxador ponto dourado', n, k)

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




def ripado(it, L, A, mat, ripa=3, vao=2, base=True, nome='Ripado'):
    """Ripas de MDF 18 sobre base: ripa de face `ripa`, vão `vao`."""
    n = int(L // (ripa + vao)) + 1
    if base: P(it, f'{nome} · base', A, L, 1, mat, 0)
    P(it, f'{nome} · ripas', A, ripa, n, mat, 2 * A / 100)
    F(it, f'{nome} · usinagem das ripas (un)', n, 'Usinagem de ripa')


def almofadar(it, n):
    F(it, 'Usinagem de frente almofadada (un)', n, 'Usinagem almofadada')


def pux(it, n, k='Puxador Zen Design'):
    F(it, 'Puxador (peça)', n, k)


def interno(it, larg, prof=57, prat=0, cab=0, gav=(), sap=0, sap_larg=None, calc=0, frente=None, k=BR15):
    if prat: P(it, 'Prateleira / maleiro', larg, prof, prat, BR18 if larg > 70 else k, larg / 100)
    if cab: F(it, 'Cabideiro metálico', cab, 'Cabideiro')
    for a, l in gav: gavetas(it, 1, l, a, prof - 2, frente or k, pux='espaçado')
    if sap:
        P(it, 'Sapateira', sap_larg or larg, prof - 12, sap, k, (sap_larg or larg) / 100)
        F(it, 'Corrediça · sapateira', sap, 'Corrediça Hettich')
    if calc: F(it, 'Calceiro', calc, 'Calceiro')


def pes(it, n=1): F(it, 'Pés de serralheria (jogo)', n, 'Pé metálico')


def led(it, m, fonte=True):
    F(it, 'LED (m)', m, 'LED conjunto')
    if fonte: F(it, 'Fonte de LED', 1, 'Fonte de LED')



# ══ QUARTO ═══════════════════════════════════════════════════════════════
it = item('Quarto', 'Roupeiro com palha nas portas de baixo', '164 × 256 × 62')
caixa(it, 164, 252, 59, NA18, ndiv=1)
P(it, 'Maleiro e prateleiras', 105, 57, 3, NA18, 1.05)
F(it, 'Cabideiro oval', 2, 'Cabideiro')
gavetas(it, 4, 107, 20, 55, NA18, pux='espaçado')
P(it, 'Sapateira deslizante', 51, 45, 3, NA15, 0.51); F(it, 'Corrediça · sapateira', 3, 'Corrediça Hettich')
giro(it, 3, 54.5, 60, NA18, pux='')
P(it, 'Porta alta · quadro', 192, 54.5, 3, NA18)
F(it, 'Dobradiça', 12, 'Dobradiça Hettich')
F(it, 'Usinagem do quadro da porta', 3, 'Usinagem almofadada')
M2(it, 'Palha sextavada com fundo em MDF', 50, 76, 3, 'Palha natural')
pux(it, 6)
it = item('Quarto', 'Cabeceira em painéis frisados e cabeceira estofada', '368 × 95 · estofada 158 × 105')
painel(it, 368, 95, NA18, 'Cabeceira em painéis'); F(it, 'Frisos de 1 cm', 3.6, 'Cava usinada')
P(it, 'Caixa da cabeceira (área da persiana)', 368, 10, 2, NA18, 7.4)
P(it, 'Base da cabeceira estofada', 158, 105, 1, BR15, 0)
M2(it, 'Estofado listrado, espuma D23', 158, 105, 1.4, 'Estofado')
it = item('Quarto', 'Escrivaninha suspensa e prateleira', '150 × 10 × 45 · 250 × 2 × 25')
caixa(it, 150, 10, 45, NA18, ndiv=2, base_ext=True, topo_ext=True)
gavetas(it, 3, 50, 8, 40, NA15, pux='cava'); F(it, 'Moldura de 2 cm', 1, 'Usinagem almofadada')
P(it, 'Prateleira com ponta arredondada', 250, 25, 1, NA18, 5.5)
F(it, 'Ponta arredondada', 1, 'Canto boleado'); F(it, 'Suporte oculto', 4, 'Fixação invisível')
it = item('Quarto', 'Mesas laterais com palha e pés dourados', '2 × 45 × 55 × 35')
for _ in range(2):
    caixa(it, 45, 30, 35, NA18, base_ext=True, topo_ext=True)
    P(it, 'Prateleira inferior', 41, 33, 1, NA18, 0.41)
gavetas(it, 4, 39, 15, 30, NA15, pux='')
M2(it, 'Palha sextavada nas gavetas', 35, 11, 4, 'Palha natural')
pux(it, 4); F(it, 'Pés em perfil metálico dourado (jogo)', 2, 'Pé metálico')

# ══ BANHEIRO ═════════════════════════════════════════════════════════════
it = item('Banheiro', 'Bancada com portas e gavetas em quadriculado vazado', '140 × 58 × 50')
caixa(it, 140, 58, 48, NA18, ndiv=1, base_ext=True)
giro(it, 4, 31, 34, NA18, pux='')
gavetas(it, 2, 65, 16, 44, NA18, pux='')
F(it, 'Corte a laser do quadriculado vazado', 2, 'Usinagem CNC muxarabi')
prat(it, 2, 65, 46); pux(it, 6)

AMBIENTES = list(dict.fromkeys(i['amb'] for i in ITENS))
