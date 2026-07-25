# -*- coding: utf-8 -*-
"""
Levantamento de material — Apartamento CJ (Belo Horizonte) — B+G Estúdio
Projeto: CL_ENTREGA_FINAL_MARCENARIA (13 pranchas)

ESCOPO ORÇADO (decisões do Jonathan):
  A. Móvel entrada .......... 238x40x45, suspenso, lâmina louro freijó
  B. Marcenaria varanda ..... superior 140x66x32 + inferior 95,5x69x61, RIPADO
                              lâmina natural freijó  ⚠️ PONTO CRÍTICO
  C. Salas TV e jantar ...... 636x232, laca fosca N048/X148 — OPÇÃO "MÓVEL NOVO"
                              (o projeto oferece re-laquear OU fazer novo)
FORA DO ESCOPO: espelho · manutenção/relaqueamento de laca (exige avaliação in
loco) · serralheria de vinho (serralheiro) · futton estofado · granito · vidros
(terceiro coordenado).
FERRAGENS: Hettich.
"""

CH_A, CH_L = 2.75, 1.85          # chapa 2750x1850
CH_AREA = CH_A * CH_L            # 5,0875 m²

# ---------------------------------------------------------------- materiais
# Preços = custo de compra. chapas.md é a fonte da base; itens fora do catálogo
# (lâmina natural, laca) entram como ESTIMATIVA DE MERCADO — sinalizados.
P = {
    'LAM15':  950.0,   # MDF 15mm revestido LÂMINA NATURAL louro freijó   [ESTIMATIVA]
    'LAM6':   620.0,   # MDF 6mm lâmina natural (fundos aparentes)        [ESTIMATIVA]
    'FRJ15':  500.0,   # MDF 15mm Freijó Puro (melamínico) — interno
    'FRJ6':   300.0,   # MDF 6mm Freijó — fundos
    'CRU15':   82.0,   # MDF cru 15mm (recebe laca)                        chapas.md
    'CRU18':   95.0,   # MDF cru 18mm (prateleiras/estrutura laca)         chapas.md
    'CRU6':    62.0,   # MDF cru 6mm (fundos laca)                         chapas.md
}
FITA_LAM_M   = 12.0   # fita/bordo lâmina natural (R$/m)                  [ESTIMATIVA]
FITA_FRJ_M   = 3.0    # fita melamínico cor (R$/m)
FILETAGEM_M  = 2.5    # aplicação/filetagem (R$/m)
LACA_M2      = 300.0  # laca fosca PU 2 faces (R$/m² de superfície)       [ESTIMATIVA]
LAMINA_M2    = 190.0  # lâmina natural aplicada em ripa (R$/m² extra)     [ESTIMATIVA]

# Hettich (referencias/ferragens.md)
P_SENSYS     = 17.80  # dobradiça Sensys (premium, garantia vitalícia)
P_QUADRO_V6  = 83.00  # corrediça oculta Quadro V6 500mm (par)
P_ACTRO      = 245.00 # corrediça Actro 5D (par) — módulos > 600mm
P_PUX_CAVA_M = 45.0   # usinagem puxador cava 45° (R$/m)                  [ESTIMATIVA]

pecas = []   # (movel, desc, material, comprimento_cm, largura_cm, qtd)
def add(mv, desc, mat, c, l, q=1):
    pecas.append((mv, desc, mat, c, l, q))

# =====================================================================
# A. MÓVEL ENTRADA — 238 x 40(h) x 45(p), suspenso, recuo inferior 2cm
#    2 gavetões (sapatos) + 2 portas de abrir · puxador cava 45° superior
#    interior lâmina/MDF freijó com prateleira
# =====================================================================
A = 'A. Móvel entrada'
MOD = 59.5                       # 4 módulos de 59,5 = 238
add(A, 'Tampo', 'LAM15', 238, 45)
add(A, 'Base (aparente — suspenso)', 'LAM15', 238, 45)
add(A, 'Laterais externas', 'LAM15', 40, 45, 2)
add(A, 'Divisórias internas', 'FRJ15', 40, 45, 3)
add(A, 'Fundo (estrutural — suspenso)', 'FRJ15', 238, 40)
add(A, 'Prateleiras (módulos de porta)', 'FRJ15', 58, 42, 2)
add(A, 'Frentes gavetão', 'LAM15', 59, 39, 2)
add(A, 'Frentes porta de abrir', 'LAM15', 59, 39, 2)
# caixas dos 2 gavetões
add(A, 'Gavetão — laterais', 'FRJ15', 42, 28, 4)
add(A, 'Gavetão — frente/costas', 'FRJ15', 56, 28, 4)
add(A, 'Gavetão — fundo', 'FRJ6', 56, 42, 2)

