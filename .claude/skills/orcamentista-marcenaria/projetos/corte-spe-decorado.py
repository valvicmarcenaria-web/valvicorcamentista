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

# ══ RATEIO POR AMBIENTE [Jonathan 07/08: sem RT · MC 35%] ═════════════════
GRUPO = {C1:'Cozinha', C2:'Cozinha', C3:'Cozinha', S1:'Sala', S2:'Sala',
         Q1:'Quarto', Q2:'Quarto', Q3:'Quarto', U1:'Suíte', U2:'Suíte',
         U3:'Suíte', U4:'Suíte'}
AMB = ('Cozinha', 'Sala', 'Quarto', 'Suíte')

ar_g = defaultdict(lambda: defaultdict(float))
for mov, mat, d, c, l, q in p:
    ar_g[GRUPO[mov]][mat] += c*l/10000*q

# chapa rateada por área dentro de cada material (materiais compartilhados)
ch_g = dict.fromkeys(AMB, 0.0)
for m in CH:
    tot_m = sum(ar_g[g][m] for g in AMB)
    if not tot_m: continue
    for g in AMB: ch_g[g] += CH[m]*PRECO[m]*ar_g[g][m]/tot_m

# fita e filetagem seguem a área
ar_g_tot = {g: sum(ar_g[g].values()) for g in AMB}
ft_g = {g: custo_fita*ar_g_tot[g]/ar_tot for g in AMB}
fl_g = {g: custo_filet*ar_g_tot[g]/ar_tot for g in AMB}

# terceirizados e ferragens: atribuição EXATA
te_g = {'Cozinha': INOX_ML*0.45*INOX_M,
        'Sala':    ESP_M2*ESPELHO_M2 + INOX_ML*0.55*INOX_M,
        'Quarto':  LACA_M2_Q*LACA_M2 + (1.96*0.87)*ESTOFADO_M2 + (3.0+1.5)*LED_ML,
        'Suíte':   (1.935*1.00)*ESTOFADO_M2 + (2.97+2.46)*LED_ML}
fe_g = {'Cozinha': N_DOBR*DOBR + N_ARTIC*ARTIC + N_CORR*CORR + M_CAVA*CAVA_M + 10*SUP_PRAT,
        'Sala':    6*SUP_PRAT,
        'Quarto':  DESLIZ_2P + 4*SUP_PRAT,
        'Suíte':   2*DESLIZ_2P + 2*SUP_PRAT}
# reconcilia arredondamentos com o total apurado
te_g['Sala']   += custo_terc - sum(te_g.values())
fe_g['Cozinha'] += custo_ferr - sum(fe_g.values())

sub_g = {g: ch_g[g]+ft_g[g]+fl_g[g]+te_g[g]+fe_g[g] for g in AMB}
S = sum(sub_g.values())
fr_g = {g: sub_g[g] + (ch_g[g]+ft_g[g])*0.06 + (LOG+VIS+INST)*sub_g[g]/S for g in AMB}

print('\n' + '═'*94)
print('CUSTO DIRETO POR AMBIENTE')
print('═'*94)
print(f'  {"":<10}{"área":>9}{"chapa":>11}{"fita+filet":>12}{"terceiros":>11}{"ferragem":>10}{"CUSTO":>12}')
for g in AMB:
    print(f'  {g:<10}{ar_g_tot[g]:>7.1f} m²{ch_g[g]:>11,.0f}{ft_g[g]+fl_g[g]:>12,.0f}'
          f'{te_g[g]:>11,.0f}{fe_g[g]:>10,.0f}{fr_g[g]:>12,.2f}')
print(f'  {"TOTAL":<10}{ar_tot:>7.1f} m²{sum(ch_g.values()):>11,.0f}'
      f'{sum(ft_g.values())+sum(fl_g.values()):>12,.0f}{sum(te_g.values()):>11,.0f}'
      f'{sum(fe_g.values()):>10,.0f}{sum(fr_g.values()):>12,.2f}')

# ── preço: SEM RT · MC 35% ────────────────────────────────────────────────
a_, liqF_, b_, MC = 0.162, 0.88, 0.043, 0.35
div = 1 - a_ - liqF_*b_ - MC
print('\n' + '═'*94)
print(f'PREÇO DO DECORADO — MC {MC*100:.0f}% · SEM RT · divisor {div:.5f}')
print('═'*94)
pr = {g: round(fr_g[g]/div/100)*100 for g in AMB}
for g in AMB:
    print(f'  {g:<12}R$ {fr_g[g]:>9,.2f}  ÷ {div:.5f}  =  R$ {pr[g]:>8,.0f}')
DEC = sum(pr.values()); FX = sum(fr_g.values())
print(f'  {"DECORADO":<12}R$ {FX:>9,.2f}                    R$ {DEC:>8,.0f}')
print(f'  MC conferida: {(DEC - DEC*(a_+liqF_*b_) - FX)/DEC*100:.1f}%')

VIGENTE = 88200
print('\n' + '═'*94)
print('PROPOSTA ATUALIZADA')
print('═'*94)
print(f'  {"Stand — MOB 01 + MOB 02 (inalterado)":<52}R$ {VIGENTE:>8,.0f}')
print(f'  {"Decorado — MO 03 + DET 05 + DET 06":<52}R$ {DEC:>8,.0f}')
print(f'  {"TOTAL":<52}R$ {VIGENTE+DEC:>8,.0f}')
print('\n  ESCADA (padrão da casa, sobre o total)')
for d, rot in ((0.00,'Entrada 30% + até 10x no cartao'), (0.03,'Entrada 50% + até 8x no cartao'),
               (0.05,'Entrada 70% + até 6x no cartao'), (0.07,'Entrada 70% + transferencia')):
    v = round((VIGENTE+DEC)*(1-d)/100)*100
    print(f'    {rot:<44}{"—" if not d else f"−{d*100:.0f}%":>5}   R$ {v:>9,.0f}')
print(f'\n  ⚠ O stand fechou a MC 40%; o decorado sai a 35%. A MC combinada do')
print(f'    contrato fica em ~{(0.40*VIGENTE + MC*DEC)/(VIGENTE+DEC)*100:.1f}%.')
