# -*- coding: utf-8 -*-
"""
CASA L&M — Alphaville · Caderno Técnico 07/2026 (40 pranchas, A2)
Levantamento peça-a-peça + plano de corte + ferragens + motor de preço.

ESCOPO — o que é NOSSO (marcenaria) e o que JÁ EXISTE:
  FORA: forro de gesso/tabica/cortineiro (p4) · bancadas em granito (existentes,
        conferir in loco) · armários inferiores da cozinha V1 (EXISTENTES —
        reorganizar módulos) · prateleiras da despensa (EXISTENTES) · gavetas
        MDF bege do banho suíte (existentes; removemos a de baixo) · espelhos ·
        coifa Suggar · cooktop Philco · cesta elevatória · quadro de energia.
  ATENÇÃO: "MDF cinza chumbo/grafite – IGUAL EXISTENTE" = móvel NOVO na cor do
        existente. Só "ARMÁRIOS EXISTENTES"/"PRATELEIRAS EXISTENTE" saem do escopo.
"""

CH_C, CH_L = 275.0, 185.0                 # chapa 2,75 x 1,85 m (cm)
CH_AREA = (CH_C/100)*(CH_L/100)           # 5,0875 m²

# ---------------------------------------------------------------- preços chapa
P = {
    # Carvalho Batur (painel sala) — melamínico fosco amadeirado
    'BAT15': 500.0, 'BAT18': 600.0, 'BAT6': 300.0,
    # Carvalho Brun (suíte + banheiros) — melamínico fosco amadeirado
    'BRN15': 500.0, 'BRN18': 600.0, 'BRN6': 300.0,
    # Branco Ártico Duratex (aéreos cozinha, despensa alto, piso-teto)
    'ART15': 260.0, 'ART18': 330.0, 'ART6': 190.0,
    # Cinza Chumbo/Grafite (torre cozinha, despensa baixo) — melamínico fosco cor
    'GRF15': 500.0, 'GRF18': 600.0, 'GRF6': 300.0,
    # miolo do painel de 30mm (não aparece)
    'CRU15': 260.0,
}
NOBRE = ('BAT15','BAT18','BAT6','BRN15','BRN18','BRN6','GRF15','GRF18','GRF6')

FITA_COMUM, FITA_NOBRE = 2.0, 3.0         # R$/m  (+10% desperdício aplicado depois)
FILETAGEM            = 2.5                # R$/m  aplicação na coladeira

# ------------------------------------------------------------------ ferragens
P_DOBR_BLACK   = 40.00    # Hettich Sensys Black (amortecimento integrado)
P_CORR_TELESC  = 40.00    # par
P_CORR_OCULTA  = 120.00   # par — Hettich Quadro (closet/sapateira: corrediça oculta)
P_PIVO         = 120.00   # conjunto porta pivotante
P_FECH_ROLETE  = 25.00
P_PUX_ALCA_60  = 180.00   # alça inox preto 60cm
P_PUX_METALICO = 90.00    # puxador metálico preto/grafite (roupeiro/closet)
P_CAVA_USINADA = 50.00    # peça — puxador cava 45° usinado
P_LED_M        = 150.00   # fita + perfil + lente difusora + usinagem, por metro
P_CABIDEIRO    = 120.00   # cabideiro em metal preto/grafite
P_GANCHOS      = 90.00    # conjunto ganchos vassouras (despensa)
P_PERFURADA_M2 = 450.00   # [Jonathan] chapa metálica perfurada 3mm preta
# Serralheria do closet SAI do custo: [Jonathan 28/07] a estrutura metálica cinza
# grafite já vem embutida no preço por folha do Renolfh.

# Portas em vidro reflecta — COTAÇÃO RENOLFH (preço por folha, todas h=271)
#   consistência conferida: R$ 1.085 a 1.153/m² (variação de 6%)
VIDRO = [                        # (elevação, qtd, larg_m, preço/folha)
    ('closet V3',   2, 0.772, 2270.00),   # R$ 1.085/m²
    ('closet V5',   2, 0.697, 2070.00),   # R$ 1.096/m²
    ('closet V4',   2, 0.595, 1860.00),   # R$ 1.153/m²
    ('roupeiro',    2, 0.650, 1960.00),   # R$ 1.113/m²
]
# ⚠ closet V1 (2 folhas de 0,60 x 2,71) fora — ver nota do cabeçalho.
#   Se entrar, ~R$ 1.870/folha pela mesma curva → +R$ 3.740.
custo_vidro_closet   = sum(q*p for n, q, l, p in VIDRO if n.startswith('closet'))
custo_vidro_roupeiro = sum(q*p for n, q, l, p in VIDRO if n == 'roupeiro')
custo_vidro          = custo_vidro_closet + custo_vidro_roupeiro
m2_vidro             = sum(q*l*2.71 for n, q, l, p in VIDRO)

