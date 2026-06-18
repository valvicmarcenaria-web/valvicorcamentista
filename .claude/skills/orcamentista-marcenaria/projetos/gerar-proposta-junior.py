# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
import math

W,H = A4
GOLD   = HexColor("#E0A521")
GOLD2  = HexColor("#B8860B")
INK    = HexColor("#1A1A1A")
CREME  = HexColor("#FDF6E3")
GREY   = HexColor("#5b5b5b")
LINE   = HexColor("#E4D9BD")
SERIF="Times-Roman"; SERIFB="Times-Bold"; SERIFI="Times-Italic"
SANS="Helvetica"; SANSB="Helvetica-Bold"
OUT="/home/user/valvicorcamentista/proposta-junior-valvic.pdf"
c = canvas.Canvas(OUT, pagesize=A4)

def star(cx,cy,r,col):
    c.setFillColor(col); p=c.beginPath()
    for i in range(8):
        ang=math.pi/2 + i*math.pi/4
        rad = r if i%2==0 else r*0.32
        x=cx+rad*math.cos(ang); y=cy+rad*math.sin(ang)
        (p.moveTo if i==0 else p.lineTo)(x,y)
    p.close(); c.drawPath(p,fill=1,stroke=0)

def center(txt,y,font,size,col=INK,tracking=0):
    c.setFont(font,size); c.setFillColor(col)
    if tracking:
        tw=sum(stringWidth(ch,font,size)+tracking for ch in txt)-tracking
        x=(W-tw)/2
        for ch in txt:
            c.drawString(x,y,ch); x+=stringWidth(ch,font,size)+tracking
    else:
        c.drawCentredString(W/2,y,txt)

def footer(num):
    c.setFont(SANS,8); c.setFillColor(GREY)
    c.drawString(20*mm,12*mm,"valvic  ·  marcenaria de alto padrão")
    c.drawRightString(W-20*mm,12*mm,f"Lagoa Santa · 2026   —   {num}")
    c.setStrokeColor(LINE); c.setLineWidth(0.5); c.line(20*mm,16*mm,W-20*mm,16*mm)

# ---------- PÁGINA 1 — CAPA ----------
c.setFillColor(INK); c.rect(0,0,W,H,fill=1,stroke=0)
# faixa dourada
c.setFillColor(GOLD); c.rect(0,H-300,W,120,fill=1,stroke=0)
for (sx,sy,sr) in [(60,H-150,14),(W-70,H-120,10),(W-120,H-210,7),(90,H-235,8)]:
    star(sx,sy,sr,GOLD)
center("PROPOSTA ESPECIAL PARA", H-238, SANS, 13, INK, tracking=3)
center("Júnior", H-150, SERIFB, 78, INK)
c.setFillColor(CREME)
center("Residência Bouganville — Lagoa Santa", H-330, SERIFI, 20, CREME)
center("Projeto completo de marcenaria de alto padrão", H-360, SANS, 11, HexColor("#c9c1ad"), tracking=1)
# wordmark
center("valvic", 120, SERIFB, 34, GOLD)
center("MARCENARIA", 100, SANS, 9, HexColor("#c9c1ad"), tracking=6)
center("Proposta emitida em 18/06/2026  ·  válida até 22/06/2026", 60, SANS, 9, GREY)
c.showPage()

# ---------- PÁGINA 2 — CONEXÃO / QUEM SOMOS ----------
c.setFillColor(HexColor("#ffffff")); c.rect(0,0,W,H,fill=1,stroke=0)
c.setFillColor(GOLD); c.rect(0,H-8,W,8,fill=1,stroke=0)
y=H-70*mm
center("Não desenvolvemos apenas móveis,", y, SERIFB, 26, INK); 
center("desenvolvemos a sua casa.", y-34, SERIFB, 26, INK)
y-=70
para=[
 "Júnior, esta proposta nasce de um olhar cuidadoso sobre cada ambiente da sua",
 "residência em Lagoa Santa. Pensamos a marcenaria como a espinha dorsal do",
 "projeto: o que organiza, o que ilumina e o que transforma o espaço em lar.",
 "",
 "Da cozinha que recebe à suíte master que acolhe, cada módulo foi detalhado",
 "com ferragens premium, acabamentos na cor e iluminação integrada — para durar",
 "e encantar por décadas.",
]
c.setFont(SANS,12); c.setFillColor(GREY)
for ln in para:
    c.drawCentredString(W/2,y,ln); y-=20
