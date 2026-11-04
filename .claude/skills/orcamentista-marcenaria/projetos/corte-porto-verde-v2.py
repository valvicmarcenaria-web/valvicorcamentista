# -*- coding: utf-8 -*-
"""
PORTO VERDE (Leonardo) — escritório · ORÇAMENTO V2
Base: 5 renders + planta humanizada (28/07/2026). Substitui a V1 de 22/07 (R$ 62.400),
que fora construída sobre uma única imagem de referência.

⚠️ SEM PROJETO EXECUTIVO COTADO. Todas as medidas abaixo são LEITURA DE RENDER,
   declaradas item a item para conferência. Não são cotas de projeto.

DIRETRIZES [Jonathan 28/07]
  · Esquadria de alumínio e vidros FORA do escopo (divisórias, portas de vidro) —
    mencionar explicitamente na proposta.
  · Materiais A DEFINIR · NÃO contempla a linha Acetinato.
  · Portas altas com ABERTURA TOUCH (sem puxador).
  · Prateleiras da estante: estrutura de serralheria R$ 400 + vidro incolor temperado.
  · Mesa de trabalho central com 2 gaveteiros volantes de 3 gavetas cada.
  · Porta do banheiro mimetizada no painel · painel da sala de reunião também mimetizado.
  · 3 prateleiras aéreas 20 × 150 com suporte oculto na sala de reunião.
  · Mesa da sala de reunião: custo R$ 8.500 (tampo MDF melamínico fosco + base cônica
    laqueada) — EXPOSTA À PARTE na proposta.
"""

CH_C, CH_L = 275.0, 185.0
CH_AREA = (CH_C/100)*(CH_L/100)

# ─────────────────────────────────────────────── preços de chapa (melamínico fosco)
P = {'CAR15':500.0,'CAR18':600.0,'CAR6':300.0,     # amadeirado carvalho
     'BRC15':500.0,'BRC18':600.0,'BRC6':300.0,     # branco/cinza claro fosco
     'CRU15':260.0}                                # miolo não aparente
NOBRE = ('CAR15','CAR18','CAR6','BRC15','BRC18','BRC6')
FITA_COMUM, FITA_NOBRE, FILETAGEM = 2.0, 3.0, 2.5

# ─────────────────────────────────────────────────────────────────── ferragens
P_DOBR        = 40.00     # Hettich Sensys Black
P_TOUCH       = 100.00    # pulsador Blum Tip-on — abertura touch das portas altas
P_CORR_OCULTA = 120.00    # par
P_CORR_TELESC = 40.00     # par
P_CAVA        = 50.00     # peça — cava usinada
P_LED_M       = 150.00    # fita + perfil + lente, por metro
P_PIVO        = 120.00
P_SUP_OCULTO  = 60.00     # metalon + flange por prateleira aérea
P_RODIZIO     = 25.00     # jogo por gaveteiro volante
P_SERRALHERIA_ESTANTE = 400.00    # [Jonathan] estrutura da estante
P_VIDRO_TEMP_M2       = 250.00    # incolor temperado 8mm
CUSTO_MESA_REUNIAO    = 8500.00   # [Jonathan] tampo + base cônica laqueada

PECAS = []
def add(item, desc, mat, c, l, q=1):
    PECAS.append((item, desc, mat, float(c), float(l), int(q)))

def caixa(item, nome, mat, larg, alt, prof, n_prat=0, prat18=False):
    add(item, f'{nome} · lateral',    mat, alt,  prof, 2)
    add(item, f'{nome} · base/tampo', mat, larg, prof, 2)
    add(item, f'{nome} · fundo',      mat[:3]+'6', larg, alt, 1)
    if n_prat:
        mp = (mat[:3]+'18') if (prat18 or larg > 70) else mat
        add(item, f'{nome} · prateleira', mp, larg, prof, n_prat)

def gaveta(item, nome, mat, larg, prof, alt, q=1):
    add(item, f'{nome} · frente',       mat, larg, alt, q)
    add(item, f'{nome} · contrafrente', mat, larg-3, alt-3, q)
    add(item, f'{nome} · lateral',      mat, prof, alt-3, 2*q)
    add(item, f'{nome} · traseira',     mat, larg-3, alt-3, q)
    add(item, f'{nome} · base',         mat[:3]+'6', larg-3, prof, q)

