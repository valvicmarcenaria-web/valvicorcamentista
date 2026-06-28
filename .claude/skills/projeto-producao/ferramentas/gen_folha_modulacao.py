#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
OUT="/home/user/valvicorcamentista/.claude/skills/projeto-producao/ferramentas/folha_modulacao_marceneiro.pdf"
W,H=A4
NAVY=colors.HexColor("#1F3A5F"); GREEN=colors.HexColor("#3f6b4f"); GREY=colors.HexColor("#666")
LINE=colors.HexColor("#bbbbbb"); PANEL=colors.HexColor("#ececec")
c=canvas.Canvas(OUT,pagesize=A4)
M=15*mm; x=M; top=H-M

def fld(label,xx,yy,ll,size=9):  # rótulo + linha de preenchimento
    c.setFont("Helvetica",size); c.setFillColor(colors.black); c.drawString(xx,yy,label)
    lx=xx+c.stringWidth(label,"Helvetica",size)+4
    c.setStrokeColor(LINE); c.line(lx,yy-1,lx+ll,yy-1); return lx+ll
def chk(xx,yy,txt,s=4.6*mm):
    c.setStrokeColor(colors.black); c.setLineWidth(1); c.rect(xx,yy-s+1,s,s)
    c.setFont("Helvetica",9); c.setFillColor(colors.black); c.drawString(xx+s+3,yy-s+2.2,txt)
    return xx+s+3+c.stringWidth(txt,"Helvetica",9)+10

# ===== CABEÇALHO =====
c.setFillColor(NAVY); c.rect(M,top-16*mm,W-2*M,16*mm,fill=1,stroke=0)
c.setFillColor(colors.white); c.setFont("Helvetica-Bold",15); c.drawString(M+6*mm,top-7*mm,"VALVIC MARCENARIA")
c.setFont("Helvetica",10); c.drawString(M+6*mm,top-12.5*mm,"FOLHA DE MODULAÇÃO — preenchimento do marceneiro")
# Nº pedido / Nº módulo
c.setFillColor(colors.black)
y=top-24*mm
fld("Nº DO PEDIDO:",x,y,55*mm,10)
fld("Nº DO MÓDULO:",x+95*mm,y,W-2*M-95*mm-15*mm,10)
y-=9*mm
fld("Ambiente:",x,y,45*mm); fld("Marceneiro:",x+70*mm,y,40*mm); fld("Data:",x+135*mm,y,W-2*M-135*mm)

# ===== DESENHO (armário inferior: laterais + base + testeira) =====
y-=8*mm
c.setFont("Helvetica-Bold",10); c.setFillColor(GREEN); c.drawString(x,y,"DESENHO DO MÓDULO  (acrescente portas / gavetas / porta-tempero à mão)")
c.setFillColor(colors.black)
dw,dh=120*mm,62*mm
dx=(W-dw)/2; dy=y-6*mm-dh
t=11*mm  # espessura visual dos painéis
c.setStrokeColor(colors.black); c.setLineWidth(1.3)
# contorno
c.rect(dx,dy,dw,dh)
# painéis (cinza)
c.setFillColor(PANEL); c.setStrokeColor(colors.HexColor("#888")); c.setLineWidth(0.8)
c.rect(dx,dy,t,dh,fill=1)               # lateral esq
c.rect(dx+dw-t,dy,t,dh,fill=1)          # lateral dir
c.rect(dx,dy,dw,t,fill=1)               # base
c.rect(dx,dy+dh-8*mm,dw,8*mm,fill=1)    # testeira (banda fina no topo)
# rótulos
c.setFillColor(GREY); c.setFont("Helvetica",7.5)
c.saveState(); c.translate(dx+t/2,dy+dh/2); c.rotate(90); c.drawCentredString(0,0,"LATERAL ESQ"); c.restoreState()
c.saveState(); c.translate(dx+dw-t/2,dy+dh/2); c.rotate(90); c.drawCentredString(0,0,"LATERAL DIR"); c.restoreState()
c.drawCentredString(dx+dw/2,dy+t/2-2,"BASE")
c.drawCentredString(dx+dw/2,dy+dh-5.5*mm,"TESTEIRA")
c.setFont("Helvetica-Oblique",8); c.setFillColor(colors.HexColor("#999"))
c.drawCentredString(dx+dw/2,dy+dh/2,"(área livre — desenhe as frentes à mão)")

