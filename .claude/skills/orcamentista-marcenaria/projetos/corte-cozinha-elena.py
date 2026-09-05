# -*- coding: utf-8 -*-
"""COZINHA — consultoria Rizzi Interiores ("Casa Sil" / RI-CONSUL...ELENA).

⚠ FONTE É CONSULTORIA, NÃO EXECUTIVO. O próprio documento diz:
   "Todas as medidas especificadas neste documento foram tiradas de planta baixa
    ou medidas básicas in loco, NÃO SERVINDO COMO REFERÊNCIA PARA COMPRA FINAL...
    na consultoria não tem detalhamentos, ou seja, medidas detalhadas do espaço,
    layout e Planejados."
   Mesmo caso do Kairon & Juliana: estimar por envelope + render, sinalizar o
   que precisa de conferência.

COERÊNCIA DAS COTAS (confere — o documento fecha sozinho)
   bancada 77 + sóculo recuado 10 + granito 3 = 90 ✓ ("instalada a 90cm do piso")
   90 + nicho freijó 110 + aéreo azul 70      = 270 = torre quente ✓
   parede 2: bancada B 150 + torre 70 + geladeira 80 = 300 ✓ (planta: 300)
   parede 1: bancada A 272 + retorno 60 = 332 ✓ (planta: 332) · janela nos 122 restantes

TRÊS CORES + BRANCO INTERNO
   Azul Ardósia · Freijó · Cinza Urban (todos Guararapes) — nunca dividem chapa.

FORA DO ESCOPO (do cliente / outras frentes): granito Itaúnas, porcelanato,
cooktop, cuba, misturador, purificador, forno, micro, geladeira, luminária,
cadeiras, rebaixo de gesso.
"""
from collections import defaultdict

CH_C, CH_L = 275.0, 185.0
CH_AREA = 2.75*1.85

# ── base de custos (referencias/validacao-orcamento.md) ────────────────────
BR6, BR15, BR18 = 190.0, 250.0, 290.0
COR15, COR18    = 500.0, 580.0          # Azul Ardósia · Freijó · Cinza Urban
PRECO = {'BR6':BR6, 'BR15':BR15, 'BR18':BR18,
         'AZ15':COR15, 'AZ18':COR18, 'FR15':COR15, 'FR18':COR18,
         'CZ15':COR15, 'CZ18':COR18}
FITA_BR, FITA_COR = 2.0, 3.0
FILET = 2.50

DOBR      = 10.0     # Hardt c/ amortecimento
CORR      = 70.0     # oculta c/ amortecimento, par
ARTIC     = 150.0    # articulador de báscula
SUP_PRAT  = 1.50
CAVA_M    = 50.0     # usinagem da cava, por metro de frente
TOMADA    = 120.0    # usinagem + caixa das tomadas embutidas na lateral da torre

# ── peças: (móvel, material, descrição, comprimento, largura, qtd) ─────────
p = []
def a(mov, mat, desc, c, l, q=1): p.append((mov, mat, desc, c, l, q))

M1 = '1. Bancada A · 272×77×60 · Azul'          # pia 80 + gav 60 + gav 60 + porta 72
a(M1,'BR15','Vertical',                77, 60, 5)
a(M1,'BR15','Base',                   272, 60, 1)
a(M1,'BR15','Travessa superior',      272, 10, 2)
a(M1,'BR18','Prateleira (módulo porta)',70,58, 1)
a(M1,'BR6', 'Fundo',                  272, 77, 1)
a(M1,'AZ18','Frente — báscula da pia', 80, 25, 1)
a(M1,'AZ18','Frente — gavetão da pia', 80, 50, 1)
a(M1,'AZ18','Frente — gaveta',         60, 25, 6)
a(M1,'AZ18','Porta de giro',           36, 77, 2)
a(M1,'BR15','Gaveta — lateral',        55, 18, 14)
a(M1,'BR15','Gaveta — travessa',       56, 18, 12)
a(M1,'BR15','Gavetão pia — travessa',  76, 18, 2)
a(M1,'BR6', 'Gaveta — fundo',          56, 55, 6)
a(M1,'BR6', 'Gavetão pia — fundo',     76, 55, 1)

