# -*- coding: utf-8 -*-
# Levantamento de material — Portas + painéis do vão da escada (Flávia Moacir / contato Jonathan)
# REV.03 — cliente confirmou: Porta 116cm + Porta 88cm + painéis de complemento do vão.
# MDF Ultra amadeirado fosco. Dobradiça Häfele IN600 (link do cliente). Perfil alumínio R$10/m.
# MC 37%, sem RT.
#
# LEITURA DO VÃO: "vão de passagem da escada" = 4,45 x 2,20 (medida passada pela Flávia).
# Portas 116+88=204cm ocupam parte da largura -> sobra 4,45-2,04=2,41m de PAINEL (uma só face,
# não é porta de giro) completando o vão até os 4,45m. PREMISSA — confirmar leitura do vão.

CHAPA_A, CHAPA_L = 2.75, 1.85          # m
CHAPA_AREA = CHAPA_A * CHAPA_L          # 5.0875 m²
APROV_15 = 0.82
DENS_MDF = 750                          # kg/m3 (densidade média MDF)
ESP_FACE = 0.015                        # 15mm por face

PRECO_CHAPA_ULTRA15 = 580.0             # R$/chapa — MDF Ultra amadeirado fosco (Duratex) — estimativa mercado, confirmar fornecedor
PRECO_FITA_M = 4.0                      # R$/m (fita de borda amadeirado fosco)
PRECO_SARRAFO_M = 8.0                   # R$/m (sarrafo pinus, estrutura interna)
PRECO_DOBR_IN600 = 138.51               # R$/un — Häfele IN600 (referência de mercado, link do cliente)
PRECO_FECHO_ROLETE = 75.0               # R$/un — estimativa de mercado (fecho rolete p/ porta pivotante)
PRECO_PERFIL_ALUM_M = 10.0              # R$/m — perfil de alumínio base (valor passado pelo cliente)

VAO_TOTAL = 4.45                        # m — "vão de passagem da escada" (medida da Flávia)
ALTURA = 2.20

# ---- portas (nome, altura, largura, nº dobradiças) ----
PORTAS = [
    ("Porta 1 (116cm)", ALTURA, 1.16, 4),   # porta maior -> 4 dobradiças (reforço, decisão do cliente)
    ("Porta 2 (88cm)",  ALTURA, 0.88, 3),   # padrão
]
LARG_PORTAS = sum(w for _, _, w, _ in PORTAS)
LARG_PAINEL = VAO_TOTAL - LARG_PORTAS      # sobra do vão -> painel de complemento

print("="*72)
print("LEVANTAMENTO — PORTAS (116+88) + PAINÉIS DE COMPLEMENTO DO VÃO — REV.03")
print("MDF Ultra amadeirado fosco | Dobradiça Häfele IN600 | Perfil alumínio R$10/m")
print("="*72)
print(f"\nVão de passagem da escada (informado): {VAO_TOTAL*100:.0f}x{ALTURA*100:.0f}cm")
print(f"Largura ocupada pelas 2 portas: {LARG_PORTAS*100:.0f}cm")
print(f"Largura de painel de complemento: {LARG_PAINEL*100:.0f}cm (1 face, revestimento de parede — não é porta)")

# ================= PORTAS =================
tot_area_mdf_portas = 0.0
tot_perimetro_portas = 0.0
pesos = {}
for nome, h, w, ndobr in PORTAS:
    area_2faces = h * w * 2                       # frente e verso
    perimetro = 2 * (h + w)
    peso_total = (area_2faces * ESP_FACE * DENS_MDF) * 1.15   # MDF 2 faces + 15% estrutura/ferragem
    tot_area_mdf_portas += area_2faces
    tot_perimetro_portas += perimetro
    pesos[nome] = peso_total
    print(f"\n{nome}: vão {h*100:.0f}x{w*100:.0f}cm")
    print(f"  área MDF (frente+verso): {area_2faces:.3f} m²")
    print(f"  perímetro (fita de borda): {perimetro:.2f} m")
    print(f"  peso estimado: {peso_total:.1f} kg  |  dobradiças especificadas: {ndobr} un")

# ================= PAINEL =================
area_painel = ALTURA * LARG_PAINEL             # 1 face só
perim_painel = 2 * (ALTURA + LARG_PAINEL)
print(f"\nPainel de complemento: {ALTURA*100:.0f}x{LARG_PAINEL*100:.0f}cm (1 face)")
print(f"  área MDF (1 face): {area_painel:.3f} m²")
print(f"  perímetro (fita de borda): {perim_painel:.2f} m")

tot_area_mdf = tot_area_mdf_portas + area_painel
tot_perimetro = tot_perimetro_portas + perim_painel
print(f"\n--- TOTAIS BRUTOS ---")
print(f"Área MDF total (portas 2 faces + painel 1 face): {tot_area_mdf:.3f} m²")
print(f"Perímetro total (fita): {tot_perimetro:.2f} m")

