# -*- coding: utf-8 -*-
"""⭐ AS VISTAS DO EXECUTIVO, LIMPAS — do PDF vetorial para a proposta.

⛔⛔ POR QUE ELE EXISTE. A prancha executiva é A3 cheia: planta, elevações,
  cortes e detalhe na mesma folha, com a cotagem toda em VERMELHO por cima.
  Jogada inteira numa página da proposta, ela vira um borrão ilegível — e a
  cota não é assunto de cliente, é assunto de fábrica.

⭐ O QUE ELE FAZ, em três passos que se provam sozinhos:
  ① REDESENHA a página guardando só o traço PRETO. A cota (seta, extensão e
    o número, que neste CAD é CURVA e não texto) é vermelha — filtrar por cor
    tira os três de uma vez, sem adivinhar onde cada um está.
  ② SEPARA as vistas. Marca numa grade grossa onde há traço, engorda a marca
    e acha as ilhas: cada ilha é uma vista, porque o desenhista deixou
    corredor branco entre elas. Não leio o título da vista (ele também é
    curva) — eu olho o recorte e escolho.
  ③ RECORTA no branco de verdade, pixel a pixel, depois de rasterizar.

⛔ A ARMADILHA DA ROTAÇÃO: get_drawings() devolve coordenada NÃO rotacionada
  (x ≤ 842 numa A3 deitada por rot 270). A página nova nasce com a mediabox
  não rotacionada, recebe o traço cru e só então leva set_rotation() — assim
  o recorte e o raster saem na orientação que o olho espera.
"""
import pathlib, sys
import pymupdf
import numpy as np

AQUI = pathlib.Path(__file__).resolve().parent


def _vermelho(c):
    return bool(c) and len(c) >= 3 and c[0] > .55 and c[1] < .45 and c[2] < .45


def _cota(it):
    return _vermelho(it.get('color')) or _vermelho(it.get('fill'))


def pagina_limpa(pg):
    """A mesma página, só com o traço que não é cota nem moldura de folha."""
    doc = pymupdf.open()
    mb = pg.mediabox
    nova = doc.new_page(width=mb.width, height=mb.height)
    area = mb.width * mb.height
    for it in pg.get_drawings():
        if _cota(it):
            continue
        r = it['rect']
        if r.get_area() > .80 * area:        # ⛔ a moldura e o carimbo da folha
            continue
        sh = nova.new_shape()
        for sub in it['items']:
            k = sub[0]
            if k == 'l':
                sh.draw_line(sub[1], sub[2])
            elif k == 'c':
                sh.draw_bezier(sub[1], sub[2], sub[3], sub[4])
            elif k == 're':
                sh.draw_rect(sub[1])
            elif k == 'qu':
                sh.draw_quad(sub[1])
        sh.finish(color=it.get('color'), fill=it.get('fill'),
                  width=it.get('width') or .6,
                  dashes=it.get('dashes'),
                  closePath=bool(it.get('closePath')),
                  even_odd=bool(it.get('even_odd')),
                  fill_opacity=it.get('fill_opacity', 1) or 1,
                  stroke_opacity=it.get('stroke_opacity', 1) or 1)
        sh.commit()
    nova.set_rotation(pg.rotation)
    return doc, nova


def vistas(pg, celula=6, folga=2, minimo=9000):
    """As ilhas de traço, em coordenada de TELA. Cada ilha é uma vista.

    ⛔ A FOLGA É O AJUSTE FINO E ELA TEM DOIS LADOS: pouca, e uma elevação
      se parte em pedaços; muita, e duas vistas viram uma só. 12 pt — dois
      terços de centímetro na folha A3 — é o corredor que o desenhista
      deixa entre uma vista e a seguinte, e nunca dentro de uma."""
    R = pg.rect                             # já rotacionada
    m = pg.rotation_matrix
    area_pg = R.width * R.height
    caixas = []
    for it in pg.get_drawings():
        r = it['rect'] * m
        if r.get_area() > .80 * area_pg:    # ⛔ a moldura da folha
            continue
        if (r.x1 < 14 or r.x0 > R.width - 14
                or r.y1 < 14 or r.y0 > R.height - 14):
            continue                        # ⛔ as marcas de dobra na margem
        caixas.append(r)
    nx = int(R.width / celula) + 2
    ny = int(R.height / celula) + 2
    grade = [[False] * nx for _ in range(ny)]
    for r in caixas:
        x0, x1 = int(r.x0 / celula), int(r.x1 / celula) + 1
        y0, y1 = int(r.y0 / celula), int(r.y1 / celula) + 1
        for y in range(max(0, y0 - folga), min(ny, y1 + folga + 1)):
            linha = grade[y]
            for x in range(max(0, x0 - folga), min(nx, x1 + folga + 1)):
                linha[x] = True
    visto = [[False] * nx for _ in range(ny)]
    ilhas = []
    for y0 in range(ny):
        for x0 in range(nx):
            if not grade[y0][x0] or visto[y0][x0]:
                continue
            fila, visto[y0][x0] = [(x0, y0)], True
            xa = xb = x0
            ya = yb = y0
            while fila:
                x, y = fila.pop()
                xa, xb = min(xa, x), max(xb, x)
                ya, yb = min(ya, y), max(yb, y)
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    i, j = x + dx, y + dy
                    if 0 <= i < nx and 0 <= j < ny and grade[j][i] and not visto[j][i]:
                        visto[j][i] = True
                        fila.append((i, j))
            r = pymupdf.Rect((xa - folga) * celula, (ya - folga) * celula,
                             (xb + folga + 1) * celula, (yb + folga + 1) * celula)
            r = r & R
            if r.get_area() >= minimo:
                ilhas.append(r)
    ilhas.sort(key=lambda r: (round(r.y0 / 40), r.x0))
    return ilhas


