# -*- coding: utf-8 -*-
"""APARTAMENTO MR — levantamento  [23/11/2026]
Caderno de marcenaria P50 (Bruna Teixeira), junho/2026, 25 pranchas A3, cotadas. Leitura em
_leitura-01.md e _leitura-02.md. Cores: Branco TX, Frapê, Louro Freijó Poro e Verde Jade (Arauco),
no preço da linha de cor. ⚠ Ferragem: TELESCÓPICA, como a prancha pede nas gavetas (padrão até o
Jonathan dizer outra coisa). ⛔ Fora: granito, tanque, serralheria, espelho colado na parede,
móveis existentes e Westwing.
"""
ITENS = []
BR15, BR18, BR6 = 'MDF Branco TX 15', 'MDF Branco TX 18', 'MDF Branco TX 6'
FR15, FR18 = 'MDF Frapê 15', 'MDF Frapê 18'
LF15, LF18 = 'MDF Louro Freijó 15', 'MDF Louro Freijó 18'
VJ15, VJ18 = 'MDF Verde Jade 15', 'MDF Verde Jade 18'


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
it = item('Lavanderia', 'Armário sob o tanque', '75 × 87 × 51')
caixa(it, 75, 77, 51, BR15)
giro(it, 2, 35.5, 73, BR18, pux=''); prat(it, 1, 71, 51); pux(it, 2)
P(it, 'Rodapé', 75, 10, 1, BR15)
it = item('Lavanderia', 'Armário com cesto de roupa e gaveta', '85 × 103 × 45')
caixa(it, 85, 93, 45, BR15, ndiv=1)
gavetas(it, 1, 36, 89, 42, BR18, pux='', nome='Gavetão cesto')
gavetas(it, 1, 43, 18, 42, BR18, pux='')
pux(it, 2); P(it, 'Rodapé', 85, 10, 1, BR15)

# ══ 02 · DESPENSA ════════════════════════════════════════════════════════
it = item('Despensa', 'Armário com nicho do micro-ondas e gaveta', '90 × 288 × 52')
caixa(it, 90, 278, 52, BR15)
giro(it, 2, 43, 95, BR18, pux=''); giro(it, 2, 43, 38, BR18, pux=''); giro(it, 2, 43, 49, BR18, pux='')
P(it, 'Nicho do micro · base e topo', 86, 50, 2, BR18)
gavetas(it, 1, 86, 49, 48, BR18, pux='', nome='Gavetão')
prat(it, 3, 86, 50); pux(it, 7); P(it, 'Rodapé', 90, 10, 1, BR15)
it = item('Despensa', 'Armário de piso ao teto com reforço para revestimentos', '190 × 288 × 59')
caixa(it, 190, 278, 59, BR15, ndiv=3)
giro(it, 2, 46, 274, BR18, pux=''); giro(it, 2, 46, 162, BR18, pux=''); giro(it, 2, 46, 110, BR18, pux='')
prat(it, 7, 70, 57)
gavetas(it, 2, 34, 22, 52, BR15, pux='espaçado')
P(it, 'Reforço do compartimento de revestimentos', 92, 57, 2, BR18)
pux(it, 6); P(it, 'Rodapé', 190, 10, 1, BR15)
it = item('Despensa', 'Prateleira dobrável de bordas arredondadas', '75 × 60')
P(it, 'Tampo dobrável', 75, 60, 1, BR18)
F(it, 'Mão-francesa dobrável (par)', 1, 'Mão francesa dobrável')

# ══ 03 · SALA DE JANTAR ══════════════════════════════════════════════════
it = item('Sala de jantar', 'Armário sob a bancada existente', '167 × 100 × 32')
caixa(it, 167, 90, 32, FR15, ndiv=2, lat_ext=2)
giro(it, 6, 26.5, 86, FR18, pux='')
prat(it, 6, 53, 30, BR15); pux(it, 6); P(it, 'Rodapé', 167, 10, 1, FR15)
it = item('Sala de jantar', 'Cristaleira com portas de vidro', '79 × 244 × 42')
caixa(it, 79, 234, 42, LF18, base_ext=True, topo_ext=True)
P(it, 'Porta · quadro em Freijó', 230, 8, 4, LF18); P(it, 'Porta · travessas', 22, 8, 4, LF18)
M2(it, 'Vidro incolor das portas', 21.5, 214, 2, 'Vidro temperado')
F(it, 'Dobradiça', 8, 'Dobradiça Hettich')
P(it, 'Prateleira de 3 cm (duas faces)', 75, 38, 10, LF15, 0.75)
F(it, 'Puxador redondo usinado', 2, 'Cava usinada')
P(it, 'Rodapé', 79, 10, 1, LF15)

