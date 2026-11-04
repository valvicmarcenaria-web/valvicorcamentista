# -*- coding: utf-8 -*-
# LEVANTAMENTO PECA-A-PECA — GRACA / arq. Lais Teles. Conta aberta (cotas do caderno, em cm).
# Regra da casa: cada peca L x A -> area; soma por (material, espessura); chapas = area / (5,0875 * aprov).
# Construcao Valvic: PROJETO TODO EM AZUL PETROLEO GUARARAPES — nao ha nada em Branco TX.
#   face/portas/gavetoes/tampo/prat = cor 15/18mm; caixaria interna e fundos tambem em Azul (6/15mm).
#   Como tudo e a mesma cor, o nesting e UNIFICADO no projeto inteiro (pilhas de 15 e de 6mm somadas) -> menos chapa.
# CALCULAR, nunca ESTIMAR: onde falta cota, assumo e SINALIZO (flags do caderno).
CHAPA = 2.75 * 1.85  # 5.0875 m2
APROV = {15: 0.82, 18: 0.82, 6: 0.55}
PRC = {('cor', 15): 500, ('cor', 18): 600, ('cor', 6): 300}
COR = {'Azul': 'cor'}   # projeto 100% Azul Petroleo Guararapes

tal = {}; log = []; CUR = [None]; amb_area = {}
def amb(name): CUR[0] = name; amb_area.setdefault(name, {})
def add(mat, esp, w, h, n=1, lab=''):
    if mat == 'Branco': mat = 'Azul'   # projeto todo Azul: caixaria interna e fundos tambem em Azul Petroleo
    a = (w/100.0) * (h/100.0) * n
    tal[(mat, esp)] = tal.get((mat, esp), 0) + a
    d = amb_area[CUR[0]]; d[(mat, esp)] = d.get((mat, esp), 0) + a
    log.append((CUR[0], lab, mat, esp, w, h, n, round(a, 3)))

# gavetao/gaveta padrao Valvic: frente COR18 + 2 lat Branco15 + contrafrente Branco15 + fundo Branco6
def gaveta(lab, lg, ag, prof):
    add('Azul', 18, lg, ag, 1, lab+' frente')
    add('Branco', 15, prof, ag, 2, lab+' lat')
    add('Branco', 15, lg, ag, 1, lab+' contraf')
    add('Branco', 6, lg, prof, 1, lab+' fundo')

# ==================================================================== DESPENSA
amb("Despensa")

# ---- B1: ARMARIO SUPERIOR (EXISTENTE -> REVESTIR). 163 L x 247 A ; prof 50 (principal) + 18 (rasa esq.)
#      Escopo Valvic = novas FRENTES + laterais aparentes + prateleiras + nicho alto. (Nao refaz a caixa: ja existe.)
# Frentes (porta de giro), Azul 18:
add('Azul', 18, 42, 124, 2, 'B1 portas giro 42x124')          # 2 portas do compartimento de prateleiras
add('Azul', 18, 45, 124, 1, 'B1 porta esq (secao rasa 18cm)') # porta esquerda
add('Azul', 18, 34, 245, 1, 'B1 porta cheia dir (coluna 245)')# coluna alta (nicho 30x196 + 2 pistoes)
# Laterais aparentes revestidas, Azul 15: lado dir. 50 prof x 247 ; lado esq. escalonado (50 base + 18 topo) ~ conto 50x247
add('Azul', 15, 50, 247, 2, 'B1 laterais aparentes 50x247')
# Tampo aparente (Azul 15) + base (Branco 15)
add('Azul', 15, 163, 50, 1, 'B1 tampo aparente')
add('Branco', 15, 163, 50, 1, 'B1 base')
# 4 prateleiras internas (vao 84) Branco 15
add('Branco', 15, 84, 50, 4, 'B1 prateleiras vao84')
# Nicho alto: 1 divisoria/lateral do nicho 50 x 196 (Branco 15) + fundo aparente do nicho Azul 6 (30x196)
add('Branco', 15, 50, 196, 1, 'B1 nicho alto divisoria')
add('Azul', 6, 30, 196, 1, 'B1 nicho alto fundo aparente')
# Reface de fundo do compartimento (6mm, leve) 163 x 128
add('Branco', 6, 163, 128, 1, 'B1 fundo reface')

