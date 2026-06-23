#!/usr/bin/env python3
# DXF v4 (R12, mm) cilindro R200 x H500.
# CORRECAO desta versao (regra do Jonathan): OSSO DE CAO em APENAS UMA peca do par.
#  -> osso de cao vai na ESTRUTURA (ombros das abas das reguas), NAO nos rasgos
#     dos discos. Nunca nas duas (senao folga demais).
# Mantem: ranhuras em zigzag continuo + avanco 10mm; margem 7mm.
import math

SHEET_W, SHEET_L = 1850.0, 2750.0
THICK = 15.0
GAP   = 7.0
MARG  = 7.0
OVER  = 10.0
TOOL_R= 3.0           # raio da fresa do encaixe -> raio do osso de cao

R, HEIGHT = 200.0, 500.0
CIRC = 2*math.pi*R
SPACING = 12.0
REG_W, REG_BODY = 50.0, HEIGHT-2*THICK
TAB_W, TAB_L = 30.0, THICK
OFFSET = 70.0

ents=[]
def line(layer,x1,y1,x2,y2):
    ents.extend(["0","LINE","8",layer,"10",f"{x1:.4f}","20",f"{y1:.4f}","30","0.0",
                 "11",f"{x2:.4f}","21",f"{y2:.4f}","31","0.0"])
def circle(layer,cx,cy,r):
    ents.extend(["0","CIRCLE","8",layer,"10",f"{cx:.4f}","20",f"{cy:.4f}","30","0.0","40",f"{r:.4f}"])
def polyline(layer,pts,close):
    rng = range(len(pts)) if close else range(len(pts)-1)
    for i in rng:
        x1,y1=pts[i]; x2,y2=pts[(i+1)%len(pts)]; line(layer,x1,y1,x2,y2)
def rect(layer,x0,y0,x1,y1):
    polyline(layer,[(x0,y0),(x1,y0),(x1,y1),(x0,y1)],True)

def disc(cx,cy):
    circle("PERIMETRO",cx,cy,R)
    h=TAB_W/2; t=THICK/2
    # rasgos LIMPOS (sem osso de cao — ele vai na regua)
    rect("ENCAIXE", cx+OFFSET-h, cy-t, cx+OFFSET+h, cy+t)  # Leste
    rect("ENCAIXE", cx-OFFSET-h, cy-t, cx-OFFSET+h, cy+t)  # Oeste
    rect("ENCAIXE", cx-t, cy+OFFSET-h, cx+t, cy+OFFSET+h)  # Norte
    rect("ENCAIXE", cx-t, cy-OFFSET-h, cx+t, cy-OFFSET+h)  # Sul

def regua(px,py):
    a=(REG_W-TAB_W)/2
    pts=[
        (px,py+TAB_L),(px+a,py+TAB_L),(px+a,py),(px+a+TAB_W,py),(px+a+TAB_W,py+TAB_L),
        (px+REG_W,py+TAB_L),(px+REG_W,py+TAB_L+REG_BODY),(px+a+TAB_W,py+TAB_L+REG_BODY),
        (px+a+TAB_W,py+HEIGHT),(px+a,py+HEIGHT),(px+a,py+TAB_L+REG_BODY),(px,py+TAB_L+REG_BODY),
    ]
    polyline("PERIMETRO",pts,True)
    # OSSO DE CAO nos 4 ombros das abas (quinas internas: indices 1,4,7,10)
    for i in (1,4,7,10):
        circle("PERIMETRO", pts[i][0], pts[i][1], TOOL_R)

# ================= NESTING =================
d_y = MARG+R
disc(MARG+R, d_y); disc(MARG+R+2*R+GAP, d_y)
discs_top = MARG+2*R
rx = MARG+2*(2*R)+2*GAP
for i in range(4):
    regua(rx, MARG); rx += REG_W+GAP
reg_top = MARG+HEIGHT
band_bottom_top = max(discs_top, reg_top)

PY0 = band_bottom_top + GAP + OVER
PX0 = MARG
PX1, PY1 = PX0+CIRC, PY0+HEIGHT
rect("PERIMETRO", PX0,PY0,PX1,PY1)
width=PX1-PX0; n_g=round(width/SPACING); span=(n_g-1)*SPACING; start=PX0+(width-span)/2
top_o, bot_o = PY1+OVER, PY0-OVER
pts=[]
for k in range(n_g):
    gx=start+k*SPACING
    pts += [(gx,top_o),(gx,bot_o)] if k%2==0 else [(gx,bot_o),(gx,top_o)]
polyline("RANHURAS", pts, False)

assert PX1<=SHEET_W-MARG and top_o<=SHEET_L-MARG
assert bot_o>=band_bottom_top+GAP-1e-6 and bot_o>=MARG

dxf=["0","SECTION","2","HEADER","9","$INSUNITS","70","4","0","ENDSEC",
 "0","SECTION","2","TABLES","0","TABLE","2","LAYER","70","3",
 "0","LAYER","2","PERIMETRO","70","0","62","7","6","CONTINUOUS",
 "0","LAYER","2","ENCAIXE","70","0","62","3","6","CONTINUOUS",
 "0","LAYER","2","RANHURAS","70","0","62","1","6","CONTINUOUS",
 "0","ENDTAB","0","ENDSEC","0","SECTION","2","ENTITIES"]+ents+["0","ENDSEC","0","EOF"]
path="/home/user/valvicorcamentista/.claude/skills/projeto-producao/gerados/cilindro_r200_h500_encaixe_v4_teo.dxf"
import os; os.makedirs(os.path.dirname(path),exist_ok=True); open(path,"w").write("\n".join(dxf)+"\n")

print("v4 — osso de cao SO na estrutura (reguas), rasgos dos discos LIMPOS")
print(f"osso de cao: raio {TOOL_R:.0f}mm em 4 ombros x 4 reguas = 16 (nas reguas)")
print(f"rasgos dos discos: 8, SEM osso de cao")
print(f"ranhuras: {n_g} vincos zigzag continuo, avanco {OVER:.0f}mm")
print("OK validacoes")
