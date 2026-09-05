#!/usr/bin/env python3
# Gera DXF (R12 ASCII, mm) do cilindro R200 x H500 para importar no Aspire.
# Geometria NOMINAL (tamanho final da peca) — o Aspire aplica o offset da fresa.
# Camadas: PERIMETRO (corte passante) e RANHURAS (dobra/corte parcial).
import math

R       = 200.0
HEIGHT  = 500.0
CIRC    = 2*math.pi*R          # ~1256.637
SPACING = 12.0

ents = []
def line(layer, x1, y1, x2, y2):
    ents.extend(["0","LINE","8",layer,
                 "10",f"{x1:.4f}","20",f"{y1:.4f}","30","0.0",
                 "11",f"{x2:.4f}","21",f"{y2:.4f}","31","0.0"])
def circle(layer, cx, cy, r):
    ents.extend(["0","CIRCLE","8",layer,
                 "10",f"{cx:.4f}","20",f"{cy:.4f}","30","0.0","40",f"{r:.4f}"])
def rect(layer, x0, y0, x1, y1):
    line(layer,x0,y0,x1,y0); line(layer,x1,y0,x1,y1)
    line(layer,x1,y1,x0,y1); line(layer,x0,y1,x0,y0)

# ----- PERIMETRO (corte passante) -----
circle("PERIMETRO", 300.0, 900.0, R)          # disco 1
circle("PERIMETRO", 800.0, 900.0, R)          # disco 2
for i in range(4):                             # 4 reguas 80x500
    rx0 = 1100.0 + i*120.0
    rect("PERIMETRO", rx0, 700.0, rx0+80.0, 1200.0)

# painel: retangulo (circunferencia x altura)
PX0, PY0 = 30.0, 30.0
PX1, PY1 = PX0+CIRC, PY0+HEIGHT
rect("PERIMETRO", PX0, PY0, PX1, PY1)

# ----- RANHURAS (dobra / corte parcial) -----
width = PX1-PX0
n_g = round(width/SPACING)
span = (n_g-1)*SPACING
start = PX0 + (width-span)/2.0
for k in range(n_g):
    gx = start + k*SPACING
    line("RANHURAS", gx, PY0, gx, PY1)

# ----- monta DXF R12 -----
def kv(*p): return "\n".join(p)
dxf = []
dxf += ["0","SECTION","2","HEADER","9","$INSUNITS","70","4","0","ENDSEC"]
dxf += ["0","SECTION","2","TABLES","0","TABLE","2","LAYER","70","2",
        "0","LAYER","2","PERIMETRO","70","0","62","7","6","CONTINUOUS",
        "0","LAYER","2","RANHURAS","70","0","62","1","6","CONTINUOUS",
        "0","ENDTAB","0","ENDSEC"]
dxf += ["0","SECTION","2","ENTITIES"] + ents + ["0","ENDSEC"]
dxf += ["0","EOF"]
text = "\n".join(dxf)+"\n"

import os
path = "/home/user/valvicorcamentista/.claude/skills/projeto-producao/gerados/cilindro_r200_h500_teo.dxf"
os.makedirs(os.path.dirname(path), exist_ok=True)
open(path,"w").write(text)

print(f"circunferencia: {CIRC:.3f} mm")
print(f"ranhuras (linhas de dobra): {n_g}")
print(f"painel: {PX1-PX0:.3f} x {PY1-PY0:.1f} mm")
print("entidades: 2 circulos (discos) + 4 retangulos (reguas) + 1 retangulo (painel) + ranhuras")
print(f"arquivo: {path}")