# ---- plano de corte real (nesting) — NUNCA por m² ----
print(f"\n--- PLANO DE CORTE (nesting real, chapa {CHAPA_A}x{CHAPA_L}) ---")
print("PORTAS — peças 220 x largura (o lado de 220cm corre no eixo de 275cm da chapa):")
print("  P1-face1(220x116) P1-face2(220x116) P2-face1(220x88) P2-face2(220x88)")
print("  116+88=204cm > 185cm -> não cabem juntas na mesma chapa")
print("  Chapa 1: P1-face1 (116cm) -- sobra 69cm")
print("  Chapa 2: P1-face2 (116cm) -- sobra 69cm")
print("  Chapa 3: P2-face1 (88cm)  -- sobra 97cm")
print("  Chapa 4: P2-face2 (88cm)  -- sobra 97cm")
print("PAINEL — 220x241cm: excede as DUAS dimensões úteis da chapa (275x185) em qualquer orientação")
print("  (241>185 e 220>185) -> não sai de 1 chapa. Dividido em 2 tiras de ~120,5cm (emenda central, menos junta visível):")
print("  Chapa 5: tira painel 220x120,5cm -- sobra 64,5cm")
print("  Chapa 6: tira painel 220x120,5cm -- sobra 64,5cm")
n_chapas_real = 6
n_chapas_naive = -(-tot_area_mdf // (CHAPA_AREA*APROV_15))  # ceil
print(f"\nChapas pelo NESTING REAL: {n_chapas_real}")
print(f"Chapas pela estimativa ingênua (área/aproveitamento): {int(n_chapas_naive)}  <- {'igual' if int(n_chapas_naive)==n_chapas_real else 'SUBESTIMARIA'} o corte real")

fita_total = tot_perimetro * 1.10   # +10% perda de filetagem
print(f"\nFita de borda (c/ 10% perda): {fita_total:.1f} m")

# ---- dobradiças: Häfele IN600 (produto indicado pelo cliente) ----
print(f"\n--- FERRAGEM — DOBRADIÇA HÄFELE IN600 (link do cliente) ---")
print("Especificação (pesquisa): regulagem 3D, até 60kg, espessura mín. porta 35mm, ângulo 180°,")
print("acabamento preto. Vendida por unidade (1 dobradiça + 2 capas + parafusos).")
for nome, h, w, ndobr in PORTAS:
    p = pesos[nome]
    alerta = "  <= excede 60kg nominal; reforçada com 4ª dobradiça (decisão cliente)" if p > 60 else "  <= dentro da capacidade nominal"
    print(f"  {nome}: peso {p:.1f} kg{alerta}")
n_dobradicas = sum(nd for _, _, _, nd in PORTAS)
print(f"\nTotal dobradiças IN600: {n_dobradicas} un (Porta 1: 4un + Porta 2: 3un)")

# ---- perfil de alumínio na base (só nas portas) ----
print(f"\n--- PERFIL DE ALUMÍNIO NA BASE (portas) ---")
larguras = [w for _, _, w, _ in PORTAS]
soma_larg = sum(larguras)
print(f"Larguras: {[f'{w*100:.0f}cm' for w in larguras]} -> soma {soma_larg*100:.0f}cm > barra de 200cm -> 2 barras de 2m")
n_barras_alum = 2
metros_alum = n_barras_alum * 2.0

# ---- fechadura fecho rolete (só nas portas) ----
n_fechaduras = len(PORTAS)

# ---- estrutura interna (sarrafo) — portas + painel ----
metros_sarrafo_portas = sum(2*(h+w) * 1.3 for _, h, w, _ in PORTAS)
metros_sarrafo_painel = perim_painel * 1.2
metros_sarrafo = metros_sarrafo_portas + metros_sarrafo_painel

print(f"\n{'='*72}\nCUSTO DE MATERIAL (compra)\n{'='*72}")
custo_chapas = n_chapas_real * PRECO_CHAPA_ULTRA15
custo_fita = fita_total * PRECO_FITA_M
custo_dobr = n_dobradicas * PRECO_DOBR_IN600
custo_fechadura = n_fechaduras * PRECO_FECHO_ROLETE
custo_perfil = metros_alum * PRECO_PERFIL_ALUM_M
custo_sarrafo = metros_sarrafo * PRECO_SARRAFO_M

print(f"MDF Ultra amadeirado fosco 15mm .. {n_chapas_real} chapas x R$ {PRECO_CHAPA_ULTRA15:.0f} = R$ {custo_chapas:,.2f}")
print(f"Fita de borda .................... {fita_total:.1f} m x R$ {PRECO_FITA_M:.2f} = R$ {custo_fita:,.2f}")
print(f"Dobradiças Häfele IN600 ........... {n_dobradicas} un x R$ {PRECO_DOBR_IN600:.2f} = R$ {custo_dobr:,.2f}")
print(f"Fecho rolete ...................... {n_fechaduras} un x R$ {PRECO_FECHO_ROLETE:.0f} = R$ {custo_fechadura:,.2f}  [estimativa mercado]")
print(f"Perfil alumínio base .............. {metros_alum:.1f} m x R$ {PRECO_PERFIL_ALUM_M:.0f} = R$ {custo_perfil:,.2f}")
print(f"Estrutura interna (sarrafo) ....... {metros_sarrafo:.1f} m x R$ {PRECO_SARRAFO_M:.0f} = R$ {custo_sarrafo:,.2f}")

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
print(f"INVESTIMENTO TOTAL (2 portas + painel) = R$ {fixedR:,.2f} / {divisor:.5f} = R$ {inv_total:,.2f}")

print(f"\n--- Alocação proporcional por item (área de MDF) ---")
for nome, h, w, _ in PORTAS:
    frac = (h*w*2) / tot_area_mdf
    print(f"  {nome}: {frac*100:.1f}% -> R$ {inv_total*frac:,.2f}")
frac_painel = area_painel / tot_area_mdf
print(f"  Painel de complemento ({LARG_PAINEL*100:.0f}cm): {frac_painel*100:.1f}% -> R$ {inv_total*frac_painel:,.2f}")

print(f"\nMC verificada = {MC*100:.1f}% | RT = 0% | Sem desconto.")
