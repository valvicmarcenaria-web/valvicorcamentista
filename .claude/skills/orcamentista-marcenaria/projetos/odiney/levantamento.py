# -*- coding: utf-8 -*-
"""ODINEY — levantamento da casa  [16/11/2026]
Projeto executivo de interiores, Rev. 001, abril/2026, 104 pranchas A3 (pasta "odiney" no Drive).
Leitura em quatro partes (_leitura-0*.md nesta pasta); aqui viram peças, ferragens e terceiros.

Cores: MDF Areia Matt (Guararapes), Carvalho Hanover e Titânio (Duratex), Frapê e Verde Jade
(Arauco) · todas no preço da linha de cor (550 a de 15, 700 a de 18) · interior em Branco TX onde
o projeto não pede cor por dentro.
Ferragem: HETTICH (padrão da casa até o Jonathan dizer outra coisa).
⛔ Fora: pedra (bancadas, tampos, caixa do nicho, sóculos, rodapé), eletros, metais, louças, box,
   espelhos soltos, móveis comprados prontos (cabeceira Mira II, bancos, poltronas, cama, puffs),
   portas Pormade, boiseries pintadas, forro e sanefas de gesso, tampo da mesa em madeira maciça.
"""
ITENS = []
AM15, AM18 = 'MDF Areia Matt 15', 'MDF Areia Matt 18'
CH15, CH18 = 'MDF Carvalho Hanover 15', 'MDF Carvalho Hanover 18'
TI18 = 'MDF Titânio 18'
FR15, FR18 = 'MDF Frapê 15', 'MDF Frapê 18'
VJ15 = 'MDF Verde Jade 15'
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

# ══ 01 · HALL DE ACESSO ══════════════════════════════════════════════════
it = item('Hall de acesso', 'Prateleira iluminada atravessando o espelho', '185 × 3 × 20')
P(it, 'Prateleira · duas faces de 15', 185, 20, 2, CH15, 3.7)
F(it, 'Pontas arredondadas e recorte do espelho', 1, 'Canto boleado')
F(it, 'Fixação invisível', 4, 'Fixação invisível')
led(it, 1.85)

# ══ 02 · SALA DE TV E VARANDA ════════════════════════════════════════════
it = item('Sala de TV', 'Home suspenso com gavetões e nicho', '495 × 50 × 50')
caixa(it, 495, 50, 50, AM18, ndiv=5, base_ext=True)
gavetas(it, 5, 74.5, 33, 45, AM15, pux='cava')
P(it, 'Nicho em Carvalho (forro)', 114, 50, 3, CH15)
F(it, 'Fixação do home suspenso (jogo)', 3, 'Fixação invisível')

it = item('Sala de TV', 'Painel em Titânio com frisos metálicos dourados', '495 × 560')
painel(it, 495, 560, TI18, 'Painel Titânio')
F(it, 'Friso metálico dourado (m)', 53, 'Perfil metálico dourado')

it = item('Sala de TV', 'Cristaleira com portas de vidro e suporte de vinhos', '195 × 280 × 55 + lateral')
caixa(it, 195, 280, 55, CH18, ndiv=1, base_ext=True, topo_ext=True)
P(it, 'Forro interno em Areia Matt', 270, 189, 1, AM15, 0)
P(it, 'Prateleira com rasgo de LED', 189, 50, 2, AM15, 3.8)
M2(it, 'Porta de vidro incolor com quadro', 46, 105, 4, 'Porta de vidro incolor')
M2(it, 'Porta de vidro incolor com quadro (baixo)', 63, 87, 2, 'Porta de vidro incolor')
F(it, 'Dobradiça para porta de vidro', 12, 'Dobradiça Hettich')
P(it, 'Suporte de vinhos em Areia Matt', 64, 47, 6, AM18)
led(it, 3.8)
P(it, 'Painel lateral em Carvalho', 280, 55, 1, CH18)

