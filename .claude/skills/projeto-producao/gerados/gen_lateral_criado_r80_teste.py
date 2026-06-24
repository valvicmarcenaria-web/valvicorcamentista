#!/usr/bin/env python3
# DXF (R12, mm) — LATERAL DE CRIADO desenvolvida (planificada) p/ TESTE.
# Baseado no caso real criado-mudo (ver referencias/dobra-de-mdf.md, Variante 2):
#   dobra por BOLSO continuo ate a pele; bolso = arco da curva = R * angulo(rad).
#
# Parametros deste teste (pedido do Paulo, 24/06):
#   altura 350mm | raio R80 (raio, nao diametro) | profundidade 600mm | canto 90 graus
#
# A peca sai PLANA na CNC. A zona de dobra (bolso) é rebaixada ate deixar a pele,
# e depois a peca dobra 90 graus formando a quina de R80.
import math

ALT   = 350.0          # altura da lateral (Y) = eixo da dobra
R     = 80.0           # RAIO da curva (Ø160)
LEG1  = 600.0          # profundidade (aba reta principal)
LEG2  = 200.0          # aba de retorno (ASSUMIDA — ajustar c/ o Paulo)
ANG   = 90.0           # angulo do canto (graus)
THICK = 15.0           # espessura da chapa (provavel)
PELE  = 1.0            # pele deixada no fundo do bolso
TOOL_D= 6.0            # fresa (T2) — passo das ranhuras < TOOL_D p/ bolso liso
STEP  = 5.7            # passo das ranhuras (do .tap real; 5,7 < 6 => sobrepoe)

ARC   = R*math.radians(ANG)          # largura do bolso de dobra = comprimento do arco
DEPTH = THICK-PELE                    # profundidade do bolso
TOTAL = LEG1+ARC+LEG2                 # comprimento desenvolvido total (X)
X_B0, X_B1 = LEG1, LEG1+ARC           # inicio/fim do bolso (tangentes da curva)

ents=[]
def line(layer,x1,y1,x2,y2):
    ents.extend(["0","LINE","8",layer,"10",f"{x1:.4f}","20",f"{y1:.4f}","30","0.0",
                 "11",f"{x2:.4f}","21",f"{y2:.4f}","31","0.0"])
def rect(layer,x0,y0,x1,y1):
    for a,b,c,d in [(x0,y0,x1,y0),(x1,y0,x1,y1),(x1,y1,x0,y1),(x0,y1,x0,y0)]:
        line(layer,a,b,c,d)
def text(layer,x,y,h,s):
    ents.extend(["0","TEXT","8",layer,"10",f"{x:.4f}","20",f"{y:.4f}","30","0.0",
                 "40",f"{h:.4f}","1",s])

# 1) perimetro da chapa plana
rect("PERIMETRO", 0,0, TOTAL, ALT)
# 2) zona de dobra (bolso) — regiao a rebaixar ate a pele
rect("DOBRA", X_B0,0, X_B1,ALT)
# 3) eixos: tangentes (inicio/fim da curva) + apice da dobra
line("EIXO", X_B0,0, X_B0,ALT)
line("EIXO", X_B1,0, X_B1,ALT)
line("EIXO", (X_B0+X_B1)/2,0, (X_B0+X_B1)/2,ALT)
# 4) legendas
text("TEXTO", 10, ALT+12, 12.0, f"LATERAL CRIADO (planificada) - alt {ALT:.0f}")
text("TEXTO", LEG1/2-40, ALT/2, 14.0, f"ABA {LEG1:.0f} (profundidade)")
text("TEXTO", X_B0+5, ALT/2+20, 9.0, f"DOBRA 90deg R{R:.0f}: bolso {ARC:.1f}mm / pele {PELE:.0f}mm")
text("TEXTO", X_B1+10, ALT/2, 14.0, f"RETORNO {LEG2:.0f} (?)")

dxf=["0","SECTION","2","HEADER","9","$INSUNITS","70","4","0","ENDSEC",
 "0","SECTION","2","TABLES","0","TABLE","2","LAYER","70","4",
 "0","LAYER","2","PERIMETRO","70","0","62","7","6","CONTINUOUS",
 "0","LAYER","2","DOBRA","70","0","62","3","6","CONTINUOUS",
 "0","LAYER","2","EIXO","70","0","62","5","6","CONTINUOUS",
 "0","LAYER","2","TEXTO","70","0","62","4","6","CONTINUOUS",
 "0","ENDTAB","0","ENDSEC","0","SECTION","2","ENTITIES"]+ents+["0","ENDSEC","0","EOF"]
path="/home/user/valvicorcamentista/.claude/skills/projeto-producao/gerados/lateral_criado_r80_teste_teo.dxf"
import os; os.makedirs(os.path.dirname(path),exist_ok=True); open(path,"w").write("\n".join(dxf)+"\n")

print("LATERAL CRIADO (planificada) — teste R80")
print(f"  altura: {ALT:.0f}mm | canto: {ANG:.0f}deg | raio: R{R:.0f} (Ø{2*R:.0f})")
print(f"  comprimento desenvolvido: {TOTAL:.1f}mm = aba {LEG1:.0f} + bolso {ARC:.2f} + retorno {LEG2:.0f}")
print(f"  BOLSO de dobra: largura {ARC:.2f}mm (= arco 90deg a R{R:.0f}), no X {X_B0:.0f}..{X_B1:.1f}")
print(f"  rebaixo: {DEPTH:.0f}mm (chapa {THICK:.0f} - pele {PELE:.0f}); ranhuras passo {STEP:.1f}mm < fresa {TOOL_D:.0f} => bolso liso")
print(f"  deformacao da pele: {PELE/(2*R)*100:.2f}% (seguro)")
print(f"  arquivo: {path}")
