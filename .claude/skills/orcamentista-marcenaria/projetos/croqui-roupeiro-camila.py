import math, os
W,H=1600,1180
INK="#1A1A1A"; GOLD="#C8901E"; GDEEP="#9C6B12"; GRAY="#8a8170"; WOOD="#b88f51"; LINE="#cdbf95"; BACK="#e7d9b6"
S=[]
def t(x,y,s,size=15,col=INK,anc="start",w="400",sp="0"):
    S.append(f'<text x="{x:.1f}" y="{y:.1f}" font-family="DejaVu Sans,Helvetica,Arial,sans-serif" font-size="{size}" fill="{col}" text-anchor="{anc}" font-weight="{w}" letter-spacing="{sp}">{s}</text>')
def line(x1,y1,x2,y2,col=INK,wd=1.4,dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ""
    S.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{wd}"{d}/>')
def rect(x,y,w,h,fill="none",col=INK,wd=1.4,dash=None,rx=0):
    d=f' stroke-dasharray="{dash}"' if dash else ""
    S.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}" stroke="{col}" stroke-width="{wd}"{d} rx="{rx}"/>')
def polyf(pts,fill="none",col=INK,wd=1.4,dash=None):
    p=" ".join(f"{x:.1f},{y:.1f}" for x,y in pts); d=f' stroke-dasharray="{dash}"' if dash else ""
    S.append(f'<polygon points="{p}" fill="{fill}" stroke="{col}" stroke-width="{wd}"{d}/>')
def circ(x,y,r,fill="none",col=INK,wd=1.2):
    S.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" stroke="{col}" stroke-width="{wd}"/>')
def dimv(x,y1,y2,txt,col=GDEEP):
    line(x,y1,x,y2,col,1); line(x-6,y1,x+6,y1,col,1); line(x-6,y2,x+6,y2,col,1)
    cy=(y1+y2)/2
    S.append(f'<text x="{x-9:.1f}" y="{cy:.1f}" font-family="DejaVu Sans,Helvetica,Arial,sans-serif" font-size="13" fill="{col}" text-anchor="middle" font-weight="700" transform="rotate(-90 {x-9:.1f} {cy:.1f})">{txt}</text>')
def dimh(x1,x2,y,txt,col=GDEEP):
    line(x1,y,x2,y,col,1); line(x1,y-6,x1,y+6,col,1); line(x2,y-6,x2,y+6,col,1)
    t((x1+x2)/2,y-5,txt,13,col,"middle","700")

S.append('<defs>'
 '<pattern id="hatch" width="7" height="7" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">'
 '<line x1="0" y1="0" x2="0" y2="7" stroke="#b9ac86" stroke-width="1"/></pattern>'
 f'<marker id="arr" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="{GDEEP}"/></marker>'
 '</defs>')
S.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ffffff"/>')

# title
line(40,106,W-40,106,GOLD,2)
t(48,74,"valvic",31,INK,"start","700"); t(170,74,".",31,GOLD,"start","700")
t(50,94,"MARCENARIA",11,GDEEP,"start","700","4")
t(W-48,58,"Roupeiro — Camila · Closet",21,INK,"end","700")
t(W-48,81,"VISTA LATERAL (corte) · transpasso das portas de correr",13,GDEEP,"end","700","1")
t(W-48,99,"Esquemático — proporções representativas · JUN/2026",11,GRAY,"end","400")

