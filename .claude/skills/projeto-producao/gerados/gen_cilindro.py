#!/usr/bin/env python3
# Gerador de .tap no dialeto JRG CNC SOLID TAF (Vision V1.01 / Aspire)
# Cilindro R200 x H500: 2 discos + 4 reguas + painel ranhurado.
import math

# ---- parametros da maquina / material (dialeto JRG decodificado) ----
THICK   = 15.0          # espessura da chapa (mm)
CLEAR   = THICK + 5.08  # altura de seguranca (clearance) = 20.08
Z_THRU  = -0.100        # corte passante: Z-zero na mesa, 0.1 no sacrificio
SKIN    = 1.0           # pele deixada na dobra
Z_KERF  = THICK - (THICK - SKIN)   # = SKIN = 1.0 (corte parcial deixa 1mm)
TOOL_D  = 6.0
TOOL_R  = TOOL_D / 2.0  # 3.0
SPACING = 12.0          # espacamento dos vincos
RPM     = 24000
FPLUNGE = 2500.0
FCUT    = 10000.0

# ---- projeto do cilindro ----
R       = 200.0
HEIGHT  = 500.0
CIRC    = 2 * math.pi * R          # ~1256.637

out = []
n = [5]  # contador de linha (comeca em N5)

def body(code):
    out.append(f"N{n[0]}{code}")   # linhas de corpo: SEM espaco apos N
    n[0]+=1
def named(code):
    out.append(f"N{n[0]} {code}")  # cabecalho/rodape: COM espaco apos N
    n[0]+=1
def comment(txt):
    out.append(txt)                # comentario: sem N, mas consome numero
    n[0]+=1
def f3(v): return f"{v:.3f}"

# ---- cabecalho ----
out.append("(JrgCnC - Vision V1.01 - by Aspire)")
out.append("(######## Troca de ferramentas ########)")
out.append("(   NUMERO DA FERRAMENTA:2)")
out.append(" ")
named("M158"); named("M162"); named("M6T2"); named(f"M3S{RPM}"); named("G0 G43 H2")
# n agora = 10

# ---- helpers de operacao ----
def profile_circle(cx, cy, rad, z):
    """contorno circular (4 arcos G3 CCW), plunge+retract. tool center em 'rad'."""
    x0, y0 = cx+rad, cy
    body(f"G00X{f3(x0)}Y{f3(y0)}")
    body(f"G00X{f3(x0)}Y{f3(y0)}Z{f3(CLEAR)}")
    body(f"G1X{f3(x0)}Y{f3(y0)}Z{f3(z)}F{FPLUNGE:.1f}")
    body(f"G3X{f3(cx)}Y{f3(cy+rad)}I{f3(-rad)}J{f3(0)}F{FCUT:.1f}")
    body(f"G3X{f3(cx-rad)}Y{f3(cy)}I{f3(0)}J{f3(-rad)}")
    body(f"G3X{f3(cx)}Y{f3(cy-rad)}I{f3(rad)}J{f3(0)}")
    body(f"G3X{f3(x0)}Y{f3(y0)}I{f3(0)}J{f3(rad)}")
    body(f"G00X{f3(x0)}Y{f3(y0)}Z{f3(CLEAR)}")

def profile_rect(x0, y0, x1, y1, z, offset=TOOL_R):
    """retangulo (contorno externo, offset para fora). plunge+retract."""
    ax0,ay0,ax1,ay1 = x0-offset, y0-offset, x1+offset, y1+offset
    body(f"G00X{f3(ax0)}Y{f3(ay0)}")
    body(f"G00X{f3(ax0)}Y{f3(ay0)}Z{f3(CLEAR)}")
    body(f"G1X{f3(ax0)}Y{f3(ay0)}Z{f3(z)}F{FPLUNGE:.1f}")
    body(f"G1X{f3(ax1)}Y{f3(ay0)}Z{f3(z)}F{FCUT:.1f}")
    body(f"G1X{f3(ax1)}Y{f3(ay1)}Z{f3(z)}")
    body(f"G1X{f3(ax0)}Y{f3(ay1)}Z{f3(z)}")
    body(f"G1X{f3(ax0)}Y{f3(ay0)}Z{f3(z)}")
    body(f"G00X{f3(ax0)}Y{f3(ay0)}Z{f3(CLEAR)}")