M2 = '2. Bancada B · 150×77×60 · Azul'          # 75 (4 gav) + 75 (2 portas)
a(M2,'BR15','Vertical',                77, 60, 3)
a(M2,'BR15','Base',                   150, 60, 1)
a(M2,'BR15','Travessa superior',      150, 10, 2)
a(M2,'BR18','Prateleira',              73, 58, 1)
a(M2,'BR6', 'Fundo',                  150, 77, 1)
a(M2,'AZ18','Frente — gaveta',         75, 19, 4)
a(M2,'AZ18','Porta de giro',         37.5, 77, 2)
a(M2,'BR15','Gaveta — lateral',        55, 18, 8)
a(M2,'BR15','Gaveta — travessa',       71, 18, 8)
a(M2,'BR6', 'Gaveta — fundo',          71, 55, 4)

M3 = '3. Nicho · 150×110 · Freijó'              # vão aberto de 70 + prateleira
a(M3,'FR15','Fundo aparente do nicho',150, 70, 1)
a(M3,'FR18','Prateleira do nicho',    150, 15, 1)
a(M3,'FR15','Arremate lateral',        70,  8, 2)

M4 = '4. Aéreo básculas · 147×40×45 · Freijó'   # 3 módulos de 49
a(M4,'BR15','Vertical',                40, 45, 4)
a(M4,'BR15','Tampo',                  147, 45, 1)
a(M4,'BR15','Base',                   147, 45, 1)
a(M4,'BR6', 'Fundo',                  147, 40, 1)
a(M4,'FR18','Frente — báscula',        49, 40, 3)

M5 = '5. Aéreo · 150×70×60 · Azul'              # 3 portas de giro
a(M5,'BR15','Vertical',                70, 60, 4)
a(M5,'BR15','Tampo',                  150, 60, 1)
a(M5,'BR15','Base',                   150, 60, 1)
a(M5,'BR18','Prateleira',              48, 58, 3)
a(M5,'BR6', 'Fundo',                  150, 70, 1)
a(M5,'AZ18','Porta de giro',           50, 70, 3)
a(M5,'AZ18','Tamponamento lateral',    70, 60, 1)

M6 = '6. Torre quente · 70×270×60 · Cinza Urban'
a(M6,'BR15','Lateral',                270, 60, 2)
a(M6,'BR15','Tampo',                   67, 60, 1)
a(M6,'BR15','Base',                    67, 60, 1)
a(M6,'BR15','Divisória horizontal',    67, 60, 5)
a(M6,'BR6', 'Fundo',                  270, 70, 1)
a(M6,'CZ18','Frente — gaveta',         70, 40, 2)
a(M6,'CZ18','Frente — gavetão',        70, 40, 1)
a(M6,'CZ18','Frente — báscula',        70, 40, 2)
a(M6,'CZ18','Tamponamento lateral (tomadas embutidas)', 270, 60, 1)
a(M6,'BR15','Gaveta — lateral',        55, 18, 6)
a(M6,'BR15','Gaveta — travessa',       66, 18, 6)
a(M6,'BR6', 'Gaveta — fundo',          66, 55, 3)

M7 = '7. Aéreo da geladeira · 80×70×60 · Cinza Urban'
a(M7,'BR15','Vertical',                70, 60, 2)
a(M7,'BR15','Tampo',                   77, 60, 1)
a(M7,'BR15','Base',                    77, 60, 1)
a(M7,'BR18','Prateleira',              76, 58, 1)
a(M7,'BR6', 'Fundo',                   80, 70, 1)
a(M7,'CZ18','Porta de giro',           40, 70, 2)

# ⚠ os dois itens abaixo estao PARCIALMENTE OBSCURECIDOS na captura (barra de
#   rolagem por cima do texto). Dimensoes ESTIMADAS do render — confirmar.
M8 = '8. Painel ripado · Freijó ⚠ ESTIMADO'
N_RIPA = int(120/6)                                   # ripa de 4 + vao de 2
a(M8,'FR15','Base do painel',         270,120, 1)
a(M8,'FR18','Ripa',                   270,  4, N_RIPA)