# ============================================================== estrutura dados
PECAS = []            # (item, desc, mat, comp, larg, qtd)
def add(item, desc, mat, c, l, q=1):
    PECAS.append((item, desc, mat, float(c), float(l), int(q)))

def caixa(item, nome, mat, larg, alt, prof, n_prat=0, mat_fundo=None, prat18=False):
    """Caixaria padrão Valvic: 2 laterais + base + tampo + fundo 6mm + prateleiras."""
    f = mat_fundo or (mat[:3] + '6')
    add(item, f'{nome} · lateral',   mat, alt,  prof, 2)
    add(item, f'{nome} · base/tampo',mat, larg, prof, 2)
    add(item, f'{nome} · fundo',     f,   larg, alt,  1)
    if n_prat:
        mp = (mat[:3] + '18') if (prat18 or larg > 70) else mat
        add(item, f'{nome} · prateleira', mp, larg, prof, n_prat)

def gaveta(item, nome, mat, larg, prof, alt, q=1, frente_mat=None):
    """Gaveta Valvic de 6 peças: frente + contrafrente + 2 laterais + fundo + base."""
    fm = frente_mat or mat
    add(item, f'{nome} · frente',       fm,  larg, alt,  q)
    add(item, f'{nome} · contrafrente', mat, larg-3, alt-3, q)
    add(item, f'{nome} · lateral',      mat, prof, alt-3, 2*q)
    add(item, f'{nome} · traseira',     mat, larg-3, alt-3, q)
    add(item, f'{nome} · base',         mat[:3]+'6', larg-3, prof, q)

# ═══════════════════════════════════════════════════ 1. PAINEL SALA JANTAR
# MDF Carvalho Batur Duratex 30mm = 15mm (face) + 15mm (miolo). Altura 256.
# Elev01 382 (contém porta pivotante mimetizada 86,5x210) · Elev02 288 · Elev03 180
I = '1 Painel sala jantar'
for larg, nome in ((382-86.5, 'elev.01'), (288, 'elev.02'), (180, 'elev.03')):
    add(I, f'painel {nome} · face vista',  'BAT15', larg, 256)
    add(I, f'painel {nome} · miolo 30mm',  'CRU15', larg, 256)
# porta pivotante mimetizada — 30mm, DUAS faces à vista (lado sala e lado cozinha)
add(I, 'porta pivotante · face sala',    'BAT15', 86.5, 210)
add(I, 'porta pivotante · face cozinha', 'BAT15', 86.5, 210)
# batente em MDF Carvalho Batur 30mm (2 montantes + verga), 12cm de largura
add(I, 'batente · montante', 'BAT15', 210, 12, 4)
add(I, 'batente · verga',    'BAT15', 86.5, 12, 2)
# suporte de fixação na alvenaria 20mm — sarrafos verticais a cada 45cm
add(I, 'suporte fixação alvenaria', 'CRU15', 256, 8, 20)

# ═══════════════════════════════════════════════ 2. ARMÁRIO ALTO COZINHA (aéreo L)
# MDF Branco Ártico · em L 182 + 147 · prof 36,5 · altura 126 · furo coifa
I = '2 Aéreo cozinha (L)'
caixa(I, 'trecho A (182)', 'ART15', 182, 126, 36.5, n_prat=2)
caixa(I, 'trecho B (147)', 'ART15', 147, 126, 36.5, n_prat=2)
add(I, 'divisória vertical', 'ART15', 126, 36.5, 5)
# portas: trecho A = 3x44,9 + 37 · trecho B = 3x48,4 + 36,7 · altura 126
add(I, 'porta 44,9', 'ART15', 44.9, 126, 3)
add(I, 'porta 37',   'ART15', 37.0, 126, 1)
add(I, 'porta 48,4', 'ART15', 48.4, 126, 3)
add(I, 'porta 36,7', 'ART15', 36.7, 126, 1)
# prateleiras soltas da parede da janela (4 un, 65 x 28)
add(I, 'prateleira parede janela', 'ART18', 65, 28, 4)
# testeira/rodapé de arremate do aéreo
add(I, 'testeira', 'ART15', 182, 8, 1)
add(I, 'testeira', 'ART15', 147, 8, 1)

