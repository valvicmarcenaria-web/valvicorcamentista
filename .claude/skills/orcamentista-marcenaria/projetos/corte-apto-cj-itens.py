# -*- coding: utf-8 -*-
"""
APTO CJ — CUSTO E PREÇO POR ITEM, EM CADA VERSÃO  [Jonathan 28/07]
Base de chapa REAL: branca 15 R$300 · 6 R$200 · cor 15 R$500 · 6 R$350
                    (18mm derivado: branca 380 · cor 600 — CONFIRMAR)

Móveis:  A entrada · B varanda/gourmet · C estante (salas) · D adega (serralheria)
Versões: A/B → v1 lâmina natural  ·  v2 100% melamínico Freijó Puro
         C   → v1 laca completa · v2 laca ext+branco int · v3 melamínico cor
               inteiro · v4 cor ext + branco int
Divisor CALIBRADO para honrar a opção 1 já entregue (R$ 84.600) → MC real 32,2%.
Fecha por construção: soma dos itens = total do cenário.
"""
import io, contextlib, pathlib
from collections import defaultdict

g = {}
with contextlib.redirect_stdout(io.StringIO()):
    exec((pathlib.Path(__file__).parent/'corte-apto-cj.py').read_text(encoding='utf-8'), g)

pecas, nest = g['pecas'], g['nest']
CH_AREA = g['CH_AREA']
LACA, LAMINA = g['LACA_M2'], g['LAMINA_M2']
FITA_LAM, FITA_FRJ, FILET = g['FITA_LAM_M'], g['FITA_FRJ_M'], g['FILETAGEM_M']
area_ripado, fita_ripas, n_ripas = g['area_ripado'], g['fita_ripas'], g['n_ripas']
P_SENSYS, P_QUADRO, P_ACTRO = g['P_SENSYS'], g['P_QUADRO_V6'], g['P_ACTRO']

# ─────────────────────────────────── base de chapa REAL [Jonathan]
P = {'SUB15':500.0, 'MEL15':500.0, 'MEL6':350.0,      # cor (Freijó Puro)
     'BRC15':300.0, 'BRC18':380.0, 'BRC6':200.0,      # branca (18 derivado)
     'RIPA15':82.0}                                    # MDF cru p/ receber lâmina
MELC = {'BRC15':500.0, 'BRC18':600.0, 'BRC6':350.0}   # se a peça virar melamínico NA COR
FITA_COR, FITA_BRC = 3.0, 2.0
A, B, C = 'A. Móvel entrada', 'B. Varanda/gourmet', 'C. Salas TV e jantar'

# peças aparentes da estante (viram "na cor" na versão 4; o resto vai branco TX)
EXT = {'C1 — laterais/divisórias verticais':2, 'C1 — tampo/base':4,
       'C1 — painel de TV (fundo aparente)':1,
       'C1 — prateleira acima TV (laca 3cm = 2x15mm colados)':2,
       'C1 — portas altas de abrir':2, 'C1 — gavetas inferiores: frentes':2,
       'C2 — laterais':2, 'C2 — tampo/base':2, 'C2 — caixilhos das portas de vidro':4,
       'C3 — laterais':2, 'C3 — tampo/base':2, 'C3 — fundo':1,
       'C3 — divisória dos nichos':1, 'C3 — prateleira dos nichos':1,
       'C3 — bancada/tampo intermediário':1, 'C3 — portas da base':2}

def chapa_custo(items, preco):
    """items: [(c,l)] → nº de chapas (nesting real) × preço."""
    return (nest(items) if items else 0) * preco

# ── agrupa peças por móvel/material
mv_mat = defaultdict(list)          # (movel, material) -> [(c,l)]
mv_area = defaultdict(float)
for mv, desc, mat, c, l, q in pecas:
    for _ in range(q):
        mv_mat[(mv, mat)].append((c, l))
        mv_area[(mv, mat)] += c*l/10000

def perim(mv, mats, frac):
    return sum(q*2*(c+l)/100 for m, d, mat, c, l, q in pecas if m == mv and mat in mats)*frac