# ══════════════════════ 1. ARMÁRIO PISO-TETO + COPA  (parede de fundo)
# LEITURA: extensão 600 · altura 270 · prof 60 · nicho de copa iluminado 210 × 60
I = '1 Armário piso-teto + copa'
caixa(I, 'torre esquerda', 'BRC15', 210, 270, 60, n_prat=4, prat18=True)
caixa(I, 'torre direita',  'BRC15', 180, 270, 60, n_prat=4, prat18=True)
add(I, 'divisória vertical', 'BRC15', 270, 60, 4)
# portas altas com abertura touch — 8 folhas de ~70 × 200
add(I, 'porta alta touch', 'BRC15', 70, 200, 8)
# nicho da copa: fundo e bancada em amadeirado, com LED de testeira
add(I, 'nicho copa · fundo',   'CAR15', 210, 60, 1)
add(I, 'nicho copa · bancada', 'CAR18', 210, 60, 1)
add(I, 'nicho copa · testeira LED', 'BRC15', 210, 12, 1)
# balcão inferior sob o nicho: 4 gavetas + 2 portas
gaveta(I, 'gaveta balcão', 'BRC15', 52, 55, 20, q=4)
add(I, 'porta balcão', 'BRC15', 52, 75, 2)
add(I, 'sóculo', 'CRU15', 600, 10, 2)

# ══════════════════════ 2. PAINÉIS AMADEIRADOS  (parede, teto e mimetizados)
# LEITURA: painel lateral 220×270 · painel sala de reunião 320×270 (porta mimetizada)
#          painel do banheiro 160×270 (porta mimetizada) · faixa de teto 600×80
I = '2 Painéis amadeirados'
add(I, 'painel lateral',              'CAR15', 220, 270, 1)
add(I, 'painel sala reunião',         'CAR15', 320, 270, 1)
add(I, 'painel banheiro',             'CAR15', 160, 270, 1)
add(I, 'faixa de teto',               'CAR15', 600, 80, 1)
add(I, 'sarrafo de fixação',          'CRU15', 270, 8, 26)
# duas portas mimetizadas — folha 90 × 230, batente e travessas
add(I, 'porta mimetizada · folha',    'CAR15', 90, 230, 2)
add(I, 'porta mimetizada · batente',  'CAR15', 230, 12, 4)
add(I, 'porta mimetizada · verga',    'CAR15', 90, 12, 2)

# ══════════════════════ 3. MESA DE TRABALHO CENTRAL  (6 estações)
# LEITURA: 300 × 160 · divisória central 300 × 35 · 2 gaveteiros volantes 3 gavetas
I = '3 Mesa de trabalho central'
add(I, 'tampo',              'BRC18', 300, 80, 2)
add(I, 'divisória central',  'BRC18', 300, 35, 1)
add(I, 'saia/estrutura',     'BRC15', 300, 25, 2)
add(I, 'pé/apoio',           'BRC15', 72, 70, 4)
for n in ('volante A', 'volante B'):
    caixa(I, n, 'BRC15', 40, 60, 50)
    gaveta(I, f'{n} · gaveta', 'BRC15', 40, 48, 18, q=3)

# ══════════════════════ 4. BANCADA LATERAL  (estação junto à janela)
# LEITURA: 220 × 50 · prateleira suspensa acima
I = '4 Bancada lateral'
add(I, 'tampo',        'BRC18', 220, 50, 1)
add(I, 'saia',         'BRC15', 220, 20, 1)
add(I, 'lateral/apoio','BRC15', 72, 50, 2)
add(I, 'prateleira suspensa', 'CAR18', 220, 25, 1)

# ══════════════════════ 5. ESTANTE — SERRALHERIA + VIDRO
# LEITURA: 4 prateleiras de 100 × 30 em vidro incolor temperado, estrutura metálica preta
I = '5 Estante serralheria + vidro'
m2_vidro_estante = 4*(1.00*0.30)
add(I, 'testeira de arremate', 'CAR15', 100, 10, 1)   # único item de marcenaria

