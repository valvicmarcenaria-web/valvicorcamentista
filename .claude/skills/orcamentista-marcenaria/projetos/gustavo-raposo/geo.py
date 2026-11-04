# -*- coding: utf-8 -*-
"""Lê a prancha vetorial COM POSIÇÃO: amarra cota à vista e conta frente.

⭐ O executivo da Luiza Pacheco não tem folha de detalhamento por móvel: tudo
  mora nas elevações 1/25. O texto plano (read_file_content) devolve as cotas
  soltas — "60 190 293 130 293 88 395 483" — sem dizer de que peça é cada uma.
  Aqui cada palavra traz bbox e DIREÇÃO, então dá para agrupar a cota na
  cadeia da vista e conferir se a cadeia fecha na cota total.

⛔ A direção vem do span ('dir'), nunca da proporção do bbox: uma cota de dois
  dígitos girada 90° fica 10 × 10 e passa por horizontal.

⛔ pymupdf no container novo: `pip install` cai no python3.13 e o interpretador
  é o 3.11. Instalar com `python3 -m pip install pymupdf`.

   uso:  python3 -I geo.py 20 41 ...
"""
import re, sys, pathlib, pymupdf
PR = pathlib.Path(__file__).resolve().parent/'pr'
VISTA = re.compile(r'(PLANTA\s+DE\s+LAYOUT|PLANTA\s+BAIXA|ELEVA[ÇC][ÃA]O\s*\w*|'
                   r'VISTA\s+\w+|CORTE\s*\w*|DETALHE\s*\d*)', re.I)
FRENTE = re.compile(r'^(gavet[ãa]o|gaveta|b[áa]scula|giro|corre|fixo|nicho|'
                    r'prateleira|cabideiro|maleiro|sapateira|porta|espelho|'
                    r'prat\.?|porta-temperos|talheres)', re.I)

def cota(s):
    s = s.replace(',', '.').strip(' .')
    if not re.fullmatch(r'\d{1,4}(\.\d{1,2})?', s): return None
    v = float(s)
    return v if 1 <= v <= 900 else None

def ler(arq):
    pg = pymupdf.open(arq)[0]
    cotas, frentes, vistas = [], [], []
    for b in pg.get_text('dict')['blocks']:
        for ln in b.get('lines', ()):
            vert = abs(ln['dir'][1]) > 0.7          # ⭐ girada 90°
            txt = ''.join(sp['text'] for sp in ln['spans']).strip()
            x0, y0, x1, y1 = ln['bbox']
            if VISTA.search(txt): vistas.append((txt[:60], (x0+x1)/2, (y0+y1)/2))
            if FRENTE.match(txt): frentes.append((txt[:40], (x0+x1)/2, (y0+y1)/2))
            for sp in ln['spans']:
                sx0, sy0, sx1, sy1 = sp['bbox']
                for w in sp['text'].split():
                    v = cota(w)
                    if v: cotas.append((v, (sx0+sx1)/2, (sy0+sy1)/2, vert))
    return pg.rect, vistas, frentes, cotas

def cadeias(cotas, vert, tol=6):
    """Agrupa as cotas de uma direção pela linha de chamada: as horizontais
    partilham o Y, as verticais o X. Devolve cada cadeia e a soma."""
    sel = [c for c in cotas if c[3] == vert]
    eixo = (lambda c: c[2]) if not vert else (lambda c: c[1])
    ordem = (lambda c: c[1]) if not vert else (lambda c: c[2])
    grupos = []
    for c in sorted(sel, key=eixo):
        for g in grupos:
            if abs(eixo(g[0]) - eixo(c)) <= tol: g.append(c); break
        else: grupos.append([c])
    out = []
    for g in grupos:
        g.sort(key=ordem)
        vs = [x[0] for x in g]
        out.append((round(eixo(g[0]), 1), vs, round(sum(vs), 1)))
    return sorted(out, key=lambda t: -len(t[1]))

if __name__ == '__main__':
    for n in sys.argv[1:]:
        for arq in sorted(PR.glob(f'{int(n):02d}-*.pdf')):
            rect, vistas, frentes, cotas = ler(arq)
            print(f'\n{"═"*78}\n{arq.name}  ·  {rect.width:.0f} × '
                  f'{rect.height:.0f} pt  ·  {len(cotas)} cotas\n{"═"*78}')
            print('VISTAS:')
            for t, x, y in sorted(vistas, key=lambda v: (v[2], v[1])):
                print(f'   ({x:6.0f},{y:6.0f})  {t}')
            print('FRENTES:')
            for t, x, y in sorted(frentes, key=lambda v: (v[2], v[1])):
                print(f'   ({x:6.0f},{y:6.0f})  {t}')
            for vert, nome in ((False, 'HORIZONTAIS'), (True, 'VERTICAIS')):
                print(f'CADEIAS {nome}:')
                for eixo, vs, s in cadeias(cotas, vert)[:14]:
                    if len(vs) < 2 and s < 100: continue
                    print(f'   eixo {eixo:6.1f} · soma {s:7.1f} · ' +
                          ' + '.join(f'{v:g}' for v in vs))
