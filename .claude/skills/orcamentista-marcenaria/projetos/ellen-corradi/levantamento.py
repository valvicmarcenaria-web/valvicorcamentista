# -*- coding: utf-8 -*-
"""ELLEN CORRADI — levantamento do apartamento  [24/11/2026]
Caderno de marcenaria de Jessica Sollero, 10/12/2025, 33 pranchas A4 (só imagem). Leituras em _leitura-0*.md.
Cores: Branco Brilhante (cozinha, rack), Branco TX, Carvalho Malva (Duratex), Frapê e Sal Rosa (Arauco),
todas no preço da linha de cor. Puxador chanfrado; Sotille nos roupeiros de correr.
⛔ Fora: pedra (bancadas, rodabancas, sóculos), eletros, metais, espelhos bisotados da sala (vidraçaria),
   tampo de vidro da escrivaninha das meninas, móveis soltos.
"""
ITENS = []
BR15, BR18, BR6 = 'MDF Branco TX 15', 'MDF Branco TX 18', 'MDF Branco TX 6'
BB15, BB18 = 'MDF Branco Brilhante 15', 'MDF Branco Brilhante 18'
CM15, CM18 = 'MDF Carvalho Malva 15', 'MDF Carvalho Malva 18'
FR15, FR18 = 'MDF Frapê 15', 'MDF Frapê 18'
SR15, SR18 = 'MDF Sal Rosa 15', 'MDF Sal Rosa 18'


def chanfro(it, m): F(it, 'Puxador chanfrado (m)', round(m, 2), 'Cava usinada')

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



# ══ SALA ═════════════════════════════════════════════════════════════════
it = item('Sala', 'Painel da TV em Carvalho com canais de luz', '180 × 253 × 6')
painel(it, 180, 253.5, CM18, 'Painel da TV'); P(it, 'Frisos e canais de LED', 253.5, 6, 4, CM18, 5.1)
led(it, 5.0)
it = item('Sala', 'Rack suspenso com gavetões e prateleira', '180 × 35 × 34 + prateleira')
caixa(it, 180, 35, 34, BB18, ndiv=2, base_ext=True, topo_ext=True)
gavetas(it, 3, 60, 35, 32, BB18, pux=''); chanfro(it, 1.8)
P(it, 'Prateleira de 5 · faces', 180, 34, 2, CM15, 0); P(it, 'Prateleira · frente e topos', 248, 5, 1, CM15, 2.48)
F(it, 'Fixação invisível', 6, 'Fixação invisível')

# ══ VARANDA ══════════════════════════════════════════════════════════════
it = item('Sala', 'Prateleira recortada da varanda, em Carvalho', '38 × 45 × 5')
P(it, 'Prateleira de 5 · faces', 45, 38, 2, CM15); F(it, 'Recorte chanfrado e fixação invisível', 1, 'Canto boleado')

