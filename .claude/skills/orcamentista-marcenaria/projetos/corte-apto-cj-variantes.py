# -*- coding: utf-8 -*-
"""
APTO CJ — VARIANTES DE PRODUTO · BASE DE CHAPA CORRIGIDA [Jonathan 28/07]

Preços REAIS de chapa (Jonathan): branca 15mm R$ 300 · branca 6mm R$ 200 ·
cor 15mm R$ 500 · cor 6mm R$ 350. 18mm DERIVADOS (confirmar): branca 380 · cor 600.
O corte original usava 108/78/180/130 — barato demais; os cenários intensivos em
chapa estavam subprecificados.

DECISÃO DE ANCORAGEM (padrão deste script):
  A opção 1 JÁ FOI ENTREGUE ao cliente por R$ 84.600 / 76.100 — fica HONRADA.
  Com o custo real de chapa, esse preço carrega MC ~32% (não 37%). O menu inteiro
  é recalculado com o MESMO divisor calibrado → margem uniforme e economias coerentes.
  Alternativa (reancorar tudo em MC 37%): tabela impressa ao final.
"""
import io, contextlib, pathlib

SRC = pathlib.Path(__file__).parent / 'corte-apto-cj.py'
g = {}
with contextlib.redirect_stdout(io.StringIO()):
    exec(SRC.read_text(encoding='utf-8'), g)

mat0_old = g['mat_total']
fixo     = g['logistica'] + g['visita'] + g['serralheria']
div37    = g['divisor']              # 0,41102 — MC 37%
inv1     = g['inv']                  # 84.530,93 → entregue como 84.600
LACA     = g['LACA_M2']
LAMINA_C = g['custo_lamina']
area_laca = g['area_laca']
custo_laca = g['custo_laca']
fita_lam, fita_ripas, fita_cru = g['fita_lam'], g['fita_ripas'], g['fita_cru']
FILET = g['FILETAGEM_M']
chapas = g['chapas_por_mat']         # SUB15/MEL15/MEL6/BRC15/BRC18/BRC6
nest, pecas, P_OLD = g['nest'], g['pecas'], g['P']
a_, liqF_, b_ = 0.182, 0.86, 0.043

# ══════════════════════ BASE NOVA DE CHAPA [Jonathan 28/07]
P_NEW = {
    'SUB15': 500.0, 'MEL15': 500.0,   # cor 15 (Freijó Puro)
    'MEL6':  350.0,                    # cor 6
    'BRC15': 300.0, 'BRC6': 200.0,     # branca 15 / 6
    'BRC18': 380.0,                    # DERIVADO de 300 (confirmar)
    'RIPA15': 82.0,                    # MDF cru (recebe lâmina) — inalterado
}
MELC = {'15': 500.0, '18': 600.0, '6': 350.0}   # melamínico NA COR (18 derivado)
FITA_COR, FITA_BRC = 3.0, 2.0

d_int = sum(chapas[m] * (P_NEW[m] - P_OLD[m]) for m in chapas)
fixedR1 = mat0_old + d_int + fixo               # custo real da opção 1
div = fixedR1 / inv1                            # divisor CALIBRADO p/ honrar 84.600
MC_real = 1 - a_ - liqF_*b_ - div

def preco(fixedR): return fixedR/div, fixedR/div*0.9
def r100(v): return round(v/100)*100

# ── deltas de CUSTO por alavanca (base nova)
d2 = -LAMINA_C + (fita_lam+fita_ripas)*(FITA_COR-12.0) + 1*(P_NEW['MEL15']-P_NEW['RIPA15'])
d3 = -(0.6*area_laca)*LACA + fita_cru*0.6*(FITA_BRC+FILET)
d4_ch = sum(chapas[f'BRC{t}'] * (MELC[t]-P_NEW[f'BRC{t}']) for t in ('15','18','6'))
d4 = -custo_laca + d4_ch + fita_cru*(FITA_COR+FILET)