it = item('Sala de TV', 'Painel em Carvalho com porta de correr embutida (sala e cozinha)', '235 × 280 + porta')
painel(it, 235, 280, CH18, 'Painel do lado da sala')
porta_passagem(it, 110, 210, CH18, 'correr')
P(it, 'Porta · contraface em Carvalho (lado da cozinha)', 210, 110, 1, CH18)

# ══ 03 · COZINHA ═════════════════════════════════════════════════════════
it = item('Cozinha', 'Armário da pia, almofadado', '475 × 78 × 70')
caixa(it, 475, 78, 68, AM15, ndiv=8, lat_ext=1)
giro(it, 5, 55, 78, AM18, pux='')
gavetas(it, 2, 84, 39, 60, AM18, pux='', nome='Gavetão')
gavetas(it, 4, 51, 19.5, 60, AM18, pux='', nome='Gaveta')
P(it, 'Porta-pano · frente e bandeja', 30, 78, 1, AM18)
F(it, 'Corrediça · porta-pano', 1, 'Corrediça Hettich')
P(it, 'Frente fixa estreita', 15, 78, 1, AM18)
prat(it, 5, 55, 68)
almofadar(it, 12); pux(it, 12)

it = item('Cozinha', 'Ilha · torres de forno e micro-ondas', '180 × 78 × 80')
caixa(it, 180, 78, 78, AM15, ndiv=2, lat_ext=0)
P(it, 'Lateral de encosto', 78, 78, 2, BR15, 0.78)
gavetas(it, 1, 77, 25, 60, AM18, pux='')
giro(it, 1, 20, 78, AM18, pux='')
P(it, 'Base dos eletros', 77, 76, 2, BR18, 0.77)
almofadar(it, 2); pux(it, 2)

it = item('Cozinha', 'Painel em Carvalho do lado da cozinha', '430 × 277')
painel(it, 430, 277, CH18, 'Painel do lado da cozinha')

# ══ 04 · DESPENSA ════════════════════════════════════════════════════════
it = item('Despensa', 'Prateleiras em L com chumbador oculto', '150 + 175 · 5 níveis')
prat_grossa(it, 5, 150, 50, AM15, led=False)
prat_grossa(it, 5, 175, 35, AM15, led=False)

# ══ 05 · LAVANDERIA ══════════════════════════════════════════════════════
it = item('Lavanderia', 'Armário superior almofadado com LED', '315 × 110 × 35')
caixa(it, 315, 110, 35, AM15, ndiv=5, base_ext=True)
prat(it, 6, 52.5, 35)
giro(it, 6, 52.5, 110, AM18, pux='')
almofadar(it, 6); pux(it, 6)
led(it, 3.15)

it = item('Lavanderia', 'Armários inferiores almofadados', '245 × 78 × 70 + 165 × 78 × 60')
caixa(it, 245, 78, 68, AM15, ndiv=4, lat_ext=1)
giro(it, 4, 49, 78, AM18, pux='')
gavetas(it, 4, 49, 19.5, 60, AM18, pux='')
caixa(it, 165, 78, 58, AM15, ndiv=1, lat_ext=1)
giro(it, 4, 41, 78, AM18, pux='')
prat(it, 6, 49, 60)
almofadar(it, 12); pux(it, 12)

it = item('Lavanderia', 'Nicho suspenso e despenseiro', '165 × 70 × 35 · 40 × 260 × 60')
caixa(it, 165, 70, 35, AM18, base_ext=True, topo_ext=True)
P(it, 'Forro interno em Carvalho', 159, 54, 1, CH15, 0)
P(it, 'Caixa inferior com LED', 149, 15, 2, AM15)
led(it, 3.1)
caixa(it, 40, 260, 60, AM15)
prat(it, 3, 37, 58)
giro(it, 1, 40, 260, AM18, pux='')
almofadar(it, 1); pux(it, 1)

