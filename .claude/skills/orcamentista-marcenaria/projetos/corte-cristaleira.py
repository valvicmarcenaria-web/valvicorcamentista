# -*- coding: utf-8 -*-
"""CRISTALEIRA — levantamento e preço.

Prancha A3 cotada (DETCristaleira.pdf), escala 1:20, quatro vistas.
Premissas do Jonathan [04/08/2026]: SEM RT · MC 35% · 60 dias corridos ·
pagamento na escada padrão da empresa · ferragens Hardt.

Geometria lida da prancha
  externa 100 L × 205 A × 40 P   ·  corpo 201 A × 38 P  ·  interno 96 L
  superior 115 = tampo 2 + 4 vãos de 26,75 + 3 prateleiras
  divisória 2  ·  inferior 84 = 3 gavetas de 28 (25 de frente + 3 de folga)
  pé 4 com recuo frontal de 2
  2 portas de 50 × 201, moldura de 4 cm, vidro incolor 42 × 193
  puxador a 110 do piso
"""
from collections import defaultdict

CH_C, CH_L = 275.0, 185.0
CH_AREA = 2.75*1.85                      # 5,0875 m²

# ── base de custos (dados/materiais.json) ────────────────────────────────────
# "MDF Arauco Moscada Matt" = melamínico fosco amadeirado
MOS6, MOS15, MOS18 = 300.0, 500.0, 600.0
BRC6, BRC15        = 190.0, 260.0
FITA_COR, FITA_BRC = 3.0, 2.0            # R$/m  (+10% desperdício)
FILET_MAQ, FILET_MAN = 2.50, 4.0         # R$/m aplicados
DOBR_HARDT   = 8.0                       # un
CORR_HARDT   = 70.0                      # par — oculta
CAVA45       = 52.0                      # por peça usinada
PUXADOR      = 60.0                      # Italyline Ales 118 cobre velho ⚠ A CONFIRMAR
VIDRO_M2     = 200.0                     # incolor temperado 6 mm
VIDRACEIRO   = 150.0                     # corte, embalagem e transporte de peça de 1,93 m

PRECO = {'MOS6':MOS6, 'MOS15':MOS15, 'MOS18':MOS18, 'BRC6':BRC6, 'BRC15':BRC15}

# ── peças  (material, descrição, comprimento, largura, qtd) ──────────────────
pecas = [
    # caixaria em 15 mm — regra da casa: caixaria 15, prateleira de vão >70 em 18
    ('MOS15', 'Lateral',                    201, 38, 2),
    ('MOS15', 'Tampo',                       96, 38, 1),
    ('MOS15', 'Base',                        96, 38, 1),
    ('MOS15', 'Pé — frente (recuo 2 cm)',    96,  4, 1),
    ('MOS15', 'Pé — travessa traseira',      96,  4, 1),
    ('MOS15', 'Pé — lateral',                36,  4, 2),
    # 18 mm — prateleiras (vão de 96), divisória estrutural, portas e frentes
    ('MOS18', 'Prateleira',                  96, 36, 3),
    ('MOS18', 'Divisória prateleiras/gavetas',96, 38, 1),
    ('MOS18', 'Porta — montante da moldura',201,  4, 4),
    ('MOS18', 'Porta — travessa da moldura', 42,  4, 4),
    ('MOS18', 'Frente de gaveta',            96, 25, 3),
    ('MOS6',  'Fundo',                       98,199, 1),
    # gavetas: caixa em Branco TX (a prancha manda interior de gaveta em branco)
    ('BRC15', 'Gaveta — lateral',            34, 20, 6),
    ('BRC15', 'Gaveta — travessa',           90, 20, 6),
    ('BRC6',  'Gaveta — fundo',              93, 34, 3),
]

