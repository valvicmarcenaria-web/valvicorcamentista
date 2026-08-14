# -*- coding: utf-8 -*-
"""ELIUTON · Residência Brisas da Pampulha — MOTOR DE LEVANTAMENTO E PREÇO.

⛔ ESQUELETO. A lista `pecas` está VAZIA — as pranchas ainda não foram lidas.
   Ver `2026-eliuton-brisas-da-pampulha.md` (o bloqueio) e
   `2026-eliuton-duvidas-tecnicas.md` (o que precisa ser respondido antes).

[Jonathan 13/08/2026] TRÊS CENÁRIOS DE FERRAGEM, cada um com a sua MC:
     simples (telescópica) 32% · intermediária (Hettich) 37% · top (Blum) 42%
   E: **toda parte com RIPADO sai a MC 40%**, em qualquer cenário.

O ripado tem MC própria, então o preço NÃO é um divisor único sobre o custo total:
é a soma de duas parcelas — a de ripado no seu divisor, e o resto no divisor do
cenário. É por isso que `preco()` separa `custo_ripado` de `custo_resto`.

⚠️ No cenário 3 o ripado (40%) sai MAIS BARATO que o resto (42%). Nos cenários 1 e 2
   sai mais caro. Está na lista de dúvidas (E2) para o Jonathan confirmar.
"""
from collections import defaultdict

CH_C, CH_L = 275.0, 185.0
CH_AREA = 2.75 * 1.85                       # 5,0875 m²

# ── motor comercial ────────────────────────────────────────────────────────
A_, LIQF_, B_ = 0.162, 0.88, 0.043          # conjunto SEM RT
BASE = 1 - A_ - LIQF_*B_                    # 0,80016
RT_PCT = 0.10                               # se houver RT: subtrair LIQF_*RT_PCT

MC_RIPADO = 0.40                            # [Jonathan] vale nos três cenários
CENARIOS = [
    ('Simples',       'Corrediça telescópica',      0.32),
    ('Intermediária', 'Hettich',                    0.37),
    ('Top de linha',  'Blum',                       0.42),
]

def div(mc, rt=False):
    return BASE - mc - (LIQF_*RT_PCT if rt else 0.0)

def preco(custo_resto, custo_ripado, mc, rt=False):
    """Duas parcelas: o ripado no divisor dele, o resto no divisor do cenário."""
    return custo_resto/div(mc, rt) + custo_ripado/div(MC_RIPADO, rt)

def mc_conferida(preco_total, custo_total):
    return BASE - custo_total/preco_total

# ── nesting da casa (dois empacotadores × quatro ordens) ───────────────────
# Ver referencias/quantitativo.md. O de faixa corrente só tenta a ÚLTIMA faixa
# aberta e abandona a sobra das anteriores; o best-fit procura a melhor faixa já
# aberta em qualquer chapa. Rodar os dois e ficar com o mínimo.
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
    ch = []                    # ch[i] = [altura_usada, [[alt_faixa, sobra_larg], ...]]
    for c, l in pcs:
        if c > CH_C and l <= CH_C: c, l = l, c
        if c > CH_C or l > CH_L: ch.append([CH_L, []]); continue
        best = None
        for s in ch:
            for fx in s[1]:
                if fx[0] >= l and fx[1] >= c and (best is None or fx[1] < best[1]):
                    best = fx
        if best is not None: best[1] -= c; continue
        for s in ch:
            if s[0] + l <= CH_L:
                s[0] += l; s[1].append([l, CH_C - c]); break
        else:
            ch.append([l, [[l, CH_C - c]]])
    return len(ch)

def nest(items):
    if not items: return 0
    base = [(max(c, l), min(c, l)) for c, l in items]
    ordens = [lambda p: -p[1], lambda p: (-p[1], -p[0]),
              lambda p: -p[0], lambda p: -p[0]*p[1]]
    chapas = min(pk(sorted(base, key=k))
                 for pk in (_pack_faixa, _pack_bf) for k in ordens)
    area = sum(c*l for c, l in items)/10000
    return max(chapas, -(-int(area/(CH_AREA*0.80)*1000)//1000) or 1)

# ── peças: (material, ambiente, descrição, comprimento, largura, qtd, ripado?)
# ⛔ VAZIO — aguardando as pranchas PR 01–05 COZINHA e PR 06–07 A. GOURMET.
pecas = []

# ── quando houver peças, o resto do motor já roda ──────────────────────────
if not pecas:
    print('═'*78)
    print('ELIUTON · Brisas da Pampulha — MOTOR PRONTO, SEM GEOMETRIA')
    print('═'*78)
    print('\nA lista `pecas` está vazia: as pranchas ainda não foram lidas.')
    print('Faltam no chat: PR 01 a PR 05 COZINHA · PR 06 e PR 07 A. GOURMET.\n')
    print('DIVISORES JÁ CALIBRADOS  (a=0,162 · liqF=0,88 · b=0,043 · SEM RT)')
    print(f'  {"cenário":<16}{"ferragem":<24}{"MC":>5}{"divisor":>11}{"×custo":>9}')
    for nome, ferr, mc in CENARIOS:
        d = div(mc)
        print(f'  {nome:<16}{ferr:<24}{mc*100:>4.0f}%{d:>11.5f}{1/d:>9.3f}')
    d = div(MC_RIPADO)
    print(f'  {"RIPADO":<16}{"(vale nos três)":<24}{MC_RIPADO*100:>4.0f}%'
          f'{d:>11.5f}{1/d:>9.3f}')
    print('\n  COM RT 10% os divisores caem para:')
    for nome, _, mc in CENARIOS:
        print(f'    {nome:<16}{div(mc, True):.5f}   (+{(div(mc)/div(mc,True)-1)*100:.0f}% no preço)')
    print('\n⚠ Cenário 3: o ripado (40%) sai MAIS BARATO que o resto (42%).')
    print('  Nos cenários 1 e 2 sai mais caro. Confirmar com o Jonathan (dúvida E2).')
    raise SystemExit(0)

# ── daqui para baixo só roda com geometria ─────────────────────────────────
por_mat, area_mat = defaultdict(list), defaultdict(float)
for mat, amb, desc, c, l, q, rip in pecas:
    for _ in range(q):
        por_mat[mat].append((c, l))
        area_mat[mat] += c*l/10000
CHAPAS = {m: nest(v) for m, v in por_mat.items()}
