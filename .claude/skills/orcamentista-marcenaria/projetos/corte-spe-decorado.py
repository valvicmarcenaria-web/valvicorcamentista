# -*- coding: utf-8 -*-
"""SPE NOVA LIMA 1 — APARTAMENTO DECORADO  [Jonathan 07/08/2026]

Três pranchas EXECUTIVAS novas do Lodi Motta (R00, emissão 05–06/08/2026):
  MO 03  · Mobiliário Sala / Cozinha  (A2 79,3×42)  — 4 elevações + 2 plantas
  DET 05 · Quarto                     (A2 59,4×42)  — 4 elevações + planta
  DET 06 · Suíte                      (A2 59,4×42)  — 3 elevações + planta

⚠️ ESCOPO NOVO. A proposta vigente (R$ 88.200) cobre MOB 01 + MOB 02 —
   painéis, pérgola e móveis das ÁREAS COMERCIAIS do stand. Estas pranchas são
   o APARTAMENTO DECORADO: cozinha, sala, quarto e suíte. Não há sobreposição.

ACABAMENTOS (legenda das pranchas)
  Sala/Cozinha e Suíte .... MDF Arauco ANIS MATT  +  MDF Arauco FRAPÉ MATT
  Quarto .................. MDF CILIEGIO PORO  +  laca brilhante Sayerlack M072
  Rodapé sala/cozinha ..... perfil de INOX escovado 5×0,5, h=5 (DET.02)
  Rodapé quarto/suíte ..... h=7
  Puxador cozinha ......... perfil embutido 1,5+1,5, prof. 8 (DET.03) = cava
"""
from collections import defaultdict

CH_C, CH_L = 275.0, 185.0
CH_AREA = 2.75*1.85

# ── custos ────────────────────────────────────────────────────────────────
# ⚠ Arauco linha MATT é premium. A base "cor" (500/580) é o piso; ver FLAG 1.
BR6, BR15, BR18 = 190.0, 250.0, 290.0
COR15, COR18    = 500.0, 580.0
PRECO = {'BR6':BR6, 'BR15':BR15, 'BR18':BR18,
         'AN15':COR15, 'AN18':COR18,   # Anis Matt
         'FR15':COR15, 'FR18':COR18,   # Frapé Matt
         'CI15':COR15, 'CI18':COR18}   # Ciliegio Poro
FITA_BR, FITA_COR, FILET = 2.0, 3.0, 2.50

DOBR, CORR, ARTIC   = 10.0, 70.0, 150.0
CAVA_M, SUP_PRAT    = 50.0, 1.50
DESLIZ_2P           = 250.0   # sistema de correr 2 portas (base: "Sistema roupeiro")
ESPELHO_M2          = 285.0   # espelho prata com perfil
LACA_M2             = 300.0   # material de pintura/laca — terceiro
INOX_M              = 52.0    # rodapé perfil inox escovado h=5
LED_ML              = 130.0   # fita + perfil com difusor
ESTOFADO_M2         = 450.0   # cabeceira estofada — terceiro (estofador)

p = []
def a(mov, mat, desc, c, l, q=1): p.append((mov, mat, desc, c, l, q))

# ══ MO 03 · COZINHA ═══════════════════════════════════════════════════════
# E01 inferiores 67+65+64+160 = 356 × 94 · E02 inferiores ~235 × 94 (forno + 3 gav)
C1 = 'Cozinha · bancada inferior'
a(C1,'BR15','Vertical',                 94, 60, 9)
a(C1,'BR15','Base',                    275, 60, 2)
a(C1,'BR15','Travessa superior',       275, 10, 4)
a(C1,'BR6', 'Fundo',                   275, 94, 3)
a(C1,'AN18','Frente — porta de giro',   67, 94, 2)
a(C1,'AN18','Frente — porta de giro',   65, 94, 1)
a(C1,'AN18','Frente — porta de giro',   64, 94, 1)
a(C1,'AN18','Frente — porta (vão 160)', 80, 94, 2)
a(C1,'AN18','Frente — gaveta (torre do forno)', 120, 31, 3)
a(C1,'BR15','Gaveta — lateral',         55, 18, 6)
a(C1,'BR15','Gaveta — travessa',       116, 18, 6)
a(C1,'BR6', 'Gaveta — fundo',          116, 55, 3)

