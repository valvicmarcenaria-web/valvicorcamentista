# -*- coding: utf-8 -*-
"""JESSICA FERNANDES — área social (cozinha e lavanderia) e quarto · levantamento  [23/11/2026]
Projeto executivo da designer Rubia Nascimento, 10/2026: área social em 12 pranchas, quarto em 5.
P.D. 264/265. Belo Horizonte.
Cores: MDF Alecrim e Lume (Guararapes) na área social, Carvalho Avelã (Duratex) no roupeiro, no preço
da linha de cor. Puxador cava 45° usinado. Palha sextavada nas portas do roupeiro.
⛔ Fora: granito Verde Candeias (bancadas), tanque, eletros, depurador, torre de tomadas, revestimentos,
   pintura, móveis e decoração de loja.
"""
ITENS = []
BR15, BR18, BR6 = 'MDF Branco TX 15', 'MDF Branco TX 18', 'MDF Branco TX 6'
AL15, AL18 = 'MDF Alecrim 15', 'MDF Alecrim 18'
LU15, LU18 = 'MDF Lume 15', 'MDF Lume 18'
CA15, CA18 = 'MDF Carvalho Avelã 15', 'MDF Carvalho Avelã 18'


def cava45(it, m): F(it, 'Puxador cava 45° (m)', round(m, 2), 'Cava usinada')

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



# ══ 01 · LAVANDERIA ══════════════════════════════════════════════════════
it = item('Lavanderia', 'Armário do tanque com lixeira deslizante', '65 × 75 × 60')
caixa(it, 65, 68, 58, AL15, lat_ext=1)
giro(it, 2, 32.5, 68, AL18, pux=''); cava45(it, 0.65)
F(it, 'Lixeira de embutir deslizante', 1, 'Lixeira deslizante')
P(it, 'Rodapé recuado', 65, 7, 1, AL15)
it = item('Lavanderia', 'Armário superior do tanque', '65 × 100 × 30')
caixa(it, 65, 100, 30, LU15, base_ext=True)
giro(it, 2, 32.5, 97, LU18, pux=''); cava45(it, 0.65); prat(it, 2, 61, 28, LU15)
it = item('Lavanderia', 'Armário alto de vassouras e prateleiras', '50 × 264 × 60 + 2 prateleiras')
caixa(it, 50, 254, 60, LU15, lat_ext=2)
giro(it, 1, 49, 251, LU18, pux=''); F(it, 'Puxador passante (m)', 2.51, 'Cava usinada')
prat(it, 2, 46, 58, LU15); P(it, 'Rodapé', 50, 10, 1, LU15)
P(it, 'Prateleira da lavanderia', 70, 30, 2, LU18, 1.4); F(it, 'Fixação invisível', 4, 'Fixação invisível')
it = item('Lavanderia', 'Armário sobre a geladeira', '75 × 75 × 60')
caixa(it, 75, 72, 58, LU15, base_ext=True)
giro(it, 2, 37.5, 72, LU18, pux=''); cava45(it, 0.75)

# ══ 02 · COZINHA ═════════════════════════════════════════════════════════
it = item('Cozinha', 'Armário da bancada com nichos do micro e do forno', '204 × 90 × 60')
caixa(it, 204, 75, 50, AL15, ndiv=2, lat_ext=1)
gavetas(it, 2, 65, 34.5, 48, AL18, pux='', nome='Gavetão'); gavetas(it, 1, 65, 34.5, 48, AL18, pux='', nome='Gavetão')
P(it, 'Nicho do micro e do forno · bases', 70, 50, 2, BR18)
cava45(it, 1.95); P(it, 'Rodapé', 204, 10, 1, AL15)
it = item('Cozinha', 'Armário superior com luz e depurador embutido', '204 × 99 × 30')
caixa(it, 204, 99, 30, LU15, ndiv=1, base_ext=True)
giro(it, 4, 51, 96, LU18, pux=''); cava45(it, 2.04); prat(it, 2, 100, 28, LU15)
P(it, 'Recorte e fundo do depurador', 60, 28, 1, LU15)
led(it, 2.04)
it = item('Cozinha', 'Península com gaveteiro, nichos e tampo de madeira natural', '148 × 100 · tampo 142 × 90')
caixa(it, 148, 83, 58, AL18, ndiv=2, base_ext=True)
gavetas(it, 4, 35, 17, 50, AL18, pux='')
giro(it, 1, 35, 83, AL18, pux='')
P(it, 'Nichos · prateleiras e fundo', 65, 50, 3, AL15)
cava45(it, 1.75); P(it, 'Rodapé', 148, 10, 1, AL15)
F(it, 'Recorte e acabamento das quinas', 2, 'Canto boleado')
F(it, 'Tampo em madeira natural, recortado', 1, 'Tampo madeira natural')

# ══ 03 · QUARTO ══════════════════════════════════════════════════════════
it = item('Quarto', 'Roupeiro de correr com palha sextavada e estante lateral', '190 × 265 × 60')
caixa(it, 190, 255, 60, CA18, ndiv=1)
interno(it, 87, prat=5, cab=2, gav=[(17, 87), (17, 87), (17, 87), (17, 87)], sap=2, sap_larg=43, k=BR15)
P(it, 'Nicho interno', 43, 40, 2, BR15)
P(it, 'Porta de correr · quadro e almofada', 255, 90, 2, CA18)
F(it, 'Usinagem do quadro da porta', 2, 'Usinagem almofadada')
M2(it, 'Palha sextavada com fundo em MDF', 78, 165, 2, 'Palha natural')
F(it, 'Desempenador de porta', 4, 'Desempenador de porta')
F(it, 'Sistema de correr', 1, 'Sistema de correr Dominus')
F(it, 'Puxador vão usinado (un)', 2, 'Cava usinada')
P(it, 'Estante lateral · prateleiras', 56, 22, 5, CA18, 0.56)
P(it, 'Fechamento e rodapé', 190, 10, 2, CA15)

AMBIENTES = list(dict.fromkeys(i['amb'] for i in ITENS))
