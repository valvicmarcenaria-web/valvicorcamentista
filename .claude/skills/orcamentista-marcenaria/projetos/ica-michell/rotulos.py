# -*- coding: utf-8 -*-
"""Lê os RÓTULOS de uma página de prancha — o que a cota não diz.

⭐ A cota dá a medida; o rótulo dá a NATUREZA da peça: "PORTA DE GIRO
  ESTILO PROVENÇAL", "BÁSCULA", "GAVETA", "PRATELEIRA", "NICHO".
  Sem o rótulo eu conto vãos; com ele eu conto FRENTES — e frente é
  ferragem, moldura e puxador, que é onde o preço mora.

⭐ Agrupa por vista igual ao lerprancha.py: cada rótulo vai para o
  centro de vista mais próximo, e dentro da vista sai em ordem de y.
"""
import sys, re, math, pymupdf, pathlib
SP = pathlib.Path('/tmp/claude-0/-home-user-valvicorcamentista/'
                  '7882701a-ab48-5bc5-bc38-040da97b2b38/scratchpad/ica/pgs')

def ler(n, so_frente=False):
    pg = pymupdf.open(SP/f'p{int(n):03d}.pdf')[0]
    W, H = pg.rect.width, pg.rect.height
    # junta palavras em linhas por bloco/linha do pymupdf
    linhas = []
    for b in pg.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            t = ''.join(s['text'] for s in l['spans']).strip()
            if not t: continue
            x0, y0 = l['bbox'][0], l['bbox'][1]
            if x0 > W*0.46 and y0 > H*0.88: continue          # legenda
            if re.fullmatch(r'[\d\s.,\-/x°²]+', t): continue   # só números
            linhas.append((x0, y0, t))
    pos = [(l['bbox'][0], l['bbox'][1]) for b in pg.get_text('dict')['blocks']
           for l in b.get('lines', [])
           if 'VISTA' in ''.join(s['text'] for s in l['spans']).upper()]
    nomes = re.findall(r'VISTA\s+([A-ZÁÊÓ]+(?:\s+INTERNA)?)', pg.get_text())
    rot = [(x, y, nomes[i] if i < len(nomes) else f'?{i}')
           for i, (x, y) in enumerate(pos)] or [(W/2, H/2, 'FOLHA')]
    g = {}
    for x, y, t in linhas:
        k = min(rot, key=lambda r: math.hypot(r[0]-x, r[1]-y))
        g.setdefault(k[2], []).append((y, x, t))
    return g

if __name__ == '__main__':
    for n in sys.argv[1:]:
        print(f'\n{"═"*76}\nARQ {n}  ·  doc pág {int(n)+1}\n{"═"*76}')
        for nome, ls in ler(n).items():
            print(f'\n  ▸ VISTA {nome}')
            vistos = set()
            for y, x, t in sorted(ls):
                if t in vistos: continue
                vistos.add(t)
                print(f'      {t}')
