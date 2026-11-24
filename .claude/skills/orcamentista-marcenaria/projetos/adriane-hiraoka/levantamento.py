# -*- coding: utf-8 -*-
"""ADRIANE HIRAOKA — levantamento do apartamento  [24/11/2026]
Projeto executivo da designer Rubia Nascimento: sala, cozinha, lavanderia, suíte e quarto infantil (42 pranchas).
Leituras em _leitura-0*.md. Cores: Nogueira Caiena, Off White Suave e Mint (Duratex), Atenna e Azul Sereno
(Arauco), no preço da linha de cor. Puxadores: alça Primus e Phenix pretos, chanfro 45°, cava, fecho toque.
⛔ Fora: quartzito e granito, sóculos de alvenaria, eletros, metais, iluminação do gesso, móveis e decoração da
   legenda de produtos, troca de puxadores dos armários existentes.
"""
ITENS = []
BR15, BR18, BR6 = 'MDF Branco TX 15', 'MDF Branco TX 18', 'MDF Branco TX 6'
NC15, NC18 = 'MDF Nogueira Caiena 15', 'MDF Nogueira Caiena 18'
OW15, OW18 = 'MDF Off White Suave 15', 'MDF Off White Suave 18'
AT18 = 'MDF Atenna 18'
MI15, MI18 = 'MDF Mint 15', 'MDF Mint 18'
AZ15 = 'MDF Azul Sereno 15'


def pux(it, n, k='Puxador Zen Design'): F(it, 'Puxador (peça)', n, k)
def chanfro(it, m): F(it, 'Puxador usinado (m)', round(m, 2), 'Cava usinada')
def moldura(it, n): F(it, 'Moldura de 2 cm nas frentes (un)', n, 'Usinagem almofadada')

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
it = item('Sala', 'Painel com portas de correr embutidas, buffet e prateleiras', '713 × 210 · buffet 297 × 50 × 30')
painel(it, 713, 210, NC18, 'Painel de parede')
P(it, 'Folha de correr · face e contraface', 210, 90, 4, NC18)
F(it, 'Kit de porta de correr embutida', 2, 'Kit porta de correr de passagem')
chanfro(it, 4.2)
# ⭐ [Jonathan, 24/11/2026] "unifique o painel com o buffet e prateleiras": mesmo item
caixa(it, 297, 48, 30, NC18, ndiv=4, base_ext=True)
P(it, 'Tampo em Off White Suave', 297, 32, 1, OW18, 3.3)
giro(it, 5, 43, 48, NC18, pux=''); P(it, 'Portas curvas em MDF flexível', 48, 36, 2, NC18)
F(it, 'Dobradiça', 4, 'Dobradiça Hettich'); F(it, 'Curvatura da ponta', 2, 'Canto boleado')
F(it, 'Fecho toque', 7, 'Fecho toque'); prat(it, 3, 70, 28)
P(it, 'Prateleiras em Atenna de 3 cm · faces', 297, 25, 6, AT18, 0); P(it, 'Prateleiras · frentes', 320, 3, 3, AT18, 9.6)
P(it, 'Divisórias', 27, 25, 5, AT18); F(it, 'Pontas curvas', 3, 'Canto boleado'); F(it, 'Fixação invisível', 9, 'Fixação invisível')
F(it, 'Porta-vinhos em couro caramelo', 1, 'Porta vinhos couro')
it = item('Sala', 'Estante com portas de correr frisadas', '100 × 210 × 39')
caixa(it, 100, 207, 39, NC18, ndiv=1)
P(it, 'Prateleiras e divisórias desencontradas', 50, 37, 13, NC18, 0.5)
P(it, 'Porta de correr frisada', 48, 42, 2, NC18); F(it, 'Frisos de ventilação', 2, 'Usinagem almofadada')
F(it, 'Sistema de correr leve', 1, 'Sistema de correr leve')
it = item('Sala', 'Rack curvo com cachepô', '180 × 45 × 65')
caixa(it, 116, 45, 30, NC18, ndiv=1, base_ext=True, topo_ext=True)
P(it, 'Ponta curva · tampo, base e frente curva', 80, 65, 3, NC18)
F(it, 'Curvatura em MDF flexível', 2, 'Canto boleado')
giro(it, 2, 35, 41, NC18, pux=''); chanfro(it, 0.7)
P(it, 'Nicho', 26, 38, 2, NC18); F(it, 'Cachepô com forro impermeável', 1, 'Cachepô')
it = item('Sala', 'Revestimento do pilar e moldura de ripas da TV', 'pilar até o teto · 116 × 165')
P(it, 'Estrutura do pilar', 271, 30, 4, BR15, 0); M2(it, 'Revestimento curvo do pilar', 120, 271, 1, 'Revestimento curvo')
P(it, 'Ripas de 2 cm em volta da TV', 165, 4, 4, NC18, 3.3); P(it, 'Ripas horizontais', 116, 4, 2, NC18, 2.3)