# ═══════════════════════════════════════════ 3. ARMÁRIO COZINHA (torre + gabinete)
# MDF Cinza Chumbo/Grafite "igual existente" · elevação 234 x 271,4 · prof 62/57
I = '3 Armário cozinha (torre)'
caixa(I, 'torre esquerda',  'GRF15', 70,  271.4, 62, n_prat=2)
caixa(I, 'torre direita',   'GRF15', 64,  271.4, 62, n_prat=0)
caixa(I, 'módulo central',  'GRF15', 100, 193,   62, n_prat=2)
add(I, 'divisória vertical', 'GRF15', 271.4, 62, 3)
# portas superiores (2x 34,9 e 2x 50,1) e torre (2x 32) — altura 117 / 271
add(I, 'porta 34,9 (h117)', 'GRF15', 34.9, 117, 2)
add(I, 'porta 50,1 (h89)',  'GRF15', 50.1, 89,  2)
add(I, 'porta torre 32',    'GRF15', 32.0, 271.4, 2)
add(I, 'porta tempero',     'GRF15', 23.0, 28.3, 1)
# gavetões e gavetas (frente em grafite)
gaveta(I, 'gavetão 1', 'GRF15', 102.6, 55, 28.3)
gaveta(I, 'gavetão 2', 'GRF15', 102.6, 55, 28.3)
gaveta(I, 'gaveta',    'GRF15', 27.0,  55, 28.3, q=2)
# 6 prateleiras com corrediça telescópica (coluna de 61)
add(I, 'prateleira corrediça', 'GRF15', 61, 55, 6)
# nichos abertos
add(I, 'nicho · divisória', 'GRF15', 44.5, 62, 3)
# testeira / sóculo novo (altura e revestimento igual existente)
add(I, 'sóculo novo', 'GRF15', 234, 10, 2)

# ═══════════════════════════════════════════════════ 4. ARMÁRIO ALTO DESPENSA
# MDF Branco Ártico · 292 x 65 x 31 · 8 portas de 36,5
I = '4 Despensa · armário alto'
caixa(I, 'corpo', 'ART15', 292, 65, 31, n_prat=0)
add(I, 'divisória vertical', 'ART15', 65, 31, 3)
add(I, 'porta 36,5', 'ART15', 36.5, 65, 8)

# ═══════════════════════════════════════════════════ 5. ARMÁRIO BAIXO DESPENSA
# MDF Cinza Chumbo/Grafite · 292 x 60 x 30 · gavetas 3(x6) 4(x3, perfurada) 5(x2)
I = '5 Despensa · armário baixo'
caixa(I, 'corpo', 'GRF15', 292, 60, 30, n_prat=0)
add(I, 'divisória vertical', 'GRF15', 60, 30, 3)
gaveta(I, 'gaveta 3', 'GRF15', 71.9, 28, 27.5, q=4)
gaveta(I, 'gaveta 5', 'GRF15', 72.3, 28, 27.5, q=2)
# gaveta 4 = quadro em MDF + chapa metálica perfurada (só o quadro é madeira)
add(I, 'gaveta 4 · frente',  'GRF15', 70.8, 18, 3)
add(I, 'gaveta 4 · quadro',  'GRF15', 68.8, 4,  6)
add(I, 'gaveta 4 · quadro lateral', 'GRF15', 26.5, 4, 6)

# ═══════════════════════════════════════════ 6. ARMÁRIO PISO-TETO DESPENSA
# MDF Branco Ártico · 103 x 286 x 30 · 2 portas · puxador cava · 5 prat. corrediça
I = '6 Despensa · piso-teto'
caixa(I, 'corpo', 'ART15', 103, 286, 30, n_prat=3, prat18=True)
add(I, 'divisória vertical', 'ART15', 181, 30, 1)
add(I, 'porta 41,5', 'ART15', 41.5, 286, 2)
# 5 prateleiras corrediça (bandeja 30 x 28 x 8,5)
gaveta(I, 'prat. corrediça', 'ART15', 30, 28, 8.5, q=5)

