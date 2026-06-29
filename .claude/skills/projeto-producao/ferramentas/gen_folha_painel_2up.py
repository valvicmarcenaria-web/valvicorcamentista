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
def lab(x,y,t): c.setFont("Helvetica-Bold",7.6); c.setFillColor(colors.black); c.drawString(x,y,t)
def unit(x,y,t="mm"):
    c.setFont("Helvetica",7); c.setFillColor(GREY); c.drawString(x,y,t); c.setFillColor(colors.black)

def card(ox,oy,cw,ch):
    p=6*mm
    img=ImageReader(LOGO); iw,ih=img.getSize(); lw=36*mm; lh=lw*ih/iw
    c.drawImage(img,ox+p,oy+ch-p-lh,width=lw,height=lh,mask='auto')
    c.setFont("Helvetica",7); c.setFillColor(GREY); c.drawRightString(ox+cw-p,oy+ch-p-4,"FOLHA DE MODULAÇÃO — PAINEL")
    y=oy+ch-p-lh-6*mm
    c.setFont("Helvetica",9); c.setFillColor(colors.black)
    c.drawString(ox+p,y,"Pedido:"); fline(ox+p+16*mm,y-0.5,ox+p+50*mm)
    c.drawString(ox+p+55*mm,y,"Módulo:"); fline(ox+p+72*mm,y-0.5,ox+cw-p)
    # ===== DESENHO — CHAPA DE MDF LISA (espaço p/ o marceneiro desenhar a ripa) =====
    w_,h_=64*mm,80*mm
    bx=ox+(cw-w_)/2; by=y-8*mm-h_
    c.setFillColor(colors.HexColor("#efe9df")); c.setStrokeColor(colors.HexColor("#555")); c.setLineWidth(1.0)
    c.rect(bx,by,w_,h_,fill=1,stroke=1)                       # chapa lisa
    y=by-8*mm
    g=14*mm
    # ===== MEDIDAS =====
    lab(ox+p,y,"Alt"); fline(ox+p+9*mm,y-0.5,ox+p+24*mm)
    lab(ox+p+27*mm,y,"Larg"); fline(ox+p+38*mm,y-0.5,ox+p+52*mm)
    lab(ox+p+55*mm,y,"Esp."); fline(ox+p+63*mm,y-0.5,ox+cw-p-7*mm); unit(ox+cw-p-5*mm,y)
    y-=g
    lab(ox+p,y,"Ripado:")
    xx=chk(ox+p+15*mm,y-1.6,"Sim"); chk(xx,y-1.6,"Não")
    y-=g
    lab(ox+p,y,"Larg. ripa:"); fline(ox+p+20*mm,y-0.5,ox+p+31*mm)
    lab(ox+p+34*mm,y,"Friso:"); fline(ox+p+45*mm,y-0.5,ox+p+55*mm)
    lab(ox+p+58*mm,y,"Prof.:"); fline(ox+p+68*mm,y-0.5,ox+cw-p-7*mm); unit(ox+cw-p-5*mm,y)
    y-=g
    lab(ox+p,y,"Acabam.:")
    xx=chk(ox+p+18*mm,y-1.6,"Lâmina"); xx=chk(xx,y-1.6,"Melamínico"); chk(xx,y-1.6,"Laca")
    y-=g
    lab(ox+p,y,"Material:"); fline(ox+p+19*mm,y-0.5,ox+cw-p)
    y-=g
    lab(ox+p,y,"Rodapé:")
    xx=chk(ox+p+16*mm,y-1.6,"Alumínio"); xx=chk(xx,y-1.6,"MDF Ultra")
    lab(xx+1*mm,y,"Alt:"); fline(xx+8*mm,y-0.5,xx+20*mm)
    lab(xx+22*mm,y,"Recuo:"); fline(xx+34*mm,y-0.5,ox+cw-p)
    y-=g
    lab(ox+p,y,"Arremate:")
    xx=chk(ox+p+18*mm,y-1.6,"Sim"); xx=chk(xx,y-1.6,"Não")
    lab(xx+1*mm,y,"Alt:"); fline(xx+8*mm,y-0.5,xx+20*mm)
    lab(xx+22*mm,y,"Recuo:"); fline(xx+34*mm,y-0.5,ox+cw-p)
    y-=g
    lab(ox+p,y,"Encaixe/Fixação:"); fline(ox+p+32*mm,y-0.5,ox+cw-p)
    y-=g
    lab(ox+p,y,"Usinagem esp.:")
    xx=chk(ox+p+30*mm,y-1.6,"Sim"); chk(xx,y-1.6,"Não")
    y-=g
    lab(ox+p,y,"Qual usinagem:"); fline(ox+p+30*mm,y-0.5,ox+cw-p)
    y-=g
    lab(ox+p,y,"LED:")
    xx=chk(ox+p+11*mm,y-1.6,"Sim"); chk(xx,y-1.6,"Não")
    y-=g
    lab(ox+p,y,"Obs:"); fline(ox+p+11*mm,y-0.5,ox+cw-p)
    fline(ox+p,y-9*mm,ox+cw-p)

cw,ch=W/2,H
for cx in (0,cw):
    card(cx,0,cw,ch)
c.setStrokeColor(colors.HexColor("#cccccc")); c.setLineWidth(0.5); c.setDash(3,3)
c.line(cw,0,cw,H); c.setDash()
c.showPage(); c.save(); print("PDF:",OUT)
