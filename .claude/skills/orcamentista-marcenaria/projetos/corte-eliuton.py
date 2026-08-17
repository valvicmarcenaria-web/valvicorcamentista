# -*- coding: utf-8 -*-
"""ELIUTON · Residência Brisas da Pampulha — LEVANTAMENTO E PREÇO.

Projeto executivo Arq. Luciana Beatriz Simplício · Núcleo SC Arquitetura.
DUAS séries de pranchas, lidas vetorialmente em 17/08/2026:
  · folhas 01–08 de 08  — COZINHA e ÁREA GOURMET      (12/12/25)
  · folhas 01–10 de 10  — ÁREA DE SERVIÇO e BANHEIROS (17/12/25)
Escala 1:25 aferida no próprio desenho: a porta 80×210 mediu 80,0 × 210,0.
Falta a folha 02/10 (detalhes da área de serviço) — não estava na pasta.

⚠ OS NOMES DOS ARQUIVOS NÃO CORRESPONDEM ÀS FOLHAS. `PR 05_COZINHA` é a folha
  08/08 (gourmet) e `PR 05_COZINHA (1)` é a 05/08 (ilha). O Jonathan já tinha
  avisado que não eram duplicatas — estava certo, e por isso mesmo o carimbo é
  a única referência confiável.

[Jonathan 13/08/2026] TRÊS CENÁRIOS DE FERRAGEM, cada um com a sua MC:
     telescópica 32% · Hardt 37% · Hettich 42%   ⟵ BLUM FORA
     …exceto as BÁSCULAS dos cenários 2 e 3, que são Blum HK-xs a R$ 250.
   E: **toda parte com RIPADO sai a MC 40%**, em qualquer cenário.

O ripado tem MC própria, então o preço NÃO é um divisor único sobre o custo
total: é a soma de duas parcelas — a de ripado no seu divisor, e o resto no
divisor do cenário. É por isso que `preco()` separa `custo_ripado` de
`custo_resto`.
"""
from collections import defaultdict

CH_C, CH_L = 275.0, 185.0
CH_AREA = 2.75 * 1.85                       # 5,0875 m²

# ── motor comercial ────────────────────────────────────────────────────────
A_, LIQF_, B_ = 0.162, 0.88, 0.043          # conjunto SEM RT
BASE = 1 - A_ - LIQF_*B_                    # 0,80016
RT_PCT = 0.10                               # se houver RT: subtrair LIQF_*RT_PCT

MC_RIPADO = 0.40                            # [Jonathan] vale nos três cenários

HK_XS = 250.0                               # Blum HK-xs [Jonathan 13/08]
CENARIOS = [
    ('1 · Telescópica', 'Padrão · telescópica · pistão simples',    0.32,
     dict(dobr=6.0,  corr=40.0,  art=20.0),  '2 anos'),
    ('2 · Hardt',       'Hardt · oculta Hardt · Blum HK-xs',        0.37,
     dict(dobr=8.0,  corr=70.0,  art=HK_XS), '5 anos'),
    ('3 · Hettich',     'Novisys · oculta Quadro · Blum HK-xs',     0.42,
     dict(dobr=10.0, corr=120.0, art=HK_XS), '10 anos'),
]

def div(mc, rt=False):
    return BASE - mc - (LIQF_*RT_PCT if rt else 0.0)

def preco(custo_resto, custo_ripado, mc, rt=False):
    """Duas parcelas: o ripado no divisor dele, o resto no divisor do cenário."""
    return custo_resto/div(mc, rt) + custo_ripado/div(MC_RIPADO, rt)

def mc_conferida(preco_total, custo_total):
    return BASE - custo_total/preco_total

# ── nesting da casa (dois empacotadores × quatro ordens) ───────────────────
def _pack_faixa(pcs):
    chapas = 0; y = x = faixa = 0.0
    for c, l in pcs:
        if c > CH_C and l <= CH_C: c, l = l, c
        if c > CH_C or l > CH_L: chapas += 1; continue
        if x + c > CH_C: y += faixa; x = 0.0; faixa = 0.0
        if y + l > CH_L: chapas += 1; y = x = faixa = 0.0
        x += c; faixa = max(faixa, l)
    return chapas + 1

def _pack_bf(pcs):
    ch = []                    # ch[i] = [altura_usada, [[alt_faixa, sobra_larg], ...]]
    for c, l in pcs:
        if c > CH_C and l <= CH_C: c, l = l, c
        if c > CH_C or l > CH_L: ch.append([CH_L, []]); continue
        best = None
        for s in ch:
            for fx in s[1]:
                if fx[0] >= l and fx[1] >= c and (best is None or fx[1] < best[1]):
                    best = fx
        if best is not None: best[1] -= c; continue
        for s in ch:
            if s[0] + l <= CH_L:
                s[0] += l; s[1].append([l, CH_C - c]); break
        else:
            ch.append([l, [[l, CH_C - c]]])
    return len(ch)