# ═══════════════════════════════════════════════ 7. ROUPEIRO SUÍTE (lateral curva)
# MDF Carvalho Brun · 151 x 271 x 40 · 2 portas em VIDRO REFLECTA · 6 prateleiras
I = '7 Suíte · roupeiro'
caixa(I, 'corpo', 'BRN15', 136, 271, 40, n_prat=6, prat18=True)
add(I, 'lateral curva (raio 23,5) · gomos', 'BRN6', 271, 26, 4)
add(I, 'lateral curva · miolo estrutural',  'BRN15', 271, 15, 2)

# ═══════════════════════════════════════════════════════ 8. SAPATEIRA SUÍTE
# MDF Carvalho Brun · 113 x 280 x 32,6 · 2 portas · 13 prateleiras corrediça · LED
I = '8 Suíte · sapateira'
caixa(I, 'corpo', 'BRN15', 106, 280, 32.6, n_prat=0)
add(I, 'porta 54,5', 'BRN15', 54.5, 272, 2)
# 13 bandejas corrediça (106 x 26 x 4,5 · caixa 104 x 23 x 1,5)
gaveta(I, 'bandeja sapato', 'BRN15', 104, 24.5, 6.0, q=13)

# ═══════════════════════════════════════════════════════ 9. CLOSET SUÍTE (em U)
# MDF Carvalho Brun · U 241,5 x 220 · altura 280 · portas vidro reflecta cinza
# + estrutura metálica cinza grafite · 20 gavetas corrediça oculta · LED
I = '9 Suíte · closet'
# três corpos: V3 (160), V4 (124), V5 (160) — prof 60/61,5
caixa(I, 'corpo V3', 'BRN15', 160, 280, 60, n_prat=5, prat18=True)
caixa(I, 'corpo V4', 'BRN15', 124, 280, 60, n_prat=4, prat18=True)
caixa(I, 'corpo V5', 'BRN15', 160, 280, 60, n_prat=4, prat18=True)
add(I, 'divisória vertical', 'BRN15', 280, 60, 6)
# gavetas: tipo 1 (76,25x51,5x19) x9 · tipo 2 (76,25x51,5x26) x3
#          tipo 3 (59,75x53,5x19) x6 · tipo 4 (59,75x53,5x26) x2
gaveta(I, 'gaveta 1', 'BRN15', 76.25, 51.5, 19, q=9)
gaveta(I, 'gaveta 2', 'BRN15', 76.25, 51.5, 26, q=3)
gaveta(I, 'gaveta 3', 'BRN15', 59.75, 53.5, 19, q=6)
gaveta(I, 'gaveta 4', 'BRN15', 59.75, 53.5, 26, q=2)
# testeiras de arremate do topo (280)
add(I, 'testeira topo', 'BRN15', 241.5, 10, 1)

# ═══════════════════════════════════════════════════ 10. ARMÁRIO BANHO SUÍTE
# MDF Carvalho Brun · 200 x 55,5 · 3 gavetas (1 = cesto de roupa) · bancada existente
I = '10 Banho suíte'
add(I, 'lateral/divisória', 'BRN15', 55, 30, 4)
gaveta(I, 'gaveta 68', 'BRN15', 68, 52.5, 30)
gaveta(I, 'gaveta 73', 'BRN15', 73, 52.5, 30)
gaveta(I, 'gaveta-cesto 59', 'BRN15', 59, 52.5, 30)
add(I, 'cesto · corpo', 'BRN15', 52.5, 44.5, 2)

# ═════════════════════════════════════ 11-14. ARMÁRIOS DE BANHEIRO E LAVABO
# Todos MDF Carvalho Brun · bancada em granito EXISTENTE (conferir in loco)
def banheiro(item, larg, prof, alt, n_porta, larg_porta, n_gav, larg_gav, n_prat):
    caixa(item, 'corpo', 'BRN15', larg, alt, prof, n_prat=n_prat)
    add(item, 'divisória vertical', 'BRN15', alt, prof, 2)
    if n_porta: add(item, 'porta', 'BRN15', larg_porta, alt, n_porta)
    if n_gav:   gaveta(item, 'gaveta', 'BRN15', larg_gav, prof-3, alt/2-1, q=n_gav)
    add(item, 'batente', 'BRN15', larg, 5, 2)

