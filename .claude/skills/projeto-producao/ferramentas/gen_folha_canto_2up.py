#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os
_B=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(_B,"folha_modulacao_canto_2up.pdf")
LOGO=os.path.join(_B,"logo_clean.png")
W,H=A4
NAVY=colors.HexColor("#1F3A5F"); GREY=colors.HexColor("#777"); LINE=colors.HexColor("#c4c4c4")
c=canvas.Canvas(OUT,pagesize=A4)

def chk(xx,yy,txt,s=3.0*mm,fs=7.0):
    c.setLineWidth(0.9); c.setStrokeColor(colors.black); c.rect(xx,yy,s,s)
    c.setFont("Helvetica",fs); c.setFillColor(colors.black); c.drawString(xx+s+1.6,yy+0.5,txt)
    return xx+s+1.6+c.stringWidth(txt,"Helvetica",fs)+3*mm
def fline(xx,yy,x2):
    c.setStrokeColor(LINE); c.setLineWidth(0.7); c.line(xx,yy,x2,yy)
def lab(x,y,t): c.setFont("Helvetica-Bold",7.6); c.setFillColor(colors.black); c.drawString(x,y,t)
def unit(x,y,t="mm"):
    c.setFont("Helvetica",7); c.setFillColor(GREY); c.drawString(x,y,t); c.setFillColor(colors.black)

