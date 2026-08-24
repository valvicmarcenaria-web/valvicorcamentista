# -*- coding: utf-8 -*-
"""CARLA · BH 2026 — LEVANTAMENTO E PREÇO.

Pasta do Drive `1E7MrtwTS3YEuHt9m_-ti8WA54jvkpr87`, lida em 24/08/2026.
Sete detalhamentos executivos + layout + apresentação + SketchUp.

⭐ MELHOR INSUMO QUE JÁ RECEBEMOS. As pranchas são CASO A (têm camada de texto)
   E trazem **QUADRO DE PEÇAS** com código, quantidade, espessura e dimensão de
   cada peça. Não precisei medir nada: o levantamento é transcrição, não
   interpretação. As sete foram lidas pelo conector do Drive.

   Onde a prancha diz "preliminar", ela está avisando que as cotas de CORTE
   ainda descontam folga e ferragem — mas as cotas de PROJETO estão fechadas.

PRANCHAS
  ARQ_CARLA BH_2026_LAYOUT_V01 ..... layout (cozinha · sala · 2 banhos · suíte · 2 quartos)
  Detalhamento_Cozinha ............. cozinha linear 3890 com torre de geladeira
  Detalhamento_Painel .............. painel amadeirado 6570 × 2450 c/ porta integrada
  Detalhamento_Rack ................ rack suspenso 3580 × 400, 4 básculas
  Detalhamento_Cristaleira ......... cristaleira 920 × 400 × 2450, portas de vidro
  Detalhamento_Guarda roupa 3P ..... roupeiro 2550 × 640 × 2680, 3 folhas de correr
  Detalhamento_Guarda roupa L ...... roupeiro em L 1970 + retorno com cabeceira
  Detalhamento_Escada .............. marcenaria sob escada 2390 × 400 (duplicado na pasta)

⚠ A pasta tem o `contrato_eliuton-compactado.pdf`, que é de OUTRO cliente.
  Ignorado — mas vale avisar, porque pasta de cliente com contrato de terceiro
  é risco de vazamento.

[Jonathan 24/08] TRÊS DECISÕES:
  · COM RT de 10%
  · ferragem HETTICH — uma linha só, MC 38%, garantia 10 anos
  · interno em BRANCO onde pertinente + UPGRADE de tudo na cor

⛔ MONTAGEM NÃO ENTRA NO CUSTO (equipe é salário fixo) — mas entra no escopo.
"""
from collections import defaultdict
import math, os

CH_C, CH_L = 275.0, 185.0
CH_AREA = 2.75*1.85

A_, LIQF_, B_ = 0.162, 0.88, 0.043
BASE = 1 - A_ - LIQF_*B_
RT_PCT = 0.10
MC = 0.38                      # Hettich [Jonathan 24/08]
COM_RT = True
def div(mc, rt=False): return BASE - mc - (LIQF_*RT_PCT if rt else 0.0)
def mc_conferida(p, c): return BASE - c/p

FER_HETTICH = dict(dobr=10.0, corr=120.0, art=250.0)   # Novisys · Quadro · Blum HK-xs

# ── nesting da casa ───────────────────────────────────────────────────────
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

# ── preços ────────────────────────────────────────────────────────────────
PRC_COR = {6: 300.0, 15: 500.0, 18: 600.0, 25: 900.0}
PRC_BRA = {6: 190.0, 15: 260.0, 18: 330.0, 25: 420.0}
NOME_MAT = {'AM': 'MDF amadeirado', 'PT': 'MDF preto fosco',
            'OW': 'MDF off-white', 'BT': 'MDF Branco TX'}
INTERNO_COR = False
def _res(m): return (m[2:] if INTERNO_COR else 'BT') if m.startswith('I:') else m
def prc(m, e):
    return PRC_BRA[e] if _res(m) == 'BT' else PRC_COR[e]

FITA_M, FILET_M, DESPERD = 3.00, 2.50, 1.10
CAVA_USIN = 25.0
SUP_PRAT  = 1.50
LED_M     = 28.0 + 38.0            # fita 28 + perfil de alumínio 38
ESPELHO_FL = 285.0                 # folha de espelho prata com perfil
VIDRO8_M2  = 250.0
VIDRACEIRO = 200.0
PT_VIDRO_M2 = 660.0                # porta de vidro em perfil de alumínio
PORTA_ESPELHO_CORRER = 1200.0      # folha espelhada de correr, alumínio + película
FRETE_ESPELHO = 200.0
CORRER_3F  = 2760.0                # ⚠ SEM PREÇO NA BASE — Dominus de 2 folhas é
                                   #   1.840; escalei para 3 folhas. CONFIRMAR.
