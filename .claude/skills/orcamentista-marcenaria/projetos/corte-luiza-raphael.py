# -*- coding: utf-8 -*-
"""LUIZA E RAPHAEL — quarto casal, espaço gourmet e sala da cobertura.

FONTE: `CADERNO_MARCENARIA_LUIZA_E_RAPHAEL` · 14 folhas A4 paisagem, escala
1/25, arq./decoradora **Jéssica Sollero**, 31/08/2026. É caderno de verdade:
planta, elevações A e B, cortes AA/BB/CC e renders, com cota peça a peça e
memorial de acabamento em cada móvel. Base FORTE — nada aqui é leitura de
render, só o que a folha cota.
"CONFERIR MEDIDAS NO LOCAL" está carimbado em todas as folhas.

[Jonathan 09/09/2026]
  · com RT              · prazo 70 dias corridos
  · formas de pagamento padrão
  · DUAS versões: Telescópica MC 32% · Hettich MC 40%
  · "na penteadeira tem dois divisores de acrílico. Apresente os valores deles
    separados desses divisores, será um custo de 800,00."
  · "se atente para não esquecer de considerar nada (metragem de fitas,
    insumos, ferragens etc)"

⛔ FORA DO ESCOPO (não é marcenaria): bancada e rodabanca em pedra do gourmet
   (marmoraria), eletrodomésticos (geladeira, lava-louças, máquina de lavar,
   cooktop, forno, coifa), TV, cuba, torneira, gesso, elétrica e pintura.
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

# ═══════════════════════════════════════════════════════════════════════════
# PREÇOS — dados/materiais.json + referencias/chapas.md (11/06/2026)
# ═══════════════════════════════════════════════════════════════════════════
PRC_COR = {6: 300.0, 15: 500.0, 18: 600.0, 25: 900.0}   # melamínico fosco/cor
PRC_BRA = {6: 190.0, 15: 260.0, 18: 330.0, 25: 420.0}   # Branco TX
# Quatro cores diferentes = quatro grupos de nesting. Cada uma puxa chapa
# inteira mesmo com pouca área — é o que encarece um job de cores múltiplas.
NOME_MAT = {'CV': 'MDF Carvalho (Arauco)',
            'GF': 'MDF Grafito Chess (Arauco)',
            'JQ': 'MDF Jequitibá (Arauco)',
            'GR': 'MDF Griss Chess (Arauco)',
            'BR': 'MDF Branco TX'}
def prc(m, e): return (PRC_BRA if m == 'BR' else PRC_COR)[e]

FITA_COR, FITA_BRA, FILET_M, DESPERD = 3.00, 2.00, 2.50, 1.10
CHANF_M  = 15.0   # ★ PUXADOR CHANFRADO — chanfro a 45° usinado na borda da
                  #   frente. Mesma operação da meia esquadria (R$ 15/m), não
                  #   a cava de pega (R$ 25/m): é um passe só, sem rebaixo.
ESQ_M    = 15.0   # meia esquadria (encontros a 45°)
CURVA_M  = 60.0   # ★ canto/topo CURVO: CNC + fita a quente + lixamento
LED_M    = 66.0   # fita 28 + perfil de alumínio 38 — LED comum, não COB
DRIVER_UN= 90.0
SUP_PRAT = 8.0    # ★ suporte de prateleira

# ── terceirizados e acessórios ────────────────────────────────────────────
ESPELHO_COL   = 220.0   # espelho prata COLADO, por folha (chapas.md)
VIDRO_TEMP_M2 = 250.0   # vidro incolor temperado 8 mm, por m²
BASC_VIDRO    = 280.0   # porta basculante reflecta bronze + perfil bronze +
                        # puxador sotille + furos — referência CONFIRMADA
                        # (Kenia & Fábio 12/06/2026, 4 un = R$ 1.120)
ESTOFADO_M2   = 650.0   # ★ proxy da linha Laca/Pintura R$ 650/m²
ACRILICO      = 800.0   # [Jonathan 09/09] CRAVADO: os 2 divisores da gaveta
DOBR_CAMARAO  = 180.0   # ★ conjunto de dobradiça camarão (porta que dobra)
VASSOUREIRO   = 350.0   # ★ vassoureiro deslizante, acessório pronto
GANCHOS       = 60.0    # ★ jogo de ganchos de vassoura/rodo
ESCORREDOR    = 280.0   # ★ escorredor metálico interno de báscula
GIRO_TV       = 450.0   # ★ suporte/dobradiça de 90° para rotação da TV

# ═══════════════════════════════════════════════════════════════════════════
# [Jonathan 09/09/2026] DUAS VERSÕES
# ═══════════════════════════════════════════════════════════════════════════
CENARIOS = [
    ('1 · Telescópica', 'Hardt · corrediça telescópica · pistão normal', 0.32,
     dict(dobr=8.0,  corr=40.0,  pist=20.0), '2 anos'),
    ('2 · Hettich', 'Hettich Sensys · oculta Quadro · pistão com amortecimento',
     0.40, dict(dobr=35.0, corr=120.0, pist=30.0), '10 anos'),
]

# ── coleta ────────────────────────────────────────────────────────────────
P, FITA, TERC, LED, CHANF, ESQ, CURVA, DUV = [], [], [], [], [], [], [], []
FER = defaultdict(lambda: [0, 0, 0])       # dobradiças · corrediças · pistões
IT, ROUP, ORD_IT = ['—'], {}, []
def item(nome): IT[0] = nome
def _k(a):
    k = (a, IT[0])
    if k not in ROUP: ROUP[k] = True; ORD_IT.append(k)
    return k
def add(mat, esp, amb, desc, c, l, q=1):
    P.append((mat, esp, amb, IT[0], desc, c, l, q)); _k(amb)
def fer(a, dobr=0, corr=0, pist=0):
    k = _k(a); FER[k][0] += dobr; FER[k][1] += corr; FER[k][2] += pist
def fita(a, d, m, cor=True): FITA.append((_k(a), d, m, cor))
def terc(a, d, v, est=False): TERC.append((_k(a), d, v, est))
def led(a, d, m): LED.append((_k(a), d, m))
def chanf(a, m): CHANF.append((_k(a), m))
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
def gaveta(amb, nome, L, Pf, alt, q=1):
    """Caixa de gaveta em Branco TX — laterais/frente/costas 15, fundo 6."""
    add('BR', 15, amb, f'{nome} · caixa lateral',       Pf-10, alt, 2*q)
    add('BR', 15, amb, f'{nome} · caixa frente/costas', L-6,   alt, 2*q)
    add('BR', 6,  amb, f'{nome} · fundo de gaveta',     L-6,   Pf-10, q)

# ═══════════════════════════════════════════════════════════════════════════
# GEOMETRIA — tudo em cm, LIDO das folhas cotadas 1/25
# ═══════════════════════════════════════════════════════════════════════════

# ───────────────────────────────────────────────────────────────────────────
# 1 · QUARTO CASAL — folhas 1 e 2
# ───────────────────────────────────────────────────────────────────────────
A = 'Quarto casal'

item('Cabeceira estofada em Bouclé · 3,10 × 1,10 m')
painel('BR', 15, A, 'cabeceira · painel de fundo 3100 × 1100', 310, 110)
painel('BR', 15, A, 'cabeceira · moldura de 10 (topo e base)', 310, 10, 2)
add('BR', 15, A, 'cabeceira · moldura de 10 (laterais)',    110, 10, 2)
terc(A, 'Estofamento em tecido Bouclé (3,41 m² × R$ 650)', 3.10*1.10*ESTOFADO_M2, est=True)
esq(A, 2*(3.10+1.10))
curva(A, 2*math.pi*0.20/2)                 # R20 nos dois cantos superiores
fita(A, 'cabeceira · bordas da moldura', 2*(3.10+1.10), cor=False)
duv(A, 'a cabeceira é ESTOFADA em Bouclé sobre estrutura de MDF. ★ Adotei '
       'R$ 650/m² usando a linha Laca/Pintura da base como proxy do tapeceiro '
       '— R$ 2.217 nos 3,41 m². CONFERIR com o estofador: pode vir bem '
       'diferente, e é o maior terceirizado do quarto.')

item('Penteadeira em MDF Carvalho · 1,30 × 0,40 m')
add('CV', 15, A, 'penteadeira · tampo 1300 × 400',        130, 40)
add('CV', 15, A, 'penteadeira · lateral da caixa',         40, 10, 2)
add('CV', 15, A, 'penteadeira · travessa de fundo',       130, 10)
add('BR', 15, A, 'penteadeira · fundo de fixação',        130, 10)
add('CV', 18, A, 'penteadeira · frente de gaveta 550×100', 55, 10, 2)
gaveta(A, 'penteadeira', 55.0, 40.0, 7.0, 2)
fer(A, corr=2)
terc(A, 'Espelho prata colado 1,30 × 1,00 m (R40) — 1 folha', ESPELHO_COL)
terc(A, 'Tampo em vidro incolor temperado 8 mm (0,52 m²)', 1.30*0.40*VIDRO_TEMP_M2)
chanf(A, 2*0.55)
curva(A, math.pi*0.40/2 + math.pi*0.20/2)  # R40 do espelho + R20 da quina
esq(A, 2*(1.30+0.40))
fita(A, 'penteadeira · tampo, frentes e bordas',
     2*(1.30+0.40) + 2*2*(0.55+0.10) + 2*(0.40+0.10)*2)
fita(A, 'penteadeira · caixas de gaveta', 2*2*(0.55+0.40), cor=False)
duv(A, 'o ESPELHO de 1,30 × 1,00 entrou como UMA FOLHA colada a R$ 220 '
       '(`chapas.md`, a fonte que a regra de unidades manda usar). Se a '
       'espelharia cobrar por m² a R$ 600, sobe para R$ 780 — R$ 560 de '
       'diferença. ★ CONFERIR, ainda mais por causa do canto R40.')
duv(A, 'a gaveta da penteadeira tem 10 cm de FRENTE (80 − 70 da elevação B), '
       'ou seja ~7 cm úteis. É gaveta rasa de organização — coerente com os '
       'divisores de acrílico. CONFERIR se é isso mesmo.')

item('Divisórias internas em acrílico da penteadeira')
terc(A, '[Jonathan] Dois divisores de acrílico sob medida — CRAVADO', ACRILICO, est=True)
duv(A, 'a folha 1 detalha os divisores: dois blocos de 13+13+13+12 na largura '
       'e 14/11/11 na profundidade, um por gaveta. [Jonathan 09/09] o custo '
       'de R$ 800 é CRAVADO e o item vai SEPARADO na tabela.')

# ───────────────────────────────────────────────────────────────────────────
# 2 · ESPAÇO GOURMET — folhas 1 a 5. Corrida única: 133+37+429,5 = 599,5
# ───────────────────────────────────────────────────────────────────────────
A = 'Espaço gourmet'

item('Portas da lavanderia · 1,33 × 2,615 m')
add('GF', 18, A, 'porta da lavanderia 450 × 2615', 45, 261.5, 2)
add('GF', 18, A, 'porta da lavanderia 430 × 2615', 43, 261.5, 1)
fer(A, dobr=15)                                    # 5 por folha de 2,615
terc(A, 'Conjunto de dobradiça camarão (folhas que dobram)', DOBR_CAMARAO, est=True)
chanf(A, 3*2.615)
fita(A, 'portas da lavanderia · perímetro das 3 folhas',
     2*2*(0.45+2.615) + 2*(0.43+2.615))
duv(A, 'as 3 folhas de 2,615 m fecham o nicho da lavanderia e a folha diz '
       '"dobradiça camarão". ★ Adotei R$ 180 pelo conjunto do mecanismo, sem '
       'linha na base. CONFERIR quantas folhas realmente dobram.')

item('Armário superior da lavanderia · 1,33 × 1,075 m')
add('GF', 15, A, 'sup. lavanderia · lateral', 107.5, 35, 2)
add('GF', 15, A, 'sup. lavanderia · tampo e base', 130, 35, 2)
add('GF', 15, A, 'sup. lavanderia · divisória', 104.5, 35, 1)
add('BR', 6,  A, 'sup. lavanderia · fundo', 130, 104.5, 1)
add('BR', 15, A, 'sup. lavanderia · prateleira do módulo 87', 87, 34, 2)
add('BR', 15, A, 'sup. lavanderia · prateleira do módulo 40', 40, 34, 2)
add('GF', 18, A, 'sup. lavanderia · porta 435 × 1075', 43.5, 107.5, 2)
add('GF', 18, A, 'sup. lavanderia · porta 400 × 1075', 40, 107.5, 1)
fer(A, dobr=9)
terc(A, 'Suportes das 4 prateleiras (16 un)', 16*SUP_PRAT)
chanf(A, 3*1.075)
fita(A, 'sup. lavanderia · portas e bordas',
     2*2*(0.435+1.075) + 2*(0.40+1.075) + 2*(1.30+0.35))
fita(A, 'sup. lavanderia · frente das prateleiras', 2*0.87 + 2*0.40, cor=False)

item('Armário inferior da lavanderia · 0,68 m')
add('GF', 15, A, 'inf. lavanderia · lateral', 72, 70, 2)
add('GF', 15, A, 'inf. lavanderia · base', 68, 70, 1)
add('BR', 6,  A, 'inf. lavanderia · fundo', 68, 72, 1)
add('GF', 18, A, 'inf. lavanderia · frente da báscula', 68, 36, 1)
add('GF', 18, A, 'inf. lavanderia · frente do gavetão', 68, 36, 1)
gaveta(A, 'inf. lavanderia · gavetão', 68.0, 70.0, 32.0, 1)
add('GF', 15, A, 'inf. lavanderia · sóculo', 68, 15, 1)
fer(A, dobr=2, corr=1, pist=2)
chanf(A, 2*0.68)
fita(A, 'inf. lavanderia · frentes e bordas',
     2*2*(0.68+0.36) + 2*(0.68+0.70) + 0.68)
fita(A, 'inf. lavanderia · caixa do gavetão', 2*(0.68+0.70), cor=False)

item('Vassoureiro · 0,37 × 2,495 m')
add('GF', 15, A, 'vassoureiro · lateral', 249.5, 72, 2)
add('GF', 15, A, 'vassoureiro · tampo e base', 37, 72, 2)
add('BR', 6,  A, 'vassoureiro · fundo', 37, 246.5, 1)
add('BR', 15, A, 'vassoureiro · prateleira', 37, 71, 3)
add('GF', 18, A, 'vassoureiro · porta 370 × 2465', 37, 246.5, 1)
add('GF', 15, A, 'vassoureiro · sóculo', 37, 15, 1)
fer(A, dobr=5)
terc(A, 'Vassoureiro deslizante (acessório pronto)', VASSOUREIRO, est=True)
terc(A, 'Jogo de ganchos de vassoura e rodo', GANCHOS, est=True)
terc(A, 'Suportes das 3 prateleiras (12 un)', 12*SUP_PRAT)
chanf(A, 2.465)
fita(A, 'vassoureiro · porta e bordas', 2*(0.37+2.465) + 2*(0.37+2.495))
fita(A, 'vassoureiro · frente das prateleiras', 3*0.37, cor=False)

item('Armário superior do gourmet · 2,30 × 0,725 m')
add('GF', 15, A, 'sup. gourmet · lateral', 72.5, 35, 2)
add('GF', 15, A, 'sup. gourmet · tampo e base', 230, 35, 2)
add('GF', 15, A, 'sup. gourmet · divisória', 69.5, 35, 2)
add('BR', 6,  A, 'sup. gourmet · fundo', 230, 69.5, 1)
add('BR', 15, A, 'sup. gourmet · prateleira do módulo 77', 77, 34, 2)
add('BR', 15, A, 'sup. gourmet · prateleira do módulo 68', 68, 34, 1)
add('GF', 18, A, 'sup. gourmet · porta 400 × 725', 40, 72.5, 4)
add('GF', 18, A, 'sup. gourmet · porta 350 × 725', 35, 72.5, 2)
fer(A, dobr=12)
terc(A, 'Suportes das 3 prateleiras (12 un)', 12*SUP_PRAT)
chanf(A, 6*0.725)
fita(A, 'sup. gourmet · portas e bordas',
     4*2*(0.40+0.725) + 2*2*(0.35+0.725) + 2*(2.30+0.35))
fita(A, 'sup. gourmet · frente das prateleiras', 2*0.77 + 0.68, cor=False)

item('Básculas em MDF Jequitibá · 1,50 × 0,35 m')
add('JQ', 15, A, 'básculas · lateral', 35, 35, 2)
add('JQ', 15, A, 'básculas · tampo e base', 150, 35, 2)
add('JQ', 15, A, 'básculas · divisória', 35, 35, 1)
add('BR', 6,  A, 'básculas · fundo', 150, 35, 1)
add('JQ', 18, A, 'báscula do escorredor · frente 800 × 350', 80, 35, 1)
terc(A, 'Porta basculante em vidro reflecta bronze, perfil e puxador sotille '
        'bronze (0,70 × 0,35)', BASC_VIDRO)
terc(A, 'Escorredor metálico interno da báscula', ESCORREDOR, est=True)
fer(A, dobr=4, pist=4)
led(A, 'LED 4000K sob as básculas', 1.50)
terc(A, 'Driver da iluminação das básculas', DRIVER_UN)
chanf(A, 0.80)
fita(A, 'básculas · frente e bordas', 2*(0.80+0.35) + 2*(1.50+0.35))
duv(A, 'a báscula de VIDRO entrou pela referência CONFIRMADA da base '
       '(Kenia & Fábio 12/06: porta reflecta bronze + perfil bronze + puxador '
       'sotille + furos = R$ 280 a folha de 0,96 × 0,41). A nossa é 0,70 × '
       '0,35, MENOR — o preço é conservador.')

item('Armário inferior do gourmet · 4,295 m')
add('GF', 15, A, 'inf. gourmet · lateral e divisória', 72, 70, 7)
painel('GF', 15, A, 'inf. gourmet · base', 429.5, 70, 1)
painel('BR', 6,  A, 'inf. gourmet · fundo', 429.5, 72, 1)
painel('GF', 15, A, 'inf. gourmet · sóculo', 429.5, 15, 1)
# módulo 65 · báscula + gavetão (sob a cuba)
add('GF', 18, A, 'inf. gourmet · báscula 650 × 360', 65, 36, 1)
add('GF', 18, A, 'inf. gourmet · gavetão 650 × 360', 65, 36, 1)
gaveta(A, 'inf. gourmet · gavetão 65', 65.0, 70.0, 32.0, 1)
# módulo 35 · quatro gavetas de 18
add('GF', 18, A, 'inf. gourmet · gaveta 350 × 180', 35, 18, 4)
gaveta(A, 'inf. gourmet · gaveta 35', 35.0, 70.0, 14.0, 4)
# módulo 70 · nicho do forno
add('BR', 15, A, 'inf. gourmet · travessa de apoio do forno', 70, 70, 1)
# módulo 30 · porta de temperos
add('GF', 18, A, 'inf. gourmet · porta de temperos 300 × 720', 30, 72, 1)
add('BR', 15, A, 'inf. gourmet · prateleira de temperos', 30, 68, 2)
# módulo 85 · báscula + gavetão
add('GF', 18, A, 'inf. gourmet · báscula 850 × 360', 85, 36, 1)
add('GF', 18, A, 'inf. gourmet · gavetão 850 × 360', 85, 36, 1)
gaveta(A, 'inf. gourmet · gavetão 85', 85.0, 70.0, 32.0, 1)
fer(A, dobr=6, corr=6, pist=4)
terc(A, 'Suportes das 2 prateleiras de temperos (8 un)', 8*SUP_PRAT)
chanf(A, 0.65 + 0.65 + 4*0.35 + 0.30 + 0.85 + 0.85)
fita(A, 'inf. gourmet · frentes',
     2*2*(0.65+0.36) + 4*2*(0.35+0.18) + 2*(0.30+0.72) + 2*2*(0.85+0.36))
fita(A, 'inf. gourmet · bordas do corpo e sóculo', 4.295*2 + 7*0.72)
fita(A, 'inf. gourmet · caixas de gaveta e prateleiras',
     2*(0.65+0.70) + 4*2*(0.35+0.70) + 2*(0.85+0.70) + 2*0.30, cor=False)
duv(A, 'o trecho de 144,5 do armário inferior é VÃO DE ELETRODOMÉSTICO — a '
       'folha 3 mostra a lava-louças Electrolux embutida e o espaço da '
       'geladeira. Orcei laterais e sóculo, SEM frentes. CONFERIR se entra '
       'porta de painel na lava-louças (aí sobe uma frente de 60 × 72).')
duv(A, 'o módulo de 30 ao lado do forno está cotado como "porta temp." — li '
       'como PORTA DE TEMPEROS, com duas prateleiras internas. CONFERIR.')
duv(A, '⛔ BANCADA E RODABANCA SÃO PEDRA (marmoraria) e estão FORA. Os renders '
       'mostram granito preto na bancada e pedra clara na rodabanca. A '
       'marcenaria entrega o corpo, o recorte da cuba e o encosto.')

# ───────────────────────────────────────────────────────────────────────────
# 3 · SALA COBERTURA — folhas 1 a 3
# ───────────────────────────────────────────────────────────────────────────
A = 'Sala cobertura'

item('Painel de TV em MDF Griss Chess · 3,975 × 1,00 m')
painel('GR', 15, A, 'painel · face 3975 × 1000', 397.5, 100)
add('GR', 15, A, 'painel · moldura de 6 (topo e base)', 397.5/2, 6, 4)
add('GR', 15, A, 'painel · moldura de 6 (laterais)', 100, 6, 2)
add('BR', 15, A, 'painel · travessa interna de fixação', 100, 6, 6)
esq(A, 2*(3.975+1.00))
led(A, 'LED 3000K superior do painel', 3.975)
led(A, 'LED 3000K inferior do painel', 3.975)
terc(A, 'Driver da iluminação do painel', DRIVER_UN)
terc(A, 'Dobradiça/suporte de 90° para rotação da TV', GIRO_TV, est=True)
fita(A, 'painel · perímetro e moldura', 2*(3.975+1.00) + 2*(3.975+1.00))
duv(A, 'o painel tem 6 cm de espessura (corte AA) e é CAIXA, não chapa lisa: '
       'face em Griss Chess, moldura de 6 e travessas internas de fixação. É '
       'assim que ele recebe o LED nas duas bordas sem aparecer perfil.')
duv(A, '⚠ O RENDER da folha 4 mostra o painel com CANTOS BEM ARREDONDADOS e o '
       'LED contornando a curva. A ELEVAÇÃO A e o corte AA desenham o painel '
       'RETANGULAR. Segui a elevação. Se forem curvos, entram ~2,2 m de curva '
       '(~R$ 132 de custo) e o LED tem de ser flexível.')
duv(A, '⚠ O render mostra a PAREDE INTEIRA revestida em madeira atrás do '
       'painel. O caderno não descreve esse revestimento em lugar nenhum e '
       'ele NÃO está neste orçamento. Se for marcenaria, é item novo e '
       'grande. CONFERIR com a Jéssica.')

item('Rack em MDF Griss Chess · 2,00 × 0,47 m')
add('GR', 15, A, 'rack · tampo e base', 200, 55, 2)
add('GR', 15, A, 'rack · lateral e divisória', 47, 55, 4)
add('BR', 6,  A, 'rack · fundo', 200, 47, 1)
add('GR', 18, A, 'rack · frente do gavetão 800 × 440', 80, 44, 2)
gaveta(A, 'rack · gavetão', 80.0, 50.0, 40.0, 2)
add('GR', 15, A, 'rack · rodapé recuado', 200, 3, 1)
fer(A, corr=2)
chanf(A, 2*0.80)
curva(A, 2.5)                              # cantos arredondados R20, 2 pontas
fita(A, 'rack · frentes e bordas', 2*2*(0.80+0.44) + 2*(2.00+0.55) + 2.00)
fita(A, 'rack · caixas de gaveta', 2*2*(0.80+0.50), cor=False)

# ═══════════════════════════════════════════════════════════════════════════
# CÁLCULO — rateio POR CUSTO, item a item (regra da casa, 29/08)
# ═══════════════════════════════════════════════════════════════════════════
N_CARRETO, R_CARRETO = 2, 600.0     # 3 ambientes num apartamento só
N_VISITA,  R_VISITA  = 2, 250.0
LOG = N_CARRETO*R_CARRETO + N_VISITA*R_VISITA

def brl(v, n=2):
    return f'{v:,.{n}f}'.replace(',', '§').replace('.', ',').replace('§', '.')

por, area_ch, area_it, area_amb = (defaultdict(list), defaultdict(float),
                                   defaultdict(float), defaultdict(float))
for m, e, a, it, d, c, l, q in P:
    for _ in range(q): por[(m, e)].append((c, l))
    ar = c*l*q/10000
    area_ch[(m, e)] += ar; area_it[(a, it)] += ar; area_amb[a] += ar
CH = {k: nest(v) for k, v in por.items()}
custo_chapa = sum(n*prc(k[0], k[1]) for k, n in CH.items())
area_tot, tot_ch = sum(area_ch.values()), sum(CH.values())

# ── FITA: explícita por item, com o piso de 2,6 m/m² como guarda ──────────
m_fita_cor = sum(m for _, _, m, cor in FITA if cor)
m_fita_bra = sum(m for _, _, m, cor in FITA if not cor)
m_fita_expl = m_fita_cor + m_fita_bra
m_fita_piso = area_tot*2.6
USOU_PISO = m_fita_piso > m_fita_expl
if USOU_PISO:                       # rateia o acréscimo na proporção declarada
    _f = m_fita_piso/m_fita_expl
    m_fita_cor *= _f; m_fita_bra *= _f
m_fita = m_fita_cor + m_fita_bra
custo_fita  = (m_fita_cor*FITA_COR + m_fita_bra*FITA_BRA)*DESPERD
custo_filet = m_fita*FILET_M

m_chanf = sum(m for _, m in CHANF); custo_chanf = m_chanf*CHANF_M
m_esq   = sum(m for _, m in ESQ);   custo_esq   = m_esq*ESQ_M
m_cur   = sum(m for _, m in CURVA); custo_curva = m_cur*CURVA_M
m_led   = sum(m for _, _, m in LED); custo_led  = m_led*LED_M
custo_terc = sum(v for _, _, v, _ in TERC)
consum = (custo_chapa + custo_fita)*0.06        # parafuso, cavilha, cola, fita

def custo_ferr(cen):
    f = CENARIOS[cen][3]
    return sum(v[0]*f['dobr'] + v[1]*f['corr'] + v[2]*f['pist']
               for v in FER.values())
def CD(cen):
    return (custo_chapa + custo_fita + custo_filet + custo_chanf + custo_esq
            + custo_curva + custo_led + custo_terc + consum + custo_ferr(cen)
            + LOG)

def cd_por_item(cen):
    cdi = defaultdict(float)
    _ar = defaultdict(float)
    for m, e, a, it, d, c, l, q in P: _ar[(m, e, a, it)] += c*l*q/10000
    for (m, e, a, it), ar in _ar.items():
        cdi[(a, it)] += CH[(m, e)]*prc(m, e) * ar/area_ch[(m, e)]
    _fc = (custo_fita + custo_filet)/m_fita
    _mult = m_fita/m_fita_expl
    for k, _, mm, _c in FITA: cdi[k] += mm*_mult*_fc
    for k, mm in CHANF: cdi[k] += mm*CHANF_M
    for k, mm in ESQ:   cdi[k] += mm*ESQ_M
    for k, mm in CURVA: cdi[k] += mm*CURVA_M
    for k, _, mm in LED: cdi[k] += mm*LED_M
    for k, _, v, _e in TERC: cdi[k] += v
    # ⛔ [Jonathan 09/09] CONSUMÍVEL E LOGÍSTICA SE RATEIAM ANTES DA FERRAGEM.
    #    Eu rateava os dois sobre o custo bruto JÁ COM a ferragem dentro. O
    #    efeito: quando a ferragem encarece, os itens que TÊM ferragem puxam
    #    uma fatia maior do bolo, e os que NÃO TÊM — cabeceira, divisórias de
    #    acrílico, painel de TV — ficavam mais BARATOS de uma versão para a
    #    outra. Não faz sentido: nada neles muda. E consumível é 6% de chapa
    #    + fita, não tem relação nenhuma com ferragem.
    #    A base do rateio agora é a parte do custo que NÃO depende do cenário.
    base_fixa = sum(cdi.values())
    for k in list(cdi): cdi[k] += (consum + LOG)*cdi[k]/base_fixa
    f = CENARIOS[cen][3]
    for k, v in FER.items():
        cdi[k] += v[0]*f['dobr'] + v[1]*f['corr'] + v[2]*f['pist']
    assert abs(sum(cdi.values()) - CD(cen)) < 0.01, (sum(cdi.values()), CD(cen))
    return dict(cdi)

ORD_AMB = list(dict.fromkeys(a for a, _ in ORD_IT))

_fora = [(m, e, a, d, c, l) for m, e, a, it, d, c, l, q in P
         if max(c, l) > CH_C or min(c, l) > CH_L]
if _fora:
    print('\n' + '!'*W + '\nPEÇAS QUE NÃO CABEM NA CHAPA')
    for m, e, a, d, c, l in _fora:
        print(f'  {NOME_MAT[m]} {e} · {a} · {d}: {c:.0f} × {l:.0f}')
    print('!'*W + '\n')

print('═'*W)
print('LUIZA E RAPHAEL — QUARTO CASAL · ESPAÇO GOURMET · SALA DA COBERTURA')
print('═'*W)
print('Caderno de marcenaria 1/25 da decoradora Jéssica Sollero · 31/08/2026 ·')
print('14 folhas com planta, elevações, cortes e memorial de acabamento.')

print('\nESCOPO')
for a in ORD_AMB:
    print(f'  {a}')
    for k in [k for k in ORD_IT if k[0] == a]:
        d, c, p_ = FER[k]
        ex = ' · '.join(x for x in (f'{d} dobr.' if d else '',
                                    f'{c} corr.' if c else '',
                                    f'{p_} pistões' if p_ else '') if x)
        print(f'     {k[1]:<48}{area_it[k]:>6.2f} m²   {ex}')
    print(f'     {"— subtotal do ambiente":<48}{area_amb[a]:>6.2f} m²')
print(f'  {"TOTAL":<53}{area_tot:>6.2f} m²')

print('\n' + '─'*W)
print('PLANO DE CORTE — quatro cores diferentes, quatro nestings separados')
print('─'*W)
for k, n in sorted(CH.items(), key=lambda x: (-x[1], x[0])):
    print(f'  {NOME_MAT[k[0]]+" "+str(k[1])+" mm":<32}{area_ch[k]:>7.2f} m²  →  '
          f'{n:>2} ch. × R$ {prc(*k):>6.2f} = R$ {brl(n*prc(*k)):>9}   aprov. '
          f'{area_ch[k]/(n*CH_AREA)*100:>3.0f}%')
print(f'  {"TOTAL":<32}{area_tot:>7.2f} m²  →  {tot_ch:>2} chapas'
      f'{"":>13}R$ {brl(custo_chapa):>9}   médio '
      f'{area_tot/(tot_ch*CH_AREA)*100:.0f}%')

print('\n' + '─'*W)
print('INSUMOS, USINAGEM E ILUMINAÇÃO')
print('─'*W)
print(f'  Fita de borda COR 22 mm       {m_fita_cor:>7.1f} m × R$ {brl(FITA_COR)} '
      f'× 1,10 desperdício')
print(f'  Fita de borda BRANCA 22 mm    {m_fita_bra:>7.1f} m × R$ {brl(FITA_BRA)} '
      f'× 1,10 desperdício')
print(f'  {"— fita, total":<30}{m_fita:>7.1f} m{"":>21}R$ {brl(custo_fita):>9}')
print(f'  Filetagem (coladeira)         {m_fita:>7.1f} m × R$ {brl(FILET_M)}'
      f'{"":>13}R$ {brl(custo_filet):>9}')
print(f'  ★ Puxador chanfrado           {m_chanf:>7.1f} m × R$ {brl(CHANF_M)}'
      f'{"":>13}R$ {brl(custo_chanf):>9}')
print(f'  Meia esquadria                {m_esq:>7.1f} m × R$ {brl(ESQ_M)}'
      f'{"":>13}R$ {brl(custo_esq):>9}')
print(f'  ★ Canto curvo (R20/R40)       {m_cur:>7.1f} m × R$ {brl(CURVA_M)}'
      f'{"":>13}R$ {brl(custo_curva):>9}')
print(f'  Iluminação em LED             {m_led:>7.1f} m × R$ {brl(LED_M)}'
      f'{"":>13}R$ {brl(custo_led):>9}')
print(f'  Consumíveis (6% de chapa+fita){"":>26}R$ {brl(consum):>9}')
print(f'  Logística ({N_CARRETO} carretos + {N_VISITA} visitas){"":>20}'
      f'R$ {brl(LOG):>9}')
_conf = 'declarada peça a peça' if not USOU_PISO else \
        f'PISO de 2,6 m/m² aplicado (declarei {m_fita_expl:.1f} m)'
print(f'  ↳ metragem de fita: {_conf}')

print('\n' + '─'*W)
print('TERCEIRIZADOS E ACESSÓRIOS   (★ = sem preço fechado na base)')
print('─'*W)
for (a, it), d, v, est in TERC:
    print(f'  {"★" if est else " "} {a[:14]:<15}{d[:56]:<57}R$ {brl(v):>9}')
print(f'  {"":<17}{"TOTAL":<57}R$ {brl(custo_terc):>9}')

print('\n' + '═'*W)
print('FERRAGENS — as duas versões')
print('═'*W)
TD = sum(v[0] for v in FER.values())
TC = sum(v[1] for v in FER.values())
TP = sum(v[2] for v in FER.values())
print(f'  {TD} dobradiças · {TC} pares de corrediça · {TP} pistões a gás')
for i, (nome, ferr, mc, f, gar) in enumerate(CENARIOS):
    print(f'  {nome:<18}dobr. R$ {f["dobr"]:>3.0f} · corr. R$ {f["corr"]:>3.0f} · '
          f'pist. R$ {f["pist"]:>3.0f}  →  R$ {brl(custo_ferr(i)):>9}   {ferr}')

print('\n' + '═'*W)
print('PREÇO — duas versões, o mesmo desenho, COM RT de 10%')
print('═'*W)
print(f'  {"Versão":<18}{"Custo direto":>14}{"MC alvo":>9}{"Investimento":>15}'
      f'{"MC bruta":>10}{"líquida":>9}   Garantia')
# ⛔ [Jonathan 09/09] ITEM QUE NÃO MUDA ENTRE AS VERSÕES TEM UM PREÇO SÓ.
#    "A cabeceira estofada deve custar o mesmo valor para o cliente em ambos
#     os contextos, assim como em todos os demais contextos semelhantes."
#    Item sem ferragem nenhuma não tem versão: é o MESMO móvel, com o MESMO
#    custo. Ele é precificado UMA VEZ, na MC da versão base, e esse preço vai
#    idêntico para as duas propostas. Só o que realmente muda de ferragem
#    carrega a MC da sua versão.
MC_BASE = CENARIOS[0][2]
CDI = [cd_por_item(i) for i in range(len(CENARIOS))]
SEM_FER = [k for k in ORD_IT if FER.get(k, [0, 0, 0]) == [0, 0, 0]]
COM_FER = [k for k in ORD_IT if k not in SEM_FER]
PV_FIXO = {k: round(CDI[0][k]/div(MC_BASE, True)/100)*100 for k in SEM_FER}
CD_SF   = sum(CDI[0][k] for k in SEM_FER)
PV_SF   = sum(PV_FIXO.values())

PRECOS, PV = [], {}
for i, (nome, ferr, mc, f, gar) in enumerate(CENARIOS):
    cd_var = sum(CDI[i][k] for k in COM_FER)
    pv_var = round(cd_var/div(mc, True)/100)*100
    v = {k: round(pv_var*CDI[i][k]/cd_var/100)*100 for k in COM_FER}
    _maior = max(COM_FER, key=lambda k: CDI[i][k])
    v[_maior] += pv_var - sum(v.values())
    v.update(PV_FIXO)
    PV[i] = (CDI[i], v)
    pv = PV_SF + pv_var
    PRECOS.append(pv)
    mb = mc_conferida(pv, CD(i))
    print(f'  {nome:<18}{"R$ "+brl(CD(i),0):>14}{mc*100:>8.0f}%{"R$ "+brl(pv,0):>15}'
          f'{mb*100:>9.1f}%{(mb-LIQF_*RT_PCT)*100:>8.1f}%   {gar}')
for k in SEM_FER:                       # a guarda do Jonathan
    assert PV[0][1][k] == PV[1][1][k], (k, PV[0][1][k], PV[1][1][k])
print(f'\n  Itens SEM ferragem, preço ÚNICO na MC de {MC_BASE*100:.0f}%: '
      f'R$ {brl(PV_SF,0)} nas duas versões')
print(f'  Itens COM ferragem: MC da versão · '
      f'R$ {brl(PRECOS[0]-PV_SF,0)} (32%) · R$ {brl(PRECOS[1]-PV_SF,0)} (40%)')
SEM_RT = [round(CD(i)/div(CENARIOS[i][2], False)/100)*100 for i in range(2)]
print(f'  {"":<18}{"sem RT":>14}{"":>9}{"R$/m² sem RT":>15}{"R$/m² com RT":>19}')
for i in range(2):
    print(f'  {CENARIOS[i][0]:<18}{"R$ "+brl(SEM_RT[i],0):>14}{"":>9}'
          f'{SEM_RT[i]/area_tot:>15.0f}{PRECOS[i]/area_tot:>19.0f}')
print('  (faixa da casa: 626–834 por m² de chapa, sem RT)')

print(f'\n  ⚠ A DIFERENÇA DE R$ {brl(PRECOS[1]-PRECOS[0],0)} ENTRE AS DUAS VERSÕES SE DECOMPÕE ASSIM:')
_d_ferr = custo_ferr(1) - custo_ferr(0)
_pv_ferr = round(_d_ferr/div(CENARIOS[0][2], True)/100)*100
print(f'     ferragem, custo real ................. R$ {brl(_d_ferr,0):>8}')
print(f'     o mesmo, repassado na MC de 32% ...... R$ {brl(_pv_ferr,0):>8}')
print(f'     margem adicional (32% → 40%) ......... R$ {brl(PRECOS[1]-PRECOS[0]-_pv_ferr,0):>8}')
print(f'  Ou seja: R$ {brl(_d_ferr,0)} de ferragem a mais e '
      f'R$ {brl(PRECOS[1]-PRECOS[0]-_pv_ferr,0)} de margem a mais.')
print(f'  A MC LÍQUIDA da versão Hettich fica em '
      f'{(mc_conferida(PRECOS[1], CD(1))-LIQF_*RT_PCT)*100:.1f}%, e não nos 40%')
print(f'  cravados: os itens sem ferragem carregam 32% nas duas versões, então')
print(f'  os 40% valem só sobre os {PRECOS[1]-PV_SF:,.0f} de itens com ferragem.'
      .replace(',', '.'))
print(f'  É o preço da coerência linha a linha — e é o que o cliente consegue')
print(f'  comparar sem fazer pergunta que a gente não sabe responder.')
print(f'  A dobradiça Hettich SENSYS (R$ 35) sozinha vale')
print(f'  R$ {brl(53*(35-8),0)} dos R$ {brl(_d_ferr,0)}. Com a NOVISYS (R$ 10) a ferragem')
print(f'  ficaria em R$ {brl(53*10 + 11*120 + 10*30,0)}, quase igual à telescópica.')

print('\n' + '─'*W)
print('CUSTO E VENDA, ITEM A ITEM')
print('─'*W)
_c0, _c1 = CDI[0], CDI[1]
for k in ORD_IT:
    if FER.get(k, [0, 0, 0]) == [0, 0, 0]:
        assert abs(_c0[k] - _c1[k]) < 0.01, (k, _c0[k], _c1[k])
print(f'  {"":52}{"custo dir.":>11}{"TELESCÓP.":>12}{"custo dir.":>12}{"HETTICH":>11}')
for a in ORD_AMB:
    print(f'  {a}')
    for k in [k for k in ORD_IT if k[0] == a]:
        print(f'    {k[1]:<50}{"R$ "+brl(PV[0][0][k],0):>11}'
              f'{"R$ "+brl(PV[0][1][k],0):>12}{"R$ "+brl(PV[1][0][k],0):>12}'
              f'{"R$ "+brl(PV[1][1][k],0):>11}')
    ks = [k for k in ORD_IT if k[0] == a]
    print(f'    {"— subtotal":.<50}{"R$ "+brl(sum(PV[0][0][k] for k in ks),0):>11}'
          f'{"R$ "+brl(sum(PV[0][1][k] for k in ks),0):>12}'
          f'{"R$ "+brl(sum(PV[1][0][k] for k in ks),0):>12}'
          f'{"R$ "+brl(sum(PV[1][1][k] for k in ks),0):>11}')
print(f'  {"TOTAL":<52}{"R$ "+brl(CD(0),0):>11}{"R$ "+brl(PRECOS[0],0):>12}'
      f'{"R$ "+brl(CD(1),0):>12}{"R$ "+brl(PRECOS[1],0):>11}')

print('\n' + '─'*W)
print('OS ITENS QUE NÃO MUDAM ENTRE AS VERSÕES')
print('─'*W)
print('  Não levam uma dobradiça, corrediça ou pistão sequer — são o MESMO')
print('  móvel nas duas propostas, com o mesmo custo e o MESMO PREÇO:')
print(f'     {"":<66}{"custo":>10}{"venda":>11}')
for k in SEM_FER:
    print(f'     {(k[0]+" · "+k[1])[:64]:<66}{"R$ "+brl(CDI[0][k],0):>10}'
          f'{"R$ "+brl(PV_FIXO[k],0):>11}')
print(f'     {"— somados":.<66}{"R$ "+brl(CD_SF,0):>10}{"R$ "+brl(PV_SF,0):>11}')
print(f'  Precificados uma vez só, na MC de {MC_BASE*100:.0f}% com RT.')
print(f'  {PV_SF/PRECOS[0]*100:.0f}% da proposta telescópica e '
      f'{PV_SF/PRECOS[1]*100:.0f}% da Hettich saem por este preço fixo.')

print('\n' + '─'*W)
print('⚠ O QUE AS QUATRO CORES CUSTAM')
print('─'*W)
_peq = {('CV', 18), ('JQ', 18), ('GR', 18)}
_gasto = sum(CH[k]*prc(*k) for k in _peq if k in CH)
_area  = sum(area_ch[k] for k in _peq if k in CH)
print(f'  Três lotes de FRENTE PEQUENA em 18 mm puxam chapa inteira só para si:')
for k in sorted(_peq):
    if k in CH:
        print(f'     {NOME_MAT[k[0]]+" 18 mm":<34}{area_ch[k]:>5.2f} m² em '
              f'{CH[k]} chapa  →  R$ {brl(CH[k]*prc(*k),0):>5}   '
              f'aprov. {area_ch[k]/(CH[k]*CH_AREA)*100:.0f}%')
print(f'     {"— total":<34}{_area:>5.2f} m²{"":>10}R$ {brl(_gasto,0):>5}')
print(f'  Passar essas frentes para 15 mm — a mesma chapa da cor que JÁ está')
print(f'  sendo comprada — economiza até R$ {brl(_gasto,0)} de chapa. São frentes')
print(f'  pequenas (gaveta de 10, báscula de 35, gavetão de 44): 15 mm não')
print(f'  empena. ⚠ DECISÃO DE ESPECIFICAÇÃO, não minha — orcei em 18 mm, que')
print(f'  é o padrão da casa para frente.')

print('\n' + '─'*W)
print(f'DÚVIDAS E CONFERÊNCIAS — {len(DUV)} itens')
print('─'*W)
for i, (a, t) in enumerate(DUV, 1):
    print(f'  {i:>2}. [{a}]\n      {t}')
print('\n  ★ Preços adotados, SEM linha fechada na base:')
for n, v in (('puxador chanfrado (chanfro 45° na CNC)', f'R$ {brl(CHANF_M,0)}/m'),
             ('canto curvo R20/R40', f'R$ {brl(CURVA_M,0)}/m'),
             ('estofamento em Bouclé (proxy da laca)', f'R$ {brl(ESTOFADO_M2,0)}/m²'),
             ('conjunto de dobradiça camarão', f'R$ {brl(DOBR_CAMARAO,0)}'),
             ('vassoureiro deslizante', f'R$ {brl(VASSOUREIRO,0)}'),
             ('escorredor metálico de báscula', f'R$ {brl(ESCORREDOR,0)}'),
             ('ganchos de vassoura e rodo', f'R$ {brl(GANCHOS,0)}'),
             ('dobradiça/suporte de 90° da TV', f'R$ {brl(GIRO_TV,0)}'),
             ('divisores de acrílico', f'R$ {brl(ACRILICO,0)} — CRAVADO pelo Jonathan')):
    print(f'     · {n:<48}{v}')
print('\n⛔ FORA DO ESCOPO: bancada e rodabanca em pedra do gourmet (marmoraria),')
print('   revestimento de madeira da parede da sala (não descrito no caderno),')
print('   eletrodomésticos, cuba, torneira, TV, gesso, elétrica e pintura.')
print('═'*W)
