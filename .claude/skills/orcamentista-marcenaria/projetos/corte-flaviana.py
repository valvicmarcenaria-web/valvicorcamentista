# -*- coding: utf-8 -*-
"""FLAVIANA E IGOR — MARCENARIA DO BANHEIRO SUÍTE. LEVANTAMENTO E PREÇO.

Rua Espírito Santo, apto 602, Lourdes, BH
PROJETO EXECUTIVO · arq. DANI ROSARIA Arquitetura e Design · 8/07 · rev. 00
Caderno de 8 páginas A3, CASO A. Banho suíte de 5,10 m², pé-direito 2,54.

ESCOPO DE MARCENARIA — três itens, dentro de um caderno que tem muito mais:
  1 · Armário aéreo sobre a bancada .... 147 × 118 × 17 · 3 portas espelhadas
                                          + frente fixa espelhada
  2 · Armário inferior sob a bancada ... 194 × 61 × 45 · nichos + gavetão de
                                          roupa suja + 4 gavetas
  3 · Porta de correr em MDF ........... 70 × 210, embutida na parede

⛔ FORA — o caderno detalha, mas NÃO é marcenaria:
   · bancada esculpida em mármore Bege Bahia levigado (página 7) — MARMORARIA
   · porcelanato, paginação de piso e parede, forro de gesso, sanca
   · box de vidro, louças, metais, aquecimento Cardal
   · nicho em porcelanato iluminado (é revestimento, não marcenaria)

⛔ MONTAGEM NÃO ENTRA NO CUSTO (equipe é salário fixo) — mas entra no escopo.
"""
from collections import defaultdict
import math

W = 100
CH_C, CH_L = 275.0, 185.0
CH_AREA = 2.75*1.85
A_, LIQF_, B_ = 0.162, 0.88, 0.043
BASE = 1 - A_ - LIQF_*B_
RT_PCT = 0.10
def div(mc, rt=False): return BASE - mc - (LIQF_*RT_PCT if rt else 0.0)
def mc_conferida(p, c): return BASE - c/p

def _pack_faixa(pcs):
    ch = 0; y = x = f = 0.0
    for c, l in pcs:
        if c > CH_C and l <= CH_C: c, l = l, c
        if c > CH_C or l > CH_L: ch += 1; continue
        if x + c > CH_C: y += f; x = 0.0; f = 0.0
        if y + l > CH_L: ch += 1; y = x = f = 0.0
        x += c; f = max(f, l)
    return ch + 1
def _pack_bf(pcs):
    ch = []
    for c, l in pcs:
        if c > CH_C and l <= CH_C: c, l = l, c
        if c > CH_C or l > CH_L: ch.append([CH_L, []]); continue
        best = None
        for s in ch:
            for fx in s[1]:
                if fx[0] >= l and fx[1] >= c and (best is None or fx[1] < best[1]): best = fx
        if best is not None: best[1] -= c; continue
        for s in ch:
            if s[0] + l <= CH_L:
                s[0] += l; s[1].append([l, CH_C - c]); break
        else: ch.append([l, [[l, CH_C - c]]])
    return len(ch)
