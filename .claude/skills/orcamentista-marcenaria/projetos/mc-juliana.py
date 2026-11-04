# -*- coding: utf-8 -*-
"""MC conferida das três linhas da Juliana & Kairon, direto dos JSONs.

Lê orcamento-juliana-{gold,essencial,telescopica}.json, soma material pela
biblioteca de preços do próprio arquivo, soma os terceirizados/logística e
confere a margem contra os preços de venda dos builds v2/v3.

  MC = BASE - custo/preco        BASE = 1 - 0,162 - 0,88*0,043 = 0,80016

A mesa de refeições (R$ 2.350 nas duas colunas) NÃO entra: ela é venda sem
linha de custo lançada — ver "em aberto" no dossiê.
"""
import json, pathlib
P = pathlib.Path(__file__).resolve().parent
A_, LIQF_, B_ = 0.162, 0.88, 0.043
BASE = 1 - A_ - LIQF_*B_

# preços de venda por ambiente (build-juliana-v2.py / v3.py), sem a mesa
VENDA = {
    'gold':        {'Cozinha': 21900, 'Quarto de casal': 18700, 'Closet': 31304},
    'essencial':   {'Cozinha': 19300, 'Quarto de casal': 16500, 'Closet': 25121},
    'telescopica': {'Cozinha': 18800, 'Quarto de casal': 14400, 'Closet': 26400},
}

def custos(arq):
    d = json.load(open(P/arq, encoding='utf-8'))
    preco = {cat: dict(itens) for cat, itens in d['lib']}
    out = {}
    for a in d['ambientes']:
        mat = 0.0
        for chave, qt in a.get('q', {}).items():
            cat, item = chave.split('¦')
            mat += preco[cat][item] * qt
        terc = sum(a.get('terc', {}).values())
        out[a['nome']] = (mat, terc, mat + terc)
    return out

def brl(v): return f'{v:,.0f}'.replace(',', '.')

print(f'{"linha":<12} {"ambiente":<16} {"material":>10} {"terc/log":>9} '
      f'{"CD":>10} {"venda":>10} {"MC":>7}')
print('-'*70)
geral = {}
for linha in ('gold', 'essencial', 'telescopica'):
    c = custos(f'orcamento-juliana-{linha}.json')
    tcd = tv = 0
    for amb, pv in VENDA[linha].items():
        mat, terc, cd = c[amb]
        tcd += cd; tv += pv
        print(f'{linha:<12} {amb:<16} {brl(mat):>10} {brl(terc):>9} '
              f'{brl(cd):>10} {brl(pv):>10} {BASE-cd/pv:>6.1%}')
    geral[linha] = (tcd, tv)
    print(f'{"":<12} {"3 ambientes":<16} {"":>10} {"":>9} '
          f'{brl(tcd):>10} {brl(tv):>10} {BASE-tcd/tv:>6.1%}')
    print('-'*70)