# ---- B2: BANCADA INFERIOR (NOVA, em "L"). 154 L x 73 A x 61 P (+ retorno ~50)
# Tampo = PEDRA (marmorista, NAO conta MDF). Base em Azul 15.
add('Branco', 15, 154, 61, 1, 'B2 base')
# 2 laterais externas (Azul 15) + 3 divisorias internas (Branco 15) entre modulos
add('Azul', 15, 61, 73, 2, 'B2 laterais ext')
add('Branco', 15, 61, 73, 3, 'B2 divisorias')
# fundo (Branco 6)
add('Branco', 6, 154, 73, 1, 'B2 fundo')
# retorno em L (~50 larg): tampo = pedra (marmorista, fora) ; base + 1 lateral + fundo em Azul
add('Branco', 15, 50, 61, 1, 'B2 retorno base')
add('Azul', 15, 61, 73, 1, 'B2 retorno lateral'); add('Branco', 6, 50, 73, 1, 'B2 retorno fundo')
# 2 gavetoes 71 x 34
gaveta('B2 gavetao1', 71, 34, 61); gaveta('B2 gavetao2', 71, 34, 61)
# nichos abertos (39x50, 39x14, 2x 38x32): revestimento interno aparente Azul 15 (fundo dos nichos)
add('Azul', 6, 39, 50, 1, 'B2 nicho fundo 39x50')
add('Azul', 6, 38, 32, 2, 'B2 nicho fundo 38x32')
# 3 cestos aramados (frutas/legumes) = acessorio metalico (terceiro) -> em FERRAGENS/acessorios

# ==================================================================== LAVANDERIA
amb("Lavanderia")
# ---- B3: TORRE MAQUINA DE LAVAR. 84 L x 152 A x 67 P (prof escalonada 42+25). Vao maquina 69x87.
add('Azul', 15, 84, 67, 1, 'B3 tampo')
add('Branco', 15, 84, 67, 1, 'B3 base')
add('Azul', 15, 67, 152, 2, 'B3 laterais ext')
add('Branco', 15, 67, 152, 1, 'B3 divisoria (vao maq | coluna produtos)')
add('Branco', 6, 84, 152, 1, 'B3 fundo')
# bancada de apoio (fixa, sobre vao maquina) Azul 15
add('Azul', 15, 84, 67, 1, 'B3 bancada de apoio')
# coluna "gaveta de produtos": 3 gavetas ~15 x 27
gaveta('B3 produtos1', 15, 27, 42); gaveta('B3 produtos2', 15, 27, 42); gaveta('B3 produtos3', 15, 27, 42)
# gavetao de roupas 79 x 47
gaveta('B3 gavetao roupas', 79, 47, 60)
# apoio p/ roupas (prateleira extraivel) 79 x 60 Branco 15 + testeira Azul18
add('Branco', 15, 79, 60, 1, 'B3 apoio extraivel')
add('Azul', 18, 79, 5, 1, 'B3 apoio extraivel testeira')

# ==================================================================== ARMARIO TANQUE
amb("Armário Tanque")
# ---- B4: BALCAO TANQUE. 50 L x 65 A x 48 P. Tampo = PEDRA (terceiro, NAO conta MDF). 2 portas de giro 24x64.
add('Branco', 15, 50, 48, 1, 'B4 base')
add('Azul', 15, 48, 65, 2, 'B4 laterais ext')
add('Branco', 15, 48, 65, 1, 'B4 divisoria central')
add('Branco', 6, 50, 65, 1, 'B4 fundo')
add('Azul', 18, 24, 64, 2, 'B4 portas giro 24x64')
add('Branco', 15, 46, 48, 1, 'B4 prateleira interna')