# ══ COZINHA ══════════════════════════════════════════════════════════════
it = item('Cozinha', 'Bancada em L com frentes emolduradas e gaveteiro', '295 + 215 × 78 × 60')
caixa(it, 510, 78, 58, NC15, ndiv=6, lat_ext=1)
giro(it, 5, 52, 78, NC18, pux=''); gavetas(it, 4, 45, 19, 52, NC18, pux='')
P(it, 'Fechamentos dos cantos', 78, 60, 2, NC18); prat(it, 5, 52, 56)
moldura(it, 9); pux(it, 9)
it = item('Cozinha', 'Armário superior com luz e canto arredondado', '176 × 100 × 35')
caixa(it, 176, 100, 35, OW15, ndiv=1, base_ext=True)
giro(it, 3, 53, 97, OW18, pux=''); P(it, 'Fechamento arredondado', 100, 15, 2, OW18); F(it, 'Curvatura', 1, 'Canto boleado')
prat(it, 2, 80, 33); chanfro(it, 1.6); led(it, 1.6)
it = item('Cozinha', 'Torre quente e aéreo da geladeira', '145 × 260 × 60')
caixa(it, 65, 250, 60, OW18, lat_ext=2)
gavetas(it, 1, 65, 80, 55, OW18, pux='', nome='Gavetão')
P(it, 'Nichos do forno e do micro · bases', 61, 58, 3, OW18)
giro(it, 1, 65, 30, OW18, pux='')
P(it, 'Basculante', 72, 30, 2, OW18); F(it, 'Dobradiça', 4, 'Dobradiça Hettich'); F(it, 'Pistão', 4, 'Pistão com amortecimento')
caixa(it, 80, 35, 60, OW15, base_ext=True)
chanfro(it, 2.9)
it = item('Cozinha', 'Cristaleira com vidro e luz, e armários do aparador', '75 × 170 + 190 × 78 + 115 × 100')
caixa(it, 75, 170, 30, OW18, base_ext=True, topo_ext=True)
P(it, 'Porta · quadro de 3 cm', 167, 37.5, 2, OW18, 4.1); M2(it, 'Vidro incolor', 31, 161, 2, 'Vidro temperado')
F(it, 'Dobradiça', 8, 'Dobradiça Hettich'); prat(it, 4, 71, 28); led(it, 3.2)
caixa(it, 150, 78, 58, NC15, ndiv=1, lat_ext=1)
gavetas(it, 2, 75, 15, 52, NC18, pux=''); giro(it, 4, 37.5, 63, NC18, pux=''); prat(it, 2, 72, 56)
P(it, 'Nicho lateral · prateleiras arredondadas', 40, 58, 4, NC18, 0.5)
moldura(it, 6); pux(it, 8)
caixa(it, 75, 100, 30, OW15, base_ext=True); giro(it, 2, 37.5, 96, OW18, pux=''); prat(it, 1, 71, 28)
P(it, 'Prateleiras abertas arredondadas', 40, 28, 3, OW18, 0.5); F(it, 'Pontas arredondadas', 2, 'Canto boleado')
chanfro(it, 0.75)