# ══ COZINHA ══════════════════════════════════════════════════════════════
it = item('Cozinha', 'Torre quente com nichos em Carvalho', '68,5 × 278 × 62')
caixa(it, 68.5, 263, 62, BB18, lat_ext=2)
giro(it, 2, 34.3, 78, BB18, pux=''); chanfro(it, 0.7); prat(it, 1, 64, 60)
P(it, 'Nichos em Carvalho · bases e forros', 64.5, 60, 4, CM18, 0.645); P(it, 'Nichos · laterais', 110, 60, 2, CM15)
it = item('Cozinha', 'Aéreos com básculas em Carvalho, luz e escorredor', '161,5 + 62 × 78 + básculas')
caixa(it, 161.5, 78, 33, BB15, ndiv=1, base_ext=True)
giro(it, 3, 40.5, 78, BB18, pux=''); P(it, 'Painel fixo', 78, 39.5, 1, BB18); prat(it, 3, 79, 31)
caixa(it, 62, 78, 30, BB15, base_ext=True); giro(it, 1, 58, 78, BB18, pux=''); prat(it, 1, 58, 28)
caixa(it, 161.5, 35, 30, CM15, ndiv=1, base_ext=True)
P(it, 'Báscula em Carvalho', 81, 35, 2, CM18); F(it, 'Dobradiça', 4, 'Dobradiça Hettich'); F(it, 'Pistão', 4, 'Pistão com amortecimento')
F(it, 'Escorredor metálico', 1, 'Escorredor')
led(it, 1.6); chanfro(it, 3.1)
it = item('Cozinha', 'Armários inferiores da pia e do cooktop', '106,5 + 95 + canto × 72 × 55')
caixa(it, 106.5, 72, 55, BB15, ndiv=1, lat_ext=0); giro(it, 2, 53, 72, BB18, pux=''); prat(it, 2, 52, 53)
caixa(it, 95, 72, 55, BB15, lat_ext=1)
gavetas(it, 2, 95, 18, 50, BB18, pux='', nome='Gaveta de talher'); gavetas(it, 1, 95, 36, 50, BB18, pux='', nome='Gavetão')
caixa(it, 62, 72, 55, BB15, lat_ext=0); prat(it, 1, 58, 53); P(it, 'Fechamento do canto', 72, 20, 1, BB18)
chanfro(it, 3.0)
it = item('Cozinha', 'Aéreo da geladeira e despensa deslizante', '105 × 77 × 60 · 30 × 183 × 60')
caixa(it, 105, 77, 60, BB15, base_ext=True); giro(it, 3, 35, 77, BB18, pux=''); prat(it, 2, 51, 58)
caixa(it, 30, 183, 60, BB18, base_ext=True, topo_ext=True)
P(it, 'Despensa · prateleiras com grade', 26, 55, 5, BR15, 0.26)
F(it, 'Kit despensa deslizante', 1, 'Kit despensa deslizante')
chanfro(it, 1.35)

# ══ LAVANDERIA ═══════════════════════════════════════════════════════════
it = item('Lavanderia', 'Aéreo em L com nicho e cabideiro', '95,5 + 76 × 61 × 30')
caixa(it, 171.5, 61, 30, BR15, ndiv=2, base_ext=True)
giro(it, 4, 37, 61, BR18, pux=''); prat(it, 3, 72, 28); chanfro(it, 1.5)
F(it, 'Cabideiro metálico', 1, 'Cabideiro')
it = item('Lavanderia', 'Armário de limpeza com vão de vassouras', '70 × 255 × 30')
caixa(it, 70, 240, 30, BR15, ndiv=1)
giro(it, 2, 35, 237, BR18, pux=''); prat(it, 4, 32, 28); chanfro(it, 0.7)

# ══ BANHO SOCIAL ═════════════════════════════════════════════════════════
it = item('Banho social', 'Espelheira e gabinete suspenso', '82 × 126 × 15 · 82 × 65 × 49,5')
caixa(it, 82, 126, 15, FR15, base_ext=True); prat(it, 4, 78, 13)
M2(it, 'Porta de espelho prata em alumínio', 52, 126, 1, 'Porta de espelho em alumínio'); F(it, 'Dobradiça', 3, 'Dobradiça Hettich')
P(it, 'Faixas fixas', 126, 15, 2, FR18)
caixa(it, 82, 65, 49.5, FR15, base_ext=True); giro(it, 1, 60, 65, FR18, pux=''); P(it, 'Faixas fixas', 65, 11, 2, FR18)
prat(it, 1, 78, 47); chanfro(it, 1.2)

# ══ BANHO SUÍTE ══════════════════════════════════════════════════════════
it = item('Banho suíte', 'Espelheira com nichos e gabinete chanfrado', '136,5 × 126 × 15 · 136,5 × 65 × 40,5')
caixa(it, 136.5, 126, 15, FR15, ndiv=1, base_ext=True); prat(it, 4, 84, 13); P(it, 'Nichos', 13.5, 13, 3, FR15)
M2(it, 'Porta de espelho prata em alumínio', 42.4, 121, 2, 'Porta de espelho em alumínio'); F(it, 'Dobradiça', 6, 'Dobradiça Hettich')
M2(it, 'Espelho fixo colado', 34, 121, 1, 'Espelho colado')
caixa(it, 136.5, 65, 40.5, FR15, ndiv=2, base_ext=True); giro(it, 3, 32, 65, FR18, pux='')
P(it, 'Faces chanfradas e nichos', 65, 22.4, 3, FR18); prat(it, 2, 60, 38)
F(it, 'Recorte chanfrado da frente', 2, 'Canto boleado'); chanfro(it, 2.0)

