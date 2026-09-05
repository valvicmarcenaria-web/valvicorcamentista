# -*- coding: utf-8 -*-
# LEVANTAMENTO PECA-A-PECA — Resolve Consorcio. Conta aberta (cotas do caderno, em cm).
# Regra: cada peca L x A -> area; soma por (material, espessura); chapas = area / (5,0875 * aprov).
# Construcao Valvic: face/portas/gavetoes = material da cor 18mm; tampo/prateleira visivel/jardineira/banco = cor 15mm;
# caixaria interna (laterais internas, base, divisorias, prat. internas, lat/contrafrente de gaveta) = Branco TX 15mm;
# fundos e fundos de gaveta = 6mm. Laterais EXTERNAS visiveis e o tampo = material da cor (Grafito).
CHAPA=2.75*1.85  # 5.0875 m2
APROV={15:0.82,18:0.82,6:0.55}
PRC={('cor',15):500,('cor',18):600,('cor',6):300,('branco',15):260,('branco',6):190}
COR={'Grafito':'cor','Freijo':'cor','Carvalho':'cor','AzulA':'cor','AzulS':'cor','AzulP':'cor','Similar':'cor','Branco':'branco'}
tal={}; log=[]; CUR=[None]; amb_area={}   # amb_area[amb][(mat,esp)] = m2
def amb(name): CUR[0]=name; amb_area.setdefault(name,{})
def add(mat,esp,w,h,n=1,lab=''):
    a=(w/100.0)*(h/100.0)*n
    tal[(mat,esp)]=tal.get((mat,esp),0)+a
    d=amb_area[CUR[0]]; d[(mat,esp)]=d.get((mat,esp),0)+a
    log.append((CUR[0],lab,mat,esp,w,h,n,round(a,3)))

# ================= caixa generica de armario/credenza =================
def cx(lab,mat,L,A,P,ndiv,nprat,portas,gavs,tampo_cor=True,fundo_cor=False):
    # portas: lista de (larg, alt). gavs: lista de alturas (larg = vao); nprat: (larg_vao, qtd)
    fund='branco' if not fundo_cor else 'cor'; fmat='Branco' if not fundo_cor else mat
    # tampo (visivel) + base
    add(mat if tampo_cor else 'Branco',15,L,P,1,lab+' tampo')
    add('Branco',15,L,P,1,lab+' base')
    # 2 laterais externas (visiveis = cor) + divisorias internas (branco)
    add(mat,15,P,A,2,lab+' lat.ext')
    if ndiv>0: add('Branco',15,P,A,ndiv,lab+' divisorias')
    # prateleiras internas (branco 15)
    for (lv,q) in nprat:
        if q>0: add('Branco',15,lv,P,q,lab+' prat.int')
    # fundo (6mm)
    add(fmat,6,L,A,1,lab+' fundo')
    # portas (cor 18)
    for (lp,ap) in portas: add(mat,18,lp,ap,1,lab+' porta')
    # gavetoes: frente cor18 + 2 laterais branco15 + contrafrente branco15 + fundo branco6
    for (lg,ag) in gavs:
        add(mat,18,lg,ag,1,lab+' gav.frente')
        add('Branco',15,P,ag,2,lab+' gav.lat')
        add('Branco',15,lg,ag,1,lab+' gav.contraf')
        add('Branco',6,lg,P,1,lab+' gav.fundo')

# ============================================================ RECEPCAO (rc_02..04)
amb("Recepção")
# Jardineira Grafito 257 x 40(alt) x 30(prof): frente+costas+base+2 lat  (caixa aberta em cima)
add('Grafito',15,257,40,1,'Recep jard frente'); add('Grafito',15,257,40,1,'Recep jard costas')
add('Grafito',15,257,30,1,'Recep jard base'); add('Grafito',15,30,40,2,'Recep jard lat')
# Fechamento superior em L (Grafito), faixa 40 alt, ~257+100 corrido
add('Grafito',15,357,40,1,'Recep fechamento sup L')
# (Ripado = produto Eucatex, fora das chapas)

# ============================================================ SALA REUNIAO (rc_05..08)
amb("Sala de Reunião")
# 4 prateleiras Grafito 233 x 30prof, esp 5: painel 15mm + fascia frontal 5cm (canal do LED)
for i in range(4):
    add('Grafito',15,233,30,1,'SReuniao prat painel'); add('Grafito',15,233,5,1,'SReuniao prat fascia')
# Armario 233 x 80 x 50: 5 portas (~46) + nicho; caixaria
cx('SReuniao arm','Grafito',233,80,50,ndiv=4,nprat=[(46,3)],
   portas=[(46,80)]*5, gavs=[])