banheiro('11 Banho 01 (visita)',      156, 53, 44, 2, 25.0, 2, 50.0, 2)
banheiro('12 Banho 02 (Terezinha)',   169, 53, 44, 2, 34.5, 2, 52.0, 2)
banheiro('13 Banho 03 (Natalia/Gab)', 138, 53, 44, 2, 28.5, 2, 43.0, 2)
# lavabo: 166 x 46 x 30 · nicho aberto (64) + 2 gavetas (48)
I = '14 Lavabo'
caixa(I, 'corpo', 'BRN15', 166, 30, 46, n_prat=0)
add(I, 'divisória vertical', 'BRN15', 30, 46, 2)
gaveta(I, 'gaveta 48', 'BRN15', 48, 42.5, 27, q=2)
add(I, 'nicho · fundo aparente', 'BRN15', 64, 27, 1)
add(I, 'batente', 'BRN15', 166, 5, 2)

# ═══════════════════════════════════════════════════════════ PLANO DE CORTE
def fit_pieces(c, l):
    """Divide recursivamente até a peça caber na chapa (respeita AS DUAS dimensões)."""
    A, B = CH_C, CH_L
    out = []
    def rec(x, y):
        if (x <= A and y <= B) or (y <= A and x <= B):
            out.append((max(x, y), min(x, y))); return
        if x >= y: rec(x/2, y)
        else:      rec(x, y/2)
    rec(c, l); return out

