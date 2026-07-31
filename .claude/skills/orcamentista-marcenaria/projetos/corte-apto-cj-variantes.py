# -*- coding: utf-8 -*-
"""
APTO CJ — VARIANTES DE PRODUTO para o folder comparativo [Jonathan 28/07]
Roda o corte original (exec) e recalcula 5 configurações com o MESMO motor:

  1. INTEGRAL — como orçado (lâmina natural + laca completa). Valores intocados.
  2. Móveis de lâmina natural (entrada + gourmet) em MDF MELAMÍNICO (freijó padrão).
  3. Estante das salas: LACA só nas faces externas · interno em MDF BRANCO TX.
  4. Estante das salas: SEM laca — MELAMÍNICO NA COR por inteiro (ext + int).
  5. Estante das salas: SEM laca — MELAMÍNICO NA COR externo · BRANCO TX interno.

"Estante" = móvel C (salas TV e jantar, 636 × 232 — painel, cristaleira, nichos).
As opções 2 e 3–5 mexem em móveis DIFERENTES (A+B vs C) → economias combináveis.
"""
import io, contextlib, pathlib

SRC = pathlib.Path(__file__).parent / 'corte-apto-cj.py'
g = {}
with contextlib.redirect_stdout(io.StringIO()):
    exec(SRC.read_text(encoding='utf-8'), g)

# ── baseline
mat0     = g['mat_total']
fixo     = g['logistica'] + g['visita'] + g['serralheria']
div      = g['divisor']
inv1     = g['inv']
LACA     = g['LACA_M2']            # 300
LAMINA_C = g['custo_lamina']       # 4.781,90
area_laca      = g['area_laca']    # 1 face de todas as peças BRC
custo_laca     = g['custo_laca']   # area_laca*1.6*300
fita_lam, fita_ripas = g['fita_lam'], g['fita_ripas']
fita_cru = g['fita_cru']           # m de borda BRC visível (0.5 do perímetro)
FILET    = g['FILETAGEM_M']        # 2.5
chapas   = g['chapas_por_mat']     # por material
nest, pecas, P = g['nest'], g['pecas'], g['P']

FITA_COR, FITA_BRC = 3.0, 2.0
MELC = {'15': 180.0, '18': 220.0, '6': 130.0}   # melamínico NA COR, linha do projeto
                                                 # (15 = mesma ref. MEL15; 18/6 proporcionais)

def preco(mat_total):
    inv = (mat_total + fixo) / div
    return inv, inv * 0.90

def r100(v):                        # apresentação em valores cheios
    return round(v / 100) * 100

# ═════════════════ OPÇÃO 2 — lâmina natural → melamínico (móveis A+B)
d_lamina = -LAMINA_C                                  # serviço de lâmina sai inteiro
d_fita   = (fita_lam + fita_ripas) * (FITA_COR - 12.0)  # bordo lâmina → fita cor
d_ripa   = 1 * (P['MEL15'] - P['RIPA15'])             # ripas: cru → melamínico
mat2 = mat0 + d_lamina + d_fita + d_ripa
inv2, av2 = preco(mat2)

# ═════════════════ OPÇÃO 3 — estante: laca externa · interno branco TX
d_laca3  = -(0.6 * area_laca) * LACA                  # 1.6x → 1.0x (só faces externas)
d_fita3  = fita_cru * 0.6 * (FITA_BRC + FILET)        # bordas internas: fita branca
mat3 = mat0 + d_laca3 + d_fita3
inv3, av3 = preco(mat3)

# ═════════════════ classificação ext/int das peças da estante (p/ opções 4 e 5)
EXT = {  # peça aparente → NA COR na opção 5
    'C1 — laterais/divisórias verticais': 2,   # 2 das 4 são laterais externas
    'C1 — tampo/base': 4, 'C1 — painel de TV (fundo aparente)': 1,
    'C1 — prateleira acima TV (laca 3cm = 2x15mm colados)': 2,
    'C1 — portas altas de abrir': 2, 'C1 — gavetas inferiores: frentes': 2,
    'C2 — laterais': 2, 'C2 — tampo/base': 2, 'C2 — caixilhos das portas de vidro': 4,
    'C3 — laterais': 2, 'C3 — tampo/base': 2, 'C3 — fundo': 1,          # nichos abertos
    'C3 — divisória dos nichos': 1, 'C3 — prateleira dos nichos': 1,
    'C3 — bancada/tampo intermediário': 1, 'C3 — portas da base': 2,
}
ext_pcs, int_pcs = {'15': [], '18': [], '6': []}, {'15': [], '18': [], '6': []}
per_ext = per_int = 0.0
for mv, desc, mat, c, l, q in pecas:
    if not mat.startswith('BRC'):
        continue
    th = mat[3:]
    n_ext = min(EXT.get(desc, 0), q)
    for _ in range(n_ext):
        ext_pcs[th].append((c, l)); per_ext += 2 * (c + l) / 100
    for _ in range(q - n_ext):
        int_pcs[th].append((c, l)); per_int += 2 * (c + l) / 100