def card(ox,oy,cw,ch):
    p=6*mm
    img=ImageReader(LOGO); iw,ih=img.getSize(); lw=36*mm; lh=lw*ih/iw
    c.drawImage(img,ox+p,oy+ch-p-lh,width=lw,height=lh,mask='auto')
    c.setFont("Helvetica",7); c.setFillColor(GREY); c.drawRightString(ox+cw-p,oy+ch-p-4,"FOLHA DE MODULAÇÃO — CANTO")
    y=oy+ch-p-lh-6*mm
    c.setFont("Helvetica",9); c.setFillColor(colors.black)
    c.drawString(ox+p,y,"Pedido:"); fline(ox+p+16*mm,y-0.5,ox+p+50*mm)
    c.drawString(ox+p+55*mm,y,"Módulo:"); fline(ox+p+72*mm,y-0.5,ox+cw-p)
    # ===== DESENHO — PLANTA EM "L" (vista de cima) do armário de canto =====
    S=78*mm; d=30*mm
    bx=ox+(cw-S)/2; by=y-8*mm-S
    pts=[(bx,by),(bx+d,by),(bx+d,by+S-d),(bx+S,by+S-d),(bx+S,by+S),(bx,by+S)]
    pth=c.beginPath(); pth.moveTo(*pts[0])
    for q in pts[1:]: pth.lineTo(*q)
    pth.close()
    c.setFillColor(colors.HexColor("#efe9df")); c.setStrokeColor(colors.HexColor("#555")); c.setLineWidth(1.0)
    c.drawPath(pth,fill=1,stroke=1)
    # paredes (hachura nas 2 costas: topo e esquerda)
    c.setStrokeColor(colors.HexColor("#888")); c.setLineWidth(0.5)
    ht=2.5*mm
    xx=bx
    while xx<bx+S:
        c.line(xx,by+S,xx+ht,by+S+ht); xx+=3.0*mm
    yy=by
    while yy<by+S:
        c.line(bx,yy,bx-ht,yy+ht); yy+=3.0*mm
    # frente (diagonal opcional, tracejada) atravessando o canto interno
    c.setDash(2.5,2.5); c.setStrokeColor(colors.HexColor("#b06a3a")); c.setLineWidth(0.8)
    c.line(bx+d,by,bx+S,by+S-d)
    c.setDash()
    c.setFont("Helvetica-Oblique",6.5); c.setFillColor(GREY)
    c.drawCentredString(bx+S*0.62,by+S*0.60,"vista de cima")
    c.setFillColor(colors.black)
    y=by-8*mm
    g=14.5*mm
    # ===== MEDIDAS =====
    lab(ox+p,y,"Altura:"); fline(ox+p+15*mm,y-0.5,ox+p+30*mm)
    lab(ox+p+33*mm,y,"Profund.:"); fline(ox+p+52*mm,y-0.5,ox+cw-p-7*mm); unit(ox+cw-p-5*mm,y)
    y-=g
    lab(ox+p,y,"Lado A:"); fline(ox+p+14*mm,y-0.5,ox+p+30*mm)
    lab(ox+p+34*mm,y,"Lado B:"); fline(ox+p+48*mm,y-0.5,ox+cw-p-7*mm); unit(ox+cw-p-5*mm,y)
    y-=g
    lab(ox+p,y,"Tipo:")
    xx=chk(ox+p+12*mm,y-1.6,"Reto (L)"); xx=chk(xx,y-1.6,"Diagonal"); chk(xx,y-1.6,"Giratório")
    y-=g
    lab(ox+p,y,"Tamponam.:")
    c.setFont("Helvetica",7); c.drawString(ox+p+22*mm,y,"L"); fline(ox+p+25*mm,y-0.5,ox+p+34*mm)
    c.drawString(ox+p+35*mm,y,"C"); fline(ox+p+38*mm,y-0.5,ox+p+47*mm)
    xx=chk(ox+p+50*mm,y-1.6,"15"); xx=chk(xx,y-1.6,"6"); chk(xx,y-1.6,"18")
    y-=g
    lab(ox+p,y,"Acabam.:")
    c.setFont("Helvetica",7); c.drawString(ox+p+22*mm,y,"L"); fline(ox+p+25*mm,y-0.5,ox+p+34*mm)
    c.drawString(ox+p+35*mm,y,"C"); fline(ox+p+38*mm,y-0.5,ox+p+47*mm)
    xx=chk(ox+p+50*mm,y-1.6,"15"); xx=chk(xx,y-1.6,"6"); chk(xx,y-1.6,"18")
    y-=g
    lab(ox+p,y,"Porta:")
    fline(ox+p+13*mm,y-0.5,ox+p+27*mm)
    xx=chk(ox+p+29*mm,y-1.6,"15"); xx=chk(xx,y-1.6,"18"); xx=chk(xx,y-1.6,"Provençal"); xx=chk(xx,y-1.6,"Vidro"); chk(xx,y-1.6,"Correr")
    y-=g
    lab(ox+p,y,"Prat/Div:")
    xx=chk(ox+p+18*mm,y-1.6,"15"); xx=chk(xx,y-1.6,"18")
    lab(xx+1*mm,y,"Qtd:"); fline(xx+12*mm,y-0.5,ox+cw-p)
    y-=g
    lab(ox+p,y,"Fundo:")
    xx=chk(ox+p+14*mm,y-1.6,"Sim"); xx=chk(xx,y-1.6,"Não")
    lab(xx+1*mm,y,"LED:")
    xx=chk(xx+11*mm,y-1.6,"Sim"); chk(xx,y-1.6,"Não")
    y-=g
    lab(ox+p,y,"Puxador:"); fline(ox+p+18*mm,y-0.5,ox+cw-p)
    y-=g
    lab(ox+p,y,"Ferragens:"); fline(ox+p+21*mm,y-0.5,ox+cw-p)
    y-=g
    lab(ox+p,y,"Obs:"); fline(ox+p+11*mm,y-0.5,ox+cw-p)
    fline(ox+p,y-9*mm,ox+cw-p)

cw,ch=W/2,H
for cx in (0,cw):
    card(cx,0,cw,ch)
c.setStrokeColor(colors.HexColor("#cccccc")); c.setLineWidth(0.5); c.setDash(3,3)
c.line(cw,0,cw,H); c.setDash()
c.showPage(); c.save(); print("PDF:",OUT)