# ==================== FECHAMENTO ====================
import math
print("PECAS lancadas:", len(log))
print("\n=== CHAPAS (compra global) ===")
tot_cost = 0; tot_ch = 0; cpm = {}
for (mat, esp), area in sorted(tal.items(), key=lambda x: (-x[1])):
    cor = COR[mat]; ch = max(1, math.ceil(area/(CHAPA*APROV[esp]))); preco = PRC[(cor, esp)]; cost = ch*preco
    tot_cost += cost; tot_ch += ch; cpm[(mat, esp)] = cost/area if area else 0
    print(f"{mat:7s} {esp:>2}mm  {area:6.2f} m2 -> {ch:>2} ch x R${preco} = R${cost}")
print(f"TOTAL CHAPAS: {tot_ch} chapas = R$ {tot_cost:.0f}")

# ---------- FERRAGENS (2 linhas) ----------
# Contagem: corredicas (pares) = 2 (B2 gavetoes) + 3 (B3 produtos) + 1 (B3 gavetao roupas) + 1 (B3 apoio extraivel) = 7
# dobradicas: B1 4 portas (~14 dob.) + B4 2 portas (4 dob.) = 18 dobradicas
PARES_CORR = 7
DOBRADICAS = 18
FERR = {
    'Telescopica': PARES_CORR*40 + DOBRADICAS*6,    # corredica telescopica R$40/par + dobradica padrao R$6 (garantia 2 anos)
    'Hardt':       PARES_CORR*70 + DOBRADICAS*8,    # corredica oculta Hardt c/ amort. R$70/par + dobradica Hardt R$8 (garantia 5 anos)
}
# comuns as 2 linhas:
PISTOES = 2*50          # 2 pistoes a gas (nicho alto despensa)
CESTOS = 3*90           # 3 cestos aramados frutas/legumes
ACESS = PISTOES + CESTOS

# ---------- INSUMOS (por chapa) + usinagem + LED ----------
FITA = tot_ch*75        # fita de borda (~R$75/chapa)
INSUMOS = tot_ch*60     # cola, parafuso, minifix, cavilha, bucha, suporte prat. (~R$60/chapa)
USINAGEM = 450          # cava/puxador porta passante (lavanderia) + furacoes especiais
LED = 300               # perfil de LED embutir 3000K + fita + fonte (despensa, ~1,6 m)
VISITAS = 2*250         # 2 visitas tecnicas
LOGISTICA = 2*150       # 2 carretos (projeto pequeno)
common_fixo = ACESS + FITA + INSUMOS + USINAGEM + LED + VISITAS + LOGISTICA

print("\n=== CUSTO DE MATERIAL (Valvic) ===")
print(f"chapas={tot_cost:.0f} · fita={FITA:.0f} · insumos={INSUMOS:.0f} · usinagem={USINAGEM} · LED={LED} · acess(pistoes+cestos)={ACESS} · visitas={VISITAS} · logistica={LOGISTICA}")
for linha, ferr in FERR.items():
    material = tot_cost + common_fixo + ferr
    print(f"{linha:12s}: fixedR = R$ {material:.0f}  (ferragem {ferr})")

# ---------- MOTOR (COM cartao: parc=8 -> a=0.18 ; liqF=0.88 ; RT10 -> b=0.143) ----------
# Regras da casa (mesmas do Jairo, com parcelamento): a=(nf4+parc8+vend3+erro2+serra.5+manut.5)=0.18 ;
#   liqF=1-(nf4+parc8)/100=0.88 ; b=(prog0.8+coord1+marc2.5+rt10)/100=0.143 ; denom = 1 - a - liqF*b - mc = 0.69416 - mc
a_enc = 0.18; liqF = 0.88; b = (0.8+1+2.5+10)/100
def preco(fixedR, mc): return fixedR/(1 - a_enc - liqF*b - mc)
LINHAS = {'Essencial (Telescópica/2a)': ('Telescopica', 0.32),
          'Essencial Prime (Hardt/5a)': ('Hardt', 0.37)}   # 2a linha +5% de MC
