#!/usr/bin/env python3
# DXF (R12, mm) — 2 quadrados 600x600 FINAIS com 45 graus nos 4 lados.
# Regras aprendidas (Paulo):
#  - 45 come ~3mm/lado -> desenhar +6mm na medida: 600 final => 606x606 desenhado.
#  - 2 pecas com 45 -> 30mm de distancia entre elas no lado chanfrado.
#  - linhas = caminho da T7 (45 graus); contorno livre depois com T2 (se precisar).
import os
SIDE_FINAL=600.0; COME=3.0                 # come por lado
SIDE=SIDE_FINAL+2*COME                      # 606 desenhado
GAP45=30.0                                  # folga entre pecas no lado chanfrado
MARG=20.0
SHEET_W,SHEET_L=1850.0,2750.0

ents=[]
def poly(layer,x,y,w,h):
    pts=[(x,y),(x+w,y),(x+w,y+h),(x,y+h)]
    s=["0","POLYLINE","8",layer,"66","1","70","1"]
    for px,py in pts: s+=["0","VERTEX","8",layer,"10",f"{px:.3f}","20",f"{py:.3f}","30","0.0"]
    s+=["0","SEQEND"]; ents.extend(s)
def text(layer,x,y,h,t):
    ents.extend(["0","TEXT","8",layer,"10",f"{x:.3f}","20",f"{y:.3f}","30","0.0","40",f"{h:.3f}","1",t])

# chapa
poly("CHAPA",0,0,SHEET_W,SHEET_L)
# quadrado A
ax,ay=MARG,MARG
poly("CHANFRO_45",ax,ay,SIDE,SIDE)
text("TEXTO",ax+40,ay+SIDE/2,24,"QUAD 1  606x606 (final 600)")
# quadrado B (30mm a direita do A)
bx=ax+SIDE+GAP45; by=ay
poly("CHANFRO_45",bx,by,SIDE,SIDE)
text("TEXTO",bx+40,by+SIDE/2,24,"QUAD 2  606x606 (final 600)")
text("TEXTO",ax,ay+SIDE+30,22,"45 graus nos 4 lados (T7) - folga 30mm entre pecas no lado chanfrado")

dxf=["0","SECTION","2","HEADER","9","$INSUNITS","70","4","0","ENDSEC",
 "0","SECTION","2","TABLES","0","TABLE","2","LAYER","70","3",
 "0","LAYER","2","CHAPA","70","0","62","5","6","CONTINUOUS",
 "0","LAYER","2","CHANFRO_45","70","0","62","6","6","CONTINUOUS",
 "0","LAYER","2","TEXTO","70","0","62","3","6","CONTINUOUS",
 "0","ENDTAB","0","ENDSEC","0","SECTION","2","ENTITIES"]+ents+["0","ENDSEC","0","EOF"]
path="/home/user/valvicorcamentista/.claude/skills/projeto-producao/gerados/dois_quadrados_600_45graus.dxf"
os.makedirs(os.path.dirname(path),exist_ok=True); open(path,"w").write("\n".join(dxf)+"\n")

# preview
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
fig,ax_=plt.subplots(figsize=(9,7))
ax_.add_patch(Rectangle((ax,ay),SIDE,SIDE,facecolor="#FDEBD0",edgecolor="#C0398C",lw=2))
ax_.add_patch(Rectangle((bx,by),SIDE,SIDE,facecolor="#FDEBD0",edgecolor="#C0398C",lw=2))
ax_.annotate("",xy=(bx,ay+SIDE/2),xytext=(ax+SIDE,ay+SIDE/2),arrowprops=dict(arrowstyle="<->",color="#C0392B",lw=1.5))
ax_.text((ax+SIDE+bx)/2,ay+SIDE/2+18,"30 mm",ha="center",color="#C0392B",weight="bold",fontsize=10)
for X,lbl in [(ax,"QUAD 1"),(bx,"QUAD 2")]:
    ax_.text(X+SIDE/2,ay+SIDE/2,f"{lbl}\n606x606\n(final 600)",ha="center",va="center",fontsize=10,weight="bold")
ax_.set_xlim(-20,bx+SIDE+40); ax_.set_ylim(-20,ay+SIDE+80); ax_.set_aspect("equal"); ax_.axis("off")
ax_.set_title("2 quadrados 600x600 final · 45° nos 4 lados · desenhados 606×606 · 30mm entre eles",fontsize=10,weight="bold")
fig.savefig("/tmp/claude-0/-home-user-valvicorcamentista/1d917bda-5670-5e8e-99d3-c980f393e67a/scratchpad/prev_2quad45.png",dpi=120,bbox_inches="tight")
print(f"desenhado {SIDE:.0f}x{SIDE:.0f} (final {SIDE_FINAL:.0f}), gap {GAP45:.0f}mm, 2 quadrados")
print("arquivo:",path)
