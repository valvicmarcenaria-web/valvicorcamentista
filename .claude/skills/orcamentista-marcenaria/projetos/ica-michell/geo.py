# -*- coding: utf-8 -*-
"""Lê a página vetorial COM POSIÇÃO: amarra cota a vista e conta frente.

⚠ read_file_content e extrair.py devolvem texto plano: a cota sai solta e
não se sabe de que peça é. Aqui cada palavra traz bbox e DIREÇÃO, então dá
para agrupar as cotas em cadeias, ver se a cadeia fecha na cota total — a
prova de que a leitura está certa — e contar as frentes por faixa.

⛔ A direção vem do span, nunca da proporção do bbox: uma cota de dois
dígitos girada 90° fica 10 × 10 e passa por horizontal.
⚠ ARQUIVO N = PÁGINA N+1 do documento.
"""
import re, sys, pathlib, pymupdf
PG = pathlib.Path('/tmp/claude-0/-home-user-valvicorcamentista/'
                  '7882701a-ab48-5bc5-bc38-040da97b2b38/scratchpad/ica/pgs')
FRENTE = re.compile(r'(gavet[ãa]o|gaveta|basculante|porta de giro|porta|'
                    r'divis[óo]ria|prateleira|nicho|lixeira|tempero|cabideiro|'
                    r'calceiro|gaveteiro|espelho|led|cuba|cava)', re.I)
VISTA = re.compile(r'(PERSPECTIVA|VISTA\s+\w+|ELEVA[ÇC][ÃA]O\s*\d*|'
                   r'PLANTA[\w\s-]*|CORTE\s*\w*)', re.I)
# ⭐ o que decide o preço do material: padrão, linha, pedra, vidro, luz
MAT = re.compile(r'(MDF|Duratex|Linha \w+|Quartzito|Granito|Travertino|'
                 r'vidro|espelho|reflecta|LED|fita|lamin|f[óo]rmica|laca|'
                 r'palha|corda|alum[íi]nio|ferro|a[çc]o|ripad|fecho toque|'
                 r'puxador|cava|bancada|cuba|pedra)', re.I)


def cota(s):
    s = s.replace(',', '.').strip(' .')
    if not re.fullmatch(r'\d{1,4}(\.\d{1,2})?', s): return None
    v = float(s)
    return v if 1 <= v <= 900 else None


def ler(arq):
    pg = pymupdf.open(arq)[0]
    cotas, frentes, vistas, mats = [], [], [], []
    for b in pg.get_text('dict')['blocks']:
        for ln in b.get('lines', ()):
            vert = abs(ln['dir'][1]) > 0.7          # ⭐ girada 90°
            for sp in ln['spans']:
                t = sp['text'].strip()
                x0, y0, x1, y1 = sp['bbox']
                x, y = (x0 + x1) / 2, (y0 + y1) / 2
                for w in t.split():
                    v = cota(w)
                    if v is not None and len(t.split()) == 1:
                        cotas.append((x, y, v, vert))
            txt = ' '.join(sp['text'] for sp in ln['spans'])
            if FRENTE.search(txt) and len(txt) < 90:
                frentes.append((round(x), round(y), re.sub(r'\s+', ' ', txt)[:40]))
            m = VISTA.search(txt)
            if m: vistas.append((round(x), round(y), m.group(1).strip()[:30]))
            if MAT.search(txt) and 8 < len(txt) < 140:
                mats.append(re.sub(r'\s+', ' ', txt).strip(' .'))
    return cotas, frentes, vistas, mats


def cadeias(cotas, vert, tol=5.0):
    """Agrupa as cotas que estão na mesma linha de cota."""
    k, o = (0, 1) if vert else (1, 0)            # girada: agrupa por x
    gs = []
    for c in sorted(cotas, key=lambda c: (c[k], c[o])):
        if gs and abs(gs[-1][-1][k] - c[k]) <= tol: gs[-1].append(c)
        else: gs.append([c])
    out = []
    for g in gs:
        g.sort(key=lambda c: c[o])
        vs = [c[2] for c in g]
        out.append((vs, round(sum(vs), 1), round(g[0][k]), g))
    return out


if __name__ == '__main__':
    alvo = set(sys.argv[1:])
    for f in sorted(PG.glob('p*.pdf')):
        n = int(f.stem[1:])
        if alvo and str(n) not in alvo: continue
        cotas, frentes, vistas, mats = ler(f)
        print(f'\n{"═"*72}\nARQ {n} · doc pág {n+1}\n{"═"*72}')
        if vistas:
            print('VISTAS: ' + ' | '.join(
                f'{v}@({x},{y})' for x, y, v in sorted(vistas, key=lambda t: t[1])))
        for vert in (False, True):
            cs = [c for c in cadeias([c for c in cotas if c[3] is vert], vert)
                  if len(c[0]) > 1]
            if not cs: continue
            print(f'\n  CADEIAS {"VERTICAIS (altura)" if vert else "HORIZONTAIS (largura)"}:')
            for vs, s, pos, g in sorted(cs, key=lambda t: -len(t[0]))[:10]:
                # a cota total: uma cota solta por perto que vale a soma
                lin = ' + '.join(f'{v:g}' for v in vs)
                perto = [c[2] for c in cotas if c[3] is vert
                         and abs(c[2] - s) <= max(2.0, s * 0.02)
                         and c not in g]
                sel = ' ⭐ FECHA EM %g' % perto[0] if perto else ''
                print(f'   {lin} = {s:g}{sel}   [{"x" if vert else "y"}≈{pos}]')
        if mats:
            print('\n  MATERIAL E ACABAMENTO:')
            vistos = set()
            for m in mats:
                k = m[:48].lower()
                if k in vistos: continue
                vistos.add(k); print('   ·', m)
        if frentes:
            print('\n  FRENTES E PEÇAS, por faixa de altura:')
            for yk in sorted({round(fr[1] / 14) for fr in frentes}):
                fx = sorted([fr for fr in frentes if round(fr[1] / 14) == yk])
                print(f'   y≈{yk*14:4d} · ' + ' | '.join(w for _, _, w in fx))