C2 = 'Cozinha · aéreos'
# E01 prof 62: 66+64,5+64,5+73+35 = 303 × 66 · prof 40: h 39/40
a(C2,'BR15','Vertical (prof. 62)',      66, 62, 6)
a(C2,'BR15','Tampo/base (prof. 62)',   275, 62, 2)
a(C2,'AN18','Porta (prof. 62)',         66, 66, 2)
a(C2,'AN18','Porta (prof. 62)',       64.5, 66, 2)
a(C2,'AN18','Porta (prof. 62)',         73, 66, 1)
# E02 prof 40, duas fileiras de 40: 35+59+59+78+73 = 304
a(C2,'BR15','Vertical (prof. 40)',      80, 40, 6)
a(C2,'BR15','Tampo/base/divisória (prof. 40)', 275, 40, 3)
a(C2,'FR18','Frente — báscula',         59, 40, 4)
a(C2,'FR18','Frente — báscula',         78, 40, 2)
a(C2,'FR18','Frente — báscula',         73, 40, 2)
a(C2,'FR18','Frente — nicho do microondas (testeira)', 73, 10, 1)
a(C2,'BR6', 'Fundo dos aéreos',        275, 80, 2)

C3 = 'Cozinha · torre e painel alto (E02)'
# painel Anis 70+83+82,5 = 235,5 × 255, com nichos 55/30/10/30/10/30 + 88
a(C3,'AN15','Painel — face',           255, 78.5, 3)
a(C3,'AN18','Nicho — prateleira',       70, 30, 3)
a(C3,'AN18','Nicho — lateral',          55, 30, 2)
a(C3,'BR15','Estrutura interna do painel', 255, 20, 3)

# ══ MO 03 · SALA (painéis E03 e E04) ══════════════════════════════════════
S1 = 'Sala · painel com espelhos (E03)'
a(S1,'AN15','Painel — face',           255, 97.5, 2)
a(S1,'AN18','Moldura dos nichos de espelho', 39, 8, 8)
a(S1,'AN18','Nicho horizontal — moldura', 195, 8, 2)
a(S1,'BR15','Estrutura interna',       255, 20, 4)

S2 = 'Sala · painel com nichos e porta (E04)'
a(S2,'AN15','Painel — face',           255, 118.5, 1)
a(S2,'AN15','Painel — face (porta)',   255, 132, 1)
a(S2,'AN15','Módulo de nichos — face',  255, 85, 1)
a(S2,'AN18','Nicho — prateleira',       85, 35, 3)
a(S2,'AN18','Nicho — lateral',          30, 35, 6)
a(S2,'BR15','Estrutura interna',       255, 20, 3)

# ══ DET 05 · QUARTO ═══════════════════════════════════════════════════════
Q1 = 'Quarto · roupeiro'
a(Q1,'BR15','Vertical',                255, 55, 4)
a(Q1,'BR15','Tampo/base',              154, 55, 2)
a(Q1,'BR15','Prateleira',              150, 53, 4)
a(Q1,'BR6', 'Fundo',                   255, 154, 1)
a(Q1,'CI18','Porta de correr',          77, 255, 2)
a(Q1,'CI18','Tamponamento lateral',    255, 55, 1)

Q2 = 'Quarto · módulo de nichos em laca (E01)'
a(Q2,'BR15','Vertical',                255, 40, 2)
a(Q2,'BR15','Prateleira do nicho',      58, 38, 4)
a(Q2,'CI18','Face frontal',            255, 62, 1)

Q3 = 'Quarto · cabeceira, painel de TV e bancada'
a(Q3,'CI15','Cabeceira — base (estofada por cima)', 196, 87, 1)
a(Q3,'CI15','Painel de TV',            155, 92, 1)
a(Q3,'CI18','Prateleira suspensa',     155, 22, 1)
a(Q3,'CI15','Bancada — tampo',         144, 50, 1)
a(Q3,'CI15','Bancada — apoio lateral',  75, 50, 2)
a(Q3,'CI15','Criado suspenso',          75, 40, 1)
a(Q3,'CI15','Cortineiro',              297, 15, 1)

# ══ DET 06 · SUÍTE ════════════════════════════════════════════════════════
U1 = 'Suíte · torre de nichos (E01)'
a(U1,'BR15','Vertical',                255, 35, 2)
a(U1,'FR18','Prateleira do nicho',     100, 35, 6)
a(U1,'FR15','Face frontal / laterais', 255, 50, 2)
a(U1,'BR6', 'Fundo',                   255, 100, 1)

U2 = 'Suíte · roupeiro (E02)'
a(U2,'BR15','Vertical',                255, 55, 4)
a(U2,'BR15','Tampo/base',              193.5, 55, 2)
a(U2,'BR15','Prateleira',              190, 53, 4)
a(U2,'BR6', 'Fundo',                   255, 193.5, 1)
a(U2,'AN18','Porta de correr',          97, 255, 2)

U3 = 'Suíte · painel ripado (E03)'
N_RIPA_S = 24                       # sequência 20/3/5/5/10/5/5/5 repetida em ~245 cm
a(U3,'AN15','Base do painel',          255, 245, 1)
a(U3,'AN18','Ripa — perfil 5×1,5',     255, 5, N_RIPA_S)