# ══ 04 · HALL DE ENTRADA ═════════════════════════════════════════════════
it = item('Hall de entrada', 'Banco sapateira solto com palhinha', '110 × 50 × 42')
caixa(it, 110, 41, 42, LF18, base_ext=True, topo_ext=True)
P(it, 'Tampo de 2', 110, 42, 1, LF18); P(it, 'Base com pés', 110, 7, 2, LF18)
P(it, 'Porta · quadro', 53, 8, 4, LF18); P(it, 'Porta · montantes', 25, 8, 4, LF18)
M2(it, 'Palhinha natural', 37, 25, 2, 'Palha natural')
F(it, 'Dobradiça', 4, 'Dobradiça Hettich'); prat(it, 1, 106, 38, LF15)
# ⭐ [Jonathan, 23/11/2026] "pode considerar o custo da almofada"
M2(it, 'Almofada estofada do assento', 110, 42, 1, 'Estofado')
F(it, 'Puxador cava (m)', 1.06, 'Cava usinada')
it = item('Hall de entrada', 'Armário com portas de palhinha e nicho em Freijó', '93 × 254 × 65')
caixa(it, 93, 244, 65, FR18, ndiv=0, base_ext=True, topo_ext=True)
P(it, 'Nicho em Freijó', 87, 61, 3, LF18); P(it, 'Nicho · fundo', 87, 80, 1, LF15, 0)
for a in (64, 88):
    P(it, f'Porta {a} · quadro', 43.5, 8, 4, FR18); P(it, f'Porta {a} · montantes', a - 16, 8, 4, FR18)
    F(it, 'Dobradiça', 2 * ndob(a), 'Dobradiça Hettich')
M2(it, 'Palhinha natural', 27.5, 48, 2, 'Palha natural'); M2(it, 'Palhinha natural', 27.5, 72, 2, 'Palha natural')
prat(it, 1, 87, 61, FR15)
F(it, 'Puxador cava (m)', 1.74, 'Cava usinada')
P(it, 'Rodapé', 93, 10, 1, FR15)

# ══ 05 · SALA DE TV E BRINQUEDOTECA ══════════════════════════════════════
it = item('Sala de TV', 'Estante com nicho da TV, de piso a teto', '355 × 287 × 57')
caixa(it, 355, 287, 57, LF18, ndiv=2, base_ext=True, topo_ext=True)
P(it, 'Prateleiras de toda a largura', 349, 55, 2, LF18, 3.49)
P(it, 'Prateleiras das colunas e do centro', 82, 55, 10, LF18, 0.82)
P(it, 'Fundo em Freijó', 287, 355 / 2, 2, LF15, 0)
giro(it, 4, 41, 78, LF18, pux=''); giro(it, 4, 44, 40, LF18, pux='')
F(it, 'Puxador redondo usinado', 8, 'Cava usinada')
P(it, 'Rodapé', 355, 10, 1, LF15)
it = item('Brinquedoteca', 'Bancada solta com caixas de brinquedo e suportes', '150 × 55 × 50 + caixas')
caixa(it, 150, 50, 50, LF18, base_ext=True, topo_ext=True, fundo=True)
P(it, 'Base', 150, 5, 2, LF18)
P(it, 'Caixa de brinquedo · laterais, frente e fundo', 36, 33, 12, VJ15)
P(it, 'Caixa de brinquedo · base', 36, 36, 3, VJ15)
F(it, 'Rodízio', 12, 'Rodízio')
P(it, 'Prateleira expositora · base e aba', 60, 20, 8, LF18)
P(it, 'Suporte de bola com furo', 25, 33, 6, VJ18)

# ══ 06 · QUARTO DIEGO ════════════════════════════════════════════════════
it = item('Quarto Diego', 'Guarda-roupa com maleiro e armário raso', '239 × 288 × 57 + 102 × 288 × 25')
caixa(it, 239, 282, 57, FR18, ndiv=1)
interno(it, 113, prat=4, cab=3, sap=5, k=BR15)
gavetas(it, 3, 56, 18, 52, BR15, pux='espaçado'); gavetas(it, 3, 111, 15, 52, BR15, pux='espaçado')
giro(it, 4, 56.5, 230, FR18, pux=''); giro(it, 4, 56.5, 52, FR18, pux='')
# ⭐ [Jonathan, 23/11/2026] "é o inverso": 102 de frente por 25 de profundidade
caixa(it, 102, 282, 25, FR18, ndiv=1)
giro(it, 2, 49, 280, FR18, pux=''); prat(it, 6, 49, 23)
F(it, 'Puxador cava (m)', 8.1, 'Cava usinada')
P(it, 'Fechamento até o teto e rodapé', 264, 10, 2, FR15)
it = item('Quarto Diego', 'Mesa de estudo regulável e nichos redondos', '118 × 86 × 52 · 2 nichos Ø 50')
P(it, 'Mesa · laterais com encaixes', 86, 52, 2, FR18)
P(it, 'Tampo regulável em Verde Jade', 114, 48, 1, VJ18)
P(it, 'Mesa · prateleira inferior e travessa', 114, 20, 2, FR18)
F(it, 'Suporte de regulagem', 4, 'Suporte de prateleira')
F(it, 'Usinagem dos encaixes', 1, 'Canto boleado')
P(it, 'Nicho redondo · fundo', 50, 50, 2, LF18, 0)
P(it, 'Nicho redondo · aro curvo', 157, 20, 2, LF15, 1.57)
F(it, 'Usinagem curva dos nichos', 2, 'Canto boleado')

