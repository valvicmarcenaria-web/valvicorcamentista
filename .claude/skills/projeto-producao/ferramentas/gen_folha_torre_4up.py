#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
OUT="/home/user/valvicorcamentista/.claude/skills/projeto-producao/ferramentas/folha_modulacao_torre_4up.pdf"
LOGO="/tmp/claude-0/-home-user-valvicorcamentista/1d917bda-5670-5e8e-99d3-c980f393e67a/scratchpad/logo_clean.png"
W,H=A4
NAVY=colors.HexColor("#1F3A5F"); GREY=colors.HexColor("#777"); LINE=colors.HexColor("#c4c4c4")
c=canvas.Canvas(OUT,pagesize=A4)

def chk(xx,yy,txt,s=2.8*mm,fs=6.5):
    c.setLineWidth(0.8); c.setStrokeColor(colors.black); c.rect(xx,yy,s,s)
    c.setFont("Helvetica",fs); c.setFillColor(colors.black); c.drawString(xx+s+1.5,yy+0.4,txt)
    return xx+s+1.5+c.stringWidth(txt,"Helvetica",fs)+3*mm
def fline(xx,yy,x2):
    c.setStrokeColor(LINE); c.setLineWidth(0.6); c.line(xx,yy,x2,yy)
def quad(pts,fill):
    p=c.beginPath(); p.moveTo(*pts[0])
    for q in pts[1:]: p.lineTo(*q)
    p.close(); c.setFillColor(fill); c.setStrokeColor(colors.HexColor("#9a9a9a")); c.setLineWidth(0.5); c.drawPath(p,fill=1,stroke=1)

