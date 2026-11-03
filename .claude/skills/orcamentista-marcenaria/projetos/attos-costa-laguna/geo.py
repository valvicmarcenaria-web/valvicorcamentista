# -*- coding: utf-8 -*-
"""ATTOS · Costa Laguna — lê a prancha vetorial COM POSIÇÃO.

⭐ Herdado do `gustavo-raposo/geo.py`. O que muda: as pranchas do Attos não
  são numeradas, têm nome de ambiente (`cozinha-01.pdf`), então o argumento
  é o PREFIXO do arquivo, não o número da folha.

⛔ A direção vem do span ('dir'), nunca da proporção do bbox: uma cota de
  dois dígitos girada 90° fica 10 × 10 e passa por horizontal.

⚠ ESTAS PRANCHAS PODEM ESTAR COM O TEXTO VETORIZADO. O `read_file_content`
  do Drive devolveu só "R=0,00 / A3" na folha da cozinha, o que é sinal de
  texto convertido em curva. Se `ler()` voltar com zero cota, não insista no
  texto: a leitura vira visual, pelo `zoom.py`, e a cota sai da ESCALA.

   uso:  python3 -I geo.py cozinha hall suite ...
         python3 -I geo.py --todas
"""
import re, sys, pathlib, pymupdf

PR = pathlib.Path(__file__).resolve().parent / 'pr'
VISTA = re.compile(r'(PLANTA\s+DE\s+LAYOUT|PLANTA\s+BAIXA|ELEVA[ÇC][ÃA]O\s*\w*|'
                   r'VISTA\s+\w+|CORTE\s*\w*|DETALHE\s*\d*|ESC\.?\s*1[:/]\d+)', re.I)
FRENTE = re.compile(r'^(gavet[ãa]o|gaveta|b[áa]scula|giro|corre|fixo|nicho|'
                    r'prateleira|cabideiro|maleiro|sapateira|porta|espelho|'
                    r'prat\.?|porta-temperos|talheres|aparador|painel|rack|'
                    r'cristaleira|bancada|torre|cuba)', re.I)


def cota(s):
    s = s.replace(',', '.').strip(' .')
    if not re.fullmatch(r'\d{1,4}(\.\d{1,2})?', s):
        return None
    v = float(s)
    return v if 1 <= v <= 900 else None


def ler(arq, pagina=0):
    pg = pymupdf.open(arq)[pagina]
    cotas, frentes, vistas, texto = [], [], [], []
    for b in pg.get_text('dict')['blocks']:
        for ln in b.get('lines', ()):
            vert = abs(ln['dir'][1]) > 0.7          # ⭐ girada 90°
            txt = ''.join(sp['text'] for sp in ln['spans']).strip()
            if not txt:
                continue
            x0, y0, x1, y1 = ln['bbox']
            texto.append((txt, (x0 + x1) / 2, (y0 + y1) / 2, vert))
            if VISTA.search(txt):
                vistas.append((txt[:60], (x0 + x1) / 2, (y0 + y1) / 2))
            if FRENTE.match(txt):
                frentes.append((txt[:40], (x0 + x1) / 2, (y0 + y1) / 2))
            for sp in ln['spans']:
                sx0, sy0, sx1, sy1 = sp['bbox']
                for w in sp['text'].split():
                    v = cota(w)
                    if v:
                        cotas.append((v, (sx0 + sx1) / 2, (sy0 + sy1) / 2, vert))
    return pg.rect, vistas, frentes, cotas, texto


def cadeias(cotas, vert, tol=6):
    """Agrupa as cotas de uma direção pela linha de chamada: as horizontais
    partilham o Y, as verticais o X. Devolve cada cadeia e a soma."""
    sel = [c for c in cotas if c[3] == vert]
    eixo = (lambda c: c[2]) if not vert else (lambda c: c[1])
    ordem = (lambda c: c[1]) if not vert else (lambda c: c[2])
    grupos = []
    for c in sorted(sel, key=eixo):
        for g in grupos:
            if abs(eixo(g[0]) - eixo(c)) <= tol:
                g.append(c)
                break
        else:
            grupos.append([c])
    out = []
    for g in grupos:
        g.sort(key=ordem)
        vs = [x[0] for x in g]
        out.append((round(eixo(g[0]), 1), vs, round(sum(vs), 1)))
    return sorted(out, key=lambda t: -len(t[1]))


if __name__ == '__main__':
    alvos = sys.argv[1:]
    arqs = sorted(PR.glob('*.pdf')) if (not alvos or alvos[0] == '--todas') \
        else [a for p in alvos for a in sorted(PR.glob(f'{p}*.pdf'))]
    for arq in arqs:
        doc = pymupdf.open(arq)
        for i in range(doc.page_count):
            rect, vistas, frentes, cotas, texto = ler(arq, i)
            cab = f'{arq.name}' + (f'  p{i+1}' if doc.page_count > 1 else '')
            print(f'\n{"═"*78}\n{cab}  ·  {rect.width:.0f} × {rect.height:.0f} pt'
                  f'  ·  {len(texto)} linhas de texto  ·  {len(cotas)} cotas\n{"═"*78}')
            if not texto:
                print('⚠ NENHUM TEXTO — prancha vetorizada. A leitura é visual '
                      '(zoom.py) e a cota sai da ESCALA.')
                continue
            if vistas:
                print('VISTAS:')
                for t, x, y in sorted(vistas, key=lambda v: (v[2], v[1])):
                    print(f'   ({x:6.0f},{y:6.0f})  {t}')
            if frentes:
                print('FRENTES:')
                for t, x, y in sorted(frentes, key=lambda v: (v[2], v[1])):
                    print(f'   ({x:6.0f},{y:6.0f})  {t}')
            for vert, nome in ((False, 'HORIZONTAIS'), (True, 'VERTICAIS')):
                ch = [c for c in cadeias(cotas, vert) if len(c[1]) >= 2 or c[2] >= 100]
                if not ch:
                    continue
                print(f'CADEIAS {nome}:')
                for eixo, vs, s in ch[:14]:
                    print(f'   eixo {eixo:6.1f} · soma {s:7.1f} · '
                          + ' + '.join(f'{v:g}' for v in vs))
