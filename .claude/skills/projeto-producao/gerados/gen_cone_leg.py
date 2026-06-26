#!/usr/bin/env python3
# DXF (R12, mm) — PÉ DE MESA CÔNICO (tronco de cone) revestido em MDF 15mm.
# Topo Ø250 (r=125), base Ø600 (r=300). ALTURA H = a confirmar (palpite 700mm).
# Gera: PLANIFICAÇÃO da lateral (setor de coroa) + vincos radiais p/ curvar (kerf),
# e os discos de topo (Ø250) e base (Ø600).
# Planificação do tronco de cone:
#   L  = geratriz do tronco = sqrt((R-r)^2 + H^2)
#   Sr = geratriz do ápice ao círculo de topo  = r*L/(R-r)
#   SR = geratriz do ápice ao círculo de base   = R*L/(R-r)
#   ang(setor) = 2*pi*(R-r)/L  (rad)  -> arco externo = 2*pi*R ; arco interno = 2*pi*r
import math, os

r_top=125.0; r_bot=300.0          # raios (Ø250 / Ø600)
H=700.0                            # ALTURA — A CONFIRMAR (palpite)
THICK=15.0; PELE=1.0
KERF_PITCH=12.0                    # passo dos vincos medido no arco EXTERNO (base)

R=r_bot; r=r_top; dR=R-r
L=math.hypot(dR,H)
SR=R*L/dR; Sr=r*L/dR
ang=2*math.pi*dR/L                 # abertura do setor (rad)
arc_out=2*math.pi*R; arc_in=2*math.pi*r

# centra o setor em 90° (apontando p/ cima)
a_mid=math.radians(90); a0=a_mid-ang/2; a1=a_mid+ang/2
CX,CY=900.0, 950.0                 # centro (ápice) do desenvolvimento

ents=[]
def line(layer,x1,y1,x2,y2):
    ents.extend(["0","LINE","8",layer,"10",f"{x1:.4f}","20",f"{y1:.4f}","30","0.0",
                 "11",f"{x2:.4f}","21",f"{y2:.4f}","31","0.0"])
def arc(layer,cx,cy,rad,a_start_deg,a_end_deg):
    ents.extend(["0","ARC","8",layer,"10",f"{cx:.4f}","20",f"{cy:.4f}","30","0.0",
                 "40",f"{rad:.4f}","50",f"{a_start_deg:.4f}","51",f"{a_end_deg:.4f}"])
def circle(layer,cx,cy,rad):
    ents.extend(["0","CIRCLE","8",layer,"10",f"{cx:.4f}","20",f"{cy:.4f}","30","0.0","40",f"{rad:.4f}"])
def text(layer,x,y,h,s):
    ents.extend(["0","TEXT","8",layer,"10",f"{x:.4f}","20",f"{y:.4f}","30","0.0","40",f"{h:.4f}","1",s])
def pol(a,rad): return (CX+rad*math.cos(a), CY+rad*math.sin(a))

# ---- PLANIFICAÇÃO (PERIMETRO): 2 arcos + 2 bordas radiais ----
arc("PERIMETRO",CX,CY,SR,math.degrees(a0),math.degrees(a1))   # arco externo (base)
arc("PERIMETRO",CX,CY,Sr,math.degrees(a0),math.degrees(a1))   # arco interno (topo)
for a in (a0,a1):
    p1=pol(a,Sr); p2=pol(a,SR); line("PERIMETRO",p1[0],p1[1],p2[0],p2[1])

# ---- VINCOS radiais (RANHURAS), passo ~12mm no arco externo ----
dang=KERF_PITCH/SR
n=max(1,int(round(ang/dang)))
for k in range(1,n):           # internos (não em cima das bordas)
    a=a0+ k*(ang/n)
    p1=pol(a,Sr); p2=pol(a,SR); line("RANHURAS",p1[0],p1[1],p2[0],p2[1])

