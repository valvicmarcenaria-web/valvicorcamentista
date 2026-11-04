# -*- coding: utf-8 -*-
"""Renderiza uma página (ou um recorte dela) em PNG para eu OLHAR o desenho.

⭐ A cota diz a medida, o rótulo diz a natureza — mas só o desenho diz o
  ARRANJO: quantas frentes, onde cada uma está, qual vão ficou aberto.
  Contar frente por cadeia de cota é adivinhar; contar por olho é contar.
"""
import sys, pathlib, pymupdf
SP = pathlib.Path('/tmp/claude-0/-home-user-valvicorcamentista/'
                  '7882701a-ab48-5bc5-bc38-040da97b2b38/scratchpad/ica')

def png(n, x0=0, y0=0, x1=1, y1=1, largura=1400, nome=None):
    pg = pymupdf.open(SP/'pgs'/f'p{int(n):03d}.pdf')[0]
    R = pg.rect
    cl = pymupdf.Rect(R.x0 + x0*R.width, R.y0 + y0*R.height,
                      R.x0 + x1*R.width, R.y0 + y1*R.height)
    z = largura / cl.width
    pm = pg.get_pixmap(matrix=pymupdf.Matrix(z, z), clip=cl)
    out = SP/'png'/(nome or f'p{int(n):03d}.png')
    pm.save(out); print(out, pm.width, 'x', pm.height)
    return out

if __name__ == '__main__':
    a = sys.argv[1:]
    png(a[0], *(map(float, a[1:5]) if len(a) >= 5 else ()),
        largura=int(a[5]) if len(a) > 5 else 1400,
        nome=a[6] if len(a) > 6 else None)
