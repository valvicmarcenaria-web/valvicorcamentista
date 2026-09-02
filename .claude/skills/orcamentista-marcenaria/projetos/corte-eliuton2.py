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
NOME_MAT = {'AM': 'MDF amadeirado', 'BR': 'MDF Branco TX'}
def prc(m, e): return PRC_BRA[e] if m == 'BR' else PRC_COR[e]

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

P, FITA, TERC, LED, USIN, ESQ, CURVA, DUV = [], [], [], [], [], [], [], []
FER = defaultdict(lambda: [0, 0, 0])       # dobradiças · corrediças · articul.
def add(mat, esp, amb, desc, c, l, q=1): P.append((mat, esp, amb, desc, c, l, q))
def fer(a, dobr=0, corr=0, art=0):
    FER[a][0] += dobr; FER[a][1] += corr; FER[a][2] += art
def fita(a, d, m): FITA.append((a, d, m))
def terc(a, d, v, est=False): TERC.append((a, d, v, est))
def led(a, d, m): LED.append((a, d, m))
def usin(a, m): USIN.append((a, m))
def esq(a, m): ESQ.append((a, m))
def curva(a, m): CURVA.append((a, m))
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

def corpo(mat, amb, larg, alt, prof, n_div, nome='módulo'):
    """Caixaria de roupeiro/closet: laterais, tampo, base, fundo e divisórias."""
    add(mat, 15, amb, f'{nome} · lateral', alt, prof, 2)
    painel(mat, 15, amb, f'{nome} · tampo e base', larg-3, prof, 2)
    painel('BR', 6, amb, f'{nome} · fundo', larg-3, alt-3, 1)
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
# ═══════════════════════════════════════════════════════════════════════════

# ───────────────────────────────────────────────────────────────────────────
# 1 · QUARTO MASTER — suíte 01, 17,20 m². Parede da cabeceira 85 + 195 + 80 = 360
# ───────────────────────────────────────────────────────────────────────────
A = 'Quarto master'
painel('AM', 15, A, 'painel de cabeceira 3600 × 2400', 360, H_PAINEL)
painel('AM', 15, A, 'retorno do painel na parede lateral', 150, H_PAINEL)
curva(A, 3.2)                      # topo curvo do painel, nas duas paredes
esq(A, (2*(3.60+2.40) + 2*(1.50+2.40)))
fita(A, 'painel de cabeceira e retorno', 2*(3.60+2.40) + 2*(1.50+2.40))
terc(A, 'Cabeceira estofada, 2,00 × 1,00 m', 2.0*ESTOFADO_M2, est=True)
# criados-mudos: 85 e 80 de largura, 3 gavetas cada, bordas arredondadas
for i, lc in enumerate((85.0, 80.0), 1):
    corpo('BR', A, lc, 50.0, 45.0, 0, nome=f'criado {i}')
    gaveteiro('BR', A, lc-3, 45.0, 3, 14.0, nome=f'criado {i}')
    curva(A, 1.2)
# painel lateral com espelho orgânico + rack suspenso de TV
painel('AM', 15, A, 'painel do espelho 1200 × 2400', 120, H_PAINEL)
curva(A, 2.4)
_m2esp = 0.60*1.60
terc(A, f'Espelho prata de CORTE ORGÂNICO ({_m2esp:.2f} m²)',
     _m2esp*ESPELHO_M2*ESPELHO_CURVO, est=True)
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
duv(A, 'o ESPELHO É ORGÂNICO (formato de nuvem, sem raio constante). Corte '
       'curvo em espelho é lapidação ponto a ponto: adotei 1,8× o preço do '
       'espelho reto. ★ CONFERIR com a espelharia — pode ser bem mais.')

# ───────────────────────────────────────────────────────────────────────────
# 2 · CLOSET MASTER — closet 02, 7,21 m². Dois lados de 294, aberto.
# ───────────────────────────────────────────────────────────────────────────
A = 'Closet master'
for lado, nome in ((294.0, 'lado A'), (294.0, 'lado B')):
    corpo('BR', A, lado, H_ROUP, P_CLOSET, 3, nome=nome)