M9 = '9. Mesa · Freijó ⚠ ESTIMADO'
a(M9,'FR18','Tampo (2 lâminas = 3,6 cm)',150, 60, 2)
a(M9,'FR18','Apoio lateral esquerdo',  75, 60, 1)

# ── nesting por cor × espessura ────────────────────────────────────────────
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

def levanta(pecas, rot):
    por, area = defaultdict(list), defaultdict(float)
    for mov, mat, d, c, l, q in pecas:
        for _ in range(q):
            por[mat].append((c, l)); area[mat] += c*l/10000
    CH = {m: nest(v) for m, v in por.items()}
    print(f'\nPLANO DE CORTE — {rot}')
    custo = 0.0
    for m in sorted(CH, key=lambda k: (k[:2], k)):
        n = CH[m]; c = n*PRECO[m]; custo += c
        print(f'  {m:<6}{area[m]:>6.2f} m²  →  {n} chapa(s) × R$ {PRECO[m]:>6.2f} = '
              f'R$ {c:>9,.2f}   aproveitamento {area[m]/(n*CH_AREA)*100:>3.0f}%')
    tot = sum(CH.values()); ar = sum(area.values())
    print(f'  {"TOTAL":<6}{ar:>6.2f} m²  →  {tot} chapas'
          f'                    R$ {custo:>9,.2f}   médio {ar/(tot*CH_AREA)*100:.0f}%')
    return custo, tot, ar

print('═'*98)
print('COZINHA — consultoria Rizzi Interiores · 9 móveis · 3 cores + branco interno')
print('═'*98)
print('\nMÓVEIS')
for mov in dict.fromkeys(x[0] for x in p): print(f'  {mov}')

BASE = [x for x in p if x[0] not in (M8, M9)]
EXTRA = [x for x in p if x[0] in (M8, M9)]
c_base, n_base, a_base = levanta(BASE, 'móveis 1 a 7 (escopo firme)')
c_extra, n_extra, a_extra = levanta(EXTRA, 'móveis 8 e 9 (painel ripado + mesa) ⚠ estimados')
# o nesting real e' conjunto: o freijo dos dois grupos divide chapa
c_tot, n_tot, a_tot = levanta(p, 'CONJUNTO (nesting real, freijó compartilhado)')