# ══ 06 · LAVABO ══════════════════════════════════════════════════════════
it = item('Lavabo', 'Prateleira ripada em Carvalho', '100 × 3 × 50')
P(it, 'Quadro da prateleira', 100, 3, 2, CH18); P(it, 'Quadro · laterais', 44, 3, 2, CH18)
ripado(it, 94, 44, CH18, ripa=3, vao=1, base=False)
F(it, 'Fixação invisível', 2, 'Fixação invisível')

# ══ 07 · QUARTO 01 ═══════════════════════════════════════════════════════
it = item('Quarto 01', 'Roupeiro com portas de correr espelhadas', '300 × 280 × 60')
caixa(it, 300, 262, 60, AM18, ndiv=2)
interno(it, 96, prat=8, cab=2, gav=[(15, 96), (15, 96), (20, 96), (20, 96), (20, 96)], sap=4, calc=1, k=AM15)
M2(it, 'Porta de correr espelhada, perfil cromado', 97, 255, 3, 'Porta de espelho em alumínio')
F(it, 'Sistema de correr 3 folhas', 1, 'Sistema de correr 3 folhas')
P(it, 'Faixas de acabamento (topo, base e laterais)', 300, 13, 2, AM18)

it = item('Quarto 01', 'Home suspenso ripado em Carvalho', '240 × 55 × 45')
caixa(it, 240, 55, 45, CH18, ndiv=3, base_ext=True)
giro(it, 4, 60, 55, CH18, pux='')
ripado(it, 240, 55, CH18, ripa=4, vao=2, base=False, nome='Ripado das portas')
F(it, 'Fecho toque', 4, 'Fecho toque')

it = item('Quarto 01', 'Painel em Carvalho, ripado e cabeceira estofada', '340 × 225 + ripado 7,4 m')
painel(it, 340, 225, CH18, 'Painel atrás da cama')
ripado(it, 740, 40, AM18, ripa=2, vao=2, nome='Ripado sob o forro')
P(it, 'Base da cabeceira estofada', 300, 105, 1, BR15, 0)
M2(it, 'Estofado da cabeceira', 300, 105, 1, 'Estofado')

it = item('Quarto 01', 'Criados com pés de serralheria', '2 × 50 × 55 × 45')
P(it, 'Criado · caixa', 50, 45, 8, AM18)
gavetas(it, 4, 47, 18.5, 40, AM15, pux='')
pux(it, 4); pes(it, 2)

# ══ 08 · BANHEIRO SOCIAL ═════════════════════════════════════════════════
it = item('Banheiro social', 'Armário de gavetões suspenso', '150 × 25 × 55')
caixa(it, 150, 25, 55, CH18, ndiv=2, base_ext=True)
gavetas(it, 3, 50, 25, 50, CH15, pux='cava', nome='Gavetão')

# ══ 09 · SUÍTE MASTER ════════════════════════════════════════════════════
it = item('Suíte master', 'Painel frisado e muxarabi em Carvalho com LED', '435 × 265')
painel(it, 435, 145, CH18, 'Painel frisado')
F(it, 'Frisos de 1 cm (usinagem, m)', 4.35, 'Cava usinada')
P(it, 'Muxarabi 5×5 em Carvalho', 120, 435 / 2, 2, CH18, 2 * 1.2)
M2(it, 'Usinagem CNC do muxarabi', 435, 120, 1, 'Usinagem CNC muxarabi')
led(it, 4.35)

it = item('Suíte master', 'Mesas de cabeceira com pés dourados', '120 × 60 × 50 e 60 × 60 × 60')
P(it, 'Mesa esquerda · tampo, base e laterais', 120, 50, 3, FR18)
gavetas(it, 1, 116, 20, 45, FR15, pux='', nome='Gavetão')
P(it, 'Mesa direita · tampo, base e laterais', 60, 60, 3, FR18)
gavetas(it, 2, 56, 10, 55, FR15, pux='')
pux(it, 3); pes(it, 2)