def side_view(ox, upper, titulo, sub):
    s=2.8; Hc,Dc,split=258,58,202; oy=205
    floorY=oy+Hc*s; topY=oy
    backX=ox+8; interior=Dc*s; openX=backX+interior
    db=openX+4; df=db+14; dt=10; midY=floorY-split*s; frontmost=df+dt
    # parede + piso + teto
    rect(ox-22,topY-16,22,Hc*s+40,fill="url(#hatch)",col="#b9ac86",wd=1)
    line(ox,topY-16,ox,floorY+6,INK,1.6)
    rect(ox-22,floorY+6,frontmost-ox+58,15,fill="url(#hatch)",col="#b9ac86",wd=1)
    line(ox-22,floorY+6,frontmost+40,floorY+6,INK,1.6)
    line(ox-22,topY-16,frontmost+40,topY-16,INK,1.1,dash="2 5")
    # corpo
    line(backX,topY,backX,floorY,INK,1.6); line(backX,topY,openX,topY,INK,1.6)
    line(backX,floorY,openX,floorY,INK,1.6); line(backX,midY,openX,midY,INK,1.4)
    shelfY=midY+90; line(backX+8,shelfY,openX-6,shelfY,GRAY,1.2)
    circ(backX+30,shelfY+26,4,col=GRAY); line(backX+30,shelfY+26,openX-22,shelfY+26,GRAY,1.2)
    t(backX+12,topY+(midY-topY)/2,"corpo",11,GRAY)
    cx=frontmost+22
    # INFERIOR RO-65 (2 planos)
    rect(openX,floorY-10,frontmost-openX,10,fill="#efe9d8",col=INK,wd=1.1)
    circ(db+dt/2,floorY-4.5,3,fill="#fff",col=INK); circ(df+dt/2,floorY-4.5,3,fill="#fff",col=INK)
    rect(db,midY+4,dt,floorY-10-(midY+4),fill=BACK,col=INK,wd=1.3)
    rect(df,midY+12,dt,floorY-10-(midY+12),fill=WOOD,col=INK,wd=1.3)
    rect(openX,midY,frontmost-openX,6,fill="#efe9d8",col=INK,wd=1)
    cyc=(midY+floorY)/2
    line(df+dt,cyc,cx,cyc-6,GDEEP,1,dash="3 3")
    t(cx,cyc-10,"RO-65 (base)",13,GDEEP,"start","700"); t(cx,cyc+9,"roldana embaixo +",10.5,INK)
    t(cx,cyc+24,"guia no topo · 60 kg",10.5,INK); t(cx,cyc+39,"2 planos → transpasso",10.5,GDEEP,"start","700")
    # SUPERIOR
    cy2=(topY+midY)/2
    if upper=="multi":
        rect(openX,topY,frontmost-openX,7,fill="#efe9d8",col=INK,wd=1)
        rect(db,topY+7,dt,midY-3-(topY+7),fill=BACK,col=INK,wd=1.3)
        rect(df,topY+7,dt,midY-9-(topY+7),fill=WOOD,col=INK,wd=1.3)
        line(df+dt,cy2,cx,cy2,GDEEP,1,dash="3 3")
        t(cx,cy2-6,"Multi (suspenso)",13,GDEEP,"start","700"); t(cx,cy2+9,"trilho só no topo,",10.5,INK)
        t(cx,cy2+24,"slim · 2 planos",10.5,INK); t(cx,cy2+39,"(correr ripado)",10.5,GDEEP,"start","700")
    else:
        hingeX=openX+6; hingeY=topY+8
        L=midY-12-(topY+8)
        rect(openX+3,topY+8,dt,L,fill=WOOD,col=INK,wd=1.3)            # fechada (vertical)
        ang=math.radians(33); dx_,dy_=math.cos(ang),-math.sin(ang)   # up-right
        px,py=-dy_,dx_                                               # perp
        p1=(hingeX,hingeY); p2=(hingeX+L*dx_,hingeY+L*dy_)
        p2b=(p2[0]+dt*px,p2[1]+dt*py); p1b=(p1[0]+dt*px,p1[1]+dt*py)
        polyf([p1,p2,p2b,p1b],fill="none",col=INK,wd=1.6,dash="5 3")  # aberta
        # arco de abertura (do pé fechado até o pé aberto)
        S.append(f'<path d="M {openX+3+dt:.1f} {topY+8+L:.1f} A {L:.0f} {L:.0f} 0 0 1 {p2[0]:.1f} {p2[1]:.1f}" fill="none" stroke="{GDEEP}" stroke-width="1.3" stroke-dasharray="2 4" marker-end="url(#arr)"/>')
        line(openX-3,cy2+30,openX+3+dt-2,topY+40,INK,2)              # pistão
        circ(openX-3,cy2+30,2.5,fill=INK,col=INK); circ(hingeX,hingeY,3.2,fill="#fff",col=INK)
        line(openX+3+dt,cy2,cx,cy2,GDEEP,1,dash="3 3")
        t(cx,cy2-6,"Báscula",13,GDEEP,"start","700"); t(cx,cy2+9,"abre para cima,",10.5,INK)
        t(cx,cy2+24,"dobradiça no topo",10.5,INK); t(cx,cy2+39,"+ pistão a gás",10.5,GDEEP,"start","700")
    dimv(ox-42,topY,floorY,"258 cm")
    dimh(backX,frontmost,floorY+32,"~60 cm prof.")
    t((backX+frontmost)/2,floorY+72,titulo,16,INK,"middle","700")
    t((backX+frontmost)/2,floorY+91,sub,11.5,GDEEP,"middle","700")

