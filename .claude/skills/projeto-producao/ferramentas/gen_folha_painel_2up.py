#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
OUT="/home/user/valvicorcamentista/.claude/skills/projeto-producao/ferramentas/folha_modulacao_painel_2up.pdf"
LOGO="/tmp/claude-0/-home-user-valvicorcamentista/1d917bda-5670-5e8e-99d3-c980f393e67a/scratchpad/logo_clean.png"
W,H=A4
NAVY=colors.HexColor("#1F3A5F"); GREY=colors.HexColor("#777"); LINE=colors.HexColor("#c4c4c4")
c=canvas.Canvas(OUT,pagesize=A4)

def chk(xx,yy,txt,s=3.0*mm,fs=7.0):
    c.setLineWidth(0.9); c.setStrokeColor(colors.black); c.rect(xx,yy,s,s)
    c.setFont("Helvetica",fs); c.setFillColor(colors.black); c.drawString(xx+s+1.6,yy+0.5,txt)
    return xx+s+1.6+c.stringWidth(txt,"Helvetica",fs)+3*mm
def fline(xx,yy,x2):
    c.setStrokeColor(LINE); c.setLineWidth(0.7); c.line(xx,yy,x2,yy)
def quad(pts,fill,stroke="#9a9a9a"):
    p=c.beginPath(); p.moveTo(*pts[0])
    for q in pts[1:]: p.lineTo(*q)
    p.close(); c.setFillColor(fill); c.setStrokeColor(colors.HexColor(stroke)); c.setLineWidth(0.6); c.drawPath(p,fill=1,stroke=1)
def lab(x,y,t): c.setFont("Helvetica-Bold",7.6); c.setFillColor(colors.black); c.drawString(x,y,t)

