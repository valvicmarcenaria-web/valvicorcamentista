#!/usr/bin/env python3
# DXF (R12, mm) — TAMPO DE MESA REDONDO Ø309 (30,9 cm) com bisel 45 atravessando 30mm.
# Mesma tecnica do Ø300: 2 chapas de 15mm, cada uma biselada a 45; empilhadas o bisel
# vira UM cone continuo (45 = 1:1, cada 15mm de profundidade anda 15mm no raio).
#
# Calibracao do Paulo: desenhar +3mm no DIAMETRO (a fresa "come" 3mm).
#   chave do encaixe: DIFERENCA DE RAIO entre os 2 circulos = espessura (15mm).
#
# Geometria do cone:
#   chapa de CIMA:  topo 309 -> base 279
#   chapa de BAIXO: topo 279 -> base 249   (faces de cola coincidem em 279)
# Cada peca leva furo de centro p/ CAVILHA de 8mm (alinhamento concentrico).
import math, os

THICK   = 15.0          # espessura de cada chapa
KERF_D  = 3.0           # "come" no diametro (calibracao do Paulo)
TOP_FIN = 309.0         # diametro final do topo desejado (30,9 cm)
PIN_D   = 8.0           # furo de centro p/ cavilha de alinhamento

D1 = TOP_FIN + KERF_D                 # chapa de cima  -> 312
D2 = D1 - 2*THICK                     # chapa de baixo -> 282 (raio 15mm menor)
R1, R2, RP = D1/2, D2/2, PIN_D/2
GAP = 30.0                            # folga entre as duas pecas no nesting

ents=[]
def circle(layer,cx,cy,r):
    ents.extend(["0","CIRCLE","8",layer,"10",f"{cx:.4f}","20",f"{cy:.4f}","30","0.0","40",f"{r:.4f}"])
def text(layer,cx,cy,h,s):
    ents.extend(["0","TEXT","8",layer,"10",f"{cx:.4f}","20",f"{cy:.4f}","30","0.0",
                 "40",f"{h:.4f}","1",s,"72","1","11",f"{cx:.4f}","21",f"{cy:.4f}","31","0.0"])

# ---- peca 1: chapa de CIMA ----
c1x, c1y = R1, R1
circle("BISEL", c1x, c1y, R1)
circle("CENTRO", c1x, c1y, RP)
text("TEXTO", c1x, c1y - R1 - 18, 10.0, f"CIMA Ø{D1:.0f} (topo{TOP_FIN:.0f}/base{TOP_FIN-2*THICK:.0f})")

# ---- peca 2: chapa de BAIXO ----
c2x = c1x + R1 + GAP + R2
c2y = R1
circle("BISEL", c2x, c2y, R2)
circle("CENTRO", c2x, c2y, RP)
text("TEXTO", c2x, c2y - R1 - 18, 10.0, f"BAIXO Ø{D2:.0f} (topo{TOP_FIN-2*THICK:.0f}/base{TOP_FIN-4*THICK:.0f})")

dxf=["0","SECTION","2","HEADER","9","$INSUNITS","70","4","0","ENDSEC",
 "0","SECTION","2","TABLES","0","TABLE","2","LAYER","70","3",
 "0","LAYER","2","BISEL","70","0","62","7","6","CONTINUOUS",
 "0","LAYER","2","CENTRO","70","0","62","1","6","CONTINUOUS",
 "0","LAYER","2","TEXTO","70","0","62","5","6","CONTINUOUS",
 "0","ENDTAB","0","ENDSEC","0","SECTION","2","ENTITIES"]+ents+["0","ENDSEC","0","EOF"]
path=os.path.join(os.path.dirname(os.path.abspath(__file__)),"tampo_redondo_309_bisel45_teo.dxf")
open(path,"w").write("\n".join(dxf)+"\n")

print("TAMPO Ø309 (30,9cm) bisel 45 em 2 chapas de 15mm")
print(f"  DESENHAR: CIMA Ø{D1:.0f} (raio {R1:.1f}) | BAIXO Ø{D2:.0f} (raio {R2:.1f})")
print(f"  dif. de raio = {R1-R2:.0f}mm (= espessura {THICK:.0f}mm) -> cone continuo")
print(f"  FINAL: topo {TOP_FIN:.0f} -> emenda {TOP_FIN-2*THICK:.0f} -> base {TOP_FIN-4*THICK:.0f}")
print(f"  arquivo: {path}")