# ============================================================ CONVIVENCIA (rc_09..12)
amb("Convivência")
# Jardineira Grafito em L: 330 + 82 + 82 = 494 corrido x 60alt x 40prof
add('Grafito',15,494,60,1,'Conviv jard frente'); add('Grafito',15,494,60,1,'Conviv jard costas')
add('Grafito',15,494,40,1,'Conviv jard base'); add('Grafito',15,40,60,3,'Conviv jard lat/ret')
# Painel liso Freijo 150 x 210 (chapa)
add('Freijo',15,150,210,1,'Conviv painel liso')
# (2 paredes ripado = produto)

# ============================================================ COFFE POINT (rc_13..14)
amb("Coffe Point")
# Painel + teto Freijo (chapa): painel 449 x 260 ; teto 460 x 185
add('Freijo',15,449,260,1,'Coffe painel'); add('Freijo',15,460,185,1,'Coffe teto')
# Armario Grafito 304 x 95 x 50: 5 portas de 50 + nicho frigobar (51) ; fechamento sup Freijo
cx('Coffe arm','Grafito',304,95,50,ndiv=5,nprat=[(50,2)],portas=[(50,87)]*5,gavs=[])
add('Freijo',15,304,10,1,'Coffe fechamento sup')

# ============================================================ DESCOMPRESSAO (rc_15..17)
amb("Descompressão")
# 2 bancos Grafito (148 e 145) x 45alt x 50prof: assento+frente+2lat+base
for L in (148,145):
    add('Grafito',15,L,50,1,'Descomp banco assento'); add('Grafito',15,L,45,1,'Descomp banco frente')
    add('Grafito',15,50,45,2,'Descomp banco lat'); add('Grafito',15,L,50,1,'Descomp banco base')
# Jardineira central 100 x 60 x 50 (Grafito, ver flag material)
add('Grafito',15,100,60,2,'Descomp jard f/c'); add('Grafito',15,100,50,1,'Descomp jard base'); add('Grafito',15,50,60,2,'Descomp jard lat')

# ============================================================ REFEITORIO (rc_18..19)
amb("Refeitório")
# Basculas Carvalho Americano 184 x 80 x 50: 2 portas basculantes de 92 ; caixaria interna branco
cx('Refeit bascula','Carvalho',184,80,50,ndiv=1,nprat=[(90,2)],portas=[(92,80),(92,80)],gavs=[])
# Armario inferior "Similar" A72 x ~180 x 50 (sob bancada) com nichos
cx('Refeit arm inf','Similar',180,72,50,ndiv=2,nprat=[(56,2)],portas=[(56,72),(56,72)],gavs=[])

# ============================================================ JURIDICO (rc_20..24)
amb("Jurídico")
# 4 prateleiras Grafito (347,232,232,347) x 30prof esp5: painel + fascia (as de 347 levam reforco -> +1 painel)
for L in (347,232,232,347):
    add('Grafito',15,L,30,1,'Jurid prat painel'); add('Grafito',15,L,5,1,'Jurid prat fascia')
    if L>300: add('Grafito',15,L,28,1,'Jurid prat reforco (vao 347)')  # torcao anti-flecha no vao longo
# Credenza A 418 x 80 x 50: 7 gavetoes (~86 larg, ~38 alt) + nicho 85x34 + coluna 71 c/ 2 nichos 67x35
cx('Jurid credA','Grafito',418,80,50,ndiv=4,nprat=[(67,2)],portas=[],
   gavs=[(86,38)]*7)
# Credenza B 350 x 80 x 50: 8 gavetoes (88 larg, 38 alt)
cx('Jurid credB','Grafito',350,80,50,ndiv=3,nprat=[],portas=[],gavs=[(88,38)]*8)

# ============================================================ COMPLIANCE (rc_25..26)
amb("Compliance")
# Jardineira Freijo em L: 109 + 103 = 212 x 60 x 40
add('Freijo',15,212,60,2,'Compl jard f/c'); add('Freijo',15,212,40,1,'Compl jard base'); add('Freijo',15,40,60,2,'Compl jard lat')
# (ripado = produto)

# ============================================================ CIRCULACAO — 63 LOCKERS (rc_27..31)
amb("Circulação (lockers)")
# Parte01: 10 col x3 (500x153x40) -> 11 verticais ; Parte02: 11 col x3 (550x153x40) -> 12 verticais
for nver in (11,12):
    add('Branco',15,40,153,nver,'Locker verticais')