prateleiras('BR', A, 90.0, P_CLOSET, 6, 'prateleira superior', com_led=True)
prateleiras('BR', A, 90.0, P_CLOSET, 5, 'sapateira', com_led=True)   # lado B
cabideiro(A, 90.0, 4)                       # cabideiro duplo em 2 vãos
gaveteiro('BR', A, 87.0, P_CLOSET, 4, 18.0, nome='gaveteiro A')
gaveteiro('BR', A, 87.0, P_CLOSET, 4, 18.0, nome='gaveteiro B')
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
corpo('BR', A, 342.0, H_ROUP, P_ROUP, 4, nome='roupeiro · trecho longo')
corpo('BR', A, 230.0, H_ROUP, P_ROUP, 2, nome='roupeiro · retorno em L')
add('BR', 18, A, 'roupeiro · porta 570 × 2500', 57, H_ROUP, 10)
fer(A, dobr=20)
prateleiras('BR', A, 80.0, P_ROUP, 10, 'prateleira do roupeiro')
cabideiro(A, 80.0, 4, com_led=False)
gaveteiro('BR', A, 77.0, P_ROUP, 5, 18.0, nome='gaveteiro do roupeiro')
add('AM', 15, A, 'nicho da TV embutido no roupeiro · fundo e laterais', 100, 60, 3)
led(A, 'LED no nicho da TV', 2.0)
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
corpo('BR', A, 381.0, H_ROUP, P_ROUP, 5, nome='roupeiro')
add('BR', 18, A, 'roupeiro · porta 630 × 2500', 63, H_ROUP, 6)
fer(A, dobr=12)
prateleiras('BR', A, 60.0, P_ROUP, 10, 'prateleira do roupeiro')
cabideiro(A, 60.0, 4, com_led=False)
gaveteiro('BR', A, 57.0, P_ROUP, 4, 18.0, nome='gaveteiro do roupeiro')
# bancada/penteadeira sob a janela
add('AM', 25, A, 'bancada 1660 × 450', 166, 45, 1)
add('AM', 15, A, 'bancada · lateral e montante', 72, 45, 2)
gaveteiro('AM', A, 60.0, 45.0, 2, 14.0, nome='bancada')
led(A, 'LED sob a bancada', 1.66)
esq(A, 2*(3.81+2.50) + 2*(1.66+0.45))
fita(A, 'portas, bancada e bordas',
     6*2*(0.63+2.50) + 10*0.60 + 2*(3.81+2.50) + 2*(1.66+0.45))
duv(A, 'o roupeiro saiu com 381, que é a cota da faixa de marcenaria na planta. '
       'Seis portas de 63 é a modulação que fecha. A bancada de 166 é a cota '
       'da parede sob a janela.')

# ───────────────────────────────────────────────────────────────────────────
# 5 · QUARTO DE VISITAS — suíte 04, 11,26 m². Roupeiro 245.
# ───────────────────────────────────────────────────────────────────────────
A = 'Quarto de visitas'
corpo('BR', A, 245.0, H_ROUP, P_ROUP, 3, nome='roupeiro')
add('BR', 18, A, 'roupeiro · porta de correr 830 × 2500', 83, H_ROUP, 3)
prateleiras('BR', A, 60.0, P_ROUP, 8, 'prateleira do roupeiro')
cabideiro(A, 60.0, 3, com_led=False)
gaveteiro('BR', A, 57.0, P_ROUP, 4, 18.0, nome='gaveteiro do roupeiro')
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
corpo('BR', A, 250.0, H_ROUP, P_ROUP, 3, nome='roupeiro')
add('BR', 18, A, 'roupeiro · porta 620 × 2500', 62, H_ROUP, 4)
fer(A, dobr=8)
prateleiras('BR', A, 60.0, P_ROUP, 8, 'prateleira do roupeiro')
cabideiro(A, 60.0, 3, com_led=False)
gaveteiro('BR', A, 57.0, P_ROUP, 3, 18.0, nome='gaveteiro do roupeiro')
# painel de TV com nichos + bancada de trabalho curva
painel('AM', 15, A, 'painel de TV com nichos 3000 × 2400', 300, H_PAINEL)
add('AM', 15, A, 'nicho suspenso · fundo, laterais e prateleira', 90, 30, 6)
led(A, 'LED nos nichos do painel', 3.6)
add('AM', 25, A, 'bancada de trabalho curva 2000 × 600', 200, 60, 1)
add('AM', 15, A, 'bancada · lateral e montante', 72, 60, 2)
curva(A, 2.2)                    # a bancada é curva na ponta, e o nicho também
gaveteiro('AM', A, 60.0, 60.0, 2, 14.0, nome='bancada')
esq(A, 2*(2.50+2.50) + 2*(3.00+2.40) + 2*(2.00+0.60))
fita(A, 'portas, painel, nichos e bancada',
     4*2*(0.62+2.50) + 8*0.60 + 2*(2.50+2.50) + 2*(3.00+2.40)
     + 6*2*(0.90+0.30) + 2*(2.00+0.60))
