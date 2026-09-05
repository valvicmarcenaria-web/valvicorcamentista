# -*- coding: utf-8 -*-
# LEVANTAMENTO — LM / SPE Nova Lima 1 (arq. Lodi Motta / JBA) — comercial.
# Painel Corretores/Pilar (MOB 01) + Painel/Pérgula Gourmet-Lounge (MOB 02).
# CALCULAR, nunca ESTIMAR: cotas do vetor do CAD (planta/elevações). Alturas painel = 2,62 m (confirmado).
import math
CHAPA = 2.75*1.85          # 5.0875 m2
APRO_PN = 0.85             # aproveitamento paineis planos grandes
APRO_MV = 0.82             # moveis
APRO_6  = 0.55
PRC = {15:500, 18:600, 6:300}   # MDF cor (base). Arauco Realce Cravo/Moscada/madeirado -> ver FLAG premium.

def chapas(area, esp, apro): 
    return math.ceil(area/(CHAPA*apro)) if area>0 else 0

# ============================================================ CRAVO TREND (paineis 15mm)
# --- MOB 02 paredes (comprimento planta x 2,62) ---
paredes_m02 = {'E05 esquerda':4.27,'Topo':2.946,'Copa E04':3.384,'Corredor pergola':5.63,
               'E03':1.42,'Hall E02':1.57,'IS inferior frente':1.86,'Retornos/faces IS':2.937}
A_cravo_m02 = sum(paredes_m02.values())*2.62
# --- MOB 01 ---
A_corretor = 8.175*3.85           # backdrop 817,5 x 385 (faixa 125 + stand 260)
A_pilar    = 0.445*3.85*2.5       # envolvimento coluna ~2,5 faces
A_cravo_m01 = A_corretor + A_pilar
# --- porta ripada (elev.2 gourmet) + armario gourmet exterior (Cravo) ---
A_porta_ripada = 0.90*2.10        # 1 porta ripada
A_arm_ext = (0.975*2.48)*2 + (0.42*2.48)*2   # frente+costas + 2 laterais do armario gourmet (Cravo)
A_CRAVO = A_cravo_m02 + A_cravo_m01 + A_porta_ripada + A_arm_ext
ch_cravo = chapas(A_CRAVO,15,APRO_PN)

# ============================================================ MOSCADA MATT (moveis 15/18/6)
# Movel Lounge 300x60(40 corpo)x35 : tampo+base+2lat+3div+fundo+4 gavetas
A_ml = 0
A_ml += 3.00*0.35            # tampo
A_ml += 3.00*0.35            # base
A_ml += 0.35*0.40*2          # laterais
A_ml += 0.35*0.40*3          # divisorias (3)
A_ml_6 = 3.00*0.40           # fundo 6mm
# 4 gavetas ~0.477 x 0.17 frente + caixa (2 lat 0.31x0.17 + contraf 0.477x0.17) + fundo 6
A_ml += (0.477*0.17 + 0.31*0.17*2 + 0.477*0.17)*4
A_ml_6 += 0.477*0.31*4       # fundos gaveta
# Armario Gourmet interior/nicho Moscada: nicho 0.805x0.855 fundo + prat + compart 56
A_am = 0
A_am += 0.805*0.855          # fundo nicho aberto
A_am += 0.805*0.42*2         # 2 prateleiras internas
A_am += 0.805*0.56           # fundo compartimento fechado (Moscada)
A_am += 0.42*0.56*2          # laterais internas compart
A_MOSCADA = A_ml + A_am
A_MOSCADA_6 = A_ml_6
ch_moscada = chapas(A_MOSCADA,15,APRO_MV)
ch_moscada6 = chapas(A_MOSCADA_6,6,APRO_6)