text("TEXTO",CX-120,CY+SR+25,26,f"PLANIFICACAO LATERAL (revestir cone) - geratriz {L:.0f}mm - {n} vincos")
text("TEXTO",CX-120,CY+Sr-30,20,f"topo O250  ->  base O600   (vincos passo ~{KERF_PITCH:.0f}mm, pele {PELE:.0f}mm)")

# ---- DISCOS topo e base ----
circle("PERIMETRO",350,400,r_top); text("TEXTO",350-55,400,20,"TOPO O250")
circle("PERIMETRO",1100,400,r_bot); text("TEXTO",1100-60,400,22,"BASE O600")

dxf=["0","SECTION","2","HEADER","9","$INSUNITS","70","4","0","ENDSEC",
 "0","SECTION","2","TABLES","0","TABLE","2","LAYER","70","3",
 "0","LAYER","2","PERIMETRO","70","0","62","7","6","CONTINUOUS",
 "0","LAYER","2","RANHURAS","70","0","62","1","6","CONTINUOUS",
 "0","LAYER","2","TEXTO","70","0","62","3","6","CONTINUOUS",
 "0","ENDTAB","0","ENDSEC","0","SECTION","2","ENTITIES"]+ents+["0","ENDSEC","0","EOF"]
path="/home/user/valvicorcamentista/.claude/skills/projeto-producao/gerados/pe_mesa_cone_O250_O600.dxf"
os.makedirs(os.path.dirname(path),exist_ok=True); open(path,"w").write("\n".join(dxf)+"\n")

# preview
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots(figsize=(12,11))
ts=np.linspace(a0,a1,200)
ax.plot([CX+SR*math.cos(t) for t in ts],[CY+SR*math.sin(t) for t in ts],color="#1F618D",lw=2)
ax.plot([CX+Sr*math.cos(t) for t in ts],[CY+Sr*math.sin(t) for t in ts],color="#1F618D",lw=2)
for a in (a0,a1):
    ax.plot([CX+Sr*math.cos(a),CX+SR*math.cos(a)],[CY+Sr*math.sin(a),CY+SR*math.sin(a)],color="#1F618D",lw=2)
for k in range(1,n):
    a=a0+k*(ang/n); ax.plot([CX+Sr*math.cos(a),CX+SR*math.cos(a)],[CY+Sr*math.sin(a),CY+SR*math.sin(a)],color="#C0392B",lw=0.3)
th=np.linspace(0,2*math.pi,80)
ax.plot([350+r_top*math.cos(t) for t in th],[400+r_top*math.sin(t) for t in th],color="#1F618D",lw=2)
ax.plot([1100+r_bot*math.cos(t) for t in th],[400+r_bot*math.sin(t) for t in th],color="#1F618D",lw=2)
ax.text(350,400,"TOPO\nØ250",ha="center",va="center",fontsize=9,weight="bold")
ax.text(1100,400,"BASE\nØ600",ha="center",va="center",fontsize=9,weight="bold")
ax.text(CX,CY+ (Sr+SR)/2,f"PLANIFICAÇÃO\nlateral do cone\n{n} vincos",ha="center",va="center",fontsize=10,weight="bold")
ax.set_aspect("equal"); ax.axis("off")
ax.set_title(f"Pé de mesa cônico Ø250→Ø600 · H={H:.0f}mm (palpite) · geratriz {L:.0f} · setor {math.degrees(ang):.0f}°",fontsize=11,weight="bold")
fig.savefig("/tmp/claude-0/-home-user-valvicorcamentista/1d917bda-5670-5e8e-99d3-c980f393e67a/scratchpad/prev_cone.png",dpi=110,bbox_inches="tight")

print(f"H={H:.0f} | geratriz tronco L={L:.1f} | Sr={Sr:.1f} SR={SR:.1f} | setor={math.degrees(ang):.1f}° | {n} vincos")
print(f"arco externo={arc_out:.0f} (=2piR) arco interno={arc_in:.0f} (=2pir)")
print("arquivo:",path)