# 5 diferenciais
y-=24
c.setFillColor(CREME); c.rect(20*mm,y-78,W-40*mm,78,fill=1,stroke=0)
difs=["Ética","Qualidade","Foco no cliente","Inovação","Relacionamento"]
n=len(difs); cellw=(W-40*mm)/n
for i,d in enumerate(difs):
    cx=20*mm+cellw*(i+0.5)
    star(cx,y-26,7,GOLD)
    c.setFont(SANSB,10.5); c.setFillColor(INK); c.drawCentredString(cx,y-52,d)
footer("quem somos")
c.showPage()

# ---------- PÁGINA 3 — CONFIGURAÇÃO TÉCNICA ----------
c.setFillColor(HexColor("#ffffff")); c.rect(0,0,W,H,fill=1,stroke=0)
c.setFillColor(GOLD); c.rect(0,H-8,W,8,fill=1,stroke=0)
center("CONFIGURAÇÃO TÉCNICA DOS MÓVEIS", H-60, SANSB, 14, INK, tracking=2)
center("o que está por trás de cada peça", H-78, SERIFI, 13, GOLD2)
cards=[
 ("Ferragens Hettich","Corrediças ocultas com amortecedor e dobradiças soft-close — fechamento suave e silencioso, alemão."),
 ("Garantia 10 anos","Linha de ferragem Hettich: garantia de 10 anos nos sistemas de movimento."),
 ("Vidro Reflecta Bronze","Cristaleiras e closets com vidro reflecta bronze e perfil champanhe — sofisticação e leveza."),
 ("Iluminação integrada","Fita de LED em perfil de alumínio embutido, com fonte dimensionada — ambientação em nichos e closets."),
 ("MDF de alto padrão","Metallic Suede, Cacao Matt, Areia Matt, Itapuã e Volakas (Berneck/Duratex/Guararapes/Arauco)."),
 ("Espessuras corretas","Estrutura 15mm, portas de correr 18mm e louçaria reforçada 30mm — resistência e estética."),
 ("Portas de passagem","Folhas piso-teto estruturadas (MDF + reforço de metalon), integradas ao painel."),
 ("Laminação premium","Fita de borda na cor em todas as faces aparentes — acabamento contínuo e durável."),
 ("Interno na cor","Opção de mobiliário todo na cor, inclusive o interior — percepção de valor em cada detalhe."),
]
cols=3; mx=20*mm; gw=(W-2*mx)/cols; ch_=66*mm/3*1.0
top=H-110; cardh=58
for i,(t,d) in enumerate(cards):
    r=i//cols; col=i%cols
    x=mx+col*gw; yb=top-20 - r*(cardh+14)
    c.setFillColor(CREME); c.roundRect(x+4,yb-cardh,gw-8,cardh,6,fill=1,stroke=0)
    star(x+16,yb-14,5,GOLD)
    c.setFont(SANSB,9.6); c.setFillColor(INK); c.drawString(x+26,yb-17,t)
    c.setFont(SANS,7.7); c.setFillColor(GREY)
    # wrap desc
    words=d.split(); line=""; ly=yb-30
    for w in words:
        if stringWidth(line+" "+w,SANS,7.7) < gw-22:
            line=(line+" "+w).strip()
        else:
            c.drawString(x+12,ly,line); ly-=10; line=w
    c.drawString(x+12,ly,line)
footer("configuração técnica")
c.showPage()