# ═════════════════ OPÇÃO 4 — estante toda em melamínico NA COR
d_laca4  = -custo_laca
d_chapa4 = sum(chapas[f'BRC{t}'] * (MELC[t] - P[f'BRC{t}']) for t in ('15', '18', '6'))
d_fita4  = fita_cru * (FITA_COR + FILET)              # bordas: fita cor (antes lacadas)
mat4 = mat0 + d_laca4 + d_chapa4 + d_fita4
inv4, av4 = preco(mat4)

# ═════════════════ OPÇÃO 5 — estante: externo NA COR · interno BRANCO TX
# nesting separado por cor (cores não dividem chapa — custo real da mistura)
d_laca5  = -custo_laca
chapa5 = 0.0
det5 = []
for t in ('15', '18', '6'):
    n_e = nest(ext_pcs[t]) if ext_pcs[t] else 0
    n_i = nest(int_pcs[t]) if int_pcs[t] else 0
    chapa5 += n_e * MELC[t] + n_i * P[f'BRC{t}']
    det5.append((t, n_e, n_i))
chapa0_BRC = sum(chapas[f'BRC{t}'] * P[f'BRC{t}'] for t in ('15', '18', '6'))
d_chapa5 = chapa5 - chapa0_BRC
d_fita5  = (per_ext * 0.5) * (FITA_COR + FILET) + (per_int * 0.5) * (FITA_BRC + FILET)
mat5 = mat0 + d_laca5 + d_chapa5 + d_fita5
inv5, av5 = preco(mat5)

# ═════════════════ RELATÓRIO
print('═' * 78)
print('APTO CJ — TABELA COMPARATIVA DE PRODUTO   (divisor 0,41102 · MC 37% · sem RT)')
print('═' * 78)
OPTS = [
    ('1. INTEGRAL — lâmina natural + laca completa (como o projeto pede)', inv1),
    ('2. Entrada + gourmet em melamínico (sem lâmina natural)',            inv2),
    ('3. Estante: laca externa · interno branco TX',                       inv3),
    ('4. Estante: sem laca — melamínico na cor (ext + int)',               inv4),
    ('5. Estante: sem laca — cor externo · branco interno',                inv5),
]
for nome, inv in OPTS:
    econ = inv1 - inv
    print(f'  {nome}')
    print(f'      parcelado R$ {r100(inv):>7,.0f}   ·   à vista R$ {r100(inv*0.9):>7,.0f}'
          + (f'   ·   economia R$ {r100(econ):>6,.0f}' if econ > 1 else '   ·   —'))
print()
print('  Deltas de custo (auditoria):')
print(f'    op2: lâmina {-LAMINA_C:+,.0f} · fita {(fita_lam+fita_ripas)*(FITA_COR-12):+,.0f} '
      f'· chapa ripa {1*(P["MEL15"]-P["RIPA15"]):+,.0f}')
print(f'    op3: laca {d_laca3:+,.0f} · fita branca int {d_fita3:+,.0f}')
print(f'    op4: laca {d_laca4:+,.0f} · chapas {d_chapa4:+,.0f} · fita cor {d_fita4:+,.0f}')
print(f'    op5: laca {d_laca5:+,.0f} · chapas {d_chapa5:+,.0f} · fita {d_fita5:+,.0f}')
print(f'    op5 nesting por cor (15/18/6): ' +
      ' · '.join(f'{t}mm ext {e} + int {i}' for t, e, i in det5))
print(f'\n  Economias combináveis: op2 + op5 → R$ {r100((inv1-inv2)+(inv1-inv5)):,.0f} '
      f'(mexem em móveis diferentes)')

# ═════════════════ OPÇÃO 6 — projeto 100% MELAMÍNICO (sem lâmina, sem laca)
# Combinação das alavancas: A+B como na op2 · estante como na op5 (cor fora,
# branco TX dentro). Deltas independentes — móveis diferentes, mesmo divisor.
mat6 = mat0 + (d_lamina + d_fita + d_ripa) + (d_laca5 + d_chapa5 + d_fita5)
inv6, av6 = preco(mat6)
print('\n  6. PROJETO 100% MELAMÍNICO — sem lâmina, sem laca (op2 + op5)')
print(f'      parcelado R$ {r100(inv6):>7,.0f}   ·   à vista R$ {r100(inv6*0.9):>7,.0f}'
      f'   ·   economia R$ {r100(inv1-inv6):>6,.0f}')
print(f'      exato: inv {inv6:,.2f} · à vista {inv6*0.9:,.2f} · mat {mat6:,.2f}')
print(f'      variação se a estante for TODA na cor (op4 no lugar da op5): '
      f'+R$ {(mat4-mat5)/div:,.0f}')
