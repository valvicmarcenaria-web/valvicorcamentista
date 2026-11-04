# -*- coding: utf-8 -*-
"""Renderiza um pedaço da prancha em alta resolução, para CONTAR frente.

⭐ Ler a cota solta do texto não diz quantas portas existem. Olhar a prancha
  diz. ⛔ PIL do sistema está quebrado no container (shadow do _imaging), e a
  do pip não sobe por cima — então o corte sai do próprio pymupdf, por clip.

   uso:  python3 zoom.py 20 0.20 0.04 0.82 0.42 [dpi]
         (nº da prancha e a janela em fração da página: x0 y0 x1 y1)
"""
import sys, pathlib, pymupdf
PR = pathlib.Path(__file__).resolve().parent/'pr'
OUT = pathlib.Path('/tmp/claude-0/-home-user-valvicorcamentista/'
                   '7882701a-ab48-5bc5-bc38-040da97b2b38/scratchpad/png')
OUT.mkdir(parents=True, exist_ok=True)
n = int(sys.argv[1])
x0, y0, x1, y1 = (float(v) for v in sys.argv[2:6])
dpi = int(sys.argv[6]) if len(sys.argv) > 6 else 220
arq = next(PR.glob(f'{n:02d}-*.pdf'))
pg = pymupdf.open(arq)[0]; r = pg.rect
clip = pymupdf.Rect(r.x0 + x0*r.width,  r.y0 + y0*r.height,
                    r.x0 + x1*r.width,  r.y0 + y1*r.height)
pm = pg.get_pixmap(dpi=dpi, clip=clip)
alvo = OUT/f'z{n}.png'
pm.save(alvo); print(alvo, pm.width, 'x', pm.height)