# ── fita: bordas aparentes ────────────────────────────────────────────────
# grupo: 'B' = armários inferiores da bancada (móveis 1 e 2) · 'R' = resto
FR_COR = [
    ('B','Frentes da bancada A — perímetro', 2*(0.80+0.25) + 2*(0.80+0.50) + 6*2*(0.60+0.25) + 2*2*(0.36+0.77)),
    ('B','Frentes da bancada B — perímetro', 4*2*(0.75+0.19) + 2*2*(0.375+0.77)),
    ('R','Nicho freijó — fundo, prateleira e arremates', 2*(1.50+0.70) + 2*(1.50+0.15) + 2*2*(0.70+0.08)),
    ('R','Frentes das básculas freijó',      3*2*(0.49+0.40)),
    ('R','Portas e tamponamento do aéreo azul', 3*2*(0.50+0.70) + (0.70+0.60)),
    ('R','Frentes e tamponamento da torre',  5*2*(0.70+0.40) + (2.70+0.60)),
    ('R','Portas do aéreo da geladeira',     2*2*(0.40+0.70)),
    ('R','Painel ripado — ripas (2 faces longas) ⚠', N_RIPA*2*2.70),
    ('R','Mesa — perímetro do tampo ⚠',      2*(1.50+0.60)),
]
FR_BR = [
    ('B','Verticais da bancada — canto frontal', 5*0.77 + 3*0.77),
    ('R','Demais verticais e laterais — canto frontal', 4*0.40 + 4*0.70 + 2*2.70 + 2*0.70),
    ('B','Bases e travessas da bancada — frente', 2.72 + 2*2.72 + 1.50 + 2*1.50),
    ('R','Demais bases e travessas — frente', 1.47*2 + 1.50*2 + 0.67*7 + 0.77*2),
    ('B','Prateleiras da bancada — frente', 0.70 + 0.73),
    ('R','Demais prateleiras — frente',  3*0.48 + 0.76),
    ('B','Caixas de gaveta da bancada — topo', 14*2*(0.56+0.55)/2 + 4*2*(0.71+0.55)/2),
    ('R','Caixas de gaveta da torre — topo',   3*2*(0.66+0.55)/2),
]
m_cor = sum(m for _, _, m in FR_COR); m_br = sum(m for _, _, m in FR_BR)
custo_fita = m_cor*1.10*FITA_COR + m_br*1.10*FITA_BR
custo_filet = (m_cor + m_br)*FILET
print('\nFITA DE BORDA  (+10% de desperdício)')
for g, d, m in FR_COR + FR_BR: print(f'  {g}  {d:<47}{m:>7.2f} m')
print(f'  {"— cor":<50}{m_cor:>7.2f} m × R$ {FITA_COR:.2f}')
print(f'  {"— branco":<50}{m_br:>7.2f} m × R$ {FITA_BR:.2f}')
print(f'  {"material":<50}{m_cor+m_br:>7.2f} m        R$ {custo_fita:>9,.2f}')
print(f'  {"filetagem":<50}{m_cor+m_br:>7.2f} m × R$ {FILET:.2f} = R$ {custo_filet:>9,.2f}')

# ── ferragens ─────────────────────────────────────────────────────────────
N_DOBR  = 2*2 + 2*2 + 3*2 + 2*2                    # portas de giro (todas ≤ 90 cm)
N_CORR  = 7 + 4 + 3                                # gavetas
N_ARTIC = 3 + 2                                    # básculas freijó + torre
N_PRAT  = 1 + 1 + 3 + 1 + 1                        # prateleiras com suporte
M_CAVA  = (0.80+0.80+6*0.60+2*0.36) + (4*0.75+2*0.375) + 3*0.49 + 3*0.50 + 5*0.70 + 2*0.40
CAVA_B = (0.80+0.80+6*0.60+2*0.36) + (4*0.75+2*0.375)
ferr = [
    ('B', 'Dobradiça Hardt — 8 un (portas de giro da bancada)',   8*DOBR),
    ('R', f'Dobradiça Hardt — {N_DOBR-8} un (aéreos)',            (N_DOBR-8)*DOBR),
    ('B', 'Corrediça oculta c/ amortecimento — 11 pares',         11*CORR),
    ('R', 'Corrediça oculta c/ amortecimento — 3 pares (torre)',  3*CORR),
    ('R', f'Articulador de báscula — {N_ARTIC} un',               N_ARTIC*ARTIC),
    ('B', 'Suporte de báscula da pia (frente falsa) — 1 un',      40.0),
    ('B', 'Suporte de prateleira — 8 un',                         8*SUP_PRAT),
    ('R', f'Suporte de prateleira — {N_PRAT*4-8} un',             (N_PRAT*4-8)*SUP_PRAT),
    ('B', f'Cava usinada — {CAVA_B:.2f} m (frentes da bancada)',  CAVA_B*CAVA_M),
    ('R', f'Cava usinada — {M_CAVA-CAVA_B:.2f} m (aéreos e torre)', (M_CAVA-CAVA_B)*CAVA_M),
    ('R', 'Usinagem e caixa das tomadas embutidas na torre',      TOMADA),
]
custo_ferr = sum(v for _, _, v in ferr)
print('\nFERRAGENS  (linha básica/Hardt — a definir)')
for g, d, v in ferr: print(f'  {g}  {d:<59}R$ {v:>9,.2f}')
print(f'  {"TOTAL":<62}R$ {custo_ferr:>9,.2f}')

