#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
OUT="/home/user/valvicorcamentista/.claude/skills/projeto-producao/ferramentas/folha_modulacao_4up.pdf"
LOGO="/tmp/claude-0/-home-user-valvicorcamentista/1d917bda-5670-5e8e-99d3-c980f393e67a/scratchpad/logo_clean.png"
W,H=A4
NAVY=colors.HexColor("#1F3A5F"); GREY=colors.HexColor("#777"); LINE=colors.HexColor("#c4c4c4")
TOPF=colors.HexColor("#e9e9e9"); SIDEF=colors.HexColor("#dcdcdc")
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
    p.close(); c.setFillColor(fill); c.setStrokeColor(colors.HexColor("#7d7d7d")); c.setLineWidth(0.8); c.drawPath(p,fill=1,stroke=1)

def card(ox,oy,cw,ch):
    p=4*mm
    img=ImageReader(LOGO); iw,ih=img.getSize(); lw=28*mm; lh=lw*ih/iw
    c.drawImage(img,ox+p,oy+ch-p-lh,width=lw,height=lh,mask='auto')
    c.setFont("Helvetica",5.5); c.setFillColor(GREY); c.drawRightString(ox+cw-p,oy+ch-p-3,"FOLHA DE MODULAÇÃO")
    y=oy+ch-p-lh-4*mm
    c.setFont("Helvetica",7); c.setFillColor(colors.black)
    c.drawString(ox+p,y,"Pedido:"); fline(ox+p+13*mm,y-0.5,ox+p+38*mm)
    c.drawString(ox+p+42*mm,y,"Módulo:"); fline(ox+p+56*mm,y-0.5,ox+cw-p)
    # ===== DESENHO 3D (iso) estreito, sem escritas =====
    fw,fh=38*mm,21*mm; ddx,ddy=9*mm,6*mm
    bx=ox+(cw-(fw+ddx))/2; by=y-7*mm-(fh+ddy)
    # topo e lateral (atrás)
    quad([(bx,by+fh),(bx+fw,by+fh),(bx+fw+ddx,by+fh+ddy),(bx+ddx,by+fh+ddy)],TOPF)         # topo
    quad([(bx+fw,by),(bx+fw+ddx,by+ddy),(bx+fw+ddx,by+fh+ddy),(bx+fw,by+fh)],SIDEF)         # lateral dir
    # frente (caixa aberta -> mostra fundo recuado)
    c.setFillColor(colors.white); c.setStrokeColor(colors.black); c.setLineWidth(1.1); c.rect(bx,by,fw,fh,fill=1)
    inn=3.0*mm
    c.setStrokeColor(colors.HexColor("#aaaaaa")); c.setLineWidth(0.6); c.rect(bx+inn,by+inn,fw-2*inn,fh-2*inn)
    y=by-5*mm
    # ===== MEDIDAS =====
    c.setFont("Helvetica-Bold",7); c.setFillColor(colors.black)
    c.drawString(ox+p,y,"Alt"); fline(ox+p+8*mm,y-0.5,ox+p+24*mm)
    c.drawString(ox+p+27*mm,y,"Larg"); fline(ox+p+37*mm,y-0.5,ox+p+53*mm)
    c.drawString(ox+p+56*mm,y,"Prof"); fline(ox+p+66*mm,y-0.5,ox+cw-p-6*mm)
    c.setFont("Helvetica",6); c.setFillColor(GREY); c.drawRightString(ox+cw-p,y,"mm")
    y-=6*mm; c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Tamponam.:")
    c.setFont("Helvetica",6.5); c.drawString(ox+p+20*mm,y,"L"); fline(ox+p+23*mm,y-0.5,ox+p+32*mm)
    c.drawString(ox+p+33*mm,y,"C"); fline(ox+p+36*mm,y-0.5,ox+p+45*mm)
    xx=chk(ox+p+48*mm,y-1.5,"15"); xx=chk(xx,y-1.5,"6"); chk(xx,y-1.5,"18")
    y-=6*mm
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Acabam.:")
    c.setFont("Helvetica",6.5); c.drawString(ox+p+20*mm,y,"L"); fline(ox+p+23*mm,y-0.5,ox+p+32*mm)
    c.drawString(ox+p+33*mm,y,"C"); fline(ox+p+36*mm,y-0.5,ox+p+45*mm)
    xx=chk(ox+p+48*mm,y-1.5,"15"); xx=chk(xx,y-1.5,"6"); chk(xx,y-1.5,"18")
    y-=6*mm
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Fundo:")
    xx=chk(ox+p+12*mm,y-1.5,"Sim"); xx=chk(xx,y-1.5,"Não")
    c.setFont("Helvetica-Bold",6.8); c.drawString(xx+1*mm,y,"LED:")
    xx=chk(xx+9*mm,y-1.5,"Sim"); chk(xx,y-1.5,"Não")
    y-=6*mm
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Prat/Div:")
    chk(ox+p+16*mm,y-1.5,"15");
    xx=chk(ox+p+16*mm,y-1.5,"15"); chk(xx,y-1.5,"18")
    y-=6*mm
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Puxador:"); fline(ox+p+15*mm,y-0.5,ox+cw-p)
    y-=6*mm
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Ferragens:"); fline(ox+p+17*mm,y-0.5,ox+cw-p)
    y-=6*mm
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Obs:"); fline(ox+p+9*mm,y-0.5,ox+cw-p)

cw,ch=W/2,H/2
for cx in (0,cw):
    for cy in (0,ch): card(cx,cy,cw,ch)
c.setStrokeColor(colors.HexColor("#cccccc")); c.setLineWidth(0.5); c.setDash(3,3)
c.line(cw,0,cw,H); c.line(0,ch,W,ch); c.setDash()
c.showPage(); c.save(); print("PDF:",OUT)