U4 = 'Suíte · cabeceira e cortineiro'
a(U4,'AN15','Cabeceira — base (estofada por cima)', 193.5, 100, 1)
a(U4,'AN15','Cortineiro',              246, 15, 1)

# ── nesting ───────────────────────────────────────────────────────────────
def _pack(pcs):
    ch = 0; y = x = f = 0.0
    for c, l in pcs:
        if c > CH_C and l <= CH_C: c, l = l, c
        if c > CH_C or l > CH_L: ch += 1; continue
        if x + c > CH_C: y += f; x = 0.0; f = 0.0
        if y + l > CH_L: ch += 1; y = x = f = 0.0
        x += c; f = max(f, l)
    return ch + 1
def nest(items):
    if not items: return 0
    base = [(max(c, l), min(c, l)) for c, l in items]
    ords = [lambda q: -q[1], lambda q: (-q[1], -q[0]), lambda q: -q[0], lambda q: -q[0]*q[1]]
    ch = min(_pack(sorted(base, key=k)) for k in ords)
    ar = sum(c*l for c, l in items)/10000
    return max(ch, -(-int(ar/(CH_AREA*0.80)*1000)//1000) or 1)

por, area, area_mov = defaultdict(list), defaultdict(float), defaultdict(float)
for mov, mat, d, c, l, q in p:
    for _ in range(q):
        por[mat].append((c, l)); area[mat] += c*l/10000; area_mov[mov] += c*l/10000
CH = {m: nest(v) for m, v in por.items()}

print('═'*94)
print('SPE NOVA LIMA 1 — APARTAMENTO DECORADO · MO 03 + DET 05 + DET 06')
print('═'*94)
print('\nÁREA DE CHAPA POR MÓVEL')
for mov in dict.fromkeys(x[0] for x in p):
    print(f'  {mov:<48}{area_mov[mov]:>7.2f} m²')

print('\nPLANO DE CORTE — nesting por cor × espessura')
NOME = {'BR6':'branco 6','BR15':'branco 15','BR18':'branco 18','AN15':'Anis 15','AN18':'Anis 18',
        'FR15':'Frapé 15','FR18':'Frapé 18','CI15':'Ciliegio 15','CI18':'Ciliegio 18'}
custo_chapa = 0.0
for m in sorted(CH, key=lambda k: (k[:2], k)):
    n = CH[m]; c = n*PRECO[m]; custo_chapa += c
    print(f'  {NOME[m]:<12}{area[m]:>6.2f} m²  →  {n:>2} chapa(s) × R$ {PRECO[m]:>6.2f} = '
          f'R$ {c:>9,.2f}   aprov. {area[m]/(n*CH_AREA)*100:>3.0f}%')
tot_ch, ar_tot = sum(CH.values()), sum(area.values())
print(f'  {"TOTAL":<12}{ar_tot:>6.2f} m²  →  {tot_ch:>2} chapas'
      f'                     R$ {custo_chapa:>9,.2f}   médio {ar_tot/(tot_ch*CH_AREA)*100:.0f}%')

# ── fita, terceiros e ferragens ───────────────────────────────────────────
m_fita = ar_tot*2.6                       # fator da casa p/ painelaria + caixaria
custo_fita  = m_fita*1.10*((FITA_COR+FITA_BR)/2)
custo_filet = m_fita*FILET

ESP_M2  = (1.90*2.40) + 4*(0.39*0.50)     # espelho grande E03 + 4 nichos
LACA_M2_Q = 2*(2.55*0.62)                 # módulo de nichos do quarto, laca brilhante
ESTOF_M2 = (1.96*0.87) + (1.935*1.00)     # cabeceiras do quarto e da suíte
INOX_ML = 7.2 + 3.4                        # rodapé inox sala/cozinha (E03+E04)
LED_ML_T = 3.0 + 2.97 + 2.46 + 1.5         # cortineiros e nichos iluminados
N_DOBR  = 2*2 + 1*2 + 1*2 + 2*2 + 5*2      # portas de giro da cozinha
N_ARTIC = 8                                # básculas dos aéreos Frapé
N_CORR  = 3                                # gavetas da torre do forno
M_CAVA  = 3.56 + 2.35 + 3.04               # frentes com cava (DET.03)

terc = [
    (f'Espelho prata com perfil — {ESP_M2:.2f} m²',        ESP_M2*ESPELHO_M2),
    (f'Laca brilhante Sayerlack M072 — {LACA_M2_Q:.2f} m²', LACA_M2_Q*LACA_M2),
    (f'Cabeceiras estofadas — {ESTOF_M2:.2f} m²',           ESTOF_M2*ESTOFADO_M2),
    (f'Rodapé em perfil de inox escovado — {INOX_ML:.1f} m', INOX_ML*INOX_M),
    (f'Fita de LED com perfil — {LED_ML_T:.1f} m',          LED_ML_T*LED_ML),
]
ferr = [
    (f'Dobradiça com amortecimento — {N_DOBR} un',      N_DOBR*DOBR),
    (f'Articulador de báscula — {N_ARTIC} un',          N_ARTIC*ARTIC),
    (f'Corrediça oculta — {N_CORR} pares',              N_CORR*CORR),
    ('Sistema de correr — 3 conjuntos de 2 portas',     3*DESLIZ_2P),
    (f'Cava usinada — {M_CAVA:.2f} m',                  M_CAVA*CAVA_M),
    ('Suportes de prateleira — 22 un',                  22*SUP_PRAT),
]
custo_terc = sum(v for _, v in terc)
custo_ferr = sum(v for _, v in ferr)

print(f'\nFITA E FILETAGEM  ({m_fita:.0f} m estimados pelo fator 2,6 m/m²)')
print(f'  material R$ {custo_fita:,.2f}   ·   filetagem R$ {custo_filet:,.2f}')
print('\nTERCEIRIZADOS')
for d, v in terc: print(f'  {d:<56}R$ {v:>9,.2f}')
print(f'  {"TOTAL":<56}R$ {custo_terc:>9,.2f}')
print('\nFERRAGENS')
for d, v in ferr: print(f'  {d:<56}R$ {v:>9,.2f}')
print(f'  {"TOTAL":<56}R$ {custo_ferr:>9,.2f}')

consum = (custo_chapa + custo_fita)*0.06
MAT = custo_chapa + custo_fita + custo_filet + custo_terc + custo_ferr + consum
LOG, VIS, INST = 1600.0, 750.0, 6500.0    # 4 ambientes, obra em Nova Lima
fixedR = MAT + LOG + VIS + INST

print('\n' + '─'*94)
for d, v in (('Chapas', custo_chapa), ('Fita (material)', custo_fita), ('Filetagem', custo_filet),
             ('Terceirizados', custo_terc), ('Ferragens e usinagem', custo_ferr),
             ('Consumíveis (6%)', consum), ('Logística · 3 visitas · instalação', LOG+VIS+INST)):
    print(f'  {d:<56}R$ {v:>9,.2f}')
print(f'  {"CUSTO DIRETO — DECORADO":<56}R$ {fixedR:>9,.2f}')

# ── preço ─────────────────────────────────────────────────────────────────
a_, liqF_, b_ = 0.162, 0.88, 0.043
print('\n' + '═'*94)
print('PREÇO DO DECORADO — os parâmetros do SPE continuam abertos')
print('═'*94)
print(f'  {"MC":<6}{"SEM RT":>16}{"COM RT (10% do líquido)":>30}')
for MC in (0.35, 0.37, 0.40):
    d0 = 1 - a_ - liqF_*b_ - MC
    d1 = 1 - a_ - liqF_*b_ - liqF_*0.10 - MC
    print(f'  {MC*100:>4.0f}%  R$ {round(fixedR/d0/100)*100:>13,.0f}   R$ {round(fixedR/d1/100)*100:>24,.0f}')

VIGENTE = 88200
d40 = 1 - a_ - liqF_*b_ - 0.40
dec40 = round(fixedR/d40/100)*100
print(f'\n  PROPOSTA VIGENTE (MOB 01 + MOB 02, MC 40% sem RT) ....... R$ {VIGENTE:>8,.0f}')
print(f'  DECORADO (MO 03 + DET 05 + DET 06, MC 40% sem RT) ....... R$ {dec40:>8,.0f}')
print(f'  {"TOTAL ATUALIZADO":<55}R$ {VIGENTE+dec40:>8,.0f}')

print('\n' + '─'*94)
print('⚠ FLAGS — as três primeiras vêm do dossiê e continuam abertas')
print('  1. Preço da chapa Arauco MATT — usei a base "cor" (R$ 500/580). A linha Matt é')
print(f'     premium; a R$ 800/chapa o custo sobe ~R$ {tot_ch*250:,.0f} e o preço ~R$ '
      f'{round(tot_ch*250/d40/100)*100:,.0f}.')
print('  2. RT — projeto do escritório Lodi Motta. Tem RT? Muda ~24% do preço.')
print('  3. MC — a vigente fechou em 40% sem RT.')
print('  4. Interno branco assumido; as pranchas só especificam o acabamento aparente.')
print('  5. Fita estimada pelo fator 2,6 m/m² — não apurada peça a peça.')
print('  6. Divisão interna dos módulos lida das elevações; as plantas cotam o')
print('     desenvolvimento, não a divisão de gavetas.')
print('  7. Caixa de gypsum, pintura, cortina e tapetes: fora do escopo Valvic.')
