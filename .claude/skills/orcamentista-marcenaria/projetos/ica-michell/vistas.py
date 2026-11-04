# -*- coding: utf-8 -*-
"""Lê a prancha SEPARANDO POR VISTA, não só por cadeia.

⛔ [Jonathan 28/10] "analise todas as visoes, como vista superior e vista
   frontal". O geo.py agrupa cotas em cadeias e acha a cadeia que fecha —
   mas joga todas as vistas no mesmo saco. Quando a folha traz três vistas
   do mesmo móvel, a cota da vista superior entra na cadeia da frontal e o
   móvel sai errado.

⭐ Aqui cada rótulo de VISTA vira um centro, e cada cota vai para a vista
   MAIS PRÓXIMA. Daí dá para ler "o que a vista superior diz" separado de
   "o que a frontal diz" — que é como um marceneiro lê a prancha.
"""
import sys, pathlib, math, pymupdf, re
import geo

def por_vista(arq, raio=400):
    cotas, frentes, vistas, mats = geo.ler(arq)
    if not vistas: vistas = [(0, 0, 'FOLHA')]
    # ⭐ cada vista é um centro; a cota vai para a mais próxima
    def perto(x, y):
        return min(vistas, key=lambda v: math.hypot(v[0]-x, v[1]-y))
    grupos = {}
    for x, y, v, vert in cotas:
        k = perto(x, y)
        grupos.setdefault(k[2] + f'@({k[0]},{k[1]})', []).append((x, y, v, vert))
    return grupos, frentes, vistas, mats

if __name__ == '__main__':
    for n in sys.argv[1:]:
        f = geo.PG / f'p{int(n):03d}.pdf'
        grupos, frentes, vistas, mats = por_vista(f)
        print(f'\n{"═"*74}\nARQ {n} · doc pág {int(n)+1}\n{"═"*74}')
        for nome, cs in sorted(grupos.items(), key=lambda t: -len(t[1])):
            h = sorted({c[2] for c in cs if not c[3]})
            v = sorted({c[2] for c in cs if c[3]})
            print(f'\n  ▸ {nome}  ({len(cs)} cotas)')
            print(f'    horizontais: {h}')
            print(f'    verticais  : {v}')
            # cadeias dentro da vista
            for vert in (False, True):
                cc = [c for c in cs if c[3] is vert]
                for vs, soma, pos, g in geo.cadeias(cc, vert):
                    if len(vs) > 1:
                        print(f'      {"alt" if vert else "larg"}: '
                              + ' + '.join(f'{x:g}' for x in vs) + f' = {soma:g}')
        if frentes:
            print(f'\n  PEÇAS CITADAS:')
            for _, _, w in sorted(set(frentes), key=lambda t: t[1]):
                print(f'    · {w}')