duv(A, 'o escritório tem 9,66 m² e a planta cota 320 de parede. Adotei roupeiro '
       'de 250 e painel de TV de 300 — os dois não cabem na mesma parede, e o '
       'render mostra que não estão. CONFERIR em qual parede vai cada um.')
duv(A, 'a bancada de trabalho é CURVA na ponta, como o render mostra. Entram '
       '2,2 m de curva. Tampo em 25 mm para não fletir nos 2 m de vão.')

# ───────────────────────────────────────────────────────────────────────────
# 7 · SALA DE TV — 15,25 m². Painel de 400 com nichos, ripado e bancada.
# ───────────────────────────────────────────────────────────────────────────
A = 'Sala de TV'
painel('AM', 15, A, 'painel de TV 4000 × 2600', 400, 260)
add('AM', 15, A, 'nicho iluminado · fundo, laterais e prateleira', 45, 30, 12)
led(A, 'LED nos nichos e no rasgo do painel', 7.5)
terc(A, 'Drivers da iluminação do painel', 2*DRIVER_UN)
corpo('AM', A, 320.0, 40.0, 40.0, 3, nome='bancada suspensa')
add('AM', 18, A, 'bancada suspensa · porta', 80, 40, 4)
fer(A, dobr=8)
usin(A, 4*0.80)
# ripado da faixa inferior do painel — ripa de 3 cm a passo de 6
N_RIP = 55
add('AM', 15, A, 'ripa do painel', 3, 90, N_RIP)
esq(A, 2*(4.00+2.60) + 2*(3.20+0.40))
fita(A, 'painel, nichos, ripado e bancada',
     2*(4.00+2.60) + 12*2*(0.45+0.30) + N_RIP*2*(0.03+0.90)
     + 4*2*(0.80+0.40) + 2*(3.20+0.40))
duv(A, 'a sala de TV tem 15,25 m² e o render mostra o painel ocupando a parede '
       'inteira, com faixa de mármore atrás da TV. ⛔ O MÁRMORE É MARMORARIA, '
       'está FORA — prevemos o recorte e o encosto da marcenaria nele.')
duv(A, 'o ripado da faixa inferior saiu com 55 ripas de 3 cm a passo de 6, que '
       'é a leitura do render. Sem elevação, é estimativa: cada 10 ripas a '
       'mais ou a menos mexem ~R$ 250 no custo.')
duv(A, 'painel de 400 × 260: a planta dá 15,25 m² de sala mas não cota a parede '
       'do painel. 400 é leitura de escala. CONFERIR.')

# ═══════════════════════════════════════════════════════════════════════════
# CÁLCULO
# ═══════════════════════════════════════════════════════════════════════════
W = 100
N_CARRETO, R_CARRETO = 3, 600.0     # 7 ambientes em 2 pavimentos
N_VISITA,  R_VISITA  = 2, 250.0
LOG = N_CARRETO*R_CARRETO + N_VISITA*R_VISITA

por, area_ch, area_amb = defaultdict(list), defaultdict(float), defaultdict(float)
for m, e, a, d, c, l, q in P:
    for _ in range(q): por[(m, e)].append((c, l))
    ar = c*l*q/10000
    area_ch[(m, e)] += ar; area_amb[a] += ar
CH = {k: nest(v) for k, v in por.items()}
custo_chapa = sum(n*prc(k[0], k[1]) for k, n in CH.items())
area_tot, tot_ch = sum(area_ch.values()), sum(CH.values())
ordem = list(dict.fromkeys(x[2] for x in P))

m_fita_expl = sum(m for _, _, m in FITA)
m_fita = max(m_fita_expl, area_tot*2.6)
custo_fita, custo_filet = m_fita*DESPERD*FITA_M, m_fita*FILET_M
m_usin = sum(m for _, m in USIN);  custo_usin  = m_usin*USIN_M
m_esq  = sum(m for _, m in ESQ);   custo_esq   = m_esq*ESQ_M
m_cur  = sum(m for _, m in CURVA); custo_curva = m_cur*CURVA_M
m_led  = sum(m for _, _, m in LED); custo_led  = m_led*LED_M
custo_terc = sum(v for _, _, v, _ in TERC)
TD = sum(f[0] for f in FER.values())
TC = sum(f[1] for f in FER.values())
TA = sum(f[2] for f in FER.values())
consum_base = custo_chapa + custo_fita

def custo_ferr(cen):
    f = CENARIOS[cen][3]
    return TD*f['dobr'] + TC*f['corr'] + TA*f['art']
def CD(cen):
    return (custo_chapa + custo_fita + custo_filet + custo_usin + custo_esq
            + custo_curva + custo_led + custo_terc + consum_base*0.06
            + custo_ferr(cen) + LOG)

