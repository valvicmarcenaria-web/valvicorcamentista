# -*- coding: utf-8 -*-
"""Lê uma página de prancha AGRUPANDO A COTA NA VISTA A QUE ELA PERTENCE.

⛔⛔ A regra que me custou um erro: cota sem posição mente. O 65 da
  cristaleira do Living eu li como largura, e é PROFUNDIDADE — porque o
  texto solto do PDF joga as três vistas no mesmo saco.

⭐ Aqui cada rótulo "DET. nn - VISTA X" vira um centro, e cada número vai
  para o centro mais próximo. Horizontal × vertical se decide pela forma
  da caixa do número (cota vertical vem rotacionada, mais alta que larga).

⭐ E filtra o que NÃO é cota: litro de freezer, potência, telefone, página.
  Na p082 o "594" é o litro do freezer — pela posição ele cai longe de
  qualquer linha de cota, e pelo valor não fecha cadeia nenhuma.
"""
import sys, pathlib, math, re, pymupdf
SP = pathlib.Path('/tmp/claude-0/-home-user-valvicorcamentista/'
                  '7882701a-ab48-5bc5-bc38-040da97b2b38/scratchpad/ica/pgs')
RUIDO = {594, 596, 2897, 8252, 7525, 8989, 93028, 36970, 53, 31, 60000}

def ler(n):
    pg = pymupdf.open(SP/f'p{int(n):03d}.pdf')[0]
    W, H = pg.rect.width, pg.rect.height
    vistas, cotas, txt = [], [], pg.get_text()
    for x0, y0, x1, y1, w, *_ in pg.get_text('words'):
        # ⛔ a legenda do canto inferior direito não é desenho
        if x0 > W*0.46 and y0 > H*0.88: continue
        if re.fullmatch(r'\d{1,4}', w):
            v = int(w)
            if v in RUIDO or v > 600 or v < 2: continue
            cotas.append((x0, y0, v, (y1-y0) > (x1-x0)*1.3))
    for m in re.finditer(r'VISTA\s+([A-ZÁÊÓ]+(?:\s+INTERNA)?)', txt):
        vistas.append(m.group(1))
    # posições dos rótulos de vista
    pos = [(x0, y0, w) for x0, y0, x1, y1, w, *_ in pg.get_text('words')
           if w.upper() == 'VISTA']
    rot = []
    for i, (x, y, _) in enumerate(pos):
        rot.append((x, y, vistas[i] if i < len(vistas) else f'?{i}'))
    if not rot: rot = [(W/2, H/2, 'FOLHA')]
    g = {}
    for x, y, v, vert in cotas:
        k = min(rot, key=lambda r: math.hypot(r[0]-x, r[1]-y))
        g.setdefault(k[2], {'h': [], 'v': []})['v' if vert else 'h'].append((x, y, v))
    return g, txt

def cadeia(vals, tol=3):
    """Soma de corridas contíguas: cota de cadeia se alinha no mesmo eixo."""
    out = []
    for eixo in (0, 1):
        vals2 = sorted(vals, key=lambda t: (round(t[1-eixo]/8), t[eixo]))
        grupo, ant = [], None
        for x, y, v in vals2:
            k = round((y if eixo == 0 else x)/8)
            if ant is not None and k != ant and grupo:
                if len(grupo) > 1: out.append(grupo)
                grupo = []
            grupo.append(v); ant = k
        if len(grupo) > 1: out.append(grupo)
    return out

if __name__ == '__main__':
    for n in sys.argv[1:]:
        g, txt = ler(n)
        print(f'\n{"═"*76}\nARQ {n}  ·  doc pág {int(n)+1}\n{"═"*76}')
        d = re.search(r'DET\.?\s*0?(\d{1,2})\s*[-–]\s*([^\n.]{2,44})', txt)
        if d: print(f'  {d.group(0).strip()}')
        for nome, c in g.items():
            hs = [v for _,_,v in c['h']]; vs = [v for _,_,v in c['v']]
            if not hs and not vs: continue
            print(f'\n  ▸ VISTA {nome}')
            if hs: print(f'      horizontais {sorted(hs)}')
            if vs: print(f'      verticais   {sorted(vs)}')
            for cd in cadeia(c['h']):
                if len(cd) > 1: print(f'      cadeia H: {" + ".join(map(str,cd))} = {sum(cd)}')
            for cd in cadeia(c['v']):
                if len(cd) > 1: print(f'      cadeia V: {" + ".join(map(str,cd))} = {sum(cd)}')