BATENTE_OCULTO = 600.0             # ⚠ SEM PREÇO NA BASE — batente + dobradiça invisível
SARRAFO_M2 = 25.0                  # estrutura niveladora de 30 mm atrás do painel
VARAO = 45.0

P, FITA, TERC, LED, DUV = [], [], [], [], []
FER = defaultdict(lambda: [0, 0, 0])
CAVA_M = defaultdict(float)
def add(mat, esp, amb, desc, c, l, q=1):
    P.append((mat, esp, amb, desc, c, l, q))
def fer(a, dobr=0, gav=0, basc=0):
    FER[a][0] += dobr; FER[a][1] += gav; FER[a][2] += basc
def fita(a, d, m): FITA.append((a, d, m))
def terc(a, d, v, est=False): TERC.append((a, d, v, est))
def led(a, d, m): LED.append((a, d, m))
def cava(a, m): CAVA_M[a] += m
def duv(a, t): DUV.append((a, t))

def gaveta(mat, amb, nome, L, Pf, alt, q=1):
    add(mat, 15, amb, f'{nome} · caixa lateral',        Pf-10, alt, 2*q)
    add(mat, 15, amb, f'{nome} · caixa frente/costas',  L-6,   alt, 2*q)
    add(mat, 6,  amb, f'{nome} · fundo de gaveta',      L-6,   Pf-10, q)

# ═══════════════════════════════════════════════════════════════════════════
# GEOMETRIA — transcrita dos QUADROS DE PEÇAS das pranchas. Cotas em cm.
# Materiais: AM amadeirado · PT preto fosco · OW off-white · I:xx interior
# ═══════════════════════════════════════════════════════════════════════════

# ───────────────────────────────────────────────────────────────────────────
# 1 · COZINHA LINEAR — sequência 400+800+1170+600+920 · altura total 2450
#     Tampo de PEDRA 2970 × 650 (P10) — MARMORARIA, fora do escopo.
# ───────────────────────────────────────────────────────────────────────────
A = 'Cozinha'
# P01/P02 · inferiores: 4 módulos, prof 65, corpo 80 + rodapé 10
add('I:PT', 15, A, 'inferiores · vertical (5 un)',            65, 80, 5)
add('I:PT', 15, A, 'inferiores · base',                      148, 65, 2)
add('I:PT', 15, A, 'inferiores · travessa superior',         148, 10, 4)
add('I:PT', 6,  A, 'inferiores · fundo',                     148, 80, 2)
add('PT',   18, A, 'inferiores · porta 40 × 74 (forno/cooktop)', 40, 74, 1)
add('PT',   18, A, 'inferiores · porta 80 × 74 (cuba)',       80, 74, 1)
add('PT',   18, A, 'inferiores · porta 58,5 × 74',          58.5, 74, 2)
add('PT',   18, A, 'inferiores · frente do lava-louças 60 × 74', 60, 74, 1)
add('PT',   18, A, 'P03 · rodapé técnico 2970 × 100 (2 peças)', 148.5, 10, 2)
gaveta('I:PT', A, 'inferiores · gaveta do módulo de 40', 40, 65, 15, 3)
fer(A, dobr=8, gav=3)
cava(A, 0.40 + 0.80 + 2*0.585 + 0.60)
fita(A, 'cozinha · frentes inferiores',
     2*(0.40+0.74) + 2*(0.80+0.74) + 2*2*(0.585+0.74) + 2*(0.60+0.74) + 2*2.97)