# ── custo direto ──────────────────────────────────────────────────────────
consum = (c_tot + custo_fita)*0.06
MAT = c_tot + custo_fita + custo_filet + custo_ferr + consum
LOG, VIS, INST = 900.0, 500.0, 2800.0
fixedR = MAT + LOG + VIS + INST
print('\n' + '─'*98)
for d, v in (('Chapas', c_tot), ('Fita (material)', custo_fita), ('Filetagem', custo_filet),
             ('Ferragens e usinagem', custo_ferr), ('Consumíveis (6%)', consum),
             ('Logística · 2 visitas · instalação', LOG+VIS+INST)):
    print(f'  {d:<62}R$ {v:>9,.2f}')
print(f'  {"CUSTO DIRETO":<62}R$ {fixedR:>9,.2f}')

# ══ SEPARAÇÃO DOS ARMÁRIOS INFERIORES DA BANCADA [Jonathan 07/08] ═════════
# Móveis 1 e 2 (bancada A 272 + bancada B 150) saem em linha própria.
#
# A chapa é RATEADA POR ÁREA dentro de cada material, não re-nestada. Motivo:
# BR15/BR18/BR6 e AZ18 são compartilhados com os aéreos — nestar os dois grupos
# em separado somaria mais chapas que o conjunto (piso de 1 chapa por cor). O
# rateio faz as duas linhas fecharem no total. Logo abaixo eu mostro o que
# REALMENTE se economiza se o bloco sair do escopo, que é outro número.
BANC = (M1, M2)
ar_g = defaultdict(lambda: defaultdict(float))
for mov, mat, d, c, l, q in p:
    ar_g['B' if mov in BANC else 'R'][mat] += c*l/10000*q

por = defaultdict(list)
for mov, mat, d, c, l, q in p:
    for _ in range(q): por[mat].append((c, l))
CH = {m: nest(v) for m, v in por.items()}

ch_g = {'B': 0.0, 'R': 0.0}
print('\n' + '═'*98)
print('RATEIO DA CHAPA — armários inferiores da bancada × restante')
print('═'*98)
print(f'  {"":<6}{"bancada":>16}{"restante":>16}{"chapas":>9}{"custo":>13}')
for m in sorted(CH, key=lambda k: (k[:2], k)):
    tb, tr = ar_g['B'][m], ar_g['R'][m]
    custo_m = CH[m]*PRECO[m]
    if tb + tr:
        ch_g['B'] += custo_m*tb/(tb+tr); ch_g['R'] += custo_m*tr/(tb+tr)
    print(f'  {m:<6}{tb:>13.2f} m²{tr:>13.2f} m²{CH[m]:>9}   R$ {custo_m:>9,.2f}')
print(f'  {"":<6}{"":>16}{"":>16}{"":>9}   R$ {sum(ch_g.values()):>9,.2f}')
print(f'  Chapa rateada:  bancada R$ {ch_g["B"]:,.2f}   ·   restante R$ {ch_g["R"]:,.2f}')

# fita, filetagem e ferragens saem exatos pelas tags de grupo
ft_g, fl_g, fe_g = {}, {}, {}
for g in ('B', 'R'):
    mc = sum(m for gg, _, m in FR_COR if gg == g)
    mb = sum(m for gg, _, m in FR_BR  if gg == g)
    ft_g[g] = mc*1.10*FITA_COR + mb*1.10*FITA_BR
    fl_g[g] = (mc + mb)*FILET
    fe_g[g] = sum(v for gg, _, v in ferr if gg == g)

# consumíveis e logística seguem a proporção do material
sub = {g: ch_g[g] + ft_g[g] + fl_g[g] + fe_g[g] for g in ('B', 'R')}
fr_g = {}
for g in ('B', 'R'):
    prop = sub[g]/sum(sub.values())
    fr_g[g] = sub[g] + (ch_g[g] + ft_g[g])*0.06 + (LOG + VIS + INST)*prop

