#!/usr/bin/env python3
# DXF v2 (R12, mm) cilindro R200 x H500 COM ENCAIXE + nesting otimizado.
# Chapa 1850(X larg) x 2750(Y comp). Gap 7mm. Reguas 50mm, corpo 470 (desconto
# 15 teto + 15 base), abas 15mm. 4 reguas em cruz; discos com 4 rasgos em "+".
import math

# --- material / chapa ---
SHEET_W, SHEET_L = 1850.0, 2750.0   # X, Y
THICK = 15.0
GAP   = 7.0
MARG  = 10.0

# --- projeto ---
R, HEIGHT = 200.0, 500.0
CIRC = 2*math.pi*R
SPACING = 12.0
REG_W   = 50.0          # largura da regua
REG_BODY= HEIGHT - 2*THICK   # 470 (desconto teto+base)
TAB_W   = 30.0          # largura da aba (centrada nos 50)
TAB_L   = THICK         # 15 (atravessa o disco, rente)
OFFSET  = 70.0          # raio do centro ate o centro de cada rasgo

ents=[]
def line(layer,x1,y1,x2,y2):
    ents.extend(["0","LINE","8",layer,"10",f"{x1:.4f}","20",f"{y1:.4f}","30","0.0",
                 "11",f"{x2:.4f}","21",f"{y2:.4f}","31","0.0"])
def circle(layer,cx,cy,r):
    ents.extend(["0","CIRCLE","8",layer,"10",f"{cx:.4f}","20",f"{cy:.4f}","30","0.0","40",f"{r:.4f}"])
def poly(layer,pts):  # fecha
    for i in range(len(pts)):
        x1,y1=pts[i]; x2,y2=pts[(i+1)%len(pts)]
        line(layer,x1,y1,x2,y2)
def rect(layer,x0,y0,x1,y1):
    poly(layer,[(x0,y0),(x1,y0),(x1,y1),(x0,y1)])

def disc(cx,cy):
    circle("PERIMETRO",cx,cy,R)
    h=TAB_W/2; t=THICK/2
    # 4 rasgos em + (E,O,N,S), 30x15 cada, recebem as abas
    rect("ENCAIXE", cx+OFFSET-h, cy-t,   cx+OFFSET+h, cy+t)   # Leste
    rect("ENCAIXE", cx-OFFSET-h, cy-t,   cx-OFFSET+h, cy+t)   # Oeste
    rect("ENCAIXE", cx-t, cy+OFFSET-h,   cx+t, cy+OFFSET+h)   # Norte
    rect("ENCAIXE", cx-t, cy-OFFSET-h,   cx+t, cy-OFFSET+h)   # Sul

def regua(px,py):
    # bounding 50(X) x 500(Y): corpo 470 + abas 15 em cima/baixo, abas 30 centradas
    a=(REG_W-TAB_W)/2   # ombro = 10
    poly("PERIMETRO",[
        (px,        py+TAB_L),
        (px+a,      py+TAB_L),
        (px+a,      py),
        (px+a+TAB_W,py),
        (px+a+TAB_W,py+TAB_L),
        (px+REG_W,  py+TAB_L),
        (px+REG_W,  py+TAB_L+REG_BODY),
        (px+a+TAB_W,py+TAB_L+REG_BODY),
        (px+a+TAB_W,py+HEIGHT),
        (px+a,      py+HEIGHT),
        (px+a,      py+TAB_L+REG_BODY),
        (px,        py+TAB_L+REG_BODY),
    ])

# ====== NESTING (gap 7mm, chapa 1850x2750) ======
# painel embaixo-esq
PX0,PY0 = MARG, MARG
PX1,PY1 = PX0+CIRC, PY0+HEIGHT
rect("PERIMETRO", PX0,PY0,PX1,PY1)
# ranhuras do painel
width=PX1-PX0; n_g=round(width/SPACING); span=(n_g-1)*SPACING; start=PX0+(width-span)/2
for k in range(n_g):
    gx=start+k*SPACING; line("RANHURAS",gx,PY0,gx,PY1)
# 4 reguas a direita do painel
rx=PX1+GAP
for i in range(4):
    regua(rx, MARG); rx += REG_W+GAP
# 2 discos acima
dy = max(PY1, MARG+HEIGHT)+GAP+R
dx1 = MARG+R
disc(dx1, dy)
dx2 = dx1+2*R+GAP
disc(dx2, dy)

# limites usados
maxx = max(rx-GAP, dx2+R); maxy = dy+R
assert maxx<=SHEET_W and maxy<=SHEET_L, f"ESTOUROU A CHAPA: {maxx:.1f}x{maxy:.1f}"

# ----- DXF R12 -----
dxf=["0","SECTION","2","HEADER","9","$INSUNITS","70","4","0","ENDSEC",
 "0","SECTION","2","TABLES","0","TABLE","2","LAYER","70","3",
 "0","LAYER","2","PERIMETRO","70","0","62","7","6","CONTINUOUS",
 "0","LAYER","2","ENCAIXE","70","0","62","3","6","CONTINUOUS",
 "0","LAYER","2","RANHURAS","70","0","62","1","6","CONTINUOUS",
 "0","ENDTAB","0","ENDSEC","0","SECTION","2","ENTITIES"]+ents+["0","ENDSEC","0","EOF"]
path="/home/user/valvicorcamentista/.claude/skills/projeto-producao/gerados/cilindro_r200_h500_encaixe_teo.dxf"
import os; os.makedirs(os.path.dirname(path),exist_ok=True); open(path,"w").write("\n".join(dxf)+"\n")

print(f"chapa: {SHEET_W:.0f} x {SHEET_L:.0f} mm | gap {GAP:.0f}mm")
print(f"area usada (bounding): {maxx:.0f} x {maxy:.0f} mm  (sobra muito comprimento)")
print(f"painel: {width:.1f} x {HEIGHT:.0f} | {n_g} ranhuras")
print(f"reguas: 4 x ({REG_W:.0f} larg x {REG_BODY:.0f} corpo + abas {TAB_L:.0f}) = {HEIGHT:.0f} total")
print(f"discos: 2 x R{R:.0f} com 4 rasgos {TAB_W:.0f}x{THICK:.0f} em + (offset {OFFSET:.0f})")
print("camadas: PERIMETRO(passante) ENCAIXE(rasgos passantes) RANHURAS(parcial)")
print("OK cabe na chapa")