# ═══════════════════════════════ A e B — versões de lâmina
def custo_AB(mv, versao):
    """versao 'lamina' | 'melaminico'. SUB15 é MDF melamínico Freijó Puro nas duas."""
    ch = sum(chapa_custo(mv_mat[(mv, m)], P[m]) for m in ('SUB15','MEL15','MEL6') if (mv, m) in mv_mat)
    area_ext = mv_area[(mv, 'SUB15')]                      # faces externas
    p_lam = perim(mv, ['SUB15'], 0.55)                     # bordas aparentes
    p_int = perim(mv, ['MEL15','MEL6'], 0.5)
    if mv == B:                                            # ripado só existe em B
        ch += chapa_custo([(65.0, 3.0)]*n_ripas, P['RIPA15'] if versao=='lamina' else P['MEL15'])
    if versao == 'lamina':
        acab = area_ext*LAMINA
        fita = p_lam*FITA_LAM + p_int*FITA_FRJ
        ml   = p_lam + p_int
        if mv == B:
            acab += area_ripado*3*LAMINA
            fita += fita_ripas*FITA_LAM
            ml   += fita_ripas
    else:
        acab = 0.0
        fita = (p_lam + p_int)*FITA_COR
        ml   = p_lam + p_int
        if mv == B:
            fita += fita_ripas*FITA_COR
            ml   += fita_ripas
    return ch + fita + ml*FILET + acab

# ═══════════════════════════════ C — versões da estante
def custo_C(versao):
    p_ext = perim(C, ['BRC15','BRC18','BRC6'], 0.5)
    if versao in ('laca_full', 'laca_ext'):
        ch = sum(chapa_custo(mv_mat[(C, m)], P[m]) for m in ('BRC15','BRC18','BRC6'))
        mult = 1.6 if versao == 'laca_full' else 1.0     # faces internas também lacadas?
        acab = mv_area[(C,'BRC15')]+mv_area[(C,'BRC18')]+mv_area[(C,'BRC6')]
        acab = acab*mult*LACA
        # laca_ext: interior em branco TX recebe fita branca
        fita = 0.0 if versao=='laca_full' else p_ext*0.6*FITA_BRC
        ml   = 0.0 if versao=='laca_full' else p_ext*0.6
        return ch + acab + fita + ml*FILET
    if versao == 'cor_full':
        ch = sum(chapa_custo(mv_mat[(C, m)], MELC[m]) for m in ('BRC15','BRC18','BRC6'))
        return ch + p_ext*(FITA_COR + FILET)
    # cor_ext: nesting SEPARADO por cor (cores não dividem chapa)
    ext, inte = defaultdict(list), defaultdict(list)
    pe = pi = 0.0
    for mv, desc, mat, c, l, q in pecas:
        if mv != C: continue
        n_e = min(EXT.get(desc, 0), q)
        for _ in range(n_e):   ext[mat].append((c,l)); pe += 2*(c+l)/100
        for _ in range(q-n_e): inte[mat].append((c,l)); pi += 2*(c+l)/100
    ch = sum(chapa_custo(ext[m], MELC[m]) + chapa_custo(inte[m], P[m])
             for m in ('BRC15','BRC18','BRC6'))
    return ch + pe*0.5*(FITA_COR+FILET) + pi*0.5*(FITA_BRC+FILET)

# ═══════════════════════════════ ferragens por móvel
ML_CAVA = {A: 238*2/100, B: (140+95.5)/100, C: 0.0}
FERR = {
    A: 2*2*P_SENSYS + 2*P_ACTRO + ML_CAVA[A]*g['P_PUX_CAVA_M'],
    B: (3*2+2*2)*P_SENSYS + ML_CAVA[B]*g['P_PUX_CAVA_M'],
    C: (2*4+4*3+2*3)*P_SENSYS + 2*P_QUADRO + 4*38.0 + 4*(1.41*0.33)*320.0,
}
GERAIS = g['logistica'] + g['visita']     # 1.300 — rateado por material
SERRA  = g['serralheria']                 # 600 — móvel D

