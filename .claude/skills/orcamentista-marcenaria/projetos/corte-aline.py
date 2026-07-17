# -*- coding: utf-8 -*-
# LEVANTAMENTO PECA-A-PECA — ALINE SANCHES / Apto completo (Galeria 42 / Natally Duarte).
# Acabamento: MDF Nude-Berneck (ext, cor) + Branco TX (int) + Cumaru-Arauco (detalhes/ripados/nichos).
# CALCULAR, nunca ESTIMAR: cotas do vetor do caderno (17 pranchas). Alturas: piso->rebaixo 248, laje 260.
# Duas versoes (padrao Kenia): INT='Branco' (branco interno) e INT='Nude' (tudo na cor).
import math, sys
CHAPA=2.75*1.85  # 5.0875 m2
APRO={15:0.82,18:0.82,6:0.55}
PRC={('cor',15):500,('cor',18):600,('cor',6):300,('branco',15):260,('branco',6):190}
COR={'Nude':'cor','Cumaru':'cor','Branco':'branco'}
INT = sys.argv[1] if len(sys.argv)>1 and sys.argv[1] in ('Branco','Nude') else 'Branco'  # interior da caixaria

tal={}; amb_area={}; CUR=[None]; log=[]
def amb(n): CUR[0]=n; amb_area.setdefault(n,{})
def add(mat,esp,w,h,n=1,lab=''):
    if mat=='INT': mat=INT           # caixaria interna: Branco (base) ou Nude (tudo na cor)
    a=(w/100.0)*(h/100.0)*n
    tal[(mat,esp)]=tal.get((mat,esp),0)+a
    d=amb_area[CUR[0]]; d[(mat,esp)]=d.get((mat,esp),0)+a
    log.append((CUR[0],lab,mat,esp,round(a,3)))
def gaveta(lab,lg,ag,prof,frente='Nude'):
    add(frente,18,lg,ag,1,lab+' fr'); add('INT',15,prof,ag,2,lab+' lat')
    add('INT',15,lg,ag,1,lab+' cf'); add('INT',6,lg,prof,1,lab+' fd')
def porta(lab,lg,ag,mat='Nude'): add(mat,18,lg,ag,1,lab)   # porta de abrir/correr
def caixa(lab,L,A,P,divs=0,prat=0,pratL=None,tampo='Nude',fundo6=True):
    # corpo generico: tampo+base (cor/int), 2 lat ext (cor), divs (int), prat (int), fundo 6
    add(tampo,15,L,P,1,lab+' tampo'); add('INT',15,L,P,1,lab+' base')
    add('Nude',15,P,A,2,lab+' lat.ext')
    if divs>0: add('INT',15,P,A,divs,lab+' divs')
    if prat>0: add('INT',15,pratL or L,P,prat,lab+' prat')
    add('INT' if fundo6 else 'Nude',6,L,A,1,lab+' fundo')

# ===================================================== COZINHA / GOURMET
amb('Cozinha/Gourmet')
# Aereos A: 316 corr x58 x50 (Nude) : 2p40 + 4p59 ; + medio 62 Cumaru x45 (nicho micro/escorredor)
caixa('Coz aereo esq',80,58,50,divs=1,prat=2,tampo='Nude'); [porta('Coz aereo p40',40,58) for _ in range(2)]
caixa('Coz aereo centro',236,58,50,divs=3,prat=4); [porta('Coz aereo p59',59,58) for _ in range(4)]
caixa('Coz aereo medio Cumaru',62,58,45,divs=1,prat=1,tampo='Cumaru'); porta('Coz medio porta',62,58,'Cumaru')
# Baixos A: base ~167 x92 ; modulos 37,75x2 (cooktop) + 20 temperos + 67,5 (forno+gavetao) + 59 baixo
caixa('Coz baixo cooktop',75.5,92,60,divs=1); [porta('Coz baixo p37',37.75,72) for _ in range(2)]
caixa('Coz temperos',20,92,60); porta('Coz temperos porta',20,72)
caixa('Coz forno/vassoura',67.5,92,60,divs=1); gaveta('Coz gavetao vassoura',67.5,25,60)  # gavetao + nicho forno (forno=eletro)
caixa('Coz baixo dir',59,92,60,divs=0,prat=1); porta('Coz baixo dir porta',59,72)
# Basculas/nicho microondas (faixa media) — nicho micro (eletro), 1 bascula
porta('Coz bascula',59,40)
# ---- Elev B: Torre despensa 179x248 + estreito 114 + cristaleira 50x145 + portico 50
caixa('Torre despensa',179,248,50,divs=3,prat=4,fundo6=True)   # corpo
[porta('Torre sup p44',44,115) for _ in range(4)]              # 4 portas sup
add('Cumaru',15,179,36,1,'Torre nicho cumaru fundo'); add('Cumaru',15,179,15,1,'Torre nicho testeira')  # nicho cumaru
[porta('Torre inf p44',44,77) for _ in range(3)]               # 3 portas inf
gaveta('Torre fruteira1',20.5,38,45,'Nude'); gaveta('Torre fruteira2',20.5,38,45,'Nude')  # 2 fruteiras (frente vidro=terceiro)
caixa('Estreito bancada',114,88,50,divs=2); [gaveta('Estreito gav',36.25,29,50) for _ in range(3)]
# Cristaleira 50x145 Cumaru, prof 15, 5 prat vidro (vidro=terceiro), corpo cumaru
add('Cumaru',15,50,15,1,'Crist tampo'); add('Cumaru',15,50,15,1,'Crist base')
add('Cumaru',15,15,145,2,'Crist lat'); add('Cumaru',6,50,145,1,'Crist fundo')  # portas+prat = vidro (terceiro)
# Portico 50 Cumaru (moldura em L, ~248 alt, 2 montantes + travessa)
add('Cumaru',18,50,30,1,'Portico trav'); add('Cumaru',18,15,248,2,'Portico montantes')