def nest(items):
    if not items: return 0
    base = [(max(c, l), min(c, l)) for c, l in items]
    ordens = [lambda p: -p[1], lambda p: (-p[1], -p[0]),
              lambda p: -p[0], lambda p: -p[0]*p[1]]
    chapas = min(pk(sorted(base, key=k))
                 for pk in (_pack_faixa, _pack_bf) for k in ordens)
    area = sum(c*l for c, l in items)/10000
    return max(chapas, -(-int(area/(CH_AREA*0.80)*1000)//1000) or 1)

# ═══════════════════════════════════════════════════════════════════════════
# PREÇOS DE COMPRA — dados/materiais.json + referencias/validacao-orcamento.md
# ═══════════════════════════════════════════════════════════════════════════
# As quatro cores do projeto são Arauco: Nogueira Persa e Jequitibá (madeirados),
# Sálvia e Beige (lisos). A base da casa não tem preço nominal de linha Arauco
# madeirada — `corte-lm.py` deixou a marca "ver FLAG premium" e nunca foi
# fechada. Aqui rodo em COR (500/600/300) e mostro a sensibilidade em ESPECIAL
# (950/1200/800) no fim. ⚠ CONFIRMAR COM O FORNECEDOR ANTES DE FECHAR.
PRC_COR = {15: 500.0, 18: 600.0, 6: 300.0}
PRC_ESP = {15: 950.0, 18: 1200.0, 6: 800.0}
PRECO_CHAPA = PRC_COR

FITA_COR   = 3.00      # R$/m — fita de borda cor 22 mm
FILET_MAQ  = 2.50      # R$/m — aplicação na coladeira automática
DESPERD    = 1.10      # +10% de fita

# ⚠ CORREÇÃO 17/08 — a cava é por METRO, não por peça.
# `materiais.json` traz "Cava 35° usinada · peça · R$ 50" e a Honda usou
# "R$ 25/m de usinagem de cava embutida na CNC" — número que o Jonathan validou
# num job real. A CNC cobra tempo de percurso, e percurso é metro linear.
# Eu tinha usado R$ 50 × 50 frentes = R$ 2.500. Correto: ~30 m × R$ 25 = R$ 750.
CAVA_USIN  = 25.0      # R$/m linear de cava usinada  [convenção Honda 07/08]
PUX_ALCA   = 60.0      # R$/un   — puxador metálico tipo alça preto (banheiro master)
SUP_PRAT   = 1.50      # R$/un   — 4 por prateleira
# ⚠ CORREÇÃO — LED. `materiais.json` diz "LED COB (fita+perfil) R$ 150/m";
# `chapas.md` decompõe: fita branco quente R$ 28/m + perfil alumínio R$ 38/m.
# Uso a decomposta, que é a que tem origem rastreável.
LED_M      = 28.0 + 38.0
# ⚠ CORREÇÃO — ARMADILHA Nº 4 DA MINHA PRÓPRIA LISTA: "vidro e espelho a casa
# cota POR FOLHA, não por m². Nunca usar os R$ da tabela como R$/m²."
# Eu usei R$ 600/m². `chapas.md`: espelho prata colado R$ 220 · com perfil R$ 285.
ESPELHO_FL = 285.0     # R$/folha — espelho prata com perfil
VIDRO8     = 250.0     # R$/m²   — vidro incolor temperado 8 mm
SERRALH    = 300.0     # R$/serviço
# ⚠ CORREÇÃO — SS150 é sistema de ROUPEIRO (folha pesada, 65 cm de profundidade).
# Porta de espelho num armário de banheiro de 15 cm NÃO é SS150: é RO65 Rometal.
RO65_PORTA = 60.0      # conjunto por porta
TRILHO_RO65 = 60.0     # 2 m
PIVO       = 120.0     # sistema de porta pivotante
RO82_TOP   = 400.0     # deslizante embutido amortecido (porta de correr ripada)
TABUA      = 480.0     # tábua de passar embutida dobrável

# ⚠ SEM PREÇO NA BASE — entram como estimativa, marcadas no relatório:
VARAL_RETR = 350.0     # un — varal retrátil embutido (2 na área de serviço)
SUP_DOURAD = 180.0     # un — suporte metálico dourado de prateleira (banheiro 04)

# ── ripado: geometria adotada ──────────────────────────────────────────────
# Tipo 2 (referencias/laminacao-e-construcao.md): painel em MDF 18 mm, régua
# fitada em UMA face, topo colado no painel de fundo.
# ⚠ O passo NÃO é legível na prancha (a 1:25 uma régua de 4 cm dá 1,6 mm no
#   papel). PREMISSA: régua 4,0 cm + espaçamento 1,5 cm ⇒ passo 5,5 cm.
RIPA_L, RIPA_PASSO = 4.0, 5.5

# ═══════════════════════════════════════════════════════════════════════════
# GEOMETRIA — (material, espessura, ambiente, descrição, comp, larg, qtd, ripado)
# ═══════════════════════════════════════════════════════════════════════════
# Materiais: NP Nogueira Persa · SA Sálvia · JQ Jequitibá · BG Beige
# Regra de espessura da casa: 15 caixaria · 18 frentes e prateleiras · 6 fundos.
# Os fundos vão NA COR porque as perspectivas de armário aberto mostram o
# interior todo na cor. Alavanca de custo medida no fim (fundo branco).

P = []            # peças
def add(mat, esp, amb, desc, c, l, q=1, rip=False):
    P.append((mat, esp, amb, desc, c, l, q, rip))

def caixa(mat, amb, nome, L, H, Pf, nvert=0, nprat=0, fundo=True,
          tampo=True, base=True):
    """Caixaria de um módulo: laterais/divisórias, tampo, base, prateleiras, fundo."""
    nlat = 2 + nvert
    add(mat, 15, amb, f'{nome} · lateral/divisória', Pf, H, nlat)
    Lh = L - 1.5*nlat
    if tampo: add(mat, 15, amb, f'{nome} · tampo', Lh, Pf)
    if base:  add(mat, 15, amb, f'{nome} · base',  Lh, Pf)
    if nprat:
        Lv = Lh/(nvert+1)
        add(mat, 18, amb, f'{nome} · prateleira', Lv, Pf-2, nprat)
    if fundo: add(mat, 6, amb, f'{nome} · fundo', L, H)

def gaveta(mat, amb, nome, L, Pf, alt, q=1):
    """Caixa de gaveta — 6 peças (referencias/laminacao-e-construcao.md)."""
    add(mat, 15, amb, f'{nome} · gaveta lateral',       Pf-10, alt, 2*q)
    add(mat, 15, amb, f'{nome} · gaveta frente/costas', L-6,   alt, 2*q)
    add(mat, 6,  amb, f'{nome} · gaveta fundo',         L-6,   Pf-10, q)

def ripado(mat, amb, nome, L, H, base_esp=15, nh=1, nv=1):
    """Painel ripado tipo 2, quebrado em nh × nv peças para caber na chapa.

    ⚠ A chapa é 275 × 185. Uma ripa de 288 cm NÃO CABE em nenhum sentido —
      tem de sair emendada. Aqui a emenda é modelada: `nv` trechos na altura.
      Na obra a emenda cai na horizontal do acabamento sobre a porta de correr.
    """
    n = int(L/RIPA_PASSO)
    add(mat, base_esp, amb, f'{nome} · painel de fundo ({nh}×{nv} peças)',
        L/nh, H/nv, nh*nv, True)
    add(mat, 18, amb, f'{nome} · régua {RIPA_L:.0f} × {H/nv:.0f} cm',
        RIPA_L, H/nv, n*nv, True)
    return n

# contadores de ferragem: (dobradiças, gavetas, básculas)
FER = defaultdict(lambda: [0, 0, 0])
def fer(amb, dobr=0, gav=0, basc=0):
    FER[amb][0] += dobr; FER[amb][1] += gav; FER[amb][2] += basc

FITA = []         # (ambiente, descrição, metros)
def fita(amb, desc, m): FITA.append((amb, desc, m))

TERC = []         # (ambiente, descrição, valor, estimado?)
def terc(amb, desc, v, est=False): TERC.append((amb, desc, v, est))

CAVA_M = defaultdict(float)       # metros lineares de cava usinada
def cava(amb, m): CAVA_M[amb] += m

# ───────────────────────────────────────────────────────────────────────────
# 1 · COZINHA — CONJUNTO COMPLETO EM UM ÚNICO ITEM  [Jonathan 17/08]
#     folhas 02, 03, 04 e 05 de 08 · Nogueira Persa + Sálvia
#     · torre quente + nicho geladeira 187 × 70 × 290   (Nogueira Persa)
#     · acabamento superior — faixa de 15 sob o forro    (Nogueira Persa)
#     · bancada 01 · armário inferior 355 × 70 × 88      (Sálvia)
#     · aéreo 351 × 40 × 96 · 5 portas                   (Sálvia)
#     · ilha 226 × 70 × 88                               (Sálvia)
#     O painel ripado do estar/jantar fica FORA deste item: é outra parede e
#     tem MC própria de 40%, então precisa de linha separada no motor.
# ───────────────────────────────────────────────────────────────────────────
A = 'Cozinha (conjunto completo)'

# ── torre quente + nicho da geladeira ──────────────────────────────────────
# ⚠ CORREÇÃO 17/08 — NICHO DE ELETRODOMÉSTICO NÃO LEVA FUNDO DE MDF.
#   Geladeira, forno e micro-ondas precisam de ventilação, tomada e folga de
#   dissipação; o fundo é a alvenaria. Eu tinha lançado 2,81 m² de fundo atrás
#   da geladeira e 1,93 m² atrás da torre de cocção — 4,74 m² que não existem.
# ⚠ CORREÇÃO 17/08 — o tampo sobre o nicho da geladeira JÁ É a base do armário
#   basculante de cima. Eu tinha lançado as duas peças: −0,72 m².
add('NP', 18, A, 'torre · lateral vazada (batente da porta do gourmet)', 70, 275)
add('NP', 15, A, 'torre · divisória geladeira/torre', 70, 275)
add('NP', 15, A, 'torre · lateral direita (encosta na bancada)', 70, 275)
add('NP', 15, A, 'torre · horizontal entre geladeira e basculante', 103, 70)
add('NP', 15, A, 'torre · tampo do armário basculante', 103, 70)
add('NP', 15, A, 'torre · horizontais da coluna (tampo + 4 div + base)', 67, 70, 6)
add('NP', 18, A, 'torre · báscula sobre a geladeira 103 × 58', 103, 58)
add('NP', 18, A, 'torre · báscula superior da coluna 70 × 58', 70, 58)
add('NP', 18, A, 'torre · báscula do 2º nicho 70 × 39', 70, 39)
add('NP', 18, A, 'torre · frente do gavetão 70 × 58', 70, 58)
add('NP', 18, A, 'torre · prateleira do armário basculante', 100, 68)
gaveta('NP', A, 'torre · gavetão', 70, 70, 50)
fer(A, dobr=6, gav=1, basc=3)
cava(A, 1.03 + 0.70 + 0.70 + 0.70)
fita(A, 'torre · perímetro das 3 básculas + gavetão',
     2*(1.03+0.58) + 2*(0.70+0.58) + 2*(0.70+0.39) + 2*(0.70+0.58))
fita(A, 'torre · lateral vazada + frentes de caixaria',
     2*(0.70+2.75) + 6*0.67 + 2*1.03)

# ── acabamento superior — faixa de 15 sob o forro, ao longo dos 541,5 ──────
add('NP', 18, A, 'acabamento superior sob o forro (541,5 em 2 peças)', 271, 15, 2)
fita(A, 'acabamento superior · borda inferior aparente', 5.42)

# ── bancada 01 · armário inferior · Sálvia ────────────────────────────────
#    355 × 70 × 88 (corpo 78 + rodapé 10) · a bancada é de MÁRMORE
#    64 gaveteiro | 104 (2 portas 50) | 23 pano de prato | 64 nicho LL | 104
add('SA', 15, A, 'bancada 01 · verticais (2 externas + 5 divisórias)', 70, 78, 7)
add('SA', 15, A, 'bancada 01 · base (349 em 2 peças)', 175, 70, 2)
add('SA', 15, A, 'bancada 01 · travessa superior', 175, 10, 2)
add('SA', 6,  A, 'bancada 01 · fundo (355 em 2 peças)', 178, 78, 2)
add('SA', 18, A, 'bancada 01 · frente de gaveta 64 × 15', 64, 15, 3)
add('SA', 18, A, 'bancada 01 · frente do gavetão 64 × 29', 64, 29)
add('SA', 18, A, 'bancada 01 · porta 50 × 74', 50, 74, 4)
add('SA', 18, A, 'bancada 01 · porta pano de prato 23 × 74', 23, 74)
add('SA', 18, A, 'bancada 01 · prateleira dos módulos de porta', 100, 68, 2)
add('SA', 18, A, 'bancada 01 · rodapé recuado (355 em 2 peças)', 178, 10, 2)
gaveta('SA', A, 'bancada 01 · gaveteiro', 64, 70, 13, 3)
gaveta('SA', A, 'bancada 01 · gavetão',   64, 70, 27, 1)
fer(A, dobr=10, gav=4)
cava(A, 3*0.64 + 0.64 + 4*0.50 + 0.23)
fita(A, 'bancada 01 · frentes de gaveta + gavetão',
     3*2*(0.64+0.15) + 2*(0.64+0.29))
fita(A, 'bancada 01 · portas', 4*2*(0.50+0.74) + 2*(0.23+0.74))
fita(A, 'bancada 01 · verticais + prateleiras + rodapé',
     7*0.78 + 2*1.00 + 3.55)
fita(A, 'bancada 01 · nicho da lava-louça (bordas aparentes)', 2*0.78 + 0.64)

# ── aéreo · Sálvia · 351 × 40 × 96 · portas 85 · 85 · 56 · 57 · 56 ────────
add('SA', 15, A, 'aéreo · verticais (2 externas + 4 divisórias)', 40, 96, 6)
add('SA', 15, A, 'aéreo · tampo (342 em 2 peças)', 171, 40, 2)
add('SA', 15, A, 'aéreo · base (342 em 2 peças)',  171, 40, 2)
add('SA', 18, A, 'aéreo · prateleira dos módulos de 85', 85, 38, 2)
add('SA', 18, A, 'aéreo · prateleira dos módulos de 56/57', 56, 38, 3)
add('SA', 6,  A, 'aéreo · fundo (351 em 2 peças)', 176, 96, 2)
add('SA', 18, A, 'aéreo · porta 85 × 92', 85, 92, 2)
add('SA', 18, A, 'aéreo · porta 56/57 × 92', 56, 92, 3)
fer(A, dobr=10)
cava(A, 2*0.85 + 3*0.57)
fita(A, 'aéreo · portas', 2*2*(0.85+0.92) + 3*2*(0.57+0.92))
fita(A, 'aéreo · base aparente por baixo + prateleiras',
     3.51 + 2*0.85 + 3*0.56)

# ── ilha · Sálvia · 226 × 70 × 88 · cascata em mármore (fora do escopo) ────
#    20 porta temperos | 122 (2 portas de 60) | 78 gaveteiro
add('SA', 15, A, 'ilha · verticais (2 externas + 3 divisórias)', 70, 78, 5)
add('SA', 15, A, 'ilha · base (218 em 2 peças)', 109, 70, 2)
add('SA', 15, A, 'ilha · travessa superior', 109, 10, 2)
add('SA', 18, A, 'ilha · costas aparente (vista posterior, 226 em 2)', 113, 88, 2)
add('SA', 18, A, 'ilha · porta temperos 20 × 74', 20, 74)
add('SA', 18, A, 'ilha · porta 60 × 74', 60, 74, 2)
add('SA', 18, A, 'ilha · frente de gaveta 78 × 15', 78, 15, 3)
add('SA', 18, A, 'ilha · frente do gavetão 78 × 29', 78, 29)
add('SA', 18, A, 'ilha · prateleira do módulo de 122', 120, 68)
add('SA', 18, A, 'ilha · rodapé recuado (226 em 2 peças)', 113, 10, 2)
gaveta('SA', A, 'ilha · gaveteiro', 78, 70, 13, 3)
gaveta('SA', A, 'ilha · gavetão',   78, 70, 27, 1)
fer(A, dobr=6, gav=4)
cava(A, 0.20 + 2*0.60 + 3*0.78 + 0.78)
fita(A, 'ilha · portas', 2*(0.20+0.74) + 2*2*(0.60+0.74))
fita(A, 'ilha · frentes de gaveta', 3*2*(0.78+0.15) + 2*(0.78+0.29))
fita(A, 'ilha · costas + rodapé + prateleira', 2*(2.26+0.88) + 2.26 + 1.20)
# 6 · COZINHA/JANTAR — PAINEL RIPADO                  folha 02/08 · Nogueira
#     572 × 288 = 16,47 m². Porta de correr ripada + porta pivotante ripada
#     EMBUTIDAS no painel (o ripado delas já está na área).
# ───────────────────────────────────────────────────────────────────────────
A = 'Cozinha · painel ripado'
n_reg = ripado('NP', A, 'painel do estar/jantar', 572, 288, nh=3, nv=2)
fita(A, f'réguas fitadas em 1 face — {n_reg} × 2,88 m', n_reg*2.88)
fita(A, 'acabamento superior sobre a porta de correr', 5.72)
terc(A, 'Sistema deslizante embutido amortecido (porta de correr ripada)', RO82_TOP)
terc(A, 'Sistema pivotante (porta 80 × 210 ripada)', PIVO)
cava(A, 2*0.80)

# ───────────────────────────────────────────────────────────────────────────
# 7 · GOURMET — BANCADA 02 (inferior + superior)      folhas 07 e 08/08 · Nog.
#     215 = 145 bancada + 70 cervejeira · 290 de altura
# ───────────────────────────────────────────────────────────────────────────
A = 'Gourmet · bancada 02'
# inferior 145 × 70 × 88: gaveteiro 51 + 2 portas de 47
add('NP', 15, A, 'inferior · verticais (2 ext + 1 div)', 70, 78, 3)
add('NP', 15, A, 'inferior · base', 140, 70)
add('NP', 15, A, 'inferior · travessa superior', 140, 10)
add('NP', 6,  A, 'inferior · fundo', 145, 78)
add('NP', 18, A, 'inferior · frente de gaveta 51 × 15', 51, 15, 3)
add('NP', 18, A, 'inferior · frente do gavetão 51 × 29', 51, 29)
add('NP', 18, A, 'inferior · porta 47 × 74', 47, 74, 2)
add('NP', 18, A, 'inferior · prateleira', 92, 68)
add('NP', 18, A, 'inferior · rodapé recuado', 145, 10)
gaveta('NP', A, 'inferior · gaveteiro', 51, 70, 13, 3)
gaveta('NP', A, 'inferior · gavetão',   51, 70, 27, 1)
# coluna da cervejeira 70 × 70 × 290: nicho 213 + báscula 62 + acabamento 15
# ⚠ 290 não cabe na chapa de 275 — lateral emendada no plano do tampo do nicho.
add('NP', 15, A, 'cervejeira · laterais do nicho (213)', 70, 213, 2)
add('NP', 15, A, 'cervejeira · laterais do armário superior (77)', 70, 77, 2)
add('NP', 15, A, 'cervejeira · base + divisória + tampo', 67, 70, 3)
add('NP', 6,  A, 'cervejeira · fundo do armário superior', 70, 77)
add('NP', 18, A, 'cervejeira · báscula superior 70 × 62', 70, 62)
add('NP', 18, A, 'cervejeira · acabamento 15', 70, 15)
# prateleira c/ LED por baixo + armário superior de vidro
add('NP', 18, A, 'prateleira c/ borda frontal e LED por baixo', 145, 25)
add('NP', 15, A, 'superior · laterais do caixote de vidro', 40, 77, 2)
add('NP', 15, A, 'superior · tampo e base do caixote', 142, 40, 2)
add('NP', 6,  A, 'superior · fundo', 145, 77)
fer(A, dobr=6, gav=4, basc=1)
cava(A, 3*0.51 + 0.51 + 2*0.47 + 0.70)
fita(A, 'frentes de gaveta + portas', 3*2*(0.51+0.15) + 2*(0.51+0.29)
        + 2*2*(0.47+0.74))
fita(A, 'básculas + acabamento + prateleira LED', 2*(0.70+0.62) + 0.70
        + 2*(1.45+0.25))
fita(A, 'verticais, rodapé, caixotes', 3*0.78 + 1.45 + 2*2.90 + 2*1.42)
terc(A, 'Serralheria — 2 portas basculantes c/ estrutura em metal fendi', 2*SERRALH)
terc(A, 'Vidro incolor temperado 8 mm — 2 folhas de 0,71 × 0,73', 2*0.71*0.73*VIDRO8)
terc(A, 'LED fita + perfil de alumínio sob a prateleira — 1,45 m', 1.45*LED_M)

# ───────────────────────────────────────────────────────────────────────────
# 8 · ÁREA DE SERVIÇO                                 folha 01/10 · Nogueira
#     359 larg × 55 prof × 226 (+ rodapé) — medido no vetor: 359,0 × 238,1
#     112 portas de abrir | 147 lavar+secar | 100 inferior sob bancada
# ───────────────────────────────────────────────────────────────────────────
A = 'Área de serviço'
# módulo 1 — armário alto 112 × 226 (vassouras e tábua de passar)
add('NP', 15, A, 'M1 · laterais', 55, 226, 2)
add('NP', 15, A, 'M1 · tampo e base', 109, 55, 2)
add('NP', 18, A, 'M1 · prateleiras', 107, 53, 4)
add('NP', 6,  A, 'M1 · fundo', 112, 226)
add('NP', 18, A, 'M1 · porta 56 × 224', 56, 224, 2)
# módulo 2 — 147 × 226, duas colunas de 73
add('NP', 15, A, 'M2 · laterais e divisória central', 55, 226, 3)
add('NP', 15, A, 'M2 · tampo e base', 71, 55, 4)
add('NP', 15, A, 'M2 · horizontais internas (varal/nicho/máquina/gavetão)', 71, 55, 8)
add('NP', 6,  A, 'M2 · fundo', 147, 226)
add('NP', 18, A, 'M2 · porta superior 73 × 113', 73, 113, 2)
add('NP', 18, A, 'M2 · frente do gavetão 73 × 30', 73, 30, 2)
add('NP', 18, A, 'M2 · frente da gaveta do varal 73 × 12', 73, 12, 2)
gaveta('NP', A, 'M2 · gavetão', 73, 55, 28, 2)
gaveta('NP', A, 'M2 · gaveta do varal', 73, 55, 10, 2)
# módulo 3 — inferior sob a bancada 100 × 68
add('NP', 15, A, 'M3 · laterais', 55, 68, 2)
add('NP', 15, A, 'M3 · base', 97, 55)
add('NP', 15, A, 'M3 · travessa superior (a bancada é mármore)', 97, 10)
add('NP', 6,  A, 'M3 · fundo', 100, 68)
add('NP', 18, A, 'M3 · porta 49 × 66', 49, 66, 2)
add('NP', 18, A, 'M3 · prateleira', 95, 53)
add('NP', 18, A, 'rodapé recuado (359 em 2 peças)', 180, 10, 2)
# painel-caixa para embutir as portas de correr da cozinha
add('NP', 18, A, "'painel caixa' p/ embutir as portas de correr da cozinha", 115, 55)
# ⚠ A prancha traz DOIS textos — "portas de abrir" e "portas basculantes" — e
#   manda ver o detalhe na FOLHA 02/10, que NÃO ESTÁ NA PASTA. Adotei as duas
#   folhas de 73 × 113 do topo do módulo central como basculantes. Se forem
#   mesmo basculantes, 113 cm de altura NÃO é caso de HK-xs: é Aventos
#   (R$ 600/un contra R$ 250). Swing de R$ 700 no custo. Pedir a folha 02/10.
# M1: 2 portas de 2,24 m → 4 dobradiças cada · M2: 2 básculas → 2 cada ·
# M3: 2 portas de 66 → 2 cada.
fer(A, dobr=8+4+4, gav=4, basc=2)
cava(A, 2*0.56 + 2*0.73 + 2*0.73 + 2*0.73 + 2*0.49)
fita(A, 'portas altas e superiores', 2*2*(0.56+2.24) + 2*2*(0.73+1.13))
fita(A, 'frentes de gavetão e do varal', 2*2*(0.73+0.30) + 2*2*(0.73+0.12))
fita(A, 'porta do módulo inferior', 2*2*(0.49+0.66))
fita(A, 'verticais, prateleiras, horizontais, rodapé',
     5*2.26 + 4*1.07 + 12*0.71 + 3.59 + 0.95)
terc(A, 'Tábua de passar embutida dobrável', TABUA)
terc(A, 'Varal retrátil embutido — 2 un ⚠ sem preço na base', 2*VARAL_RETR, True)

# ───────────────────────────────────────────────────────────────────────────
# 9 · LAVABO EXTERNO                                  folha 03/10 · Nogueira
#     painel 130 × 248 · armário 150 × 50 × 32 · acabamento no forro
# ───────────────────────────────────────────────────────────────────────────
A = 'Lavabo externo'
add('NP', 18, A, 'painel de parede 130 × 248', 130, 248)
add('NP', 18, A, 'acabamento no forro 130 × 40', 130, 40)
add('NP', 15, A, 'armário · laterais e divisória', 50, 32, 3)
# ⚠ CORREÇÃO 17/08 — onde a bancada é de MÁRMORE não existe tampo de MDF.
#   Eu tinha lançado 'tampo e base' em todo gabinete de banheiro e no lavabo.
#   Vira base + travessa, como já estava na bancada 01, na ilha e no gourmet.
add('NP', 15, A, 'armário · base', 145, 50)
add('NP', 15, A, 'armário · travessa superior (a bancada é mármore)', 145, 10)
add('NP', 6,  A, 'armário · fundo', 150, 32)
add('NP', 18, A, 'armário · porta basculante 71 × 30', 71, 30)
add('NP', 18, A, 'armário · fundo do nicho aparente 73 × 30', 73, 30)
fer(A, dobr=2, basc=1)
cava(A, 0.71)
fita(A, 'painel + acabamento no forro', 2*(1.30+2.48) + 2*(1.30+0.40))
fita(A, 'armário — báscula, nicho, bordas', 2*(0.71+0.30) + 2*(0.73+0.30)
        + 2*1.50 + 3*0.32)

# ───────────────────────────────────────────────────────────────────────────
# 10 · BANHEIRO MASTER                                folha 06/10 · Jequitibá
#      superior (espelheira) 185 × 15 × 120 · inferior RIPADO 185 × 50 × 52
# ───────────────────────────────────────────────────────────────────────────
A = 'Banheiro master'
# superior: nicho 18 | 3 portas de correr espelhadas em 141 | nicho 18
add('JQ', 15, A, 'superior · laterais e 2 divisórias', 15, 120, 4)
add('JQ', 15, A, 'superior · tampo e base', 179, 15, 2)
add('JQ', 18, A, 'superior · prateleiras dos nichos vazados', 18, 14, 4)
add('JQ', 6,  A, 'superior · fundo', 185, 120)
# inferior ripado: 4 portas de 45 × 52
add('JQ', 15, A, 'inferior · laterais e divisória', 50, 52, 3)
add('JQ', 15, A, 'inferior · base', 181, 50)
add('JQ', 15, A, 'inferior · travessa superior (a bancada é mármore)', 181, 10)
add('JQ', 6,  A, 'inferior · fundo', 185, 52)
n_bm = 4*int(45/RIPA_PASSO)
add('JQ', 15, A, 'inferior · base das portas ripadas 45 × 52', 45, 52, 4, True)
add('JQ', 18, A, f'inferior · régua {RIPA_L:.0f} cm das portas', RIPA_L, 52, n_bm, True)
fer(A, dobr=8)
fita(A, f'réguas das portas ripadas — {n_bm} × 0,52 m', n_bm*0.52)
fita(A, 'perímetro das 4 portas + nichos', 4*2*(0.45+0.52) + 4*2*(0.18+0.14)
        + 2*(1.85+0.15))
terc(A, 'Espelho prata c/ perfil — 3 folhas de correr (por FOLHA, não por m²)', 3*ESPELHO_FL)
terc(A, 'Deslizante RO65 Rometal — 3 portas + trilho 2 m', 3*RO65_PORTA + TRILHO_RO65)
terc(A, 'Puxador metálico tipo alça preto — 8 un', 8*PUX_ALCA)

# ───────────────────────────────────────────────────────────────────────────
# 11 · BANHEIRO 02 (social 1º pav)              folhas 07 e 08/10 · Nog.+Beige
#      superior 190 × 15 × 124 (106 correr espelhado + 74 nicho Beige)
#      inferior 110 × 42 × 52
# ───────────────────────────────────────────────────────────────────────────
A = 'Banheiro 02'
add('NP', 15, A, 'superior · laterais e divisória', 15, 124, 3)
add('NP', 15, A, 'superior · tampo e base', 185, 15, 2)
add('BG', 18, A, 'superior · prateleiras do nicho (MDF Beige)', 74, 14, 4)
add('BG', 6,  A, 'superior · fundo do nicho aparente (Beige)', 74, 124)
add('NP', 6,  A, 'superior · fundo do trecho de correr', 116, 124)
add('NP', 15, A, 'inferior · laterais e divisória', 42, 52, 3)
add('NP', 15, A, 'inferior · base', 106, 42)
add('NP', 15, A, 'inferior · travessa superior (a bancada é mármore)', 106, 10)
add('NP', 6,  A, 'inferior · fundo', 110, 52)
add('NP', 18, A, 'inferior · porta 53 × 50', 53, 50, 2)
add('NP', 18, A, 'inferior · nicho papeleiro embutido', 20, 24, 3)
fer(A, dobr=4)
cava(A, 2*0.53)
fita(A, 'portas + prateleiras Beige + bordas', 2*2*(0.53+0.50) + 4*0.74
        + 2*(1.90+0.15) + 2*(1.10+0.42))
terc(A, 'Espelho prata c/ perfil — 2 folhas de correr (por FOLHA, não por m²)', 2*ESPELHO_FL)
terc(A, 'Deslizante RO65 Rometal — 2 portas + trilho 2 m', 2*RO65_PORTA + TRILHO_RO65)
terc(A, 'LED fita + perfil de alumínio em L no nicho — 2,6 m', 2.6*LED_M)

# ───────────────────────────────────────────────────────────────────────────
# 12 · BANHEIRO 04                                folhas 09 e 10/10 · Nogueira
#      superior 110 × 15 × 124 + prateleiras laterais de 78 e 36
#      inferior 146 (91 c/ 2 portas + 55 nicho aberto) × 45 × 51
# ───────────────────────────────────────────────────────────────────────────
A = 'Banheiro 04'
add('NP', 15, A, 'superior · laterais', 15, 124, 2)
add('NP', 15, A, 'superior · tampo e base', 107, 15, 2)
add('NP', 6,  A, 'superior · fundo', 110, 124)
add('NP', 18, A, 'prateleira lateral esquerda 78 × 15', 78, 15, 2)
add('NP', 18, A, 'prateleira lateral direita 36 × 15', 36, 15, 2)
add('NP', 15, A, 'inferior · laterais e divisória', 45, 51, 3)
add('NP', 15, A, 'inferior · base', 142, 45)
add('NP', 15, A, 'inferior · travessa superior (a bancada é mármore)', 142, 10)
add('NP', 6,  A, 'inferior · fundo', 146, 51)
add('NP', 18, A, 'inferior · porta 44 × 49', 44, 49, 2)
add('NP', 18, A, 'inferior · nicho aberto 55 — fundo e prateleira', 55, 30, 2)
add('NP', 18, A, 'inferior · nicho papeleiro embutido', 20, 24, 3)
fer(A, dobr=4)
cava(A, 2*0.44)
fita(A, 'portas + prateleiras + nicho', 2*2*(0.44+0.49) + 4*2*(0.78+0.15)/2
        + 2*(1.46+0.45) + 2*(0.55+0.30))
terc(A, 'Espelho prata c/ perfil — 2 folhas de correr (por FOLHA, não por m²)', 2*ESPELHO_FL)
terc(A, 'Deslizante RO65 Rometal — 2 portas + trilho 2 m', 2*RO65_PORTA + TRILHO_RO65)
terc(A, 'Suporte metálico dourado de prateleira — 4 un ⚠ sem preço na base',
     4*SUP_DOURAD, True)

# ═══════════════════════════════════════════════════════════════════════════
# APURAÇÃO
# ═══════════════════════════════════════════════════════════════════════════
NOME_MAT = {'NP': 'Nogueira Persa', 'SA': 'Sálvia', 'JQ': 'Jequitibá',
            'BG': 'Beige'}
W = 96

# ⚠ GUARDA DE PEÇA FORA DE CHAPA — aprendizado deste projeto.
# A ripa do painel tem 288 cm e a chapa 275 × 185: não cabe em nenhum sentido.
# O `nest` não reclama, ele só abre uma chapa por peça — e o resultado (111
# chapas de Nogueira, 9% de aproveitamento) parece um plano de corte válido.
# Peça que não cabe é ERRO DE PROJETO DE MARCENARIA, não de empacotamento:
# ou emenda, ou muda o desenho. O motor tem de gritar.
_fora = [(m, e, a, d, c, l) for m, e, a, d, c, l, q, r in P
         if max(c, l) > CH_C or min(c, l) > CH_L]
if _fora:
    print('\n' + '!'*W)
    print('PEÇAS QUE NÃO CABEM NA CHAPA DE 275 × 185 — corrigir antes de orçar')
    for m, e, a, d, c, l in _fora:
        print(f'  {NOME_MAT[m]} {e} mm · {a} · {d}: {c:.0f} × {l:.0f} cm')
    print('!'*W + '\n')

por_chapa, area_chapa = defaultdict(list), defaultdict(float)
area_amb, area_rip_amb = defaultdict(float), defaultdict(float)
for mat, esp, amb, desc, c, l, q, rip in P:
    for _ in range(q):
        por_chapa[(mat, esp)].append((c, l))
    a = c*l*q/10000
    area_chapa[(mat, esp)] += a
    area_amb[amb] += a
    if rip: area_rip_amb[amb] += a

CHAPAS = {k: nest(v) for k, v in por_chapa.items()}

def linha(ch='─'): print(ch*W)

print('═'*W)
print('ELIUTON RIBEIRO · RESIDÊNCIA BRISAS DA PAMPULHA — LEVANTAMENTO DE MATERIAL E CUSTO')
print('═'*W)
print('Projeto executivo: Arq. Luciana Beatriz Simplício · Núcleo SC Arquitetura')
print('Pranchas: folhas 01–08/08 (cozinha e gourmet) e 01–10/10 (serviço e banheiros)')
print('Escala 1:25 · geometria lida no vetor · a folha 02/10 não estava na pasta')

print('\nESCOPO POR AMBIENTE')
ordem = list(dict.fromkeys(a for *_, a, _1, _2, _3, _4, _5 in
                           [(m, e, amb, d, c, l, q, r) for m, e, amb, d, c, l, q, r in P]))
ordem = []
for _m, _e, amb, *_r in P:
    if amb not in ordem: ordem.append(amb)
for amb in ordem:
    d, g, b = FER[amb]
    extra = []
    if d: extra.append(f'{d} dobr.')
    if g: extra.append(f'{g} gav.')
    if b: extra.append(f'{b} básc.')
    rip = f'  ·  ripado {area_rip_amb[amb]:.2f} m²' if area_rip_amb[amb] else ''
    print(f'  {amb:<32}{area_amb[amb]:>7.2f} m² de chapa   '
          f'{" · ".join(extra):<26}{rip}')
print(f'  {"TOTAL":<32}{sum(area_amb.values()):>7.2f} m²')

print('\nPLANO DE CORTE  (nesting por cor × espessura — cores nunca dividem chapa)')
custo_chapa = 0.0
for (mat, esp) in sorted(CHAPAS, key=lambda k: (k[0], -k[1])):
    n = CHAPAS[(mat, esp)]; pr = PRECO_CHAPA[esp]; c = n*pr
    custo_chapa += c
    ap = area_chapa[(mat, esp)]/(n*CH_AREA)*100
    print(f'  {NOME_MAT[mat]+" "+str(esp)+" mm":<22}'
          f'{area_chapa[(mat,esp)]:>7.2f} m²  →  {n:>2} chapa(s) × R$ {pr:>7,.2f}'
          f'  = R$ {c:>9,.2f}   aprov. {ap:>3.0f}%'.replace(',', '.'))
tot_ch = sum(CHAPAS.values()); area_tot = sum(area_chapa.values())
print(f'  {"TOTAL":<22}{area_tot:>7.2f} m²  →  {tot_ch:>2} chapas'
      f'                       R$ {custo_chapa:>9,.2f}   médio '
      f'{area_tot/(tot_ch*CH_AREA)*100:.0f}%'.replace(',', '.'))

print('\nFITA DE BORDA E FILETAGEM  (+10% de desperdício na fita)')
m_amb = defaultdict(float)
for amb, d, m in FITA: m_amb[amb] += m
for amb in ordem:
    if m_amb[amb]: print(f'  {amb:<40}{m_amb[amb]:>9.2f} m')
m_fita = sum(m for _, _, m in FITA)
custo_fita  = m_fita*DESPERD*FITA_COR
custo_filet = m_fita*FILET_MAQ
print(f'  {"TOTAL":<40}{m_fita:>9.2f} m')
_v = f'{custo_fita:,.2f}'.replace(',', '.')
print(f'  {"material da fita (cor, R$ 3,00/m +10%)":<40}          R$ {_v:>9}')
_v = f'{custo_filet:,.2f}'.replace(',', '.')
print(f'  {"filetagem na coladeira (R$ 2,50/m)":<40}          R$ {_v:>9}')

print('\nUSINAGEM DE PUXADOR  (o projeto pede "puxador tipo cava" em quase tudo)')
n_cava = sum(CAVA_M.values())
custo_cava = n_cava*CAVA_USIN
_v = f'{custo_cava:,.2f}'.replace(',', '.')
print(f'  Cava 35° usinada — {n_cava:.1f} m × R$ 25,00/m{"":>21}R$ {_v:>9}')

print('\nTERCEIRIZADOS E ITENS ESPECIAIS')
custo_terc = 0.0
for amb, d, v, est in TERC:
    custo_terc += v
    print(f'  {amb:<26} {d:<52}R$ {v:>8,.2f}'.replace(',', '.'))
print(f'  {"TOTAL":<79}R$ {custo_terc:>8,.2f}'.replace(',', '.'))

TOT_DOBR = sum(f[0] for f in FER.values())
TOT_GAV  = sum(f[1] for f in FER.values())
TOT_BASC = sum(f[2] for f in FER.values())
N_PRAT   = sum(q for m, e, a, d, c, l, q, r in P if 'prateleira' in d.lower())
custo_sup = N_PRAT*4*SUP_PRAT

print(f'\nFERRAGEM DO PROJETO — {TOT_DOBR} dobradiças · {TOT_GAV} gavetas · '
      f'{TOT_BASC} básculas · {N_PRAT} prateleiras')

# ── logística e instalação ─────────────────────────────────────────────────
# ⛔ MONTAGEM NÃO ENTRA NA PROPOSTA  [Jonathan 17/08]
#    Está em `referencias/validacao-orcamento.md`, na lista de custos FIXOS:
#    "salários de toda a equipe (7 profissionais — marceneiros, montadores,
#     etc.) … A produção é fixa, não por demanda."
#    E logo abaixo: "o marceneiro tem salário (fixo, fora do orçamento) e pode
#    ter comissão (variável, dentro do orçamento). Só a comissão entra."
#    A comissão já está DENTRO do motor, nos coeficientes a = 0,162 e
#    liqF·b = 0,0378. Lançar dia de montador como custo direto é contar duas
#    vezes: uma no salário que a empresa já paga de qualquer jeito, outra na
#    comissão que o divisor já cobra.
#
#    Eu tinha lançado 13 dias de dupla (R$ 7.800) — e antes disso 22 (R$ 13.200).
#    Os dois estavam errados pela mesma razão: a linha não existe.
#
#    Da logística sobra o que É variável e por demanda: CARRETO e VISITA.
N_CARRETO, R_CARRETO = 4, 600.0
N_VISITA,  R_VISITA  = 3, 250.0
LOG = N_CARRETO*R_CARRETO + N_VISITA*R_VISITA

# ── fechamento por cenário ─────────────────────────────────────────────────
print('\n' + '═'*W)
print('CUSTO DIRETO E PREÇO — TRÊS CENÁRIOS')
print('═'*W)

# Rateio do ripado. NÃO é proporcional ao custo total: o painel ripado não tem
# ferragem, não tem cava e quase não tem terceirizado. Ele leva a fatia de
# chapa/fita/filetagem/consumíveis/logística proporcional à área, mais os dois
# sistemas de porta que são dele (deslizante embutido + pivotante).
area_rip = sum(area_rip_amb.values())
frac_rip = area_rip/area_tot
TERC_RIP = RO82_TOP + PIVO

resultados = []
for nome, ferr_desc, mc, f, gar in CENARIOS:
    custo_ferr = TOT_DOBR*f['dobr'] + TOT_GAV*f['corr'] + TOT_BASC*f['art']
    consum = (custo_chapa + custo_fita)*0.06
    MAT = (custo_chapa + custo_fita + custo_filet + custo_cava + custo_ferr
           + custo_sup + custo_terc + consum)
    CD = MAT + LOG
    cd_rip = ((custo_chapa + custo_fita + custo_filet + consum + LOG)*frac_rip
              + TERC_RIP)
    cd_resto = CD - cd_rip
    inv = preco(cd_resto, cd_rip, mc)
    inv_r = round(inv/100)*100
    resultados.append((nome, ferr_desc, mc, gar, custo_ferr, CD, inv_r,
                       mc_conferida(inv_r, CD)))

print(f'  {"":<17}{"ferragem":>10}{"custo direto":>14}{"INVESTIMENTO":>15}'
      f'{"MC real":>9}{"garantia":>11}')
for nome, fd, mc, gar, cf, cd, inv, mcr in resultados:
    print(f'  {nome:<17}{cf:>10,.0f}{cd:>14,.0f}{inv:>15,.0f}'
          f'{mcr*100:>8.1f}%{gar:>11}'.replace(',', '.'))

print('\n  Composição do custo direto (igual nos três, exceto a ferragem):')
consum = (custo_chapa + custo_fita)*0.06
for rot, v in (('Chapas', custo_chapa), ('Fita (material)', custo_fita),
               ('Filetagem (aplicação)', custo_filet),
               ('Usinagem das cavas', custo_cava),
               ('Suportes de prateleira', custo_sup),
               ('Terceirizados e especiais', custo_terc),
               ('Consumíveis (6% de chapa + fita)', consum),
               (f'Logística — {N_CARRETO} carretos + {N_VISITA} visitas técnicas '
                f'(montagem NÃO entra: é custo fixo)', LOG)):
    _v = f'{v:,.2f}'.replace(',', '.')
    print(f'    {rot:<74}R$ {_v:>9}')

consum = (custo_chapa + custo_fita)*0.06
cd_rip_v = (custo_chapa + custo_fita + custo_filet + consum + LOG)*frac_rip + TERC_RIP
_v = f'{cd_rip_v:,.0f}'.replace(',', '.')
print(f'\n  Ripado = {area_rip:.2f} m² de chapa ({frac_rip*100:.0f}% do projeto) '
      f'⇒ R$ {_v} de custo direto, à parte, a MC {MC_RIPADO*100:.0f}%.')
print('  (o painel não tem ferragem nem cava — só leva chapa, fita, consumível,')
print('   logística e os dois sistemas de porta que são dele.)')

print('\n  ⚠ NÃO ESTÁ INCLUÍDO: todo o mármore. Bancadas 01/02/03, ilha tipo')
print('    cascata, ripado da bancada 03, rodabancas, nichos, cubas esculpidas,')
print('    prateleiras e o "detalhe caixa" da cozinha são MARMORARIA. As pranchas')
print('    especificam Carrara e Travertino em praticamente todo ambiente. Se a')
print('    Valvic for fornecer, é orçamento à parte e muda o total.')

# ── sensibilidade ──────────────────────────────────────────────────────────
# ── rateio por ambiente, nos três cenários ─────────────────────────────────
# Exato onde dá (ferragem, cava, terceirizado são atribuíveis); rateado por
# área de chapa onde não dá (chapa, fita, filetagem, consumível, logística).
#
# [Jonathan 17/08] REALOCAÇÃO COMERCIAL: −R$ 5.000 da área de serviço,
# +R$ 5.000 no painel ripado. O total NÃO muda — é remanejamento de vitrine
# entre itens, não mudança de escopo nem de margem do projeto.
REALOC = {'Área de serviço': -5000, 'Cozinha · painel ripado': +5000}

terc_amb = defaultdict(float)
for amb, d, v, est in TERC: terc_amb[amb] += v
consum = (custo_chapa + custo_fita)*0.06
rateavel = custo_chapa + custo_fita + custo_filet + consum + LOG
prat_amb = defaultdict(int)
for m, e, a, d, c, l, q, r in P:
    if 'prateleira' in d.lower(): prat_amb[a] += q

ITENS = {}                       # ambiente -> [inv_cen1, inv_cen2, inv_cen3]
for ci, (nome_c, _fd, mc, f, _g) in enumerate(CENARIOS):
    for amb in ordem:
        fr = area_amb[amb]/area_tot
        d, g, b = FER[amb]
        exato = (d*f['dobr'] + g*f['corr'] + b*f['art'] + CAVA_M[amb]*CAVA_USIN
                 + prat_amb[amb]*4*SUP_PRAT + terc_amb[amb])
        cd = exato + rateavel*fr
        fr_r = area_rip_amb[amb]/area_amb[amb] if area_amb[amb] else 0.0
        cd_r = rateavel*fr*fr_r + (TERC_RIP if amb == 'Cozinha · painel ripado' else 0)
        inv = round((preco(cd - cd_r, cd_r, mc) + REALOC.get(amb, 0))/100)*100
        ITENS.setdefault(amb, []).append(inv)

print('\n' + '─'*W)
print('INVESTIMENTO POR ITEM — os três cenários')
print('  (já com a realocação de R$ 5.000 da área de serviço para o painel ripado)')
print(f'  {"item":<34}{"chapa":>8}{"1 · Telesc.":>14}{"2 · Hardt":>13}{"3 · Hettich":>14}')
somas = [0, 0, 0]
for amb in ordem:
    v = ITENS[amb]
    for k in range(3): somas[k] += v[k]
    cols = ''.join(f'{f"{x:,.0f}".replace(",", "."):>14}' if k == 0 else
                   f'{f"{x:,.0f}".replace(",", "."):>13}' if k == 1 else
                   f'{f"{x:,.0f}".replace(",", "."):>14}'
                   for k, x in enumerate(v))
    print(f'  {amb:<34}{area_amb[amb]:>8.2f}{cols}')
cols = ''.join(f'{f"{x:,.0f}".replace(",", "."):>14}' if k != 1 else
               f'{f"{x:,.0f}".replace(",", "."):>13}' for k, x in enumerate(somas))
print(f'  {"TOTAL":<34}{area_tot:>8.2f}{cols}')

print('\n' + '─'*W)
print('SENSIBILIDADE — as três premissas que mais mexem no número')
custo_esp = sum(CHAPAS[k]*PRC_ESP[k[1]] for k in CHAPAS)
d_esp = custo_esp - custo_chapa
base_mc = CENARIOS[1][2]
print(f'  1. Chapa Arauco madeirada cotada como ESPECIAL (950/1200/800) em vez '
      f'de COR:\n     custo +R$ {d_esp:,.0f}  →  preço +R$ {d_esp/div(base_mc):,.0f} '
      f'no cenário 2.'.replace(',', '.'))
# fundos em branco
area_f6 = sum(c*l*q/10000 for m, e, a, d, c, l, q, r in P if e == 6)
ec_branco = area_f6/(CH_AREA*0.80)
d_fundo = -(PRC_COR[6]-190.0)*ec_branco
print(f'  2. Fundos em branco 6 mm em vez da cor ({area_f6:.1f} m²):'
      f'\n     custo R$ {d_fundo:,.0f}  →  preço R$ {d_fundo/div(base_mc):,.0f}. '
      f'⚠ as perspectivas mostram o interior na cor.'.replace(',', '.'))
# ripado do painel
cd_pain = area_rip_amb['Cozinha · painel ripado']
print(f'  3. O painel do estar/jantar sozinho tem {cd_pain:.2f} m² de chapa '
      f'({cd_pain/area_tot*100:.0f}% do projeto).\n     A prancha diz "parte '
      f'ripado parte liso" e eu adotei 100% ripado. Se metade for lisa,\n'
      f'     saem ~{int(572/RIPA_PASSO)//2} réguas e ~{int(572/RIPA_PASSO)//2*2.88:.0f} m de fita.')
bg = sum(CHAPAS[k]*PRECO_CHAPA[k[1]] for k in CHAPAS if k[0] == 'BG')
abg = sum(area_chapa[k] for k in area_chapa if k[0] == 'BG')
_v = f'{bg:,.0f}'.replace(',', '.'); _p = f'{bg/div(base_mc):,.0f}'.replace(',', '.')
print(f'  4. O MDF BEIGE existe só nas 4 prateleiras do nicho do banheiro 02 '
      f'({abg:.2f} m²).\n     Como cor não divide chapa, custa R$ {_v} de chapa '
      f'inteira → R$ {_p} de preço.\n     Trocar por Nogueira Persa apaga essa '
      f'linha sem tocar em mais nada do projeto.')

print('\n' + '─'*W)
print('COM RT DE 10% PARA A ARQUITETA  (a alavanca isolada mais cara do projeto)')
for nome, fd, mc, gar, cf, cd, inv, mcr in resultados:
    cd_rip = cd*frac_rip
    inv_rt = round(preco(cd-cd_rip, cd_rip, mc, rt=True)/100)*100
    print(f'  {nome:<17}R$ {inv:>9,.0f}  →  R$ {inv_rt:>9,.0f}   '
          f'(+{(inv_rt/inv-1)*100:.0f}%)'.replace(',', '.'))

print('\n' + '─'*W)
print('REVISÃO 17/08 — O QUE ESTAVA ERRADO NA 1ª VERSÃO  [Jonathan: "valores altos demais"]')
CORR = [
 ('Nicho de eletrodoméstico com FUNDO de MDF. Geladeira, forno, micro-ondas e',
  'cervejeira precisam de ventilação e tomada — o fundo é a alvenaria.', '−6,2 m²'),
 ('Tampo contado duas vezes na torre: o tampo do nicho da geladeira JÁ É a',
  'base do armário basculante de cima.', '−0,7 m²'),
 ('Fundo do caixote de vidro do gourmet contado duas vezes.', '', '−0,4 m²'),
 ('Tampo de MDF sob bancada de MÁRMORE, em 5 gabinetes.',
  'Vira travessa — quem faz o tampo é a marmoraria.', '−1,8 m²'),
 ('CAVA cobrada por PEÇA (R$ 50 × 50) em vez de por METRO (R$ 25 × 30,3 m),',
  'que é a convenção que o Jonathan validou na Honda.', '−R$ 1.744'),
 ('ESPELHO cotado por m² — a armadilha nº 4 da minha própria lista.',
  'A casa cota por FOLHA: R$ 285 com perfil.', '−R$ 542'),
 ('SS150 (sistema de ROUPEIRO) em porta de espelho de armário de 15 cm de',
  'profundidade. O certo é RO65 Rometal.', '−R$ 1.610'),
 ('LED a R$ 150/m; a decomposição rastreável dá R$ 66/m (fita 28 + perfil 38).',
  '', '−R$ 341'),
 ('MONTAGEM lançada como custo direto — 22 dias de dupla, depois 13.',
  'A linha NÃO EXISTE: montador é salário fixo, fora do orçamento.', '−R$ 13.200'),
]
for i, (l1, l2, v) in enumerate(CORR, 1):
    print(f'  {i:>2}. {l1:<73}{v:>12}')
    if l2: print(f'      {l2}')
print(f'\n  Efeito: 169,93 → {area_tot:.2f} m² de chapa · 49 → {tot_ch} chapas')
_a = f'{resultados[1][5]:,.0f}'.replace(',', '.')
_b = f'{resultados[1][6]:,.0f}'.replace(',', '.')
print(f'          custo direto R$ 61.219 → R$ {_a} · preço R$ 143.800 → R$ {_b} (cenário 2)')
print('  A correção 9 sozinha vale mais que as oito outras somadas.')
print(f'  Sanidade R$/m² de chapa: 846 → {resultados[1][6]/area_tot:.0f}  (faixa da casa 626–834)')
print('═'*W)