def card(ox,oy,cw,ch):
    p=4*mm
    img=ImageReader(LOGO); iw,ih=img.getSize(); lw=28*mm; lh=lw*ih/iw
    c.drawImage(img,ox+p,oy+ch-p-lh,width=lw,height=lh,mask='auto')
    c.setFont("Helvetica",5.5); c.setFillColor(GREY); c.drawRightString(ox+cw-p,oy+ch-p-3,"FOLHA DE MODULAÇÃO — TORRE")
    y=oy+ch-p-lh-4*mm
    c.setFont("Helvetica",7); c.setFillColor(colors.black)
    c.drawString(ox+p,y,"Pedido:"); fline(ox+p+13*mm,y-0.5,ox+p+38*mm)
    c.drawString(ox+p+42*mm,y,"Módulo:"); fline(ox+p+56*mm,y-0.5,ox+cw-p)
    # ===== DESENHO 3D iso — TORRE (armário alto vertical, paredes finas MDF) =====
    w_,h_=22*mm,30*mm; ddx,ddy=7*mm,4.5*mm; t=1.2*mm
    bx=ox+(cw-(w_+ddx))/2; by=y-6*mm-(h_+ddy)
    A=(bx,by);B=(bx+w_,by);Cc=(bx+w_,by+h_);D=(bx,by+h_)
    A2=(bx+ddx,by+ddy);B2=(bx+w_+ddx,by+ddy);C2=(bx+w_+ddx,by+h_+ddy);D2=(bx+ddx,by+h_+ddy)
    quad([A2,B2,C2,D2],colors.HexColor("#f3f3f3"))   # fundo (parede de trás)
    quad([D,Cc,C2,D2],colors.HexColor("#ededed"))    # topo
    quad([A,D,D2,A2],colors.HexColor("#eeeeee"))     # lateral esq (interna)
    quad([B,Cc,C2,B2],colors.HexColor("#dcdcdc"))    # lateral dir
    quad([A,B,B2,A2],colors.HexColor("#e7e7e7"))     # base
    # arestas de trás
    c.setStrokeColor(colors.HexColor("#666")); c.setLineWidth(0.5)
    for a,b in [(B,B2),(Cc,C2),(D,D2),(A,A2)]: c.line(*a,*b)
    # frente = abertura, com a espessura fina da chapa (parece MDF)
    c.setLineWidth(0.6); c.setStrokeColor(colors.HexColor("#555"))
    c.rect(bx,by,w_,h_)                              # contorno externo da frente
    c.setLineWidth(0.4); c.setStrokeColor(colors.HexColor("#888"))
    c.rect(bx+t,by+t,w_-2*t,h_-2*t)                 # contorno interno = espessura
    y=by-6*mm
    # ===== MEDIDAS =====
    c.setFont("Helvetica-Bold",7); c.setFillColor(colors.black)
    c.drawString(ox+p,y,"Alt"); fline(ox+p+8*mm,y-0.5,ox+p+24*mm)
    c.drawString(ox+p+27*mm,y,"Larg"); fline(ox+p+37*mm,y-0.5,ox+p+53*mm)
    c.drawString(ox+p+56*mm,y,"Prof"); fline(ox+p+66*mm,y-0.5,ox+cw-p-6*mm)
    c.setFont("Helvetica",6); c.setFillColor(GREY); c.drawRightString(ox+cw-p,y,"mm")
    g=7.0*mm
    y-=g; c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Tamponam.:")
    c.setFont("Helvetica",6.5); c.drawString(ox+p+20*mm,y,"L"); fline(ox+p+23*mm,y-0.5,ox+p+32*mm)
    c.drawString(ox+p+33*mm,y,"C"); fline(ox+p+36*mm,y-0.5,ox+p+45*mm)
    xx=chk(ox+p+48*mm,y-1.5,"15"); xx=chk(xx,y-1.5,"6"); chk(xx,y-1.5,"18")
    y-=g
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Acabam.:")
    c.setFont("Helvetica",6.5); c.drawString(ox+p+20*mm,y,"L"); fline(ox+p+23*mm,y-0.5,ox+p+32*mm)
    c.drawString(ox+p+33*mm,y,"C"); fline(ox+p+36*mm,y-0.5,ox+p+45*mm)
    xx=chk(ox+p+48*mm,y-1.5,"15"); xx=chk(xx,y-1.5,"6"); chk(xx,y-1.5,"18")
    y-=g
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Porta:")
    fline(ox+p+11*mm,y-0.5,ox+p+26*mm)
    xx=chk(ox+p+28*mm,y-1.5,"15"); xx=chk(xx,y-1.5,"18"); xx=chk(xx,y-1.5,"Provençal"); xx=chk(xx,y-1.5,"Vidro"); chk(xx,y-1.5,"Correr")
    y-=g
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Vão Forno:")
    fline(ox+p+18*mm,y-0.5,ox+cw-p-6*mm)
    c.setFont("Helvetica",6); c.setFillColor(GREY); c.drawRightString(ox+cw-p,y,"mm")
    c.setFillColor(colors.black)
    y-=g
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Vão Microond.:")
    fline(ox+p+24*mm,y-0.5,ox+cw-p-6*mm)
    c.setFont("Helvetica",6); c.setFillColor(GREY); c.drawRightString(ox+cw-p,y,"mm")
    c.setFillColor(colors.black)
    y-=g
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Gaveteiro:")
    xx=chk(ox+p+17*mm,y-1.5,"Sim"); xx=chk(xx,y-1.5,"Não")
    c.setFont("Helvetica-Bold",6.8); c.drawString(xx+1*mm,y,"Qtd gav.:"); fline(xx+17*mm,y-0.5,ox+cw-p)
    y-=g
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Sapateira:")
    xx=chk(ox+p+17*mm,y-1.5,"Sim"); xx=chk(xx,y-1.5,"Não")
    c.setFont("Helvetica-Bold",6.8); c.drawString(xx+1*mm,y,"Qtd:"); fline(xx+10*mm,y-0.5,ox+cw-p)
    y-=g
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Prat/Div:")
    xx=chk(ox+p+16*mm,y-1.5,"15"); xx=chk(xx,y-1.5,"18")
    c.setFont("Helvetica",6.5); c.setFillColor(colors.black); c.drawString(xx+1*mm,y,"Qtd:"); fline(xx+10*mm,y-0.5,ox+cw-p)
    y-=g
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Puxador:"); fline(ox+p+15*mm,y-0.5,ox+cw-p)
    y-=g
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Ferragens:"); fline(ox+p+17*mm,y-0.5,ox+cw-p)
    y-=g
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Obs:"); fline(ox+p+9*mm,y-0.5,ox+cw-p)

cw,ch=W/2,H/2
for cx in (0,cw):
    for cy in (0,ch): card(cx,cy,cw,ch)
c.setStrokeColor(colors.HexColor("#cccccc")); c.setLineWidth(0.5); c.setDash(3,3)
c.line(cw,0,cw,H); c.line(0,ch,W,ch); c.setDash()
c.showPage(); c.save(); print("PDF:",OUT)
