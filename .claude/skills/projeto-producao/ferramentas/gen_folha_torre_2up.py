#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os
_B=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(_B,"folha_modulacao_torre_2up.pdf")
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
def quad(pts,fill):
    p=c.beginPath(); p.moveTo(*pts[0])
    for q in pts[1:]: p.lineTo(*q)
    p.close(); c.setFillColor(fill); c.setStrokeColor(colors.HexColor("#9a9a9a")); c.setLineWidth(0.6); c.drawPath(p,fill=1,stroke=1)
def lab(x,y,t): c.setFont("Helvetica-Bold",7.6); c.setFillColor(colors.black); c.drawString(x,y,t)

def card(ox,oy,cw,ch):
    p=6*mm
    img=ImageReader(LOGO); iw,ih=img.getSize(); lw=36*mm; lh=lw*ih/iw
    c.drawImage(img,ox+p,oy+ch-p-lh,width=lw,height=lh,mask='auto')
    c.setFont("Helvetica",7); c.setFillColor(GREY); c.drawRightString(ox+cw-p,oy+ch-p-4,"FOLHA DE MODULAÇÃO — TORRE")
    y=oy+ch-p-lh-6*mm
    c.setFont("Helvetica",9); c.setFillColor(colors.black)
    c.drawString(ox+p,y,"Pedido:"); fline(ox+p+16*mm,y-0.5,ox+p+50*mm)
    c.drawString(ox+p+55*mm,y,"Módulo:"); fline(ox+p+72*mm,y-0.5,ox+cw-p)
    # ===== DESENHO 3D iso — TORRE (armário alto vertical, paredes finas MDF) =====
    w_,h_=38*mm,55*mm; ddx,ddy=12*mm,8*mm; t=1.8*mm
    bx=ox+(cw-(w_+ddx))/2; by=y-8*mm-(h_+ddy)
    A=(bx,by);B=(bx+w_,by);Cc=(bx+w_,by+h_);D=(bx,by+h_)
    A2=(bx+ddx,by+ddy);B2=(bx+w_+ddx,by+ddy);C2=(bx+w_+ddx,by+h_+ddy);D2=(bx+ddx,by+h_+ddy)
    quad([A2,B2,C2,D2],colors.HexColor("#f3f3f3"))   # fundo (parede de trás)
    quad([D,Cc,C2,D2],colors.HexColor("#ededed"))    # topo
    quad([A,D,D2,A2],colors.HexColor("#eeeeee"))     # lateral esq (interna)
    quad([B,Cc,C2,B2],colors.HexColor("#dcdcdc"))    # lateral dir
    quad([A,B,B2,A2],colors.HexColor("#e7e7e7"))     # base
    c.setStrokeColor(colors.HexColor("#666")); c.setLineWidth(0.6)
    for a,b in [(B,B2),(Cc,C2),(D,D2),(A,A2)]: c.line(*a,*b)
    c.setLineWidth(0.8); c.setStrokeColor(colors.HexColor("#555"))
    c.rect(bx,by,w_,h_)                              # contorno externo da frente
    c.setLineWidth(0.5); c.setStrokeColor(colors.HexColor("#888"))
    c.rect(bx+t,by+t,w_-2*t,h_-2*t)                 # contorno interno = espessura
    y=by-8*mm
    g=12*mm
    # ===== MEDIDAS =====
    lab(ox+p,y,"Alt"); fline(ox+p+9*mm,y-0.5,ox+p+26*mm)
    lab(ox+p+29*mm,y,"Larg"); fline(ox+p+40*mm,y-0.5,ox+p+56*mm)
    lab(ox+p+59*mm,y,"Prof"); fline(ox+p+70*mm,y-0.5,ox+cw-p-7*mm)
    c.setFont("Helvetica",7); c.setFillColor(GREY); c.drawRightString(ox+cw-p,y,"mm"); c.setFillColor(colors.black)
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
    lab(ox+p,y,"Base:")
    xx=chk(ox+p+13*mm,y-1.6,"Sim"); xx=chk(xx,y-1.6,"Não")
    lab(xx+1*mm,y,"Recuo:")
    xx=chk(xx+13*mm,y-1.6,"Sim"); xx=chk(xx,y-1.6,"Não")
    fline(xx,y-0.5,ox+cw-p-7*mm)
    c.setFont("Helvetica",7); c.setFillColor(GREY); c.drawRightString(ox+cw-p,y,"mm"); c.setFillColor(colors.black)
    y-=g
    lab(ox+p,y,"Acab. base:"); fline(ox+p+24*mm,y-0.5,ox+cw-p)
    y-=g
    lab(ox+p,y,"Porta:")
    fline(ox+p+13*mm,y-0.5,ox+p+27*mm)
    xx=chk(ox+p+29*mm,y-1.6,"15"); xx=chk(xx,y-1.6,"18"); xx=chk(xx,y-1.6,"Provençal"); xx=chk(xx,y-1.6,"Vidro"); chk(xx,y-1.6,"Correr")
    y-=g
    lab(ox+p,y,"Vão Forno:"); fline(ox+p+22*mm,y-0.5,ox+cw-p-7*mm)
    c.setFont("Helvetica",7); c.setFillColor(GREY); c.drawRightString(ox+cw-p,y,"mm"); c.setFillColor(colors.black)
    y-=g
    lab(ox+p,y,"Vão Microond.:"); fline(ox+p+29*mm,y-0.5,ox+cw-p-7*mm)
    c.setFont("Helvetica",7); c.setFillColor(GREY); c.drawRightString(ox+cw-p,y,"mm"); c.setFillColor(colors.black)
    y-=g
    lab(ox+p,y,"Gaveteiro:")
    xx=chk(ox+p+20*mm,y-1.6,"Sim"); xx=chk(xx,y-1.6,"Não")
    lab(xx+1*mm,y,"Qtd gav.:"); fline(xx+20*mm,y-0.5,ox+cw-p)
    y-=g
    lab(ox+p,y,"Sapateira:")
    xx=chk(ox+p+20*mm,y-1.6,"Sim"); xx=chk(xx,y-1.6,"Não")
    lab(xx+1*mm,y,"Qtd:"); fline(xx+12*mm,y-0.5,ox+cw-p)
    y-=g
    lab(ox+p,y,"Fundo:")
    xx=chk(ox+p+14*mm,y-1.6,"Sim"); xx=chk(xx,y-1.6,"Não")
    lab(xx+1*mm,y,"LED:")
    xx=chk(xx+11*mm,y-1.6,"Sim"); chk(xx,y-1.6,"Não")
    y-=g
    lab(ox+p,y,"Prat/Div:")
    xx=chk(ox+p+18*mm,y-1.6,"15"); xx=chk(xx,y-1.6,"18")
    lab(xx+1*mm,y,"Qtd:"); fline(xx+12*mm,y-0.5,ox+cw-p)
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
