# -*- coding: utf-8 -*-
"""
TRT 3ª Região — Espaço de Convivência dos Desembargadores (via MLQ Engenharia)
GRUPO 16 — MARCENARIA (7 itens). Só marcenaria: portas prontas, bancadas de pedra
e persianas ficam com outros fornecedores (decisão Jonathan).

Medidas lidas do executivo (arq. Renata Lodi, 26/03/2026, esc. 1:25):
  pr.08 — cozinha: inferior 2x169 (prof 60, h70) · aéreo L 274+257 (prof 36, h96)
  pr.09 — buffet/lavatório: armário 7 mód. 54,3 · prateleira 4 tramos 93,7 · shaft 315x230
  pr.10 — armário alto 87x230x70 (escamoteável) · painel ripado 173x230 · painel L 492,5+266,5

DECISÕES: BDI fica com a MLQ (entregamos preço fechado) · shaft em MDF padrão fosco ·
espelhos FORA · COM RT · prazo 60-70 dias corridos · MC 45%.
"""

CH_A, CH_L = 2.75, 1.85
CH_AREA = CH_A * CH_L                       # 5,0875 m²

# ------------------------------------------------------------------ materiais
P = {
    'BRC15': 110.0,  # MDF Branco fosco 15mm                        chapas.md (melam. fosco)
    'BRC18': 125.0,  # MDF Branco fosco 18mm (prateleiras)          chapas.md
    'BRC6':   78.0,  # MDF Branco 6mm (fundos)                      chapas.md
    'FRJ15': 320.0,  # MDF Arauco Mad. Brasileiras LOURO FREIJÓ 15mm  [ESTIM. linha premium]
    'FRJ6':  190.0,  # idem 6mm (fundos aparentes)                    [ESTIM.]
    'MOSS15':260.0,  # MDF Duratex Unicolores MOSS 15mm               [ESTIM. linha cor]
    'PAD15': 110.0,  # MDF padrão fosco 15mm — SHAFT (decisão Jonathan)
}
FITA_COMUM = 3.0     # R$/m fita branca/padrão
FITA_NOBRE = 6.0     # R$/m fita Louro Freijó / MOSS               [ESTIM.]
FILETAGEM  = 2.5     # R$/m aplicação

# ferragens (referencias/ferragens.md + estimativas sinalizadas)
P_SENSYS      = 17.80   # dobradiça Hettich Sensys
P_CORREDICA   = 83.00   # corrediça Hettich Quadro V6 (par)
P_PUX_SLIM    = 30.00   # puxador slim inox 128mm preto (un)        [Jonathan 26/07]
P_ESCAMOT     = 6000.0  # sistema escamoteável + DOBRADIÇAS das portas do armário alto
                        #                                           [Jonathan 26/07]
P_FECHO_TOQUE = 22.00   # fecho-toque / push (un)                   [ESTIM.]
P_LED_M       = 55.00   # fita LED COB 15W/m 12V 3000K + perfil (R$/m) [ESTIM.]
P_GRELHA      = 380.0   # grelha ventilação inox 60cm preta (un)     [ESTIM.]

pecas = []   # (item, desc, material, C cm, L cm, qtd)
def add(it, d, mat, c, l, q=1): pecas.append((it, d, mat, c, l, q))

# ============================================================ 16.1 COZINHA
# MDF BRANCO · puxador slim inox 128 preto · caixa de gordura c/ acesso no sóculo
I = '16.1 Cozinha'
# --- inferior: 2 trechos de 169, h70, prof 60 → 8 portas de ~42,3
for t in (1, 2):
    add(I, f'Inf t{t} — laterais/divisórias', 'BRC15', 70, 60, 5)
    add(I, f'Inf t{t} — base e tampo estrutural', 'BRC15', 169, 60, 2)
    add(I, f'Inf t{t} — fundo', 'BRC6', 169, 70)
    add(I, f'Inf t{t} — portas (4x42,3)', 'BRC15', 68, 42.3, 4)
    add(I, f'Inf t{t} — prateleira interna', 'BRC18', 41, 55, 4)
    add(I, f'Inf t{t} — sóculo', 'BRC15', 169, 12)