# ══ LAVANDERIA ═══════════════════════════════════════════════════════════
it = item('Lavanderia', 'Armário do tanque e armário inferior com tulha', '70 + 140 × 78')
caixa(it, 70, 78, 58, NC15, lat_ext=1); giro(it, 2, 35, 76, NC18, pux='')
caixa(it, 140, 78, 42, NC15, ndiv=2, lat_ext=1); giro(it, 2, 47, 76, NC18, pux='')
P(it, 'Frente da tulha', 46, 76, 1, NC18); F(it, 'Kit tulha basculante', 1, 'Kit tulha')
prat(it, 1, 46, 40); pux(it, 5)
it = item('Lavanderia', 'Armário alto raso e prateleiras com cabideiro', '80 × 273 × 24 · 2 × 140 × 25')
caixa(it, 80, 263, 24, OW15, ndiv=1)
P(it, 'Painel fixo', 259, 38, 1, OW18); P(it, 'Porta de correr', 259, 38, 1, OW18)
F(it, 'Sistema de correr leve', 1, 'Sistema de correr leve'); F(it, 'Desempenador', 1, 'Desempenador de porta')
prat(it, 2, 38, 22); pux(it, 1); F(it, 'Recorte do registro', 1, 'Canto boleado')
P(it, 'Prateleira em Nogueira', 140, 25, 2, NC18, 2.8); F(it, 'Fixação invisível', 4, 'Fixação invisível')
F(it, 'Cabideiro em perfil metálico preto', 1, 'Cabideiro')

# ══ SUÍTE ════════════════════════════════════════════════════════════════
it = item('Suíte', 'Cabeceira emoldurada com estofado e painel ripado', '390 × 105 · 180 × 265')
painel(it, 390, 105, NC18, 'Cabeceira'); P(it, 'Moldura', 390, 5, 2, NC18, 7.8)
P(it, 'Base dos estofados', 255, 40, 1, BR15, 0); M2(it, 'Estofado em linho bege', 255, 40, 1, 'Estofado')
painel(it, 108, 265, NC18, 'Painel liso'); ripado(it, 72, 265, NC18, ripa=4, vao=4)
it = item('Suíte', 'Penteadeira suspensa e mesas de cabeceira', '180 × 7 × 50 · 2 × 45 × 30 × 30')
caixa(it, 180, 7, 50, NC18, ndiv=3, base_ext=True, topo_ext=True)
gavetas(it, 4, 42, 5, 45, NC15, pux='cava'); F(it, 'Canto arredondado', 1, 'Canto boleado')
F(it, 'Pé em metalon preto', 1, 'Pé metálico')
caixa(it, 45, 30, 30, NC18, base_ext=True, topo_ext=True); caixa(it, 45, 30, 30, NC18, base_ext=True, topo_ext=True)
gavetas(it, 4, 35, 15, 27, NC15, pux=''); F(it, 'Cantos arredondados', 2, 'Canto boleado'); pux(it, 4)

# ══ QUARTO INFANTIL ══════════════════════════════════════════════════════
it = item('Quarto infantil', 'Estante com gaveteiro colorido e torre de nichos', '167 × 271 × 50')
caixa(it, 167, 75, 50, OW18, ndiv=3, base_ext=True, topo_ext=True)
P(it, 'Frentes de gaveta em Mint', 40.5, 30.5, 4, MI18); P(it, 'Frentes de gaveta em Azul Sereno', 40.5, 30.5, 4, 'MDF Azul Sereno 18')
gavetas(it, 8, 40, 30, 45, BR15, pux='espaçado')
F(it, 'Puxador de marcenaria', 8, 'Cava usinada')
caixa(it, 45, 196, 30, OW18, base_ext=True, topo_ext=True, fundo=False)
P(it, 'Nichos · prateleiras', 39, 28, 5, OW18, 0.39)
P(it, 'Fundos coloridos dos nichos', 39, 30.5, 3, MI15, 0); P(it, 'Fundos coloridos', 39, 30.5, 3, AZ15, 0)
it = item('Quarto infantil', 'Escrivaninha, placa com nome e rodateto', '100 × 75 × 50 · placa · rodateto')
P(it, 'Laterais de borda arredondada', 75, 50, 2, OW18); F(it, 'Bordas arredondadas', 2, 'Canto boleado')
P(it, 'Tampo em Mint', 92, 50, 1, MI18); P(it, 'Prateleira inferior', 92, 40, 1, OW18)
P(it, 'Placa com nome recortada em CNC', 60, 10, 1, MI18); F(it, 'Recorte CNC das letras', 1, 'Canto boleado')
P(it, 'Rodateto em Mint', 275, 10, 3, MI18, 8.25)

AMBIENTES = list(dict.fromkeys(i['amb'] for i in ITENS))