# ===================================================== AREA SOCIAL / SALA
amb('Area Social')
# Painel TV 181 x248 Nude + ripado Cumaru (ripas 3+3)
add('Nude',18,181,248,1,'Painel TV base')
add('Cumaru',18,181*0.5,248,1,'Painel TV ripado (50% cobertura)')   # ripas 3/3 -> ~50% area em Cumaru 18
# Prateleira 180 prof25 Cumaru
add('Cumaru',18,180,25,1,'Prat social tampo'); add('Cumaru',18,180,8,1,'Prat social testeira')
# Hack suspenso 63,5 (2 gav) prof40 Cumaru ext/branco int
caixa('Hack',63.5,40,40,divs=1,tampo='Cumaru'); gaveta('Hack gav1',63.5,18.75,40,'Nude'); gaveta('Hack gav2',63.5,18.75,40,'Nude')
# Ripado sob bancada L 114x95 Cumaru
add('Cumaru',18,114*0.5,95,1,'Ripado bancada L (50%)')
# (2o portico e cristaleira ja contados na cozinha/ref B)

# ===================================================== QUARTO 02 (escritorio + roupeiro)
amb('Quarto 02')
# Escritorio D: coluna 5 nichos Cumaru (lat roupeiro) 50x248
add('Cumaru',15,50,248,2,'Q2 coluna nichos lat'); add('Cumaru',15,50,38.5,6,'Q2 coluna prat nichos'); add('Cumaru',6,50,248,1,'Q2 coluna fundo')
# aereo Cumaru 127x48,5 prof38,5 (2 portas nude 63,5)
caixa('Q2 aereo',127,48.5,38.5,divs=1,tampo='Cumaru'); [porta('Q2 aereo porta',63.5,48.5) for _ in range(2)]
# nicho cumaru + prateleira + painel cumaru (fundo)
add('Cumaru',15,197,38.5,1,'Q2 nicho fundo'); add('Cumaru',18,197,25,1,'Q2 prateleira')
add('Cumaru',18,197,120,1,'Q2 painel cumaru fundo')
# mesa trabalho 130 prof60 Nude (2 gav) + tampo
add('Nude',18,130,60,1,'Q2 mesa tampo'); add('Nude',18,60,72,2,'Q2 mesa pes'); gaveta('Q2 mesa gav1',30,12,60); gaveta('Q2 mesa gav2',30,12,60)
# penteadeira 70 prof60 Cumaru (1 gav, tampo vidro=terceiro)
add('Cumaru',18,70,60,1,'Q2 pent base'); add('Cumaru',18,60,72,2,'Q2 pent pes'); gaveta('Q2 pent gav',70,15,60,'Cumaru')
# Roupeiro correr E: 156 x248 x60 ; 2 portas correr 67x234 ; interno completo
caixa('Roup Q2',156,248,60,divs=2,prat=3)
add('Nude',18,67,234,2,'Roup Q2 portas correr')     # 2 portas correr
add('INT',15,66,30,3,'Roup Q2 gavetas int'); [gaveta('Roup Q2 gav',66,18,55) for _ in range(3)]
add('INT',15,66,25,2,'Roup Q2 sapateiras')
# Cabeceira em L Q2 (peitoril 117) Nude — assumido 200x40 (FLAG sem cota)
add('Nude',18,200,40,1,'Q2 cabeceira L (flag)')