# --- aéreo em L: 274 (6 mód. 45,7) + 257 (5 mód. 51,4), h96, prof 36
for nome, comp, nmod, larg in (('A', 274, 6, 45.7), ('B', 257, 5, 51.4)):
    add(I, f'Aéreo {nome} — laterais/divisórias', 'BRC15', 96, 36, nmod + 1)
    add(I, f'Aéreo {nome} — tampo/base', 'BRC15', comp, 36, 2)
    add(I, f'Aéreo {nome} — fundo', 'BRC6', comp, 96)
    add(I, f'Aéreo {nome} — portas', 'BRC15', 94, larg, nmod)
    add(I, f'Aéreo {nome} — 2 prateleiras int.', 'BRC18', larg - 3, 33, nmod * 2)
# --- prateleira suspensa (prof 48,4)
add(I, 'Prateleira suspensa', 'BRC18', 130, 48.4)

# ============================================================ 16.2 BUFFET armário
# MDF Duratex Unicolores MOSS · vão inferior p/ ventilação da pista fria
I = '16.2 Buffet armário'
add(I, 'Laterais/divisórias', 'MOSS15', 75, 61, 8)
add(I, 'Base e tampo estrutural', 'MOSS15', 372, 61, 2)
add(I, 'Fundo', 'BRC6', 372, 75)
add(I, 'Portas (7 mód. 54,3)', 'MOSS15', 73, 54.3, 7)
add(I, 'Prateleira interna', 'BRC18', 53, 57, 7)
add(I, 'Sóculo c/ vão de ventilação (pista fria)', 'MOSS15', 372, 12)

# ============================================================ 16.3 BUFFET prateleira
# MDF Louro Freijó + LED contínua
I = '16.3 Buffet prateleira'
add(I, 'Prateleira (4 tramos 93,7)', 'FRJ15', 93.7, 45.4, 4)
add(I, 'Testeira/fechamento frontal (esconde LED)', 'FRJ15', 93.7, 8, 4)
ML_LED_BUFFET = 3.75

# ============================================================ 16.4 ARMÁRIO ALTO
# MDF Louro Freijó · 87x230x70 · porta frontal girar+correr ESCAMOTEÁVEL + porta traseira giro
I = '16.4 Armário alto'
add(I, 'Laterais', 'FRJ15', 230, 70, 2)
add(I, 'Tampo/base', 'FRJ15', 84, 70, 2)
add(I, 'Fundo', 'FRJ6', 84, 230)
add(I, 'Prateleiras internas', 'BRC18', 82, 66, 4)
add(I, 'Divisória horizontal (parte inf. cega)', 'FRJ15', 84, 66)
add(I, 'Porta frontal escamoteável (2 folhas 42)', 'FRJ15', 157, 42, 2)
add(I, 'Porta frontal inferior cega', 'FRJ15', 71, 84)
add(I, 'Porta traseira de giro', 'FRJ15', 157, 84)