# ══ QUARTO LARA ══════════════════════════════════════════════════════════
it = item('Quarto Lara', 'Roupeiro de correr com portas de espelho', '146,5 × 279 × 65')
caixa(it, 146.5, 273, 60, FR18, ndiv=1)
interno(it, 70, prat=3, cab=2, gav=[(21, 70), (21, 70), (21, 70), (21, 70)], k=BR15)
M2(it, 'Porta de correr de espelho prata em alumínio', 71.3, 273, 2, 'Porta de espelho em alumínio')
F(it, 'Sistema de correr', 1, 'Sistema de correr Dominus'); F(it, 'Puxador Sotille', 2, 'Puxador Sotille')
it = item('Quarto Lara', 'Escrivaninha, painel com espelho e ripado, prateleiras', '180 × 80 · painel 180 × 132')
caixa(it, 180, 10, 45, CM18, ndiv=2, base_ext=True, topo_ext=True)
P(it, 'Báscula do tampo', 60, 45, 1, CM18); F(it, 'Pistão', 2, 'Pistão com amortecimento')
F(it, 'Divisória de acrílico', 1, 'Divisória de acrílico')
gavetas(it, 2, 55, 10, 42, CM15, pux=''); chanfro(it, 1.7)
painel(it, 120, 132, FR18, 'Painel do ripado'); ripado(it, 120, 132, CM18, ripa=3, vao=3, base=False)
M2(it, 'Espelho prata colado', 60, 132, 1, 'Espelho colado')
P(it, 'Prateleira de 4 · faces', 180, 15, 2, CM15, 3.6); led(it, 1.8)
P(it, 'Prateleiras de 5 · faces', 121.5, 15, 4, CM15, 2.4); F(it, 'Fixação invisível', 8, 'Fixação invisível')
it = item('Quarto Lara', 'Cabeceira estofada em arcos, mesa de cabeceira e painel da TV', '270 × 110 · 55 × 60 × 50 · 170 × 80')
P(it, 'Base da cabeceira', 270, 110, 1, BR15, 0)
M2(it, 'Estofado em arcos, tecido Facto off-white', 270, 110, 1, 'Estofado')
caixa(it, 55, 60, 50, CM18, base_ext=True, topo_ext=True); giro(it, 1, 55, 57, CM18, pux='')
P(it, 'Sapateira', 51, 45, 3, BR15, 0.51); F(it, 'Corrediça · sapateira', 3, 'Corrediça Hettich')
painel(it, 170, 80, FR18, 'Painel da TV')

