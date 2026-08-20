# -*- coding: utf-8 -*-
"""CAROL E VINÍCIUS — CADERNO DE MARCENARIA · LEVANTAMENTO E PREÇO.

Projeto: Jéssica Sollero Design de Interiores (jessicasollerointeriores@gmail.com
· 31-98406.0172) · MARCENARIA · 20 de julho de 2026 · escala 1:25 · 49 pranchas.
Carimbo em todas as folhas: "CONFERIR MEDIDAS NO LOCAL".

O PDF é do CASO B (`referencias/quantitativo.md`, "Prancha em PDF: três casos"):
0 palavras de texto, 337.884 vetores — o texto está EM CURVAS. Não dá para ler
pelo conector; a leitura foi visual sobre render a 2,9× com rotação de +90°.
A geometria, porém, é vetorial e cotada: as medidas abaixo saíram das COTAS
ESCRITAS na prancha, não de medição em pixel.

MATERIAIS DO PROJETO (nomenclatura da arquiteta):
  · MDF **Areal** — ARAUCO     (amadeirado claro: painéis, ripados, prateleiras)
  · MDF **Frapê** — ARAUCO     (armários, racks, bancadas, frentes)
  · MDF **Branco TX**          (interno de armário)
  · MDF **Trevi** — DURATEX    (nicho da sala de jantar)
  · MDF **Cru**                (base do espelho do lavabo)
Nota em todas as pranchas: "ATENÇÃO AO PADRÃO DE VEIOS DOS MDF AMADEIRADOS —
SEGUIR VEIOS NOS ENCONTROS EM TODOS OS DETALHES." Isso ENCARECE o nesting:
peça de veio orientado não gira 90° para caber. Está tratado no fim, na
sensibilidade.

⚠ MESMO BURACO DO ELIUTON: Areal e Frapê são linhas Arauco e a base da casa não
  tem preço nominal de Arauco amadeirado. Rodo em COR (500/600/300) e mostro a
  sensibilidade em ESPECIAL (950/1200/800). CONFIRMAR COM O FORNECEDOR.

[Jonathan 19/08] TRÊS DECISÕES FECHADAS:
  · o projeto vai **COM RT** de 10% para a Jéssica Sollero
  · a escada de MC é **30 / 35 / 38** — confirmada
  · preço de chapa em COR e as estimativas dos terceirizados — confirmados

⛔ MONTAGEM NÃO ENTRA NO CUSTO (montador é salário fixo) — mas ENTRA NO ESCOPO
   da proposta. Ver `referencias/validacao-orcamento.md`.
"""
from collections import defaultdict
import math

CH_C, CH_L = 275.0, 185.0
CH_AREA = 2.75 * 1.85                       # 5,0875 m²

# ── motor comercial ────────────────────────────────────────────────────────
A_, LIQF_, B_ = 0.162, 0.88, 0.043          # conjunto SEM RT
BASE = 1 - A_ - LIQF_*B_                    # 0,80016
RT_PCT = 0.10
MC_RIPADO = 0.40                            # ripado tem MC própria em todo cenário

def div(mc, rt=False): return BASE - mc - (LIQF_*RT_PCT if rt else 0.0)
def preco(resto, rip, mc, rt=False): return resto/div(mc, rt) + rip/div(MC_RIPADO, rt)
def mc_conferida(p, c): return BASE - c/p

HK_XS = 250.0
MCS = [0.30, 0.35, 0.38]        # [Jonathan 19/08] confirmada
COM_RT = True                   # [Jonathan 19/08] o projeto vai com RT de 10%
CENARIOS = [
    ('I · Telescópica', 'Padrão · telescópica · pistão simples', dict(dobr=6.0,  corr=40.0,  art=20.0),  '2 anos'),
    ('II · Hardt',      'Hardt · oculta Hardt · Blum HK-xs',     dict(dobr=8.0,  corr=70.0,  art=HK_XS), '5 anos'),
    ('III · Hettich',   'Novisys · oculta Quadro · Blum HK-xs',  dict(dobr=10.0, corr=120.0, art=HK_XS), '10 anos'),
]

