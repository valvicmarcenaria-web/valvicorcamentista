# -*- coding: utf-8 -*-
"""Detalhe de um ambiente, móvel a móvel.  uso: LINHA=hettich python3 detalhe.py 'Quarto casal'"""
import sys, importlib
import motor as M
from resumo import AMBS
for a in AMBS: importlib.import_module(a)
R = M.calcula(600.0)
m2 = {k: R['chapas'][k] * M.preco_chapa(k) / R['area'][k] for k in R['area']}
alvo = sys.argv[1]
mv = {}
for p in M.pecas:
    if p['amb'] != alvo: continue
    d = mv.setdefault(p['movel'], {'mdf': 0, 'fita': 0, 'itens': [], 'pecas': 0})
    a = p['c'] * p['l'] / 1e4 * p['qtd']; f = p['fita'] * p['qtd']
    d['mdf'] += a * m2[p['chapa']]; d['pecas'] += p['qtd']
    d['fita'] += f * (1 + M.FITA_PERD) * M.FITA[p['tf']][0] + f * M.FITA[p['tf']][1]
for o in M.outras:
    if o['amb'] != alvo: continue
    d = mv.setdefault(o['movel'], {'mdf': 0, 'fita': 0, 'itens': [], 'pecas': 0})
    d['itens'].append(o)
for k, d in mv.items():
    fer = sum(o['qtd'] * o['pu'] for o in d['itens'])
    print(f"\n{k} · {d['pecas']} peças · MDF {M.brl(d['mdf'])} · fita {M.brl(d['fita'])} · outros {M.brl(fer)}")
    for o in d['itens']:
        print(f"   {o['item']}: {o['qtd']:.2f} {o['un']} × {M.brl(o['pu'])} = {M.brl(o['qtd']*o['pu'])}")
