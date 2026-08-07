# -*- coding: utf-8 -*-
"""COZINHA (Rizzi) — duas variantes de corrediça  [Jonathan 07/08/2026]

"faça um orçamento com corrediça telescópica e outro com oculta Hardt ·
 MC 30% · se atente para o tempo de garantia de cada · prazo 60 a 70 dias"

A ÚNICA variável entre as duas versões é a corrediça. Chapa, fita, dobradiça,
articulador, cava, logística e instalação são idênticas — é o que permite opor
as duas colunas sem ressalva.

GARANTIA — de `referencias/proposta-comercial.md`:
  Oculta slow motion (Gold) ...... 10 anos em estrutura E ferragens
  Telescópica (Silver) ........... 10 anos / **2 anos nas corrediças**
São 8 anos de diferença, e eles moram exatamente na peça que muda.
"""
# ── componentes por grupo, de corte-cozinha-elena.py ───────────────────────
# B = armários inferiores da bancada (móveis 1 e 2) · R = demais móveis
CHAPA  = {'B': 2127.34, 'R': 4572.66}
FITA   = {'B':  193.84, 'R':  577.59}
FILET  = {'B':  180.88, 'R':  461.90}
FERR   = {'B': 1385.50, 'R': 1573.50}     # inclui corrediça OCULTA a R$ 70/par
LOG    = 4200.00                           # logística + 2 visitas + instalação
N_CORR = {'B': 11, 'R': 3}                 # 14 pares no total
P_OCULTA, P_TELESC = 70.0, 30.0            # R$/par — validacao-orcamento.md

a_, liqF_, b_, rt_, MC = 0.162, 0.88, 0.043, 0.10, 0.30
ENC = a_ + liqF_*b_ + liqF_*rt_
div = 1 - ENC - MC

def custo(p_corr):
    """Custo direto por grupo, trocando só o preço da corrediça."""
    ferr = {g: FERR[g] - N_CORR[g]*(P_OCULTA - p_corr) for g in ('B', 'R')}
    sub  = {g: CHAPA[g] + FITA[g] + FILET[g] + ferr[g] for g in ('B', 'R')}
    tot  = sum(sub.values())
    cons = {g: (CHAPA[g] + FITA[g])*0.06 for g in ('B', 'R')}
    return {g: sub[g] + cons[g] + LOG*sub[g]/tot for g in ('B', 'R')}, ferr

def br(v): return f'{v:,.0f}'.replace(',', '.')

print('═'*88)
print(f'DUAS VARIANTES DE CORREDIÇA — MC {MC*100:.0f}% · COM RT · divisor {div:.5f}')
print('═'*88)

RES = {}
for rot, p_corr in (('OCULTA Hardt c/ amortecimento', P_OCULTA),
                    ('TELESCÓPICA', P_TELESC)):
    c, ferr = custo(p_corr)
    pr = {g: round(c[g]/div/100)*100 for g in ('B', 'R')}
    tot = pr['B'] + pr['R']
    fx = c['B'] + c['R']
    RES[rot] = (c, pr, tot, fx)
    print(f'\n{rot}  —  14 pares × R$ {p_corr:.0f} = R$ {14*p_corr:,.2f}')
    print(f'  {"Armários inferiores da bancada":<44}R$ {c["B"]:>9,.2f}  →  R$ {pr["B"]:>7,.0f}')
    print(f'  {"Demais móveis":<44}R$ {c["R"]:>9,.2f}  →  R$ {pr["R"]:>7,.0f}')
    print(f'  {"TOTAL":<44}R$ {fx:>9,.2f}  →  R$ {tot:>7,.0f}')
    print(f'  MC conferida {(tot - tot*ENC - fx)/tot*100:.1f}%   ·   '
          f'RT ao parceiro R$ {tot*liqF_*rt_:,.0f}')

(cO, pO, tO, fO) = RES['OCULTA Hardt c/ amortecimento']
(cT, pT, tT, fT) = RES['TELESCÓPICA']
print('\n' + '─'*88)
print(f'  Diferença de custo ..... R$ {fO-fT:>8,.2f}   (14 pares × R$ {P_OCULTA-P_TELESC:.0f})')
print(f'  Diferença de preço ..... R$ {tO-tT:>8,.0f}')
print(f'  → {(tO-tT)/tT*100:.1f}% de acréscimo para trocar a corrediça e ganhar 8 anos')
print(f'    de garantia na gaveta. São R$ {(tO-tT)/14:,.0f} por gaveta.')

print('\n' + '═'*88)
print('ESCADA DE PAGAMENTO — a MC 30% os dois últimos degraus furam o piso de 28%')
print('═'*88)
print(f'  {"":<44}{"OCULTA":>12}{"MC":>7}{"TELESC.":>12}{"MC":>7}')
for d, rot in ((0.00, 'Entrada 30% + até 10× no cartão'), (0.03, 'Entrada 50% + até 8× no cartão'),
               (0.05, 'Entrada 70% + até 6× no cartão'), (0.07, 'Entrada 70% + transferência')):
    vO, vT = round(tO*(1-d)/100)*100, round(tT*(1-d)/100)*100
    mO = (vO - vO*ENC - fO)/vO*100
    mT = (vT - vT*ENC - fT)/vT*100
    fl = ' ⚠' if min(mO, mT) < 28 else ''
    print(f'  {rot:<44}{vO:>12,.0f}{mO:>6.1f}%{vT:>12,.0f}{mT:>6.1f}%{fl}')

print('\n' + '═'*88)
print('GARANTIA — a diferença mora na peça que muda')
print('═'*88)
print('  Oculta Hardt c/ amortecimento .... 10 anos em estrutura E ferragens')
print('  Telescópica ...................... 10 anos em estrutura e ferragens')
print('                                      2 anos nas corrediças')
print('  → 8 anos de diferença, só na gaveta. Fonte: referencias/proposta-comercial.md')

print('\n' + '─'*88)
print('SEM OS ARMÁRIOS INFERIORES DA BANCADA')
FR_SO = 10961.04                        # restante nestado sozinho, corrediça oculta
FR_SO_T = FR_SO - 3*(P_OCULTA-P_TELESC)
for rot, v, t in (('Oculta', FR_SO, tO), ('Telescópica', FR_SO_T, tT)):
    p = round(v/div/100)*100
    print(f'  {rot:<14} restante sozinho R$ {p:>7,.0f}   ·   economia real R$ {t-p:>7,.0f}')
print('  (a linha rateada da bancada mostra mais do que isso — o piso de 1 chapa')
print('   por cor não encolhe, e a instalação continua sendo uma cozinha inteira)')