# ---------- PÁGINA 4 — ESCOPO POR AMBIENTE ----------
c.setFillColor(HexColor("#ffffff")); c.rect(0,0,W,H,fill=1,stroke=0)
c.setFillColor(GOLD); c.rect(0,H-8,W,8,fill=1,stroke=0)
center("O PROJETO, AMBIENTE A AMBIENTE", H-60, SANSB, 14, INK, tracking=2)
center("marcenaria completa da residência", H-78, SERIFI, 13, GOLD2)
ambs=[
 ("Cozinha","Armários superiores e inferiores, ilha, torre de fornos e geladeiras, cristaleira e adega em vidro reflecta bronze."),
 ("Sala de TV","Painel de TV, armários inferiores e painel com porta pivotante; espelho bronze."),
 ("Quarto de serviço","Armários inferiores e painéis ripados; painel de TV."),
 ("Louçaria + Lavabo","Louçarias com prateleiras e montantes reforçados (30mm) e gabinete do lavabo."),
 ("Despensa","Armários com prateleiras e gavetas; frentes em vidro."),
 ("Suíte 1","Closet com portas de correr em vidro reflecta bronze, painéis, cabeceira e espelho bronze."),
 ("Suíte 2","Closet em vidro reflecta bronze, painel ripado chumbo e cabeceira estofada."),
 ("Suíte 3","Closet em vidro reflecta bronze, painéis ripados e cabeceira estofada."),
 ("Suíte Master","Três closets em vidro reflecta bronze, painel ondulado, painel de TV, penteadeira e divisórias."),
]
y=H-110
for nome,desc in ambs:
    c.setFillColor(GOLD); star(24*mm,y-2,5,GOLD)
    c.setFont(SERIFB,13); c.setFillColor(INK); c.drawString(30*mm,y-5,nome)
    c.setFont(SANS,9.5); c.setFillColor(GREY)
    # wrap
    words=desc.split(); line=""; ly=y-5; first=True
    xstart=72*mm
    for w in words:
        if stringWidth(line+" "+w,SANS,9.5) < (W-20*mm-xstart):
            line=(line+" "+w).strip()
        else:
            c.drawString(xstart,ly,line); ly-=12; line=w
    c.drawString(xstart,ly,line)
    y-=  (max(2, (ly< y-5) and 2 or 1))*0  # noop
    y-=  ( (y-5-ly)+ 20 )
    c.setStrokeColor(LINE); c.setLineWidth(0.4); c.line(24*mm,y+6,W-20*mm,y+6)
footer("escopo do projeto")
c.showPage()

# ---------- PÁGINA 5 — INVESTIMENTO ----------
c.setFillColor(HexColor("#ffffff")); c.rect(0,0,W,H,fill=1,stroke=0)
c.setFillColor(GOLD); c.rect(0,H-8,W,8,fill=1,stroke=0)
center("INVESTIMENTO", H-62, SANSB, 16, INK, tracking=3)
center("marcenaria completa · 9 ambientes · instalação inclusa", H-82, SERIFI, 12, GOLD2)

def versao(yt, titulo, sub, preco, destaque):
    x=22*mm; w=W-44*mm; h=58
    if destaque:
        c.setFillColor(GOLD); c.roundRect(x,yt-h,w,h,8,fill=1,stroke=0); tcol=INK; pcol=INK; scol=HexColor("#5a4410")
    else:
        c.setFillColor(CREME); c.roundRect(x,yt-h,w,h,8,fill=1,stroke=0); tcol=INK; pcol=GOLD2; scol=GREY
    c.setFont(SERIFB,18); c.setFillColor(tcol); c.drawString(x+16,yt-26,titulo)
    c.setFont(SANS,9.5); c.setFillColor(scol); c.drawString(x+16,yt-42,sub)
    c.setFont(SANSB,24); c.setFillColor(pcol); c.drawRightString(x+w-16,yt-32,preco)
    return yt-h-16

y=H-120
y=versao(y,"Assinada — Tudo na Cor","Mobiliário completo com interior na cor em todos os móveis.","R$ 395.000",True)
y=versao(y,"Essencial — Interior Branco","Mesma marcenaria; interior dos armários fechados em Branco TX.","R$ 370.000",False)

# bloco condições
y-=6
c.setStrokeColor(LINE); c.setLineWidth(0.6); c.line(22*mm,y,W-22*mm,y); y-=22
def linha(lbl,val):
    global y
    c.setFont(SANSB,10); c.setFillColor(INK); c.drawString(24*mm,y,lbl)
    c.setFont(SANS,10.5); c.setFillColor(GREY); c.drawString(74*mm,y,val); y-=20
linha("Garantia","10 anos (ferragens Hettich) · instalação e regulagens 2 anos")
linha("Pagamento","Entrada de 30% + 4 boletos (60 / 90 / 120 / 150 dias)")
linha("Prazo","45 a 60 dias úteis após aprovação do projeto executivo")
linha("Validade","Proposta válida até 22/06/2026")
linha("Incluso","Projeto, produção, transporte, montagem e instalação")

# selo garantia (centralizado, abaixo das condições)
sx=W/2; sy=y-60
c.setFillColor(INK); c.circle(sx, sy, 46, fill=1, stroke=0)
c.setFillColor(GOLD); c.setFont(SERIFB,26); c.drawCentredString(sx, sy+2, "10")
c.setFont(SANS,7); c.setFillColor(CREME); c.drawCentredString(sx, sy-16, "ANOS DE GARANTIA")

center("Obrigado pela confiança, Júnior. Vamos construir juntos.", 40*mm, SERIFI, 14, INK)
center("valvic · marcenaria", 30*mm, SERIFB, 14, GOLD)
footer("investimento")
c.showPage()
c.save()
print("PDF gerado:",OUT)