# ============================================================ MDF MADEIRADO
A_perg_revest = 0.46*3.09*28     # revestimento das 28 ripas (~0,46 m/m desenv.)
A_forro_mad   = 6.0              # forro em MDF madeirado (trecho, estimado -> FLAG)
A_MAD = A_perg_revest + A_forro_mad
ch_mad = chapas(A_MAD,15,APRO_PN)

# ============================================================ METALON (pergola) — dado do cliente
BARRAS = 28
metalon_mat = BARRAS*150
metalon_frete = 150              # 1 entrega dedicada (confirmado)
metalon_total = metalon_mat + metalon_frete

# ============================================================ CUSTO MATERIAL
custo_cravo   = ch_cravo*PRC[15]
custo_moscada = ch_moscada*PRC[15] + ch_moscada6*PRC[6]
custo_mad     = ch_mad*PRC[15]
# terceiros / insumos
pes_metalicos = 6*60             # movel lounge sobre pes
rodape_inox   = (24+8)*40        # ~32 m perfil inox h5 x R$40/m (terceiro inox)
rodape_polies = 8*18             # poliestireno santa luzia (corretor)
porta_vidro   = 0                # vidro jateado do pilar = VIDRACEIRO (terceiro), fora do escopo Valvic
sanca_led     = 350              # perfil+fita+fonte 3000K
moldura_hidr  = 200              # caixa MDF moldura hidrante
ch_tot = ch_cravo+ch_moscada+ch_moscada6+ch_mad
fita   = ch_tot*80
insumos= ch_tot*60
usinagem = 900                   # frisos quinas + puxador calha (SEM porta ripada/veneziana = terceiro)
visitas  = 3*250
logistica= 4*150
forro_gypsum = 0                 # gesseiro -> FLAG (por conta de terceiro/cliente?)

material = (custo_cravo+custo_moscada+custo_mad+metalon_total+pes_metalicos+rodape_inox+
            rodape_polies+porta_vidro+sanca_led+moldura_hidr+fita+insumos+usinagem+visitas+logistica)

print("=== CHAPAS ===")
print(f"Cravo Trend : {A_CRAVO:6.1f} m2 -> {ch_cravo} chapas (15mm) = R$ {custo_cravo}")
print(f"Moscada 15  : {A_MOSCADA:6.1f} m2 -> {ch_moscada} chapas = R$ {ch_moscada*PRC[15]}")
print(f"Moscada 6   : {A_MOSCADA_6:6.1f} m2 -> {ch_moscada6} chapas = R$ {ch_moscada6*PRC[6]}")
print(f"MDF madeirado:{A_MAD:6.1f} m2 -> {ch_mad} chapas = R$ {custo_mad}")
print(f"TOTAL chapas: {ch_tot}")
print("\n=== METALON PERGOLA ===")
print(f"{BARRAS} barras x R$150 + R$150 frete = R$ {metalon_total}")
print("\n=== TERCEIROS/INSUMOS ===")
print(f"pes {pes_metalicos} · rodape inox {rodape_inox} · rodape polies {rodape_polies} · porta vidro {porta_vidro} · sanca LED {sanca_led} · moldura hidr {moldura_hidr}")
print(f"fita {fita} · insumos {insumos} · usinagem {usinagem} · visitas {visitas} · logistica {logistica}")
print(f"\n=== CUSTO MATERIAL TOTAL = R$ {material:,.0f} ===".replace(',','.'))

# ============================================================ PRECO (comercial)
# motor com cartao (a=0.18, liqF=0.88, b sem RT=0.043 prog/coord/marc) — RT a confirmar.
print("\n=== PRECO (motor comercial) ===")
for mc in (0.38,0.40,0.43):
    for rt in (0.0,0.10):
        b=(0.8+1+2.5+rt*100)/100; a=0.18; liqF=0.88
        denom=1-a-liqF*b-mc
        inv=material/denom
        print(f"MC {int(mc*100)}% · RT {int(rt*100)}% -> denom {denom:.3f} -> INVEST R$ {inv:,.0f}".replace(',','.'))