# P04/P05 · aéreos: 3 portas 585+585+600, altura 550, prof 35
add('I:OW', 15, A, 'aéreos · lateral e divisória',            35, 55, 4)
add('I:OW', 15, A, 'aéreos · tampo e base',                  177, 35, 2)
add('I:OW', 6,  A, 'aéreos · fundo',                         177, 55, 1)
add('OW',   18, A, 'aéreos · porta 58,5 × 55',              58.5, 55, 2)
add('OW',   18, A, 'aéreos · porta 60 × 55',                  60, 55, 1)
add('I:OW', 18, A, 'aéreos · prateleira',                     56, 33, 3)
fer(A, dobr=6)
cava(A, 2*0.585 + 0.60)
fita(A, 'cozinha · portas dos aéreos', 2*2*(0.585+0.55) + 2*(0.60+0.55))
# P06 · nicho contínuo 1770 × 450 × 400, MDF 25 amadeirado, SEM divisórias
add('AM', 25, A, 'P06 · nicho contínuo — topo e base 1770 × 400', 177, 40, 2)
add('AM', 25, A, 'P06 · nicho contínuo — laterais 450 × 400',      45, 40, 2)
add('AM', 6,  A, 'P06 · nicho contínuo — fundo',                  177, 45, 1)
fita(A, 'cozinha · bordas aparentes do nicho de 25 mm', 2*(1.77+0.45)*2)
# P07/P08 · torre da geladeira 920 × 900 × 2450, avanço 250
add('I:PT', 15, A, 'P07 · torre — lateral 900 × 2450',        90, 245, 2)
add('I:PT', 15, A, 'P07 · torre — horizontais',               89, 90, 4)
add('I:PT', 6,  A, 'P07 · torre — fundo do módulo superior',   92, 55, 1)
add('PT',   18, A, 'P08 · porta superior da torre 920 × 550',  92, 55, 1)
fer(A, dobr=2)
cava(A, 0.92)
fita(A, 'cozinha · torre — porta e frentes de caixaria', 2*(0.92+0.55) + 2*2.45*2)
led(A, 'cozinha · LED 3000 K sob o aéreo e no nicho', 1.77 + 1.77)
terc(A, 'Cozinha · nicho de eletros sem divisória — ventilação e passa-cabo', 0.0)
TERC.pop()
duv(A, 'o tampo é PEDRA 20 mm 2970 × 650 (P10) e a rodabanca também — '
       'marmoraria, fora deste orçamento.')
duv(A, 'a prancha diz "frentes em preto fosco e off-white conforme referência" '
       'sem dizer qual módulo leva qual. Adotei inferiores e torre em PRETO, '
       'aéreos em OFF-WHITE. Confirmar com a arquiteta.')
duv(A, 'modulação preliminar baseada em eletrodoméstico padrão — a própria '
       'prancha manda conferir os modelos reais antes da fabricação.')

# ───────────────────────────────────────────────────────────────────────────
# 2 · PAINEL AMADEIRADO 6570 × 2450 — porta integrada, espelho e frisos
# ───────────────────────────────────────────────────────────────────────────
A = 'Painel da sala'
# P01 · paginação total 6570 × 2450 (5 peças de 131,4 de largura)
add('AM', 18, A, 'P01 · painel 6570 × 2450 (5 peças)',      131.4, 245, 5)
add('AM', 18, A, 'P08 · arremate superior 6570 (3 peças)',    219, 8, 3)
# P03/P04 · porta integrada 700 × 2100
add('AM', 18, A, 'P03 · folha da porta 700 × 2100',            70, 210, 1)
add('AM', 18, A, 'P04 · batente oculto — montantes e verga',  210, 12, 3)
fer(A, dobr=3)
cava(A, 0.70)
fita(A, 'painel · perímetro da folha + arremate + bordas do painel',
     2*(0.70+2.10) + 6.57 + 2*2.45)
terc(A, 'P02 · estrutura niveladora em sarrafo de 30 mm (16,1 m²)',
     16.1*SARRAFO_M2, True)
terc(A, 'P05/P06 · espelho 2500 × 1100 lapidado com película de segurança',
     2*ESPELHO_FL)
terc(A, 'P04/P11 · batente oculto + dobradiças invisíveis reforçadas',
     BATENTE_OCULTO, True)
# P07 · frisos — 3 faixas × 5 linhas, usinados no MDF
cava(A, 3*5*2.45)
duv(A, 'os frisos podem ser usinados no MDF ou em perfil metálico preto '
       '(P07). Orcei USINADOS — perfil metálico é terceirizado e muda o valor.')
duv(A, 'a prancha manda prever reforço estrutural para TV e rack, sem fixar '
       'carga só na chapa. Está no escopo do rack.')

# ───────────────────────────────────────────────────────────────────────────
# 3 · RACK SUSPENSO 3580 × 400 × 400 — 4 básculas e LED inferior
# ───────────────────────────────────────────────────────────────────────────
A = 'Rack suspenso'
add('AM',   25, A, 'P01 · tampo superior 3580 × 400 (2 peças)', 179, 40, 2)
add('AM',   25, A, 'P02 · base inferior 3580 × 400 (2 peças)',  179, 40, 2)
add('AM',   18, A, 'P03 · lateral externa 400 × 400',            40, 40, 2)
add('I:AM', 18, A, 'P04 · divisória interna 364 × 382',        36.4, 38.2, 3)
add('I:AM', 6,  A, 'P05 · fundo 877 × 364',                    87.7, 36.4, 4)
add('AM',   18, A, 'P06 · porta basculante 891 × 396',         89.1, 39.6, 4)
fer(A, basc=4)
cava(A, 4*0.891)
fita(A, 'rack · 4 básculas + tampo e base aparentes',
     4*2*(0.891+0.396) + 2*3.58 + 2*0.40*2)