def card(ox,oy,cw,ch):
    p=6*mm
    img=ImageReader(LOGO); iw,ih=img.getSize(); lw=36*mm; lh=lw*ih/iw
    c.drawImage(img,ox+p,oy+ch-p-lh,width=lw,height=lh,mask='auto')
    c.setFont("Helvetica",7); c.setFillColor(GREY); c.drawRightString(ox+cw-p,oy+ch-p-4,"FOLHA DE MODULAÇÃO — PAINEL")
    y=oy+ch-p-lh-6*mm
    c.setFont("Helvetica",9); c.setFillColor(colors.black)
    c.drawString(ox+p,y,"Pedido:"); fline(ox+p+16*mm,y-0.5,ox+p+50*mm)
    c.drawString(ox+p+55*mm,y,"Módulo:"); fline(ox+p+72*mm,y-0.5,ox+cw-p)
    # ===== DESENHO — PAINEL RIPADO (vista frontal + leve 3D) =====
    w_,h_=48*mm,52*mm; ddx,ddy=8*mm,6*mm
    bx=ox+(cw-(w_+ddx))/2; by=y-8*mm-(h_+ddy)
    Cc=(bx+w_,by+h_); D=(bx,by+h_); B=(bx+w_,by)
    quad([D,Cc,(Cc[0]+ddx,Cc[1]+ddy),(D[0]+ddx,D[1]+ddy)],colors.HexColor("#e0e0e0"))  # topo
    quad([B,Cc,(Cc[0]+ddx,Cc[1]+ddy),(B[0]+ddx,B[1]+ddy)],colors.HexColor("#cccccc"))  # lateral dir
    # frente (fundo escuro = sombra dos frisos)
    c.setFillColor(colors.HexColor("#c4c4c4")); c.setStrokeColor(colors.HexColor("#555")); c.setLineWidth(0.8)
    c.rect(bx,by,w_,h_,fill=1,stroke=1)
    # ripas verticais (slats claras, deixando o friso = sombra entre elas)
    m=2.2*mm; n=9; fr=1.3*mm
    uw=w_-2*m; rw=(uw-(n-1)*fr)/n
    c.setStrokeColor(colors.HexColor("#9b9b9b")); c.setLineWidth(0.4)
    for k in range(n):
        rx=bx+m+k*(rw+fr)
        c.setFillColor(colors.HexColor("#efefef")); c.rect(rx,by+m,rw,h_-2*m,fill=1,stroke=1)
    y=by-8*mm
    g=11.6*mm
    # ===== MEDIDAS =====
    lab(ox+p,y,"Alt"); fline(ox+p+9*mm,y-0.5,ox+p+24*mm)
    lab(ox+p+27*mm,y,"Larg"); fline(ox+p+38*mm,y-0.5,ox+p+52*mm)
    lab(ox+p+55*mm,y,"Esp."); fline(ox+p+63*mm,y-0.5,ox+cw-p-7*mm)
    c.setFont("Helvetica",7); c.setFillColor(GREY); c.drawRightString(ox+cw-p,y,"mm"); c.setFillColor(colors.black)
    y-=g
    lab(ox+p,y,"Ripado:")
    xx=chk(ox+p+15*mm,y-1.6,"Sim"); xx=chk(xx,y-1.6,"Não")
    lab(xx+1*mm,y,"Larg. ripa:"); fline(xx+20*mm,y-0.5,ox+cw-p-7*mm)
    c.setFont("Helvetica",7); c.setFillColor(GREY); c.drawRightString(ox+cw-p,y,"mm"); c.setFillColor(colors.black)
    y-=g
    lab(ox+p,y,"Friso:"); fline(ox+p+11*mm,y-0.5,ox+p+30*mm)
    c.setFont("Helvetica",7); c.setFillColor(GREY); c.drawString(ox+p+31*mm,y,"mm"); c.setFillColor(colors.black)
    lab(ox+p+42*mm,y,"Prof. ripa:"); fline(ox+p+62*mm,y-0.5,ox+cw-p-7*mm)
    c.setFont("Helvetica",7); c.setFillColor(GREY); c.drawRightString(ox+cw-p,y,"mm"); c.setFillColor(colors.black)
    y-=g
    lab(ox+p,y,"Acabam.:")
    xx=chk(ox+p+18*mm,y-1.6,"Lâmina"); xx=chk(xx,y-1.6,"Melam."); xx=chk(xx,y-1.6,"Laca"); chk(xx,y-1.6,"Pintura")
    y-=g
    lab(ox+p,y,"Lâmina/cor:"); fline(ox+p+24*mm,y-0.5,ox+cw-p)
    y-=g
    lab(ox+p,y,"Rodapé:")
    xx=chk(ox+p+16*mm,y-1.6,"Alumínio"); xx=chk(xx,y-1.6,"MDF Ultra")
    lab(xx+1*mm,y,"Alt.:"); fline(xx+10*mm,y-0.5,ox+cw-p-7*mm)
    c.setFont("Helvetica",7); c.setFillColor(GREY); c.drawRightString(ox+cw-p,y,"mm"); c.setFillColor(colors.black)
    y-=g
    lab(ox+p,y,"Arremate:")
    xx=chk(ox+p+18*mm,y-1.6,"Sim"); xx=chk(xx,y-1.6,"Não")
    lab(xx+1*mm,y,"Alt.:"); fline(xx+10*mm,y-0.5,ox+cw-p-7*mm)
    c.setFont("Helvetica",7); c.setFillColor(GREY); c.drawRightString(ox+cw-p,y,"mm"); c.setFillColor(colors.black)
    y-=g
    lab(ox+p,y,"Encaixe/Fixação:"); fline(ox+p+32*mm,y-0.5,ox+cw-p)
    y-=g
    lab(ox+p,y,"Usinagem esp.:")
    xx=chk(ox+p+30*mm,y-1.6,"Sim"); chk(xx,y-1.6,"Não")
    y-=g
    lab(ox+p,y,"Qual usinagem:"); fline(ox+p+30*mm,y-0.5,ox+cw-p)
    y-=g
    lab(ox+p,y,"LED:")
    xx=chk(ox+p+11*mm,y-1.6,"Sim"); xx=chk(xx,y-1.6,"Não")
    lab(xx+1*mm,y,"Fundo:")
    xx=chk(xx+13*mm,y-1.6,"Sim"); chk(xx,y-1.6,"Não")
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