# ===== TÓPICOS =====
y=dy-10*mm
def topic(label,fill):  # imprime label em negrito e retorna y do conteúdo
    c.setFont("Helvetica-Bold",10); c.setFillColor(colors.black); c.drawString(x,y,label)
def line_adv(d):
    return d
gap=10*mm
c.setFont("Helvetica-Bold",10)
# Altura / Largura / Profundidade
for lab in ["ALTURA:","LARGURA:","PROFUNDIDADE:"]:
    c.setFont("Helvetica-Bold",10); c.setFillColor(colors.black); c.drawString(x,y,lab)
    c.setStrokeColor(LINE); c.line(x+45*mm,y-1,x+110*mm,y-1)
    c.setFont("Helvetica",9); c.setFillColor(GREY); c.drawString(x+112*mm,y,"mm")
    c.setFillColor(colors.black)
    y-=gap
# Tamponamento
c.setFont("Helvetica-Bold",10); c.drawString(x,y,"TAMPONAMENTO:")
c.setFont("Helvetica",9)
c.line(x+38*mm,y-1,x+62*mm,y-1); c.drawString(x+40*mm,y+1.5*mm,"")
c.drawString(x+30*mm,y+3.0*mm,"")
c.setFont("Helvetica",8.5); c.setFillColor(GREY)
c.drawString(x+38*mm,y+2.2*mm,"")
c.setFillColor(colors.black); c.setFont("Helvetica",9)
c.drawString(x+34*mm,y, "Larg ____  ×  Comp ____  ×  Espessura:")
xx=x+118*mm; xx=chk(xx,y,"15"); xx=chk(xx,y,"06"); xx=chk(xx,y,"18  mm")
y-=gap
# Acabamento
c.setFont("Helvetica-Bold",10); c.drawString(x,y,"ACABAMENTO:")
c.setFont("Helvetica",9); c.drawString(x+30*mm,y,"Larg ____  ×  Comp ____  ×  Espessura:")
xx=x+118*mm; xx=chk(xx,y,"15"); xx=chk(xx,y,"06"); xx=chk(xx,y,"18  mm")
y-=gap
# Fundo
c.setFont("Helvetica-Bold",10); c.drawString(x,y,"FUNDO:")
xx=x+30*mm; xx=chk(xx,y,"Sim"); xx=chk(xx,y,"Não")
y-=gap
# Puxador
c.setFont("Helvetica-Bold",10); c.drawString(x,y,"PUXADOR:")
c.setStrokeColor(LINE); c.line(x+30*mm,y-1,W-M,y-1)
y-=gap
# Ferragens
c.setFont("Helvetica-Bold",10); c.drawString(x,y,"FERRAGENS:")
c.setStrokeColor(LINE); c.line(x+30*mm,y-1,W-M,y-1)
y-=gap
# Prateleiras e divisórias
c.setFont("Helvetica-Bold",10); c.drawString(x,y,"PRATELEIRAS E DIVISÓRIAS:")
xx=x+62*mm; xx=chk(xx,y,"15"); xx=chk(xx,y,"18  mm")
y-=gap+2*mm
# Observações
c.setFont("Helvetica-Bold",10); c.drawString(x,y,"OBSERVAÇÕES:")
c.setStrokeColor(LINE)
for k in range(3):
    yy=y-(k+1)*7*mm; c.line(x,yy,W-M,yy)

c.setFont("Helvetica-Oblique",7.5); c.setFillColor(GREY)
c.drawString(M, M-3, "Valvic Marcenaria · Folha de modulação do marceneiro")
c.showPage(); c.save()
print("PDF:",OUT)