# ══════════════════════ 6. PRATELEIRAS AÉREAS — SALA DE REUNIÃO
# [Jonathan] 3 un de aprox. 20 × 150, com suporte oculto
I = '6 Prateleiras aéreas · reunião'
add(I, 'prateleira 20×150', 'CAR18', 150, 20, 3)

# ═══════════════════════════════════════════════════════ PLANO DE CORTE
def fit_pieces(c, l):
    A, B = CH_C, CH_L
    out = []
    def rec(x, y):
        if (x <= A and y <= B) or (y <= A and x <= B):
            out.append((max(x,y), min(x,y))); return
        if x >= y: rec(x/2, y)
        else:      rec(x, y/2)
    rec(c, l); return out

def nest(items):
    items = sorted(items, key=lambda p: -max(p))
    chapas, cur, used_h, row_w, row_h = 0, [], 0.0, 0.0, 0.0
    for c, l in items:
        w, h = max(c,l), min(c,l)
        if row_w + w <= CH_C:
            row_w += w; row_h = max(row_h, h)
        else:
            used_h += row_h; row_w, row_h = w, h
            if used_h + row_h > CH_L:
                chapas += 1; used_h, row_w, row_h = 0.0, w, h
        cur.append((c,l))
    n_shelf = chapas + (1 if cur else 0)
    area = sum(c*l for c,l in items)/10000
    return max(n_shelf, int(-(-area // (CH_AREA*0.80))), 1)

por_mat = {}
for it, d, m, c, l, q in PECAS:
    for _ in range(q):
        for pc in fit_pieces(c, l):
            por_mat.setdefault(m, []).append(pc)

print('═'*76); print('PORTO VERDE V2 — PLANO DE CORTE'); print('═'*76)
custo_chapa = 0.0; chapas_por_mat = {}
for m in sorted(por_mat, key=lambda x: -sum(a*b for a,b in por_mat[x])):
    area = sum(a*b for a,b in por_mat[m])/10000
    n = nest(por_mat[m]); chapas_por_mat[m] = n
    c = n*P[m]; custo_chapa += c
    print(f'  {m:6s} {area:6.2f} m² → {n:3d} chapas × R$ {P[m]:6.2f} = R$ {c:8,.2f}  '
          f'(aprov. {area/(n*CH_AREA)*100:4.1f}%)')
print(f'  {"":6s} {"":6s}   {sum(chapas_por_mat.values()):3d} chapas'
      f'{"":21s}R$ {custo_chapa:8,.2f}')

ml_n = ml_c = 0.0
for it, d, m, c, l, q in PECAS:
    ml = 2*(c+l)/100*q*0.5*1.10
    if m in NOBRE: ml_n += ml
    else:          ml_c += ml
custo_fita  = ml_n*FITA_NOBRE + ml_c*FITA_COMUM
custo_filet = (ml_n+ml_c)*FILETAGEM
print(f'\n  Fita {ml_n:6.1f} m nobre + {ml_c:5.1f} m comum → R$ {custo_fita:8,.2f}'
      f'   ·   filetagem R$ {custo_filet:8,.2f}')

# ══════════════════════════════════════════════════════════════ FERRAGENS
n_touch  = 8                      # portas altas da parede de fundo
n_dobr   = 8*2 + 2*2 + 2*3        # portas altas + balcão + portas mimetizadas
n_gav_oc = 6                      # gaveteiros volantes (3+3)
n_gav_tl = 4                      # gavetas do balcão da copa
ml_led   = 2.10 + 1.50            # nicho da copa + prateleira da bancada lateral

FERR = [
    ('Pulsador touch (portas altas)',            n_touch,  P_TOUCH),
    ('Dobradiça Hettich Sensys Black',           n_dobr,   P_DOBR),
    ('Corrediça oculta (gaveteiros volantes)',   n_gav_oc, P_CORR_OCULTA),
    ('Corrediça telescópica (balcão copa)',      n_gav_tl, P_CORR_TELESC),
    ('Rodízio p/ gaveteiro volante (jogo)',      2,        P_RODIZIO),
    ('Suporte oculto — prateleira aérea',        3,        P_SUP_OCULTO),
    ('Cava usinada',                             8,        P_CAVA),
    ('Conjunto pivotante (portas mimetizadas)',  2,        P_PIVO),
    (f'Fita LED + perfil ({ml_led:.1f} m)',      1,        ml_led*P_LED_M),
    ('Serralheria — estrutura da estante',       1,        P_SERRALHERIA_ESTANTE),
    (f'Vidro incolor temperado ({m2_vidro_estante:.2f} m²)', 1, m2_vidro_estante*P_VIDRO_TEMP_M2),
]
print('\n' + '═'*76); print('FERRAGENS E TERCEIRIZADOS'); print('═'*76)
custo_ferr = 0.0
for n_, q, pu in FERR:
    v = q*pu; custo_ferr += v
    print(f'  {n_:46s} {q:3d} × {pu:8,.2f} = R$ {v:8,.2f}')
print(f'  {"TOTAL FERRAGENS":46s} {"":17s}R$ {custo_ferr:8,.2f}')

consum = (custo_chapa + custo_fita)*0.06
MAT = custo_chapa + custo_fita + custo_filet + custo_ferr + consum
LOGISTICA, VISITA, INSTALACAO = 1200.0, 600.0, 900.0
fixedR = MAT + LOGISTICA + VISITA + INSTALACAO

MC, a, liqF = 0.37, 0.162, 0.88
b   = 0.008 + 0.010 + 0.025 + 0.10        # prog + coord + marc + RT 10%
div = 1 - a - liqF*b - MC

print('\n' + '═'*76); print('CUSTO E PREÇO — MC 37% · COM RT 10%'); print('═'*76)
print(f'  Chapas                                       R$ {custo_chapa:9,.2f}')
print(f'  Fita + filetagem                             R$ {custo_fita+custo_filet:9,.2f}')
print(f'  Ferragens / LED / serralheria / vidro        R$ {custo_ferr:9,.2f}')
print(f'  Consumíveis (6%)                             R$ {consum:9,.2f}')
print(f'  Logística · visita · instalação              R$ {LOGISTICA+VISITA+INSTALACAO:9,.2f}')
print(f'  ══ CUSTO DIRETO (marcenaria)                 R$ {fixedR:9,.2f}')
print(f'  divisor {div:.5f}')
print(f'  ══ MARCENARIA                                R$ {fixedR/div:9,.2f}')
print(f'  + Mesa da sala de reunião (custo {CUSTO_MESA_REUNIAO:,.0f})   R$ '
      f'{CUSTO_MESA_REUNIAO/div:9,.2f}')
print(f'  ══ TOTAL                                     R$ {(fixedR+CUSTO_MESA_REUNIAO)/div:9,.2f}')

# ═══════════════════════════════════════════════ PREÇO POR FRENTE
esforco = {}
for it, d, m, c, l, q in PECAS:
    esforco[it] = esforco.get(it, 0) + (c*l/10000*q)/CH_AREA*P[m]
    esforco[it] += 2*(c+l)/100*q*0.5*(FITA_NOBRE if m in NOBRE else FITA_COMUM)
tot_esf = sum(esforco.values())

ESPEC = {
    '1 Armário piso-teto + copa':    n_touch*P_TOUCH + 2.10*P_LED_M,
    '2 Painéis amadeirados':         2*P_PIVO,
    '3 Mesa de trabalho central':    n_gav_oc*P_CORR_OCULTA + 2*P_RODIZIO,
    '5 Estante serralheria + vidro': P_SERRALHERIA_ESTANTE + m2_vidro_estante*P_VIDRO_TEMP_M2,
    '6 Prateleiras aéreas · reunião': 3*P_SUP_OCULTO,
}
spec = sum(ESPEC.values())
resto = (fixedR - spec)/div

print('\n' + '═'*76); print('PREÇO POR FRENTE'); print('═'*76)
tot = 0.0
for it in sorted(esforco):
    v = resto*esforco[it]/tot_esf + ESPEC.get(it, 0)/div
    tot += v
    print(f'  {it:34s} R$ {v:9,.2f}')
print(f'  {"7 Mesa da sala de reunião":34s} R$ {CUSTO_MESA_REUNIAO/div:9,.2f}')
print(f'  {"TOTAL":34s} R$ {tot + CUSTO_MESA_REUNIAO/div:9,.2f}')
print(f'\n  À vista (−10%)                     R$ {(tot + CUSTO_MESA_REUNIAO/div)*0.9:9,.2f}')
