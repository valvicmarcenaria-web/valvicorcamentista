import math, os
W,H=1720,1320
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
    line(x,y1,x,y2,GDEEP,1); line(x-5,y1,x+5,y1,GDEEP,1); line(x-5,y2,x+5,y2,GDEEP,1)
    cy=(y1+y2)/2
    S.append(f'<text x="{x-9:.1f}" y="{cy:.1f}" font-family="DejaVu Sans,Helvetica,Arial,sans-serif" font-size="12" fill="{GDEEP}" text-anchor="middle" font-weight="700" transform="rotate(-90 {x-9:.1f} {cy:.1f})">{txt}</text>')
def dimh(x1,x2,y,txt):
    line(x1,y,x2,y,GDEEP,1); line(x1,y-5,x1,y+5,GDEEP,1); line(x2,y-5,x2,y+5,GDEEP,1)
    t((x1+x2)/2,y-5,txt,12,GDEEP,"middle","700")

S.append('<defs>'
 '<pattern id="hatch" width="7" height="7" patternTransform="rotate(45)" patternUnits="userSpaceOnUse"><line x1="0" y1="0" x2="0" y2="7" stroke="#b9ac86" stroke-width="1"/></pattern>'
 '<pattern id="trk" width="5" height="5" patternTransform="rotate(45)" patternUnits="userSpaceOnUse"><line x1="0" y1="0" x2="0" y2="5" stroke="#6f6a5e" stroke-width="0.8"/></pattern>'
 f'<marker id="arr" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="{GDEEP}"/></marker></defs>')