side_view(150,"multi","VERSÃO 1 — superior CORRER","ripado Cumaru no sistema Multi")
side_view(590,"bascula","VERSÃO 2 — superior BÁSCULA","abre para cima, com pistão")

# DETALHE TRANSPASSO (planta)
dx,dy=1000,250; dw=470
rect(dx-12,dy-46,dw+24,250,fill="#fdfaf0",col=LINE,wd=1.2,rx=6)
t(dx,dy-24,"DETALHE — transpasso (vista superior)",14,GDEEP,"start","700")
t(dx,dy-6,"como as portas de correr se cruzam (RO-65)",11,GRAY)
py=dy+24; pw=dw-16
line(dx,py,dx+pw,py,INK,1.4); t(dx,py-4,"fundo do armário",10,GRAY)
plane1=py+34; plane2=py+62; th=18
ax0=dx+8; aw=pw*0.60; bx0=dx+pw*0.40-8; bw=pw*0.60
rect(ax0,plane1,aw,th,fill=BACK,col=INK,wd=1.3); t(ax0+8,plane1+13,"porta A — plano traseiro",10,INK)
rect(bx0,plane2,bw,th,fill=WOOD,col=INK,wd=1.3); t(bx0+bw-8,plane2+13,"porta B — plano dianteiro",10,INK,"end")
ov0=bx0; ov1=ax0+aw
S.append(f'<rect x="{ov0:.1f}" y="{plane1-8:.1f}" width="{ov1-ov0:.1f}" height="{(plane2+th)-(plane1-8):.1f}" fill="#C8901E" fill-opacity="0.16" stroke="{GDEEP}" stroke-width="1.1" stroke-dasharray="3 2"/>')
dimh(ov0,ov1,plane2+th+24,"transpasso")
S.append(f'<line x1="{ax0+aw-28:.1f}" y1="{plane1-16:.1f}" x2="{ax0+28:.1f}" y2="{plane1-16:.1f}" stroke="{GDEEP}" stroke-width="1.3" marker-end="url(#arr)"/>')
S.append(f'<line x1="{bx0+28:.1f}" y1="{plane2+th+9:.1f}" x2="{bx0+bw-28:.1f}" y2="{plane2+th+9:.1f}" stroke="{GDEEP}" stroke-width="1.3" marker-end="url(#arr)"/>')
t(dx,py+170,"As portas correm em 2 planos paralelos e se sobrepõem (transpasso):",11,INK)
t(dx,py+187,"uma passa atrás da outra ao abrir e não fica fresta entre elas.",11,INK)

# LEGENDA
ly=590
rect(dx-12,ly-34,dw+24,300,fill="#ffffff",col=LINE,wd=1.2,rx=6)
t(dx,ly-12,"LEGENDA — como cada sistema se comporta",14,GDEEP,"start","700")
items=[(WOOD,"RO-65 (Rometal) — INFERIOR, nas 2 versões","sustentação na base (roldana) + guia no topo;","60 kg/porta · 2 planos sobrepostos (transpasso)."),
 (BACK,"Multi (Rometal) — SUPERIOR da Versão 1","suspenso pelo trilho de cima, slim, sem trilho","na base; ideal p/ porta pequena na faixa alta."),
 ("#ffffff","Báscula — SUPERIOR da Versão 2","porta única que gira no topo e abre p/ cima","com pistão a gás (não tem transpasso).")]
yy=ly+22
for col,tit,l1,l2 in items:
    rect(dx,yy-13,18,18,fill=col,col=INK,wd=1.2)
    t(dx+28,yy,tit,12.5,INK,"start","700"); t(dx+28,yy+17,l1,11,GRAY); t(dx+28,yy+33,l2,11,GRAY); yy+=68
t(dx,yy+2,"Obs.: desenho esquemático p/ leitura do cliente — espessuras de porta",10.2,GRAY)
t(dx,yy+18,"e folgas exageradas p/ clareza; cotas finais no projeto executivo.",10.2,GRAY)

svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'+"".join(S)+"</svg>"
open("croqui-roupeiro-camila.svg","w").write(svg); print("SVG bytes:",len(svg))
import fitz
d=fitz.open("croqui-roupeiro-camila.svg"); pdfb=d.convert_to_pdf(); doc=fitz.open("pdf",pdfb)
doc[0].get_pixmap(matrix=fitz.Matrix(1.15,1.15)).save("croqui-roupeiro-camila.png")
doc.save("croqui-roupeiro-camila.pdf")
print("render OK · PNG:",os.path.getsize("croqui-roupeiro-camila.png"),"bytes")