# ══ QUARTO ISABELA E LÍVIA ═══════════════════════════════════════════════
it = item('Quarto Isabela e Lívia', 'Beliche com gavetões, escada, guarda-corpo e nicho iluminado', '214,5 × 279 × 105')
P(it, 'Estrutura · laterais até o teto', 279, 105, 2, CM18); P(it, 'Estrutura · montantes', 279, 10, 4, CM18)
P(it, 'Estrados das duas camas', 196, 101, 2, CM18, 0)
P(it, 'Base da cama de baixo', 196, 30, 2, CM18)
gavetas(it, 2, 68, 25, 90, CM18, pux='', nome='Gavetão')
P(it, 'Guarda-corpo ripado', 196, 6, 7, CM18, 3.9)
P(it, 'Escada · degraus e montantes', 50, 20, 6, CM18); P(it, 'Escada · montantes', 165, 8, 2, CM18)
P(it, 'Nicho revisteiro', 41, 15, 4, CM18); led(it, 1.2)
it = item('Quarto Isabela e Lívia', 'Roupeiro de correr, uma porta de espelho', '188 × 279 × 60')
caixa(it, 188, 273, 60, FR18, ndiv=1)
interno(it, 91, prat=4, cab=2, gav=[(18, 91), (18, 91), (18, 91), (18, 91)], sap=6, k=BR15)
P(it, 'Porta de correr em Frapê', 273, 92, 1, FR18); F(it, 'Desempenador de porta', 2, 'Desempenador de porta')
M2(it, 'Porta de correr de espelho prata em alumínio', 92, 273, 1, 'Porta de espelho em alumínio')
F(it, 'Sistema de correr', 1, 'Sistema de correr Dominus'); F(it, 'Puxador Sotille', 2, 'Puxador Sotille')
it = item('Quarto Isabela e Lívia', 'Baú, coluna de prateleiras e escrivaninha em Sal Rosa', '85 × 85 · 20 × 194 · 68 × 75')
caixa(it, 85, 85, 52, SR18, base_ext=True)
P(it, 'Tampa basculante', 85, 52, 1, SR18); F(it, 'Pistão', 2, 'Pistão com amortecimento')
P(it, 'Coluna · laterais', 194, 50, 1, SR18); P(it, 'Coluna · prateleiras', 50, 20, 5, SR18, 0.5)
caixa(it, 75, 75, 52, SR18, base_ext=True, topo_ext=True)
gavetas(it, 1, 68, 10, 48, SR15, pux=''); F(it, 'Divisória de acrílico', 1, 'Divisória de acrílico')
F(it, 'Meia esquadria', 1, 'Canto boleado')
it = item('Quarto Isabela e Lívia', 'Painéis estofados em arcos', '2 × 195,5 × 70')
P(it, 'Base dos painéis', 195.5, 70, 2, BR15, 0)
M2(it, 'Estofado em arcos, tecido Facto off-white', 195.5, 70, 2, 'Estofado')

# ══ QUARTO SUÍTE ═════════════════════════════════════════════════════════
it = item('Quarto suíte', 'Guarda-roupa com portas de espelho', '222 × 279 × 55')
caixa(it, 222, 273, 55, FR18, ndiv=2)
interno(it, 55, prat=3, cab=3, gav=[(23, 55), (23, 55), (23, 55), (23, 55)], sap=5, k=BR15)
M2(it, 'Porta de giro de espelho prata em alumínio', 56.5, 273, 3, 'Porta de espelho em alumínio')
F(it, 'Dobradiça', 15, 'Dobradiça Hettich'); P(it, 'Painel fixo em Frapê', 273, 48, 1, FR18)
F(it, 'Puxador', 3, 'Puxador Zen Design')
it = item('Quarto suíte', 'Armário aéreo sobre a cama', '282,5 × 112 × 50')
caixa(it, 282.5, 106, 50, FR15, ndiv=2, base_ext=True)
giro(it, 6, 47, 106, FR18, pux=''); prat(it, 3, 94, 48); chanfro(it, 2.8)
it = item('Quarto suíte', 'Cabeceira em Carvalho com estofado e mesas de cabeceira', '282,5 × 107 · 2 × 47 × 60 × 43')
painel(it, 182.5, 107, CM18, 'Cabeceira em Carvalho')
P(it, 'Base do estofado', 282.5, 95, 1, BR15, 0); M2(it, 'Estofado em gomos, tecido Facto off-white', 282.5, 95, 1, 'Estofado')
caixa(it, 47, 60, 43, CM18, base_ext=True, topo_ext=True); caixa(it, 47, 60, 43, CM18, base_ext=True, topo_ext=True)
gavetas(it, 6, 47, 19, 40, CM15, pux=''); chanfro(it, 2.8)
it = item('Quarto suíte', 'Painel da TV com ripado em Carvalho', '129 × 100')
painel(it, 129, 94, FR18, 'Painel da TV'); ripado(it, 129, 94, CM18, ripa=3, vao=0.1, base=False)
P(it, 'Prateleiras de 3', 129, 15, 4, CM15, 2.6)

AMBIENTES = list(dict.fromkeys(i['amb'] for i in ITENS))