S.append(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')

# ---- title ----
line(40,108,W-40,108,GOLD,2)
t(48,74,"valvic",31,INK,"start","700"); t(170,74,".",31,GOLD,"start","700"); t(50,95,"MARCENARIA",11,GDEEP,"start","700","4")
t(W-48,56,"Roupeiro — Camila · Closet",21,INK,"end","700")
t(W-48,79,"VISTA LATERAL (corte) · sistema de correr + transpasso · 3 hipóteses do módulo superior",12.5,GDEEP,"end","700")
t(W-48,97,"Croqui esquemático — proporções representativas · JUN/2026",11,GRAY,"end","400")

def panel(ox, kind, titulo, sub):
    s=2.5; Hcm=258; Dcm=58; oy=182
    floorY=oy+Hcm*s; topY=oy
    def Y(cm): return floorY-cm*s
    backX=ox+10; openX=backX+Dcm*s
    db=openX+4; df=db+13; dt=9; frontmost=df+dt
    cx=frontmost+22
    # bandas (cm): base 0-3 | porta inf 3-191 | TRILHO 191-196 | base sup 196-199 | porta sup 199-253 | topo 254-257
    # parede / piso / teto
    rect(ox-22,topY-14,22,Hcm*s+38,fill="url(#hatch)",col="#b9ac86",wd=1)
    line(ox,topY-14,ox,floorY+6,INK,1.6)
    rect(ox-22,floorY+6,frontmost-ox+46,14,fill="url(#hatch)",col="#b9ac86",wd=1)
    line(ox-22,floorY+6,frontmost+30,floorY+6,INK,1.6)
    line(ox-22,topY-14,frontmost+30,topY-14,INK,1.1,dash="2 5"); t(ox-18,topY-19,"teto (laje)",9.5,GRAY)
    # fundo (back)
    line(backX,Y(258),backX,floorY,INK,1.6)
    # ---- estrutura horizontal (croqui): base inferior, topo do móvel, base do módulo sup ----
    rect(backX,Y(3),openX-backX,Y(0)-Y(3),fill=PANEL,col=INK,wd=1.2)        # base inferior
    rect(backX,Y(257),openX-backX,Y(253)-Y(257),fill=PANEL,col=INK,wd=1.2)  # topo do conjunto
    rect(backX,Y(199),openX-backX,Y(196)-Y(199),fill=PANEL,col=INK,wd=1.2)  # base do módulo superior (independente)
    t(backX+6,Y(160),"corpo",10,GRAY)
    t(backX+6,Y(225),"módulo",9.5,GRAY); t(backX+6,Y(218),"superior",9.5,GRAY)
    line(backX,Y(196),openX,Y(196),INK,1.0,dash="1 3")  # separa módulos
    # ---- TRILHO superior do módulo inferior (~5 cm) ----
    trilho_hidden = (kind=="tampa")
    rect(openX,Y(196),frontmost-openX,Y(191)-Y(196),fill=("none" if trilho_hidden else "url(#trk)"),
         col=(GRAY if trilho_hidden else INK),wd=1.2,dash=("3 2" if trilho_hidden else None))
    _ty=(Y(191)+Y(196))/2
    if trilho_hidden:
        lead(openX+(frontmost-openX)/2,_ty,cx,_ty); t(cx,_ty-3,"trilho ~5 cm",10,GDEEP,"start","700"); t(cx,_ty+11,"(coberto: só aparece aberta)",9.3,GRAY)
    else:
        lead(frontmost,_ty,cx,_ty); t(cx,_ty-3,"trilho ~5 cm",10,GDEEP,"start","700"); t(cx,_ty+11,"(guia RO-65, à vista)",9.3,GRAY)
    # ---- PORTAS INFERIORES RO-65 (2 planos, base) ----
    rect(openX,floorY-10,frontmost-openX,10,fill="#efe9d8",col=INK,wd=1.0)   # trilho/base de rolagem
    circ(db+dt/2,floorY-5,2.6,fill="#fff",col=INK); circ(df+dt/2,floorY-5,2.6,fill="#fff",col=INK)
    rect(db,Y(191),dt,floorY-10-Y(191),fill=BACK,col=INK)                     # plano traseiro
    rect(df,Y(189),dt,floorY-10-Y(189),fill=WOOD,col=INK)                     # plano dianteiro
    lead(df+dt,Y(95),cx,Y(95)); t(cx,Y(95)-4,"RO-65 (base)",12,GDEEP,"start","700")
    t(cx,Y(95)+11,"roldana embaixo,",10,INK); t(cx,Y(95)+25,"60 kg · 2 planos",10,INK)
    t(cx,Y(95)+39,"→ transpasso",10,GDEEP,"start","700")
    # cota do trilho
    lead(openX, (Y(191)+Y(196))/2, openX-30,(Y(191)+Y(196))/2)
    # ---- MÓDULO SUPERIOR ----
    if kind=="multi":
        rect(openX,Y(253),frontmost-openX,Y(250)-Y(253),fill="#efe9d8",col=INK,wd=1.0)  # trilho superior (no topo)
        rect(db,Y(250),dt,Y(199)-2-Y(250),fill=BACK,col=INK)     # porta traseira (corre sobre a base)
        rect(df,Y(250),dt,Y(199)-2-Y(250),fill=WOOD,col=INK)     # porta dianteira
        # seta "corre sobre a base"
        line(df-4,Y(202),df+22,Y(202),GDEEP,1.1,dash=None);
        lead(df+dt,Y(228),cx,Y(228)); t(cx,Y(228)-4,"Multi (módulo",12,GDEEP,"start","700")
        t(cx,Y(228)+11,"independente)",12,GDEEP,"start","700"); t(cx,Y(228)+26,"porta corre SOBRE",10,INK)
        t(cx,Y(228)+40,"a base · suspensa no topo",10,INK); t(cx,Y(228)+54,"2 planos (transpasso)",10,GDEEP,"start","700")
    else:
        # báscula: painel único, espessura = dt (igual às outras portas), dobradiça no topo
        topHinge = 253 if kind=="bascula" else 253
        botCm = 199 if kind=="bascula" else 191      # tampa desce até cobrir o trilho (191)
        yH=Y(253); yB=Y(botCm); L=yB-yH
        hingeX=openX+2
        # fechada (painel vertical fino na frente)
        rect(openX+1,yH,dt,L,fill=WOOD,col=INK)
        circ(hingeX,yH,3,fill="#fff",col=INK)
        # aberta — só uma INDICAÇÃO compacta (não invade o título): painel curto girado p/ cima
        Lh=min(L,74); ang=math.radians(50); dxu,dyu=math.cos(ang),-math.sin(ang); px,py=-dyu,dxu
        p1=(hingeX,yH); p2=(hingeX+Lh*dxu,yH+Lh*dyu)
        p1b=(p1[0]+dt*px,p1[1]+dt*py); p2b=(p2[0]+dt*px,p2[1]+dt*py)
        polyf([p1,p2,p2b,p1b],col=INK,wd=1.5,dash="5 3")
        S.append(f'<path d="M {hingeX:.1f} {yH+Lh:.1f} A {Lh:.0f} {Lh:.0f} 0 0 1 {p2[0]:.1f} {p2[1]:.1f}" fill="none" stroke="{GDEEP}" stroke-width="1.2" stroke-dasharray="2 4" marker-end="url(#arr)"/>')
        t(p2[0]+4,p2[1]-2,"aberta",9,GDEEP)
        # pistão
        line(openX-3,Y(232),openX+1+dt-2,Y(248),INK,1.8); circ(openX-3,Y(232),2.3,fill=INK,col=INK)
        lead(openX+1+dt,Y(228),cx,Y(228)); t(cx,Y(228)-4,"Báscula",12,GDEEP,"start","700")
        t(cx,Y(228)+11,"painel único, abre",10,INK); t(cx,Y(228)+25,"p/ cima (pistão)",10,INK)
        if kind=="bascula":
            t(cx,Y(228)+39,"trilho fica à vista",10,GDEEP,"start","700")
        else:
            t(cx,Y(228)+39,"desce e TAMPA o trilho",10,GDEEP,"start","700")
            t(cx,Y(228)+53,"(fechada esconde,",9.6,GRAY); t(cx,Y(228)+65,"aberta revela)",9.6,GRAY)
    # cotas + título
    dimv(ox-40,Y(258),floorY,"258")
    dimh(backX,frontmost,floorY+30,"~60")
    t(ox-40,floorY+50,"cm",9.5,GRAY)
    t((backX+frontmost)/2,floorY+74,titulo,15,INK,"middle","700")
    t((backX+frontmost)/2,floorY+92,sub,11,GDEEP,"middle","700")
    return frontmost

panel(140,"multi","V1 — superior CORRER","módulo Multi independente")
panel(610,"bascula","V2 — superior BÁSCULA","trilho do módulo de baixo à vista")
panel(1080,"tampa","V3 — BÁSCULA tampando o trilho","fechada esconde o trilho")

# ---- BOTTOM: transpasso + legenda ----
by=1015
# transpasso (planta)
dx=140; dw=720
rect(dx-12,by-30,dw,250,fill="#fdfaf0",col=LINE,wd=1.2)
t(dx,by-8,"DETALHE — transpasso (vista superior do módulo inferior RO-65)",13.5,GDEEP,"start","700")
py=by+28; pw=dw-40
line(dx,py,dx+pw,py,INK,1.3); t(dx,py-4,"fundo do armário",9.5,GRAY)
pl1=py+30; pl2=py+58; th=17
ax0=dx+6; aw=pw*0.60; bx0=dx+pw*0.40-6; bw=pw*0.60
rect(ax0,pl1,aw,th,fill=BACK,col=INK); t(ax0+8,pl1+12,"porta A — plano traseiro",9.5,INK)
rect(bx0,pl2,bw,th,fill=WOOD,col=INK); t(bx0+bw-8,pl2+12,"porta B — plano dianteiro",9.5,INK,"end")
S.append(f'<rect x="{bx0:.1f}" y="{pl1-7:.1f}" width="{(ax0+aw)-bx0:.1f}" height="{(pl2+th)-(pl1-7):.1f}" fill="#C8901E" fill-opacity="0.16" stroke="{GDEEP}" stroke-width="1.1" stroke-dasharray="3 2"/>')
dimh(bx0,ax0+aw,pl2+th+22,"transpasso")
S.append(f'<line x1="{ax0+aw-26:.1f}" y1="{pl1-15:.1f}" x2="{ax0+26:.1f}" y2="{pl1-15:.1f}" stroke="{GDEEP}" stroke-width="1.3" marker-end="url(#arr)"/>')
S.append(f'<line x1="{bx0+26:.1f}" y1="{pl2+th+8:.1f}" x2="{bx0+bw-26:.1f}" y2="{pl2+th+8:.1f}" stroke="{GDEEP}" stroke-width="1.3" marker-end="url(#arr)"/>')
t(dx,py+150,"As portas correm em 2 planos paralelos e se sobrepõem (transpasso): uma passa",10.5,INK)
t(dx,py+166,"atrás da outra ao abrir e não fica fresta entre elas. (vale p/ RO-65 e Multi)",10.5,INK)

# legenda
lx=900; lw=W-40-lx
rect(lx-12,by-30,lw+24,250,fill="#ffffff",col=LINE,wd=1.2)
t(lx,by-8,"LEGENDA / estrutura e sistemas",13.5,GDEEP,"start","700")
sw=[(PANEL,"Estrutura (corpo, bases e topos) — MDF"),(TRK,"Trilho superior do módulo inferior (~5 cm)"),
    (WOOD,"Porta (dianteira) / báscula"),(BACK,"Porta (plano traseiro)")]
yy=by+22
for c,lab in sw:
    fillv = c if c!=TRK else "url(#trk)"
    rect(lx,yy-12,17,17,fill=fillv,col=INK,wd=1.1); t(lx+26,yy,lab,11,INK); yy+=27
yy+=4
notes=["RO-65 (inferior, nas 3): sustentação na base, guia no topo (o trilho de ~5 cm), 60 kg, 2 planos.",
 "Multi (V1): módulo independente — a porta corre SOBRE a base do módulo, suspensa no trilho do topo.",
 "Báscula (V2/V3): painel único de espessura normal, dobradiça no topo + pistão a gás (sem transpasso).",
 "V3: a báscula desce além do vão e TAMPA o trilho — fechada esconde, aberta revela.",
 "Obs.: croqui esquemático; espessuras/folgas exageradas p/ leitura. Cotas finais no executivo."]
for n in notes:
    t(lx,yy,n,10.2,GRAY); yy+=17

svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'+"".join(S)+"</svg>"
open("croqui-roupeiro-camila.svg","w").write(svg); print("SVG bytes:",len(svg))
import fitz
d=fitz.open("croqui-roupeiro-camila.svg"); pdfb=d.convert_to_pdf(); doc=fitz.open("pdf",pdfb)
doc[0].get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save("croqui-roupeiro-camila.png"); doc.save("croqui-roupeiro-camila.pdf")
print("render OK · PNG:",os.path.getsize("croqui-roupeiro-camila.png"),"bytes")