it = item('Suíte master', 'Bancada suspensa com gavetões', '345 × 20 × 55')
caixa(it, 345, 20, 55, FR18, ndiv=4, base_ext=True, topo_ext=True)
gavetas(it, 5, 69, 15, 50, FR15, pux='cava', nome='Gavetão')
F(it, 'Fixação do suspenso (jogo)', 3, 'Fixação invisível')

it = item('Suíte master', 'Painel de TV e painel lateral em Carvalho, prateleira em Frapê', '365 + 230 × 265')
painel(it, 365, 265, CH18, 'Painel de TV')
painel(it, 230, 265, CH18, 'Painel lateral')
P(it, 'Prateleira · duas faces', 225, 30, 2, FR15, 5.1)
F(it, 'Fixação invisível', 4, 'Fixação invisível')

# ══ 10 · CLOSET MASTER ═══════════════════════════════════════════════════
it = item('Closet master', 'Closet aberto em U, Frapê com interno em Carvalho', '950 de frente × 280 × 60')
caixa(it, 950, 274, 60, FR18, ndiv=10)
P(it, 'Forro interno em Carvalho', 270, 80, 12, CH15, 0)
P(it, 'Fechamentos de canto', 280, 60, 3, FR18)
interno(it, 80, prat=14, cab=7, sap=12, k=CH15)
gavetas(it, 9, 75.5, 17, 55, FR15, pux='cava')
M2(it, 'Porta de correr espelhada', 78, 261, 1, 'Porta de espelho em alumínio')
F(it, 'Sistema de correr', 1, 'Sistema de correr Dominus')
F(it, 'Prateleira de vidro com serralheria dourada', 5, 'Prateleira de vidro com serralheria')
led(it, 3.2)

# ══ 11 · BANHEIRO MASTER ═════════════════════════════════════════════════
it = item('Banheiro master', 'Armário suspenso com nicho central', '350 × 30 × 58')
caixa(it, 350, 30, 58, CH18, ndiv=4, base_ext=True)
giro(it, 4, 58.5, 30, CH15, pux='')
F(it, 'Fecho toque', 4, 'Fecho toque')

# ══ 12 · HALL ÍNTIMO ═════════════════════════════════════════════════════
it = item('Hall íntimo', 'Armário em Frapê com nicho iluminado em Carvalho', '295 × 260 × 60')
caixa(it, 295, 260, 60, FR18, ndiv=5)
prat(it, 10, 49, 58)
giro(it, 3, 49, 260, FR18, pux='')
giro(it, 3, 49, 90, FR18, pux='')
giro(it, 3, 49, 75, FR18, pux='')
P(it, 'Nicho em Carvalho (forro)', 143, 91, 1, CH15, 0); P(it, 'Nicho · laterais, base e topo', 143, 58, 2, CH15)
F(it, 'Fecho toque', 9, 'Fecho toque')
led(it, 1.45)

# ══ 13 · SUÍTE HÓSPEDES ══════════════════════════════════════════════════
it = item('Suíte hóspedes', 'Roupeiro de correr em Frapê, uma folha espelhada', '270 × 280 × 60')
caixa(it, 270, 270, 60, FR18, ndiv=2)
interno(it, 85, prat=7, cab=2, gav=[(15, 85), (15, 85), (20, 85), (20, 85), (20, 85)], sap=8, calc=1)
P(it, 'Porta de correr em Frapê', 260, 87, 2, FR18)
F(it, 'Desempenador de porta', 4, 'Desempenador de porta')
M2(it, 'Porta de correr espelhada', 87, 260, 1, 'Porta de espelho em alumínio')
F(it, 'Sistema de correr 3 folhas', 1, 'Sistema de correr 3 folhas')
F(it, 'Puxador perfil preto (m)', 7.8, 'Perfil de proteção de piso')

