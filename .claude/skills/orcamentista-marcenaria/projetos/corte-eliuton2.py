# -*- coding: utf-8 -*-
"""ELIUTON · Brisas da Pampulha — 2ª FASE: QUARTOS, CLOSETS E SALA DE TV.

⚠ ESTE É O SEGUNDO ORÇAMENTO DO MESMO CLIENTE.
   O primeiro — cozinha, área gourmet, área de serviço e banheiros — FECHOU em
   20/08/2026 a R$ 73.000 (6 conjuntos, condição especial de fechamento).
   Motor: `corte-eliuton.py` · dossiê: `2026-eliuton-brisas-da-pampulha.md`.
   Nada aqui repete aquilo: são os ambientes que ficaram de fora.

FONTES — e a diferença entre elas importa:
  1. `PLANTAS_COTADAS_Executivo1` · folha 02/06 · arq. Luciana Beatriz
     Simplício / Núcleo · 29/10/2025 · UMA folha 2384 × 1684 pt, escala 1:50.
     É PLANTA DE LAYOUT COTADA, não executivo de marcenaria.
  2. `PROJETO_ELIUTON.pdf` · 31 páginas · deck de RENDERS com a marca Valvic.
     Mostra cada móvel, mas NÃO tem uma cota sequer.

⚠⚠ NÃO HÁ ELEVAÇÃO DE MARCENARIA NESTE PACOTE. O primeiro orçamento foi feito
    sobre 18 pranchas de detalhamento a 1:25, com cota peça a peça. Este é
    feito sobre COMPRIMENTO DE PAREDE lido da planta 1:50 + ALTURA ADOTADA
    pelo padrão da casa + a leitura dos renders. É uma base mais fraca, e o
    número tem de ser lido assim. Toda altura e toda profundidade neste motor
    são ADOÇÃO, não cota — estão marcadas uma a uma nas dúvidas.

ESCOPO — 7 ambientes:
  2º pavimento
    1 · Quarto master (suíte 01, 17,20 m²) ..... painel de cabeceira curvo,
          2 criados, painel lateral com espelho orgânico, rack suspenso
    2 · Closet master (closet 02, 7,21 m²) ..... dois lados abertos, cabideiro
          duplo, gaveteiros, sapateira iluminada
    3 · Quarto dos pais (suíte 02, 18,34 m²) ... roupeiro em L com TV embutida
    4 · Quarto da filha (suíte 03, 16,77 m²) ... roupeiro + bancada
    5 · Quarto de visitas (suíte 04, 11,26 m²) . roupeiro de correr
  Térreo
    6 · Escritório (semi-suíte, 9,66 m²) ....... roupeiro + bancada curva +
          painel de TV com nichos
    7 · Sala de TV (15,25 m²) .................. painel com nichos iluminados,
          ripado e bancada suspensa

⛔ MONTAGEM NÃO ENTRA NO CUSTO (equipe é salário fixo) — mas entra no escopo.
"""
from collections import defaultdict
import math

W = 100
CH_C, CH_L = 275.0, 185.0
CH_AREA = 2.75*1.85
A_, LIQF_, B_ = 0.162, 0.88, 0.043
BASE = 1 - A_ - LIQF_*B_
RT_PCT = 0.10
def div(mc, rt=False): return BASE - mc - (LIQF_*RT_PCT if rt else 0.0)
def mc_conferida(p, c): return BASE - c/p

def _pack_faixa(pcs):
    ch = 0; y = x = f = 0.0
    for c, l in pcs:
        if c > CH_C and l <= CH_C: c, l = l, c
        if c > CH_C or l > CH_L: ch += 1; continue
        if x + c > CH_C: y += f; x = 0.0; f = 0.0
        if y + l > CH_L: ch += 1; y = x = f = 0.0
        x += c; f = max(f, l)
    return ch + 1
def _pack_bf(pcs):
    ch = []
    for c, l in pcs:
        if c > CH_C and l <= CH_C: c, l = l, c
        if c > CH_C or l > CH_L: ch.append([CH_L, []]); continue
        best = None
        for s in ch:
            for fx in s[1]:
                if fx[0] >= l and fx[1] >= c and (best is None or fx[1] < best[1]): best = fx
        if best is not None: best[1] -= c; continue
        for s in ch:
            if s[0] + l <= CH_L:
                s[0] += l; s[1].append([l, CH_C - c]); break
        else: ch.append([l, [[l, CH_C - c]]])
    return len(ch)