# ── nesting da casa ────────────────────────────────────────────────────────
def _pack_faixa(pcs):
    chapas = 0; y = x = faixa = 0.0
    for c, l in pcs:
        if c > CH_C and l <= CH_C: c, l = l, c
        if c > CH_C or l > CH_L: chapas += 1; continue
        if x + c > CH_C: y += faixa; x = 0.0; faixa = 0.0
        if y + l > CH_L: chapas += 1; y = x = faixa = 0.0
        x += c; faixa = max(faixa, l)
    return chapas + 1

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
    base = [(max(c, l), min(c, l)) for c, l in items]
    ordens = [lambda p: -p[1], lambda p: (-p[1], -p[0]), lambda p: -p[0], lambda p: -p[0]*p[1]]
    chapas = min(pk(sorted(base, key=k)) for pk in (_pack_faixa, _pack_bf) for k in ordens)
    area = sum(c*l for c, l in items)/10000
    return max(chapas, -(-int(area/(CH_AREA*0.80)*1000)//1000) or 1)

# ═══════════════════════════════════════════════════════════════════════════
# PREÇOS DE COMPRA — dados/materiais.json + referencias/*
# ═══════════════════════════════════════════════════════════════════════════
PRC_COR = {15: 500.0, 18: 600.0, 6: 300.0, 25: 900.0}
PRC_ESP = {15: 950.0, 18: 1200.0, 6: 800.0, 25: 1600.0}
PRC_BRA = {15: 260.0, 18: 330.0, 6: 190.0, 25: 420.0}
PRC_CRU = {15: 190.0, 18: 240.0, 6: 140.0, 25: 320.0}   # ⚠ não está na base — estimado

NOME_MAT = {'AR': 'MDF Areal (Arauco)', 'FR': 'MDF Frapê (Arauco)',
            'TV': 'MDF Trevi (Duratex)', 'BT': 'MDF Branco TX', 'CR': 'MDF Cru'}
FAMILIA  = {'AR': 'cor', 'FR': 'cor', 'TV': 'cor', 'BT': 'branco', 'CR': 'cru'}
ESPECIAL = False           # alavanca da sensibilidade
def prc(mat, esp):
    f = FAMILIA[mat]
    if f == 'branco': return PRC_BRA[esp]
    if f == 'cru':    return PRC_CRU[esp]
    return (PRC_ESP if ESPECIAL else PRC_COR)[esp]

FITA_COR, FILET_MAQ, DESPERD = 3.00, 2.50, 1.10
CAVA_USIN = 25.0        # R$/m linear de cava/chanfro usinado na CNC [Honda 07/08]
SUP_PRAT  = 1.50
LED_M     = 28.0 + 38.0 # fita 28 + perfil alumínio 38  (NÃO os R$150 agregados)
ESPELHO_FL = 285.0      # R$/FOLHA de espelho prata com perfil — NUNCA por m²
VIDRO8_M2  = 250.0      # vidro incolor temperado 8 mm — este a casa cota por m²
VIDRACEIRO = 200.0      # serviço mínimo
PT_VIDRO   = 475.0      # porta de vidro reflecta bronze + alumínio + Sotille (mín.)
PT_VIDRO_M2 = 660.0     # acima do mínimo, por m²  [ref. Kenia & Fábio 12/06]
RO65, TRILHO_RO65 = 60.0, 60.0   # correr de armário RASO (espelho de banheiro)
RO82_TOP   = 400.0      # deslizante embutido no gesso, amortecido (portas grandes)
PERF_ALU_M = 60.0       # perfil de alumínio na base da porta
PUX_TRAVERTINO = 150.0  # ⚠ SEM PREÇO NA BASE — marmoraria, peça 6×6 usinada
SERRALH_MEZ = 2500.0    # ⚠ SEM PREÇO NA BASE — estrutura de metalon do mezanino
CORDA_GC    = 800.0     # ⚠ SEM PREÇO NA BASE — guarda-corpo de corda + ferragem
TUBO_CHAMP  = 900.0     # ⚠ SEM PREÇO NA BASE — pés chumbados em tubo champagne
TUBINHO_CH  = 400.0     # ⚠ SEM PREÇO NA BASE — acabamento tubinho champagne
ESTOF_PAREDE = 1800.0   # estofador — peça 'completo' da base
ESTOF_CAB    = 650.0    # estofador — peça 'cabeceira'
ACRILICO     = 180.0    # divisória interna em acrílico (penteadeira)

# ── ripado: a prancha CRAVA a geometria ────────────────────────────────────
# "ripas de 3x2 espassamento de 3cm" ⇒ ripa 3,0 cm larga × 2,0 cm espessa,
# vão de 3,0 cm ⇒ passo 6,0 cm. Diferente do Eliuton, onde o passo era premissa.
# ⚠ 2,0 cm não é espessura de chapa: corto a régua em 18 mm (chapa existente).
RIPA_L, RIPA_PASSO = 3.0, 6.0

# ═══════════════════════════════════════════════════════════════════════════
# GEOMETRIA — (material, espessura, ambiente, descrição, comp, larg, qtd, ripado)
# Regra da casa: 15 caixaria · 18 frentes e prateleiras · 6 fundos.
# ═══════════════════════════════════════════════════════════════════════════
P = []
def add(mat, esp, amb, desc, c, l, q=1, rip=False):
    P.append((mat, esp, amb, desc, c, l, q, rip))

def caixa(mat, amb, nome, L, H, Pf, nvert=0, nprat=0, fundo=True, tampo=True,
          base=True, mat_int=None):
    mi = mat_int or mat
    nlat = 2 + nvert
    add(mi, 15, amb, f'{nome} · lateral/divisória', Pf, H, nlat)
    Lh = L - 1.5*nlat
    # ⚠ peça horizontal maior que a chapa sai EMENDADA — a emenda cai sobre uma
    #   divisória, que é onde ela some. Sem isso o `nest` abre uma chapa por peça.
    kt = math.ceil(Lh/260.0)
    sf = ' (emendado)' if kt > 1 else ''
    if tampo: add(mi, 15, amb, f'{nome} · tampo{sf}', Lh/kt, Pf, kt)
    if base:  add(mi, 15, amb, f'{nome} · base{sf}',  Lh/kt, Pf, kt)
    if nprat:
        Lv = Lh/(nvert+1)
        add(mi, 18, amb, f'{nome} · prateleira', Lv, Pf-2, nprat)
    if fundo:
        kf = math.ceil(L/260.0)
        add(mi, 6, amb, f'{nome} · fundo{" (emendado)" if kf > 1 else ""}',
            L/kf, H, kf)

def gaveta(mat, amb, nome, L, Pf, alt, q=1):
    add(mat, 15, amb, f'{nome} · gaveta lateral',       Pf-10, alt, 2*q)
    add(mat, 15, amb, f'{nome} · gaveta frente/costas', L-6,   alt, 2*q)
    add(mat, 6,  amb, f'{nome} · gaveta fundo',         L-6,   Pf-10, q)

def ripado(mat, amb, nome, L, H, base_esp=15, nh=1, nv=1):
    """Painel ripado tipo 2 — painel de fundo + réguas coladas, quebrado em
    nh × nv peças para caber na chapa de 275 × 185."""
    n = int(L/RIPA_PASSO)
    add(mat, base_esp, amb, f'{nome} · painel de fundo ({nh}×{nv} peças)',
        L/nh, H/nv, nh*nv, True)
    add(mat, 18, amb, f'{nome} · régua {RIPA_L:.0f} × {H/nv:.0f} cm',
        RIPA_L, H/nv, n*nv, True)
    return n

FER = defaultdict(lambda: [0, 0, 0])
def fer(amb, dobr=0, gav=0, basc=0):
    FER[amb][0] += dobr; FER[amb][1] += gav; FER[amb][2] += basc

FITA = []
def fita(amb, desc, m): FITA.append((amb, desc, m))

TERC = []
def terc(amb, desc, v, est=False): TERC.append((amb, desc, v, est))

CAVA_M = defaultdict(float)
def cava(amb, m): CAVA_M[amb] += m

LED = []
def led(amb, desc, m): LED.append((amb, desc, m))

DUVIDAS = []
def duv(amb, txt): DUVIDAS.append((amb, txt))

# ───────────────────────────────────────────────────────────────────────────
# 1 · LAVABO — pranchas 02 e 03 · painel ripado de 126 × 148
#     Ripado MDF Areal · espelho prata colado em MDF Cru · LED 4000K sup+inf
# ───────────────────────────────────────────────────────────────────────────
A = 'Lavabo'
# faixa ripada superior 126 × 30 e inferior 126 × 20; espelho de 126 × 98 no meio
ripado('AR', A, 'painel ripado superior 126 × 30', 126, 30)
ripado('AR', A, 'painel ripado inferior 126 × 20', 126, 20)
add('CR', 15, A, 'base do espelho prata 126 × 98 (MDF Cru)', 126, 98)
add('AR', 18, A, 'moldura/testeira do painel (perímetro, 3 peças)', 148, 5, 3)
terc(A, 'Espelho prata 126 × 98 colado em MDF Cru — 1 folha', ESPELHO_FL)
led(A, 'LED 4000K superior e inferior do painel ripado', 2*1.26)
fita(A, 'painel ripado · bordas aparentes', 2*(1.26+1.48) + 2*(1.26+0.98))
duv(A, 'a bancada e o nicho inferior do lavabo aparecem em pedra na perspectiva '
       '— não entraram. Se forem marcenaria, são item novo.')

# ───────────────────────────────────────────────────────────────────────────
# 2 · SALA JANTAR — pranchas 04 a 11 · pé-direito 262,5 · armário 242,5
#     Cristaleira + nicho Trevi + armário inferior na parede de 230 (prof 50)
#     Painéis e portas de correr em MDF Frapê · marco do vão em MDF Areal
#     Sapateira em MDF Areal · PUXADOR TRAVERTINO 6×6 — 04 UNIDADES
# ───────────────────────────────────────────────────────────────────────────
A = 'Sala de jantar'
# ── cristaleira 230 × 114,5 × 35,5 — 4 portas de vidro reflecta bronze ─────
# ⚠ a cristaleira tem porta de VIDRO: o interior aparece. Caixaria toda em
#   Frapê, sem forro branco — ao contrário dos armários fechados.
caixa('FR', A, 'cristaleira 230 × 114,5 × 35,5', 230, 114.5, 35.5, nvert=1,
      nprat=0, fundo=True, mat_int=None)
fer(A, dobr=8)
terc(A, 'Cristaleira · 4 portas de vidro reflecta bronze c/ alumínio bronze e '
        'puxador Sotille (47,5 × 109,5)', 4*max(PT_VIDRO, 0.475*1.095*PT_VIDRO_M2))
terc(A, 'Cristaleira · 4 prateleiras de vidro incolor temperado 8 mm (92 × 32)',
     4*0.92*0.32*VIDRO8_M2 + VIDRACEIRO)
led(A, 'cristaleira · LED 3000K posterior das prateleiras', 4*0.92)
fita(A, 'cristaleira · bordas frontais da caixaria', 2*1.145*3 + 2*2.30)

# ── nicho MDF Trevi 230 × 66 × 35,5 c/ LED superior ───────────────────────
caixa('TV', A, 'nicho Trevi 230 × 66 × 35,5', 230, 66, 35.5, nvert=1, nprat=0)
led(A, 'nicho Trevi · LED superior 3000K', 2.30)
fita(A, 'nicho Trevi · bordas frontais', 2*(2.30+0.66) + 2*0.66)

# ── armário inferior 230 × 82 × 50 — 4 gavetas + 4 portas ─────────────────
caixa('FR', A, 'armário inferior 230 × 82 × 50', 230, 82, 50, nvert=3, nprat=4,
      mat_int='BT')
add('FR', 18, A, 'armário inferior · frente de gaveta 47,5 × 17,2', 47.5, 17.2, 4)
add('FR', 18, A, 'armário inferior · porta 47,5 × 60', 47.5, 60, 4)
gaveta('BT', A, 'armário inferior · gaveta', 47.5, 50, 14, 4)
fer(A, dobr=8, gav=4)
cava(A, 4*0.475)          # puxador chanfrado nas 4 portas
fita(A, 'armário inferior · frentes de gaveta e portas',
     4*2*(0.475+0.172) + 4*2*(0.475+0.60))
terc(A, 'Puxador em mármore travertino 6×6 cm — 04 unidades (gavetas)',
     4*PUX_TRAVERTINO, True)

# ── elevação B: painel c/ porta de giro + marco do vão + painel/porta correr ─
add('FR', 18, A, 'elev. B · painel 120 × 262,5 (2 peças)', 120, 131.25, 2)
add('FR', 18, A, 'elev. B · porta de giro 76 × 210', 76, 210)
fer(A, dobr=3); cava(A, 0.76)
fita(A, 'elev. B · painel + porta de giro', 2*(1.20+2.625) + 2*(0.76+2.10))
add('AR', 18, A, 'marco do vão 140 × 150 · montantes (150 × 22)', 150, 22, 2)
add('AR', 18, A, 'marco do vão 140 × 150 · travessas (140 × 22)', 140, 22, 2)
fita(A, 'marco do vão · perímetro aparente', 2*(1.40+1.50)*2)
add('FR', 18, A, 'elev. B · painel 140 × 262,5 (2 peças)', 140, 131.25, 2)
add('FR', 18, A, 'elev. B · porta de correr 140 × 242,5 (2 peças emendadas)',
    140, 121.25, 2)
cava(A, 1.40)
fita(A, 'elev. B · painel + porta de correr', 2*(1.40+2.625) + 2*(1.40+2.425))
terc(A, 'Elev. B · sistema deslizante embutido no gesso, amortecido (porta 140)',
     RO82_TOP)
terc(A, 'Elev. B · perfil de alumínio na base (porta 140 + porta 76)',
     (1.40+0.76)*PERF_ALU_M)

# ── elevação C: painel 120 × 262,5 + porta de correr 72 × 230 ─────────────
add('FR', 18, A, 'elev. C · painel 120 × 262,5 (2 peças)', 120, 131.25, 2)
add('FR', 18, A, 'elev. C · porta de correr 72 × 230', 72, 230)
cava(A, 0.72)
fita(A, 'elev. C · painel + porta de correr', 2*(1.20+2.625) + 2*(0.72+2.30))
terc(A, 'Elev. C · sistema deslizante embutido no gesso, amortecido (porta 72)',
     RO82_TOP)
terc(A, 'Elev. C · perfil de alumínio na base (porta 72)', 0.72*PERF_ALU_M)

# ── elevação D: sapateira MDF Areal 52,5 × 105 × 25, 4 prateleiras inclinadas ─
caixa('AR', A, 'sapateira 52,5 × 105 × 25', 52.5, 105, 25, nprat=4)
fita(A, 'sapateira · bordas frontais', 2*(0.525+1.05) + 4*0.50)
duv(A, 'a sapateira tem 52,5 de largura na elevação D e a planta traz 94 e 62 '
       'na mesma região — adotei a cota da elevação (52,5 × 105 × 25).')
duv(A, 'a região de 140 × 100 abaixo do vão da elevação B está com hachura de '
       'parede e rodapé, não de marcenaria — não entrou.')

# ───────────────────────────────────────────────────────────────────────────
# 3 · SALA ESTAR — pranchas 12 a 17 · parede de 443,5 e painel de 228
#     PUXADOR TRAVERTINO 6×6 — 09 UNIDADES (6 do buffet + 3 do rack)
# ───────────────────────────────────────────────────────────────────────────
A = 'Sala de estar'
# ── buffet suspenso 443,5 × 80 × 45 — 6 gavetões, LED sup e inf ───────────
caixa('FR', A, 'buffet suspenso 443,5 × 80 × 45', 443.5, 80, 45, nvert=5,
      nprat=0, mat_int='BT')
add('FR', 18, A, 'buffet · frente de gavetão 70,5 × 60', 70.5, 60, 6)
gaveta('BT', A, 'buffet · gavetão', 70.5, 45, 55, 6)
fer(A, gav=6)
led(A, 'buffet · LED 3000K superior e inferior', 2*4.435)
fita(A, 'buffet · frentes dos 6 gavetões', 6*2*(0.705+0.60))
terc(A, 'Puxador em mármore travertino 6×6 cm — 06 unidades (buffet)',
     6*PUX_TRAVERTINO, True)

# ── painel elevação B 228 × 262,5 — armário superior, ripado, prateleiras ──
caixa('AR', A, 'elev. B · armário superior 228 × 59 × 30', 228, 59, 30, nvert=1,
      nprat=0, mat_int='BT')
n1 = ripado('AR', A, 'elev. B · frentes ripadas do armário superior (6 × 38 × 59)',
            228, 59)
fer(A, dobr=12); cava(A, 6*0.38)
fita(A, 'elev. B · 6 portas superiores', 6*2*(0.38+0.59))
# painel ripado central da TV (152 × 118,5) + faixa ripada de 30
n2 = ripado('AR', A, 'elev. B · painel ripado central da TV 152 × 118,5', 152, 118.5)
n3 = ripado('AR', A, 'elev. B · faixa ripada 228 × 30', 228, 30)
led(A, 'elev. B · LED 3000K inferior do painel', 2.28)
# colunas laterais abertas — 8 prateleiras de 34 × 30
add('AR', 15, A, 'elev. B · laterais das colunas abertas', 30, 118.5, 4)
add('AR', 18, A, 'elev. B · prateleira lateral 34 × 30', 34, 30, 8)
add('BT', 6,  A, 'elev. B · fundo das colunas abertas', 34, 118.5, 2)
fita(A, 'elev. B · 8 prateleiras laterais + colunas', 8*0.34 + 4*1.185)
# rack 228 × 50 × 61 — 3 gavetões de 76
caixa('FR', A, 'rack 228 × 50 × 61', 228, 50, 61, nvert=2, nprat=0, mat_int='BT')
add('FR', 18, A, 'rack · frente de gavetão 76 × 47', 76, 47, 3)
gaveta('BT', A, 'rack · gavetão', 76, 61, 42, 3)
fer(A, gav=3)
fita(A, 'rack · frentes dos 3 gavetões', 3*2*(0.76+0.47))
terc(A, 'Puxador em mármore travertino 6×6 cm — 03 unidades (rack)',
     3*PUX_TRAVERTINO, True)

# ───────────────────────────────────────────────────────────────────────────
# 4 · VARANDA — pranchas 18 a 21
#     Armário MDF Areal SEM FUNDO c/ prateleiras de vidro e tubinho champagne
#     Armário inferior MDF Frapê 90 × 80 × 50 · bancada MDF Areal 300 × 90
#     PUXADOR TRAVERTINO 6×6 — 01 UNIDADE
# ───────────────────────────────────────────────────────────────────────────
A = 'Varanda'
caixa('AR', A, 'armário superior 73 × 168 × 22 (SEM FUNDO)', 73, 168, 22,
      nprat=0, fundo=False)
terc(A, 'Varanda · 3 prateleiras de vidro incolor temperado 8 mm (69 × 22)',
     3*0.69*0.22*VIDRO8_M2 + VIDRACEIRO)
terc(A, 'Varanda · acabamento em tubinho champagne do armário superior',
     TUBINHO_CH, True)
fita(A, 'armário superior · bordas aparentes (sem fundo, os 4 lados aparecem)',
     2*(0.73+1.68)*2)
caixa('FR', A, 'armário inferior 90 × 80 × 50', 90, 80, 50, nvert=1, nprat=1,
      mat_int='BT')
add('FR', 18, A, 'armário inferior · porta 56 × 72', 56, 72)
fer(A, dobr=2); cava(A, 0.56)
fita(A, 'armário inferior · porta + boca do nicho 30 × 68',
     2*(0.56+0.72) + 2*(0.30+0.68))
terc(A, 'Puxador em mármore travertino 6×6 cm — 01 unidade', PUX_TRAVERTINO, True)
# bancada curva 300 × 40 × 5 — duas lâminas de 18 + bordas arredondadas
add('AR', 18, A, 'bancada curva 300 × 40 · lâmina (2 camadas, 2 peças cada)',
    150, 40, 4)
add('AR', 18, A, 'bancada curva · enchimento de borda', 150, 5, 4)
fita(A, 'bancada · borda arredondada (perímetro, 2 camadas)', 2*(3.00+0.40)*2)
terc(A, 'Varanda · pés chumbados em tubo champagne da bancada (2 un)',
     TUBO_CHAMP, True)
duv(A, 'a bancada da varanda é curva (R40/R46, arcos de 210,7 e 301,1). Adotei '
       '300 × 40 de projeção; o raio consome mais chapa e está na sensibilidade.')

# ───────────────────────────────────────────────────────────────────────────
# 5 · QUARTO RAFAEL E MIGUEL — pranchas 22 a 31 · pé-direito 280
#     Cama suspensa (mezanino) estruturada com METALON · guarda-corpo de CORDA
#     Escada em MDF Areal · armário existente ENVELOPADO em MDF Frapê
# ───────────────────────────────────────────────────────────────────────────
A = 'Quarto Rafael e Miguel'
# ── mezanino: estrado 203 × 150 + testeira + fundo do vão de acesso ───────
add('AR', 18, A, 'mezanino · estrado 203 × 150 (2 peças sobre metalon)', 150, 101.5, 2)
add('AR', 18, A, 'mezanino · testeira frontal 203 × 23', 203, 23)
add('AR', 18, A, 'mezanino · fechamento lateral do vão de acesso', 150, 23, 2)
add('AR', 18, A, 'mezanino · porta do vão de acesso 55 × 39', 55, 39)
fer(A, dobr=2)
terc(A, 'Mezanino · estrutura de metalon (serralheria sob medida)', SERRALH_MEZ, True)
terc(A, 'Mezanino · guarda-corpo de corda + ferragem de fixação', CORDA_GC, True)
led(A, 'mezanino · LED 4000K inferior', 2.03)
fita(A, 'mezanino · testeira e bordas do estrado', 2*(2.03+0.23) + 2*(2.03+1.50))
# ── escada MDF Areal — 9 degraus de 17, altura 170, largura 55/65 ─────────
add('AR', 18, A, 'escada · lateral 170 × 30', 170, 30, 2)
add('AR', 18, A, 'escada · degrau 55 × 30', 55, 30, 9)
add('AR', 18, A, 'escada · espelho do degrau 55 × 17', 55, 17, 9)
fita(A, 'escada · bordas de 9 degraus + 2 laterais', 9*0.55 + 2*(1.70+0.30))
# ── cama inferior 203 × 105 c/ 2 gavetões MDF Frapê ──────────────────────
add('AR', 18, A, 'cama inferior · estrado 203 × 105 (2 peças)', 203, 52.5, 2)
add('AR', 15, A, 'cama inferior · caixa lateral', 105, 32, 2)
add('AR', 15, A, 'cama inferior · caixa frente/fundo', 203, 32, 2)
add('FR', 18, A, 'cama inferior · frente de gavetão 93,5 × 32', 93.5, 32, 2)
gaveta('BT', A, 'cama inferior · gavetão', 93.5, 100, 27, 2)
fer(A, gav=2)
fita(A, 'cama inferior · frentes dos gavetões + bordas', 2*2*(0.935+0.32) + 2*2.03)
# ── 2 cabeceiras 146 × 35 c/ LED 3000K e 2 nichos 146 × 23 c/ suporte Frapê ─
add('AR', 18, A, 'cabeceira 146 × 35 c/ LED superior', 146, 35, 2)
add('AR', 18, A, 'nicho 146 × 23 · fundo e frente', 146, 23, 4)
add('AR', 15, A, 'nicho 146 × 23 · base e topo (prof 20)', 146, 20, 4)
add('FR', 18, A, 'nicho · suporte em MDF Frapê', 23, 20, 4)
led(A, 'cabeceiras · LED 3000K superior (2 un)', 2*1.46)
led(A, 'nichos · LED de leitura', 2*1.46)
fita(A, 'cabeceiras e nichos · bordas aparentes', 2*2*(1.46+0.35) + 4*(1.46+0.23))
# ── bancada/escrivaninha MDF Frapê 113 × 46 × 80 c/ 2 gavetas ────────────
caixa('FR', A, 'bancada 113 × 80 × 46', 113, 80, 46, nvert=0, nprat=0, mat_int='BT')
add('FR', 18, A, 'bancada · frente de gaveta 52 × 10', 52, 10, 2)
gaveta('BT', A, 'bancada · gaveta', 52, 46, 8, 2)
fer(A, gav=2); cava(A, 2*0.52)
fita(A, 'bancada · tampo e frentes', 2*(1.13+0.46) + 2*2*(0.52+0.10))
# ── armário MDF Frapê 104,5 × 170 × 40 — 4 portas + 2 gavetas + prateleira ─
caixa('FR', A, 'armário 104,5 × 170 × 40', 104.5, 170, 40, nvert=1, nprat=2,
      mat_int='BT')
add('FR', 18, A, 'armário · porta superior 52,3 × 90', 52.3, 90, 2)
add('FR', 18, A, 'armário · porta inferior 52,3 × 67', 52.3, 67, 2)
add('FR', 18, A, 'armário · frente de gaveta 52,3 × 10', 52.3, 10, 2)
gaveta('BT', A, 'armário · gaveta', 52.3, 40, 8, 2)
fer(A, dobr=8, gav=2); cava(A, 4*0.523)
fita(A, 'armário · 4 portas + 2 gavetas',
     2*2*(0.523+0.90) + 2*2*(0.523+0.67) + 2*2*(0.523+0.10))
# ── armário existente, ENVELOPAR em MDF Frapê — 204 × 280, 3 portas espelho ─
add('FR', 18, A, 'envelopamento · porta 68 × 266 c/ espelho prata colado', 68, 266, 3)
add('FR', 18, A, 'envelopamento · lateral aparente 60 × 280', 60, 140, 2)
add('FR', 18, A, 'envelopamento · testeira superior 204 × 14', 204, 14)
fer(A, dobr=9); cava(A, 3*0.68)
terc(A, 'Envelopamento · espelho prata colado nas 3 portas (68 × 266) — 3 folhas',
     3*ESPELHO_FL)
fita(A, 'envelopamento · 3 portas + laterais',
     3*2*(0.68+2.66) + 2*2*(0.60+2.80))
duv(A, 'o armário existente do quarto Rafael/Miguel será envelopado: as 3 portas '
       'de espelho são NOVAS, mas a caixaria interna é a que já está lá. Conferir '
       'no local se o corpo aceita a ferragem nova.')

# ───────────────────────────────────────────────────────────────────────────
# 6 · QUARTO MARIA LUÍSA — pranchas 32 a 37 · pé-direito 280 · parede 318,5
#     Cabeceira ESTOFADA em tecido facto branco (gomos), cortineiro em Frapê,
#     prateleiras de desenho ORGÂNICO em Areal, bancada/penteadeira em Frapê,
#     armário existente ENVELOPADO com portas de espelho.
# ───────────────────────────────────────────────────────────────────────────
A = 'Quarto Maria Luísa'
# ── fechamento do cortineiro MDF Frapê — 318,5 × 37 e 214,5 × 38 ─────────
add('FR', 18, A, 'cortineiro · frente 318,5 × 37 (2 peças)', 159.25, 37, 2)
add('FR', 18, A, 'cortineiro · frente 214,5 × 38', 214.5, 38)
add('FR', 15, A, 'cortineiro · fundo/apoio (prof 20)', 159.25, 20, 4)
led(A, 'cortineiro · LED 3000K inferior (2 paredes)', 3.185 + 2.145)
fita(A, 'cortineiro · borda inferior aparente', 3.185 + 2.145)
# ── painel e teto em MDF Areal (nicho da bancada) ────────────────────────
add('AR', 18, A, 'painel MDF Areal 60 × 266 (2 peças)', 60, 133, 2)
add('AR', 18, A, 'teto MDF Areal 169,5 × 60', 169.5, 60)
fita(A, 'painel e teto · bordas em ½ esquadria', 2*(0.60+2.66) + 2*(1.695+0.60))
# ── 3 prateleiras orgânicas, 5 cm de espessura (2 lâminas de 18) ─────────
add('AR', 18, A, 'prateleira orgânica 170 × 40 · lâmina (2 por prateleira)', 170, 40, 4)
add('AR', 18, A, 'prateleira orgânica 125 × 40 · lâmina (2 por prateleira)', 125, 40, 2)
add('AR', 18, A, 'prateleira orgânica · retorno de canto 60 × 40 (2 lâminas)', 60, 40, 6)
add('AR', 18, A, 'prateleira orgânica · enchimento de borda', 170, 5, 6)
led(A, 'prateleiras orgânicas · LED 3000K inferior', 2*1.70 + 1.25)
fita(A, 'prateleiras orgânicas · borda curva (perímetro, 3 peças)',
     3*2*(2.30+0.40))
# ── cabeceira ESTOFADA em gomos — 214,5 + 199,5 = 414 cm, altura 110 ─────
add('BT', 15, A, 'cabeceira estofada · base de MDF 214,5 × 110 (2 peças)',
    107.25, 110, 2)
add('BT', 15, A, 'cabeceira estofada · base de MDF 199,5 × 110 (2 peças)',
    99.75, 110, 2)
terc(A, 'Estofador · cabeceira em gomos, tecido facto branco — parede de 214,5',
     ESTOF_PAREDE)
terc(A, 'Estofador · cabeceira em gomos, tecido facto branco — parede de 199,5',
     ESTOF_PAREDE)
led(A, 'cabeceira estofada · LED 3000K superior', 4.14)
duv(A, 'a cabeceira estofada do quarto Maria Luísa tem 4,14 m em duas paredes, '
       'com vão posterior para persiana. A base da casa cota estofador POR PEÇA '
       '(cabeceira 650 · completo 1800) — lancei duas peças "completo".')
# ── bancada/penteadeira em L, 172 + 167,5, prof 50, altura 80 ───────────
caixa('FR', A, 'bancada em L 172 × 80 × 50 (trecho A)', 172, 80, 50, nvert=1,
      nprat=0, mat_int='BT')
caixa('FR', A, 'bancada em L 167,5 × 80 × 50 (trecho B)', 167.5, 80, 50, nvert=1,
      nprat=0, mat_int='BT')
add('FR', 18, A, 'bancada · frente de gavetão 75 × 42', 75, 42, 2)
add('FR', 18, A, 'bancada · frente de gaveta 49 × 20', 49, 20, 2)
add('FR', 18, A, 'bancada · báscula c/ espelho prata colado 49,5 × 45', 49.5, 45)
gaveta('BT', A, 'bancada · gavetão', 75, 50, 37, 2)
gaveta('BT', A, 'bancada · gaveta', 49, 50, 16, 2)
add('BT', 6, A, 'bancada · divisória interna (base do acrílico)', 49, 45, 2)
add('FR', 18, A, 'bancada · báscula do tampo c/ pistão a gás 50 × 42', 50, 42)
fer(A, gav=4, basc=2, dobr=2); cava(A, 2*0.75 + 2*0.49 + 0.50)
terc(A, 'Penteadeira · espelho prata colado na báscula (49,5 × 45) — 1 folha',
     ESPELHO_FL)
terc(A, 'Penteadeira · divisória interna em acrílico', ACRILICO, True)
led(A, 'penteadeira · LED 4000K do espelho', 1.00)
fita(A, 'bancada · frentes e tampo',
     2*2*(0.75+0.42) + 2*2*(0.49+0.20) + 2*(0.495+0.45) + 2*(1.72+0.50) + 2*(1.675+0.50))
# ── banco-armário 50 × 80 × 50 c/ assento estofado ──────────────────────
caixa('FR', A, 'banco-armário 50 × 80 × 50', 50, 80, 50, nprat=1, mat_int='BT')
add('FR', 18, A, 'banco-armário · frente de gaveta 49 × 42', 49, 42)
gaveta('BT', A, 'banco-armário · gaveta', 49, 50, 37, 1)
add('BT', 15, A, 'banco-armário · base do assento estofado', 50, 50)
fer(A, gav=1)
terc(A, 'Estofador · assento do banco em tecido facto branco (50 × 50)', ESTOF_CAB)
fita(A, 'banco-armário · frente e bordas', 2*(0.49+0.42) + 2*(0.50+0.80))
# ── armário existente, ENVELOPAR em MDF Frapê — elev. D 188,5 × 266 ─────
add('FR', 18, A, 'envelopamento · porta 62,8 × 266 c/ espelho prata colado',
    62.8, 266, 3)
add('FR', 18, A, 'envelopamento · testeira e montantes aparentes', 188.5, 14, 2)
fer(A, dobr=9); cava(A, 3*0.628)
terc(A, 'Envelopamento ML · espelho prata colado nas 3 portas — 3 folhas',
     3*ESPELHO_FL)
fita(A, 'envelopamento ML · 3 portas', 3*2*(0.628+2.66))
duv(A, 'na elevação D do quarto Maria Luísa o espelho aparece com 188,5 de vão '
       'e 266 de altura, mas a prancha não divide as folhas. Adotei 3 portas '
       'de 62,8 — mesma solução do quarto Rafael. Conferir no local.')

# ───────────────────────────────────────────────────────────────────────────
# 7 · BANHO SOCIAL — pranchas 38 a 40
#     Armário superior 140 × 120,5 × 15 c/ 3 portas de correr em espelho prata
#     Armário inferior 140 × 91 × 35 c/ báscula a gás e gavetões tulha
# ───────────────────────────────────────────────────────────────────────────
A = 'Banho social'
caixa('FR', A, 'armário superior 140 × 120,5 × 15', 140, 120.5, 15, nvert=2,
      nprat=12, mat_int='BT')
add('FR', 18, A, 'armário superior · porta de correr c/ espelho prata 46,7 × 117,5',
    46.7, 117.5, 3)
terc(A, 'Banho social · espelho prata colado nas 3 portas de correr — 3 folhas',
     3*ESPELHO_FL)
terc(A, 'Banho social · correr RO65 Rometal (3 portas) + trilho',
     3*RO65 + 2*TRILHO_RO65)
fita(A, 'armário superior · 3 portas + 12 prateleiras',
     3*2*(0.467+1.175) + 12*0.44)
caixa('FR', A, 'armário inferior 140 × 91 × 35', 140, 91, 35, nvert=2, nprat=0,
      mat_int='BT')
add('FR', 18, A, 'armário inferior · báscula c/ pistão a gás 50 × 28', 50, 28)
add('FR', 18, A, 'armário inferior · frente de gavetão tulha 45 × 56', 45, 56, 2)
add('FR', 18, A, 'armário inferior · frente de gavetão 50 × 20', 50, 20)
gaveta('BT', A, 'armário inferior · gavetão tulha', 45, 35, 51, 2)
gaveta('BT', A, 'armário inferior · gavetão', 50, 35, 15, 1)
fer(A, gav=3, basc=1); cava(A, 2*0.45 + 2*0.50)
fita(A, 'armário inferior · frentes', 2*2*(0.45+0.56) + 2*(0.50+0.20) + 2*(0.50+0.28))
duv(A, 'no banho social a bancada da cuba aparece em pedra na perspectiva — '
       'não entrou no escopo de marcenaria.')

# ───────────────────────────────────────────────────────────────────────────
# 8 · QUARTO CASAL — pranchas 41 a 46 · painel de 272,5 × 256
#     Cristaleira em MDF Areal c/ portas de vidro reflecta bronze
#     Cabeceira estofada em Tecido Bouclé Elba Cor Branco Bruma
#     PUXADOR TRAVERTINO 6×6 — 01 UNIDADE (mesa de cabeceira)
# ───────────────────────────────────────────────────────────────────────────
A = 'Quarto casal'
# ── painel MDF Areal 272,5 × 256, acima do rodapé ───────────────────────
add('AR', 18, A, 'painel da cabeceira 272,5 × 256 (4 peças)', 136.25, 128, 4)
fita(A, 'painel da cabeceira · perímetro em ½ esquadria', 2*(2.725+2.56))
# ── cabeceira estofada Bouclé Elba 177,5 ────────────────────────────────
add('BT', 15, A, 'cabeceira estofada · base de MDF 177,5 × 64', 177.5, 64)
terc(A, 'Estofador · cabeceira em Tecido Bouclé Elba Branco Bruma (177,5 × 64)',
     ESTOF_CAB)
# ── penteadeira MDF Frapê 52 × 50 prof × 80 ─────────────────────────────
caixa('FR', A, 'penteadeira 52 × 80 × 50', 52, 80, 50, nprat=0, mat_int='BT')
add('FR', 18, A, 'penteadeira · báscula c/ espelho prata colado 50 × 45', 50, 45)
add('FR', 18, A, 'penteadeira · frente de gaveta 50 × 20', 50, 20)
gaveta('BT', A, 'penteadeira · gaveta', 50, 50, 16, 1)
add('BT', 6, A, 'penteadeira · divisória interna (base do acrílico)', 50, 45)
add('FR', 18, A, 'penteadeira · báscula do tampo c/ pistão a gás 50 × 42', 50, 42)
fer(A, basc=2, gav=1, dobr=2); cava(A, 2*0.50)
terc(A, 'Penteadeira · espelho prata colado na báscula (50 × 45) — 1 folha',
     ESPELHO_FL)
terc(A, 'Penteadeira · divisória interna em acrílico', ACRILICO, True)
led(A, 'penteadeira · LED 4000K do espelho', 1.00)
fita(A, 'penteadeira · frentes e tampo', 2*(0.50+0.45) + 2*(0.50+0.20) + 2*(0.52+0.50))
# ── mesa de cabeceira MDF Frapê 45 × 50 × 42, 1 gaveta, puxador travertino ─
caixa('FR', A, 'mesa de cabeceira 45 × 42 × 50', 45, 42, 50, nprat=0, mat_int='BT')
add('FR', 18, A, 'mesa de cabeceira · frente de gaveta 44 × 35', 44, 35)
gaveta('BT', A, 'mesa de cabeceira · gaveta', 44, 50, 30, 1)
fer(A, gav=1)
terc(A, 'Puxador em mármore travertino 6×6 cm — 01 unidade (mesa de cabeceira)',
     PUX_TRAVERTINO, True)
fita(A, 'mesa de cabeceira · frente e tampo', 2*(0.44+0.35) + 2*(0.45+0.50))
# ── cristaleira MDF Areal 100,5 × 181 × 30 + armário inferior 100,5 × 85 ──
# ⚠ porta de VIDRO: interior aparece ⇒ caixaria em Areal, não em branco.
caixa('AR', A, 'cristaleira 100,5 × 181 × 30', 100.5, 181, 30, nprat=0,
      mat_int=None)
fer(A, dobr=4)
terc(A, 'Cristaleira · 2 portas de vidro reflecta bronze c/ alumínio bronze e '
        'puxador Sotille (50,3 × 178)',
     2*max(PT_VIDRO, 0.503*1.78*PT_VIDRO_M2))
terc(A, 'Cristaleira · 4 prateleiras de vidro incolor temperado 8 mm (96,5 × 28)',
     4*0.965*0.28*VIDRO8_M2 + VIDRACEIRO)
led(A, 'cristaleira · LED 3000K posterior das prateleiras', 4*0.965)
fita(A, 'cristaleira · bordas frontais', 2*(1.005+1.81))
caixa('FR', A, 'armário inferior da cristaleira 100,5 × 85 × 30', 100.5, 85, 30,
      nvert=1, nprat=0, mat_int='BT')
add('FR', 18, A, 'armário inferior · frente de gaveta 50,3 × 20', 50.3, 20, 8)
gaveta('BT', A, 'armário inferior · gaveta', 50.3, 30, 16, 8)
fer(A, gav=8); cava(A, 8*0.503)
fita(A, 'armário inferior · 8 frentes de gaveta', 8*2*(0.503+0.20))
# ── portas em MDF Areal (giro 97,5 × 242 e correr 59 × 242) ─────────────
add('AR', 18, A, 'porta de giro 97,5 × 242 c/ puxador cava', 97.5, 242)
add('AR', 18, A, 'porta de correr 59 × 242 c/ puxador cava', 59, 242)
fer(A, dobr=3); cava(A, 0.975 + 0.59)
terc(A, 'Quarto casal · sistema deslizante embutido, amortecido (porta 59)', RO82_TOP)
terc(A, 'Quarto casal · perfil de alumínio na base das 2 portas',
     (0.975+0.59)*PERF_ALU_M)
fita(A, 'portas · perímetro', 2*(0.975+2.42) + 2*(0.59+2.42))

# ───────────────────────────────────────────────────────────────────────────
# 9 · BANHO CASAL — pranchas 47 a 49
#     Armário superior 112 × 120,5 × 15 c/ 2 portas de correr em espelho prata
#     e iluminação FRONTAL em LED 4000K · armário inferior 112 × 91 × 51,5
# ───────────────────────────────────────────────────────────────────────────
A = 'Banho casal'
caixa('FR', A, 'armário superior 112 × 120,5 × 15', 112, 120.5, 15, nvert=0,
      nprat=4, mat_int='BT')
add('FR', 18, A, 'armário superior · porta de correr c/ espelho prata 46 × 117,5',
    46, 117.5, 2)
add('FR', 18, A, 'armário superior · montante fixo iluminado 10 × 120,5', 10, 120.5, 2)
terc(A, 'Banho casal · espelho prata colado nas 2 portas de correr — 2 folhas',
     2*ESPELHO_FL)
terc(A, 'Banho casal · correr RO65 Rometal (2 portas) + trilho',
     2*RO65 + TRILHO_RO65)
led(A, 'armário superior · iluminação frontal LED 4000K (2 montantes)', 2*1.205)
fita(A, 'armário superior · 2 portas + 4 prateleiras + montantes',
     2*2*(0.46+1.175) + 4*0.88 + 2*2*(0.10+1.205))
caixa('FR', A, 'armário inferior 112 × 91 × 51,5', 112, 91, 51.5, nvert=1,
      nprat=0, mat_int='BT')
add('FR', 18, A, 'armário inferior · báscula c/ pistão a gás 52 × 28', 52, 28)
add('FR', 18, A, 'armário inferior · frente de gavetão tulha 52 × 56', 52, 56)
add('FR', 18, A, 'armário inferior · frente de gavetão 60 × 56', 60, 56)
gaveta('BT', A, 'armário inferior · gavetão tulha', 52, 51.5, 51, 1)
gaveta('BT', A, 'armário inferior · gavetão', 60, 51.5, 51, 1)
fer(A, gav=2, basc=1); cava(A, 0.52 + 0.60)
fita(A, 'armário inferior · frentes',
     2*(0.52+0.56) + 2*(0.60+0.56) + 2*(0.52+0.28))
duv(A, 'as bancadas dos dois banheiros e do lavabo aparecem em pedra — fora do '
       'escopo de marcenaria, como no padrão da casa.')

# ═══════════════════════════════════════════════════════════════════════════
# RELATÓRIO
# ═══════════════════════════════════════════════════════════════════════════
W = 100

def rodar(especial=False):
    """Retorna o pacote de custo para um cenário de preço de chapa."""
    global ESPECIAL
    ESPECIAL = especial
    por_chapa, area_chapa = defaultdict(list), defaultdict(float)
    area_amb, area_rip_amb = defaultdict(float), defaultdict(float)
    for mat, esp, amb, desc, c, l, q, rip in P:
        for _ in range(q): por_chapa[(mat, esp)].append((c, l))
        a = c*l*q/10000
        area_chapa[(mat, esp)] += a
        area_amb[amb] += a
        if rip: area_rip_amb[amb] += a
    CHAPAS = {k: nest(v) for k, v in por_chapa.items()}
    custo_chapa = sum(n*prc(k[0], k[1]) for k, n in CHAPAS.items())
    return CHAPAS, area_chapa, area_amb, area_rip_amb, custo_chapa

# ── guarda de peça que não cabe na chapa ──────────────────────────────────
_fora = [(m, e, a, d, c, l) for m, e, a, d, c, l, q, r in P
         if max(c, l) > CH_C or min(c, l) > CH_L]
if _fora:
    print('\n' + '!'*W)
    print('PEÇAS QUE NÃO CABEM NA CHAPA DE 275 × 185 — corrigir antes de orçar')
    for m, e, a, d, c, l in _fora:
        print(f'  {NOME_MAT[m]} {e} mm · {a} · {d}: {c:.0f} × {l:.0f} cm')
    print('!'*W + '\n')

CHAPAS, area_chapa, area_amb, area_rip_amb, custo_chapa = rodar(False)
area_tot = sum(area_chapa.values()); tot_ch = sum(CHAPAS.values())

ordem = []
for _m, _e, amb, *_r in P:
    if amb not in ordem: ordem.append(amb)

print('═'*W)
print('CAROL E VINÍCIUS · CADERNO DE MARCENARIA — LEVANTAMENTO DE MATERIAL E CUSTO')
print('═'*W)
print('Projeto: Jéssica Sollero Design de Interiores · 20 de julho de 2026 · escala 1:25')
print('49 pranchas · 9 ambientes · texto em curvas (caso B) — geometria lida no vetor')

print('\nESCOPO POR AMBIENTE')
for amb in ordem:
    d, g, b = FER[amb]
    extra = []
    if d: extra.append(f'{d} dobr.')
    if g: extra.append(f'{g} gav.')
    if b: extra.append(f'{b} básc.')
    rip = f'  ·  ripado {area_rip_amb[amb]:.2f} m²' if area_rip_amb[amb] else ''
    print(f'  {amb:<26}{area_amb[amb]:>7.2f} m² de chapa   {" · ".join(extra):<26}{rip}')
print(f'  {"TOTAL":<26}{area_tot:>7.2f} m²')

print('\nPLANO DE CORTE  (nesting por cor × espessura — cores nunca dividem chapa)')
for k in sorted(CHAPAS, key=lambda k: (k[0], -k[1])):
    mat, esp = k; n = CHAPAS[k]; pr = prc(mat, esp); c = n*pr
    ap = area_chapa[k]/(n*CH_AREA)*100
    print(f'  {NOME_MAT[mat]+" "+str(esp)+" mm":<26}{area_chapa[k]:>7.2f} m²  →  {n:>2} ch. × '
          f'R$ {pr:>7,.2f} = R$ {c:>9,.2f}   aprov. {ap:>3.0f}%'.replace(',', '.'))
print(f'  {"TOTAL":<26}{area_tot:>7.2f} m²  →  {tot_ch:>2} chapas'
      f'{"":>21}R$ {custo_chapa:>9,.2f}   médio {area_tot/(tot_ch*CH_AREA)*100:.0f}%'.replace(',', '.'))

print('\nFITA DE BORDA E FILETAGEM  (+10% de desperdício na fita)')
m_fita = sum(m for _, _, m in FITA)
custo_fita  = m_fita*DESPERD*FITA_COR
custo_filet = m_fita*FILET_MAQ
_a = f'{custo_fita:,.2f}'.replace(',', '.'); _b = f'{custo_filet:,.2f}'.replace(',', '.')
print(f'  {"total de borda aparente":<52}{m_fita:>9.2f} m')
print(f'  {"material da fita (cor, R$ 3,00/m +10%)":<52}         R$ {_a:>10}')
print(f'  {"filetagem na coladeira (R$ 2,50/m)":<52}         R$ {_b:>10}')

print('\nUSINAGEM DE PUXADOR CAVA / CHANFRADO  (CNC, por metro de percurso)')
n_cava = sum(CAVA_M.values()); custo_cava = n_cava*CAVA_USIN
_v = f'{custo_cava:,.2f}'.replace(',', '.')
print(f'  {n_cava:.1f} m × R$ 25,00/m{"":>36}         R$ {_v:>10}')

print('\nILUMINAÇÃO EM LED  (fita R$ 28/m + perfil de alumínio R$ 38/m)')
m_led = sum(m for _, _, m in LED); custo_led = m_led*LED_M
for amb in ordem:
    ml = sum(m for a, _, m in LED if a == amb)
    if ml: print(f'  {amb:<52}{ml:>9.2f} m')
_v = f'{custo_led:,.2f}'.replace(',', '.')
print(f'  {"TOTAL":<52}{m_led:>9.2f} m      R$ {_v:>10}')

print('\nTERCEIRIZADOS E ITENS ESPECIAIS   (★ = sem preço na base, estimado)')
custo_terc = 0.0
for amb, d, v, est in TERC:
    custo_terc += v
    mk = '★' if est else ' '
    _v = f'{v:,.2f}'.replace(',', '.')
    print(f' {mk}{amb:<23}{d[:54]:<55}R$ {_v:>10}')
_v = f'{custo_terc:,.2f}'.replace(',', '.')
print(f'  {"TOTAL":<78}R$ {_v:>10}')

TOT_DOBR = sum(f[0] for f in FER.values())
TOT_GAV  = sum(f[1] for f in FER.values())
TOT_BASC = sum(f[2] for f in FER.values())
N_PRAT   = sum(q for m, e, a, d, c, l, q, r in P if 'prateleira' in d.lower())
custo_sup = N_PRAT*4*SUP_PRAT
print(f'\nFERRAGEM DO PROJETO — {TOT_DOBR} dobradiças · {TOT_GAV} gavetas · '
      f'{TOT_BASC} básculas · {N_PRAT} prateleiras de MDF')

# ── logística — montagem NÃO entra (salário fixo) ─────────────────────────
N_CARRETO, R_CARRETO = 5, 600.0
N_VISITA,  R_VISITA  = 3, 250.0
LOG = N_CARRETO*R_CARRETO + N_VISITA*R_VISITA

# ── fechamento ────────────────────────────────────────────────────────────
area_rip = sum(area_rip_amb.values()); frac_rip = area_rip/area_tot
consum = (custo_chapa + custo_fita)*0.06
MAT_FIXO = (custo_chapa + custo_fita + custo_filet + custo_cava + custo_led
            + custo_sup + custo_terc + consum)

def fechar(mcs, rt=True):
    out = []
    for (nome, fdesc, f, gar), mc in zip(CENARIOS, mcs):
        custo_ferr = TOT_DOBR*f['dobr'] + TOT_GAV*f['corr'] + TOT_BASC*f['art']
        CD = MAT_FIXO + custo_ferr + LOG
        cd_rip = (custo_chapa + custo_fita + custo_filet + consum + LOG)*frac_rip
        inv = preco(CD - cd_rip, cd_rip, mc, rt)
        inv_r = round(inv/100)*100
        out.append((nome, fdesc, mc, gar, custo_ferr, CD, inv_r,
                    mc_conferida(inv_r, CD)))
    return out

print('\n' + '═'*W)
print('CUSTO DIRETO E PREÇO')
print('═'*W)
print('\n  Composição do custo direto (igual nos três cenários, exceto a ferragem):')
for rot, v in (('Chapas', custo_chapa), ('Fita (material)', custo_fita),
               ('Filetagem (aplicação)', custo_filet),
               ('Usinagem das cavas e chanfros', custo_cava),
               ('Iluminação em LED (fita + perfil)', custo_led),
               ('Suportes de prateleira', custo_sup),
               ('Terceirizados e itens especiais', custo_terc),
               ('Consumíveis (6% de chapa + fita)', consum),
               (f'Logística — {N_CARRETO} carretos + {N_VISITA} visitas técnicas '
                f'(montagem NÃO entra: é custo fixo)', LOG)):
    _v = f'{v:,.2f}'.replace(',', '.')
    print(f'    {rot:<78}R$ {_v:>10}')

RES = {}
for rot, rt in (('COM RT de 10% — configuração entregue', True),
                ('sem RT (referência interna)', False)):
    RES[rot] = fechar(MCS, rt)
    print(f'\n  {rot}')
    print(f'  {"":<17}{"MC":>6}{"ferragem":>11}{"custo direto":>14}'
          f'{"INVESTIMENTO":>15}{"MC real":>9}{"garantia":>11}')
    for nome, fd, mc, gar, cf, cd, inv, mcr in RES[rot]:
        print(f'  {nome:<17}{mc*100:>5.0f}%{cf:>11,.0f}{cd:>14,.0f}{inv:>15,.0f}'
              f'{mcr*100:>8.1f}%{gar:>11}'.replace(',', '.'))

PRINC = 'COM RT de 10% — configuração entregue'
_v = f'{(custo_chapa + custo_fita + custo_filet + consum + LOG)*frac_rip:,.0f}'.replace(',', '.')
print(f'\n  Ripado = {area_rip:.2f} m² de chapa ({frac_rip*100:.0f}% do projeto) ⇒ '
      f'R$ {_v} de custo direto, à parte, a MC {MC_RIPADO*100:.0f}%.')
print('  (lavabo, painel da TV da sala de estar e as frentes do armário superior.)')

print('\n' + '─'*W)
print('INVESTIMENTO POR AMBIENTE — escada principal ' + PRINC)
print(f'  {"ambiente":<26}{"chapa":>8}{"I · Telesc.":>14}{"II · Hardt":>13}{"III · Hettich":>15}')
TOTS = [0, 0, 0]
linhas = []
for amb in ordem:
    fr = area_amb[amb]/area_tot
    vals = [round(RES[PRINC][i][6]*fr/100)*100 for i in range(3)]
    linhas.append((amb, area_amb[amb], vals))
    for i in range(3): TOTS[i] += vals[i]
# ajuste de arredondamento no maior ambiente
maior = max(range(len(linhas)), key=lambda i: linhas[i][1])
for i in range(3):
    linhas[maior][2][i] += RES[PRINC][i][6] - TOTS[i]
for amb, ar, vals in linhas:
    cols = ''.join(f'{v:>14,.0f}'.replace(',', '.') for v in vals)
    print(f'  {amb:<26}{ar:>8.2f}{cols}')
cols = ''.join(f'{RES[PRINC][i][6]:>14,.0f}'.replace(',', '.') for i in range(3))
print(f'  {"TOTAL":<26}{area_tot:>8.2f}{cols}')

print('\n' + '─'*W)
print('SENSIBILIDADE')
CH_E, AC_E, _, _, custo_chapa_esp = rodar(True)
rodar(False)
d_esp = custo_chapa_esp - custo_chapa
inv2 = RES[PRINC][1][6]
_a = f'{d_esp:,.0f}'.replace(',', '.')
_b = f'{d_esp/div(MCS[1], COM_RT):,.0f}'.replace(',', '.')
print(f'  1. Areal e Frapê cotadas como chapa ESPECIAL (950/1200/800) em vez de')
print(f'     COR (500/600/300): +R$ {_a} de custo ⇒ +R$ {_b} de preço (cenário II).')
print(f'     ⚠ É A MAIOR INCERTEZA DO ORÇAMENTO. Confirmar a linha com a Arauco.')
area_bt = sum(a for k, a in area_chapa.items() if k[0] == 'BT')
_d = ((500-260)*CHAPAS.get(('BT', 15), 0) + (600-330)*CHAPAS.get(('BT', 18), 0)
      + (300-190)*CHAPAS.get(('BT', 6), 0))
_v = f'{_d:,.0f}'.replace(',', '.')
print(f'  2. O interno já está em Branco TX ({area_bt:.1f} m²), como manda a prancha —')
print(f'     se a arquiteta pedir interno na cor, some ~R$ {_v} de chapa.')
print(f'  3. "SEGUIR VEIOS NOS ENCONTROS" trava a rotação das peças amadeiradas no')
print(f'     nesting. O plano acima gira peça livremente; com veio travado o')
print(f'     aproveitamento cai ~8 pontos ⇒ ~{math.ceil(tot_ch*0.09)} chapas a mais.')
est_terc = sum(v for _, _, v, e in TERC if e)
_v = f'{est_terc:,.0f}'.replace(',', '.')
print(f'  4. Terceirizados SEM preço na base (★): R$ {_v} — metalon do mezanino,')
print(f'     guarda-corpo de corda, tubo champagne, puxadores de travertino e acrílico.')

print('\n' + '─'*W)
print('O QUE O RT CUSTA  (10% para a Jéssica Sollero, dentro do preço)')
for i, (nome, fd, mc, gar, cf, cd, inv, mcr) in enumerate(RES[PRINC]):
    sem = RES['sem RT (referência interna)'][i][6]
    print(f'  {nome:<17}sem RT R$ {sem:>9,.0f}  →  com RT R$ {inv:>9,.0f}   '
          f'(+{(inv/sem-1)*100:.0f}%)  ·  RT ≈ R$ {inv*0.10:>8,.0f}'.replace(',', '.'))

print('\n' + '─'*W)
print('SANIDADE — R$/m² de chapa  (faixa da casa: 626 Rizzi · 647 · 739 SPE · 834 Honda)')
for rot in RES:
    print(f'  {rot:<42}' + '  '.join(f'{RES[rot][i][6]/area_tot:>6.0f}' for i in range(3)))

print('\n' + '─'*W)
print(f'DÚVIDAS PARA A ARQUITETA / PARA CONFERIR NO LOCAL — {len(DUVIDAS)} itens')
for i, (amb, t) in enumerate(DUVIDAS, 1):
    print(f'  {i:>2}. [{amb}] {t}')
print('═'*W)