it = item('Suíte hóspedes', 'Home suspenso com gavetões', '225 × 31 × 50')
caixa(it, 225, 31, 50, FR18, ndiv=3, base_ext=True, topo_ext=True)
gavetas(it, 4, 56, 28, 45, CH15, pux='cava', nome='Gavetão')

it = item('Suíte hóspedes', 'Cabeceira: painéis ripados em Carvalho e painel Frapê com frisos', '345 × 265')
painel(it, 174, 265, CH18, 'Painéis lisos em Carvalho')
ripado(it, 102, 265, CH18, base=False, nome='Ripado em Carvalho')
painel(it, 171, 250, FR18, 'Painel em Frapê')
F(it, 'Friso metálico preto (m)', 12.5, 'Perfil metálico dourado')

it = item('Suíte hóspedes', 'Mesa de cabeceira com pés de serralheria', '70 × 60 × 50')
P(it, 'Mesa · tampo, base e prateleira', 70, 50, 3, FR18)
gavetas(it, 1, 70, 15, 45, FR15, pux='')
pux(it, 1); pes(it, 1)

# ══ 14 · BANHEIRO SUÍTE HÓSPEDES ═════════════════════════════════════════
it = item('Banheiro suíte hóspedes', 'Armário suspenso iluminado e prateleiras', '155 × 30 × 48')
caixa(it, 155, 30, 48, CH18, base_ext=True)
gavetas(it, 2, 77, 27, 43, CH15, pux='cava', nome='Gavetão')
P(it, 'Prateleira inferior (duas faces)', 155, 48, 2, CH15, 3.1)
P(it, 'Prateleiras sobre a bacia (duas faces)', 65, 22, 4, CH15, 1.3)
F(it, 'Fixação invisível', 6, 'Fixação invisível')
led(it, 1.55)

# ══ 15 · SUÍTE FILHA ═════════════════════════════════════════════════════
it = item('Suíte filha', 'Estante e home suspenso em Frapê com Carvalho', '60 × 205 · 235 × 40 × 35')
P(it, 'Estante · quadro e divisórias (3 cm)', 205, 30, 6, FR18)
P(it, 'Estante · prateleiras', 31, 29, 7, FR18, 0.31)
P(it, 'Estante · fundos em Carvalho', 205, 60, 1, CH15, 0)
giro(it, 2, 26, 55, CH15, pux='')
caixa(it, 235, 37, 35, FR18, ndiv=4, base_ext=True)
P(it, 'Tampo em Carvalho', 235, 35, 1, CH18)
giro(it, 4, 37, 37, FR15, pux='')
gavetas(it, 2, 44, 20, 30, FR15, pux='')
pux(it, 8)

it = item('Suíte filha', 'Painel de TV e ripados com portas embutidas', '110 × 205 + ripados até o forro')
painel(it, 110, 205, FR18, 'Painel de TV')
ripado(it, 200, 265, FR18, nome='Ripado da TV')
ripado(it, 135, 210, FR18, nome='Ripado lateral até o piso')
ripado(it, 90, 280, FR18, nome='Ripado do acesso ao closet')
porta_passagem(it, 80, 210, FR18, 'giro')
porta_passagem(it, 88, 210, FR18, 'giro')

it = item('Suíte filha', 'Bancada ripada e mesa de cabeceira ripada', '220 × 18 × 50 · 100 × 45 × 50')
caixa(it, 220, 18, 50, FR18, ndiv=3, base_ext=True, topo_ext=True)
gavetas(it, 4, 54, 15, 45, FR15, pux='')
ripado(it, 220, 15, FR18, ripa=3, vao=1, base=False, nome='Ripado da bancada')
caixa(it, 100, 45, 50, FR18, ndiv=1, base_ext=True, topo_ext=True)
giro(it, 2, 50, 45, FR15, pux='')
ripado(it, 100, 45, FR18, ripa=3, vao=1, base=False, nome='Ripado da mesa')
F(it, 'Fecho toque', 6, 'Fecho toque')