# ============================================================ 16.5 PAINEL RIPADO
# MDF Louro Freijó · 173x230 · ripas verticais 5,5cm
I = '16.5 Painel ripado'
add(I, 'Base do painel', 'FRJ15', 230, 173)
RIPA_L, PASSO = 5.5, 7.5                 # ripa 5,5 + vão 2,0
n_ripas = int(173 // PASSO)
add(I, f'Ripas verticais ({n_ripas} un)', 'FRJ15', 226, RIPA_L, n_ripas)
add(I, 'Travessas sup. e inf. de fixação', 'FRJ15', 173, 8, 2)

# ============================================================ 16.6 PAINEL SHAFT
# MDF PADRÃO FOSCO (decisão Jonathan) · 315x230 · portas fecho-toque
I = '16.6 Painel shaft'
add(I, 'Base/estrutura do painel', 'PAD15', 230, 315)
add(I, 'Portas fecho-toque (4 mód. 78,8)', 'PAD15', 226, 78.8, 4)
add(I, 'Montantes/travessas', 'PAD15', 230, 8, 5)

# ============================================================ 16.7 PAINEL DESCANSO
# MDF Louro Freijó · L: 492,5 (4 mód. 123,1) + 266,5 · h230 · friso 1x1 · cantoneira L preta
I = '16.7 Painel descanso'
add(I, 'Painel trecho A (492,5)', 'FRJ15', 230, 492.5)
add(I, 'Painel trecho B (266,5)', 'FRJ15', 230, 266.5)
add(I, 'Fechamento lateral recuado', 'FRJ15', 230, 20, 2)
add(I, 'Montantes de reforço', 'BRC15', 230, 10, 8)

# ===================================================================== NESTING
def fit_pieces(c, l):
    """Divide a peça até que TODA parte caiba em 275x185 (ambas as dimensões)."""
    A, B = CH_A*100, CH_L*100          # 275 x 185
    out = []
    def rec(x, y):
        if (x <= A and y <= B) or (y <= A and x <= B):
            out.append((max(x, y), min(x, y))); return
        # divide a maior dimensão que estoura
        if x >= y: rec(x/2, y)
        else:      rec(x, y/2)
    rec(c, l)
    return out

def nest(items):
    """Empacota em faixas: cada faixa tem altura = maior 'b'; soma de faixas <= 185."""
    A, B = CH_A*100, CH_L*100
    pcs = []
    for c, l in items:
        pcs.extend(fit_pieces(c, l))
    pcs.sort(key=lambda p: (-p[1], -p[0]))   # por altura desc
    faixas = []
    for a, b in pcs:
        posto = False
        for f in faixas:
            if f['h'] >= b and f['rest'] >= a:
                f['rest'] -= a; posto = True; break
        if not posto:
            faixas.append({'h': b, 'rest': A - a})
    # agrupa faixas em chapas (soma das alturas <= 185)
    hs = sorted([f['h'] for f in faixas], reverse=True)
    chapas, cur = 0, 0.0
    for h in hs:
        if cur + h <= B: cur += h
        else: chapas += 1; cur = h
    n_shelf = max(1, chapas + (1 if cur else 0))
    # piso realista: o shelf-packing acima é otimista (assume encaixe perfeito).
    # Nenhum corte real passa de ~80% de aproveitamento -> usa o maior dos dois.
    area = sum(c*l for c, l in items)/10000
    n_area = int(-(-area // (CH_AREA*0.80)))
    return max(n_shelf, n_area, 1)

from collections import defaultdict
por_mat = defaultdict(list)
for it, d, mat, c, l, q in pecas:
    for _ in range(int(q)): por_mat[mat].append((c, l))

NOME = {'BRC15':'MDF Branco fosco 15mm','BRC18':'MDF Branco fosco 18mm','BRC6':'MDF Branco 6mm (fundos)',
        'FRJ15':'MDF Arauco LOURO FREIJÓ 15mm','FRJ6':'MDF Louro Freijó 6mm','MOSS15':'MDF Duratex MOSS 15mm',
        'PAD15':'MDF padrão fosco 15mm (shaft)'}

print('='*82); print('TRT 3ª REGIÃO — GRUPO 16 MARCENARIA — QUANTITATIVO'); print('='*82)
print('\n1) PLANO DE CORTE (nesting real, chapa 275x185)')
print('-'*82)
tot_ch, custo_ch = 0, 0.0
for mat in ['BRC15','BRC18','BRC6','FRJ15','FRJ6','MOSS15','PAD15']:
    if mat not in por_mat: continue
    its = por_mat[mat]
    area = sum(c*l for c, l in its)/10000
    n = nest(its)
    tot_ch += n; custo_ch += n*P[mat]
    print(f'{NOME[mat]:<34} {len(its):>3} pç · {area:>6.2f} m² · **{n:>2} chapas** · R$ {n*P[mat]:>9,.2f}')
print(f'\nTOTAL: {tot_ch} chapas   |   R$ {custo_ch:,.2f}')

# ------------------------------------------------------------------ fita
def perim(mats):
    return sum(2*(c+l)/100*q for it, d, mat, c, l, q in pecas if mat in mats)
fita_nobre = (perim(['FRJ15','FRJ6','MOSS15']))*0.55
fita_comum = (perim(['BRC15','BRC18','PAD15']))*0.5
custo_fita = fita_nobre*FITA_NOBRE + fita_comum*FITA_COMUM
custo_filet = (fita_nobre+fita_comum)*FILETAGEM
print(f'\n2) FITA DE BORDA')
print('-'*82)
print(f'Fita nobre (Freijó/MOSS) ...... {fita_nobre:>7.1f} m x R$ {FITA_NOBRE:.2f} = R$ {fita_nobre*FITA_NOBRE:>9,.2f}')
print(f'Fita comum (branco/padrão) .... {fita_comum:>7.1f} m x R$ {FITA_COMUM:.2f} = R$ {fita_comum*FITA_COMUM:>9,.2f}')
print(f'Filetagem ..................... {fita_nobre+fita_comum:>7.1f} m x R$ {FILETAGEM:.2f} = R$ {custo_filet:>9,.2f}')

# ------------------------------------------------------------------ ferragens
print(f'\n3) FERRAGENS E INSUMOS')
print('-'*82)
n_portas_coz  = 8 + 11            # inferior + aéreo
n_portas_buf  = 7
n_portas_alto = 2 + 1 + 1         # escamoteável(2) + inf cega + traseira
n_portas_shaft= 4
# armário alto NÃO entra: suas dobradiças já estão no pacote de R$ 6.000
n_dobr = (n_portas_coz + n_portas_buf)*2 + n_portas_shaft*2
n_pux  = n_portas_coz + n_portas_buf + 2   # slim inox 128 preto (shaft = fecho-toque, sem puxador)
ml_led = ML_LED_BUFFET
ferr = [
    (f'Dobradiça Hettich Sensys ({n_dobr} un)', n_dobr*P_SENSYS),
    (f'Puxador slim inox 128mm preto ({n_pux} un)', n_pux*P_PUX_SLIM),
    (f'Sistema escamoteável + dobradiças do armário alto', P_ESCAMOT),
    (f'Fecho-toque shaft ({n_portas_shaft} un) [ESTIM.]', n_portas_shaft*P_FECHO_TOQUE),
    (f'Fita LED COB 3000K + perfil ({ml_led:.2f} m) [ESTIM.]', ml_led*P_LED_M),
    (f'Grelha ventilação inox 60cm preta (1 un) [ESTIM.]', P_GRELHA),
    (f'Corrediças Hettich (2 pares, gavetas cozinha)', 2*P_CORREDICA),
]
custo_ferr = sum(v for _, v in ferr)
for n, v in ferr: print(f'   {n:<58} R$ {v:>9,.2f}')

# ------------------------------------------------------------------ resumo
material = custo_ch + custo_fita + custo_filet + custo_ferr
logistica = 1200.0    # obra em prédio público, 10º andar, acesso controlado
visita    =  600.0    # medição + compatibilização com a MLQ
montagem_extra = 900.0  # içamento/elevador de serviço, horário restrito de obra pública
fixedR = material + logistica + visita + montagem_extra

print(f'\n4) CUSTO DIRETO')
print('-'*82)
print(f'   Chapas ..................................... R$ {custo_ch:>10,.2f}')
print(f'   Fita + filetagem ........................... R$ {custo_fita+custo_filet:>10,.2f}')
print(f'   Ferragens e insumos ........................ R$ {custo_ferr:>10,.2f}')
print(f'   SUBTOTAL MATERIAL .......................... R$ {material:>10,.2f}')
print(f'   Logística .................................. R$ {logistica:>10,.2f}')
print(f'   Visita técnica / compatibilização .......... R$ {visita:>10,.2f}')
print(f'   Acesso de obra (içamento/horário) .......... R$ {montagem_extra:>10,.2f}')
print(f'   CUSTO DIRETO (fixedR) ...................... R$ {fixedR:>10,.2f}')

# ------------------------------------------------------------------ motor
NF, PARC, VEND, ERRO, SERRA, MANUT = 0.04, 0.08, 0.03, 0.005, 0.002, 0.005
a = NF+PARC+VEND+ERRO+SERRA+MANUT
liqF = 1-(NF+PARC)
PROG, COORD, MARC, RT = 0.008, 0.01, 0.025, 0.10      # *** COM RT 10% ***
b = PROG+COORD+MARC+RT
MC = 0.45
div = 1 - a - liqF*b - MC
inv = fixedR/div

print(f'\n5) PRECIFICAÇÃO — MC {MC*100:.0f}% · **COM RT {RT*100:.0f}%**')
print('-'*82)
print(f'   a={a*100:.1f}%  liqF={liqF:.2f}  b={b*100:.1f}% (prog .8 + coord 1 + marc 2,5 + RT 10)  mc={MC*100:.0f}%')
print(f'   Divisor: 1 - {a:.3f} - {liqF:.2f}x{b:.3f} - {MC:.2f} = {div:.5f}')
print(f'   >>> INVESTIMENTO TOTAL ..................... R$ {inv:>10,.2f}')
print(f'   RT embutida (10% do líquido) ............... R$ {inv*liqF*RT:>10,.2f}')

# ---------------------------------------------------------------- alocação
# Rateio em duas camadas (senão a ferragem de R$6k distorce tudo):
#   (a) ferragem ESPECÍFICA de cada item entra direto, com o mesmo markup;
#   (b) todo o resto (chapa, fita, dobradiças gerais, logística, mão de obra)
#       é rateado pelo ESFORÇO DE PRODUÇÃO — proxy = chapa + fita de cada item.
print(f'\n6) ALOCAÇÃO POR ITEM DA PLANILHA (grupo 16)')
print('-'*82)
ESPEC = {
    '16.1 Cozinha':          P_GRELHA + 19*P_PUX_SLIM + 2*P_CORREDICA,
    '16.2 Buffet armário':   7*P_PUX_SLIM,
    '16.3 Buffet prateleira': ml_led*P_LED_M,
    '16.4 Armário alto':     P_ESCAMOT + 2*P_PUX_SLIM,
    '16.6 Painel shaft':     n_portas_shaft*P_FECHO_TOQUE,
}
esforco = defaultdict(float)
for it, d, mat, c, l, q in pecas:
    a = c*l*q/10000
    esforco[it] += a/CH_AREA*P[mat]                      # chapa
    esforco[it] += 2*(c+l)/100*q*0.5*(FITA_NOBRE if mat in ('FRJ15','FRJ6','MOSS15') else FITA_COMUM)
tot_esf = sum(esforco.values())
spec_tot = sum(ESPEC.values())
resto = (fixedR - spec_tot)/div                          # bolo a ratear, já com markup
print(f'   (ferragem específica: R$ {spec_tot:,.2f} · rateio de produção sobre o restante)')
soma = 0.0
for it in sorted(esforco):
    v = resto*esforco[it]/tot_esf + ESPEC.get(it, 0)/div
    soma += v
    esp = f"  [inclui ferragem própria R$ {ESPEC[it]/div:,.0f}]" if it in ESPEC else ''
    print(f'   {it:<26} R$ {v:>10,.2f}{esp}')
print(f'   {"TOTAL":<26} R$ {soma:>10,.2f}')
print(f'\n   MC verificada {MC*100:.1f}% · RT {RT*100:.0f}% · prazo 60–70 dias corridos.')