def brl(v, n=2):
    return f'{v:,.{n}f}'.replace(',', '§').replace('.', ',').replace('§', '.')

_fora = [(m, e, a, d, c, l) for m, e, a, d, c, l, q in P
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

print('\nESCOPO')
for a in ordem:
    d, c, t = FER[a]
    ex = [f'{d} dobr.' if d else '', f'{c} corr.' if c else '',
          f'{t} artic.' if t else '']
    print(f'  {a:<24}{area_amb[a]:>7.2f} m²   {" · ".join(x for x in ex if x)}')
print(f'  {"TOTAL":<24}{area_tot:>7.2f} m²')

print('\nPLANO DE CORTE')
for k, n in sorted(CH.items(), key=lambda x: (-x[1], x[0])):
    print(f'  {NOME_MAT[k[0]]+" "+str(k[1])+" mm":<26}{area_ch[k]:>7.2f} m²  →  '
          f'{n:>2} ch. × R$ {prc(*k):>7.2f} = R$ {brl(n*prc(*k)):>9}   aprov. '
          f'{area_ch[k]/(n*CH_AREA)*100:>3.0f}%')
print(f'  {"TOTAL":<26}{area_tot:>7.2f} m²  →  {tot_ch:>2} chapas{"":>19}'
      f'R$ {brl(custo_chapa):>9}   médio {area_tot/(tot_ch*CH_AREA)*100:.0f}%')

print(f'\nFITA E FILETAGEM   {m_fita:.1f} m · R$ {brl(custo_fita)} + R$ {brl(custo_filet)}')
print(f'USINAGEM DE CAVA   {m_usin:.1f} m × R$ {brl(USIN_M)} · R$ {brl(custo_usin)}')
print(f'MEIA ESQUADRIA     {m_esq:.1f} m × R$ {brl(ESQ_M)} · R$ {brl(custo_esq)}')
print(f'★ CURVA            {m_cur:.1f} m × R$ {brl(CURVA_M)} · R$ {brl(custo_curva)}')
print(f'ILUMINAÇÃO         {m_led:.1f} m × R$ {brl(LED_M)} · R$ {brl(custo_led)}')

print('\nTERCEIRIZADOS E ITENS ESPECIAIS   (★ = sem preço fechado na base)')
_por_amb = defaultdict(float)
for a, d, v, est in TERC: _por_amb[a] += v
for a in ordem:
    if _por_amb[a]: print(f'  {a:<24}R$ {brl(_por_amb[a]):>9}')
print(f'  {"TOTAL":<24}R$ {brl(custo_terc):>9}')
for a, d, v, est in TERC:
    if est: print(f'   ★ {a} · {d}: R$ {brl(v)}')

print('\n' + '═'*W)
print('PREÇO — três cenários de ferragem, o mesmo desenho em todos')
print('═'*W)
print(f'  {"Cenário":<18}{"Custo direto":>14}{"sem RT":>13}{"MC real":>9}'
      f'{"com RT 10%":>14}{"MC real":>9}   Garantia')
PRECOS = []
for i, (nome, ferr, mc, _f, gar) in enumerate(CENARIOS):
    cd = CD(i)
    s = round(cd/div(mc, False)/100)*100
    r = round(cd/div(mc, True)/100)*100
    PRECOS.append((s, r))
    print(f'  {nome:<18}{"R$ "+brl(cd,0):>14}{"R$ "+brl(s,0):>13}'
          f'{mc_conferida(s, cd)*100:>8.1f}%{"R$ "+brl(r,0):>14}'
          f'{mc_conferida(r, cd)*100:>8.1f}%   {gar}')
    print(f'  {"":<18}{ferr}')

RT_FECHADO = True
INV = PRECOS[FECHADO][1 if RT_FECHADO else 0]
INV_SEM = PRECOS[FECHADO][0]
CD_F = CD(FECHADO)
print(f'\n  ► RECOMENDADO · cenário {CENARIOS[FECHADO][0]} '
      f'{"COM" if RT_FECHADO else "SEM"} RT ....... R$ {brl(INV,0)}')
print(f'    É o cenário que o Eliuton JÁ FECHOU no 1º orçamento — mesma ferragem,')
print(f'    mesma garantia de {CENARIOS[FECHADO][4]}. Sem RT: R$ {brl(INV_SEM,0)}.')
rm = INV_SEM/area_tot
print(f'  R$/m² de chapa: {rm:.0f} sem RT   (faixa da casa: 626–834 · '
      f'o 1º Eliuton fechou em 624)')
print(f'  Custo direto por m²: {CD_F/area_tot:.0f}   '
      f'(1º Eliuton: 265 · este job é 65% daquele)')
if rm < 626:
    print('  ⚠⚠ MUITO ABAIXO DA FAIXA — e não é erro de conta, é o tipo de job.')
    print('     O 1º Eliuton era cozinha: chapa de cor, bancada, vidro, inox.')
    print('     Este é ROUPEIRO: 213 dos 264 m² são Branco TX, a chapa mais')
    print('     barata da base, e a caixaria repete. Custo direto por m² cai de')
    print('     265 para 172, e o preço cai junto.')
    print('     ⚠ MESMO ASSIM, PRECISA DO OLHO DO JONATHAN ANTES DE IR PARA O')
    print('       CLIENTE: 401 é 36% abaixo do piso da faixa, e a faixa nunca')
    print('       foi aferida num job só de roupeiro. Ou a faixa não se aplica')
    print('       aqui, ou o preço está baixo — as duas leituras são possíveis.')

print('\n' + '─'*W)
print(f'INVESTIMENTO POR AMBIENTE  (cenário {CENARIOS[FECHADO][0]}, com RT)')
cd_amb = defaultdict(float)
_ar_gr = defaultdict(float)
for m, e, a, d, c, l, q in P: _ar_gr[(m, e, a)] += c*l*q/10000
for (m, e, a), ar in _ar_gr.items():
    cd_amb[a] += CH[(m, e)]*prc(m, e) * ar/area_ch[(m, e)]
for a in ordem: cd_amb[a] += m_fita*area_amb[a]/area_tot*(DESPERD*FITA_M + FILET_M)
for a, mm in USIN:  cd_amb[a] += mm*USIN_M
for a, mm in ESQ:   cd_amb[a] += mm*ESQ_M
for a, mm in CURVA: cd_amb[a] += mm*CURVA_M
for a, d, mm in LED: cd_amb[a] += mm*LED_M
for a, d, v, _e in TERC: cd_amb[a] += v
_f = CENARIOS[FECHADO][3]
for a, (dd, cc, tt) in FER.items():
    cd_amb[a] += dd*_f['dobr'] + cc*_f['corr'] + tt*_f['art']
_bruto = sum(cd_amb.values())
for a in list(cd_amb): cd_amb[a] += (consum_base*0.06 + LOG)*cd_amb[a]/_bruto
assert abs(sum(cd_amb.values()) - CD_F) < 0.01, (sum(cd_amb.values()), CD_F)
tots, linhas = 0, []
for a in ordem:
    v = round(INV*cd_amb[a]/CD_F/100)*100
    linhas.append([a, area_amb[a], cd_amb[a], v]); tots += v
linhas[max(range(len(linhas)), key=lambda i: linhas[i][2])][3] += INV - tots
print(f'  {"":24}{"m² chapa":>10}{"custo direto":>14}{"investimento":>15}')
for a, ar, cd_, v in linhas:
    print(f'  {a:<24}{ar:>7.2f} m²{"R$ "+brl(cd_,0):>14}{"R$ "+brl(v,0):>15}')
print(f'  {"TOTAL":<24}{area_tot:>7.2f} m²{"R$ "+brl(CD_F,0):>14}'
      f'{"R$ "+brl(INV,0):>15}')

print('\n' + '─'*W)
print(f'DÚVIDAS E CONFERÊNCIAS — {len(DUV)} itens')
for i, (a, t) in enumerate(DUV, 1):
    print(f'  {i:>2}. [{a}]\n      {t}')
print('\n  ★ Preços adotados, sem linha fechada na base:')
print(f'     · curva (CNC + fita a quente + lixamento) — R$ {brl(CURVA_M,0)}/m')
print(f'     · espelho de corte ORGÂNICO — {ESPELHO_CURVO:.1f}× o espelho reto')
print(f'     · cabeceira estofada — R$ {brl(ESTOFADO_M2,0)}/m² (proxy da laca)')
print(f'     · cabideiro em tubo — R$ {brl(CAB_M,0)}/m')
print(f'     · suporte de prateleira — R$ {brl(SUP_PRAT,0)}/un')
print(f'     · meia esquadria — R$ {brl(ESQ_M,0)}/m · LED comum R$ {brl(LED_M,0)}/m')
print('\n⛔ FORA DO ESCOPO: tudo do 1º orçamento (cozinha, gourmet, área de')
print('   serviço e banheiros, já fechado), mármore da sala de TV, camas,')
print('   colchões, sofás, poltronas, mesas, cadeiras, tapetes, cortinas,')
print('   TVs, ar-condicionado, gesso, sanca, elétrica e pintura.')
print('═'*W)
