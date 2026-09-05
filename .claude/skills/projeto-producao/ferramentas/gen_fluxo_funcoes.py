#!/usr/bin/env python3
# Fluxo de Producao & Funcoes - Valvic Marcenaria (PDF A4).
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

_B=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(_B,"fluxo_funcoes_valvic.pdf")
LOGO=os.path.join(_B,"logo_clean.png")
W,H=A4
NAVY=colors.HexColor("#1F3A5F"); GREY=colors.HexColor("#666")
c=canvas.Canvas(OUT,pagesize=A4)

# paleta por macro-area
AREA={
 "COMERCIAL":  colors.HexColor("#2C6FB3"),
 "PROJETOS":   colors.HexColor("#1F3A5F"),
 "PCP":        colors.HexColor("#B8860B"),
 "PRODUCAO":   colors.HexColor("#3F7D51"),
 "OBRA":       colors.HexColor("#6B4E8C"),
}
def tint(hexcol,f=0.16):
    r,g,b=hexcol.red,hexcol.green,hexcol.blue
    return colors.Color(r+(1-r)*(1-f)*0+ (1-r)*(1-f), g+(1-g)*(1-f), b+(1-b)*(1-f)) if False else colors.Color(1-(1-r)*f,1-(1-g)*f,1-(1-b)*f)

def header(sub):
    img=ImageReader(LOGO); iw,ih=img.getSize(); lw=34*mm; lh=lw*ih/iw
    c.drawImage(img,15*mm,H-14*mm-lh,width=lw,height=lh,mask='auto')
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold",13); c.drawRightString(W-15*mm,H-15*mm,"FLUXO DE PRODUÇÃO & FUNÇÕES")
    c.setFillColor(GREY); c.setFont("Helvetica",8.5); c.drawRightString(W-15*mm,H-20*mm,sub)
    c.setStrokeColor(colors.HexColor("#cccccc")); c.setLineWidth(0.6); c.line(15*mm,H-24*mm,W-15*mm,H-24*mm)

# ---------- PAGINA 1: FLUXO (ribbon vertical) ----------
header("Da venda à entrega — quem faz o quê, em ordem")
stages=[
 ("COMERCIAL","1. VENDA & BRIEFING","Vendedor","Fecha o contrato e entrega o briefing COMPLETO (medidas, fotos, eletro, prazos, cores)"),
 ("PROJETOS","2. PROJETO & DETALHAMENTO","Projetos (Felipe/Paulo)","Projeto executivo, tira TODAS as dúvidas com o cliente/comercial antes de liberar"),
 ("PROJETOS","3. ENGENHARIA / PROGRAMAÇÃO","Paulo + Engenharia","Modela e programa p/ o maquinário; sobe o PACOTE ao Drive (DXF, plano de corte, lista de compras, etiquetas, fotos, projeto)"),
 ("PCP","4. PCP / PLANEJAMENTO","Coordenador de Produção","Recebe o pacote, agenda na fila de produção e dispara compras/separação"),
 ("PCP","5. COMPRAS","Auxiliar Administrativa","Compra o que não tem em estoque (prazo casado com a data de corte)"),
 ("PCP","6. ALMOXARIFADO / ESTOQUE","Felipe","Recebe, confere NF, lança na planilha e separa o material do pedido"),
 ("PRODUCAO","7. SEPARAÇÃO & SEQUÊNCIA","Deivison (Gerente Prod.)","Define O QUE corta e QUANDO; libera a ordem pro operador"),
 ("PRODUCAO","8. CORTE / USINAGEM","Joelson (Operador)","Corta, fura e usina conforme plano; etiqueta cada peça"),
 ("PRODUCAO","9. COLADEIRA / FILETE","Operador coladeira","Aplica fita de borda e confere acabamento"),
 ("PRODUCAO","10. CONFERÊNCIA (PORTÃO QC)","Deivison","Confere peças x lista ANTES de montar (mata retrabalho)"),
 ("PRODUCAO","11. MONTAGEM (BANCADA)","Deivison distribui / Montadores","Pré-montagem dos módulos, ferragens, gavetas; confere folgas"),
 ("PRODUCAO","12. EXPEDIÇÃO","Produção","Embala, protege, confere romaneio e carrega na ordem de descarga"),
 ("OBRA","13. OBRA / INSTALAÇÃO","Montador + Paulo (D1/meio/fim)","Instala; Paulo alinha no 1º dia, revisa no meio e confere no fim"),
 ("OBRA","14. ENTREGA & PÓS-OBRA","Comercial + Produção","Checklist de entrega com cliente, assistência e feedback pro projeto"),
]
x0=15*mm; x1=W-15*mm; y=H-30*mm
bh=15.6*mm; gap=1.4*mm
for area,titulo,resp,desc in stages:
    col=AREA[area]
    c.setFillColor(tint(col,0.14)); c.setStrokeColor(col); c.setLineWidth(1.1)
    c.roundRect(x0,y-bh,x1-x0,bh,3*mm,fill=1,stroke=1)
    c.setFillColor(col); c.roundRect(x0,y-bh,4*mm,bh,0,fill=1,stroke=0)
    c.setFillColor(col); c.setFont("Helvetica-Bold",9.2); c.drawString(x0+7*mm,y-6.2*mm,titulo)
    c.setFillColor(colors.black); c.setFont("Helvetica-Bold",7.6); c.drawString(x0+7*mm,y-10.4*mm,"Responsável: "+resp)
    c.setFillColor(colors.HexColor("#333333")); c.setFont("Helvetica",7);
    # quebra simples do desc
    words=desc.split(); line=""; ly=y-13.8*mm
    for wd in words:
        if c.stringWidth(line+" "+wd,"Helvetica",7)>(x1-x0-12*mm):
            c.drawString(x0+7*mm,ly,line); line=wd; ly-=3.2*mm
        else: line=(line+" "+wd).strip()
    c.drawString(x0+7*mm,ly,line)
    # seta
    if area!=stages[-1][0] or titulo!=stages[-1][1]:
        cxm=x0+(x1-x0)/2
        c.setStrokeColor(colors.HexColor("#999")); c.setLineWidth(1.2)
        c.line(cxm,y-bh,cxm,y-bh-gap-1.0*mm)
        c.setFillColor(colors.HexColor("#999"))
        p=c.beginPath(); p.moveTo(cxm-1.6*mm,y-bh-gap-0.2*mm); p.lineTo(cxm+1.6*mm,y-bh-gap-0.2*mm); p.lineTo(cxm,y-bh-gap-2.0*mm); p.close(); c.drawPath(p,fill=1,stroke=0)
    y-=bh+gap