def nest(items):
    if not items: return 0
    b = [(max(c, l), min(c, l)) for c, l in items]
    ords = [lambda q: -q[1], lambda q: (-q[1], -q[0]), lambda q: -q[0], lambda q: -q[0]*q[1]]
    ch = min(pk(sorted(b, key=k)) for pk in (_pack_faixa, _pack_bf) for k in ords)
    ar = sum(c*l for c, l in items)/10000
    return max(ch, -(-int(ar/(CH_AREA*0.80)*1000)//1000) or 1)

# ── preços · dados/materiais.json (11/06/2026) ────────────────────────────
PRC_COR = {6: 300.0, 15: 500.0, 18: 600.0, 25: 900.0}   # melamínico amadeirado
PRC_BRA = {6: 190.0, 15: 260.0, 18: 330.0, 25: 420.0}   # Branco TX
# ★ GIANDUIA TRAMA — NÃO EXISTE NA BASE (`dados/materiais.json` não tem a
#   linha; o mesmo furo já está registrado no dossiê da Nádia & Maurílio).
#   Adotado no PISO do Melamínico Fosco. "Trama" é TEXTURA, e textura costuma
#   custar ACIMA do fosco liso — o delta calculado aqui é um MÍNIMO.
PRC_GT  = {6: 300.0, 15: 500.0, 18: 600.0, 25: 900.0}
NOME_MAT = {'AM': 'MDF amadeirado', 'BR': 'MDF Branco TX',
            'GT': 'MDF Gianduia Trama'}
def prc(m, e):
    return {'BR': PRC_BRA, 'GT': PRC_GT}.get(m, PRC_COR)[e]

FITA_M, FILET_M, DESPERD = 3.00, 2.50, 1.10
USIN_M   = 25.0        # cava de puxador usinada, por metro
ESQ_M    = 15.0        # ★ meia esquadria — mesma adoção do job da Lídia
CURVA_M  = 60.0        # ★ topo/canto CURVO: raio grande em painel exige corte
                       #   em CNC, fita curva aplicada a quente e lixamento.
                       #   Sem linha na base; adotado por metro de curva.
LED_M    = 66.0        # fita 28 + perfil 38, LED comum (não COB)
DRIVER_UN= 90.0
SUP_PRAT = 8.0         # ★ suporte de prateleira, mesma adoção dos jobs de 2026
CAB_M    = 45.0        # ★ cabideiro em tubo, por metro (barra + suportes)
ESPELHO_M2   = 600.0   # espelho prata, base
ESPELHO_CURVO= 1.80    # ★ multiplicador do espelho de CORTE ORGÂNICO. Corte
                       #   curvo em espelho é lapidação ponto a ponto: a
                       #   espelharia cobra perto do dobro do reto. CONFERIR.
ESTOFADO_M2  = 650.0   # laca/estofado — base "Laca/Pintura R$ 650/m²" como
                       #   proxy do estofador. ★ CONFERIR com o tapeceiro.

# [Jonathan 13/08/2026, 1º orçamento] TRÊS CENÁRIOS DE FERRAGEM, cada um com a
# sua MC — a mesma escada do primeiro job, para o cliente comparar maçã com maçã.
# O Eliuton FECHOU no cenário 2 (Hardt).
HK_XS = 250.0
CENARIOS = [
    ('1 · Telescópica', 'Padrão · telescópica · pistão simples', 0.32,
     dict(dobr=6.0,  corr=40.0,  art=20.0),  '2 anos'),
    ('2 · Hardt', 'Hardt · oculta Hardt · articulador', 0.37,
     dict(dobr=8.0,  corr=70.0,  art=HK_XS), '5 anos'),
    ('3 · Hettich', 'Novisys · oculta Quadro · articulador', 0.42,
     dict(dobr=10.0, corr=120.0, art=HK_XS), '10 anos'),
]
FECHADO = 1            # índice do cenário adotado: o mesmo que ele já fechou

# ── dimensão ITEM ─────────────────────────────────────────────────────────
# Todo registro carrega (ambiente, item). ITEM é a PEÇA DE MOBILIÁRIO — é
# assim que o cliente lê a conta, e é assim que dá para fatiar o escopo.
P, FITA, TERC, LED, USIN, ESQ, CURVA, DUV = [], [], [], [], [], [], [], []
FER = defaultdict(lambda: [0, 0, 0])       # dobradiças · corrediças · articul.
IT, _RF = ['—'], [False]                    # item corrente · é roupeiro?
ROUP, ORD_IT = {}, []                       # (amb, item) -> flag · ordem
def item(nome, roup=False):
    IT[0] = nome; _RF[0] = roup
def _k(a):
    k = (a, IT[0])
    if k not in ROUP: ROUP[k] = _RF[0]; ORD_IT.append(k)
    return k
def add(mat, esp, amb, desc, c, l, q=1):
    P.append((mat, esp, amb, IT[0], desc, c, l, q)); _k(amb)
def fer(a, dobr=0, corr=0, art=0):
    k = _k(a); FER[k][0] += dobr; FER[k][1] += corr; FER[k][2] += art
def fita(a, d, m): FITA.append((_k(a), d, m))
def terc(a, d, v, est=False): TERC.append((_k(a), d, v, est))
def led(a, d, m): LED.append((_k(a), d, m))
def usin(a, m): USIN.append((_k(a), m))
def esq(a, m): ESQ.append((_k(a), m))
def curva(a, m): CURVA.append((_k(a), m))
def duv(a, t): DUV.append((a, t))

LIM_C, LIM_L = 270.0, 180.0
def _partir(c, l):
    if c < l: c, l = l, c
    nc = max(1, math.ceil(c/LIM_C)); nl = max(1, math.ceil(l/LIM_L))
    return [(c/nc, l/nl)]*(nc*nl)
def painel(mat, esp, amb, desc, c, l, q=1):
    for cc, ll in _partir(c, l): add(mat, esp, amb, desc, cc, ll, q)
def gaveta(mat, amb, nome, L, Pf, alt, q=1):
    add(mat, 15, amb, f'{nome} · caixa lateral',       Pf-10, alt, 2*q)
    add(mat, 15, amb, f'{nome} · caixa frente/costas', L-6,   alt, 2*q)
    add(mat, 6,  amb, f'{nome} · fundo de gaveta',     L-6,   Pf-10, q)

# ═══════════════════════════════════════════════════════════════════════════
# MÓDULOS — um roupeiro/closet é sempre a mesma receita; muda a cota.
# ═══════════════════════════════════════════════════════════════════════════
H_ROUP, P_ROUP = 250.0, 60.0      # ★ ADOTADOS: a planta não cota altura nem
H_PAINEL       = 240.0            #   profundidade de nenhum móvel.
P_CLOSET       = 60.0

def corpo(mat, amb, larg, alt, prof, n_div, nome='módulo', fundo='BR'):
    """Caixaria de roupeiro/closet: laterais, tampo, base, fundo e divisórias."""
    add(mat, 15, amb, f'{nome} · lateral', alt, prof, 2)
    painel(mat, 15, amb, f'{nome} · tampo e base', larg-3, prof, 2)
    painel(fundo, 6, amb, f'{nome} · fundo', larg-3, alt-3, 1)
    if n_div: add(mat, 15, amb, f'{nome} · divisória vertical', alt-3, prof, n_div)

def prateleiras(mat, amb, larg, prof, n, nome='prateleira', com_led=False):
    add(mat, 15, amb, nome, larg, prof-1, n)
    terc(amb, f'Suportes de {nome} ({n*4} un)', n*4*SUP_PRAT)
    if com_led: led(amb, f'LED sob {nome}', n*larg/100)

def cabideiro(amb, larg, n=1, com_led=True):
    terc(amb, f'Cabideiro em tubo ({n} × {larg/100:.2f} m)', n*larg/100*CAB_M, est=True)
    if com_led: led(amb, 'LED sobre o cabideiro', n*larg/100)

def gaveteiro(mat, amb, larg, prof, n_gav, alt_gav=18.0, nome='gaveteiro'):
    add(mat, 15, amb, f'{nome} · frente', larg, alt_gav, n_gav)
    gaveta('BR', amb, nome, larg, prof, alt_gav-4, n_gav)
    fer(amb, corr=n_gav)
    usin(amb, n_gav*larg/100)          # cava de puxador na frente
    fita(amb, f'{nome} · frentes', n_gav*2*(larg+alt_gav)/100)


# ═══════════════════════════════════════════════════════════════════════════
# GEOMETRIA — comprimentos LIDOS da planta 1:50; alturas e profundidades
# ADOTADAS. Tudo em cm.
#
# INT = material do INTERNO dos roupeiros e do closet (caixaria, fundos,
# prateleiras e frentes de gaveteiro). 'BR' = Branco TX, o padrão orçado.
# 'GT' = Gianduia Trama, o upgrade. As PORTAS e os criados-mudos NÃO mudam.
# ═══════════════════════════════════════════════════════════════════════════
def montar(INT='BR', so=None):
    """`so` = conjunto de nomes de item que recebem o INT; os demais ficam
    em Branco TX. None = todos os roupeiros e o closet."""
    global P, FITA, TERC, LED, USIN, ESQ, CURVA, DUV, FER, IT, _RF, ROUP, ORD_IT
    P, FITA, TERC, LED, USIN, ESQ, CURVA, DUV = [], [], [], [], [], [], [], []
    FER = defaultdict(lambda: [0, 0, 0])
    IT, _RF = ['—'], [False]
    ROUP, ORD_IT = {}, []
    def INT_():                      # resolvido NO MOMENTO da chamada
        return INT if (so is None or IT[0] in so) else 'BR'

    # ───────────────────────────────────────────────────────────────────────────
    # 1 · QUARTO MASTER — suíte 01, 17,20 m². Parede da cabeceira 85 + 195 + 80 = 360
    # ───────────────────────────────────────────────────────────────────────────
    A = 'Quarto master'
    item('Painel de cabeceira com estofado')
    painel('AM', 15, A, 'painel de cabeceira 3600 × 2400', 360, H_PAINEL)
    painel('AM', 15, A, 'retorno do painel na parede lateral', 150, H_PAINEL)
    curva(A, 3.2)                      # topo curvo do painel, nas duas paredes
    esq(A, (2*(3.60+2.40) + 2*(1.50+2.40)))
    fita(A, 'painel de cabeceira e retorno', 2*(3.60+2.40) + 2*(1.50+2.40))
    terc(A, 'Cabeceira estofada, 2,00 × 1,00 m', 2.0*ESTOFADO_M2, est=True)
    # criados-mudos: 85 e 80 de largura, 3 gavetas cada, bordas arredondadas
    item('Criados-mudos (2)')
    for i, lc in enumerate((85.0, 80.0), 1):
        corpo('BR', A, lc, 50.0, 45.0, 0, nome=f'criado {i}')
        gaveteiro('BR', A, lc-3, 45.0, 3, 14.0, nome=f'criado {i}')
        curva(A, 1.2)
    # ⛔ [Jonathan 07/09] O PAINEL DO ESPELHO ORGÂNICO SAIU DO ESCOPO.
    #    Ele levava embora o painel de 120 × 240 em amadeirado, 2,4 m de curva
    #    e o espelho de corte orgânico (0,96 m² a 1,8× o reto, R$ 1.036,80) —
    #    a maior das adoções ★ do pacote. Com ele some também a dúvida 4.
    item('Rack suspenso de TV')
    corpo('AM', A, 180.0, 35.0, 40.0, 3, nome='rack suspenso')
    add('AM', 18, A, 'rack · porta', 45, 35, 4)
    fer(A, dobr=8)
    curva(A, 1.5)
    usin(A, 4*0.45)
    fita(A, 'rack · frentes e bordas', 4*2*(0.45+0.35) + 2*(1.80+0.35))
    duv(A, 'ALTURA ADOTADA. A planta cota só o comprimento da parede (360). Painel '
           'de cabeceira e painel lateral saíram em 240 de altura, rack suspenso '
           'em 35, criados em 50 — padrão da casa. Sem elevação, é o que dá para '
           'fazer. CONFERIR no local.')
    duv(A, 'o CURVO é o que encarece este quarto: topo do painel de cabeceira, '
           'cantos dos criados e do rack. ★ Adotei R$ 60/m de curva (CNC + fita a '
           'quente + lixamento), sem linha na base. São 8,3 m de curva no quarto.')
    duv(A, 'a cabeceira ESTOFADA foi orçada a R$ 650/m² usando a linha de laca da '
           'base como proxy. ★ CONFERIR com o tapeceiro — pode ser terceirizado '
           'inteiro, e aí sai do nosso escopo.')

    # ───────────────────────────────────────────────────────────────────────────
    # 2 · CLOSET MASTER — closet 02, 7,21 m². Dois lados de 294, aberto.
    # ───────────────────────────────────────────────────────────────────────────
    A = 'Closet master'
    item('Closet aberto · dois lados de 294', roup=True)
    for lado, nome in ((294.0, 'lado A'), (294.0, 'lado B')):
        corpo(INT_(), A, lado, H_ROUP, P_CLOSET, 3, nome=nome, fundo=INT_())
    prateleiras(INT_(), A, 90.0, P_CLOSET, 6, 'prateleira superior', com_led=True)
    prateleiras(INT_(), A, 90.0, P_CLOSET, 5, 'sapateira', com_led=True)   # lado B
    cabideiro(A, 90.0, 4)                       # cabideiro duplo em 2 vãos
    gaveteiro(INT_(), A, 87.0, P_CLOSET, 4, 18.0, nome='gaveteiro A')
    gaveteiro(INT_(), A, 87.0, P_CLOSET, 4, 18.0, nome='gaveteiro B')
    terc(A, 'Drivers da iluminação do closet', 2*DRIVER_UN)
    esq(A, 2*2*(2.94+2.50))
    fita(A, 'bordas aparentes dos dois lados', 2*2*(2.94+2.50) + 11*0.90)
    duv(A, 'o closet é ABERTO, sem portas — é o que os renders mostram. Se entrarem '
           'portas de correr, são ~6 m² de frente a mais e o sistema deslizante.')
    duv(A, 'lado A e lado B saíram com 294 de comprimento, que é a cota da planta '
           'na direção longa do closet (7,21 m²). Profundidade de 60 e altura de '
           '250 são ADOÇÃO.')

    # ───────────────────────────────────────────────────────────────────────────
    # 3 · QUARTO DOS PAIS — suíte/closet 02, 18,34 m². Roupeiro em L: 342 + 230.
    # ───────────────────────────────────────────────────────────────────────────
    A = 'Quarto dos pais'
    item('Roupeiro em L · 342 + 230', roup=True)
    corpo(INT_(), A, 342.0, H_ROUP, P_ROUP, 4, nome='roupeiro · trecho longo', fundo=INT_())
    corpo(INT_(), A, 230.0, H_ROUP, P_ROUP, 2, nome='roupeiro · retorno em L', fundo=INT_())
    add('BR', 18, A, 'roupeiro · porta 570 × 2500', 57, H_ROUP, 10)
    fer(A, dobr=20)
    prateleiras(INT_(), A, 80.0, P_ROUP, 10, 'prateleira do roupeiro')
    cabideiro(A, 80.0, 4, com_led=False)
    gaveteiro(INT_(), A, 77.0, P_ROUP, 5, 18.0, nome='gaveteiro do roupeiro')
    item('Nicho de TV embutido no roupeiro', roup=True)
    add('AM', 15, A, 'nicho da TV embutido no roupeiro · fundo e laterais', 100, 60, 3)
    led(A, 'LED no nicho da TV', 2.0)
    item('Roupeiro em L · 342 + 230', roup=True)
    esq(A, 2*(3.42+2.50) + 2*(2.30+2.50))
    fita(A, 'portas, prateleiras e bordas',
         10*2*(0.57+2.50) + 10*0.80 + 2*(3.42+2.50) + 2*(2.30+2.50))
    duv(A, 'o roupeiro em L saiu com 342 no trecho longo (120 + 140 + 82 da planta) '
           'e 230 no retorno. Dez portas de 57 é a divisão que fecha os 342 + 230 '
           'com folga de dobradiça. CONFERIR a modulação com a arquiteta.')
    duv(A, 'o render mostra TV embutida no roupeiro, com nicho amadeirado. Prevemos '
           'o nicho, o reforço e o passa-cabo; a TV e o ponto são da obra.')

    # ───────────────────────────────────────────────────────────────────────────
    # 4 · QUARTO DA FILHA — suíte 03, 16,77 m². Roupeiro 381 · bancada 166.
    # ───────────────────────────────────────────────────────────────────────────
    A = 'Quarto da filha'
    item('Roupeiro · 381', roup=True)
    corpo(INT_(), A, 381.0, H_ROUP, P_ROUP, 5, nome='roupeiro', fundo=INT_())
    # [Jonathan 07/09] portas DESLIZANTES em sistema Dominus, não mais de abrir.
    # 381 de vão → 4 folhas de 98 sobre 2 trilhos. Três folhas dariam 131 de
    # largura, e 131 × 250 em MDF 18 pesa ~44 kg por folha: fora do Dominus.
    add('BR', 18, A, 'roupeiro · porta de correr 980 × 2500', 98, H_ROUP, 4)
    terc(A, 'Sistema deslizante Dominus, 4 portas', 1150.0, est=True)
    terc(A, 'Trilho Dominus, 2 barras de 3 m', 700.0, est=True)
    terc(A, 'Desempenadores anti-empeno (4 portas × 2)', 8*60.0)
    prateleiras(INT_(), A, 60.0, P_ROUP, 10, 'prateleira do roupeiro')
    cabideiro(A, 60.0, 4, com_led=False)
    gaveteiro(INT_(), A, 57.0, P_ROUP, 4, 18.0, nome='gaveteiro do roupeiro')
    # bancada/penteadeira sob a janela
    item('Bancada/penteadeira · 166')
    add('AM', 25, A, 'bancada 1660 × 450', 166, 45, 1)
    add('AM', 15, A, 'bancada · lateral e montante', 72, 45, 2)
    gaveteiro('AM', A, 60.0, 45.0, 2, 14.0, nome='bancada')
    led(A, 'LED sob a bancada', 1.66)
    esq(A, 2*(1.66+0.45))
    fita(A, 'bancada', 2*(1.66+0.45))
    item('Roupeiro · 381', roup=True)
    esq(A, 2*(3.81+2.50))
    fita(A, 'portas, prateleiras e bordas', 4*2*(0.98+2.50) + 10*0.60 + 2*(3.81+2.50))
    duv(A, 'o roupeiro saiu com 381, que é a cota da faixa de marcenaria na planta. '
           'A bancada de 166 é a cota da parede sob a janela.')
    duv(A, '[Jonathan 07/09] as portas viraram DESLIZANTES em sistema Dominus. '
           'Adotei 4 folhas de 98 sobre 2 trilhos: três folhas dariam 131 de '
           'largura e ~44 kg por folha, acima do que o Dominus comporta. ★ O '
           'sistema de 4 portas (R$ 1.150) e as 2 barras de trilho (R$ 700) são '
           'escala do preço de 3 portas do quarto de visitas — CONFERIR com a '
           'Rometal. Saem 12 dobradiças do pacote.')

    # ───────────────────────────────────────────────────────────────────────────
    # 5 · QUARTO DE VISITAS — suíte 04, 11,26 m². Roupeiro 245.
    # ───────────────────────────────────────────────────────────────────────────
    A = 'Quarto de visitas'
    item('Roupeiro de correr · 245', roup=True)
    corpo(INT_(), A, 245.0, H_ROUP, P_ROUP, 3, nome='roupeiro', fundo=INT_())
    add('BR', 18, A, 'roupeiro · porta de correr 830 × 2500', 83, H_ROUP, 3)
    prateleiras(INT_(), A, 60.0, P_ROUP, 8, 'prateleira do roupeiro')
    cabideiro(A, 60.0, 3, com_led=False)
    gaveteiro(INT_(), A, 57.0, P_ROUP, 4, 18.0, nome='gaveteiro do roupeiro')
    terc(A, 'Sistema deslizante Dominus, 3 portas', 850.0)
    terc(A, 'Trilho Dominus 3 m', 350.0)
    terc(A, 'Desempenadores anti-empeno (3 portas × 2)', 6*60.0)
    esq(A, 2*(2.45+2.50))
    fita(A, 'portas, prateleiras e bordas',
         3*2*(0.83+2.50) + 8*0.60 + 2*(2.45+2.50))
    duv(A, 'o render mostra o roupeiro de visitas com portas LISAS de correr, sem '
           'puxador aparente. Orcei em sistema Dominus (o deslizante de roupeiro '
           'da casa, `ferragens.md`), 3 folhas de 83. Se forem portas de abrir, '
           'saem R$ 1.560 de sistema e entram 6 dobradiças.')

    # ───────────────────────────────────────────────────────────────────────────
    # 6 · ESCRITÓRIO — semi-suíte, 9,66 m². Roupeiro 250 · painel de TV 300.
    # ───────────────────────────────────────────────────────────────────────────
    A = 'Escritório'
    item('Roupeiro · 250', roup=True)
    corpo(INT_(), A, 250.0, H_ROUP, P_ROUP, 3, nome='roupeiro', fundo=INT_())
    add('BR', 18, A, 'roupeiro · porta 620 × 2500', 62, H_ROUP, 4)
    fer(A, dobr=8)
    prateleiras(INT_(), A, 60.0, P_ROUP, 8, 'prateleira do roupeiro')
    cabideiro(A, 60.0, 3, com_led=False)
    gaveteiro(INT_(), A, 57.0, P_ROUP, 3, 18.0, nome='gaveteiro do roupeiro')
    # painel de TV com nichos + bancada de trabalho curva
    item('Painel de TV com nichos · 300')
    painel('AM', 15, A, 'painel de TV com nichos 3000 × 2400', 300, H_PAINEL)
    add('AM', 15, A, 'nicho suspenso · fundo, laterais e prateleira', 90, 30, 6)
    led(A, 'LED nos nichos do painel', 3.6)
    item('Bancada de trabalho curva · 200')
    add('AM', 25, A, 'bancada de trabalho curva 2000 × 600', 200, 60, 1)
    add('AM', 15, A, 'bancada · lateral e montante', 72, 60, 2)
    curva(A, 2.2)                    # a bancada é curva na ponta, e o nicho também
    gaveteiro('AM', A, 60.0, 60.0, 2, 14.0, nome='bancada')
    esq(A, 2*(2.00+0.60))
    fita(A, 'bancada de trabalho', 2*(2.00+0.60))
    item('Painel de TV com nichos · 300')
    esq(A, 2*(3.00+2.40))
    fita(A, 'painel e nichos', 2*(3.00+2.40) + 6*2*(0.90+0.30))
    item('Roupeiro · 250', roup=True)
    esq(A, 2*(2.50+2.50))
    fita(A, 'portas, prateleiras e bordas', 4*2*(0.62+2.50) + 8*0.60 + 2*(2.50+2.50))
    duv(A, 'o escritório tem 9,66 m² e a planta cota 320 de parede. Adotei roupeiro '
           'de 250 e painel de TV de 300 — os dois não cabem na mesma parede, e o '
           'render mostra que não estão. CONFERIR em qual parede vai cada um.')
    duv(A, 'a bancada de trabalho é CURVA na ponta, como o render mostra. Entram '
           '2,2 m de curva. Tampo em 25 mm para não fletir nos 2 m de vão.')

    # ───────────────────────────────────────────────────────────────────────────
    # 7 · SALA DE TV — 15,25 m². Painel de 400 com nichos, ripado e bancada.
    # ───────────────────────────────────────────────────────────────────────────
    A = 'Sala de TV'
    item('Painel de TV com ripado · 400 × 260')
    painel('AM', 15, A, 'painel de TV 4000 × 2600', 400, 260)
    add('AM', 15, A, 'nicho iluminado · fundo, laterais e prateleira', 45, 30, 12)
    led(A, 'LED nos nichos e no rasgo do painel', 7.5)
    terc(A, 'Drivers da iluminação do painel', 2*DRIVER_UN)
    item('Bancada suspensa · 320')
    corpo('AM', A, 320.0, 40.0, 40.0, 3, nome='bancada suspensa')
    add('AM', 18, A, 'bancada suspensa · porta', 80, 40, 4)
    fer(A, dobr=8)
    usin(A, 4*0.80)
    # ripado da faixa inferior do painel — ripa de 3 cm a passo de 6
    item('Painel de TV com ripado · 400 × 260')
    N_RIP = 55
    add('AM', 15, A, 'ripa do painel', 3, 90, N_RIP)
    esq(A, 2*(4.00+2.60))
    fita(A, 'painel, nichos e ripado',
         2*(4.00+2.60) + 12*2*(0.45+0.30) + N_RIP*2*(0.03+0.90))
    item('Bancada suspensa · 320')
    esq(A, 2*(3.20+0.40))
    fita(A, 'bancada suspensa', 4*2*(0.80+0.40) + 2*(3.20+0.40))
    duv(A, 'a sala de TV tem 15,25 m² e o render mostra o painel ocupando a parede '
           'inteira, com faixa de mármore atrás da TV. ⛔ O MÁRMORE É MARMORARIA, '
           'está FORA — prevemos o recorte e o encosto da marcenaria nele.')
    duv(A, 'o ripado da faixa inferior saiu com 55 ripas de 3 cm a passo de 6, que '
           'é a leitura do render. Sem elevação, é estimativa: cada 10 ripas a '
           'mais ou a menos mexem ~R$ 250 no custo.')
    duv(A, 'painel de 400 × 260: a planta dá 15,25 m² de sala mas não cota a parede '
           'do painel. 400 é leitura de escala. CONFERIR.')

    return dict(P=P, FITA=FITA, TERC=TERC, LED=LED, USIN=USIN, ESQ=ESQ,
                CURVA=CURVA, DUV=DUV, FER=dict(FER), ROUP=dict(ROUP),
                ORD_IT=list(ORD_IT))

# ═══════════════════════════════════════════════════════════════════════════
# CÁLCULO — por ITEM. O ambiente é a soma dos seus itens.
# ═══════════════════════════════════════════════════════════════════════════
W = 100
N_CARRETO, R_CARRETO = 3, 600.0     # 7 ambientes em 2 pavimentos
N_VISITA,  R_VISITA  = 2, 250.0
LOG_CHEIO = N_CARRETO*R_CARRETO + N_VISITA*R_VISITA
# ★ só roupeiros: 5 ambientes, ainda em 2 pavimentos — 2 carretos, 2 visitas.
LOG_ROUP  = 2*R_CARRETO + 2*R_VISITA

def brl(v, n=2):
    return f'{v:,.{n}f}'.replace(',', '§').replace('.', ',').replace('§', '.')

def calcular(D, cen, chaves=None, log=None):
    """Fecha o custo. `chaves` restringe o escopo a um subconjunto de itens.

    RATEIO POR CUSTO (regra da casa, 29/08): a chapa é rateada DENTRO de cada
    grupo (material, espessura) pela área que o item ocupa naquele grupo; fita
    e filetagem pela área; usinagem, esquadria, curva, LED, terceirizados e
    ferragem já são por item. Consumíveis e logística seguem proporcionais.
    """
    K = (lambda k: True) if chaves is None else (lambda k: k in chaves)
    P_ = [r for r in D['P'] if K((r[2], r[3]))]
    if not P_: return None
    log = LOG_CHEIO if log is None else log

    por, area_ch, area_it = defaultdict(list), defaultdict(float), defaultdict(float)
    for m, e, a, it, d, c, l, q in P_:
        for _ in range(q): por[(m, e)].append((c, l))
        ar = c*l*q/10000
        area_ch[(m, e)] += ar; area_it[(a, it)] += ar
    CH = {k: nest(v) for k, v in por.items()}
    custo_chapa = sum(n*prc(k[0], k[1]) for k, n in CH.items())
    area_tot, tot_ch = sum(area_ch.values()), sum(CH.values())

    m_fita_expl = sum(m for k, _, m in D['FITA'] if K(k))
    m_fita = max(m_fita_expl, area_tot*2.6)
    custo_fita, custo_filet = m_fita*DESPERD*FITA_M, m_fita*FILET_M
    m_usin = sum(m for k, m in D['USIN'] if K(k))
    m_esq  = sum(m for k, m in D['ESQ']  if K(k))
    m_cur  = sum(m for k, m in D['CURVA'] if K(k))
    m_led  = sum(m for k, _, m in D['LED'] if K(k))
    custo_terc = sum(v for k, _, v, _ in D['TERC'] if K(k))
    f = CENARIOS[cen][3]
    custo_ferr = sum(v[0]*f['dobr'] + v[1]*f['corr'] + v[2]*f['art']
                     for k, v in D['FER'].items() if K(k))
    consum = (custo_chapa + custo_fita)*0.06
    cd = (custo_chapa + custo_fita + custo_filet + m_usin*USIN_M + m_esq*ESQ_M
          + m_cur*CURVA_M + m_led*LED_M + custo_terc + consum + custo_ferr + log)

    # ── rateio por custo, item a item ─────────────────────────────────────
    cdi = defaultdict(float)
    _ar_gr = defaultdict(float)
    for m, e, a, it, d, c, l, q in P_: _ar_gr[(m, e, a, it)] += c*l*q/10000
    for (m, e, a, it), ar in _ar_gr.items():
        cdi[(a, it)] += CH[(m, e)]*prc(m, e) * ar/area_ch[(m, e)]
    for k in area_it:
        cdi[k] += m_fita*area_it[k]/area_tot*(DESPERD*FITA_M + FILET_M)
    for k, m in D['USIN']:
        if K(k): cdi[k] += m*USIN_M
    for k, m in D['ESQ']:
        if K(k): cdi[k] += m*ESQ_M
    for k, m in D['CURVA']:
        if K(k): cdi[k] += m*CURVA_M
    for k, _, m in D['LED']:
        if K(k): cdi[k] += m*LED_M
    for k, _, v, _e in D['TERC']:
        if K(k): cdi[k] += v
    for k, v in D['FER'].items():
        if K(k): cdi[k] += v[0]*f['dobr'] + v[1]*f['corr'] + v[2]*f['art']
    bruto = sum(cdi.values())
    for k in list(cdi): cdi[k] += (consum + log)*cdi[k]/bruto
    assert abs(sum(cdi.values()) - cd) < 0.01, (sum(cdi.values()), cd)
    return dict(cd=cd, cdi=dict(cdi), CH=CH, area_ch=area_ch, area_it=dict(area_it),
                area_tot=area_tot, tot_ch=tot_ch, custo_chapa=custo_chapa,
                m_fita=m_fita, custo_fita=custo_fita, custo_filet=custo_filet,
                m_usin=m_usin, m_esq=m_esq, m_cur=m_cur, m_led=m_led,
                custo_terc=custo_terc, custo_ferr=custo_ferr, log=log)

def repartir(total, cdi, chaves):
    """Distribui um preço FECHADO pelos itens, na proporção do custo direto."""
    base = sum(cdi[k] for k in chaves)
    v = {k: round(total*cdi[k]/base/100)*100 for k in chaves}
    maior = max(chaves, key=lambda k: cdi[k])
    v[maior] += total - sum(v.values())
    assert sum(v.values()) == total
    return v

# ═══════════════════════════════════════════════════════════════════════════
# EXECUÇÃO
# ═══════════════════════════════════════════════════════════════════════════
D  = montar('BR')
DG = montar('GT')
ORD_AMB = list(dict.fromkeys(a for a, _ in D['ORD_IT']))
ITENS   = D['ORD_IT']
ROUPS   = [k for k in ITENS if D['ROUP'][k]]

R = {i: calcular(D, i) for i in range(len(CENARIOS))}
CD_F = R[FECHADO]['cd']
cdi  = R[FECHADO]['cdi']

# ═══════════════════════════════════════════════════════════════════════════
# [Jonathan 07/09/2026] PREÇO CRAVADO ITEM A ITEM — cenário 2 · Hardt · com RT.
# Não é mais rateio: cada linha tem o valor que ele definiu. O painel do
# espelho saiu do escopo. "Na separação dos itens mantenha o valor."
# ═══════════════════════════════════════════════════════════════════════════
PRECO_ITEM = {
    ('Quarto master',     'Painel de cabeceira com estofado'):    11400,
    ('Quarto master',     'Criados-mudos (2)'):                    3700,
    ('Quarto master',     'Rack suspenso de TV'):                  2400,
    ('Closet master',     'Closet aberto · dois lados de 294'):   24000,
    ('Quarto dos pais',   'Roupeiro em L · 342 + 230'):           26500,   # ↓ com o nicho
    ('Quarto dos pais',   'Nicho de TV embutido no roupeiro'):        0,   # vendido junto
    ('Quarto da filha',   'Roupeiro · 381'):                      16500,   # deslizante Dominus
    ('Quarto da filha',   'Bancada/penteadeira · 166'):            2700,
    ('Quarto de visitas', 'Roupeiro de correr · 245'):            14200,
    ('Escritório',        'Roupeiro · 250'):                       9400,
    ('Escritório',        'Painel de TV com nichos · 300'):        5600,
    ('Escritório',        'Bancada de trabalho curva · 200'):      5500,
    ('Sala de TV',        'Painel de TV com ripado · 400 × 260'): 16000,
    ('Sala de TV',        'Bancada suspensa · 320'):               3900,
}
# o nicho é vendido dentro do roupeiro em L — uma linha só na proposta
UNIR = {('Quarto dos pais', 'Nicho de TV embutido no roupeiro'):
        ('Quarto dos pais', 'Roupeiro em L · 342 + 230')}
assert set(PRECO_ITEM) == set(ITENS), (set(PRECO_ITEM) ^ set(ITENS))
INV = sum(PRECO_ITEM.values())
PRAZO = '70 dias corridos'

_fora = [(m, e, a, d, c, l) for m, e, a, it, d, c, l, q in D['P']
         if max(c, l) > CH_C or min(c, l) > CH_L]
if _fora:
    print('\n' + '!'*W + '\nPEÇAS QUE NÃO CABEM NA CHAPA')
    for m, e, a, d, c, l in _fora:
        print(f'  {NOME_MAT[m]} {e} · {a} · {d}: {c:.0f} × {l:.0f}')
    print('!'*W + '\n')

print('═'*W)
print('ELIUTON · BRISAS DA PAMPULHA — 2ª FASE · QUARTOS, CLOSETS E SALA DE TV')
print('═'*W)
print('Planta cotada 1:50 da arq. Luciana Simplício + deck de 31 renders da Valvic.')
print('⚠ SEM ELEVAÇÃO DE MARCENARIA: comprimento é cota, altura e profundidade')
print('  são ADOÇÃO. O 1º orçamento (fechado a R$ 73.000) tinha 18 pranchas a 1:25.')

print('\nPLANO DE CORTE')
r = R[FECHADO]
for k, n in sorted(r['CH'].items(), key=lambda x: (-x[1], x[0])):
    print(f'  {NOME_MAT[k[0]]+" "+str(k[1])+" mm":<26}{r["area_ch"][k]:>7.2f} m²  →  '
          f'{n:>2} ch. × R$ {prc(*k):>7.2f} = R$ {brl(n*prc(*k)):>9}   aprov. '
          f'{r["area_ch"][k]/(n*CH_AREA)*100:>3.0f}%')
print(f'  {"TOTAL":<26}{r["area_tot"]:>7.2f} m²  →  {r["tot_ch"]:>2} chapas{"":>19}'
      f'R$ {brl(r["custo_chapa"]):>9}   médio '
      f'{r["area_tot"]/(r["tot_ch"]*CH_AREA)*100:.0f}%')
print(f'\nFITA E FILETAGEM   {r["m_fita"]:.1f} m · R$ {brl(r["custo_fita"])} + R$ {brl(r["custo_filet"])}')
print(f'USINAGEM DE CAVA   {r["m_usin"]:.1f} m × R$ {brl(USIN_M)}')
print(f'MEIA ESQUADRIA     {r["m_esq"]:.1f} m × R$ {brl(ESQ_M)}')
print(f'★ CURVA            {r["m_cur"]:.1f} m × R$ {brl(CURVA_M)}')
print(f'ILUMINAÇÃO         {r["m_led"]:.1f} m × R$ {brl(LED_M)}')
print(f'TERCEIRIZADOS      R$ {brl(r["custo_terc"])}')
print(f'FERRAGEM (cen. {FECHADO+1})  R$ {brl(r["custo_ferr"])}')
print(f'LOGÍSTICA          R$ {brl(r["log"])}')

print('\n' + '═'*W)
print('PREÇO — três cenários de ferragem, o mesmo desenho em todos')
print('═'*W)
print(f'  {"Cenário":<18}{"Custo direto":>14}{"sem RT":>13}{"MC real":>9}'
      f'{"com RT 10%":>14}{"MC real":>9}   Garantia')
for i, (nome, ferr, mc, _f, gar) in enumerate(CENARIOS):
    cd = R[i]['cd']
    s = round(cd/div(mc, False)/100)*100
    rr = round(cd/div(mc, True)/100)*100
    print(f'  {nome:<18}{"R$ "+brl(cd,0):>14}{"R$ "+brl(s,0):>13}'
          f'{mc_conferida(s, cd)*100:>8.1f}%{"R$ "+brl(rr,0):>14}'
          f'{mc_conferida(rr, cd)*100:>8.1f}%   {gar}')
    print(f'  {"":<18}{ferr}')

MC_BRUTA = mc_conferida(INV, CD_F)
MC_LIQ   = MC_BRUTA - LIQF_*RT_PCT
print(f'\n  ► FECHADO PELO JONATHAN · cenário {CENARIOS[FECHADO][0]} COM RT ... R$ {brl(INV,0)}')
print(f'    Custo direto R$ {brl(CD_F,0)} · MC bruta {MC_BRUTA*100:.1f}% · '
      f'LÍQUIDA DA RT {MC_LIQ*100:.1f}%')
if MC_LIQ < 0.35:
    print(f'    ⚠ {MC_LIQ*100:.1f}% líquida fica ABAIXO do piso de 35% da casa.')
print(f'    R$/m² de chapa: {INV/r["area_tot"]:.0f} com RT · '
      f'{INV/1.10/r["area_tot"]:.0f} sem   (faixa da casa 626–834 · 1º Eliuton 624)')

print('\n' + '─'*W)
print(f'INVESTIMENTO POR AMBIENTE E POR ITEM   (R$ {brl(INV,0)} · cenário '
      f'{CENARIOS[FECHADO][0]}, com RT)')
print('─'*W)
PV = dict(PRECO_ITEM)
print(f'  {"":40}{"m² chapa":>10}{"custo dir.":>13}{"investimento":>14}{"MC":>8}')
for a in ORD_AMB:
    ks = [k for k in ITENS if k[0] == a]
    print(f'  {a}')
    for k in ks:
        mk = '  ◼' if D['ROUP'][k] else '   '
        kk = UNIR.get(k, k)
        cd_k = sum(cdi[x] for x in ITENS if UNIR.get(x, x) == kk) if kk == k else 0
        mc = f'{mc_conferida(PV[kk], cd_k)*100:>6.1f}%' if PV[k] else '     —'
        print(f'  {mk} {k[1]:<35}{R[FECHADO]["area_it"][k]:>6.2f} m²'
              f'{"R$ "+brl(cdi[k],0):>13}{"R$ "+brl(PV[k],0):>14}{mc:>8}')
    if len(ks) > 1:
        print(f'  {"":4}{"subtotal do ambiente":.<35}{sum(R[FECHADO]["area_it"][k] for k in ks):>6.2f} m²'
              f'{"R$ "+brl(sum(cdi[k] for k in ks),0):>13}'
              f'{"R$ "+brl(sum(PV[k] for k in ks),0):>14}')
print(f'  {"TOTAL":<40}{r["area_tot"]:>6.2f} m²{"R$ "+brl(CD_F,0):>13}'
      f'{"R$ "+brl(INV,0):>14}')
print('  ◼ = roupeiro / closet')

print('\n' + '─'*W)
print('SE ELE FECHAR SÓ OS ROUPEIROS   (a prioridade declarada do cliente)')
print('─'*W)
rr = calcular(D, FECHADO, chaves=set(ROUPS), log=LOG_ROUP)
P_ROUPS = sum(PV[k] for k in ROUPS)
MCB_R = mc_conferida(P_ROUPS, rr['cd'])
print(f'  Soma dos itens cravados ........... R$ {brl(P_ROUPS,0)}')
print(f'  Custo direto do pacote sozinho .... R$ {brl(rr["cd"],0)}   '
      f'({rr["area_tot"]:.2f} m² · {rr["tot_ch"]} chapas · aprov. '
      f'{rr["area_tot"]/(rr["tot_ch"]*CH_AREA)*100:.0f}%)')
print(f'  MC bruta {MCB_R*100:.1f}% · LÍQUIDA DA RT {(MCB_R-LIQF_*RT_PCT)*100:.1f}%')
print(f'  Logística reduzida para R$ {brl(LOG_ROUP,0)} (2 carretos, 2 visitas)')
print(f'\n  ⚠ O custo NÃO cai na proporção do preço: os roupeiros são '
      f'{P_ROUPS/INV*100:.0f}% do')
print(f'    preço mas {rr["cd"]/CD_F*100:.0f}% do custo direto. Tirando os 8 itens '
      f'que não são')
print('    roupeiro, o aproveitamento de chapa piora e o frete não cai junto.')
print(f'    A MC ainda fica em {(MCB_R-LIQF_*RT_PCT)*100:.1f}% líquidos — acima do piso.')
print('\n  Os cinco roupeiros, pelos valores cravados:')
for k in ROUPS:
    if PV[k]:
        print(f'    {k[0]+" · "+k[1]:<50}{"R$ "+brl(PV[k],0):>12}')
print(f'    {"TOTAL":<50}{"R$ "+brl(P_ROUPS,0):>12}')

print('\n' + '─'*W)
print('UPGRADE ★ — INTERNO EM MDF GIANDUIA TRAMA')
print('─'*W)
CLOSET_SO = {'Closet aberto · dois lados de 294'}
DC = montar('GT', so=CLOSET_SO)
rg  = calcular(DG, FECHADO)
rgr = calcular(DG, FECHADO, chaves=set(ROUPS), log=LOG_ROUP)
rc  = calcular(DC, FECHADO)
rcr = calcular(DC, FECHADO, chaves=set(ROUPS), log=LOG_ROUP)
inv_c  = round(rc['cd']/div(MC_LIQ, True)/100)*100
inv_cr = round(rcr['cd']/div(MC_LIQ, True)/100)*100
d_cd, d_cdr = rg['cd'] - CD_F, rgr['cd'] - rr['cd']
inv_g  = round(rg['cd']/div(MC_LIQ, True)/100)*100
inv_gr = round(rgr['cd']/div(MC_LIQ, True)/100)*100
# deltas de upgrade, na MC líquida do pacote — é assim que vão para a proposta
DELTA_C  = round((rc['cd']  - CD_F)/div(MC_LIQ, True)/100)*100   # só o closet
DELTA_G  = round((rg['cd']  - CD_F)/div(MC_LIQ, True)/100)*100   # tudo
DELTA_GR = round((rgr['cd'] - rr['cd'])/div(MC_LIQ, True)/100)*100
print('  O QUE MUDA: caixaria, fundos, prateleiras e frentes de gaveteiro dos')
print('  cinco roupeiros e do closet. NÃO mudam as portas (seguem Branco TX)')
print('  nem os criados-mudos do master.')
print(f'\n  {"":34}{"custo direto":>14}{"investimento":>14}{"delta":>12}')
print(f'  {"pacote cheio · interno Branco TX":<34}{"R$ "+brl(CD_F,0):>14}'
      f'{"R$ "+brl(INV,0):>14}{"":>12}')
print(f'  {"pacote cheio · SÓ o closet aberto":<34}{"R$ "+brl(rc["cd"],0):>14}'
      f'{"R$ "+brl(INV+DELTA_C,0):>14}{"+R$ "+brl(DELTA_C,0):>12}')
print(f'  {"pacote cheio · interno Gianduia":<34}{"R$ "+brl(rg["cd"],0):>14}'
      f'{"R$ "+brl(INV+DELTA_G,0):>14}{"+R$ "+brl(DELTA_G,0):>12}')
print(f'  {"só roupeiros · interno Branco TX":<34}{"R$ "+brl(rr["cd"],0):>14}'
      f'{"R$ "+brl(P_ROUPS,0):>14}{"":>12}')
print(f'  {"só roupeiros · SÓ o closet aberto":<34}{"R$ "+brl(rcr["cd"],0):>14}'
      f'{"R$ "+brl(P_ROUPS+DELTA_C,0):>14}{"+R$ "+brl(DELTA_C,0):>12}')
print(f'  {"só roupeiros · interno Gianduia":<34}{"R$ "+brl(rgr["cd"],0):>14}'
      f'{"R$ "+brl(P_ROUPS+DELTA_GR,0):>14}{"+R$ "+brl(DELTA_GR,0):>12}')
print(f'\n  Custo do upgrade: R$ {brl(d_cd,0)} no pacote cheio · '
      f'R$ {brl(d_cdr,0)} só nos roupeiros.')
print(f'  Chapas: {rg["tot_ch"]} contra {r["tot_ch"]} no cheio '
      f'(a Gianduia entra como grupo novo e o aproveitamento muda).')
print('  ⚠ O PREÇO DA GIANDUIA TRAMA NÃO ESTÁ NA BASE. Adotei o piso do')
print('    Melamínico Fosco (6/15/18 = 300/500/600). "Trama" é TEXTURA e')
print('    costuma custar ACIMA do fosco liso — este delta é um MÍNIMO.')
CUSTO_GT = sum(n*prc('GT', e) for (m, e), n in rg['CH'].items() if m == 'GT')
print(f'    A Gianduia responde por R$ {brl(CUSTO_GT,0)} de chapa no pacote cheio.')
print('    Sensibilidade — se a Trama vier ACIMA do fosco:')
for f_ in (1.00, 1.10, 1.20, 1.30):
    _c = rg['cd'] + CUSTO_GT*(f_ - 1)
    _p = round(_c/div(MC_LIQ, True)/100)*100
    print(f'      Trama {(f_-1)*100:>3.0f}% acima do fosco → R$ {brl(_p,0)}'
          f'   (+R$ {brl(_p-INV,0)} sobre o Branco TX)')

print('\n' + '─'*W)
print(f'DÚVIDAS E CONFERÊNCIAS — {len(D["DUV"])} itens')
for i, (a, t) in enumerate(D['DUV'], 1):
    print(f'  {i:>2}. [{a}]\n      {t}')
print('\n  ★ Preços adotados, sem linha fechada na base:')
print(f'     · curva (CNC + fita a quente + lixamento) — R$ {brl(CURVA_M,0)}/m')
print(f'     · espelho de corte ORGÂNICO — {ESPELHO_CURVO:.1f}× o espelho reto')
print(f'     · cabeceira estofada — R$ {brl(ESTOFADO_M2,0)}/m² (proxy da laca)')
print(f'     · cabideiro em tubo — R$ {brl(CAB_M,0)}/m')
print(f'     · suporte de prateleira — R$ {brl(SUP_PRAT,0)}/un')
print(f'     · meia esquadria — R$ {brl(ESQ_M,0)}/m · LED comum R$ {brl(LED_M,0)}/m')
print(f'     · MDF Gianduia Trama — piso do Melamínico Fosco (NÃO está na base)')
print('\n⛔ FORA DO ESCOPO: tudo do 1º orçamento (cozinha, gourmet, área de')
print('   serviço e banheiros, já fechado), mármore da sala de TV, camas,')
print('   colchões, sofás, poltronas, mesas, cadeiras, tapetes, cortinas,')
print('   TVs, ar-condicionado, gesso, sanca, elétrica e pintura.')
print('═'*W)