print('\n' + '─'*98)
print(f'  {"":<40}{"BANCADA INFERIOR":>20}{"RESTANTE":>18}{"TOTAL":>16}')
for rot, d in (('Chapas', ch_g), ('Fita (material)', ft_g), ('Filetagem', fl_g),
               ('Ferragens, cava e usinagem', fe_g)):
    print(f'  {rot:<40}R$ {d["B"]:>15,.2f}R$ {d["R"]:>13,.2f}R$ {d["B"]+d["R"]:>11,.2f}')
cs = {g: (ch_g[g]+ft_g[g])*0.06 for g in ('B','R')}
lg = {g: (LOG+VIS+INST)*sub[g]/sum(sub.values()) for g in ('B','R')}
for rot, d in (('Consumíveis (6%)', cs), ('Logística · visitas · instalação', lg)):
    print(f'  {rot:<40}R$ {d["B"]:>15,.2f}R$ {d["R"]:>13,.2f}R$ {d["B"]+d["R"]:>11,.2f}')
print(f'  {"CUSTO DIRETO":<40}R$ {fr_g["B"]:>15,.2f}R$ {fr_g["R"]:>13,.2f}'
      f'R$ {fr_g["B"]+fr_g["R"]:>11,.2f}')

# ── PREÇO — parâmetros travados [Jonathan 07/08] ──────────────────────────
# COM RT (10% do líquido) · ferragem Hardt (linha básica).
# MC 35% -> 30%: "o perfil do cliente nao condiz com esse valor".
a_, liqF_, b_, rt_, MC = 0.162, 0.88, 0.043, 0.10, 0.30
div = 1 - a_ - liqF_*b_ - liqF_*rt_ - MC
print('\n' + '═'*98)
print(f'PREÇO — MC {MC*100:.0f}% · COM RT {rt_*100:.0f}% do líquido · Hardt · divisor {div:.5f}')
print('═'*98)
pr = {g: round(fr_g[g]/div/100)*100 for g in ('B', 'R')}
print(f'  {"Armários inferiores da bancada":<46}R$ {fr_g["B"]:>9,.2f} ÷ {div:.5f} = R$ {pr["B"]:>8,.0f}')
print(f'  {"Demais móveis (aéreos, nicho, torre, ripado, mesa)":<46}'
      f'R$ {fr_g["R"]:>9,.2f} ÷ {div:.5f} = R$ {pr["R"]:>8,.0f}')
TAB = pr['B'] + pr['R']
print(f'  {"TOTAL DE TABELA":<46}{"":>28}R$ {TAB:>8,.0f}')
print(f'\n  MC conferida: '
      f'{(TAB - TAB*(a_+liqF_*b_+liqF_*rt_) - (fr_g["B"]+fr_g["R"]))/TAB*100:.1f}%')
print(f'  RT ao parceiro: R$ {TAB*(1-a_*0)*0:,.0f}'.replace('R$ 0', f'R$ {TAB*liqF_*rt_:,.0f}'))

print('\n  ESCADA DE PAGAMENTO — a MC 30% ela encosta no piso da casa')
ENC = a_ + liqF_*b_ + liqF_*rt_
for d, desc in (('Entrada 30% + até 10× no cartão', 0.00), ('Entrada 50% + até 8× no cartão', 0.03),
                ('Entrada 70% + até 6× no cartão', 0.05), ('Entrada 70% + transferência', 0.07)):
    v = round(TAB*(1-desc)/100)*100
    mc = (v - v*ENC - (fr_g['B']+fr_g['R']))/v*100
    flag = '  ⚠ abaixo do piso de 28%' if mc < 28 else ''
    print(f'    {d:<44}{"—" if not desc else f"−{desc*100:.0f}%":>5}   '
          f'R$ {v:>8,.0f}   MC {mc:>4.1f}%{flag}')