def nest(items):
    """Empacotamento por prateleiras + piso de aproveitamento realista de 80%."""
    items = sorted(items, key=lambda p: -max(p))
    chapas, cur, used_h = 0, [], 0.0
    row_w, row_h = 0.0, 0.0
    for c, l in items:
        w, h = max(c, l), min(c, l)
        if row_w + w <= CH_C:
            row_w += w; row_h = max(row_h, h)
        else:
            used_h += row_h; row_w, row_h = w, h
            if used_h + row_h > CH_L:
                chapas += 1; used_h, row_w, row_h = 0.0, w, h
        cur.append((c, l))
    n_shelf = chapas + (1 if cur else 0)
    area = sum(c*l for c, l in items)/10000
    n_area = int(-(-area // (CH_AREA*0.80)))
    return max(n_shelf, n_area, 1)

# agrupa por material
por_mat = {}
for it, d, m, c, l, q in PECAS:
    for _ in range(q):
        for pc in fit_pieces(c, l):
            por_mat.setdefault(m, []).append(pc)

print('═'*74)
print('CASA L&M — PLANO DE CORTE POR MATERIAL')
print('═'*74)
custo_chapa = 0.0
chapas_por_mat = {}
for m in sorted(por_mat, key=lambda x: -sum(a*b for a, b in por_mat[x])):
    area = sum(a*b for a, b in por_mat[m])/10000
    n = nest(por_mat[m])
    chapas_por_mat[m] = n
    c = n*P[m]; custo_chapa += c
    print(f'  {m:7s} {area:7.2f} m²  →  {n:3d} chapas × R$ {P[m]:7.2f}  =  R$ {c:9,.2f}'
          f'   (aprov. {area/(n*CH_AREA)*100:4.1f}%)')
print(f'  {"":7s} {"":7s}      {sum(chapas_por_mat.values()):3d} chapas'
      f'{"":22s}R$ {custo_chapa:9,.2f}')

# ══════════════════════════════════════════════════════════ FITA DE BORDA
ml_nobre = ml_comum = 0.0
for it, d, m, c, l, q in PECAS:
    # regra Valvic: ~50% do perímetro recebe fita (faces aparentes)
    ml = 2*(c+l)/100*q*0.5
    if m in NOBRE: ml_nobre += ml
    else:          ml_comum += ml
ml_nobre *= 1.10; ml_comum *= 1.10
custo_fita = ml_nobre*FITA_NOBRE + ml_comum*FITA_COMUM
custo_filet = (ml_nobre+ml_comum)*FILETAGEM
print(f'\n  Fita nobre {ml_nobre:7.1f} m · fita comum {ml_comum:6.1f} m'
      f'  →  R$ {custo_fita:8,.2f}')
print(f'  Filetagem  {ml_nobre+ml_comum:7.1f} m × R$ {FILETAGEM:.2f}'
      f'{"":16s}→  R$ {custo_filet:8,.2f}')

# ═════════════════════════════════════════════════════════════ FERRAGENS
# dobradiças: 2 por porta até 1,50m · 3 até 2,20m · 4 acima
PORTAS = [
    ('2 Aéreo cozinha (L)', 8, 1.26), ('3 Armário cozinha (torre)', 4, 1.17),
    ('3 Armário cozinha (torre)', 2, 2.71), ('4 Despensa · armário alto', 8, 0.65),
    ('6 Despensa · piso-teto', 2, 2.86), ('8 Suíte · sapateira', 2, 2.72),
    ('11 Banho 01 (visita)', 2, 0.44), ('12 Banho 02 (Terezinha)', 2, 0.44),
    ('13 Banho 03 (Natalia/Gab)', 2, 0.44),
]
n_dobr = sum(q*(2 if h <= 1.5 else 3 if h <= 2.2 else 4) for _, q, h in PORTAS)
n_dobr += 2   # porta tempero
# [Jonathan 28/07] não existe corrediça OCULTA de 25 cm — as 13 bandejas da
# sapateira têm 24,5 cm de profundidade, então vão de telescópica.
GAVETAS_TELESC = (4 + 2 + 6 + 3 + 2 + 2 + 2 + 2 + 2   # cozinha/despensa/banheiros/lavabo
                  + 13)                                # + bandejas da sapateira
GAVETAS_OCULTA = 20 + 5 + 3                            # closet + piso-teto + banho suíte
n_prat_corr    = 6                                    # cozinha (telescópica)

# LED: sapateira 2,67m vertical · closet prateleiras iluminadas · aéreo cozinha
ml_led = 2.67 + (1.60*4 + 1.24*3 + 1.60*3) + (1.82 + 1.47)
# chapa perfurada — gaveta 4 da despensa (3 un): fundo + 2 faces longas + 2 curtas
m2_perf = 3 * (0.658*0.265 + 2*0.658*0.145 + 2*0.235*0.145)

FERR = [
    (f'Dobradiça Hettich Sensys Black',        n_dobr,          P_DOBR_BLACK),
    (f'Corrediça telescópica (par)',           GAVETAS_TELESC,  P_CORR_TELESC),
    (f'Corrediça oculta Hettich Quadro (par)', GAVETAS_OCULTA,  P_CORR_OCULTA),
    (f'Corrediça prateleira cozinha (par)',    n_prat_corr,     P_CORR_TELESC),
    (f'Conjunto pivotante + fechadura rolete', 1,               P_PIVO + P_FECH_ROLETE),
    (f'Puxador alça inox preto 60cm',          1,               P_PUX_ALCA_60),
    (f'Puxador metálico preto/grafite',        8,               P_PUX_METALICO),
    (f'Cava 45° usinada (peça)',               46,              P_CAVA_USINADA),
    (f'Cabideiro metal preto/grafite',         5,               P_CABIDEIRO),
    (f'Ganchos vassoura (conjunto)',           1,               P_GANCHOS),
    (f'Fita LED + perfil + lente ({ml_led:.1f} m)', 1,          ml_led*P_LED_M),
    (f'Chapa metálica perfurada 3mm ({m2_perf:.2f} m²)', 1,     m2_perf*P_PERFURADA_M2),
    (f'Portas vidro reflecta — Renolfh ({m2_vidro:.2f} m², 8 folhas)', 1, custo_vidro),
]
print('\n' + '═'*74)
print('FERRAGENS, ILUMINAÇÃO E TERCEIRIZADOS')
print('═'*74)
custo_ferr = 0.0
for nome, q, pu in FERR:
    v = q*pu; custo_ferr += v
    print(f'  {nome:52s} {q:4d} × {pu:8,.2f} = R$ {v:9,.2f}')
print(f'  {"TOTAL FERRAGENS":52s} {"":17s}R$ {custo_ferr:9,.2f}')

# ══════════════════════════════════════════════════════════════ CONSUMÍVEIS
consum = (custo_chapa + custo_fita)*0.06     # cola, cavilha, minifix, parafuso,
                                             # tinner, estopa, strech, cantoneira
print(f'\n  Consumíveis e embalagem (6% chapa+fita)          R$ {consum:9,.2f}')

# ═══════════════════════════════════════════════════════════════ MOTOR VALVIC
MAT = custo_chapa + custo_fita + custo_filet + custo_ferr + consum
LOGISTICA   = 2400.0    # Alphaville · 15 ambientes · 2 viagens de montagem
VISITA      = 900.0     # medição in loco (bancadas/quadro/sifões: várias conferências)
MONTAGEM_EX = 1800.0    # reorganizar módulos existentes da cozinha + remoção gaveta bege

fixedR = MAT + LOGISTICA + VISITA + MONTAGEM_EX

MC   = 0.37
a    = 0.162          # nf4 + parc8 + vend3 + erro0,5 + serra0,2 + manut0,5
liqF = 0.88
b    = 0.008 + 0.010 + 0.025 + 0.10     # prog + coord + marc + RT 10%
div  = 1 - a - liqF*b - MC
inv  = fixedR/div

print('\n' + '═'*74)
print('CUSTO E PREÇO — MC 37% · COM RT 10%')
print('═'*74)
print(f'  Chapas                                          R$ {custo_chapa:10,.2f}')
print(f'  Fita de borda + filetagem                       R$ {custo_fita+custo_filet:10,.2f}')
print(f'  Ferragens / LED / vidro / serralheria           R$ {custo_ferr:10,.2f}')
print(f'  Consumíveis                                     R$ {consum:10,.2f}')
print(f'  ── Subtotal material                            R$ {MAT:10,.2f}')
print(f'  Logística (Alphaville, 2 viagens)               R$ {LOGISTICA:10,.2f}')
print(f'  Visita técnica / medições in loco               R$ {VISITA:10,.2f}')
print(f'  Serviço sobre o existente (reorganizar/remover) R$ {MONTAGEM_EX:10,.2f}')
print(f'  ══ CUSTO DIRETO (fixedR)                        R$ {fixedR:10,.2f}')
print(f'  divisor = 1 − {a} − {liqF}×{b:.3f} − {MC} = {div:.5f}')
print(f'  ══ INVESTIMENTO                                 R$ {inv:10,.2f}')

# ═════════════════════════════════════════ ALOCAÇÃO POR ITEM (esforço produtivo)
esforco = {}
for it, d, m, c, l, q in PECAS:
    a_m2 = c*l/10000*q
    esforco[it] = esforco.get(it, 0) + a_m2/CH_AREA*P[m]
    esforco[it] += 2*(c+l)/100*q*0.5*(FITA_NOBRE if m in NOBRE else FITA_COMUM)
tot_esf = sum(esforco.values())

# ferragem específica por item (o que não pode ser rateado)
# A fita de LED é MUITO concentrada (14,92 dos 20,9 m estão no closet). Rateá-la
# pelo esforço de chapa jogaria custo do closet nos banheiros. Vai direto no item.
ml_led_closet = 1.60*4 + 1.24*3 + 1.60*3      # prateleiras iluminadas dos 3 corpos
ml_led_aereo  = 1.82 + 1.47                    # aéreo da cozinha
ml_led_sapat  = 2.67                           # vertical da sapateira

ESPEC = {
    '1 Painel sala jantar':      P_PIVO + P_FECH_ROLETE + P_PUX_ALCA_60,
    '2 Aéreo cozinha (L)':       ml_led_aereo*P_LED_M,
    '5 Despensa · armário baixo': m2_perf*P_PERFURADA_M2,
    '7 Suíte · roupeiro':        custo_vidro_roupeiro + 2*P_PUX_METALICO,
    '8 Suíte · sapateira':       13*P_CORR_TELESC + ml_led_sapat*P_LED_M,
    '9 Suíte · closet':          custo_vidro_closet
                                 + 20*P_CORR_OCULTA + 5*P_CABIDEIRO
                                 + 6*P_PUX_METALICO + ml_led_closet*P_LED_M,
}
spec_tot = sum(ESPEC.values())
resto = (fixedR - spec_tot)/div

print('\n' + '═'*74)
print('PREÇO POR ITEM')
print('═'*74)
tot = 0.0
for it in sorted(esforco):
    v = resto*esforco[it]/tot_esf + ESPEC.get(it, 0)/div
    tot += v
    print(f'  {it:32s} R$ {v:10,.2f}')
print(f'  {"TOTAL":32s} R$ {tot:10,.2f}')

# ══════════════════════════════════════════ ABERTURA DE CUSTO DE UM ITEM
ALVO = '9 Suíte · closet'
print('\n' + '═'*74)
print(f'ABERTURA DE CUSTO — {ALVO}')
print('═'*74)

# 1) chapas efetivamente consumidas pelo item (rateio por área dentro de cada material)
area_item, area_tot_mat = {}, {}
for it, d, m, c, l, q in PECAS:
    area_tot_mat[m] = area_tot_mat.get(m, 0) + c*l/10000*q
    if it == ALVO:
        area_item[m] = area_item.get(m, 0) + c*l/10000*q
chapa_item = 0.0
print('\n  CHAPAS')
for m in sorted(area_item, key=lambda x: -area_item[x]):
    frac = area_item[m]/area_tot_mat[m]
    ch   = chapas_por_mat[m]*frac
    v    = ch*P[m]; chapa_item += v
    print(f'    {m:7s} {area_item[m]:6.2f} m² de {area_tot_mat[m]:6.2f} '
          f'({frac*100:4.1f}% do material) → {ch:5.2f} chapas = R$ {v:8,.2f}')
print(f'    {"":7s} {"subtotal chapas":41s} R$ {chapa_item:8,.2f}')

# 2) fita + filetagem do item
mln = mlc = 0.0
for it, d, m, c, l, q in PECAS:
    if it != ALVO: continue
    ml = 2*(c+l)/100*q*0.5*1.10
    if m in NOBRE: mln += ml
    else:          mlc += ml
fita_item = mln*FITA_NOBRE + mlc*FITA_COMUM
filet_item = (mln+mlc)*FILETAGEM
print(f'\n  FITA E FILETAGEM')
print(f'    fita nobre {mln:6.1f} m × R$ {FITA_NOBRE:.2f}{"":18s} R$ {mln*FITA_NOBRE:8,.2f}')
print(f'    filetagem  {mln+mlc:6.1f} m × R$ {FILETAGEM:.2f}{"":18s} R$ {filet_item:8,.2f}')

# 3) ferragens e terceirizados diretos
print(f'\n  FERRAGENS E TERCEIRIZADOS (direto, sem rateio)')
DET = [
    ('Portas em vidro reflecta — Renolfh (6 folhas)', custo_vidro_closet),
    ('Corrediça oculta Hettich Quadro — 20 pares',    20*P_CORR_OCULTA),
    ('Fita LED 3000K/4000K + perfil (%.2f m)' % ml_led_closet, ml_led_closet*P_LED_M),
    ('Cabideiro em metal preto/grafite — 5 un',       5*P_CABIDEIRO),
    ('Puxador metálico cinza grafite — 6 un',         6*P_PUX_METALICO),
]
for n, v in DET: print(f'    {n:52s} R$ {v:8,.2f}')
print(f'    {"subtotal ferragens/terceirizados":52s} R$ {sum(v for _, v in DET):8,.2f}')

# 4) rateio dos custos gerais (consumíveis, logística, visita, serviço no existente)
share  = esforco[ALVO]/tot_esf
gerais = (consum + LOGISTICA + VISITA + MONTAGEM_EX)*share
print(f'\n  RATEIO DOS CUSTOS GERAIS  ({share*100:.1f}% do esforço de produção)')
for n, v in [('Consumíveis e embalagem', consum), ('Logística Alphaville', LOGISTICA),
             ('Visita técnica / medições', VISITA), ('Serviço sobre o existente', MONTAGEM_EX)]:
    print(f'    {n:52s} R$ {v*share:8,.2f}')

custo_item = chapa_item + fita_item + filet_item + sum(v for _, v in DET) + gerais
preco_item = resto*esforco[ALVO]/tot_esf + ESPEC.get(ALVO, 0)/div
print(f'\n  ══ CUSTO DIRETO DO ITEM                            R$ {custo_item:9,.2f}')
print(f'  ══ PREÇO AO CLIENTE                                R$ {preco_item:9,.2f}')
print(f'     markup = 1/{div:.5f} = {1/div:.3f}×   ·   margem embutida'
      f' R$ {preco_item-custo_item:9,.2f}')
