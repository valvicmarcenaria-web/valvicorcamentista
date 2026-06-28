#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
OUT="/home/user/valvicorcamentista/.claude/skills/projeto-producao/ferramentas/folha_modulacao_4up.pdf"
LOGO="/tmp/claude-0/-home-user-valvicorcamentista/1d917bda-5670-5e8e-99d3-c980f393e67a/scratchpad/logo_clean.png"
W,H=A4
NAVY=colors.HexColor("#1F3A5F"); GREY=colors.HexColor("#777"); LINE=colors.HexColor("#c4c4c4"); PANEL=colors.HexColor("#ededed")
c=canvas.Canvas(OUT,pagesize=A4)

def chk(xx,yy,txt,s=2.8*mm,fs=6.5):
    c.setLineWidth(0.8); c.setStrokeColor(colors.black); c.rect(xx,yy,s,s)
    c.setFont("Helvetica",fs); c.setFillColor(colors.black); c.drawString(xx+s+1.5,yy+0.4,txt)
    return xx+s+1.5+c.stringWidth(txt,"Helvetica",fs)+3*mm
def fline(xx,yy,x2):
    c.setStrokeColor(LINE); c.setLineWidth(0.6); c.line(xx,yy,x2,yy)

def card(ox,oy,cw,ch):
    p=4*mm
    # logo
    from reportlab.lib.utils import ImageReader
    img=ImageReader(LOGO); iw,ih=img.getSize(); lw=30*mm; lh=lw*ih/iw
    yc=oy+ch-p-lh
    c.drawImage(img,ox+p,yc,width=lw,height=lh,mask='auto')
    c.setFont("Helvetica",5.5); c.setFillColor(GREY)
    c.drawRightString(ox+cw-p,oy+ch-p-3, "FOLHA DE MODULAÇÃO")
    y=yc-4*mm
    c.setFont("Helvetica",7); c.setFillColor(colors.black)
    c.drawString(ox+p,y,"Pedido:"); fline(ox+p+13*mm,y-0.5,ox+p+38*mm)
    c.drawString(ox+p+42*mm,y,"Módulo:"); fline(ox+p+56*mm,y-0.5,ox+cw-p)
    y-=4*mm
    # desenho simples (sem escritas): laterais + base + testeira
    dw=cw-2*p; dh=24*mm; dx=ox+p; dy=y-dh; t=4.5*mm
    c.setFillColor(PANEL); c.setStrokeColor(colors.HexColor("#9a9a9a")); c.setLineWidth(0.8)
    c.rect(dx,dy,t,dh,fill=1)             # lateral esq
    c.rect(dx+dw-t,dy,t,dh,fill=1)        # lateral dir
    c.rect(dx,dy,dw,t,fill=1)            # base
    c.rect(dx,dy+dh-3*mm,dw,3*mm,fill=1)# testeira
    c.setStrokeColor(colors.black); c.setLineWidth(1); c.rect(dx,dy,dw,dh)
    y=dy-5*mm
    # medidas principais
    c.setFont("Helvetica-Bold",7); c.setFillColor(colors.black)
    c.drawString(ox+p,y,"Alt"); fline(ox+p+8*mm,y-0.5,ox+p+24*mm)
    c.drawString(ox+p+27*mm,y,"Larg"); fline(ox+p+37*mm,y-0.5,ox+p+53*mm)
    c.drawString(ox+p+56*mm,y,"Prof"); fline(ox+p+66*mm,y-0.5,ox+cw-p-6*mm)
    c.setFont("Helvetica",6); c.setFillColor(GREY); c.drawRightString(ox+cw-p,y,"mm")
    y-=6*mm
    c.setFillColor(colors.black)
    # tamponamento
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Tamponam.:")
    c.setFont("Helvetica",6.5)
    c.drawString(ox+p+20*mm,y,"L"); fline(ox+p+23*mm,y-0.5,ox+p+32*mm)
    c.drawString(ox+p+33*mm,y,"C"); fline(ox+p+36*mm,y-0.5,ox+p+45*mm)
    xx=chk(ox+p+48*mm,y-1.5,"15"); xx=chk(xx,y-1.5,"6"); chk(xx,y-1.5,"18")
    y-=6*mm
    # acabamento
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Acabam.:")
    c.setFont("Helvetica",6.5)
    c.drawString(ox+p+20*mm,y,"L"); fline(ox+p+23*mm,y-0.5,ox+p+32*mm)
    c.drawString(ox+p+33*mm,y,"C"); fline(ox+p+36*mm,y-0.5,ox+p+45*mm)
    xx=chk(ox+p+48*mm,y-1.5,"15"); xx=chk(xx,y-1.5,"6"); chk(xx,y-1.5,"18")
    y-=6*mm
    # fundo + prateleiras/divisorias (mesma linha)
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Fundo:")
    xx=chk(ox+p+12*mm,y-1.5,"Sim"); xx=chk(xx,y-1.5,"Não")
    c.setFont("Helvetica-Bold",6.8); c.drawString(xx+1*mm,y,"Prat/Div:")
    xx=chk(xx+16*mm,y-1.5,"15"); chk(xx,y-1.5,"18")
    y-=6*mm
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Puxador:"); fline(ox+p+15*mm,y-0.5,ox+cw-p)
    y-=6*mm
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Ferragens:"); fline(ox+p+17*mm,y-0.5,ox+cw-p)
    y-=6*mm
    c.setFont("Helvetica-Bold",6.8); c.drawString(ox+p,y,"Obs:"); fline(ox+p+9*mm,y-0.5,ox+cw-p)

# 2x2 grid + guias de corte
cw,ch=W/2,H/2
for cx in (0,cw):
    for cy in (0,ch):
        card(cx,cy,cw,ch)
c.setStrokeColor(colors.HexColor("#cccccc")); c.setLineWidth(0.5); c.setDash(3,3)
c.line(cw,0,cw,H); c.line(0,ch,W,ch); c.setDash()
c.showPage(); c.save(); print("PDF:",OUT)
