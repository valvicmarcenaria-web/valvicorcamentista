#!/usr/bin/env python3
# DXF (R12, mm) — TAMPO REDONDO Ø305 (30,5cm) x 30mm, TOPO RETO 6mm + CHANFRO 45.
# 2 chapas de 15mm empilhadas (a fresa de 45 corta no max 18mm).
#
# PERFIL DA BORDA (z=0 base, z=30 topo):
#   z 30->24 (6mm) : RETO vertical  -> Ø305 (raio 152,5)   [corte com fresa 6mm / T2]
#   z 24->0 (24mm) : 45 graus       -> Ø305 desce ate Ø257 (raio 152,5 -> 128,5)
#   emenda em z=15 : Ø287 (raio 143,5)  -> as 2 faces de 45 se encontram (cone continuo)
#
#   DISCO DE CIMA (z15..30): 6mm reto + 9mm de 45  (por isso "tem MENOS 45")
#   DISCO DE BAIXO(z0..15) : 15mm de 45 inteiros
#
# KERF do Paulo: fresa de 45 "come 3mm em volta" = 3mm POR LADO.
#   -> os circulos do BISEL sao desenhados +3mm no raio (+6 no diametro).
#   (o contorno reto e cortado pela fresa de 6mm com offset por fora = desenhar no final)
#
# Cada disco leva furo de centro Ø8 p/ CAVILHA (empilhar concentrico, sem degrau).
import math, os

TOPO_FIN = 305.0     # Ø final do topo (mais largo)
H_TOT    = 30.0
RETO     = 6.0       # altura do topo reto (vertical)
THICK    = 15.0
KERF_LADO= 3.0       # a fresa de 45 come 3mm por lado (raio)
PIN_D    = 8.0

R_topo  = TOPO_FIN/2.0                 # 152,5
# desce da borda de topo do bisel (z=24) ate a emenda (z=15): 24-15 = 9mm -> -9 no raio
R_emenda= R_topo - (H_TOT-RETO-THICK)  # 152,5 - 9 = 143,5   (Ø287)
R_base  = R_topo - (H_TOT-RETO)        # 152,5 - 24 = 128,5  (Ø257)
RP      = PIN_D/2.0

# circulos a DESENHAR
R_bisel_cima  = R_topo   + KERF_LADO   # 155,5  (Ø311)  -> apos corte, topo do bisel = Ø305
R_contorno_cima = R_topo               # 152,5  (Ø305)  -> fresa 6mm (topo reto), corte por fora
R_bisel_baixo = R_emenda + KERF_LADO   # 146,5  (Ø293)  -> apos corte, emenda = Ø287
R_emenda_ref  = R_emenda               # 143,5  (Ø287)  referencia da emenda/contorno de baixo

GAP = 30.0                             # nesting 45: 30mm entre pecas no lado chanfrado

ents=[]
def circle(layer,cx,cy,r):
    ents.extend(["0","CIRCLE","8",layer,"10",f"{cx:.4f}","20",f"{cy:.4f}","30","0.0","40",f"{r:.4f}"])
def text(layer,cx,cy,h,s):
    ents.extend(["0","TEXT","8",layer,"10",f"{cx:.4f}","20",f"{cy:.4f}","30","0.0",
                 "40",f"{h:.4f}","1",s,"72","1","11",f"{cx:.4f}","21",f"{cy:.4f}","31","0.0"])

# ---- DISCO DE CIMA ----
c1x = R_bisel_cima; c1y = R_bisel_cima
circle("BISEL",    c1x, c1y, R_bisel_cima)      # T7 45 (desenhar Ø311)
circle("CONTORNO", c1x, c1y, R_contorno_cima)   # T2 6mm reto (Ø305)
circle("CENTRO",   c1x, c1y, RP)
text("TEXTO", c1x, c1y - R_bisel_cima - 20, 9.0, "DISCO CIMA")
text("TEXTO", c1x, c1y - R_bisel_cima - 33, 8.0, "BISEL desenhar O311 / TOPO RETO 6mm O305")

# ---- DISCO DE BAIXO ----
c2x = c1x + R_bisel_cima + GAP + R_bisel_baixo
c2y = R_bisel_cima
circle("BISEL",    c2x, c2y, R_bisel_baixo)     # T7 45 (desenhar Ø293)
circle("CONTORNO", c2x, c2y, R_emenda_ref)      # emenda/contorno final Ø287
circle("CENTRO",   c2x, c2y, RP)
text("TEXTO", c2x, c2y - R_bisel_cima - 20, 9.0, "DISCO BAIXO")
text("TEXTO", c2x, c2y - R_bisel_cima - 33, 8.0, "BISEL desenhar O293 / emenda O287 -> base O257")

dxf=["0","SECTION","2","HEADER","9","$INSUNITS","70","4","0","ENDSEC",
 "0","SECTION","2","TABLES","0","TABLE","2","LAYER","70","4",
 "0","LAYER","2","BISEL","70","0","62","1","6","CONTINUOUS",
 "0","LAYER","2","CONTORNO","70","0","62","7","6","CONTINUOUS",
 "0","LAYER","2","CENTRO","70","0","62","2","6","CONTINUOUS",
 "0","LAYER","2","TEXTO","70","0","62","5","6","CONTINUOUS",
 "0","ENDTAB","0","ENDSEC","0","SECTION","2","ENTITIES"]+ents+["0","ENDSEC","0","EOF"]
path=os.path.join(os.path.dirname(os.path.abspath(__file__)),"tampo_redondo_305_chanfro45_topo6_teo.dxf")
open(path,"w").write("\n".join(dxf)+"\n")

print("TAMPO Ø305 x30mm — topo reto 6mm + chanfro 45 (2 chapas 15mm)")
print("  DESENHAR:")
print(f"    CIMA : BISEL Ø{2*R_bisel_cima:.0f} + CONTORNO(topo reto) Ø{2*R_contorno_cima:.0f}")
print(f"    BAIXO: BISEL Ø{2*R_bisel_baixo:.0f} + emenda Ø{2*R_emenda_ref:.0f}")
print("  FINAL (apos 45, kerf 3mm/lado ja descontado):")
print(f"    topo Ø{TOPO_FIN:.0f} -> emenda Ø{2*R_emenda:.0f} -> base Ø{2*R_base:.0f}")
print(f"    topo reto {RETO:.0f}mm | chanfro {H_TOT-RETO:.0f}mm | furo cavilha Ø{PIN_D:.0f}")
print(f"  arquivo: {path}")
