#!/usr/bin/env python3
# DXF (R12, mm) — CRIADO REDONDO M55 (projeto Fabinho) em MDF BRANCO 15mm.
# Peças: TAMPO (disco), BASE (disco) e CINTA que envolve (painel desenvolvido c/ vincos).
# Frente da gaveta = à parte (não incluída). Cinta INTEIRA (abertura recortada depois).
# Sem LED. Altura do corpo 420mm. Pés em metalon (à parte).
import math, os

D=500.0; R=D/2          # diâmetro do corpo (Ø500) — A CONFIRMAR
H=420.0                 # altura do corpo (MDF)
THICK=15.0; PELE=1.0    # chapa 15mm, pele 1mm na dobra
SPACING=12.0; OVER=10.0 # vincos: passo 12mm, avanço 10mm fora da peça
CIRC=math.pi*D          # circunferência = comprimento da cinta

ents=[]
def line(layer,x1,y1,x2,y2):
    ents.extend(["0","LINE","8",layer,"10",f"{x1:.4f}","20",f"{y1:.4f}","30","0.0",
                 "11",f"{x2:.4f}","21",f"{y2:.4f}","31","0.0"])
def circle(layer,cx,cy,r):
    ents.extend(["0","CIRCLE","8",layer,"10",f"{cx:.4f}","20",f"{cy:.4f}","30","0.0","40",f"{r:.4f}"])
def rect(layer,x0,y0,x1,y1):
    for a,b,c,d in [(x0,y0,x1,y0),(x1,y0,x1,y1),(x1,y1,x0,y1),(x0,y1,x0,y0)]:
        line(layer,a,b,c,d)
def text(layer,x,y,h,s):
    ents.extend(["0","TEXT","8",layer,"10",f"{x:.4f}","20",f"{y:.4f}","30","0.0","40",f"{h:.4f}","1",s])

# ---- TAMPO (disco) ----
tx,ty=R, R
circle("PERIMETRO",tx,ty,R)
text("TEXTO",tx-70,ty,22,f"TAMPO O{D:.0f}")
# ---- BASE (disco) ----
bx,by=D+70+R, R
circle("PERIMETRO",bx,by,R)
text("TEXTO",bx-70,by,22,f"BASE O{D:.0f}")

# ---- CINTA (painel desenvolvido) ----
cx0,cy0=0.0, D+120          # canto inferior-esq da cinta
cx1,cy1=cx0+CIRC, cy0+H
rect("PERIMETRO",cx0,cy0,cx1,cy1)
text("TEXTO",cx0+10,cy1+25,22,f"CINTA {CIRC:.0f} x {H:.0f}  (vincos p/ dobrar em O{D:.0f}, pele {PELE:.0f}mm)")
# vincos verticais em zigzag contínuo, passo 12mm, avanço 10mm
n=round(CIRC/SPACING); span=(n-1)*SPACING; start=cx0+(CIRC-span)/2
top=cy1+OVER; bot=cy0-OVER
pts=[]
for k in range(n):
    gx=start+k*SPACING
    pts += [(gx,top),(gx,bot)] if k%2==0 else [(gx,bot),(gx,top)]
# polyline RANHURAS (aberta)
ents.extend(["0","POLYLINE","8","RANHURAS","66","1","70","0"])
for px,py in pts:
    ents.extend(["0","VERTEX","8","RANHURAS","10",f"{px:.4f}","20",f"{py:.4f}","30","0.0"])
ents.extend(["0","SEQEND"])

dxf=["0","SECTION","2","HEADER","9","$INSUNITS","70","4","0","ENDSEC",
 "0","SECTION","2","TABLES","0","TABLE","2","LAYER","70","3",
 "0","LAYER","2","PERIMETRO","70","0","62","7","6","CONTINUOUS",
 "0","LAYER","2","RANHURAS","70","0","62","1","6","CONTINUOUS",
 "0","LAYER","2","TEXTO","70","0","62","3","6","CONTINUOUS",
 "0","ENDTAB","0","ENDSEC","0","SECTION","2","ENTITIES"]+ents+["0","ENDSEC","0","EOF"]
path="/home/user/valvicorcamentista/.claude/skills/projeto-producao/gerados/criado_redondo_fabinho_M55.dxf"
os.makedirs(os.path.dirname(path),exist_ok=True); open(path,"w").write("\n".join(dxf)+"\n")

# preview
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.patches import Circle as PC, Rectangle as PR
fig,ax=plt.subplots(figsize=(13,7))
ax.add_patch(PC((tx,ty),R,facecolor="#EAF2F8",edgecolor="#1F618D",lw=1.5))
ax.add_patch(PC((bx,by),R,facecolor="#EAF2F8",edgecolor="#1F618D",lw=1.5))
ax.add_patch(PR((cx0,cy0),CIRC,H,facecolor="#FEF9E7",edgecolor="#1F618D",lw=1.5))
for k in range(0,n,1):
    gx=start+k*SPACING; ax.plot([gx,gx],[cy0,cy1],color="#C0392B",lw=0.3)
ax.text(tx,ty,f"TAMPO\nØ{D:.0f}",ha="center",va="center",fontsize=10,weight="bold")
ax.text(bx,by,f"BASE\nØ{D:.0f}",ha="center",va="center",fontsize=10,weight="bold")
ax.text(cx0+CIRC/2,cy0+H/2,f"CINTA  {CIRC:.0f} x {H:.0f}\n{n} vincos (passo {SPACING:.0f}mm)",ha="center",va="center",fontsize=10,weight="bold")
ax.set_xlim(-30,cx1+30); ax.set_ylim(-30,cy1+60); ax.set_aspect("equal"); ax.axis("off")
ax.set_title(f"Criado redondo M55 — MDF branco 15mm · tampo+base Ø{D:.0f} · cinta {CIRC:.0f}x{H:.0f}",fontsize=11,weight="bold")
fig.savefig("/tmp/claude-0/-home-user-valvicorcamentista/1d917bda-5670-5e8e-99d3-c980f393e67a/scratchpad/prev_criado_fabinho.png",dpi=120,bbox_inches="tight")

print(f"OK  tampo+base O{D:.0f} | cinta {CIRC:.1f} x {H:.0f} | {n} vincos passo {SPACING:.0f}")
print("arquivo:",path)