# ══ 07 · QUARTO CASAL ════════════════════════════════════════════════════
it = item('Quarto casal', 'Guarda-roupa de correr A', '180 × 304 × 65')
caixa(it, 180, 284, 58, FR18, ndiv=1)
interno(it, 87, prat=2, cab=4, gav=[(11, 87), (16, 87), (16, 87), (16, 87), (16, 87)], k=BR15)
P(it, 'Porta de correr em Frapê', 280, 88, 2, FR18)
F(it, 'Desempenador de porta', 4, 'Desempenador de porta')
F(it, 'Sistema de correr', 1, 'Sistema de correr Dominus')
F(it, 'Puxador perfil metálico (m)', 5.6, 'Perfil de proteção de piso')
P(it, 'Fechamento e rodapé', 180, 10, 2, FR15)
it = item('Quarto casal', 'Guarda-roupa de correr D', '135 × 304 × 65')
caixa(it, 126, 284, 58, FR18, ndiv=1)
interno(it, 62, prat=3, cab=3, gav=[(11, 62), (16, 62), (16, 62), (16, 62), (16, 62)], k=BR15)
P(it, 'Porta de correr em Frapê', 280, 63, 2, FR18)
F(it, 'Desempenador de porta', 4, 'Desempenador de porta')
F(it, 'Sistema de correr', 1, 'Sistema de correr Dominus')
F(it, 'Puxador perfil metálico (m)', 5.6, 'Perfil de proteção de piso')
P(it, 'Enchimento, fechamento e rodapé', 135, 10, 2, FR15)
it = item('Quarto casal', 'Armário de giro', '115 × 304 × 40')
caixa(it, 115, 284, 40, FR18)
giro(it, 2, 55.5, 280, FR18, pux=''); prat(it, 7, 111, 38); pux(it, 2)
P(it, 'Fechamento e rodapé', 115, 10, 2, FR15)
it = item('Quarto casal', 'Cabeceira em painéis e prateleira de bordas arredondadas', '307 × 120 · 230 × 30')
painel(it, 307, 120, LF18, 'Cabeceira em 5 painéis')
P(it, 'Prateleira · duas faces', 230, 30, 2, LF15, 4.6)
F(it, 'Pontas arredondadas', 1, 'Canto boleado'); F(it, 'Fixação invisível', 4, 'Fixação invisível')

# ══ 08 · ESCRITÓRIO ══════════════════════════════════════════════════════
it = item('Escritório', 'Armário sob a bancada com prateleira da impressora', '166 × 76 × 47')
caixa(it, 157, 66, 45, FR15, ndiv=2, lat_ext=1)
giro(it, 1, 54, 62, FR18, pux=''); giro(it, 2, 37.5, 57, FR18, pux='')
P(it, 'Nicho em Frapê', 58, 45, 2, FR15)
P(it, 'Prateleira deslizante da impressora', 56, 40, 1, FR18)
F(it, 'Corrediça · impressora', 1, 'Corrediça Hettich')
prat(it, 2, 58, 45); pux(it, 3)
P(it, 'Enchimento e rodapé', 166, 10, 2, FR15)
it = item('Escritório', 'Bancada em L de 5 cm', '166 + 140,5 × 55')
P(it, 'Bancada · faces', 166, 50, 2, FR18, 3.32); P(it, 'Retorno · faces', 140.5, 55, 2, FR18, 2.81)
P(it, 'Frente e topos de 5', 360, 5, 1, FR18, 3.6)
P(it, 'Pé / apoio do retorno', 76, 55, 1, FR18)
it = item('Escritório', 'Armário aéreo em Freijó', '173 × 76 × 35')
caixa(it, 173, 72, 35, LF18, ndiv=1, base_ext=True)
giro(it, 4, 41.8, 70, LF18, pux=''); prat(it, 2, 83.5, 33, LF15); pux(it, 4)
it = item('Escritório', 'Gaveteiro móvel com rodízios', '45 × 55 × 47')
caixa(it, 45, 50, 47, FR18, base_ext=True, topo_ext=True)
gavetas(it, 3, 45, 15.3, 44, FR15, pux='')
F(it, 'Rodízio', 4, 'Rodízio'); pux(it, 3)

AMBIENTES = list(dict.fromkeys(i['amb'] for i in ITENS))