# ── o RT pesa mais que os 5 pontos de MC ──────────────────────────────────
print('\n' + '═'*98)
print('O RT PESA MAIS QUE OS 5 PONTOS DE MC')
print('═'*98)
FX = fr_g['B'] + fr_g['R']
for mc_, rt2, rot in ((0.35, rt_, 'MC 35% COM RT'), (0.30, rt_, 'MC 30% COM RT  ← o pedido'),
                      (0.35, 0.0, 'MC 35% SEM RT'), (0.30, 0.0, 'MC 30% SEM RT')):
    dv = 1 - a_ - liqF_*b_ - liqF_*rt2 - mc_
    t = round(fr_g['B']/dv/100)*100 + round(fr_g['R']/dv/100)*100
    print(f'  {rot:<28} R$ {t:>7,.0f}   MC real '
          f'{(t - t*(a_+liqF_*b_+liqF_*rt2) - FX)/t*100:>4.1f}%   RT ao parceiro R$ {t*liqF_*rt2:>6,.0f}')
d35 = 1 - a_ - liqF_*b_ - liqF_*rt_ - 0.35
t35 = round(fr_g['B']/d35/100)*100 + round(fr_g['R']/d35/100)*100
d35s = 1 - a_ - liqF_*b_ - 0.35
t35s = round(fr_g['B']/d35s/100)*100 + round(fr_g['R']/d35s/100)*100
print(f'\n  Cortar 5 pontos de MC alivia R$ {t35-TAB:,.0f} e nos custa 5 pontos.')
print(f'  Tirar o RT a MC 35% alivia R$ {t35-t35s:,.0f} e NÃO nos custa nada.')
print(f'  R$ {t35s:,.0f} a MC 35% sem RT é MAIS BARATO que os R$ {TAB:,.0f} a MC 30% com RT.')

# ── o que o rateio NÃO diz ────────────────────────────────────────────────
print('\n' + '═'*98)
print('SE A BANCADA INFERIOR SAIR DO ESCOPO, NÃO SE ECONOMIZA A LINHA INTEIRA')
print('═'*98)
RESTO = [x for x in p if x[0] not in BANC]
por_r = defaultdict(list); ar_r = defaultdict(float)
for mov, mat, d, c, l, q in RESTO:
    for _ in range(q): por_r[mat].append((c, l)); ar_r[mat] += c*l/10000
CH_R = {m: nest(v) for m, v in por_r.items()}
ch_real = sum(CH_R[m]*PRECO[m] for m in CH_R)
sub_r = ch_real + ft_g['R'] + fl_g['R'] + fe_g['R']
fr_real = sub_r + (ch_real + ft_g['R'])*0.06 + (LOG + VIS + INST)*0.72
print(f'  Chapas do restante — nestado sozinho: {sum(CH_R.values())} chapas '
      f'(no conjunto o rateio dava R$ {ch_g["R"]:,.2f}; sozinho custa R$ {ch_real:,.2f})')
print(f'  Custo direto do restante sozinho ..... R$ {fr_real:>9,.2f}')
print(f'  Preço ................................ R$ {round(fr_real/div/100)*100:>9,.0f}')
print(f'  Economia real de tirar a bancada ..... R$ {TAB - round(fr_real/div/100)*100:>9,.0f}'
      f'   (a linha rateada mostra R$ {pr["B"]:,.0f})')
print('  A diferença é o piso de 1 chapa por cor × espessura: sem a bancada, o branco')
print('  não encolhe na mesma proporção, e a instalação da cozinha não cai 28%.')

print('\n' + '─'*98)
print('⚠ A CONFERIR NO PROJETO')
print('  · Painel ripado e mesa: as duas linhas do documento estão COBERTAS pela barra')
print('    de rolagem na captura. Dimensões usadas são estimativa do render.')
print(f'  · "Ripas de 1cm" — usei ripa de 4 cm com vão de 2 ({N_RIPA} ripas). Se for ripa')
print(f'    de 1 cm mesmo, são ~{int(120/2)} ripas e a fita desse item vai de '
      f'{N_RIPA*2*2.70:.0f} m para {int(120/2)*2*2.70:.0f} m.')
print('  · Divisão interna dos módulos da bancada é leitura minha da elevação etiquetada.')
print('  · Interno branco assumido — a consultoria não especifica o interno de nenhum móvel.')
print('  · Medição no local é pré-requisito: o próprio documento diz que as cotas dele')
print('    "não servem como referência para compra final".')