# horizontais: cada coluna tem 4 (topo,2 div,base) 50x40 ; 21 colunas
add('Branco',15,50,40,21*4,'Locker horizontais')
# costas 6mm: 63 x 50x50
add('Branco',6,50,50,63,'Locker costas')
# portas 63 (50x50) por cor: AzulA 27, AzulS 18, AzulP 18
add('AzulA',18,50,50,27,'Locker portas Austral')
add('AzulS',18,50,50,18,'Locker portas Secreto')
add('AzulP',18,50,50,18,'Locker portas Petroleo')

# ============================================================ COMERCIAL (rc_32..34)
amb("Comercial")
# Jardineira de canto Freijo em L: 115 + 106 = 221 x 60 x 40
add('Freijo',15,221,60,2,'Comerc jard f/c'); add('Freijo',15,221,40,1,'Comerc jard base'); add('Freijo',15,40,60,2,'Comerc jard lat')
# Jardineira central Grafito 783 x 60 x 28 (espinha)
add('Grafito',15,783,60,2,'Comerc jard central f/c'); add('Grafito',15,783,28,1,'Comerc jard central base'); add('Grafito',15,28,60,2,'Comerc jard central lat')
# (2 paredes ripado = produto)

# ============================================================ SALA REUNIAO COLAB (rc_35..37)
amb("Sala Reunião Colab")
# Armario Grafito 410 x 80 x 50: gaveta+frigobar(1 mod) + ~4 portas de 51 + coluna 101 c/ 2 nichos 97x35
cx('Colab arm','Grafito',410,80,50,ndiv=5,nprat=[(97,2)],portas=[(51,80)]*4,gavs=[(51,38)])
# (ripado 315x260 = produto)

# ============================================================ SALA CEO (rc_38..39)
amb("Sala CEO")
# Credenza Grafito 200 x 80 x 50: 3 col x49 = 6 gavetoes (38 alt) + col 50 (1 gaveta 25 + nicho frigobar)
cx('CEO cred','Grafito',200,80,50,ndiv=3,nprat=[(50,1)],portas=[],gavs=[(49,38)]*6+[(49,25)])

# ============================================================ CALL (rc_40..43)
amb("CALL")
# Armario frigobar 110 x 95 x 50: corpo/sup/lat Grafito, porta 40 AzulP, nicho frigobar 65
cx('CALL frigobar','Grafito',110,95,50,ndiv=1,nprat=[(40,2)],portas=[],gavs=[])
add('AzulP',18,40,95,1,'CALL frigobar porta')
# Guarda-roupa 270 x 270 x 40: corpo Grafito, 6 portas de 45 AzulP, 6 col x 5 prat = 30 prat
add('Grafito',15,270,40,1,'CALL gr tampo'); add('Grafito',15,270,40,1,'CALL gr base')
add('Grafito',15,40,270,2,'CALL gr lat.ext'); add('Branco',15,40,270,5,'CALL gr divisorias')
add('Branco',15,42,40,30,'CALL gr prateleiras'); add('Branco',6,270,270,1,'CALL gr fundo')
add('AzulP',18,45,135,6,'CALL gr portas')  # 6 portas 45 larg x 135 (meia altura, 2 fileiras) -> aprox 270/2

# ============================================================ CABINES CALL x7 (rc_44..54)
amb("Cabines CALL")
# So marcenaria: banco suspenso (assento 40prof + encosto ~70) + tampo de mesa (~55x40). Pe = tubo metalico (fora). Caixa acustica = especialidade (fora).
larg_banco=[81,77,77,77,77,116,116]  # aprox por cabine (assento acompanha a cabine)
for lb in larg_banco:
    # banco SUSPENSO: assento + fascia frontal + 2 mãos-francesas MDF (sem encosto MDF -> parede acustica; sem base)
    add('Grafito',15,lb,40,1,'Cabine banco assento'); add('Grafito',15,lb,12,1,'Cabine banco fascia')
    add('Grafito',15,40,20,2,'Cabine banco suporte'); add('Grafito',15,55,40,1,'Cabine mesa tampo')  # tampo (pe=metal, fora)

# ==================== FECHAMENTO ====================
import math
def money(v): return ("R$ %0.0f"%v).replace(',','.') if v<1000 else ("R$ %0.0f"%v)[:-3].replace(',','.')+'.'+("%03d"%(int(v)%1000))
print("PECAS lancadas:",len(log))
print("\n=== CHAPAS (compra global) ===")
tot_cost=0; tot_ch=0; cpm={}
for (mat,esp),area in sorted(tal.items(), key=lambda x:(-x[1])):
    cor=COR[mat]; ch=max(1, math.ceil(area/(CHAPA*APROV[esp]))); preco=PRC[(cor,esp)]; cost=ch*preco
    tot_cost+=cost; tot_ch+=ch; cpm[(mat,esp)]=cost/area if area else 0  # custo por m2 (p/ alocacao)
    print(f"{mat:9s} {esp:>2}mm  {area:6.2f} m2 -> {ch:>2} ch x R${preco} = R${cost}")