c.setFont("Helvetica-Oblique",7); c.setFillColor(GREY)
c.drawString(15*mm,10*mm,"Valvic Marcenaria · Fluxo de produção · azul=Comercial  navy=Projetos/Eng.  âmbar=PCP/Suprimentos  verde=Produção  roxo=Obra")
c.showPage()

# ---------- PAGINA 2: FUNCOES (cards) ----------
header("Funções por pessoa — o que cada um faz")
roles=[
 ("COMERCIAL","Comercial / Vendas",["Vender e fechar contrato","Briefing COMPLETO (medidas, fotos, eletro, prazos, referências)","Alinhar expectativa/prazo com o cliente","Ponte cliente↔projeto nas dúvidas","Acompanhar pós-entrega e satisfação"]),
 ("PROJETOS","Paulo (Eng./Coord. Projetos)",["Coordenar projetos e engenharia","Programação p/ o maquinário","Padrão construtivo e liberação do pacote","Obra: alinhar D1, revisar no meio, conferir no fim","Aprovar mudanças de escopo"]),
 ("PROJETOS","Felipe (Aux. Projetos + Almox.)",["Detalhar projeto/listas sob orientação","Gerar plano de corte e etiquetas","Almoxarifado: receber, conferir NF, lançar estoque","Separar material por pedido","Avisar ruptura de estoque com antecedência"]),
 ("PCP","Coordenador de Produção",["Receber o pacote e planejar a fila (PCP)","Definir prioridades e prazos por pedido","Disparar compras e separação","Controlar capacidade x carteira","Cobrar os portões de conferência"]),
 ("PCP","Auxiliar Administrativa",["Comprar o que falta (cotação/prazo)","Emitir/lançar pedidos e NFs","Casar prazo de compra com a data de corte","Apoiar romaneio e documentos da obra","Controle de contas/recebimento de material"]),
 ("PRODUCAO","Deivison (Gerente de Produção)",["Separar e sequenciar (o quê/quando)","Distribuir os serviços de montagem","PORTÃO QC: conferir peças x lista","Controlar refugo/retrabalho e prazos","Liberar expedição"]),
 ("PRODUCAO","Joelson (Operador CNC/Corte)",["Operar corte/usinagem pelo plano","Etiquetar todas as peças","Zelar pela máquina (limpeza/aspiração)","Registrar sobras aproveitáveis","Reportar anomalia na hora"]),
 ("PRODUCAO","Coladeira / Montadores",["Coladeira: fita e acabamento","Pré-montagem, ferragens, gavetas, folgas","Lixar/limpar e conferir antes de embalar","Embalar e proteger p/ transporte","Seguir a ordem de produção"]),
 ("OBRA","Montador (Obra)",["Proteger o local e conferir romaneio","Nivelar, aprumar e fixar na parede","Portas/gavetas/tampos/arremates e folgas","Recortes em obra e vedações","Entrega limpa + checklist com o cliente"]),
]
cols=2; cw=(W-30*mm-8*mm)/cols; ch=48*mm
cx=15*mm; cy=H-30*mm
i=0
for area,nome,items in roles:
    col=AREA[area]
    px=15*mm+(i%cols)*(cw+8*mm)
    if i%cols==0 and i>0: cy-=ch+5*mm
    py=cy
    c.setFillColor(tint(col,0.10)); c.setStrokeColor(col); c.setLineWidth(1.0)
    c.roundRect(px,py-ch,cw,ch,3*mm,fill=1,stroke=1)
    c.setFillColor(col); c.roundRect(px,py-9*mm,cw,9*mm,3*mm,fill=1,stroke=0)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold",9.3); c.drawString(px+4*mm,py-6*mm,nome)
    c.setFillColor(colors.HexColor("#222")); c.setFont("Helvetica",7.4)
    ty=py-13.5*mm
    for it in items:
        c.setFillColor(col); c.circle(px+5*mm,ty+0.9*mm,0.7*mm,fill=1,stroke=0)
        c.setFillColor(colors.HexColor("#222"))
        # quebra
        words=it.split(); line=""; lx=px+7.5*mm
        first=True
        for wd in words:
            if c.stringWidth(line+" "+wd,"Helvetica",7.4)>(cw-11*mm):
                c.drawString(lx,ty,line); line=wd; ty-=3.4*mm
            else: line=(line+" "+wd).strip()
        c.drawString(lx,ty,line); ty-=4.8*mm
    i+=1
