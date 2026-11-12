# -*- coding: utf-8 -*-
"""ED. MÔNICA SALLES — academia e espaço gourmet · levantamento  [12/11/2026]
Detalhamento OCAPI Arquitetura (arq. Dalila Souza, colab. Marina Albarez), R00 de
06/11/2026: Gourmet em 4 folhas A3 e Academia em 3 folhas A3, 1/25, cotadas; e a
Apresentação R02 (renders). "Medidas a conferir no local."

⚠ TODO acabamento está "a definir" na prancha: orçado no preço da linha de cor/madeirada
  (550 a de 15, 700 a de 18), interior em Branco TX. Puxador "a definir": lançado cava.
⛔ Fora: pedra (bancadas, rodabanca até o teto, bancada com pés, mesa de jantar), eletros,
  equipamentos de academia, TV, espelho colado direto na parede (não faz parte de móvel).
As linhas: o levantamento lança a HETTICH e o precos.py troca corrediça/dobradiça (Blum).
"""
ITENS = []
AD15, AD18 = 'MDF acabamento a definir 15', 'MDF acabamento a definir 18'
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



# ══ 01 · ESPAÇO GOURMET ══════════════════════════════════════════════════
it = item('Espaço gourmet', 'Armário inferior da cozinha com nicho do forno', '325,5 × 78 × 58')
caixa(it, 325.5, 78, 57.5, AD15, ndiv=6, lat_ext=1)
prat(it, 6, 40, 57.5)
prat(it, 4, 77.5, 57.5)
giro(it, 6, 40, 78, AD15, pux='cava')
P(it, 'Nicho do forno · base reforçada', 82.5, 55, 1, BR18, 0.825)
P(it, 'Rodapé recuado', 325.5, 10, 1, AD15, 3.255)

it = item('Espaço gourmet', 'Portal e painel do bar, dos dois lados', '196,5 × 224 · faces e topos')
painel(it, 196.5, 224, AD18, 'Painel do bar · face 1')
painel(it, 196.5, 224, AD18, 'Painel do bar · face 2')
P(it, 'Topo do bar (cabeceiras)', 224, 34.5, 2, AD18)
P(it, 'Portal · testeira sob o forro', 196.5, 13, 2, AD18)
P(it, 'Portal · fundo da testeira', 196.5, 34.5, 1, AD18)

it = item('Espaço gourmet', 'Painel da TV com portal', '156 × 224')
painel(it, 156, 224, AD18, 'Painel da TV')
P(it, 'Portal · laterais', 224, 15, 2, AD18)
P(it, 'Portal · testeira', 151, 13, 1, AD18)

it = item('Espaço gourmet', 'Abrigo ripado da máquina da sauna, com portas', '83 + 74 × 216,5')
P(it, 'Requadro do abrigo', 216.5, 15, 3, AD18)
P(it, 'Requadro · topo', 83, 15, 1, AD18)
P(it, 'Porta ripada · base', 210, 38.5, 2, AD18)
P(it, 'Lateral ripada · base', 210, 68, 1, AD18)
P(it, 'Ripas 2 cm (usinagem e filetagem)', 210, 2, 2 * 8 + 14, AD18, 4.2)
F(it, 'Dobradiça', 2 * ndob(210), 'Dobradiça Hettich')
F(it, 'Puxador cava (m)', 0.8, 'Cava usinada')
F(it, 'Perfil metálico de proteção (m)', 1.6, 'Perfil de proteção de piso')

# ══ 02 · ACADEMIA ════════════════════════════════════════════════════════
it = item('Academia', 'Painel da TV com perfil metálico', '464,5 × 223')
painel(it, 464.5, 223, AD18, 'Painel da TV')

it = item('Academia', 'Painel com espelho e banco com nicho para colchonetes', '171 × 243 · banco de 55')
painel(it, 171, 178, AD18, 'Painel com espelho')
M2(it, 'Espelho prata colado no painel', 171, 178, 1, 'Espelho colado')
P(it, 'Banco · tampo (20 de espessura, duas faces)', 171, 55, 2, AD18)
P(it, 'Banco · frente e topos do tampo', 171 + 2 * 55, 20, 1, AD18)
P(it, 'Banco · laterais e fundo do nicho', 141, 35, 3, AD15)
P(it, 'Banco · base do nicho', 136, 52, 1, AD15)
P(it, 'Banco · rodapé recuado', 171 + 55, 10, 1, AD15, 2.26)
F(it, 'Lateral abaulada', 1, 'Canto boleado')

it = item('Academia', 'Estante aberta do piso ao teto', '99 × 243 × 58')
caixa(it, 99, 243, 58, AD18, fundo=True)
P(it, 'Prateleira 2,5 (duas faces de 15 coladas)', 94, 56, 12, AD15, 0.94)
P(it, 'Rodapé recuado', 99, 10, 1, AD15, 0.99)

it = item('Academia', 'Porta de correr com perfil metálico', '95,5 × 233')
P(it, 'Porta de correr · face', 233, 95.5, 1, AD18)
P(it, 'Porta de correr · contraface', 233, 95.5, 1, AD18)
F(it, 'Kit de porta de correr de passagem', 1, 'Kit porta de correr de passagem')
F(it, 'Desempenador de porta', 2, 'Desempenador de porta')
F(it, 'Perfil metálico de proteção (m)', 0.96, 'Perfil de proteção de piso')
F(it, 'Puxador cava (m)', 0.7, 'Cava usinada')

AMBIENTES = list(dict.fromkeys(i['amb'] for i in ITENS))

DUVIDAS = [
 'Todos os acabamentos estão "a definir": orçados em MDF de cor/madeirado (550/700). Se for lâmina natural ou laca, a conta muda.',
 'Espelhos prata colados DIRETO NA PAREDE da academia (359 × 213, 172 × 233, 135,5 × 233): não fazem parte de móvel, ficaram FORA. O espelho do painel sobre o banco é nosso (R$ 600 o m²). Confirmar.',
 'Painel do bar (portal): lido como parede revestida dos dois lados, do piso ao forro, com testeira de 13 sob o forro. A prancha não tem corte do portal.',
 'Abrigo ripado da sauna: ripas de 2 com vão de 3 (detalhe 01), sobre base de MDF; portas de abrir com 4 dobradiças cada.',
 'Porta de correr da academia: folha em duas chapas de 18, kit R$ 700 A COTAR, puxador "a definir" lançado como cava.',
 'Armário da cozinha: puxador "a definir" lançado como cava; prateleiras internas conforme a elevação 01 interna.',
 'RT da OCAPI Arquitetura: lançada a 10% (padrão da casa), a confirmar.',
]
