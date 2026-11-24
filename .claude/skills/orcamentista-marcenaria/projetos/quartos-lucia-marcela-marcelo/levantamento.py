# -*- coding: utf-8 -*-
"""QUARTOS LUCIA, MARCELA E MARCELO — levantamento PRELIMINAR de material  [24/11/2026]
Quatro pranchas A3 (CAD), sem carimbo, sem cliente, sem material especificado. Referência enviada pelo cliente:
roupeiro claro com a ponta de prateleiras abertas arredondadas em madeira.
⚠ PREMISSAS até as pendências serem respondidas: caixa e portas em MDF de cor 18 mm, interno Branco TX,
  prateleiras de 2,5 lidas como MDF 25 (chapa de 25 no preço de 18 + 20%), profundidade dos roupeiros 60.
⛔ Sem preço: este arquivo só conta material.
"""
ITENS = []
BR15, BR18, BR6 = 'MDF Branco TX 15', 'MDF Branco TX 18', 'MDF Branco TX 6'
CO15, CO18, CO25 = 'MDF cor 15', 'MDF cor 18', 'MDF cor 25'
MA18 = 'MDF madeirado 18'

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



# ══ QUARTO LUCIA ═════════════════════════════════════════════════════════
it = item('Quarto Lucia', 'Roupeiro de correr, 3 folhas (central com espelho)', '285 × 280 × 60')
caixa(it, 285, 270, 60, CO18, ndiv=2)
P(it, 'Prateleiras de 2,5', 92, 57, 8, CO25, 0.92)
F(it, 'Cabideiro (tubo)', 2, 'Cabideiro')
gavetas(it, 8, 92, 20, 55, BR15, pux='espaçado')
P(it, 'Sapateira', 92, 45, 2, BR15, 0.92); F(it, 'Corrediça · sapateira', 2, 'Corrediça Hettich')
P(it, 'Porta de correr', 270, 95, 2, CO18); M2(it, 'Porta de correr com espelho', 95, 270, 1, 'Porta de espelho em alumínio')
F(it, 'Sistema de correr 3 folhas', 1, 'Sistema de correr 3 folhas'); F(it, 'Desempenador', 4, 'Desempenador de porta')
P(it, 'Rodapé e faixa superior (5)', 285, 5, 2, CO18)

# ══ QUARTO MARCELA ═══════════════════════════════════════════════════════
it = item('Quarto Marcela', 'Roupeiro de correr, 3 folhas', '285 × 280 × 60')
caixa(it, 285, 270, 60, CO18, ndiv=2)
P(it, 'Prateleiras de 2,5', 92, 57, 9, CO25, 0.92)
F(it, 'Cabideiro (tubo)', 2, 'Cabideiro')
gavetas(it, 8, 80, 20, 55, BR15, pux='espaçado')
P(it, 'Sapateira', 92, 45, 2, BR15, 0.92); F(it, 'Corrediça · sapateira', 2, 'Corrediça Hettich')
P(it, 'Porta de correr', 270, 95, 3, CO18)
F(it, 'Sistema de correr 3 folhas', 1, 'Sistema de correr 3 folhas'); F(it, 'Desempenador', 6, 'Desempenador de porta')
P(it, 'Rodapé e faixa superior (5)', 285, 5, 2, CO18)
it = item('Quarto Marcela', 'Ponta curva de prateleiras abertas (referência)', '60 × 280 × 60 · curva R60')
P(it, 'Prateleiras curvas de 2,5', 60, 60, 6, MA18, 1.0); P(it, 'Lateral', 280, 60, 1, MA18)
F(it, 'Curvatura em MDF flexível / usinagem', 1, 'Canto boleado')
it = item('Quarto Marcela', 'Estante lateral de prateleiras (lado esquerdo)', '~25–40 × 280 · 7 prat.')
P(it, 'Prateleiras de 2,5', 40, 30, 7, CO25, 0.4); P(it, 'Lateral', 280, 30, 1, CO18)
it = item('Quarto Marcela', 'Peça 40 × 160 com ponta arredondada (parede inclinada)', '160 × ? × 40')
P(it, 'Tampo com ponta arredondada', 160, 40, 1, CO25, 2.0)

# ══ QUARTO MARCELO ═══════════════════════════════════════════════════════
it = item('Quarto Marcelo', 'Mesa de cabeceira / aparador com 2 portas e prateleira', '138 × 55 × 40, ponta arredondada')
caixa(it, 138, 55, 40, CO18, ndiv=1, base_ext=True, topo_ext=True)
giro(it, 2, 69, 52, CO18, pux='')
prat(it, 1, 67, 38)
F(it, 'Ponta arredondada', 1, 'Canto boleado')
it = item('Quarto Marcelo', 'Painel ripado com nichos (Vista 03)', 'sem cotas')
P(it, 'Painel de fundo (estimado 100 × 260)', 260, 100, 1, MA18, 0)
P(it, 'Ripas (estimado)', 260, 4, 18, MA18, 5.2)
P(it, 'Nichos · prateleiras (3)', 100, 25, 4, MA18, 1.0)

AMBIENTES = list(dict.fromkeys(i['amb'] for i in ITENS))
