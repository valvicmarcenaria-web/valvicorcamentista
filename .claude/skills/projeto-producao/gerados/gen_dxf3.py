#!/usr/bin/env python3
# DXF v3 (R12, mm) cilindro R200 x H500. CORRECOES:
#  - ranhuras: AVANCAM 10mm fora da peca (cima+baixo) e ligadas num UNICO ZIGZAG
#    (serpentina) -> fresa nao sai da peca entre passadas (nao quebra quinas).
#  - margem da borda = 7mm (= folga entre pecas).
#  - OSSO DE CAO (dogbone, raio = raio da fresa) em toda quina de encaixe.
import math

SHEET_W, SHEET_L = 1850.0, 2750.0
THICK = 15.0
GAP   = 7.0            # folga entre pecas E da borda
MARG  = 7.0            # margem da borda = 7mm
OVER  = 10.0           # avanco das ranhuras fora da peca (cima e baixo)
TOOL_R= 3.0           # raio da fresa do encaixe (T2 6mm) -> osso de cao

R, HEIGHT = 200.0, 500.0
CIRC = 2*math.pi*R
SPACING = 12.0
REG_W, REG_BODY = 50.0, HEIGHT-2*THICK   # 50 x 470
TAB_W, TAB_L = 30.0, THICK               # aba 30 x 15
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
def rect(layer,x0,y0,x1,y1,dogbone=False):
    polyline(layer,[(x0,y0),(x1,y0),(x1,y1),(x0,y1)],True)
    if dogbone:  # osso de cao em cada quina interna (raio = raio da fresa)
        for (cx,cy) in [(x0,y0),(x1,y0),(x1,y1),(x0,y1)]:
            circle(layer,cx,cy,TOOL_R)

def disc(cx,cy):
    circle("PERIMETRO",cx,cy,R)
    h=TAB_W/2; t=THICK/2
    rect("ENCAIXE", cx+OFFSET-h, cy-t, cx+OFFSET+h, cy+t, dogbone=True)  # Leste
    rect("ENCAIXE", cx-OFFSET-h, cy-t, cx-OFFSET+h, cy+t, dogbone=True)  # Oeste
    rect("ENCAIXE", cx-t, cy+OFFSET-h, cx+t, cy+OFFSET+h, dogbone=True)  # Norte
    rect("ENCAIXE", cx-t, cy-OFFSET-h, cx+t, cy-OFFSET+h, dogbone=True)  # Sul

def regua(px,py):
    a=(REG_W-TAB_W)/2
    polyline("PERIMETRO",[
        (px,py+TAB_L),(px+a,py+TAB_L),(px+a,py),(px+a+TAB_W,py),(px+a+TAB_W,py+TAB_L),
        (px+REG_W,py+TAB_L),(px+REG_W,py+TAB_L+REG_BODY),(px+a+TAB_W,py+TAB_L+REG_BODY),
        (px+a+TAB_W,py+HEIGHT),(px+a,py+HEIGHT),(px+a,py+TAB_L+REG_BODY),(px,py+TAB_L+REG_BODY),
    ],True)

# ================= NESTING =================
# Faixa de baixo: 2 discos + 4 reguas. Faixa de cima: painel (com folga p/ avanco).
# discos
d_y = MARG+R
disc(MARG+R, d_y); disc(MARG+R+2*R+GAP, d_y)
discs_top = MARG+2*R                       # 7+400 = 407
# reguas (a direita dos discos)
rx = MARG+2*(2*R)+2*GAP                     # depois dos 2 discos
for i in range(4):
    regua(rx, MARG); rx += REG_W+GAP
reg_top = MARG+HEIGHT                       # 7+500 = 507
band_bottom_top = max(discs_top, reg_top)  # 507

# painel: base posicionada p/ o avanco de baixo ter GAP de folga da faixa de baixo
PY0 = band_bottom_top + GAP + OVER          # 507+7+10 = 524
PX0 = MARG
PX1, PY1 = PX0+CIRC, PY0+HEIGHT
rect("PERIMETRO", PX0,PY0,PX1,PY1)          # contorno do painel
# ranhuras: zigzag continuo, avanco 10mm cima/baixo
width=PX1-PX0; n_g=round(width/SPACING); span=(n_g-1)*SPACING; start=PX0+(width-span)/2
top_o, bot_o = PY1+OVER, PY0-OVER
pts=[]
for k in range(n_g):
    gx=start+k*SPACING
    if k%2==0: pts += [(gx,top_o),(gx,bot_o)]
    else:      pts += [(gx,bot_o),(gx,top_o)]
polyline("RANHURAS", pts, False)            # UMA polilinha aberta (zigzag)

# ---- validacoes ----
maxx=max(rx-GAP, PX1, MARG+2*(2*R)+GAP); maxy=top_o
assert PX1<=SHEET_W-MARG, "painel passa da borda X"
assert top_o<=SHEET_L-MARG, "avanco passa da borda Y"
assert bot_o>=band_bottom_top+GAP-1e-6, "avanco invade a faixa de baixo"
assert bot_o>=MARG, "avanco passa da borda inferior"

dxf=["0","SECTION","2","HEADER","9","$INSUNITS","70","4","0","ENDSEC",
 "0","SECTION","2","TABLES","0","TABLE","2","LAYER","70","3",
 "0","LAYER","2","PERIMETRO","70","0","62","7","6","CONTINUOUS",
 "0","LAYER","2","ENCAIXE","70","0","62","3","6","CONTINUOUS",
 "0","LAYER","2","RANHURAS","70","0","62","1","6","CONTINUOUS",
 "0","ENDTAB","0","ENDSEC","0","SECTION","2","ENTITIES"]+ents+["0","ENDSEC","0","EOF"]
path="/home/user/valvicorcamentista/.claude/skills/projeto-producao/gerados/cilindro_r200_h500_encaixe_v3_teo.dxf"
import os; os.makedirs(os.path.dirname(path),exist_ok=True); open(path,"w").write("\n".join(dxf)+"\n")

print(f"chapa {SHEET_W:.0f}x{SHEET_L:.0f} | margem/gap {MARG:.0f}mm")
print(f"painel {width:.1f}x{HEIGHT:.0f} em Y[{PY0:.0f}..{PY1:.0f}]")
print(f"ranhuras: {n_g} vincos, ZIGZAG continuo (1 entrada/1 saida), avanco {OVER:.0f}mm")
print(f"  -> grooves de Y[{bot_o:.0f}..{top_o:.0f}] (passam {OVER:.0f}mm da peca)")
print(f"osso de cao: raio {TOOL_R:.0f}mm em todas as quinas dos 8 rasgos de encaixe")
print(f"area usada ~{maxx:.0f}x{maxy:.0f} | folga avanco-baixo p/ faixa: {bot_o-band_bottom_top:.0f}mm")
print("OK validacoes (cabe, avanco nao invade)")