it = item('Suíte filha', 'Criado oval com gavetas curvas e cabeceira estofada', '80 × 55 × 45 · 155 × 270')
P(it, 'Criado oval · caixa curva', 80, 45, 4, FR18)
gavetas(it, 3, 60, 14, 40, FR15, pux='')
F(it, 'Usinagem curva das frentes e da caixa', 2, 'Canto boleado')
pux(it, 3); pes(it, 1)
P(it, 'Base da cabeceira', 270, 155, 1, BR15, 0)
M2(it, 'Estofado em gomos, suede', 155, 270, 1, 'Estofado')

# ══ 16 · BANHEIRO SUÍTE FILHA ════════════════════════════════════════════
it = item('Banheiro suíte filha', 'Armário em Verde Jade com nicho e prateleiras suspensas', '155 × 55 × 48')
caixa(it, 155, 55, 48, VJ15, ndiv=2, base_ext=True)
gavetas(it, 3, 39, 18, 43, VJ15, pux='cava')
giro(it, 2, 39, 55, VJ15, pux='cava')
P(it, 'Nicho em Carvalho', 38, 48, 3, CH15)
P(it, 'Prateleiras em Verde Jade', 76, 18, 2, VJ15, 1.9)
F(it, 'Estrutura de metalon dourado das prateleiras', 1, 'Serralheria metalon')

# ══ 17 · CLOSET FILHA ════════════════════════════════════════════════════
it = item('Closet filha', 'Roupeiro em L com portas almofadadas e palhinha', '310 + 270 × 280 × 60')
caixa(it, 520, 263, 60, AM15, ndiv=7)
interno(it, 61, prat=17, cab=10, gav=[(15, 61), (15, 61), (20, 61), (21, 61), (20, 61)], sap=8, calc=1, k=AM15)
giro(it, 4, 62, 263, FR18, pux='')
giro(it, 4, 52, 263, FR18, pux='')
almofadar(it, 8)
M2(it, 'Palhinha natural nas portas', 50, 165, 8, 'Palha natural')
pux(it, 8)
P(it, 'Faixas de topo e base', 290, 17, 2, FR18)

AMBIENTES = list(dict.fromkeys(i['amb'] for i in ITENS))

DUVIDAS = [
 'Linha de ferragem, RT e comissão: lançado HETTICH, RT 10% e sem comissão, até você confirmar.',
 'Todas as cores (Areia Matt, Carvalho Hanover, Titânio, Frapê, Verde Jade) no preço de chapa de cor.',
 'Porta embutida entre sala e cozinha: lida como UMA porta com as duas faces em Carvalho (painel 235 × 280 na sala e 430 × 277 na cozinha).',
 'Portas de baixo da cristaleira: lidas como vidro, como as de cima.',
 'Tampo da mesa em madeira maciça (~260 × 110): FORA, é madeira maciça, não MDF.',
 'Boiseries (quarto, hall íntimo, suíte master, suíte filha): lidas como moldura pintada, FORA.',
 'Interno do armário do hall íntimo não detalhado: lançadas 10 prateleiras.',
 'Gavetas atrás da porta espelhada do closet master: consideradas reais. LED sob as prateleiras do closet só aparece no render: FORA.',
 'Prateleira do hall de acesso sem material na prancha: lançada em Carvalho Hanover.',
 'Muxarabi 5×5 da suíte master: usinagem CNC a R$ 400 o m², a cotar.',
 'Pés de serralheria (criados e mesas de cabeceira) a R$ 300 o jogo; prateleiras de vidro com serralheria dourada do closet a R$ 450 cada; metalon dourado do banho da filha a R$ 600: tudo a cotar.',
 'Estofados (cabeceira do quarto 01 e da suíte filha) a R$ 600 o m²; a da filha é em gomos, pode sair mais.',
 'Puxadores Zen Design a R$ 45 a peça em média; palhinha natural a R$ 650 o m²; frente almofadada a R$ 40 de usinagem por frente.',
]
