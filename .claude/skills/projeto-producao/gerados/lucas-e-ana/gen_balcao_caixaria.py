#!/usr/bin/env python3
# CAIXARIA do balcao da TV (Lucas e Ana) — Parte 1.
# TV (223x55) + ESPELHO (109x40), altura 45 (5 base). MDF 15mm, fundo 6mm.
# Tampo/base PASSANTES (laterais/divisorias entre eles -> altura interna 420).
import os, math
OUTDIR="/home/user/valvicorcamentista/.claude/skills/projeto-producao/gerados/lucas-e-ana/"
PREV="/tmp/claude-0/-home-user-valvicorcamentista/1d917bda-5670-5e8e-99d3-c980f393e67a/scratchpad/"
os.makedirs(OUTDIR,exist_ok=True)
SW,SL=1850.0,2750.0; MARG=7.0; GAP=7.0
T=15.0; HI=450-2*T   # 420

P15=[("TV_TAMPO",2230,550,1),("TV_BASE",2230,550,1),
     ("TV_LATERAL",550,HI,2),("TV_DIVISORIA",550,HI,3),
     ("ESP_TAMPO",1090,400,1),("ESP_BASE",1090,400,1),
     ("ESP_LATERAL",400,HI,2),("ESP_DIVISORIA",400,HI,1)]
P6=[("TV_FUNDO_6mm",2230-2*T,HI,1),("ESP_FUNDO_6mm",1090-2*T,HI,1)]

def expand(lst):
    out=[]
    for n,w,h,q in lst:
        for i in range(q): out.append({"name":(f"{n}_{i+1}" if q>1 else n),"w":float(w),"h":float(h)})
    return out

def pack(pieces,W,L,m=MARG,g=GAP):
    pcs=sorted(pieces,key=lambda p:-max(p["w"],p["h"]))
    sheets=[]; remaining=list(range(len(pcs)))
    while remaining:
        free=[(m,m,W-2*m+g,L-2*m+g)]; placed=[]; still=[]
        for idx in remaining:
            p=pcs[idx]; pw,ph=p["w"],p["h"]; best=None
            for bw,bh,rot in [(pw+g,ph+g,0),(ph+g,pw+g,1)]:
                for fi,(fx,fy,fw,fh) in enumerate(free):
                    if bw<=fw+1e-6 and bh<=fh+1e-6:
                        waste=fw*fh-bw*bh
                        if best is None or waste<best[0]: best=(waste,fi,bw,bh,rot)
            if best is None: still.append(idx); continue
            waste,fi,bw,bh,rot=best; fx,fy,fw,fh=free.pop(fi)
            aw,ah=(pw,ph) if rot==0 else (ph,pw)
            placed.append((p,fx,fy,aw,ah))
            for rr in [(fx+bw,fy,fw-bw,bh),(fx,fy+bh,fw,fh-bh)]:
                if rr[2]>1e-6 and rr[3]>1e-6: free.append(rr)
        if not placed: break
        sheets.append(placed); remaining=still
    return sheets

def dpoly(layer,x,y,w,h):
    pts=[(x,y),(x+w,y),(x+w,y+h),(x,y+h)];s=["0","POLYLINE","8",layer,"66","1","70","1"]
    for px,py in pts: s+=["0","VERTEX","8",layer,"10",f"{px:.2f}","20",f"{py:.2f}","30","0.0"]
    s+=["0","SEQEND"];return s
def dtext(layer,x,y,h,t): return ["0","TEXT","8",layer,"10",f"{x:.2f}","20",f"{y:.2f}","30","0.0","40",f"{h:.2f}","1",t]
def write_dxf(path,placed):
    e=dpoly("CHAPA",0,0,SW,SL)
    for p,x,y,w,h in placed:
        e+=dpoly("PECAS",x,y,w,h); e+=dtext("TEXTO",x+15,y+h/2,26,f'{p["name"]} {w:.0f}x{h:.0f}')
    dxf=["0","SECTION","2","HEADER","9","$INSUNITS","70","4","0","ENDSEC",
     "0","SECTION","2","TABLES","0","TABLE","2","LAYER","70","3",
     "0","LAYER","2","CHAPA","70","0","62","5","6","CONTINUOUS",
     "0","LAYER","2","PECAS","70","0","62","7","6","CONTINUOUS",
     "0","LAYER","2","TEXTO","70","0","62","3","6","CONTINUOUS",
     "0","ENDTAB","0","ENDSEC","0","SECTION","2","ENTITIES"]+e+["0","ENDSEC","0","EOF"]
    open(path,"w").write("\n".join(dxf)+"\n")
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
def util(pl): return 100*sum(w*h for _,_,_,w,h in pl)/(SW*SL)
def preview(pl,title,path):
    fig,ax=plt.subplots(figsize=(SW/240,SL/240))
    ax.add_patch(Rectangle((0,0),SW,SL,facecolor="#f7f7f7",edgecolor="#222",lw=2))
    for p,x,y,w,h in pl:
        ax.add_patch(Rectangle((x,y),w,h,facecolor="#AED6F1",edgecolor="#1F618D",lw=1))
        ax.text(x+w/2,y+h/2,f'{p["name"]}\n{w:.0f}x{h:.0f}',ha="center",va="center",fontsize=6.5,weight="bold")
    ax.set_xlim(-30,SW+30);ax.set_ylim(-30,SL+30);ax.set_aspect("equal");ax.axis("off")
    ax.set_title(title,fontsize=10,weight="bold");fig.savefig(path,dpi=110,bbox_inches="tight");plt.close(fig)

res=[]
for tag,plist,th in [("15mm",P15,"15mm"),("6mm",P6,"6mm")]:
    sheets=pack(expand(plist),SW,SL)
    for i,pl in enumerate(sheets,1):
        nm="balcao_caixaria_15mm" if tag=="15mm" else "balcao_fundos_6mm"
        p=f"{OUTDIR}{nm}_chapa{i}.dxf"; write_dxf(p,pl)
        preview(pl,f"BALCÃO {tag} — chapa {i} · {len(pl)} pç · aprov {util(pl):.0f}%",PREV+f"prev_bc_{tag}_{i}.png")
        res.append((os.path.basename(p),[f'{x[0]["name"]}' for x in pl],f"{util(pl):.0f}%"))
for r in res: print(r[0],"->",len(r[1]),"pç",r[2],r[1])