# ═══════════════════════════════ monta a matriz
VA = {'v1 · lâmina natural': custo_AB(A,'lamina')+FERR[A], 'v2 · 100% melamínico': custo_AB(A,'melaminico')+FERR[A]}
VB = {'v1 · lâmina natural': custo_AB(B,'lamina')+FERR[B], 'v2 · 100% melamínico': custo_AB(B,'melaminico')+FERR[B]}
VC = {'v1 · laca completa': custo_C('laca_full')+FERR[C], 'v2 · laca ext + branco int': custo_C('laca_ext')+FERR[C],
      'v3 · melamínico na cor': custo_C('cor_full')+FERR[C], 'v4 · cor ext + branco int': custo_C('cor_ext')+FERR[C]}

base = VA['v1 · lâmina natural'] + VB['v1 · lâmina natural'] + VC['v1 · laca completa']
def rat(cm): return GERAIS * cm/base                       # rateio dos gerais

fixedR1 = base + GERAIS + SERRA
inv1    = g['inv']                                          # 84.530,93 — entregue
div     = fixedR1/inv1
MC      = 1 - 0.182 - 0.86*0.043 - div
def pr(c): return c/div

print('═'*88)
print(f'APTO CJ — CUSTO E PREÇO POR ITEM   ·   divisor {div:.5f}  →  MC {MC*100:.1f}%')
print(f'(opção 1 honrada em R$ 84.600 · custo direto real R$ {fixedR1:,.2f})')
print('═'*88)
print(f'{"MÓVEL / VERSÃO":<42}{"CUSTO":>12}{"PREÇO":>13}{"À VISTA":>12}')
print('─'*88)
for nome, versoes in ((A, VA), (B, VB), (C, VC)):
    print(f'{nome}')
    for v, cm in versoes.items():
        cd = cm + rat(cm)
        print(f'   {v:<39}{cd:>12,.2f}{pr(cd):>13,.2f}{pr(cd)*0.9:>12,.2f}')
cd_D = SERRA
print(f'D. Adega (serralheria)')
print(f'   {"versão única":<39}{cd_D:>12,.2f}{pr(cd_D):>13,.2f}{pr(cd_D)*0.9:>12,.2f}')

# ═══════════════════════════════ conferência: soma dos itens = cenário
CEN = [('1 Integral',            'v1 · lâmina natural','v1 · lâmina natural','v1 · laca completa'),
       ('2 A+B melamínico',      'v2 · 100% melamínico','v2 · 100% melamínico','v1 · laca completa'),
       ('3 Estante laca ext',    'v1 · lâmina natural','v1 · lâmina natural','v2 · laca ext + branco int'),
       ('4 Estante cor inteira', 'v1 · lâmina natural','v1 · lâmina natural','v3 · melamínico na cor'),
       ('5 Estante cor+branco',  'v1 · lâmina natural','v1 · lâmina natural','v4 · cor ext + branco int'),
       ('6 Tudo melamínico',     'v2 · 100% melamínico','v2 · 100% melamínico','v4 · cor ext + branco int')]
print('\n' + '═'*88)
print('CONFERÊNCIA — soma dos itens por cenário')
print('═'*88)
print(f'{"CENÁRIO":<26}{"CUSTO":>12}{"PREÇO":>13}{"À VISTA":>12}{"apresentado":>16}')
print('─'*88)
APRES = {'1':(84600,76100), '2':(73100,65800), '3':(67400,60600),
         '4':(44100,39700), '5':(43200,38900), '6':(31700,28600)}
for nome, va, vb, vc in CEN:
    cm = VA[va] + VB[vb] + VC[vc]
    cd = cm + GERAIS*cm/base + SERRA
    p  = pr(cd)
    ap = APRES[nome[0]]
    print(f'{nome:<26}{cd:>12,.2f}{p:>13,.2f}{p*0.9:>12,.2f}'
          f'{ap[0]:>10,.0f}/{ap[1]:,.0f}')