def kerf_grooves(px0, py0, px1, py1, spacing, z):
    """ranhuras verticais (ao longo de Y), serpentina, 1 plunge / 1 retract."""
    width = px1 - px0
    n_g = round(width / spacing)
    span = (n_g - 1) * spacing
    start = px0 + (width - span) / 2.0
    gx = [start + k*spacing for k in range(n_g)]
    top, bot = py1, py0
    # plunge no 1o vinco, topo
    body(f"G00X{f3(gx[0])}Y{f3(top)}")
    body(f"G00X{f3(gx[0])}Y{f3(top)}Z{f3(CLEAR)}")
    body(f"G1X{f3(gx[0])}Y{f3(top)}Z{f3(z)}F{FPLUNGE:.1f}")
    body(f"G1X{f3(gx[0])}Y{f3(bot)}Z{f3(z)}F{FCUT:.1f}")  # corta vinco 0 (desce)
    cur = bot
    for k in range(1, n_g):
        body(f"G1X{f3(gx[k])}Y{f3(cur)}Z{f3(z)}")          # conector
        nxt = top if cur==bot else bot
        body(f"G1X{f3(gx[k])}Y{f3(nxt)}Z{f3(z)}")          # corta vinco k
        cur = nxt
    body(f"G00X{f3(gx[-1])}Y{f3(cur)}Z{f3(CLEAR)}")
    return n_g

# ====== CORTE 1: estrutura (passante Z-0.1) ======
# 2 discos R200 -> toolpath R203 (contorno externo, deixa disco R200)
profile_circle(300.0, 900.0, R + TOOL_R, Z_THRU)
profile_circle(800.0, 900.0, R + TOOL_R, Z_THRU)
# 4 reguas 500(Y) x 80(X)
for i in range(4):
    rx0 = 1100.0 + i*120.0
    profile_rect(rx0, 700.0, rx0+80.0, 1200.0, Z_THRU)

# ====== CORTE 2: ranhuras de dobra do painel (parcial Z+1) ======
comment("(Corte 2)"); comment("()")
PX0, PY0 = 30.0, 30.0
PX1, PY1 = PX0 + CIRC, PY0 + HEIGHT
n_grooves = kerf_grooves(PX0, PY0, PX1, PY1, SPACING, Z_KERF)

# ====== CORTE 3: solta o painel (passante Z-0.1) POR ULTIMO ======
comment("(Corte 3)"); comment("()")
profile_rect(PX0, PY0, PX1, PY1, Z_THRU)

# ---- rodape ----
named("M159"); named("M163"); named("M5"); named("G0 Y2840X51Z50"); named("M30"); named("M30")
out.append("%")

text = "\n".join(out) + "\n"
path = "/home/user/valvicorcamentista/.claude/skills/projeto-producao/gerados/cilindro_r200_h500_teo.tap"
import os
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, "w") as fh:
    fh.write(text)

# ---- VALIDACAO de seguranca ----
import re
zmin = 999
for ln in out:
    m = re.search(r'Z(-?\d+\.\d+)', ln)
    if m:
        zmin = min(zmin, float(m.group(1)))
print(f"linhas: {len(out)}")
print(f"vincos gerados: {n_grooves}")
print(f"circunferencia: {CIRC:.3f} mm")
print(f"Z minimo no arquivo: {zmin}  (limite de seguranca: -0.1)")
assert zmin >= -0.1 - 1e-9, "FALHA DE SEGURANCA: Z abaixo de -0.1!"
print("OK seguranca: nenhum Z passa de -0.1")
print(f"clearance usada: {CLEAR} (espessura {THICK} + 5.08)")
print(f"Z corte passante: {Z_THRU} | Z ranhura: {Z_KERF}")
