# -*- coding: utf-8 -*-
# Levantamento de material — Portas do vão da escada (Flávia Moacir / contato Jonathan)
# 3 portas de giro, MDF frente+verso, dobradiças invisíveis, perfil de alumínio na base,
# fechadura de fecho rolete. MC 37%, sem RT.
#
# PREMISSA ASSUMIDA (a confirmar): MDF Branco TX 15mm — cor não foi especificada no pedido.
# PREMISSA ASSUMIDA (a confirmar): as 3 medidas recebidas ("2,20x88 / 2,20x116 / 2,20x103")
#   são as 3 portas a orçar. O combinado inicial era 2 portas (vão subindo + vão descendo);
#   a Flávia enviou 3 medidas ("Tudo") — orçando as 3, sinalizado no relatório.

CHAPA_A, CHAPA_L = 2.75, 1.85          # m
CHAPA_AREA = CHAPA_A * CHAPA_L          # 5.0875 m²
APROV_15 = 0.82
DENS_MDF = 750                          # kg/m3 (densidade média MDF)
ESP_FACE = 0.015                        # 15mm por face

PRECO_CHAPA_BRANCO15 = 260.0            # R$/chapa (base Valvic)
PRECO_FITA_M = 2.5                      # R$/m (fita de borda branca)
PRECO_SARRAFO_M = 8.0                   # R$/m (sarrafo pinus, estrutura interna)
PRECO_DOBR_TE340 = 650.0                # R$/un — ESTIMATIVA DE MERCADO (Simonswerk Tectus TE.340.3D, confirmar c/ fornecedor)
PRECO_FECHO_ROLETE = 75.0               # R$/un — ESTIMATIVA DE MERCADO (fecho rolete p/ porta pivotante, confirmar)
PRECO_PERFIL_ALUM_M = 50.0              # R$/m — perfil de alumínio base (barra 2m, confirmar fornecedor)

# ---- portas (altura, largura) em metros ----
PORTAS = [
    ("Porta A", 2.20, 0.88),
    ("Porta B", 2.20, 1.16),
    ("Porta C", 2.20, 1.03),
]

print("="*72)
print("LEVANTAMENTO — PORTAS VÃO DA ESCADA (subindo/descendo) + 3ª medida")
print("="*72)

tot_area_mdf = 0.0
tot_perimetro = 0.0
tot_peso = 0.0
pesos = {}
for nome, h, w in PORTAS:
    area_face = h * w
    area_2faces = area_face * 2                  # frente e verso
    perimetro = 2 * (h + w)
    vol_mdf = area_2faces * ESP_FACE
    peso_mdf = vol_mdf * DENS_MDF
    peso_total = peso_mdf * 1.15                  # +15% alocação estrutura/ferragens
    tot_area_mdf += area_2faces
    tot_perimetro += perimetro
    tot_peso += peso_total
    pesos[nome] = peso_total
    print(f"\n{nome}: vão {h*100:.0f}x{w*100:.0f}cm")
    print(f"  área MDF (frente+verso): {area_2faces:.3f} m²")
    print(f"  perímetro (fita de borda): {perimetro:.2f} m")
    print(f"  peso estimado (MDF 15mm x2 + 15% estrutura/ferragem): {peso_total:.1f} kg")

print(f"\n--- TOTAIS BRUTOS ---")
print(f"Área MDF total (3 portas, frente+verso): {tot_area_mdf:.3f} m²")
print(f"Perímetro total (fita): {tot_perimetro:.2f} m")