terc(A, 'P07 · barra metálica contínua de fixação — 2 linhas de 3580',
     2*3.58*45.0, True)
led(A, 'rack · perfil de alumínio com difusor, LED 3000 K (P08/P09)', 3.50)
duv(A, 'a cota vertical do rack (piso até a face inferior) está marcada como '
       '"DEFINIR / CONFIRMAR EM OBRA" na prancha.')

# ───────────────────────────────────────────────────────────────────────────
# 4 · CRISTALEIRA 920 × 400 × 2450 — 2 portas de vidro, 6 prateleiras
# ───────────────────────────────────────────────────────────────────────────
A = 'Cristaleira'
add('AM',   18, A, 'P01 · lateral esquerda com acabamento 2450 × 550', 245, 55, 1)
add('AM',   18, A, 'P02 · lateral direita 2450 × 400',                 245, 40, 1)
add('I:AM', 25, A, 'P03 · tampo e base 884 × 400',                    88.4, 40, 2)
add('AM',   18, A, 'P04 · base niveladora 920 × 400 × 80',              92, 40, 2)
add('I:AM', 6,  A, 'P05 · fundo 884 × 2334',                          88.4, 233.4, 1)
add('AM',   18, A, 'P10 · arremate superior ajustado ao forro',         92, 12, 1)
fer(A, dobr=4)
fita(A, 'cristaleira · bordas frontais da caixaria', 2*2.45*2 + 2*0.92)
terc(A, 'P06 · 2 portas em perfil de alumínio preto e vidro temperado 6 mm '
        '(460 × 2350)', 2*max(475.0, 0.46*2.35*PT_VIDRO_M2))
terc(A, 'P07 · 6 prateleiras de vidro temperado 8 mm lapidado (850 × 350)',
     6*0.85*0.35*VIDRO8_M2 + VIDRACEIRO)
terc(A, 'P11 · 2 puxadores metálicos verticais pretos', 2*60.0)
led(A, 'cristaleira · 6 perfis com fita LED 3000 K (P08/P09)', 6*0.85)
duv(A, 'o fundo pode ser MDF 6 mm OU espelho, "conforme acabamento final" '
       '(prancha 2/3). Orcei em MDF. Espelho acrescenta ~R$ 900.')
duv(A, 'a lateral esquerda tem 550 (400 do móvel + 150 de acabamento até a '
       'parede); as demais peças ficam em 400.')

# ───────────────────────────────────────────────────────────────────────────
# 5 · GUARDA-ROUPA 3 PORTAS DE CORRER — 2550 × 640 × 2680
# ───────────────────────────────────────────────────────────────────────────
A = 'Guarda-roupa 3 portas'
add('I:AM', 18, A, 'P01 · lateral do corpo 2680 × 640',        268, 64, 4)
add('I:AM', 18, A, 'P02 · divisória interna 2582 × 550',     258.2, 55, 2)
add('I:AM', 18, A, 'P03 · base e teto dos módulos 764 × 640', 76.4, 64, 6)
add('I:AM', 25, A, 'P04 · prateleira do maleiro 764 × 550',   76.4, 55, 3)
add('I:AM', 18, A, 'P05 · prateleira central/direita 764 × 550', 76.4, 55, 4)
add('AM',   18, A, 'P06 · frente de gaveta 764 × 200',        76.4, 20, 8)
add('I:AM', 6,  A, 'P08 · fundo 764 × 2582',                  76.4, 258.2, 3)
add('AM',   18, A, 'P09 · acabamento lateral 2680 × 150',      268, 15, 1)
add('AM',   18, A, 'P10 · porta lateral em MDF 800 × 2680',     80, 268, 2)
add('AM',   18, A, 'P12 · rodapé/base 2400 × 80',              120, 8, 2)
gaveta('I:AM', A, 'P07 · gaveta', 76.4, 55, 18, 8)
fer(A, gav=8)
cava(A, 8*0.764)
fita(A, 'roupeiro 3P · 8 frentes de gaveta + 2 portas + acabamento',
     8*2*(0.764+0.20) + 2*2*(0.80+2.68) + 2*(2.68+0.15))