print("\n=== PRECO FINAL (motor COM cartao, RT10% liq — arq. Lais Teles) ===")
print(f"denominador = 1 - {a_enc} - {liqF}*{b:.3f} - mc = {1-a_enc-liqF*b:.5f} - mc")
precos = {}
for nome, (ferrk, mc) in LINHAS.items():
    fixedR = tot_cost + common_fixo + FERR[ferrk]
    inv = preco(fixedR, mc); precos[nome] = inv
    print(f"{nome:30s} fixedR={fixedR:.0f}  MC {int(mc*100)}%  ->  INVEST = R$ {inv:,.0f}".replace(',', '.'))

# ---------- ALOCACAO por ambiente (proporcional ao material direto: chapa alocada + ferragem por ambiente) ----------
# ferragem por ambiente (linha base Telescopica p/ fracao): B2 2 gav, B3 5 corr + apoio, B1/B4 dobradicas
tot_matdir = sum(sum(area*cpm[k] for k, area in d.items()) for d in amb_area.values())
print("\n=== ALOCACAO POR AMBIENTE (proporcional ao material direto em chapa) ===")
print(f"{'Ambiente':20s} {'%mat':>6} {'Essencial':>12} {'Ess.Prime':>12}")
alloc = {}
for a in sorted(amb_area, key=lambda x: -sum(area*cpm[k] for k, area in amb_area[x].items())):
    md = sum(area*cpm[k] for k, area in amb_area[a].items()); frac = md/tot_matdir
    e = precos['Essencial (Telescópica/2a)']*frac; p = precos['Essencial Prime (Hardt/5a)']*frac
    alloc[a] = (e, p)
    print(f"{a:20s} {frac*100:5.1f}% {e:12,.0f} {p:12,.0f}".replace(',', '.'))
te = sum(v[0] for v in alloc.values()); tp = sum(v[1] for v in alloc.values())
print(f"{'TOTAL':20s} {'100%':>6} {te:12,.0f} {tp:12,.0f}".replace(',', '.'))

# ---------- DETALHE por ambiente (dump peca-a-peca): python3 corte-graca.py detalhe [Ambiente] ----------
import sys
if len(sys.argv) > 1 and sys.argv[1].startswith('detalhe'):
    alvo = sys.argv[2] if len(sys.argv) > 2 else 'Despensa'
    print(f"\n\n######## DETALHE — {alvo} ########")
    print(f"{'Peca':34s} {'Material':8s} {'esp':>4} {'L(cm)':>6} {'A(cm)':>6} {'qt':>3} {'m2':>7}")
    sub = {}
    for (a, lab, mat, esp, w, h, n, area) in log:
        if a != alvo: continue
        print(f"{lab:34s} {mat:8s} {esp:>3}mm {w:>6.0f} {h:>6.0f} {n:>3} {area:7.3f}")
        sub[(mat, esp)] = sub.get((mat, esp), 0) + area
    print(f"\n-- m2 por material/espessura ({alvo}) --")
    ch_amb = 0; cost_amb = 0
    for (mat, esp), area in sorted(sub.items(), key=lambda x: -x[1]):
        cor = COR[mat]; frac_ch = area/(CHAPA*APROV[esp]); custo = area*cpm[(mat, esp)]
        ch_amb += frac_ch; cost_amb += custo
        print(f"{mat:8s} {esp:>2}mm  {area:6.2f} m2  ->  {frac_ch:4.2f} chapa-eq  ~R$ {custo:6.0f}")
    print(f"m2 total {alvo}: {sum(sub.values()):.2f} m2  ·  ~{ch_amb:.1f} chapas-equivalentes  ·  chapa ~R$ {cost_amb:.0f}")