c.showPage()

# ---------- PAGINA 3: MELHORIAS ----------
header("Sugestões p/ acabar com a confusão de funções")
def block(title,y,items,col):
    c.setFillColor(col); c.setFont("Helvetica-Bold",10.5); c.drawString(15*mm,y,title)
    c.setFillColor(colors.HexColor("#222")); c.setFont("Helvetica",8.6)
    yy=y-6*mm
    for it in items:
        c.setFillColor(col); c.circle(17*mm,yy+1.0*mm,0.8*mm,fill=1,stroke=0); c.setFillColor(colors.HexColor("#222"))
        words=it.split(); line="";
        for wd in words:
            if c.stringWidth(line+" "+wd,"Helvetica",8.6)>(W-30*mm-8*mm):
                c.drawString(20*mm,yy,line); line=wd; yy-=4.6*mm
            else: line=(line+" "+wd).strip()
        c.drawString(20*mm,yy,line); yy-=6.2*mm
    return yy-2*mm
y=H-30*mm
y=block("1) Portões de conferência (QC) — onde o erro morre",y,[
 "Projeto→Produção: só entra na fila com o PACOTE completo no Drive (checklist de liberação).",
 "Antes de cortar: conferir plano de corte x lista de compras x estoque.",
 "Depois de cortado/filetado: conferir peças x lista (o Deivison assina).",
 "Antes da expedição: romaneio conferido (nada sai incompleto).",
 "Na obra: checklist de entrega assinado pelo cliente."],AREA["PRODUCAO"])
y=block("2) Um DONO por etapa (RACI simples)",y,[
 "Cada etapa tem 1 responsável que responde por ela (evita 'achei que era do outro').",
 "Comercial dono do briefing; Projetos dono do pacote; PCP dono da fila; Deivison dono do chão; Paulo dono da obra.",
 "Mudou o escopo? Só o Paulo aprova e volta pro projeto atualizar o pacote."],AREA["PROJETOS"])
y=block("3) Rotina e quadro de produção (PCP visível)",y,[
 "Quadro/planilha com a fila: pedido, etapa atual, responsável, prazo (todos enxergam).",
 "Reunião rápida diária (10 min) de produção: o que corta hoje, o que monta, o que vai pra obra.",
 "Estoque mínimo dos itens de giro (fita, cola, parafuso, corrediça) com ponto de recompra."],AREA["PCP"])
y=block("4) Indicadores simples (começar por 3)",y,[
 "% de pedidos entregues no prazo · Nº de retrabalhos/mês · Refugo de chapa (%).",
 "Assistência pós-obra: quantas voltas e por quê (vira regra pra não repetir)."],AREA["COMERCIAL"])
y=block("5) Você (Paulo): saia do operacional aos poucos",y,[
 "Hoje você faz projeto + engenharia + obra. Forme o 'mais um' e o Deivison p/ delegar o repetitivo.",
 "Seu foco de maior valor: engenharia/padrão construtivo, alinhamento de obra (D1/meio/fim) e decisões.",
 "Transforme o que está na sua cabeça em padrão escrito (as folhas de modulação já ajudam nisso)."],AREA["OBRA"])
c.setFont("Helvetica-Oblique",7); c.setFillColor(GREY)
c.drawString(15*mm,10*mm,"Valvic Marcenaria · Referência de organização (v1 — a lapidar com o time)")
c.showPage()
c.save(); print("PDF:",OUT)