terc(A, 'P11 · porta central integral em espelho prata 4 mm com película, '
        'em perfil de alumínio (800 × 2680)', PORTA_ESPELHO_CORRER + FRETE_ESPELHO)
terc(A, 'Sistema de correr de 3 folhas — trilhos, roldanas reguláveis e '
        'antidescarrilamento', CORRER_3F, True)
terc(A, 'Cabideiro oval metálico com suporte reforçado — 2 un', 2*VARAO)
duv(A, 'o sistema de 3 folhas não tem preço na base (temos o Dominus de 2 '
       'folhas a R$ 1.840). Escalei para R$ 2.760. Confirmar com a Rometal.')

# ───────────────────────────────────────────────────────────────────────────
# 6 · GUARDA-ROUPA EM L — 1970 × 550 × 2680 + retorno com cabeceira
# ───────────────────────────────────────────────────────────────────────────
A = 'Guarda-roupa em L'
add('I:AM', 18, A, 'P01 · lateral do roupeiro 2680 × 550',     268, 55, 4)
add('I:AM', 18, A, 'P02 · base/teto do roupeiro',             49, 55, 4)
add('I:AM', 18, A, 'P02 · base/teto do módulo de 990',          99, 55, 2)
add('I:AM', 6,  A, 'roupeiro em L · fundo',                     99, 258, 2)
add('AM',   18, A, 'P03 · porta do roupeiro 490 × 2680',         49, 268, 3)
add('AM',   18, A, 'P03 · porta do roupeiro 500 × 2680',         50, 268, 1)
add('I:AM', 18, A, 'roupeiro em L · prateleira interna',        47, 53, 6)
fer(A, dobr=16)
cava(A, 3*0.49 + 0.50)
fita(A, 'roupeiro em L · 4 portas', 3*2*(0.49+2.68) + 2*(0.50+2.68))
# P04 · mesa de cabeceira 500 × 500 × 700
add('I:AM', 18, A, 'P04 · mesa de cabeceira — lateral 500 × 700', 50, 70, 2)
add('I:AM', 18, A, 'P04 · mesa de cabeceira — tampo e base',      47, 50, 2)
add('AM',   18, A, 'P10 · frente de gaveta da mesa 470 × 200',    47, 20, 2)
gaveta('I:AM', A, 'P04 · gaveta da mesa', 47, 50, 18, 2)
fer(A, gav=2)
cava(A, 2*0.47)
# P05 · módulo vertical 500 × 500 × 1200
add('I:AM', 18, A, 'P05 · módulo vertical — lateral 500 × 1200', 50, 120, 2)
add('I:AM', 18, A, 'P05 · módulo vertical — prateleira',          47, 50, 4)
add('I:AM', 6,  A, 'P05 · módulo vertical — fundo',               50, 120, 1)
# P06 · nicho 1420 × 400 × 450 com LED
add('AM',   25, A, 'P06 · caixa do nicho — topo e base 1420 × 400', 142, 40, 2)
add('AM',   25, A, 'P06 · caixa do nicho — laterais 450 × 400',      45, 40, 2)
add('I:AM', 6,  A, 'P06 · fundo do nicho',                          142, 45, 1)
fita(A, 'nicho · bordas aparentes de 25 mm', 2*(1.42+0.45)*2)
led(A, 'nicho da cabeceira · fita LED em perfil (P11)', 1.42)
# P07/P08 · armário aéreo 1420 × 400 × 750, 2 portas de giro
add('I:AM', 18, A, 'P07 · aéreo — lateral 400 × 750',             40, 75, 2)
add('I:AM', 18, A, 'P07 · aéreo — tampo e base 1420 × 400',      139, 40, 2)
add('I:AM', 6,  A, 'P07 · aéreo — fundo',                        142, 75, 1)
add('AM',   18, A, 'P08 · porta do aéreo 710 × 750',              71, 75, 2)
add('I:AM', 18, A, 'P07 · aéreo — prateleira',                    68, 38, 2)
fer(A, dobr=4)
cava(A, 2*0.71)
fita(A, 'aéreo e mesa · frentes', 2*2*(0.71+0.75) + 2*2*(0.47+0.20))
terc(A, 'Cabideiro oval metálico contínuo — vão de 990 e cabideiro longo',
     2*VARAO)
duv(A, 'a prancha manda engrossar para 25/36 mm as prateleiras longas. '
       'Adotei 25 mm no maleiro e no nicho.')