# ── fita: só as bordas que aparecem ──────────────────────────────────────────
# (material_da_fita, descrição, metros)
fitas = [
    ('COR', 'Laterais — canto frontal',            2*2.01),
    ('COR', 'Laterais — topo aparente',            2*0.38),
    ('COR', 'Tampo e base — frente',               2*0.96),
    ('COR', 'Prateleiras — frente',                3*0.96),
    ('COR', 'Divisória — frente',                  1*0.96),
    ('COR', 'Pé — frente',                         1*0.96),
    ('COR', 'Frentes de gaveta — perímetro',       3*2*(0.96+0.25)),
    ('COR', 'Portas — perímetro externo',          2*2*(0.50+2.01)),
    ('BRC', 'Gavetas — topo da caixa',             3*2*(0.93+0.34)),
]
# o perímetro INTERNO da moldura é filetado depois do vão pronto → manual
fita_manual = [('COR', 'Portas — perímetro do vão de vidro', 2*2*(0.42+1.93))]

# ── nesting (função da casa) ────────────────────────────────────────────────
def nest(items):
    if not items: return 0
    pcs = sorted(([max(c,l), min(c,l)] for c,l in items), key=lambda p: -p[1])
    chapas = 0; y = x = faixa = 0.0
    for c, l in pcs:
        if c > CH_C and l <= CH_C: c, l = l, c
        if c > CH_C or l > CH_L: chapas += 1; continue
        if x + c > CH_C: y += faixa; x = 0.0; faixa = 0.0
        if y + l > CH_L: chapas += 1; y = x = faixa = 0.0
        x += c; faixa = max(faixa, l)
    chapas += 1
    area = sum(c*l for c,l in items)/10000
    return max(chapas, -(-int(area/(CH_AREA*0.80)*1000)//1000) or 1)

por_mat = defaultdict(list)
area_mat = defaultdict(float)
for mat, desc, c, l, q in pecas:
    for _ in range(q):
        por_mat[mat].append((c, l))
        area_mat[mat] += c*l/10000

CHAPAS = {m: nest(v) for m, v in por_mat.items()}

print('═'*92)
print('CRISTALEIRA — 100 × 205 × 40 cm · MDF Arauco Moscada Matt · portas de vidro incolor')
print('═'*92)

print('\nPLANO DE CORTE')
custo_chapa = 0.0
for m in sorted(CHAPAS):
    n = CHAPAS[m]; c = n*PRECO[m]; custo_chapa += c
    ap = area_mat[m]/(n*CH_AREA)*100
    print(f'  {m:<7}{area_mat[m]:>6.2f} m²  →  {n} chapa(s) × R$ {PRECO[m]:>6.2f}'
          f'  = R$ {c:>8,.2f}   aproveitamento {ap:>3.0f}%')
tot_ch = sum(CHAPAS.values())
print(f'  {"TOTAL":<7}{sum(area_mat.values()):>6.2f} m²  →  {tot_ch} chapas'
      f'                      R$ {custo_chapa:>8,.2f}   médio '
      f'{sum(area_mat.values())/(tot_ch*CH_AREA)*100:.0f}%')

print('\nFITA DE BORDA  (+10% de desperdício)')
m_maq = sum(m for _, _, m in fitas)
m_man = sum(m for _, _, m in fita_manual)
custo_fita = sum(m*1.10*(FITA_COR if t == 'COR' else FITA_BRC) for t, _, m in fitas) \
           + sum(m*1.10*FITA_COR for t, _, m in fita_manual)
custo_filet = m_maq*FILET_MAQ + m_man*FILET_MAN
for t, d, m in fitas + fita_manual:
    print(f'  {d:<44}{m:>7.2f} m   fita {t}')
print(f'  {"— na coladeira":<44}{m_maq:>7.2f} m × R$ {FILET_MAQ:.2f}  = R$ {m_maq*FILET_MAQ:>8,.2f}')
print(f'  {"— manual (vão da moldura, 4 cm)":<44}{m_man:>7.2f} m × R$ {FILET_MAN:.2f}  = R$ {m_man*FILET_MAN:>8,.2f}')
print(f'  {"material da fita":<44}{m_maq+m_man:>7.2f} m'
      f'              R$ {custo_fita:>8,.2f}')

print('\nFERRAGENS E TERCEIRIZADOS  (linha Hardt)')
n_dobr = 2*5                                   # porta de 2,01 m + peso do vidro → 5 por folha
vidro_m2 = 2*(0.42*1.93)
ferr = [
    (f'Dobradiça Hardt — {n_dobr} un (5 por folha, porta de 2,01 m)', n_dobr*DOBR_HARDT),
    ('Corrediça oculta Hardt — 3 pares',                              3*CORR_HARDT),
    ('Puxador Ponto Italyline Ales 118 cobre velho — 2 un ⚠',         2*PUXADOR),
    ('Cava 45° usinada — 3 frentes de gaveta',                        3*CAVA45),
    (f'Vidro incolor temperado 6 mm — {vidro_m2:.2f} m² (2 × 42 × 193)', vidro_m2*VIDRO_M2),
    ('Vidraceiro — corte, embalagem e transporte',                    VIDRACEIRO),
]
custo_ferr = sum(v for _, v in ferr)
for d, v in ferr: print(f'  {d:<62}R$ {v:>8,.2f}')
print(f'  {"TOTAL":<62}R$ {custo_ferr:>8,.2f}')

consum = (custo_chapa + custo_fita)*0.06
MAT = custo_chapa + custo_fita + custo_filet + custo_ferr + consum
LOGISTICA, VISITA, INSTALACAO = 400.0, 250.0, 500.0    # peça única; vidro exige transporte cuidadoso
fixedR = MAT + LOGISTICA + VISITA + INSTALACAO

print('\n' + '─'*92)
print(f'  {"Chapas":<62}R$ {custo_chapa:>8,.2f}')
print(f'  {"Fita (material)":<62}R$ {custo_fita:>8,.2f}')
print(f'  {"Filetagem (aplicação)":<62}R$ {custo_filet:>8,.2f}')
print(f'  {"Ferragens, vidro e vidraceiro":<62}R$ {custo_ferr:>8,.2f}')
print(f'  {"Consumíveis (6% de chapa + fita)":<62}R$ {consum:>8,.2f}')
print(f'  {"Logística · visita · instalação":<62}R$ {LOGISTICA+VISITA+INSTALACAO:>8,.2f}')
print(f'  {"CUSTO DIRETO":<62}R$ {fixedR:>8,.2f}')

# ── preço ───────────────────────────────────────────────────────────────────
# a=0,162 · liqF=0,88 · b=0,043 — este é o conjunto SEM RT.
# RT (10% do líquido, quando há parceiro) NÃO está embutido aqui.
a_, liqF_, b_, MC = 0.162, 0.88, 0.043, 0.35
div = 1 - a_ - liqF_*b_ - MC
inv = fixedR/div
tabela = round(inv/100)*100

print('\n' + '═'*92)
print(f'PREÇO — MC {MC*100:.0f}% · SEM RT · divisor {div:.5f}')
print('═'*92)
print(f'  Custo direto R$ {fixedR:,.2f}  ÷  {div:.5f}  =  R$ {inv:,.2f}   →  tabela R$ {tabela:,.0f}')
print()
escada = [('Entrada 30% + até 10× no cartão', 0.00),
          ('Entrada 50% + até 8× no cartão',  0.03),
          ('Entrada 70% + até 6× no cartão',  0.05),
          ('Entrada 70% + restante em transferência', 0.07)]
for d, desc in escada:
    v = round(tabela*(1-desc)/100)*100
    print(f'  {d:<46}{"—" if not desc else f"−{desc*100:.0f}%":>5}   R$ {v:>9,.0f}')
print(f'\n  Prazo de entrega: 60 dias corridos')
print(f'  MC conferida: {(tabela - (tabela*(a_ + liqF_*b_)) - fixedR)/tabela*100:.1f}% sobre a tabela')

# ── o que o "interior de gaveta em branco" custa ─────────────────────────────
# A prancha manda a caixa da gaveta em MDF Branco TX. Isso obriga a comprar
# DUAS chapas inteiras (BRC15 + BRC6) para 2,44 m² de peças — e as sobras de
# Moscada dariam conta: MOS15 sobra 2,73 m² (preciso 1,49) e MOS6 sobra
# 3,14 m² (preciso 0,95).
print('\n' + '═'*92)
print('ALTERNATIVA — caixa de gaveta na sobra do Moscada em vez de Branco TX')
print('═'*92)
econ_chapa = PRECO['BRC15'] + PRECO['BRC6']
fixedR_alt = fixedR - econ_chapa - econ_chapa*0.06        # sai a chapa e o consumível dela
inv_alt = fixedR_alt/div
tab_alt = round(inv_alt/100)*100
print(f'  MOS15  2,36 → 3,85 m² (1 chapa, {3.85/CH_AREA*100:.0f}%)   ·   '
      f'MOS6  1,95 → 2,90 m² (1 chapa, {2.90/CH_AREA*100:.0f}%)')
print(f'  5 chapas → 3 chapas.  Custo direto R$ {fixedR:,.2f} → R$ {fixedR_alt:,.2f}'
      f'   (−R$ {fixedR-fixedR_alt:,.2f})')
print(f'  Tabela R$ {tabela:,.0f} → R$ {tab_alt:,.0f}   ·   diferença R$ {tabela-tab_alt:,.0f}')
print('  → o interior branco da gaveta é uma escolha de projeto que custa'
      f' R$ {tabela-tab_alt:,.0f} ao cliente.')
print('    Está mantido no preço acima, como a prancha pede.')

print('\n' + '─'*92)
print('⚠ NA MARGEM, NÃO NO CUSTO')
print('  Pelo método da casa a hora de bancada fica na margem, não em linha de custo.')
print('  Neste móvel isso pesa mais que o normal: são 8 encaixes de moldura e')
print(f'  {2*2*(0.42+1.93):.1f} m de rebaixo para assentar o vidro. Em chapa a porta é barata')
print(f'  (R$ {4*(201*4)/10000*PRECO["MOS18"]/CH_AREA + 4*(42*4)/10000*PRECO["MOS18"]/CH_AREA:.2f} '
      'de MDF); o custo dela é bancada — igual ao ripado dos quartos.')
print('  Se essa hora for cobrada, MC 35% vira ~33,5% real. Para blindar, MC 37%'
      f' → tabela R$ {round(fixedR/(1-a_-liqF_*b_-0.37)/100)*100:,.0f}.')

# ── PREÇO FECHADO [Jonathan 04/08] ──────────────────────────────────────────
# Divisor calibrado: quando o preço é dado, leio a MC de volta em vez de
# recalcular o preço.
print('\n' + '═'*92)
print('FECHADO EM R$ 7.500 — MC lida de volta')
print('═'*92)
A_CARTAO = 0.072                                   # taxa de cartão dentro do a=0,162
for alvo, rot in ((tabela, 'tabela calculada'), (7500, 'FECHADO — no cartão')):
    d = fixedR/alvo
    print(f'  {rot:<26}R$ {alvo:>6,.0f}   divisor {d:.5f}   MC {(1-a_-liqF_*b_-d)*100:>5.1f}%')
d = fixedR/7500
print(f'  {"FECHADO — em transferência":<26}R$ {7500:>6,.0f}   divisor {d:.5f}   '
      f'MC {(1-(a_-A_CARTAO)-liqF_*b_-d)*100:>5.1f}%')
print('\n  Faixa da casa: <28% abaixo do ideal · 28–38% saudável · meta 35–40%.')
print('  No cartão o negócio fica ABAIXO do piso. Em transferência encosta nele.')
print('  A forma de pagamento é que decide se esta venda se paga.')
