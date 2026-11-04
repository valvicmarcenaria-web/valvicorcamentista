# -*- coding: utf-8 -*-
"""Confere que as duas abas são a MESMA aba, traduzindo cada mesclagem e
cada regra condicional para o NOME do seu lugar no layout. ⭐ Comparar
número de linha não serve: as abas têm tamanhos diferentes de propósito."""
import json, sys, re
COL = 'ABCDEFGHIJK'
LIV = json.load(open('_aba-living.json'))['layout']
COZ = json.load(open('_aba-cozinha.json'))['layout']

# ⭐⭐ As mesclagens e as regras saem do GERADOR, não de uma lista digitada
#   aqui. A primeira versão deste arquivo trazia as duas listas à mão, e
#   isso é o mesmo vício que fez as abas divergirem: duas fontes para a
#   mesma verdade. Agora, se o gerador mudar, a conferência acompanha.
def do_req(nome):
    q = json.load(open(f'_req-{nome}.json'))
    m, c = [], []
    for r in q:
        if 'mergeCells' in r:
            g = r['mergeCells']['range']
            m.append((g['startRowIndex'], g['startColumnIndex'],
                      g['endColumnIndex']-1))
        elif 'addConditionalFormatRule' in r:
            ru = r['addConditionalFormatRule']['rule']
            f = ru['booleanRule']['condition']['values'][0]['userEnteredValue']
            c.append((f, ru['ranges'][0]['startRowIndex']+1))
    return m, c
MERGES, COND = {}, {}
for _n in ('living', 'cozinha'):
    MERGES[_n], COND[_n] = do_req(_n)



def papel(L, r):
    """Que lugar do layout é a linha r (1-based)."""
    if r == L['tit']: return 'TÍTULO'
    if r == L['sub']: return 'SUBTÍTULO'
    for s, n in (('s_amb','§AMBIENTE'),('s_itens','§ITENS'),('s_ni','§NÃO-MARC'),
                 ('s_pec','§PEÇAS'),('s_nt','§NOTAS')):
        if r == L[s]: return n
    if r == L['nota']: return 'NOTA DO PAINEL'
    if L['it0'] <= r <= L['it1']: return f"ITEM {r-L['it0']+1}"
    if L['f0']  <= r <= L['f1']:  return f"FECHAMENTO {r-L['f0']+1}"
    if L['ni0'] <= r <= L['ni1']: return f"NÃO-MARC {r-L['ni0']+1}"
    if L['nt0'] <= r <= L['nt1']: return f"NOTA {r-L['nt0']+1}"
    return f'⛔ LINHA SOLTA {r}'

falhas = 0
mapas = {}
for ab, L in (('living', LIV), ('cozinha', COZ)):
    m = {}
    for r0, c0, c1 in MERGES[ab]:
        p = papel(L, r0+1)
        if p.startswith('⛔'): print(f'⛔ {ab}: mesclagem em linha sem papel: {p}'); falhas += 1
        m[p] = f'{COL[c0]}:{COL[c1]}'
    mapas[ab] = m
    # cada lugar que DEVE existir
    esperado = ['TÍTULO','SUBTÍTULO','§AMBIENTE','§ITENS','§NÃO-MARC','§PEÇAS',
                '§NOTAS','NOTA DO PAINEL'] + \
               [f'ITEM {i}' for i in range(1, L['it1']-L['it0']+2)] + \
               [f'FECHAMENTO {i}' for i in range(1, 6)] + \
               [f'NÃO-MARC {i}' for i in range(1, L['ni1']-L['ni0']+2)] + \
               [f'NOTA {i}' for i in range(1, L['nt1']-L['nt0']+2)]
    for p in esperado:
        if p not in m: print(f'⛔ {ab}: falta mesclagem em {p}'); falhas += 1
    for p in m:
        if p not in esperado: print(f'⛔ {ab}: mesclagem a mais em {p}'); falhas += 1

# ── o teste que importa: o MESMO papel tem a MESMA extensão nas duas ────
tipos = lambda m: {p.rstrip('0123456789 ') or p: v for p, v in sorted(m.items())}
a, b = tipos(mapas['living']), tipos(mapas['cozinha'])
for p in sorted(set(a) | set(b)):
    if a.get(p) != b.get(p):
        print(f'⛔ {p}: Living {a.get(p)} × Cozinha {b.get(p)}'); falhas += 1

# ── condicionais: mesma regra, ancorada no blk0 de cada aba ─────────────
for ab, L in (('living', LIV), ('cozinha', COZ)):
    for f, r in COND[ab]:
        alvo = L['f0']+4 if 'ROUND' in f else L['blk0']
        if r != alvo:
            print(f'⛔ {ab}: regra "{f}" ancorada em {r}, devia ser {alvo}'); falhas += 1
# ⭐ as regras têm de ser as MESMAS nas duas, a menos do número de linha
anon = lambda ab: sorted(re.sub(r'\$?[A-K]\$?\d+', 'X', f)
                         for f, _ in COND[ab])
if anon('living') != anon('cozinha'):
    print('⛔ as duas abas não têm o mesmo conjunto de regras')
    print('   Living :', anon('living')); print('   Cozinha:', anon('cozinha'))
    falhas += 1

W = 72; print('═'*W)
print('CONFERÊNCIA DE FORMA · as duas abas são a mesma aba?'); print('═'*W)
for p in sorted(a): print(f'   {p:22} {a[p]}')
print(f'\n   Living  {len(mapas["living"])} mesclagens · {len(COND["living"])} regras · '
      f'{LIV["it1"]-LIV["it0"]+1} itens · fim na linha {LIV["fim"]}')
print(f'   Cozinha {len(mapas["cozinha"])} mesclagens · {len(COND["cozinha"])} regras · '
      f'{COZ["it1"]-COZ["it0"]+1} itens · fim na linha {COZ["fim"]}')
print()
if falhas: print(f'⛔⛔ {falhas} DIVERGÊNCIAS'); sys.exit(1)
print('✓ mesma forma nas duas: cada papel do layout com a mesma extensão,')
print('  as mesmas cinco regras, ancoradas no bloco de cada uma.')