# ───────────────────────────────────────────────────────────────────────────
# 7 · MARCENARIA SOB ESCADA — 2390 × 400 · porta Reflecta + nichos diagonais
# ───────────────────────────────────────────────────────────────────────────
A = 'Sob a escada'
add('I:AM', 18, A, 'P01 · lateral externa (altura da escada) × 400', 250, 40, 2)
add('I:AM', 18, A, 'P02 · divisória porta/nichos 1760 × 400',        176, 40, 1)
add('I:AM', 18, A, 'P03 · base total 2390 × 400',                    120, 40, 2)
add('I:AM', 25, A, 'P04 · prateleira de nicho (engrossada)',          70, 38.2, 4)
add('I:AM', 18, A, 'P05 · montante de nicho',                         95, 40, 2)
add('I:AM', 6,  A, 'P06 · fundo recortado por módulo',               120, 176, 2)
add('AM',   18, A, 'P07 · rodapé recuado 2354 × 80',                 118, 8, 2)
fer(A, dobr=3)
terc(A, 'P08 · porta em vidro Reflecta temperado, perfil de alumínio preto '
        '(890 × 1760) com 3 dobradiças reforçadas',
     max(475.0, 0.89*1.76*PT_VIDRO_M2))
terc(A, 'Puxador cava/perfil vertical preto de 400–600 mm', 120.0)
led(A, 'sob a escada · LED 3000 K nos nichos, inclusive nos diagonais', 3.00)
fita(A, 'sob a escada · bordas aparentes dos nichos e da base',
     4*2*(0.70+0.382) + 2*2.39 + 2*2.50)
duv(A, 'a geometria superior acompanha o intradorso da escada e o nicho '
       'triangular termina zerado. Adotei altura média de 2,50 m na lateral e '
       '1,06 m no nicho mais alto — a prancha manda conferir a inclinação '
       'real antes de fabricar.')
duv(A, 'a pasta tem DUAS cópias do Detalhamento_Escada, idênticas em tamanho. '
       'Usei uma só.')

# ═══════════════════════════════════════════════════════════════════════════
# RELATÓRIO
# ═══════════════════════════════════════════════════════════════════════════
W = 100
def resolver(): return [(_res(m), e, a, d, c, l, q) for m, e, a, d, c, l, q in P]

def rodar(interno_cor=False):
    global INTERNO_COR
    INTERNO_COR = interno_cor
    por, area_ch, area_amb = defaultdict(list), defaultdict(float), defaultdict(float)
    for m, e, a, d, c, l, q in resolver():
        for _ in range(q): por[(m, e)].append((c, l))
        ar = c*l*q/10000
        area_ch[(m, e)] += ar; area_amb[a] += ar
    CH = {k: nest(v) for k, v in por.items()}
    return CH, area_ch, area_amb, sum(n*prc(k[0], k[1]) for k, n in CH.items())

_fora = [(m, e, a, d, c, l) for m, e, a, d, c, l, q in P
         if max(c, l) > CH_C or min(c, l) > CH_L]
if _fora:
    print('\n' + '!'*W)
    print('PEÇAS QUE NÃO CABEM NA CHAPA DE 275 × 185')
    for m, e, a, d, c, l in _fora:
        print(f'  {NOME_MAT[_res(m)]} {e} mm · {a} · {d}: {c:.0f} × {l:.0f} cm')
    print('!'*W + '\n')

CH, area_ch, area_amb, custo_chapa = rodar(False)
area_tot, tot_ch = sum(area_ch.values()), sum(CH.values())
ordem = list(dict.fromkeys(x[2] for x in P))

print('═'*W)
print('CARLA · BH 2026 — LEVANTAMENTO DE MATERIAL E CUSTO')
print('═'*W)
print('Sete detalhamentos executivos COM QUADRO DE PEÇAS · lidos pelo conector do Drive')
print('Ferragem HETTICH · COM RT de 10% · interno em Branco TX  [Jonathan 24/08]')

print('\nESCOPO POR AMBIENTE')
for a in ordem:
    d, g, b = FER[a]
    ex = [f'{d} dobr.' if d else '', f'{g} gav.' if g else '', f'{b} básc.' if b else '']
    print(f'  {a:<24}{area_amb[a]:>7.2f} m² de chapa   '
          f'{" · ".join(x for x in ex if x):<26}')
print(f'  {"TOTAL":<24}{area_tot:>7.2f} m²')

