# -*- coding: utf-8 -*-
"""Confere que as duas abas são a MESMA aba, traduzindo cada mesclagem e
cada regra condicional para o NOME do seu lugar no layout. ⭐ Comparar
número de linha não serve: as abas têm tamanhos diferentes de propósito."""
import json, sys
COL = 'ABCDEFGHIJK'
LIV = json.load(open('_aba-living.json'))['layout']
COZ = json.load(open('_aba-cozinha.json'))['layout']

MERGES = {
 'living': [(16,1,8),(19,3,7),(38,1,7),(39,1,7),(161,2,8),(162,2,8),(163,2,8),
   (0,1,8),(1,1,8),(3,1,8),(34,1,8),(41,1,8),(159,1,8),(14,2,8),(20,3,7),
   (21,3,7),(22,3,7),(23,3,7),(24,3,7),(25,3,7),(26,3,7),(28,1,7),(29,1,7),
   (30,1,7),(31,1,7),(32,1,7),(36,1,7),(37,1,7)],
 'cozinha': [(17,1,8),(20,3,7),(21,3,7),(22,3,7),(24,1,7),(25,1,7),(26,1,7),
   (27,1,7),(30,1,8),(32,1,7),(33,1,7),(34,1,7),(124,2,8),(125,2,8),(126,2,8),
   (127,2,8),(0,1,8),(1,1,8),(3,1,8),(36,1,8),(122,1,8),(15,2,8),(28,1,7)],
}
COND = {   # (fórmula normalizada, primeira linha 1-based da faixa)
 'living': [('ARRED(I)<>0',33),('ITEM ',44),('MATERIAL',44),('TOTAL',44),('vazio',44)],
 'cozinha':[('ARRED(I)<>0',29),('ITEM ',39),('MATERIAL',39),('TOTAL',39),('vazio',39)],
}

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
        alvo = L['f0']+4 if f.startswith('ARRED') else L['blk0']
        if r != alvo:
            print(f'⛔ {ab}: regra "{f}" ancorada em {r}, devia ser {alvo}'); falhas += 1
if [f for f, _ in COND['living']] != [f for f, _ in COND['cozinha']]:
    print('⛔ as duas abas não têm o mesmo conjunto de regras'); falhas += 1

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