def _apara(pm, margem=14):
    """⭐ O recorte final no BRANCO DE VERDADE — depois de rasterizar.
    A caixa dos vetores superestima: um traço de 0,6 pt pede uma caixa, e a
    folga da ilha põe ar de sobra. Aqui o que manda é o pixel aceso."""
    a = np.frombuffer(pm.samples, dtype=np.uint8).reshape(pm.height, pm.width, pm.n)
    tinta = (a.min(axis=2) < 250)
    ys, xs = np.where(tinta)
    if not len(ys):
        return pm
    y0, y1 = max(0, int(ys.min()) - margem), min(pm.height, int(ys.max()) + margem + 1)
    x0, x1 = max(0, int(xs.min()) - margem), min(pm.width, int(xs.max()) + margem + 1)
    #   ⛔⛔ A ORIGEM. O pixmap de um clip NÃO começa em (0,0): ele carrega
    #     a posição do recorte na página (pm.x, pm.y). As coordenadas que eu
    #     acabei de achar no numpy são RELATIVAS ao buffer. Copiar com elas
    #     direto pede uma região que o pixmap não cobre, e o que falta sai
    #     PRETO — uma tarja na borda, que de longe parece desenho.
    #   ⭐ Dois números para a mesma coisa de novo: relativo e absoluto.
    cx = pymupdf.IRect(pm.x + x0, pm.y + y0, pm.x + x1, pm.y + y1)
    sub = pymupdf.Pixmap(pm.colorspace, cx, False)
    sub.copy(pm, cx)
    return sub


def extrai(pdf, saida, dpi=190, so_folha=False, limpar=False):
    """⭐ POR PADRÃO A VISTA SAI COMO ESTÁ, COM A COTA.

    ⛔⛔ Tentei entregá-la limpa e descobri uma coisa: neste plot a LINHA de
      cota é vermelha, mas o NÚMERO dela é traço preto, igual ao do móvel —
      o CAD plota o texto como polilinha. Filtrar o vermelho tira a seta e
      deixa o número solto no branco, o que é pior que a cota inteira.
    ⭐ E a cota cotada não é defeito na proposta: a folha 04 promete que o
      executivo de marcenaria é nosso, e a elevação cotada é a prova disso
      na mão do cliente. `limpar=True` continua existindo para quando o
      desenho tiver de virar desenho de capa."""
    pathlib.Path(saida).mkdir(parents=True, exist_ok=True)
    d = pymupdf.open(pdf)
    doc = None
    if limpar:
        doc, pg = pagina_limpa(d[0])
    else:
        pg = d[0]
    nome = pathlib.Path(pdf).stem
    feitos = []
    alvos = [(None, pg.rect)] if so_folha else \
            [(i, r) for i, r in enumerate(vistas(pg), 1)]
    for i, r in alvos:
        pm = _apara(pg.get_pixmap(clip=r, dpi=dpi, alpha=False))
        p = pathlib.Path(saida) / ('%s%s.png' % (nome, '' if i is None else '-v%d' % i))
        pm.save(p)
        feitos.append((p, pm.width, pm.height))
    if doc: doc.close()
    d.close()
    return feitos


if __name__ == '__main__':
    saida = sys.argv[1] if len(sys.argv) > 1 else str(AQUI / '_vistas')
    for f in sorted((AQUI / 'pr').glob('*.pdf')):
        for p, w, h in extrai(f, saida):
            print('%-30s %5d x %5d px' % (p.name, w, h))
