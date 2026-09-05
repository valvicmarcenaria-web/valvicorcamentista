#!/usr/bin/env python3
# Checklist de Medicao de Obra - Valvic (A4, 1 pagina, dinamico).
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
_B=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(_B,"checklist_medicao_obra.pdf")
LOGO=os.path.join(_B,"logo_clean.png")
W,H=A4
NAVY=colors.HexColor("#1F3A5F"); GREY=colors.HexColor("#666"); LINE=colors.HexColor("#c4c4c4")
c=canvas.Canvas(OUT,pagesize=A4)
p=12*mm

def fline(x,y,x2):
    c.setStrokeColor(LINE); c.setLineWidth(0.7); c.line(x,y,x2,y)
def chk(x,y,s=3.0*mm):
    c.setLineWidth(0.9); c.setStrokeColor(colors.black); c.rect(x,y,s,s); return x+s
def field(x,y,lab,x2,fs=8):
    c.setFont("Helvetica-Bold",fs); c.setFillColor(colors.black); c.drawString(x,y,lab)
    lx=x+c.stringWidth(lab,"Helvetica-Bold",fs)+2*mm; fline(lx,y-0.5,x2); return x2

# ---- cabecalho ----
img=ImageReader(LOGO); iw,ih=img.getSize(); lw=32*mm; lh=lw*ih/iw
c.drawImage(img,p,H-12*mm-lh,width=lw,height=lh,mask='auto')
c.setFillColor(NAVY); c.setFont("Helvetica-Bold",13); c.drawRightString(W-p,H-13*mm,"CHECK-LIST DE MEDIÇÃO DE OBRA")
c.setFillColor(GREY); c.setFont("Helvetica",8); c.drawRightString(W-p,H-18*mm,"Marque o que foi medido/conferido — e registre o que FALTA e por quê")
c.setStrokeColor(colors.HexColor("#cccccc")); c.setLineWidth(0.6); c.line(p,H-22*mm,W-p,H-22*mm)

y=H-28*mm
field(p,y,"Cliente:",p+95*mm); field(p+100*mm,y,"Data:",W-p)
y-=7*mm; field(p,y,"Obra/Endereço:",W-p)
y-=7*mm; field(p,y,"Ambiente:",p+80*mm); field(p+85*mm,y,"Medido por:",W-p)
y-=6*mm
c.setFont("Helvetica-Oblique",7.2); c.setFillColor(GREY)
c.drawString(p,y,"Legenda:  [ ] OK medido    [ F ] falta / pendente    [ N ] não se aplica    — anote a medida na linha")
c.setFillColor(colors.black)

# ---- helper de item de checklist com 1 caixa + linha ----
def item(x,y,txt,x2,box=True):
    if box:
        chk(x,y-2.6*mm); tx=x+5*mm
    else:
        tx=x
    c.setFont("Helvetica",7.8); c.setFillColor(colors.black); c.drawString(tx,y,txt)
    lx=tx+c.stringWidth(txt,"Helvetica",7.8)+2*mm
    fline(max(lx,x2-30*mm),y-0.5,x2)

def secao(x,y,titulo,w):
    c.setFillColor(NAVY); c.rect(x,y-4.6*mm,w,5.2*mm,fill=1,stroke=0)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold",8.2); c.drawString(x+2*mm,y-3.4*mm,titulo)
    c.setFillColor(colors.black)
    return y-9*mm

# duas colunas
colw=(W-2*p-8*mm)/2
xL=p; xR=p+colw+8*mm
xLe=xL+colw; xRe=xR+colw

yL=y-8*mm
yL=secao(xL,yL,"DIMENSÕES DO AMBIENTE",colw)
for t in ["Pé-direito (altura) — 3 pontos","Largura parede A","Largura parede B","Largura parede C","Largura parede D","Profundidade / recuos","Desnível de piso (mm)","Fora de esquadro? (qual canto)","Fora de prumo? (parede)"]:
    item(xL,yL,t,xLe); yL-=6.6*mm

yL=secao(xL,yL-1*mm,"ESQUADRIAS / ABERTURAS",colw)
for t in ["Porta: vão / altura","Janela: vão / peitoril / altura","Sentido de abertura das portas","Guarnição / batente (espessura)"]:
    item(xL,yL,t,xLe); yL-=6.6*mm

yL=secao(xL,yL-1*mm,"INSTALAÇÕES",colw)
for t in ["Pontos elétricos / tomadas","Interruptores / ponto de luz","Ponto de água / esgoto","Ponto de gás","Exaustão / coifa (duto)","Quadro / registro / medidor"]:
    item(xL,yL,t,xLe); yL-=6.6*mm

yR=y-8*mm
yR=secao(xR,yR,"REVESTIMENTO / ACABAMENTO",colw)
for t in ["Revestimento já colocado? (esp.)","Rodapé existente (altura)","Forro/gesso/sanca (altura)","Piso pronto? cota final"]:
    item(xR,yR,t,xRe); yR-=6.6*mm

yR=secao(xR,yR-1*mm,"ELETRODOMÉSTICOS (medida + definido?)",colw)
for t in ["Geladeira / frigobar","Fogão / cooktop","Forno / micro-ondas","Coifa / depurador","Lava-louças","Adega / outros"]:
    item(xR,yR,t,xRe); yR-=6.6*mm

yR=secao(xR,yR-1*mm,"BANCADA / PEDRA / CUBA",colw)
for t in ["Bancada (quem faz) / espessura","Altura da bancada","Cuba (modelo) / torneira","Interferências (viga/pilar/tubo)"]:
    item(xR,yR,t,xRe); yR-=6.6*mm

# ---- rodape: pendencias + croqui + fotos ----
ybase=min(yL,yR)-3*mm
c.setFillColor(colors.HexColor("#B8860B")); c.rect(p,ybase-4.6*mm,W-2*p,5.2*mm,fill=1,stroke=0)
c.setFillColor(colors.white); c.setFont("Helvetica-Bold",8.4); c.drawString(p+2*mm,ybase-3.4*mm,"⚠ O QUE FALTA MEDIR / PENDÊNCIAS  (o que não pôde ser medido e por quê)")
c.setFillColor(colors.black)
yy=ybase-10*mm
for _ in range(3):
    fline(p,yy,W-p); yy-=6.2*mm

# croqui
croq_h=yy-14*mm
c.setFont("Helvetica-Bold",8.2); c.setFillColor(NAVY); c.drawString(p,yy,"CROQUI (desenhe o ambiente e cote à mão):")
c.setFillColor(colors.black)
cy0=14*mm; cy1=yy-3*mm
c.setStrokeColor(colors.HexColor("#dddddd")); c.setLineWidth(0.4)
gx=p
while gx<=W-p:
    c.line(gx,cy0,gx,cy1); gx+=6*mm
gy=cy0
while gy<=cy1:
    c.line(p,gy,W-p,gy); gy+=6*mm
c.setStrokeColor(colors.HexColor("#999")); c.setLineWidth(0.9); c.rect(p,cy0,W-2*p,cy1-cy0)
c.setFont("Helvetica",7); c.setFillColor(GREY)
c.drawString(p,10*mm,"Fotos tiradas de tudo? [ ] Sim   Nº fotos: ____     Confere medidas 2x antes de sair.     Assinatura: __________________")
c.showPage(); c.save(); print("PDF:",OUT)
