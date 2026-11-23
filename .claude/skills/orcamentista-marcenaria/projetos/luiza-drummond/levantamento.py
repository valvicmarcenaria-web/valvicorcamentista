# -*- coding: utf-8 -*-
"""LUIZA DRUMMOND — sala de estar e jantar · levantamento  [23/11/2026]
Projeto executivo da designer Rubia Nascimento, 10/2026, 9 pranchas (layout, luminotécnico,
vistas 1 a 6 e detalhe de marcenaria). P.D. 277. Belo Horizonte.
Cores: MDF Nogueira Caiena (Duratex) e Areia (Guararapes) no preço da linha de cor; cristaleira em
LACA SayerLaca M145 (vinho, a cor da parede) com vidro incolor.
⛔ Fora: pintura das paredes, tapetes, puffs, quadros, espelho, cadeiras, mesa, sofá, abajur,
   luminárias, forro e o "novo estofamento" da cadeira existente.
"""
ITENS = []
BR15, BR18, BR6 = 'MDF Branco TX 15', 'MDF Branco TX 18', 'MDF Branco TX 6'
NC15, NC18 = 'MDF Nogueira Caiena 15', 'MDF Nogueira Caiena 18'
AR18 = 'MDF Areia 18'


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



# ══ PRATELEIRAS · MDF Nogueira Caiena, 4 cm (duas faces de 18 + quadro) ══
it = item('Sala', 'Prateleiras de parede com LED (sala e jantar)', '2 × 350 × 4 × 30')
for nome in ('sala', 'jantar'):
    P(it, f'Prateleira {nome} · faces', 350, 30, 2, NC18, 0)
    P(it, f'Prateleira {nome} · frente e topos de 4', 410, 4, 1, NC18, 4.1)
    F(it, 'Fixação invisível', 6, 'Fixação invisível')
    led(it, 3.5)
it = item('Sala', 'Prateleiras em L de 4 cm e prateleiras inferiores em L', '2 × 176 × 68 · 3 × 90 × 68')
P(it, 'Prateleira média em L · faces', 176, 22, 4, NC18, 0); P(it, 'Prateleira média em L · retorno', 46, 22, 4, NC18, 0)
P(it, 'Prateleira média · frentes e topos de 4', 250, 4, 2, NC18, 5)
F(it, 'Fixação invisível', 8, 'Fixação invisível')
P(it, 'Prateleira inferior em L (2 cm)', 90, 22, 3, NC18, 2.7); P(it, 'Prateleira inferior · retorno', 46, 22, 3, NC18, 1.4)
F(it, 'Fixação invisível', 6, 'Fixação invisível')
F(it, 'Arranhador torre em sisal (tubo, sisal e brinquedo)', 1, 'Arranhador sisal')

# ══ PRATELEIRA E PAINEL DA TV ════════════════════════════════════════════
it = item('Sala', 'Painel da TV com prateleiras e tubos de inox', '125 × 75 · prateleiras 160 × 70')
P(it, 'Painel da TV em Areia', 125, 75, 1, AR18, 4.0)
P(it, 'Prateleira de 4 · faces', 160, 70, 4, NC18, 0)
P(it, 'Prateleira · borda arredondada de 4', 260, 4, 2, NC18, 5.2)
F(it, 'Recorte e canto arredondado', 2, 'Canto boleado')
F(it, 'Tubo de inox de sustentação (un)', 2, 'Tubo inox')
F(it, 'Sisal de 5 mm no tubo (arranhador)', 1, 'Arranhador sisal')
F(it, 'Suporte oculto', 4, 'Fixação invisível')

# ══ SAPATEIRA ════════════════════════════════════════════════════════════
it = item('Sala', 'Sapateira basculante com pés de madeira', '85 × 90 × 35')
caixa(it, 85, 78, 35, NC18, ndiv=1, base_ext=True, topo_ext=True)
P(it, 'Frente basculante', 39.5, 36.5, 4, NC18)
F(it, 'Kit sapateira basculante', 4, 'Kit tulha')
P(it, 'Bandeja interna', 39, 30, 4, NC15)
F(it, 'Puxador ouro velho', 4, 'Puxador Zen Design'); F(it, 'Pés de madeira (jogo)', 1, 'Pé de madeira')

# ══ RACK ═════════════════════════════════════════════════════════════════
it = item('Sala', 'Rack com ponta arredondada e pés dourados', '160 × 55 × 45')
caixa(it, 160, 45, 45, NC18, ndiv=3, base_ext=True, topo_ext=True)
giro(it, 3, 47, 45, NC18, pux='')
F(it, 'Puxador cava 45° (m)', 1.4, 'Cava usinada')
F(it, 'Ponta arredondada', 1, 'Canto boleado')
prat(it, 3, 46, 43, NC15)
F(it, 'Pés de perfil metálico dourado (jogo)', 1, 'Pé metálico')

# ══ CRISTALEIRA EM LACA ══════════════════════════════════════════════════
it = item('Sala', 'Cristaleira em arco, laqueada, com portas de vidro', '125 × 277 × 40')
caixa(it, 125, 267, 40, BR18, ndiv=0, base_ext=True, topo_ext=True)
P(it, 'Porta superior em arco · quadro (5 cm)', 174, 57.5, 2, BR18, 4.6)
M2(it, 'Vidro incolor em arco', 47.5, 164, 2, 'Vidro temperado')
P(it, 'Porta inferior com boiserie', 80, 57.5, 2, BR18)
F(it, 'Boiserie usinada nas portas', 2, 'Usinagem almofadada')
F(it, 'Dobradiça', 2 * 4 + 2 * 2, 'Dobradiça Hettich')
prat(it, 3, 115, 38); P(it, 'Divisória horizontal', 115, 38, 1, BR18)
led(it, 3.5)
F(it, 'Puxador alça e ponto ouro velho', 4, 'Puxador Zen Design')
M2(it, 'Laca SayerLaca M145 (faces externas e portas)', 125, 277, 2.6, 'Laca')
P(it, 'Rodapé', 125, 10, 1, BR18)

AMBIENTES = list(dict.fromkeys(i['amb'] for i in ITENS))
