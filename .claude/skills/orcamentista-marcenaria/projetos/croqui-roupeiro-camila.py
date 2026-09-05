import math, os
W,H=1740,1330
INK="#1A1A1A"; GOLD="#C8901E"; GDEEP="#9C6B12"; GRAY="#8a8170"; WOOD="#b88f51"; BACK="#e7d9b6"
LINE="#cdbf95"; TRK="#9a958a"; PANEL="#efe6cf"
S=[]
def t(x,y,s,size=14,col=INK,anc="start",w="400",sp="0"):
    S.append(f'<text x="{x:.1f}" y="{y:.1f}" font-family="DejaVu Sans,Helvetica,Arial,sans-serif" font-size="{size}" fill="{col}" text-anchor="{anc}" font-weight="{w}" letter-spacing="{sp}">{s}</text>')
def line(x1,y1,x2,y2,col=INK,wd=1.4,dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ""
    S.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{wd}"{d}/>')
def rect(x,y,w,h,fill="none",col=INK,wd=1.3,dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ""
    S.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}" stroke="{col}" stroke-width="{wd}"{d}/>')
def polyf(pts,fill="none",col=INK,wd=1.4,dash=None):
    p=" ".join(f"{x:.1f},{y:.1f}" for x,y in pts); d=f' stroke-dasharray="{dash}"' if dash else ""
    S.append(f'<polygon points="{p}" fill="{fill}" stroke="{col}" stroke-width="{wd}"{d}/>')
def circ(x,y,r,fill="none",col=INK,wd=1.1):
    S.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" stroke="{col}" stroke-width="{wd}"/>')
def lead(x1,y1,x2,y2): line(x1,y1,x2,y2,GDEEP,1,dash="3 3")
def dimv(x,y1,y2,txt):
    line(x,y1,x,y2,GDEEP,1); line(x-5,y1,x+5,y1,GDEEP,1); line(x-5,y2,x+5,y2,GDEEP,1); cy=(y1+y2)/2
    S.append(f'<text x="{x-9:.1f}" y="{cy:.1f}" font-family="DejaVu Sans,Helvetica,Arial,sans-serif" font-size="12" fill="{GDEEP}" text-anchor="middle" font-weight="700" transform="rotate(-90 {x-9:.1f} {cy:.1f})">{txt}</text>')
def dimh(x1,x2,y,txt):
    line(x1,y,x2,y,GDEEP,1); line(x1,y-5,x1,y+5,GDEEP,1); line(x2,y-5,x2,y+5,GDEEP,1); t((x1+x2)/2,y-5,txt,12,GDEEP,"middle","700")

S.append('<defs>'
 '<pattern id="hatch" width="7" height="7" patternTransform="rotate(45)" patternUnits="userSpaceOnUse"><line x1="0" y1="0" x2="0" y2="7" stroke="#b9ac86" stroke-width="1"/></pattern>'
 '<pattern id="trk" width="5" height="5" patternTransform="rotate(45)" patternUnits="userSpaceOnUse"><line x1="0" y1="0" x2="0" y2="5" stroke="#6f6a5e" stroke-width="0.8"/></pattern>'
 f'<marker id="arr" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="{GDEEP}"/></marker></defs>')
S.append(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
# title
line(40,108,W-40,108,GOLD,2)
t(48,74,"valvic",31,INK,"start","700"); t(170,74,".",31,GOLD,"start","700"); t(50,95,"MARCENARIA",11,GDEEP,"start","700","4")
t(W-48,56,"Roupeiro — Camila · Closet",21,INK,"end","700")
t(W-48,79,"VISTA LATERAL (corte) · 2 módulos-caixa empilhados · 3 hipóteses do módulo superior",12.5,GDEEP,"end","700")
t(W-48,97,"Croqui esquemático — proporções representativas · JUN/2026",11,GRAY,"end","400")

def panel(ox, kind, titulo, sub):
    s=2.5; Dcm=56; Hcm=258; oy=184
    floorY=oy+Hcm*s; topY=oy
    def Y(cm): return floorY-cm*s
    xB=ox+10; xF=xB+Dcm*s; cx=xF+70
    dt=8; gap=4
    fp0=xF-dt; bp0=xF-2*dt-gap                # planos: frente [fp0,xF], trás [bp0,bp0+dt]
    # bandas cm
    LB=(0,3); LDOOR=(3,179); TRIL=(179,184); LTETO=(184,187); UBASE=(187,190); UDOOR=(190,248); MTRIL=(248,251); UTETO=(251,256)
    # parede / piso / teto(laje)
    rect(ox-22,topY-14,22,Hcm*s+38,fill="url(#hatch)",col="#b9ac86",wd=1); line(ox,topY-14,ox,floorY+6,INK,1.6)
    rect(ox-22,floorY+6,xF+40-ox,14,fill="url(#hatch)",col="#b9ac86",wd=1); line(ox-22,floorY+6,xF+44,floorY+6,INK,1.6)
    line(ox-22,topY-14,xF+44,topY-14,INK,1.1,dash="2 5"); t(ox-18,topY-19,"teto (laje)",9.5,GRAY)
    # fundo
    line(xB,Y(258),xB,floorY,INK,1.6)
    # ---- estrutura: bases e tetos dos 2 módulos (caixas) ----
    def hpanel(c0,c1,lbl=None):
        rect(xB,Y(c1),xF-xB,Y(c0)-Y(c1),fill=PANEL,col=INK,wd=1.2)
    hpanel(*LB)                      # base inferior
    hpanel(*LTETO)                   # teto do módulo inferior
    hpanel(*UBASE)                   # base do módulo superior
    hpanel(*UTETO)                   # teto do módulo superior
    # rótulos de módulo
    t(xB+6,Y(95),"módulo",10,GRAY); t(xB+6,Y(88),"inferior",10,GRAY)
    t(xB+6,Y(222),"módulo",9.5,GRAY); t(xB+6,Y(214),"superior",9.5,GRAY)
    # ---- TRILHO RO-65 sob o teto do módulo inferior ----
    trilho_hidden=(kind=="tampa")
    rect(bp0-2,Y(TRIL[1]),xF-(bp0-2),Y(TRIL[0])-Y(TRIL[1]),fill=("none" if trilho_hidden else "url(#trk)"),col=(GRAY if trilho_hidden else INK),wd=1.2,dash=("3 2" if trilho_hidden else None))
    # ---- PORTAS INFERIORES RO-65 (2 planos), encaixadas no módulo (base->trilho) ----
    rect(bp0,Y(TRIL[0]),dt,Y(LB[1]+0.5)-Y(TRIL[0]),fill=BACK,col=INK)   # plano traseiro
    rect(fp0,Y(TRIL[0]),dt,Y(LB[1]+0.5)-Y(TRIL[0]),fill=WOOD,col=INK)   # plano dianteiro (face em xF) (face em xF)
    circ(bp0+dt/2,Y(LB[1])+3,2.4,fill="#fff",col=INK); circ(fp0+dt/2,Y(LB[1])+3,2.4,fill="#fff",col=INK)
    line(fp0+dt,Y(95),cx,Y(95),GDEEP,1,dash="3 3"); t(cx,Y(95)-4,"RO-65 (base)",12,GDEEP,"start","700")
    t(cx,Y(95)+11,"portas encaixadas no",10,INK); t(cx,Y(95)+25,"módulo · 2 planos · 60 kg",10,INK); t(cx,Y(95)+39,"→ transpasso",10,GDEEP,"start","700")
    line(bp0-2,Y(181.5),cx-150,Y(181.5),GDEEP,1,dash="3 3"); t(cx-148,Y(181.5)+4,("trilho RO-65 (coberto)" if trilho_hidden else "trilho RO-65 (sob o teto)"),9.6,GDEEP,"start","700")
    # face de referência (porta externa do módulo inferior)
    if kind!="multi": line(xF,Y(250),xF,Y(150),INK,0.8,dash="2 3")
    # ---- MÓDULO SUPERIOR ----
    if kind=="multi":
        rect(bp0-2,Y(MTRIL[1]),xF-(bp0-2),Y(MTRIL[0])-Y(MTRIL[1]),fill="url(#trk)",col=INK,wd=1.0)  # trilho multi sob teto sup
        rect(bp0,Y(MTRIL[0]),dt,Y(UBASE[1]+0.5)-Y(MTRIL[0]),fill=BACK,col=INK)
        rect(fp0,Y(MTRIL[0]),dt,Y(UBASE[1]+0.5)-Y(MTRIL[0]),fill=WOOD,col=INK)
        line(fp0+dt,Y(220),cx,Y(220),GDEEP,1,dash="3 3"); t(cx,Y(220)-4,"Multi (Rometal)",12,GDEEP,"start","700")
        t(cx,Y(220)+11,"módulo independente:",10,INK); t(cx,Y(220)+25,"porta corre SOBRE a base,",10,INK)
        t(cx,Y(220)+39,"trilho sob o teto · 2 planos",10,INK); t(cx,Y(220)+53,"(transpasso)",10,GDEEP,"start","700")
    else:
        adv = 0 if kind=="bascula" else 12          # V3 avança à frente
        botC = UBASE[1] if kind=="bascula" else TRIL[0]   # V2 para na base sup; V3 desce e tampa teto+trilho
        fx = xF+adv                                  # face da báscula
        yH=Y(UTETO[0]); yB=Y(botC); L=yB-yH; hingeX=fx-dt
        rect(fx-dt,yH,dt,L,fill=WOOD,col=INK)        # báscula fechada (painel único, espessura dt)
        circ(hingeX+dt/2,yH,2.6,fill="#fff",col=INK)
        # aberta — indicação compacta
        Lh=min(L,72); ang=math.radians(50); dxu,dyu=math.cos(ang),-math.sin(ang); px,py=-dyu,dxu
        p1=(hingeX+dt/2,yH); p2=(p1[0]+Lh*dxu,p1[1]+Lh*dyu)
        polyf([(hingeX,yH),(hingeX+Lh*dxu,yH+Lh*dyu),(hingeX+Lh*dxu+dt*px,yH+Lh*dyu+dt*py),(hingeX+dt*px,yH+dt*py)],col=INK,wd=1.4,dash="5 3")
        S.append(f'<path d="M {fx:.1f} {yB:.1f} A {Lh:.0f} {Lh:.0f} 0 0 1 {hingeX+Lh*dxu+dt*px:.1f} {yH+Lh*dyu+dt*py:.1f}" fill="none" stroke="{GDEEP}" stroke-width="1.2" stroke-dasharray="2 4" marker-end="url(#arr)"/>')
        t(hingeX+Lh*dxu+6,yH+Lh*dyu-2,"aberta",9,GDEEP)
        line(fx-dt-2,Y(225),fx-dt,Y(245),INK,1.6); circ(fx-dt-2,Y(225),2.2,fill=INK,col=INK)  # pistão
        line(fx,Y(218),cx,Y(218),GDEEP,1,dash="3 3"); t(cx,Y(218)-4,"Báscula (1 porta)",12,GDEEP,"start","700")
        if kind=="bascula":
            t(cx,Y(218)+11,"painel único, abre p/ cima;",10,INK); t(cx,Y(218)+25,"face ALINHADA com a",10,INK)
            t(cx,Y(218)+39,"porta de baixo;",10,INK); t(cx,Y(218)+53,"teto+trilho ficam à vista",10,GDEEP,"start","700")
        else:
            t(cx,Y(218)+11,"AVANÇA à frente da face",10,INK); t(cx,Y(218)+25,"e DESCE tampando o teto",10,INK)
            t(cx,Y(218)+39,"do módulo inferior + trilho",10,INK); t(cx,Y(218)+53,"(fechada esconde, aberta revela)",9.4,GDEEP,"start","700")
            dimh(xF,fx,Y(205),"avança ~5cm")
    dimv(ox-40,Y(258),floorY,"258"); dimh(xB,xF,floorY+30,"~60"); t(ox-40,floorY+50,"cm",9.5,GRAY)
    t((xB+xF)/2,floorY+74,titulo,15,INK,"middle","700"); t((xB+xF)/2,floorY+92,sub,11,GDEEP,"middle","700")

panel(150,"multi","V1 — superior CORRER (Multi)","módulo independente, porta sobre a base")
panel(640,"bascula","V2 — superior BÁSCULA","1 porta, face alinhada com a de baixo")
panel(1130,"tampa","V3 — BÁSCULA avançada","tampa o teto do módulo inferior + trilho")

# ---- BOTTOM: transpasso + legenda ----
by=1035; dx=150; dw=720
rect(dx-12,by-30,dw,250,fill="#fdfaf0",col=LINE,wd=1.2)
t(dx,by-8,"DETALHE — transpasso (vista superior do módulo inferior RO-65)",13.5,GDEEP,"start","700")
py=by+28; pw=dw-40; line(dx,py,dx+pw,py,INK,1.3); t(dx,py-4,"fundo do armário",9.5,GRAY)
pl1=py+30; pl2=py+58; th=17; ax0=dx+6; aw=pw*0.60; bx0=dx+pw*0.40-6; bw=pw*0.60
rect(ax0,pl1,aw,th,fill=BACK,col=INK); t(ax0+8,pl1+12,"porta A — plano traseiro",9.5,INK)
rect(bx0,pl2,bw,th,fill=WOOD,col=INK); t(bx0+bw-8,pl2+12,"porta B — plano dianteiro",9.5,INK,"end")
S.append(f'<rect x="{bx0:.1f}" y="{pl1-7:.1f}" width="{(ax0+aw)-bx0:.1f}" height="{(pl2+th)-(pl1-7):.1f}" fill="#C8901E" fill-opacity="0.16" stroke="{GDEEP}" stroke-width="1.1" stroke-dasharray="3 2"/>')
dimh(bx0,ax0+aw,pl2+th+22,"transpasso")
S.append(f'<line x1="{ax0+aw-26:.1f}" y1="{pl1-15:.1f}" x2="{ax0+26:.1f}" y2="{pl1-15:.1f}" stroke="{GDEEP}" stroke-width="1.3" marker-end="url(#arr)"/>')
S.append(f'<line x1="{bx0+26:.1f}" y1="{pl2+th+8:.1f}" x2="{bx0+bw-26:.1f}" y2="{pl2+th+8:.1f}" stroke="{GDEEP}" stroke-width="1.3" marker-end="url(#arr)"/>')
t(dx,py+150,"As portas correm em 2 planos paralelos e se sobrepõem (transpasso): uma passa atrás",10.5,INK)
t(dx,py+166,"da outra ao abrir, sem fresta. Vale p/ RO-65 (inferior) e Multi (superior, V1).",10.5,INK)
lx=900; lw=W-40-lx; rect(lx-12,by-30,lw+24,250,fill="#ffffff",col=LINE,wd=1.2)
t(lx,by-8,"LEGENDA / estrutura e sistemas",13.5,GDEEP,"start","700")
sw=[(PANEL,"Estrutura: base e teto de cada módulo (MDF)"),(TRK,"Trilho (RO-65 e Multi) — sob o teto, ~5 cm"),(WOOD,"Porta dianteira / báscula"),(BACK,"Porta — plano traseiro")]
yy=by+20
for c,lab in sw:
    rect(lx,yy-12,17,17,fill=(c if c!=TRK else "url(#trk)"),col=INK,wd=1.1); t(lx+26,yy,lab,11,INK); yy+=26
yy+=3
for n in ["São 2 módulos-caixa empilhados, cada um com base e teto próprios.",
 "Inferior (RO-65): trilho sob o teto; portas grandes encaixam no módulo (base→trilho).",
 "V1 Multi: módulo superior independente, porta corre sobre a base, trilho sob o teto.",
 "V2 báscula: 1 porta no módulo superior, face alinhada com a porta de baixo.",
 "V3 báscula: avança à frente e desce, tampando teto do módulo inferior + trilho.",
 "Obs.: croqui esquemático; espessuras/folgas exageradas. Cotas finais no executivo."]:
    t(lx,yy,n,10.0,GRAY); yy+=16

svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'+"".join(S)+"</svg>"
open("croqui-roupeiro-camila.svg","w").write(svg); print("SVG bytes:",len(svg))
import fitz
d=fitz.open("croqui-roupeiro-camila.svg"); doc=fitz.open("pdf",d.convert_to_pdf())
doc[0].get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save("croqui-roupeiro-camila.png"); doc.save("croqui-roupeiro-camila.pdf")
print("render OK · PNG:",os.path.getsize("croqui-roupeiro-camila.png"),"bytes")