def nest(items):
    if not items: return 0
    b = [(max(c, l), min(c, l)) for c, l in items]
    ords = [lambda q: -q[1], lambda q: (-q[1], -q[0]), lambda q: -q[0], lambda q: -q[0]*q[1]]
    ch = min(pk(sorted(b, key=k)) for pk in (_pack_faixa, _pack_bf) for k in ords)
    ar = sum(c*l for c, l in items)/10000
    return max(ch, -(-int(ar/(CH_AREA*0.80)*1000)//1000) or 1)

# ── preços · dados/materiais.json (11/06/2026) ────────────────────────────
PRC_COR = {6: 300.0, 15: 500.0, 18: 600.0, 25: 900.0}   # Carvalho Nórdico
# [Jonathan 29/08] "os MDF branco a ser utilizados serão da linha ULTRA
# PREMIUM, inclusive a da nova porta". É o MDF Branco Ártico Ultra, que o
# `chapas.md` descreve como "interno de áreas úmidas, mais resistente à
# umidade" — banheiro é exatamente o caso.
# ★ PREÇO ADOTADO POR RAZÃO, NÃO POR LINHA DE BASE. O `materiais.json` não
#   tem o Ártico Ultra; o `chapas.md` tem, mas noutra base de preços (lá o
#   Fosco 18 é 125, aqui é 600). Aproveita-se de lá a POSIÇÃO RELATIVA:
#   Ártico Ultra 6/15/18 = 78/108/122 contra Fosco 85/110/125. Aplicada à
#   base de hoje, o branco ultra sai quase no preço de um melamínico
#   colorido — coerente com um MDF de área úmida. CONFERIR compra.
#   (o 25 mm não aparece neste job; herda a razão do 18)
_RAZAO  = {6: 78/85, 15: 108/110, 18: 122/125, 25: 122/125}
PRC_BRA = {e: round(PRC_COR[e]*r/5)*5 for e, r in _RAZAO.items()}
NOME_MAT = {'AM': 'MDF Carvalho Nórdico', 'BR': 'MDF Branco Ártico Ultra'}
def prc(m, e): return PRC_BRA[e] if m == 'BR' else PRC_COR[e]

FITA_M, FILET_M, DESPERD = 3.00, 2.50, 1.10
USIN_M   = 25.0        # puxador cava usinado com pega / passante
FURO_UN  = 18.0        # ★ furo Ø6 cm fitado na prateleira
SUP_PRAT = 8.0         # ★ suporte de prateleira (mesma adoção do job da Giza)
ESPELHO_M2 = 600.0     # espelho prata colado — só na frente FIXA
# [Jonathan 29/08] "as portas de espelho são com estrutura de ALUMÍNIO devido
# ao peso". A folha que ABRE deixa de ser frente de MDF com espelho colado e
# vira porta terceirizada de perfil de alumínio, espelho prata e película de
# segurança: sai a chapa de 18 da folha, entra a porta pronta. A frente FIXA
# de 11, que só fecha o vão, continua com espelho colado no MDF.
# ★ R$ 700/m² posto na obra — mesma adoção do job da Giza. A base tem folha
#   GRANDE a R$ 622/m² (1.200 + 200 de frete, ~90 × 250); em folha pequena o
#   perímetro de perfil pesa mais, e a referência confirmada de folha pequena
#   (Renolfh/Alumindoor, Kenia & Fábio 12/06/2026) é R$ 660–711/m².
PORTA_ESP_M2 = 700.0
DOBR = 20.0            # Häfele — a prancha manda "especificar marca"
# [Jonathan 29/08] "a gente não utiliza essas ferragens" — TELESCÓPICA SAI.
# Vira Hardt em TODAS as gavetas. É o padrão real da casa: ferragens.md diz
# "corrediça oculta com slow motion é o padrão; ~70% dos casos: Hardt", e o SKU
# de produção é a Hardt Invisível P-10 com amortecimento (400/450/550 mm).
# Telescópica é Linha Silver — rebaixamento de preço, não especificação.
CORR_HARDT = 70.0      # Corrediça Oculta Hardt · dados/materiais.json
# ★ LED: a prancha especifica perfil de SOBREPOR sem aba WOOD da Usina Design
#   (1,7 × 1 cm) com fita LED IP65 12 V, 2700 K, 15 W, Saveenergy. NÃO é COB —
#   então não cabe a linha de R$ 150/m da base. Mas o perfil é de marca
#   especificada, acima do perfil comum de R$ 38 que os motores usam. Adotei
#   R$ 110/m, entre os dois. São ~5 m: a diferença para qualquer extremo é
#   de poucas centenas.
LED_M = 110.0
DRIVER_UN = 90.0
# O ★ de R$ 450 saiu: a base TEM a linha, na categoria "Sistemas de porta de
# passagem", e ferragens.md nomeia o RO82 como o deslizante de porta de
# passagem da casa. Vai o RO82 Top, com amortecimento.
RO82_TOP  = 400.0      # Sistema deslizante RO82 Top (amortecimento)
# [Jonathan 29/08] "a porta de passagem não tem desempenadores" — a base traz
# o desempenador como padrão em porta deslizante, mas quem compra é ele. Fora.
KIT_CORRER = RO82_TOP

P, FITA, TERC, LED, USIN, DUV = [], [], [], [], [], []
FER = defaultdict(lambda: [0, 0, 0])       # dobradiças · oculta · (livre)
def add(mat, esp, amb, desc, c, l, q=1): P.append((mat, esp, amb, desc, c, l, q))
def fer(a, dobr=0, oc=0, tel=0):
    FER[a][0] += dobr; FER[a][1] += oc; FER[a][2] += tel
def fita(a, d, m): FITA.append((a, d, m))
def terc(a, d, v, est=False): TERC.append((a, d, v, est))
def led(a, d, m): LED.append((a, d, m))
def usin(a, m): USIN.append((a, m))
def duv(a, t): DUV.append((a, t))
def gaveta(mat, amb, nome, L, Pf, alt, q=1):
    add(mat, 15, amb, f'{nome} · caixa lateral',       Pf-10, alt, 2*q)
    add(mat, 15, amb, f'{nome} · caixa frente/costas', L-6,   alt, 2*q)
    add(mat, 6,  amb, f'{nome} · fundo de gaveta',     L-6,   Pf-10, q)

# ═══════════════════════════════════════════════════════════════════════════
# GEOMETRIA — cotas da prancha 06/8 (MARCENARIA). Tudo em cm.
#
#   Alturas, da elevação 19 (vista interna), somando 242 do piso ao gesso:
#     118 armário aéreo · 48 faixa da bancada · 61 armário inferior · 15 rodapé
#
#   Aéreo  147 = 11 + 43 + 2 + 46 + 2 + 43   (frente fixa de 11 + 3 portas)
#   Inferior 194, com nichos de 44, gavetão de 77 e coluna de gavetas de 38
# ═══════════════════════════════════════════════════════════════════════════

# ───────────────────────────────────────────────────────────────────────────
# 1 · ARMÁRIO AÉREO SOBRE A BANCADA — 147 × 118 × 17
#     Externo em Carvalho Nórdico, interno em Branco TX, frentes espelhadas.
#     Prateleira com borda alta de 11 p/ os drivers de todo o banheiro.
# ───────────────────────────────────────────────────────────────────────────
A = 'Armário aéreo sobre a bancada'
LA, HA, PA = 147.0, 118.0, 17.0
add('AM', 15, A, f'lateral {HA*10:.0f} × {PA*10:.0f}',      HA, PA, 2)
add('AM', 15, A, f'tampo e base {LA*10:.0f} × {PA*10:.0f}', LA-3, PA, 2)
add('BR', 6,  A, 'fundo',                                   LA-3, HA-3, 1)
add('BR', 15, A, 'divisória vertical interna',              HA-3, PA, 2)
add('BR', 15, A, 'prateleira interna',                      45, PA-1, 13)
add('BR', 15, A, 'prateleira com borda alta de 110 p/ drivers', 45, 11, 1)
# as três folhas que ABREM são porta pronta de alumínio: não entram no corte
_m2_al = (2*43 + 46)*HA/10000
terc(A, f'3 portas de espelho em perfil de alumínio, com película de '
        f'segurança ({_m2_al:.2f} m²)', _m2_al*PORTA_ESP_M2)
add('AM', 18, A, 'frente fixa espelhada 110 × 1180',        11, HA, 1)
_m2_fx = 11*HA/10000
terc(A, f'Espelho prata colado na frente fixa ({_m2_fx:.2f} m²)',
     _m2_fx*ESPELHO_M2)
fer(A, dobr=6)
# sem cava nas folhas de alumínio — o puxador é do perfil
usin(A, 0.0)
# a borda da porta de alumínio é o perfil: fita só no que é chapa nossa
fita(A, 'frente fixa, bordas e frentes de prateleira fitadas no amadeirado',
     2*(0.11+HA/100) + 2*(LA+HA)/100 + 14*0.45)
led(A, 'perfil de sobrepor Usina Design Wood + fita LED IP65 2700 K', LA/100)
terc(A, 'Drivers slim de TODA a iluminação do banheiro, guardados no aéreo',
     3*DRIVER_UN, est=True)
terc(A, '3 furos Ø6 cm fitados: secador (com espaço de cabo), babyliss e escovas',
     3*FURO_UN, est=True)
terc(A, f'Suportes de prateleira ({14*4} un)', 14*4*SUP_PRAT)
duv(A, 'a nota manda EXTERNO em Carvalho Nórdico e INTERNO em Branco TX — mas '
       'as três portas levam ESPELHO PRATA colado na frente. Ou seja, o '
       'amadeirado externo só aparece nas laterais e no arremate. Lancei '
       'assim; se o espelho for só nas duas portas grandes, muda pouco.')
duv(A, 'a prancha manda guardar no aéreo os drivers slim de TODA a iluminação '
       'do banheiro — não só a do armário. Lancei 3 drivers. Se o banheiro '
       'tiver mais circuitos (sanca, nicho, box), são mais.')

# ───────────────────────────────────────────────────────────────────────────
# 2 · ARMÁRIO INFERIOR SOB A BANCADA — 194 × 61 × 45
#     2 nichos abertos · gavetão de roupa suja com corrediça oculta invisível
#     4 gavetas com corrediça oculta Hardt com amortecimento · rodapé de 15
#     Fundo aberto para o aparelho Cardal, prateleira removível recortada.
# ───────────────────────────────────────────────────────────────────────────
A = 'Armário inferior sob a bancada'
LI, HI, PI = 194.0, 61.0, 45.0
add('AM', 15, A, f'lateral {HI*10:.0f} × {PI*10:.0f}',      HI, PI, 2)
add('AM', 15, A, f'base {LI*10:.0f} × {PI*10:.0f}',         LI-3, PI, 1)
add('AM', 15, A, 'divisória vertical',                       HI, PI, 3)
add('AM', 15, A, 'travessa superior',                       LI-3, 10, 2)
add('BR', 6,  A, 'fundo (recortado, aberto no trecho do Cardal)', LI-3, HI, 1)
add('AM', 18, A, 'nicho aberto · prateleira e fundo do nicho', 44, PI, 3)
# 15 mm, não 18: essa prateleira era a ÚNICA peça branca de 18 no job e
# puxava uma chapa inteira para 0,26 m² — 5% de aproveitamento, R$ 330.
# É prateleira interna removível: 15 mm resolve e entra na chapa que já
# está aberta.
add('BR', 15, A, 'prateleira removível recortada p/ o Cardal', 60, PI-2, 1)
add('AM', 18, A, 'frente do gavetão de roupa suja 770 × 570', 77, 57, 1)
add('AM', 18, A, 'frente de gaveta 380 × 150',               38, 15, 4)
gaveta('BR', A, 'gavetão de roupa suja', 77, PI, 55, 1)
gaveta('BR', A, 'gaveta', 38, PI, 13, 4)
add('AM', 15, A, 'rodapé recuado',                          LI, 15, 1)
fer(A, oc=5)      # gavetão + 4 gavetas, todas Hardt
usin(A, (0.77 + 4*0.38))
fita(A, 'frentes, nichos e rodapé',
     2*(0.77+0.57) + 4*2*(0.38+0.15) + 3*2*(0.44+PI/100)
     + 2*(LI+HI)/100 + LI/100)
duv(A, 'as duas elevações do inferior não fecham entre si: a externa cota '
       '44/38/38/38/37 e a interna cota 41/36/77/38. Adotei a leitura da '
       'INTERNA — nichos de 44, gavetão de 77 e coluna de 4 gavetas de 38 — '
       'que é a que casa com os móveis desenhados. CONFERIR em obra.')
duv(A, 'a profundidade do inferior não é cotada na prancha de marcenaria. A '
       'bancada de mármore tem 66 (prancha 05/8, marmoraria). Adotei 45 para o '
       'gabinete, que é o padrão sob bancada de banheiro. CONFERIR.')

# ───────────────────────────────────────────────────────────────────────────
# 3 · PORTA DE CORRER EM MDF — 70 × 210, embutida
#     "FAZER DENTE PAREDE PARA EMBUTIR PORTA DE MDF DE CORRER EM MARCENARIA".
#     O dente na parede é da obra; a folha e o sistema são nossos.
# ───────────────────────────────────────────────────────────────────────────
A = 'Porta de correr em MDF'
# [Jonathan 29/08] "inclusive a da nova porta" — a folha é BRANCA, linha
# ultra premium. É o que o render mostra; eu tinha lançado em amadeirado.
add('BR', 18, A, 'folha da porta 700 × 2100', 70, 210, 1)
add('BR', 18, A, 'folha da porta · segunda face (sanduíche)', 70, 210, 1)
fita(A, 'porta · perímetro nas duas faces', 2*(0.70+2.10))
usin(A, 2.10)
terc(A, 'Sistema deslizante RO82 Top, com amortecimento', KIT_CORRER)
duv(A, 'orcei a folha como SANDUÍCHE de duas chapas de 18 — porta de passagem '
       'de 70 × 210 em chapa única empena. Se o projeto aceitar folha oca com '
       'miolo colmeia, cai o material mas entra prensa.')
duv(A, 'o DENTE na parede para embutir o trilho é serviço de OBRA (a prancha '
       'diz "fazer dente parede"). Não está no valor.')

# ═══════════════════════════════════════════════════════════════════════════
# CÁLCULO
# ═══════════════════════════════════════════════════════════════════════════
N_CARRETO, R_CARRETO = 1, 600.0
N_VISITA,  R_VISITA  = 1, 250.0
LOG = N_CARRETO*R_CARRETO + N_VISITA*R_VISITA
ESCADA = [0.35, 0.38, 0.40]

por, area_ch, area_amb = defaultdict(list), defaultdict(float), defaultdict(float)
for m, e, a, d, c, l, q in P:
    for _ in range(q): por[(m, e)].append((c, l))
    ar = c*l*q/10000
    area_ch[(m, e)] += ar; area_amb[a] += ar
CH = {k: nest(v) for k, v in por.items()}
custo_chapa = sum(n*prc(k[0], k[1]) for k, n in CH.items())
area_tot, tot_ch = sum(area_ch.values()), sum(CH.values())
ordem = list(dict.fromkeys(x[2] for x in P))

m_fita_expl = sum(m for _, _, m in FITA)
m_fita = max(m_fita_expl, area_tot*2.6)
custo_fita, custo_filet = m_fita*DESPERD*FITA_M, m_fita*FILET_M
m_usin = sum(m for _, m in USIN); custo_usin = m_usin*USIN_M
m_led = sum(m for _, _, m in LED); custo_led = m_led*LED_M
custo_terc = sum(v for _, _, v, _ in TERC)
TD = sum(f[0] for f in FER.values())
TO = sum(f[1] for f in FER.values())
TT = sum(f[2] for f in FER.values())
custo_ferr = TD*DOBR + (TO + TT)*CORR_HARDT
consum = (custo_chapa + custo_fita)*0.06
CD = (custo_chapa + custo_fita + custo_filet + custo_usin + custo_led
      + custo_terc + consum + custo_ferr + LOG)

# ── CUSTO DIRETO POR ITEM ─────────────────────────────────────────────────
# ⛔ O rateio por ÁREA DE CHAPA estava ERRADO, e o Jonathan pegou [29/08]: o
#    gabinete inferior é o item de mais chapa e quase nenhum acessório, e
#    levava 49% do preço; o aéreo, que carrega espelho, LED, drivers e 56
#    suportes, saía barato. Área de chapa não é custo. O rateio agora é pelo
#    CUSTO DIRETO de cada item, item por item.
cd_amb = defaultdict(float)
# chapa · dentro de cada grupo (material, espessura), a chapa comprada é
#   rateada pela área que cada item ocupa NAQUELE grupo — é como ela é gasta.
_ar_gr = defaultdict(float)
for m, e, a, d, c, l, q in P: _ar_gr[(m, e, a)] += c*l*q/10000
for (m, e, a), ar in _ar_gr.items():
    cd_amb[a] += CH[(m, e)]*prc(m, e) * ar/area_ch[(m, e)]
# fita e filetagem · se o piso de 2,6 m/m² valeu, o metro é do job inteiro e
#   só a área explica quanto cada item puxa.
_f_amb = defaultdict(float)
if m_fita > m_fita_expl:
    for a in ordem: _f_amb[a] = m_fita*area_amb[a]/area_tot
else:
    for a, d, mm in FITA: _f_amb[a] += mm
for a, mm in _f_amb.items(): cd_amb[a] += mm*(DESPERD*FITA_M + FILET_M)
for a, mm in USIN:          cd_amb[a] += mm*USIN_M
for a, d, mm in LED:        cd_amb[a] += mm*LED_M
for a, d, v, _e in TERC:    cd_amb[a] += v
for a, (dd, oo, tt) in FER.items():
    cd_amb[a] += dd*DOBR + (oo + tt)*CORR_HARDT
# consumíveis e logística não têm dono: acompanham o resto.
_bruto = sum(cd_amb.values())
for a in list(cd_amb): cd_amb[a] += (consum + LOG)*cd_amb[a]/_bruto
assert abs(sum(cd_amb.values()) - CD) < 0.01, (sum(cd_amb.values()), CD)

def brl(v, n=2):
    return f'{v:,.{n}f}'.replace(',', '§').replace('.', ',').replace('§', '.')

_fora = [(m, e, a, d, c, l) for m, e, a, d, c, l, q in P
         if max(c, l) > CH_C or min(c, l) > CH_L]
if _fora:
    print('\n' + '!'*W + '\nPEÇAS QUE NÃO CABEM NA CHAPA')
    for m, e, a, d, c, l in _fora:
        print(f'  {NOME_MAT[m]} {e} · {a} · {d}: {c:.0f} × {l:.0f}')
    print('!'*W + '\n')

print('═'*W)
print('FLAVIANA E IGOR — MARCENARIA DO BANHEIRO SUÍTE · LEVANTAMENTO E CUSTO')
print('═'*W)
print('Projeto executivo · arq. Dani Rosaria · 8/07 rev.00 · caderno de 8 pranchas A3')
print('Três itens de marcenaria. A bancada esculpida é MARMORARIA, fora do escopo.')

print('\nESCOPO')
for a in ordem:
    d, o, t = FER[a]
    ex = [f'{d} dobr.' if d else '', f'{o+t} oculta Hardt' if o+t else '']
    print(f'  {a:<38}{area_amb[a]:>7.2f} m²   {" · ".join(x for x in ex if x)}')
print(f'  {"TOTAL":<38}{area_tot:>7.2f} m²')

print('\nPLANO DE CORTE')
for k in sorted(CH, key=lambda k: (k[0], -k[1])):
    m, e = k; n = CH[k]; pr = prc(m, e)
    print(f'  {NOME_MAT[m]+" "+str(e)+" mm":<28}{area_ch[k]:>7.2f} m²  →  {n:>2} ch. × '
          f'R$ {brl(pr):>8} = R$ {brl(n*pr):>9}   aprov. '
          f'{area_ch[k]/(n*CH_AREA)*100:>3.0f}%')
print(f'  {"TOTAL":<28}{area_tot:>7.2f} m²  →  {tot_ch:>2} chapas{"":>20}'
      f'R$ {brl(custo_chapa):>9}   médio {area_tot/(tot_ch*CH_AREA)*100:.0f}%')

print(f'\nFITA E FILETAGEM   {m_fita:.2f} m · R$ {brl(custo_fita)} + R$ {brl(custo_filet)}')
print(f'USINAGEM           puxador cava com pega · {m_usin:.2f} m · R$ {brl(custo_usin)}')
print(f'ILUMINAÇÃO         perfil Usina Design + fita IP65 · {m_led:.2f} m × '
      f'R$ {brl(LED_M)}/m · R$ {brl(custo_led)}')

print('\nTERCEIRIZADOS E ITENS ESPECIAIS   (★ = sem preço fechado na base)')
for a, d, v, est in TERC:
    print(f' {"★" if est else " "}{a:<32}{d[:44]:<45}R$ {brl(v):>9}')
print(f'  {"TOTAL":<78}R$ {brl(custo_terc):>9}')
print(f'\nFERRAGEM — {TD} dobradiças Häfele · {TO+TT} corrediças ocultas Hardt '
      f'Invisível P-10 com amortecimento (gavetão + 4 gavetas)')

print('\n' + '═'*W)
print('CUSTO DIRETO')
print('═'*W)
for rot, v in (('Chapas', custo_chapa), ('Fita (material)', custo_fita),
               ('Filetagem', custo_filet), ('Usinagem do puxador cava', custo_usin),
               ('Iluminação', custo_led),
               ('Terceirizados (espelho, drivers, kit de correr, furos)', custo_terc),
               ('Consumíveis (6% de chapa + fita)', consum),
               ('Ferragem', custo_ferr),
               (f'Logística — {N_CARRETO} carreto + {N_VISITA} visita', LOG)):
    print(f'    {rot:<74}R$ {brl(v):>9}')
print(f'    {"CUSTO DIRETO":<74}R$ {brl(CD):>9}')

print('\n' + '═'*W)
print('PREÇO — escada de MC, com e sem RT')
print('═'*W)
print(f'  {"MC":<6}{"sem RT":>13}{"MC real":>10}   {"com RT 10%":>13}{"MC real":>10}')
PRECOS = {}
for mc in ESCADA:
    s = round(CD/div(mc, False)/100)*100
    r = round(CD/div(mc, True)/100)*100
    PRECOS[mc] = (s, r)
    print(f'  {mc*100:>4.0f}%{"R$ "+brl(s,0):>13}{mc_conferida(s, CD)*100:>9.1f}%   '
          f'{"R$ "+brl(r,0):>13}{mc_conferida(r, CD)*100:>9.1f}%')
# [Jonathan 25/08] "MC de 40% com rt em ambos" — fechado.
REC, RT_FECHADO = 0.40, True
INV = PRECOS[REC][1 if RT_FECHADO else 0]
INV_SEM = PRECOS[REC][0]
print(f'\n  ► FECHADO · MC {REC*100:.0f}% COM RT ....... R$ {brl(INV,0)}'
      f'     [Jonathan 25/08]')
print(f'    sem RT, referência interna ......... R$ {brl(INV_SEM,0)}')
rm = INV_SEM/area_tot
print(f'  R$/m² de chapa: {rm:.0f} sem RT   (faixa da casa: 626–834)')
if not 626 <= rm <= 834:
    print('  ⚠ FORA DA FAIXA — esperado num banheiro: espelho, LED de marca,')
    print(f'    drivers e kit de correr somam R$ {custo_terc+custo_led:,.0f}.'
          .replace(',', '.'))

print('\n' + '─'*W)
print(f'INVESTIMENTO POR ITEM  (MC {REC*100:.0f}% COM RT)')
tots, linhas = 0, []
for a in ordem:
    v = round(INV*cd_amb[a]/CD/100)*100          # rateio por CUSTO, não por área
    linhas.append([a, area_amb[a], cd_amb[a], v]); tots += v
linhas[max(range(len(linhas)), key=lambda i: linhas[i][2])][3] += INV - tots
print(f'  {"":38}{"m² de chapa":>12}{"custo direto":>15}{"investimento":>15}')
for a, ar, cd, v in linhas:
    print(f'  {a:<38}{ar:>9.2f} m²{"R$ "+brl(cd,0):>15}{"R$ "+brl(v,0):>15}')
print(f'  {"TOTAL":<38}{area_tot:>9.2f} m²{"R$ "+brl(CD,0):>15}'
      f'{"R$ "+brl(INV,0):>15}')

print('\n' + '─'*W)
print(f'DÚVIDAS E CONFERÊNCIAS — {len(DUV)} itens')
for i, (a, t) in enumerate(DUV, 1):
    print(f'  {i:>2}. [{a}]\n      {t}')
print('\n  ★ Preços adotados, sem linha na base:')
print(f'     · perfil Usina Design + fita IP65 — R$ {brl(LED_M,0)}/m (não é COB,')
print('       então não vale a linha de R$ 150 da base; é acima do perfil comum)')
print(f'     · furo Ø6 fitado — R$ {brl(FURO_UN,0)}/un · suporte de prateleira '
      f'R$ {brl(SUP_PRAT,0)}/un')
print('\n⛔ FORA DO ESCOPO: bancada esculpida em mármore (marmoraria),')
print('   porcelanato e paginação, forro de gesso e sanca, box de vidro,')
print('   louças, metais, aquecimento Cardal, nicho em porcelanato,')
print('   dente na parede para o trilho, pontos elétricos e hidráulicos.')
print('═'*W)