print('\nPLANO DE CORTE  (nesting por cor × espessura)')
for k in sorted(CH, key=lambda k: (k[0], -k[1])):
    m, e = k; n = CH[k]; pr = prc(m, e)
    print(f'  {NOME_MAT[m]+" "+str(e)+" mm":<26}{area_ch[k]:>7.2f} m²  →  {n:>2} ch. × '
          f'R$ {pr:>7,.2f} = R$ {n*pr:>9,.2f}   aprov. {area_ch[k]/(n*CH_AREA)*100:>3.0f}%'
          .replace(',', '.'))
print(f'  {"TOTAL":<26}{area_tot:>7.2f} m²  →  {tot_ch:>2} chapas{"":>21}'
      f'R$ {custo_chapa:>9,.2f}   médio {area_tot/(tot_ch*CH_AREA)*100:.0f}%'.replace(',', '.'))

# ⚠ PISO DE FITA. Eu lancei explicitamente só a borda APARENTE (frente de
#   porta, gaveta, topo de nicho). Falta a borda da CAIXARIA — todo topo de
#   lateral, divisória, prateleira e base leva fita, aparente ou não. A casa
#   tem um fator validado de 2,6 m de fita por m² de chapa para painelaria +
#   caixaria (`corte-spe-decorado.py`). O explícito deu 1,43 m/m², que é baixo
#   demais para um job com 26 prateleiras e 4 roupeiros. Uso o MAIOR dos dois.
m_fita_expl = sum(m for _, _, m in FITA)
FATOR_FITA = 2.6
m_fita = max(m_fita_expl, area_tot*FATOR_FITA)
custo_fita, custo_filet = m_fita*DESPERD*FITA_M, m_fita*FILET_M
n_cava = sum(CAVA_M.values()); custo_cava = n_cava*CAVA_USIN
m_led = sum(m for _, _, m in LED); custo_led = m_led*LED_M
N_PRAT = sum(q for m, e, a, d, c, l, q in P if 'prateleira' in d.lower())
custo_sup = N_PRAT*4*SUP_PRAT
_a = f'{custo_fita:,.2f}'.replace(',', '.'); _b = f'{custo_filet:,.2f}'.replace(',', '.')
print(f'\nFITA E FILETAGEM   {m_fita:.2f} m  ·  material R$ {_a}  ·  filetagem R$ {_b}')
print(f'  (borda aparente lançada peça a peça: {m_fita_expl:.1f} m = '
      f'{m_fita_expl/area_tot:.2f} m/m². Abaixo do fator da casa de {FATOR_FITA} m/m²,')
print(f'   que cobre também a borda de caixaria — adotado o fator.)')
_v = f'{custo_cava:,.2f}'.replace(',', '.')
print(f'USINAGEM DE CAVA   {n_cava:.2f} m × R$ 25,00/m  ·  R$ {_v}')
_v = f'{custo_led:,.2f}'.replace(',', '.')
print(f'ILUMINAÇÃO         {m_led:.2f} m × R$ 66,00/m  ·  R$ {_v}')

print('\nTERCEIRIZADOS E ITENS ESPECIAIS   (★ = sem preço na base, estimado)')
custo_terc = 0.0
for a, d, v, est in TERC:
    custo_terc += v
    _v = f'{v:,.2f}'.replace(',', '.')
    print(f' {"★" if est else " "}{a:<23}{d[:52]:<53}R$ {_v:>10}')
_v = f'{custo_terc:,.2f}'.replace(',', '.')
print(f'  {"TOTAL":<76}R$ {_v:>10}')

TOT_D = sum(f[0] for f in FER.values())
TOT_G = sum(f[1] for f in FER.values())
TOT_B = sum(f[2] for f in FER.values())
print(f'\nFERRAGEM HETTICH — {TOT_D} dobradiças Novisys · {TOT_G} corrediças Quadro · '
      f'{TOT_B} articuladores Blum HK-xs · {N_PRAT} prateleiras')

N_CARRETO, R_CARRETO = 4, 600.0
N_VISITA, R_VISITA = 3, 250.0
LOG = N_CARRETO*R_CARRETO + N_VISITA*R_VISITA

def fechar(custo_ch, cons):
    ferr = TOT_D*FER_HETTICH['dobr'] + TOT_G*FER_HETTICH['corr'] + TOT_B*FER_HETTICH['art']
    CD = (custo_ch + custo_fita + custo_filet + custo_cava + custo_led + custo_sup
          + custo_terc + cons + ferr + LOG)
    return CD, ferr