# ===================================================== BANHEIRO
amb('Banheiro')
# Espelheira/aereo 123,5 x126 Cumaru ext/branco int ; 1 porta correr espelho (terceiro) + 4 nichos
caixa('Banho espelheira',123.5,126,15,divs=3,prat=4,tampo='Cumaru')  # porta espelho = terceiro
# gabinete baixo 47 Cumaru (bascula + gaveta + porta papel)
caixa('Banho gabinete',47,60,45,divs=1,tampo='Cumaru'); porta('Banho gab porta',47,40,'Cumaru'); gaveta('Banho gab gav',47,15,40,'Cumaru')

# ===================================================== QUARTO CASAL / SUITE
amb('Quarto Casal')
# Painel TV G 165x248 Nude + prateleira Cumaru prof25
add('Nude',18,165,248,1,'Casal painel TV'); add('Cumaru',18,165,25,1,'Casal prateleira')
# Roupeiro casal H: 200 (2 portas correr 93) + modulo lateral 100 ; x248 x60 ; interno completo
caixa('Roup casal',200,248,60,divs=3,prat=4)
add('Nude',18,93,234,2,'Roup casal portas correr')   # 2 portas correr (1 c/ espelho=terceiro no lugar do MDF)
caixa('Roup casal lateral',100,248,60,divs=2,prat=4)
add('INT',15,45,30,4,'Roup casal gav int'); [gaveta('Roup casal gav',45,20,55) for _ in range(4)]
add('INT',15,45,25,4,'Roup casal sapateiras')
# Painel ripado cabeceira I: 254 x148 Cumaru (ripas 3/3) + fundo
add('Cumaru',18,254*0.5,148,1,'Casal painel ripado (50%)'); add('Nude',15,254,148,1,'Casal painel ripado base')
# Mesa lateral (criado) 40x50 prof35 Nude (pes metalon=terceiro), 2 gav
caixa('Casal criado',40,50,35,tampo='Nude'); gaveta('Casal criado gav1',36,19,35); gaveta('Casal criado gav2',36,19,35)

# ===================================================== FECHAMENTO
def run():
    print(f"===== VERSAO: interior = {INT} =====")
    tot_ch=0; tot_cost=0; cpm={}
    for (mat,esp),area in sorted(tal.items(),key=lambda x:-x[1]):
        cor=COR[mat]; ch=max(1,math.ceil(area/(CHAPA*APRO[esp]))); preco=PRC[(cor,esp)]; cost=ch*preco
        tot_ch+=ch; tot_cost+=cost; cpm[(mat,esp)]=cost/area if area else 0
        print(f"{mat:7s}{esp:>3}mm {area:6.2f}m2 -> {ch:>2}ch x{preco} = {cost}")
    print(f"CHAPAS: {tot_ch} = R$ {tot_cost}")
    # ferragens (contagem aprox)
    corr_pares=3+2+3+3+3+4+2+2   # gavetas telescopicas (cozinha, hack, escritorio, roupeiros, criado...)
    correr_m2=4                   # sistemas de correr (2 roupeiros + espelheira) — kits
    dobradicas=40                 # portas de abrir
    cabideiros=5; sapateiras=6
    FERR=corr_pares*40 + correr_m2*350 + dobradicas*8 + cabideiros*60 + sapateiras*70
    LED=1200   # varias cavas 3000K (torre, nichos, prateleiras, portico, cabeceira) perfil+fita+fonte
    fita=tot_ch*80; insumos=tot_ch*60; usinagem=2500  # ripados, cavas, frisos
    vidros_esp=1700   # vidros/espelhos DOS MOVEIS (cristaleira 8mm, fruteiras, penteadeira, espelho prata roupeiros/banheiro) — escopo Valvic
    visitas=4*250; logistica=6*150
    material=tot_cost+FERR+LED+fita+insumos+usinagem+vidros_esp+visitas+logistica
    print(f"ferragens {FERR} · LED {LED} · fita {fita} · insumos {insumos} · usinagem {usinagem} · visitas {visitas} · log {logistica}")
    print(f"CUSTO MATERIAL = R$ {material:.0f}")
    # motor com cartao, RT? (flag). MC 40%.
    a=0.18; liqF=0.88
    for rt in (0.0,0.10):
        b=(0.8+1+2.5+rt*100)/100
        for mc in (0.40,0.42):
            inv=material/(1-a-liqF*b-mc)
            print(f"  MC {int(mc*100)}% RT {int(rt*100)}% -> R$ {inv:,.0f}".replace(',','.'))
    return material
run()