# =====================================================================
# B. MARCENARIA VARANDA / GOURMET  ⚠️ RIPADO EM LÂMINA NATURAL FREIJÓ
#    Superior 140 x 66 x 32 — 3 portas de abrir, prateleira interna
#    Inferior  95,5 x 69 x 61 — 2 portas de abrir, prateleira
#    + vão de 44cm para cervejeira · bancada/frontão em granito (marmoraria)
# =====================================================================
B = 'B. Varanda/gourmet'
# --- superior
add(B, 'Sup — laterais', 'LAM15', 66, 32, 2)
add(B, 'Sup — tampo/base', 'LAM15', 137, 32, 2)
add(B, 'Sup — divisórias', 'FRJ15', 66, 32, 2)
add(B, 'Sup — prateleiras', 'FRJ15', 45, 30, 3)
add(B, 'Sup — fundo', 'FRJ6', 140, 66)
add(B, 'Sup — base das portas ripadas', 'LAM15', 65, 45.7, 3)
# --- inferior
add(B, 'Inf — laterais', 'LAM15', 69, 61, 2)
add(B, 'Inf — base', 'LAM15', 93, 61)
add(B, 'Inf — travessas de apoio (bancada granito)', 'FRJ15', 93, 10, 2)
add(B, 'Inf — divisória', 'FRJ15', 69, 61)
add(B, 'Inf — prateleiras', 'FRJ15', 45, 58, 2)
add(B, 'Inf — fundo', 'FRJ6', 95.5, 69)
add(B, 'Inf — base das portas ripadas', 'LAM15', 68, 46, 2)