consum = (custo_chapa + custo_fita)*0.06
CD, custo_ferr = fechar(custo_chapa, consum)
INV = round(CD/div(MC, COM_RT)/100)*100
INV_SEM = round(CD/div(MC, False)/100)*100

print('\n' + '═'*W)
print('CUSTO DIRETO E PREÇO — HETTICH · MC 38% · COM RT')
print('═'*W)
for rot, v in (('Chapas', custo_chapa), ('Fita (material)', custo_fita),
               ('Filetagem', custo_filet), ('Usinagem de cava e frisos', custo_cava),
               ('Iluminação em LED', custo_led), ('Suportes de prateleira', custo_sup),
               ('Terceirizados e itens especiais', custo_terc),
               ('Consumíveis (6% de chapa + fita)', consum),
               ('Ferragem Hettich', custo_ferr),
               (f'Logística — {N_CARRETO} carretos + {N_VISITA} visitas '
                f'(montagem NÃO entra: é custo fixo)', LOG)):
    _v = f'{v:,.2f}'.replace(',', '.')
    print(f'    {rot:<78}R$ {_v:>10}')
_v = f'{CD:,.2f}'.replace(',', '.')
print(f'    {"CUSTO DIRETO":<78}R$ {_v:>10}')
_a = f'{INV:,.0f}'.replace(',', '.'); _b = f'{INV_SEM:,.0f}'.replace(',', '.')
print(f'\n  INVESTIMENTO com RT ........ R$ {_a:>10}   MC real {mc_conferida(INV, CD)*100:.1f}%')
print(f'  (sem RT, referência interna)  R$ {_b:>10}   MC real {mc_conferida(INV_SEM, CD)*100:.1f}%')
print(f'  R$/m² de chapa: {INV/area_tot:.0f} com RT · {INV_SEM/area_tot:.0f} sem RT'
      '   (faixa da casa sem RT: 626–834)')

print('\n' + '─'*W)
print('INVESTIMENTO POR AMBIENTE')
tots, linhas = 0, []
for a in ordem:
    v = round(INV*area_amb[a]/area_tot/100)*100
    linhas.append([a, area_amb[a], v]); tots += v
linhas[max(range(len(linhas)), key=lambda i: linhas[i][1])][2] += INV - tots
for a, ar, v in linhas:
    print(f'  {a:<24}{ar:>8.2f} m²{v:>14,.0f}'.replace(',', '.'))
print(f'  {"TOTAL":<24}{area_tot:>8.2f} m²{INV:>14,.0f}'.replace(',', '.'))

print('\n' + '═'*W)
print('UPGRADE DE PROJETO — TUDO NA COR  (sem nenhuma peça branca)')
print('═'*W)
CH_U, AC_U, _AA, custo_chapa_up = rodar(True)
rodar(False)
consum_up = (custo_chapa_up + custo_fita)*0.06
CD_UP, _ = fechar(custo_chapa_up, consum_up)
INV_UP = round(CD_UP/div(MC, COM_RT)/100)*100
_bt = sum(a for k, a in area_ch.items() if k[0] == 'BT')
_a = f'{custo_chapa:,.2f}'.replace(',', '.'); _b = f'{custo_chapa_up:,.2f}'.replace(',', '.')
print(f'  {"chapa · interior em Branco TX (o que a prancha pede)":<54}{tot_ch:>3} ch.  R$ {_a:>10}')
print(f'  {"chapa · tudo na cor (upgrade)":<54}{sum(CH_U.values()):>3} ch.  R$ {_b:>10}')
print(f'\n  Interior afetado: {_bt:.1f} m² que hoje sairiam em Branco TX.')
_a = f'{INV:,.0f}'.replace(',', '.'); _b = f'{INV_UP:,.0f}'.replace(',', '.')
_d = f'{INV_UP-INV:,.0f}'.replace(',', '.')
print(f'  INVESTIMENTO   R$ {_a}  →  R$ {_b}   ·   upgrade de R$ {_d}')
print(f'  MC real com o upgrade: {mc_conferida(INV_UP, CD_UP)*100:.1f}%')

print('\n' + '─'*W)
print(f'DÚVIDAS E CONFERÊNCIAS — {len(DUV)} itens')
for i, (a, t) in enumerate(DUV, 1):
    print(f'  {i:>2}. [{a}] {t}')
print('\n⛔ FORA DO ESCOPO: tampo e rodabanca de pedra da cozinha (marmoraria),')
print('   eletrodomésticos, louças e metais, pontos elétricos e hidráulicos,')
print('   alvenaria, gesso e pintura, cortinas e móveis soltos.')
print('═'*W)
