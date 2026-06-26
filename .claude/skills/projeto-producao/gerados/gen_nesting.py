#!/usr/bin/env python3
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

OUTDIR="/home/user/valvicorcamentista/.claude/skills/projeto-producao/gerados/"
import os; os.makedirs(OUTDIR,exist_ok=True)
PREV="/tmp/claude-0/-home-user-valvicorcamentista/1d917bda-5670-5e8e-99d3-c980f393e67a/scratchpad/"

MARG=7.0; GAP=7.0
pieces=[
 ("P1",603,693),("P2",358,693),("P3",450,693),("P4",166,693),
 ("P5",477,850),("P6",480,850),("P7",489,845),("P8",489,845),
 ("P9",486,845),("P10",486,845),("P11",462,894),
]
items=[{"name":n,"w":w,"h":h} for n,w,h in pieces]

def nest(items,W,L,m=MARG,g=GAP):
    items=sorted(items,key=lambda p:-p["h"])
    placed=[]; left=[]
    x=m; y=m; shelfH=0; started=False
    for p in items:
        w,h=p["w"],p["h"]
        if w> W-2*m:  # nao cabe nem sozinha em largura
            left.append(p); continue
        if started and x+w<=W-m and y+max(shelfH,h)<=L-m:
            placed.append((p,x,y)); x+=w+g; shelfH=max(shelfH,h)
        else:
            y2 = (y+shelfH+g) if started else y
            if y2+h<=L-m:
                y=y2; x=m; shelfH=h; started=True
                placed.append((p,x,y)); x+=w+g
            else:
                left.append(p)
    return placed,left

# chapa A primeiro, sobra vai p/ chapa B
placedA,leftA=nest(items,1850,2750)
placedB,leftB=nest(leftA,1135,2750)

def util(placed,W,L):
    a=sum(p["w"]*p["h"] for p,_,_ in placed); return 100*a/(W*L)

# ---------- DXF (R12, mm) ----------
def dxf_polyline(layer,x,y,w,h):
    pts=[(x,y),(x+w,y),(x+w,y+h),(x,y+h)]
    s=["0","POLYLINE","8",layer,"66","1","70","1"]
    for px,py in pts:
        s+=["0","VERTEX","8",layer,"10",f"{px:.3f}","20",f"{py:.3f}","30","0.0"]
    s+=["0","SEQEND"]
    return s
def dxf_text(layer,x,y,h,txt):
    return ["0","TEXT","8",layer,"10",f"{x:.3f}","20",f"{y:.3f}","30","0.0","40",f"{h:.3f}","1",txt]
def write_dxf(path,W,L,placed):
    ents=[]
    ents+=dxf_polyline("CHAPA",0,0,W,L)
    for p,x,y in placed:
        ents+=dxf_polyline("PECAS",x,y,p["w"],p["h"])
        ents+=dxf_text("TEXTO",x+8,y+p["h"]/2,28,f'{p["name"]} {p["w"]:.0f}x{p["h"]:.0f}')
    dxf=["0","SECTION","2","HEADER","9","$INSUNITS","70","4","0","ENDSEC",
     "0","SECTION","2","TABLES","0","TABLE","2","LAYER","70","3",
     "0","LAYER","2","CHAPA","70","0","62","5","6","CONTINUOUS",
     "0","LAYER","2","PECAS","70","0","62","7","6","CONTINUOUS",
     "0","LAYER","2","TEXTO","70","0","62","3","6","CONTINUOUS",
     "0","ENDTAB","0","ENDSEC","0","SECTION","2","ENTITIES"]+ents+["0","ENDSEC","0","EOF"]
    open(path,"w").write("\n".join(dxf)+"\n")

write_dxf(OUTDIR+"nesting_chapa1_1850x2750.dxf",1850,2750,placedA)
write_dxf(OUTDIR+"nesting_chapa2_1135x2750.dxf",1135,2750,placedB)

# ---------- preview PNG ----------
def preview(placed,W,L,title,path):
    fig,ax=plt.subplots(figsize=(W/220,L/220))
    ax.add_patch(Rectangle((0,0),W,L,facecolor="#f7f7f7",edgecolor="#222",lw=2))
    for p,x,y in placed:
        ax.add_patch(Rectangle((x,y),p["w"],p["h"],facecolor="#AED6F1",edgecolor="#1F618D",lw=1.2))
        ax.text(x+p["w"]/2,y+p["h"]/2,f'{p["name"]}\n{p["w"]:.0f}x{p["h"]:.0f}',ha="center",va="center",fontsize=8,weight="bold")
    ax.set_xlim(-30,W+30); ax.set_ylim(-30,L+30); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(title,fontsize=11,weight="bold")
    fig.savefig(path,dpi=110,bbox_inches="tight"); plt.close(fig)

preview(placedA,1850,2750,f"CHAPA 1 — 1850x2750 mm · {len(placedA)} peças · aprov. {util(placedA,1850,2750):.0f}%",PREV+"prev_chapa1.png")
preview(placedB,1135,2750,f"CHAPA 2 — 1135x2750 mm · {len(placedB)} peças · aprov. {util(placedB,1135,2750):.0f}%",PREV+"prev_chapa2.png")

print("CHAPA 1 (1850x2750):", [p["name"] for p,_,_ in placedA], f"({len(placedA)} pcs, {util(placedA,1850,2750):.0f}%)")
print("CHAPA 2 (1135x2750):", [p["name"] for p,_,_ in placedB], f"({len(placedB)} pcs, {util(placedB,1135,2750):.0f}%)")
print("nao alocadas:", [p["name"] for p in leftB])