# ---- plano de corte real (nesting) — NUNCA por m² ----
# Chapa 275x185. Peça = 220 x largura (a dimensão 220 sempre corre no eixo de 275).
# Larguras (88,116,103) só combinam 2-a-2 se soma <= 185cm.
# 88+88=176 (cabe) | 88+103=191 (não) | 88+116=204 (não) | 103+103=206 (não) | 116+116=232 (não)
print(f"\n--- PLANO DE CORTE (nesting real, chapa {CHAPA_A}x{CHAPA_L}) ---")
print("Peças: A-face1(220x88) A-face2(220x88) B-face1(220x116) B-face2(220x116) C-face1(220x103) C-face2(220x103)")
print("Chapa 1: A-face1 + A-face2 lado a lado (88+88=176cm <= 185cm) -> 1 chapa p/ as 2 faces da Porta A")
print("Chapa 2: B-face1 (116cm) -- sobra 69cm não aproveita nenhuma peça restante")
print("Chapa 3: B-face2 (116cm) -- sobra 69cm")
print("Chapa 4: C-face1 (103cm) -- sobra 82cm")
print("Chapa 5: C-face2 (103cm) -- sobra 82cm")
n_chapas_real = 5
n_chapas_naive = -(-tot_area_mdf // (CHAPA_AREA*APROV_15))  # ceil
print(f"\nChapas pelo NESTING REAL: {n_chapas_real}")
print(f"Chapas pela estimativa ingênua (área/aproveitamento): {int(n_chapas_naive)}  <- SUBESTIMARIA o corte real")

fita_total = tot_perimetro * 1.10   # +10% perda de filetagem
print(f"\nFita de borda (c/ 10% perda): {fita_total:.1f} m")

# ---- peso -> seleção de dobradiça (pesquisa: Simonswerk Tectus, referência de mercado p/ dobradiça invisível) ----
print(f"\n--- SELEÇÃO DE FERRAGEM (dobradiça invisível) por peso ---")
print("Linha Simonswerk Tectus (referência técnica p/ dobradiça invisível):")
print("  TE.240.3D -> até 60 kg | TE.340.3D -> até 80 kg (espessura mín. porta 35mm) | TE.540.3D -> até 120 kg")
for nome, h, w in PORTAS:
    p = pesos[nome]
    modelo = "TE.240.3D (60kg)" if p <= 60 else ("TE.340.3D (80kg)" if p <= 80 else "TE.540.3D (120kg)")
    print(f"  {nome}: {p:.1f} kg -> exigiria {modelo}")
print("  Decisão: padronizar TE.340.3D (80kg) nas 3 portas -> margem de segurança + peça única (estoque/manutenção).")
print("  Altura 2,20m > referência de catálogo (2,00m/2 dobradiças) -> 3 dobradiças por porta (reforço, evita empeno).")

N_DOBR_POR_PORTA = 3
n_dobradicas = N_DOBR_POR_PORTA * len(PORTAS)
print(f"\nTotal dobradiças TE.340.3D: {n_dobradicas} un (3 portas x 3 un)")

# ---- perfil de alumínio na base ----
larguras = [w for _, _, w in PORTAS]
print(f"\n--- PERFIL DE ALUMÍNIO NA BASE ---")
print(f"Larguras necessárias: {[f'{w*100:.0f}cm' for w in larguras]} (barra comercial de 2m)")
print("Corte: Porta A(88)+Porta C(103)=191cm <=200cm -> 1 barra de 2m | Porta B(116cm) -> 1 barra de 2m")
n_barras_alum = 2
metros_alum = n_barras_alum * 2.0

# ---- fechadura fecho rolete ----
n_fechaduras = len(PORTAS)

# ---- estrutura interna (sarrafo) ----
metros_sarrafo = sum(2*(h+w) * 1.3 for _, h, w in PORTAS)  # perímetro + reforços internos

print(f"\n{'='*72}\nCUSTO DE MATERIAL (compra)\n{'='*72}")
custo_chapas = n_chapas_real * PRECO_CHAPA_BRANCO15
custo_fita = fita_total * PRECO_FITA_M
custo_dobr = n_dobradicas * PRECO_DOBR_TE340
custo_fechadura = n_fechaduras * PRECO_FECHO_ROLETE
custo_perfil = metros_alum * PRECO_PERFIL_ALUM_M
custo_sarrafo = metros_sarrafo * PRECO_SARRAFO_M

print(f"MDF Branco TX 15mm ....... {n_chapas_real} chapas x R$ {PRECO_CHAPA_BRANCO15:.0f} = R$ {custo_chapas:,.2f}")
print(f"Fita de borda ............ {fita_total:.1f} m x R$ {PRECO_FITA_M:.2f} = R$ {custo_fita:,.2f}")
print(f"Dobradiças TE.340.3D ..... {n_dobradicas} un x R$ {PRECO_DOBR_TE340:.0f} = R$ {custo_dobr:,.2f}  [estimativa mercado]")
print(f"Fecho rolete ............. {n_fechaduras} un x R$ {PRECO_FECHO_ROLETE:.0f} = R$ {custo_fechadura:,.2f}  [estimativa mercado]")
print(f"Perfil alumínio base ..... {metros_alum:.1f} m x R$ {PRECO_PERFIL_ALUM_M:.0f} = R$ {custo_perfil:,.2f}  [estimativa mercado]")
print(f"Estrutura interna (sarrafo) {metros_sarrafo:.1f} m x R$ {PRECO_SARRAFO_M:.0f} = R$ {custo_sarrafo:,.2f}")

material = custo_chapas + custo_fita + custo_dobr + custo_fechadura + custo_perfil + custo_sarrafo
logistica = 300.0
visita = 200.0
fixedR = material + logistica + visita
print(f"\nSubtotal material ........................ R$ {material:,.2f}")
print(f"Logística ................................ R$ {logistica:,.2f}")
print(f"Visita técnica ............................ R$ {visita:,.2f}")
print(f"CUSTO DIRETO (fixedR) .................... R$ {fixedR:,.2f}")

# ---- motor de precificação (params oficiais do validador) ----
NF, PARC, VEND, ERRO, SERRA, MANUT = 0.04, 0.08, 0.03, 0.005, 0.002, 0.005
a = NF + PARC + VEND + ERRO + SERRA + MANUT
liqF = 1 - (NF + PARC)
PROG, COORD, MARC, RT = 0.008, 0.01, 0.025, 0.0
b = PROG + COORD + MARC + RT
MC = 0.37
divisor = 1 - a - liqF*b - MC
inv_total = fixedR / divisor

print(f"\n{'='*72}\nPRECIFICAÇÃO (motor validador — a={a*100:.1f}% liqF={liqF:.2f} b={b*100:.1f}% MC={MC*100:.0f}% RT=0)\n{'='*72}")
print(f"Divisor: 1 - {a:.3f} - {liqF:.2f}x{b:.3f} - {MC:.2f} = {divisor:.5f}")
print(f"INVESTIMENTO TOTAL (3 portas) = R$ {fixedR:,.2f} / {divisor:.5f} = R$ {inv_total:,.2f}")

print(f"\n--- Alocação proporcional por porta (área de MDF) ---")
for nome, h, w in PORTAS:
    area_2faces = h*w*2
    frac = area_2faces / tot_area_mdf
    print(f"  {nome} ({h*100:.0f}x{w*100:.0f}): {frac*100:.1f}% -> R$ {inv_total*frac:,.2f}")

print(f"\nMC verificada = {MC*100:.1f}% | RT = 0% | Sem desconto.")