# --- RIPADO (o gargalo): ripa 3cm + espaçamento 1,5cm -> passo 4,5cm
RIPA_L, PASSO = 3.0, 4.5
ripas = []   # (qtd, comprimento_cm)
n_sup = int(45.7 // PASSO)      # ripas por porta superior
n_inf = int(46.0 // PASSO)      # ripas por porta inferior
ripas.append((3 * n_sup, 65.0))
ripas.append((2 * n_inf, 68.0))
n_ripas   = sum(q for q, _ in ripas)
ml_ripas  = sum(q * c / 100 for q, c in ripas)
# fita das ripas — Tipo 1 (ref. laminacao-e-construcao.md): 2 x (altura + largura)
fita_ripas = sum(q * 2 * (c/100 + RIPA_L/100) for q, c in ripas)
area_ripado = sum(q * (c/100) * (RIPA_L/100) for q, c in ripas)

# =====================================================================
# C. SALAS TV E JANTAR — 636 x 232 x 47 — LACA FOSCA (opção "móvel novo")
#    C1 painel TV + armários altos (361) · C2 cristaleira 138,5 (4 portas
#    vidro) · C3 nichos + base 136,5 · prateleira acima TV em laca e 3cm
# =====================================================================
C = 'C. Salas TV e jantar'
# --- C1 painel TV + armários altos: 361 de largura
add(C, 'C1 — laterais/divisórias verticais', 'CRU15', 232, 47, 4)
add(C, 'C1 — tampo/base', 'CRU15', 178, 47, 4)
add(C, 'C1 — fundo', 'CRU6', 178, 232, 2)
add(C, 'C1 — painel de TV (fundo aparente)', 'CRU15', 175, 120)
add(C, 'C1 — prateleira acima TV (laca 3cm = 2x15mm colados)', 'CRU15', 175, 30, 2)
add(C, 'C1 — portas altas de abrir', 'CRU15', 200, 92, 2)
add(C, 'C1 — prateleiras internas', 'CRU18', 90, 45, 6)
add(C, 'C1 — gavetas inferiores: frentes', 'CRU15', 86, 22, 2)
add(C, 'C1 — gavetas: laterais', 'CRU15', 45, 20, 4)
add(C, 'C1 — gavetas: frente/costas', 'CRU15', 83, 20, 4)
add(C, 'C1 — gavetas: fundo', 'CRU6', 83, 45, 2)
# --- C2 cristaleira 138,5 x 141 x 32 — 4 portas de abrir c/ vidro incolor
add(C, 'C2 — laterais', 'CRU15', 141, 32, 2)
add(C, 'C2 — divisória central', 'CRU15', 141, 32)
add(C, 'C2 — tampo/base', 'CRU15', 137, 32, 2)
add(C, 'C2 — fundo', 'CRU6', 137, 141)
add(C, 'C2 — prateleiras internas (5 por coluna)', 'CRU18', 66, 30, 10)
add(C, 'C2 — caixilhos das portas de vidro', 'CRU15', 141, 34, 4)   # perfil/quadro
# --- C3 nichos + base 136,5
add(C, 'C3 — laterais', 'CRU15', 232, 47, 2)
add(C, 'C3 — tampo/base', 'CRU15', 133, 47, 2)
add(C, 'C3 — fundo', 'CRU6', 133, 232)
add(C, 'C3 — divisória dos nichos', 'CRU15', 45, 47)
add(C, 'C3 — prateleira dos nichos', 'CRU15', 133, 47)
add(C, 'C3 — bancada/tampo intermediário', 'CRU18', 133, 47)
add(C, 'C3 — portas da base', 'CRU15', 91, 66, 2)
add(C, 'C3 — prateleiras internas', 'CRU18', 64, 45, 2)

# =====================================================================
# NESTING — chapa 275 x 185. Estratégia: agrupar por material, ordenar por
# maior dimensão, empacotar em faixas (guillotine simplificado).
# =====================================================================
def nest(items):
    """items: lista de (c, l). Retorna nº de chapas por empacotamento em faixas."""
    pcs = []
    for c, l in items:
        a, b = max(c, l), min(c, l)
        if a > 275 or b > 185:
            # peça excede a chapa -> divide em 2 (emenda), sinalizado no relatório
            pcs.append((a/2, b)); pcs.append((a/2, b))
        else:
            pcs.append((a, b))
    pcs.sort(key=lambda p: -p[0])
    chapas = []
    for a, b in pcs:
        posto = False
        for ch in chapas:
            for faixa in ch:
                # faixa = [altura_faixa, largura_usada]
                if b <= faixa[0] + 1e-9 and faixa[1] + a <= 275 + 1e-9:
                    faixa[1] += a; posto = True; break
            if posto: break
            usado = sum(f[0] for f in ch)
            if usado + b <= 185 + 1e-9:
                ch.append([b, a]); posto = True; break
        if not posto:
            chapas.append([[b, a]])
    return len(chapas)

from collections import defaultdict
por_mat = defaultdict(list)
for mv, desc, mat, c, l, q in pecas:
    for _ in range(q):
        por_mat[mat].append((c, l))

print("=" * 78)
print("LEVANTAMENTO DE MATERIAL — APARTAMENTO CJ (B+G Estúdio)")
print("Ferragens Hettich · MC/RT a definir · plano de corte por nesting real")
print("=" * 78)

print("\n" + "-" * 78)
print("1) PEÇAS POR MÓVEL")
print("-" * 78)
mv_atual = None
for mv, desc, mat, c, l, q in pecas:
    if mv != mv_atual:
        print(f"\n### {mv}")
        mv_atual = mv
    print(f"   {q:>2}x  {desc:<48} {c:>6.1f} x {l:>5.1f} cm   [{mat}]")

print("\n" + "-" * 78)
print("2) PLANO DE CORTE — chapas por material (nesting real 275x185)")
print("-" * 78)
NOME = {
    'LAM15': 'MDF 15mm LÂMINA NATURAL louro freijó',
    'LAM6':  'MDF 6mm lâmina natural',
    'FRJ15': 'MDF 15mm Freijó Puro (interno)',
    'FRJ6':  'MDF 6mm Freijó (fundos)',
    'CRU15': 'MDF cru 15mm (p/ laca)',
    'CRU18': 'MDF cru 18mm (prateleiras/laca)',
    'CRU6':  'MDF cru 6mm (fundos laca)',
}
total_chapas = 0
custo_chapas = 0.0
chapas_por_mat = {}
for mat in ['LAM15', 'FRJ15', 'FRJ6', 'CRU15', 'CRU18', 'CRU6']:
    if mat not in por_mat: continue
    itens = por_mat[mat]
    n = nest(itens)
    area = sum(c*l for c, l in itens) / 10000
    aprov = area / (n * CH_AREA) * 100
    chapas_por_mat[mat] = n
    total_chapas += n
    custo_chapas += n * P[mat]
    print(f"{NOME[mat]:<42} {len(itens):>3} peças · {area:>6.2f} m² · "
          f"**{n:>2} chapas** (aprov. {aprov:.0f}%) · R$ {n*P[mat]:>8,.2f}")

# ripas: material adicional em lâmina natural
ch_ripas = 1
total_chapas += ch_ripas
custo_chapas += ch_ripas * P['LAM15']
print(f"{'+ ripas do ripado (lâmina natural 15mm)':<42} {n_ripas:>3} ripas · "
      f"{ml_ripas:>6.2f} m · **{ch_ripas:>2} chapa**  · R$ {ch_ripas*P['LAM15']:>8,.2f}")

print(f"\nTOTAL DE CHAPAS: {total_chapas}   |   custo de chapas: R$ {custo_chapas:,.2f}")

# =====================================================================
# 3) FITA DE BORDA / FILETAGEM
# =====================================================================
print("\n" + "-" * 78)
print("3) FITA DE BORDA E FILETAGEM")
print("-" * 78)
def perim_mat(mats):
    t = 0.0
    for mv, desc, mat, c, l, q in pecas:
        if mat in mats:
            t += q * 2 * (c + l) / 100
    return t
fita_lam = perim_mat(['LAM15']) * 0.55        # só bordas aparentes
fita_frj = perim_mat(['FRJ15', 'FRJ6']) * 0.5
fita_cru = perim_mat(['CRU15', 'CRU18']) * 0.5   # laca: bordas seladas, não fitadas
print(f"Lâmina natural (bordas aparentes) ..... {fita_lam:>7.1f} m x R$ {FITA_LAM_M:.2f} = R$ {fita_lam*FITA_LAM_M:>9,.2f}")
print(f"Ripas do ripado (2x(alt+larg)/ripa) ... {fita_ripas:>7.1f} m x R$ {FITA_LAM_M:.2f} = R$ {fita_ripas*FITA_LAM_M:>9,.2f}  <-- GARGALO")
print(f"Freijó melamínico (interno) ........... {fita_frj:>7.1f} m x R$ {FITA_FRJ_M:.2f} = R$ {fita_frj*FITA_FRJ_M:>9,.2f}")
fita_total_m = fita_lam + fita_ripas + fita_frj
custo_fita = fita_lam*FITA_LAM_M + fita_ripas*FITA_LAM_M + fita_frj*FITA_FRJ_M
custo_filet = fita_total_m * FILETAGEM_M
print(f"Filetagem (aplicação) ................. {fita_total_m:>7.1f} m x R$ {FILETAGEM_M:.2f} = R$ {custo_filet:>9,.2f}")
print(f"(peças de laca não levam fita — bordas seladas e lacadas: {fita_cru:.0f} m de borda a selar)")

# =====================================================================
# 4) LACA E LÂMINA — acabamentos por m²
# =====================================================================
print("\n" + "-" * 78)
print("4) ACABAMENTOS POR m²")
print("-" * 78)
area_laca = sum(c*l*q for mv, d, mat, c, l, q in pecas if mat.startswith('CRU')) / 10000
area_laca_2f = area_laca * 1.6      # faces aparentes + internas parciais
custo_laca = area_laca_2f * LACA_M2
custo_lamina_ripa = area_ripado * 3 * LAMINA_M2   # face + 2 laterais da ripa
print(f"Laca fosca N048/X148 (Sayerlack) ...... {area_laca_2f:>7.1f} m² x R$ {LACA_M2:.0f} = R$ {custo_laca:>9,.2f}")
print(f"Lâmina natural nas ripas (3 faces) .... {area_ripado*3:>7.1f} m² x R$ {LAMINA_M2:.0f} = R$ {custo_lamina_ripa:>9,.2f}")

# =====================================================================
# 5) FERRAGENS HETTICH E INSUMOS
# =====================================================================
print("\n" + "-" * 78)
print("5) FERRAGENS HETTICH E INSUMOS")
print("-" * 78)
# dobradiças por altura (regra ferragens.md)
def n_dobr(alt_cm):
    a = alt_cm * 10
    return 2 if a <= 900 else 3 if a <= 1600 else 4 if a <= 2000 else 5
portas = [
    ('A  portas entrada (39cm)',        2, n_dobr(39)),
    ('B  portas sup. varanda (65cm)',   3, n_dobr(65)),
    ('B  portas inf. varanda (68cm)',   2, n_dobr(68)),
    ('C1 portas altas (200cm)',         2, n_dobr(200)),
    ('C2 portas cristaleira (141cm)',   4, n_dobr(141)),
    ('C3 portas da base (91cm)',        2, n_dobr(91)),
]
tot_dobr = 0
for nome, qtd, nd in portas:
    tot_dobr += qtd * nd
    print(f"   {nome:<34} {qtd} portas x {nd} dobr. = {qtd*nd:>2}")
print(f"   {'>> Dobradiça Hettich Sensys (vitalícia)':<34} {tot_dobr:>2} un x R$ {P_SENSYS:.2f} = R$ {tot_dobr*P_SENSYS:>8,.2f}")

n_gav = 2 + 2      # 2 gavetões entrada + 2 gavetas C1
custo_corr = 2*P_ACTRO + 2*P_QUADRO_V6    # gavetões (larg. 59) Actro 5D; gavetas C1 Quadro V6
print(f"   {'Corrediça Hettich Actro 5D (gavetão)':<34} {2:>2} pares x R$ {P_ACTRO:.2f} = R$ {2*P_ACTRO:>8,.2f}")
print(f"   {'Corrediça Hettich Quadro V6':<34} {2:>2} pares x R$ {P_QUADRO_V6:.2f} = R$ {2*P_QUADRO_V6:>8,.2f}")

# puxador cava 45° (usinagem, metro linear)
ml_cava = (238*2 + 140 + 95.5) / 100      # entrada (2 faixas) + varanda sup + inf
custo_cava = ml_cava * P_PUX_CAVA_M
print(f"   {'Puxador cava 45° (usinagem)':<34} {ml_cava:>5.1f} m x R$ {P_PUX_CAVA_M:.0f} = R$ {custo_cava:>8,.2f}")

# puxador bolinha dourado fosco — cristaleira (projeto especifica)
n_bolinha = 4
P_BOLINHA = 38.0
print(f"   {'Puxador bolinha dourado fosco':<34} {n_bolinha:>2} un x R$ {P_BOLINHA:.2f} = R$ {n_bolinha*P_BOLINHA:>8,.2f}")

# vidro incolor cristaleira — terceiro
area_vidro = 4 * (1.41 * 0.33)
P_VIDRO_M2 = 320.0
print(f"   {'Vidro incolor cristaleira [terceiro]':<34} {area_vidro:>5.2f} m² x R$ {P_VIDRO_M2:.0f} = R$ {area_vidro*P_VIDRO_M2:>8,.2f}")

custo_ferragens = (tot_dobr*P_SENSYS + custo_corr + custo_cava
                   + n_bolinha*P_BOLINHA + area_vidro*P_VIDRO_M2)

# =====================================================================
# 6) FECHAMENTO
# =====================================================================
print("\n" + "=" * 78)
print("6) RESUMO DO CUSTO DE MATERIAL")
print("=" * 78)
linhas = [
    ('Chapas (todas as linhas)', custo_chapas),
    ('Fita de borda / lâmina de bordo', custo_fita),
    ('Filetagem (aplicação)', custo_filet),
    ('Laca fosca (Sayerlack N048/X148)', custo_laca),
    ('Lâmina natural aplicada nas ripas', custo_lamina_ripa),
    ('Ferragens Hettich + puxadores + vidro', custo_ferragens),
]
mat_total = sum(v for _, v in linhas)
for k, v in linhas:
    print(f"   {k:<44} R$ {v:>10,.2f}")
print(f"   {'-'*44} {'-'*14}")
print(f"   {'SUBTOTAL MATERIAL':<44} R$ {mat_total:>10,.2f}")

print(f"""
{'='*78}
7) PONTOS DE ATENÇÃO
{'='*78}
 ⚠️  RIPADO DA VARANDA EM LÂMINA NATURAL — o item mais crítico do projeto.
     {n_ripas} ripas ({ml_ripas:.1f} m lineares) exigem {fita_ripas:.0f} m de bordo em lâmina,
     acabamento em 3 faces por ripa. É o gargalo de custo e de prazo.
 ⚠️  Laca: {area_laca_2f:.1f} m² de superfície — driver de custo do móvel das salas.
 ⚠️  Peças acima de 275cm (móvel de 636) exigem EMENDA — prever junta alinhada.
 •   Fora do escopo: espelho · relaqueamento (avaliação in loco) · serralheria
     de vinho · futton estofado · granito/frontão · ponto elétrico do nicho.
""")
