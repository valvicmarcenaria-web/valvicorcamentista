# -*- coding: utf-8 -*-
"""Despeja top / notas / dúvidas de _aba-<nome>.json nos .txt de colar."""
import json, sys
n = sys.argv[1]
d = json.load(open(f'_aba-{n}.json'))
for k, suf in (('top', 'top'), ('notas', 'not'), ('duvidas', 'duv')):
    t = json.dumps(d[k], ensure_ascii=False, separators=(',', ':'))
    open(f'_{suf}-{n}.txt', 'w').write(t)
    print(f'  {k:8} {d[k + "_range"]:14} {len(t)} chars')