print(f"TOTAL: {tot_ch} chapas = R$ {tot_cost:.0f}")

# ---- ripado Eucatex por ambiente (m2 -> caixas 0.75 -> R$166.5 + perfil L) ----
RIP={'Recepção':8.4,'Convivência':7.43,'Compliance':5.0,'Comercial':5.0,'Sala Reunião Colab':7.88}
rip_cost={a:(math.ceil(m2/0.75)*166.5 + math.ceil(m2/0.75)*13) for a,m2 in RIP.items()}  # +R$13/cx perfil L
print("\n=== RIPADO Eucatex (por ambiente) ===")
for a,c in rip_cost.items(): print(f"{a:22s} {RIP[a]:.1f} m2 -> {math.ceil(RIP[a]/0.75)} cx = R${c:.0f}")
rip_total=sum(rip_cost.values()); print(f"RIPADO TOTAL = R$ {rip_total:.0f}")

# ---- material DIRETO por ambiente (chapa alocada por area x custo/m2 + ripado) ----
matdir={}
for a,d in amb_area.items():
    c=sum(area*cpm[k] for k,area in d.items()) + rip_cost.get(a,0)
    matdir[a]=c
mat_chapas_alloc=sum(sum(area*cpm[k] for k,area in d.items()) for d in amb_area.values())

# ---- custos comuns (nao-chapa) ----
FITA=6000; USINAGEM=2000; LED=3000; INSUMOS=4500; PISTOES=120
FERR={'Hardt':176*8+23*70, 'Hettich':176*35+23*120}
TERC=2100+7*150+500   # estofado 7 bancos + pes metal 7 + escorredor cromado
VISITAS=500
common_fixo=FITA+USINAGEM+LED+INSUMOS+PISTOES+TERC+VISITAS
print(f"\n=== CUSTO DE MATERIAL (Valvic) ===")
for linha,ferr in FERR.items():
    material = tot_cost + rip_total + common_fixo + ferr
    print(f"{linha:8s}: chapas {tot_cost} + ripado {rip_total:.0f} + comum {common_fixo} + ferragem {ferr} = R$ {material:.0f}")

# ---- MOTOR (sem cartao: parc=0; nf=4, vend=3, erro=2, serra .5, manut .5 -> a=0.10; liqF=0.96; RT10 -> b=0.143) ----
a_enc=0.10; liqF=0.96; b=(0.8+1+2.5+10)/100
def preco(fixedR,mc): return fixedR/(1 - a_enc - liqF*b - mc)
LINHAS={'Essencial (Hardt/5a)':('Hardt',0.35), 'Essencial Prime (Hettich/10a)':('Hettich',0.38)}
print("\n=== PRECO FINAL (motor: sem cartao, RT10%) ===")
precos={}
for nome,(ferrk,mc) in LINHAS.items():
    fixedR = tot_cost + rip_total + common_fixo + FERR[ferrk] + 0  # material+terc ja em common
    inv=preco(fixedR,mc); precos[nome]=inv
    print(f"{nome:32s} fixedR={fixedR:.0f}  MC {int(mc*100)}%  ->  INVEST = R$ {inv:,.0f}".replace(',','.'))

# ---- ALOCACAO por ambiente (proporcional ao material direto) ----
tot_matdir=sum(matdir.values())
print("\n=== ALOCACAO POR AMBIENTE (proporcional ao material direto) ===")
print(f"{'Ambiente':24s} {'%mat':>6} {'Essencial':>12} {'Ess.Prime':>12}")
alloc={}
for a in sorted(matdir, key=lambda x:-matdir[x]):
    frac=matdir[a]/tot_matdir
    e=precos['Essencial (Hardt/5a)']*frac; p=precos['Essencial Prime (Hettich/10a)']*frac
    alloc[a]=(e,p)
    print(f"{a:24s} {frac*100:5.1f}% {e:12,.0f} {p:12,.0f}".replace(',','.'))
te=sum(v[0] for v in alloc.values()); tp=sum(v[1] for v in alloc.values())
print(f"{'TOTAL':24s} {'100%':>6} {te:12,.0f} {tp:12,.0f}".replace(',','.'))