EXT = {
    'C1 — laterais/divisórias verticais': 2, 'C1 — tampo/base': 4,
    'C1 — painel de TV (fundo aparente)': 1,
    'C1 — prateleira acima TV (laca 3cm = 2x15mm colados)': 2,
    'C1 — portas altas de abrir': 2, 'C1 — gavetas inferiores: frentes': 2,
    'C2 — laterais': 2, 'C2 — tampo/base': 2, 'C2 — caixilhos das portas de vidro': 4,
    'C3 — laterais': 2, 'C3 — tampo/base': 2, 'C3 — fundo': 1,
    'C3 — divisória dos nichos': 1, 'C3 — prateleira dos nichos': 1,
    'C3 — bancada/tampo intermediário': 1, 'C3 — portas da base': 2,
}
ext_pcs, int_pcs = {'15':[], '18':[], '6':[]}, {'15':[], '18':[], '6':[]}
per_ext = per_int = 0.0
for mv, desc, mat, c, l, q in pecas:
    if not mat.startswith('BRC'): continue
    t = mat[3:]
    n_e = min(EXT.get(desc, 0), q)
    for _ in range(n_e):   ext_pcs[t].append((c,l)); per_ext += 2*(c+l)/100
    for _ in range(q-n_e): int_pcs[t].append((c,l)); per_int += 2*(c+l)/100
chapa5 = sum((nest(ext_pcs[t]) if ext_pcs[t] else 0)*MELC[t]
             + (nest(int_pcs[t]) if int_pcs[t] else 0)*P_NEW[f'BRC{t}'] for t in ('15','18','6'))
chapa0 = sum(chapas[f'BRC{t}']*P_NEW[f'BRC{t}'] for t in ('15','18','6'))
d5 = -custo_laca + (chapa5-chapa0) + (per_ext*0.5)*(FITA_COR+FILET) + (per_int*0.5)*(FITA_BRC+FILET)
d6 = d2 + d5

print('═'*78)
print('APTO CJ — MENU COM BASE DE CHAPA CORRIGIDA')
print(f'  Δ custo de chapa na opção 1: +R$ {d_int:,.2f}  →  custo real R$ {fixedR1:,.2f}')
print(f'  Opção 1 HONRADA em R$ 84.600 → divisor calibrado {div:.5f} → MC real {MC_real*100:.1f}%')
print('═'*78)
OPTS = [
    ('1. INTEGRAL — lâmina + laca (entregue; honrada)', 0.0),
    ('2. Entrada + varanda 100% melamínico Freijó Puro', d2),
    ('3. Estante: laca externa · interno branco TX',     d3),
    ('4. Estante sem laca — melamínico na cor, inteira', d4),
    ('5. Estante sem laca — cor fora · branco dentro',   d5),
    ('6. Projeto 100% melamínico (2 + 5)',               d6),
]
for nome, d in OPTS:
    inv, av = preco(fixedR1 + d)
    econ = 84600 - r100(inv) if d else 0
    print(f'  {nome}')
    print(f'      parcelado R$ {r100(inv):>7,.0f} (exato {inv:,.0f})  ·  à vista R$ {r100(av):>7,.0f}'
          + (f'  ·  economia R$ {econ:,.0f}' if d else '  ·  —'))

print('\n  Aditividade (apresentação): op2+op5−op1 = '
      f'{r100(preco(fixedR1+d2)[0]) + r100(preco(fixedR1+d5)[0]) - 84600:,.0f} '
      f'vs op6 = {r100(preco(fixedR1+d6)[0]):,.0f}')

print('\n' + '─'*78)
print('  ALTERNATIVA — reancorar TUDO em MC 37% (base nova, divisor 0,41102):')
for nome, d in OPTS:
    inv = (fixedR1 + d)/div37
    print(f'    {nome:<52} R$ {r100(inv):>8,.0f} · à vista R$ {r100(inv*.9):>8,.0f}')
