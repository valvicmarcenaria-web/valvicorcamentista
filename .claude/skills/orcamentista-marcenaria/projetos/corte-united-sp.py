# -*- coding: utf-8 -*-
"""UNITED SP — pavimentos 8 e 9  [01/10/2026]

Fit-out corporativo. Projeto executivo R08 de 29/07/26, VD Arquitetura
(Glauco Vitor Dias). Folhas 3, 4, 11, 12, 13, 14, 15 e 19.1.
Levantamento em `levantamento-united-sp.md`.

DEFINIÇÕES DO JONATHAN [01/10]
  1 Granito São Gabriel escovado  ⛔ NÃO É NOSSO
  2 As 52 estações do contact center  ⛔ NÃO SÃO NOSSAS
  3 Prateleiras: suporte oculto de 40 em 40 cm, R$ 30 a unidade
  4 Portas mimetizadas: puxador usinado em uma das ripas do painel
  5 Profundidade da cozinha do 9° = 83 cm, confirmada
  ⭐ "montantes encorpados, 5 cm de espessura: duas chapas de 6 mm
     preenchidas para dar a espessura correspondente"
  ⭐ Logística de São Paulo, valores fechados: carreto 8.000 · logística de
     equipe 2.500 · estadia e alimentação 4.000 · hora extra 1.500
  ⭐ COM RT

FLAGS
  1 ★ Linha de ferragem não especificada. Adotei Hettich Sensys + corrediça
    oculta Quadro — é obra corporativa, com RT, e a garantia da casa nessa
    linha é de 10 anos. Com Novisys + telescópica o custo cai, e a garantia
    cai para 2 anos (ferragens.md). Ver o comparativo no fim.
  2 ★ Iluminação indireta sob os painéis do hall: a prancha manda, mas não
    ficou dito se é nosso fornecimento. Lancei por nossa conta. São dois
    painéis × dois pavimentos.
  3 ★ Ripado do painel azul: passo medido nos vetores da prancha = 5,0 cm.
    Lancei como friso usinado na própria chapa, com selagem do canal. Ripa
    aplicada a 5 cm justaposta custaria o dobro só de fita e não é o que o
    desenho mostra.
  4 ★ O painel de letreiro do hall (trecho claro na elevação) foi lido como
    comunicação visual do cliente, não como marcenaria.
  5 ⚠ Faltam as folhas 16 a 20, no meio da sequência de detalhamento.
  6 ⛔⛔ O PAINEL DO HALL TEM 2,80 DE ALTURA E A CHAPA TEM 2,75.
    Não existe chapa melamínica de 2,80 na linha Guararapes. As saídas são
    duas: emenda horizontal atravessando o ripado no hall do elevador, à
    altura dos olhos — ou o ripado parar em 2,70 e os 10 de cima virarem a
    SANCA que a própria prancha já pede ("iluminação indireta sob painéis
    em marcenaria"). Lancei a segunda. É a que o desenho já estava pedindo.
    ⚠ Vale para os dois painéis e para os dois pavimentos — quatro peças.
"""
from collections import defaultdict
from math import ceil
import motor_mc as M

CH_C, CH_L = 275.0, 185.0
CH_AREA = 2.75*1.85

# ── chapa ─────────────────────────────────────────────────────────────────
BR6, BR15, BR18 = 190.0, 260.0, 330.0
COR6, COR15, COR18 = 300.0, 500.0, 600.0
PRECO = {'BR6':BR6, 'BR15':BR15, 'BR18':BR18}
# TA Guararapes Tauari · DB Guararapes Dual Black
# AP Guararapes Azul Petróleo · AT Arauco Attena
for c in ('TA','DB','AP','AT'):
    PRECO[c+'6'], PRECO[c+'15'], PRECO[c+'18'] = COR6, COR15, COR18
NOME = {'BR6':'branco 6','BR15':'branco 15','BR18':'branco 18'}
for c, n in (('TA','Tauari'),('DB','Dual Black'),('AP','Azul Petról.'),
             ('AT','Attena')):
    for e in ('6','15','18'): NOME[c+e] = f'{n} {e}'

FITA_BR, FITA_COR = 2.0, 3.0

# ── ferragem ★ FLAG 1 ─────────────────────────────────────────────────────
DOBR_UN  = 35.0    # Hettich Sensys
CORR_UN  = 120.0   # Corrediça oculta Quadro (Hettich), o par
SUP_OCU  = 30.0    # ⭐ [Jonathan] suporte oculto de prateleira, de 40 em 40
SUP_PRAT = 1.50    # suporte de prateleira interna de armário
FECHA_UN = 45.0    # fechadura com chave (quadros de energia)

# ── taxas de serviço ──────────────────────────────────────────────────────
CAVA_M     = 33.33   # perfil cava RM213: R$ 100 o perfil de 3 m
PASSANTE_M = 33.33   # puxador passante, mesmo perfil embutido
ENCORP_M2  = 85.0    # ⭐ miolo sarrafeado + cola + prensagem, por m² de peça
                     #   (as duas faces de 6 mm entram como peça no corte)
RIPADO_M2  = 180.0   # ★ friso usinado a cada 5 cm + selagem do canal
LED_M      = 150.0   # LED COB fita + perfil

p, FER, TER = [], defaultdict(lambda: defaultdict(float)), defaultdict(float)
ENCA = defaultdict(float)                      # m² de peça encorpada
def a(mov, mat, desc, c, l, q=1): p.append((mov, mat, desc, c, l, q))
def f(mov, **kw):
    for k, v in kw.items(): FER[mov][k] += v
def t(mov, v): TER[mov] += v

def enc(mov, cor, desc, c, l, q=1):
    """⭐ Peça encorpada de 5 cm: duas faces de 6 mm + miolo sarrafeado,
    mais a testeira de 6 mm que fecha o topo dos 5 cm."""
    a(mov, cor+'6', desc+' · face',    c, l, q*2)
    a(mov, cor+'6', desc+' · testeira', (c+l)*2, 5, q)
    ENCA[mov] += c*l*q/10000

# ══════════════════════════════════════════════════════════════════════════
# PAVIMENTO 8
# ══════════════════════════════════════════════════════════════════════════

K = 'Cozinha 8° · bancada principal'
# 3,50 × 2,44 × 80. Aéreos Tauari com puxador passante, inferiores com cava.
a(K,'TA18','Porta de aéreo',               50, 60, 5)
a(K,'TA18','Porta de aéreo (extrema)',     50, 50, 1)
a(K,'BR15','Aéreo · lateral e divisória',  50, 33, 7)
a(K,'BR15','Aéreo · base e tampo',        175, 33, 4)
a(K,'BR6' ,'Aéreo · fundo',               175, 50, 2)
a(K,'TA18','Porta inferior',               85, 51, 2)
a(K,'TA18','Frente de gaveta',             21, 50, 4)
a(K,'BR15','Inferior · lateral e divisória', 85, 58, 4)
a(K,'BR15','Inferior · base e travessa',  149, 58, 3)
a(K,'BR6' ,'Inferior · fundo',            149, 85, 1)
a(K,'BR15','Caixa de gaveta',              55, 15, 8)
a(K,'BR6' ,'Fundo de gaveta',              55, 45, 4)
a(K,'TA18','Torre · porta',                85, 50, 1)
a(K,'TA18','Torre · porta superior',      103, 50, 1)
a(K,'BR15','Torre · lateral',             244, 78, 2)
a(K,'BR15','Torre · prateleira e base',    48, 78, 6)
a(K,'BR6' ,'Torre · fundo',               244, 50, 1)
enc(K,'TA','Lateral aparente',            244, 80, 2)
enc(K,'TA','Travessa de topo',            350, 80, 1)
enc(K,'DB','Prateleira',                  136, 20, 1)
enc(K,'TA','Rodapé',                      350,  5, 1)
f(K, dobr=6*2 + 2*2 + 2*3, corr=4, sup=6)
t(K, 3.50*PASSANTE_M + 1.51*CAVA_M)

K = 'Cozinha 8° · bancada alta'
# volume em Dual Black, 1,50 × 60 × 1,20, para duas banquetas
enc(K,'DB','Tampo',                       150, 60, 1)
enc(K,'DB','Lateral',                     115, 60, 2)
enc(K,'DB','Fechamento frontal',          140, 115, 1)
a(K,'BR15','Travessa de estrutura',       138, 55, 3)

K = 'Cozinha 8° · módulo da cuba'
# 1,30 × 2,44 × 60
a(K,'TA18','Porta de aéreo',               44, 65, 2)
a(K,'BR15','Aéreo · lateral e divisória',  44, 33, 3)
a(K,'BR15','Aéreo · base e tampo',        128, 33, 2)
a(K,'BR6' ,'Aéreo · fundo',               128, 44, 1)
a(K,'TA18','Porta inferior',               75, 65, 2)
a(K,'BR15','Inferior · lateral e divisória', 75, 58, 3)
a(K,'BR15','Inferior · base e travessa',  128, 58, 2)
a(K,'BR6' ,'Inferior · fundo',            128, 75, 1)
a(K,'BR15','Prateleira interna',           62, 56, 2)
enc(K,'TA','Lateral aparente',            244, 60, 2)
enc(K,'TA','Travessa de topo',            130, 60, 1)
enc(K,'DB','Prateleira',                   80, 20, 1)
f(K, dobr=4*2, sup=2)
t(K, 1.30*PASSANTE_M + 1.30*CAVA_M)

# ══════════════════════════════════════════════════════════════════════════
# PAVIMENTO 9
# ══════════════════════════════════════════════════════════════════════════

K = 'Cozinha 9° · bancada'
# 3,65 × 2,45 × 83 ⭐ profundidade confirmada pelo Jonathan
a(K,'DB18','Porta de aéreo',               41, 60, 2)
a(K,'DB18','Porta de aéreo',               41, 50, 1)
a(K,'DB18','Porta de aéreo',               41, 51, 2)
a(K,'DB18','Porta de aéreo (sobre geladeira)', 41, 84, 1)
a(K,'BR15','Aéreo · lateral e divisória',  41, 38, 7)
a(K,'BR15','Aéreo · base e tampo',        178, 38, 4)
a(K,'BR6' ,'Aéreo · fundo',               178, 41, 2)
a(K,'TA18','Frente de gaveta',             20, 63, 4)
a(K,'TA18','Frente de gaveta',             20, 49, 4)
a(K,'TA18','Porta inferior',               85, 56, 1)
a(K,'TA18','Porta inferior',               85, 51, 2)
a(K,'BR15','Inferior · lateral e divisória', 85, 80, 6)
a(K,'BR15','Inferior · base e travessa',  138, 80, 4)
a(K,'BR6' ,'Inferior · fundo',            220, 173, 1)
a(K,'BR15','Caixa de gaveta',              75, 15, 16)
a(K,'BR6' ,'Fundo de gaveta',              75, 55, 8)
a(K,'BR15','Fechamento do vão da geladeira', 200, 83, 1)
enc(K,'TA','Lateral aparente',            245, 83, 2)
enc(K,'TA','Travessa de topo',            365, 83, 1)
enc(K,'TA','Rodapé',                      365,  5, 1)
enc(K,'DB','Prateleira curta',            120, 25, 1)
enc(K,'DB','Prateleira longa',            155, 25, 1)
f(K, dobr=6*2 + 3*2, corr=8, sup=0)
t(K, 2.76*CAVA_M)

# ══════════════════════════════════════════════════════════════════════════
# HALL DOS ELEVADORES — ⭐ o detalhe se repete nos DOIS pavimentos
# ══════════════════════════════════════════════════════════════════════════
for pav in ('8', '9'):
    K = f'Hall {pav}° · painel ripado azul petróleo'
    # 6,78 × 2,80, ripado de passo 5,0 cm, com duas portas mimetizadas
    # ⛔⛔ O PAINEL TEM 2,80 E A CHAPA TEM 2,75. Ver FLAG 6: o pano ripado
    #    para em 2,73 [Jonathan 01/10] e o que sobra até o teto vira a sanca
    #    que a própria prancha já pede para a iluminação indireta.
    #    Sem isso, emenda horizontal no meio do ripado, no hall do elevador.
    a(K,'AP18','Painel ripado',           273, 63, 8)      # 5,04 de painel
    a(K,'AP18','Porta mimetizada do hidrante', 216, 75, 1)
    a(K,'AP18','Porta mimetizada da escada',   216, 95, 1)
    a(K,'AP18','Bandeira sobre a porta',   57, 75, 1)
    a(K,'AP18','Bandeira sobre a porta',   57, 95, 1)
    a(K,'AP18','Sanca de iluminação',     226, 20, 3)      # prateleira do LED
    a(K,'BR15','Montante e sarrafo',      273, 10, 14)
    a(K,'AT18','Nicho · fundo e laterais',140, 40, 2)
    a(K,'AT18','Nicho · base e topo',     140, 10, 4)
    a(K,'AT18','Nicho · lateral',          40, 10, 4)
    f(K, dobr=2*4)
    t(K, 6.78*2.80*RIPADO_M2 + 6.78*LED_M + 2.16*CAVA_M)

    K = f'Hall {pav}° · painel liso Tauari'
    # 4,74 × 2,80, liso, com o vão da porta dupla de vidro (vidro não é nosso)
    a(K,'TA18','Painel',                  273, 52, 6)
    a(K,'TA18','Retorno de topo',         273, 25, 2)
    a(K,'TA18','Marco do vão de vidro',   273, 15, 2)
    a(K,'TA18','Bandeira sobre o vão',     60, 93, 2)
    a(K,'TA18','Sanca de iluminação',     237, 20, 2)      # prateleira do LED
    a(K,'BR15','Montante e sarrafo',      273, 10, 8)
    t(K, 4.74*LED_M)

# ══════════════════════════════════════════════════════════════════════════
# PRATELEIRAS SUSPENSAS  (folha 15 · posições nas folhas 3 e 4)
# ⭐ [Jonathan] suporte oculto de 40 em 40 cm, R$ 30 a unidade
# ══════════════════════════════════════════════════════════════════════════
PRAT = (('01', 2.31, 2, '8'), ('02', 4.00, 2, '8'), ('03', 3.40, 1, '8'),
        ('02', 4.00, 1, '9'), ('04', 3.69, 1, '9'), ('05', 5.00, 1, '9'))
for cod, ext, qt, pav in PRAT:
    K = f'Prateleiras {pav}° · suspensas'
    # 30 de profundidade × 3 de espessura: duas faces de 6 + miolo
    a(K,'TA6','Prateleira · face',        ext*100, 30, qt*2)
    a(K,'TA6','Prateleira · testeira',    (ext*100+30)*2, 3, qt)
    ENCA[K] += ext*0.30*qt
    f(K, supocu=ceil(ext/0.40)*qt)

# ══════════════════════════════════════════════════════════════════════════
# QUADROS DE ENERGIA  (folha 19.1) — 2 no pav. 8 e 2 no pav. 9
# ══════════════════════════════════════════════════════════════════════════
for pav in ('8', '9'):
    K = f'Quadros de energia {pav}°'
    a(K,'AP18','Porta',                   210, 75, 4)      # 2 un × 2 portas
    a(K,'AP18','Marco · montante',        210, 10, 6)
    a(K,'AP18','Marco · travessa',        150, 10, 4)
    a(K,'BR15','Contramarco de fixação',  210,  8, 6)
    f(K, dobr=4*3, fecha=2)

# ══════════════════════════════════════════════════════════════════════════
# CÁLCULO
# ══════════════════════════════════════════════════════════════════════════
def _pack(pcs):
    ch, y, x, hf = 1, 0.0, 0.0, 0.0
    for c, l in pcs:
        if l > CH_L: c, l = l, c
        if c > CH_C:
            n = -(-int(c*1000)//int(CH_C*1000)); c = c/n
        if x + c <= CH_C and l <= hf:
            x += c; continue
        if y + l <= CH_L:
            y += hf if hf else 0
            if y + l > CH_L: ch += 1; y, hf = 0.0, 0.0
            x, hf = c, l
            continue
        ch += 1; y, x, hf = 0.0, c, l
    return ch

def nest(items):
    if not items: return 0
    base = sorted(((max(c, l), min(c, l)) for c, l in items), key=lambda q: (-q[1], -q[0]))
    ch = _pack(base)
    ar = sum(c*l for c, l in items)/10000
    piso = -(-int(ar/(CH_AREA*0.85)*1000)//1000) or 1
    return max(ch, piso)

area_mov, fita_mov = defaultdict(float), defaultdict(float)
por, area = defaultdict(list), defaultdict(float)
amov = defaultdict(lambda: defaultdict(float))
for mov, mat, d, c, l, q in p:
    # peça mais longa que a chapa é emendada: entra como n módulos
    n = max(1, ceil(max(c, l)/CH_C))
    cc = c/n if c >= l else c
    ll = l/n if l > c else l
    qq = q*n
    area_mov[mov] += c*l*q/10000
    fita_mov[mov] += (c + l)*2/100*q * (0.55 if mat.startswith('BR') else 0.75)
    for _ in range(qq): por[mat].append((cc, ll))
    area[mat]      += c*l*q/10000
    amov[mat][mov] += c*l*q/10000

CH = {m: nest(v) for m, v in por.items()}
ar_tot = sum(area.values())
custo_chapa = sum(CH[m]*PRECO[m] for m in CH)

chapa_mov = defaultdict(float)
for m, n in CH.items():
    tot = sum(amov[m].values())
    for mov, v in amov[m].items(): chapa_mov[mov] += n*PRECO[m]*v/tot

_com = list(dict.fromkeys(x[0] for x in p))
MOVS = _com + [k for k in dict.fromkeys(list(FER)+list(TER)) if k not in _com]
fita_custo = {mov: fita_mov[mov]*1.10*((FITA_BR+FITA_COR)/2) for mov in MOVS}
enc_custo  = {mov: ENCA[mov]*ENCORP_M2 for mov in MOVS}

# ── logística ⭐ valores fechados do Jonathan, São Paulo capital ──────────
# ⛔ o modelo regional de `logistica.md` NÃO se aplica: é outra praça.
LOG = dict(carreto=8000.0, equipe=2500.0, estadia=4000.0, hora_extra=1500.0)
LOG_TOT = sum(LOG.values())

PRECO_FER = dict(dobr=DOBR_UN, corr=CORR_UN, sup=SUP_PRAT,
                 supocu=SUP_OCU, fecha=FECHA_UN)
def custo_fer(mov): return sum(PRECO_FER[k]*q for k, q in FER[mov].items())

# ⭐ [Jonathan 01/10] "coloque esses custos de forma estratégica na proposta,
#   mais separada do valor dos móveis."
# ⛔ A logística SAI do rateio por item e vira BLOCO PRÓPRIO, precificado à
#   parte. O móvel passa a custar o que ele custa; a ida a São Paulo aparece
#   com nome e preço seus. Isso dá ao cliente uma linha identificável e dá à
#   casa uma linha que se renegocia sem reabrir o preço do móvel.
CDI = {}
for mov in MOVS:
    proprio = chapa_mov[mov] + fita_custo[mov] + enc_custo[mov]
    cons    = proprio*0.06
    CDI[mov] = (proprio + cons + TER[mov] + custo_fer(mov))*(1 + M.EMBALAGEM)
CD_MOV = sum(CDI.values())
CD     = CD_MOV + LOG_TOT*(1 + M.EMBALAGEM)
consum = sum((chapa_mov[m] + fita_custo[m] + enc_custo[m])*0.06 for m in MOVS)

# ── margem ────────────────────────────────────────────────────────────────
RT_ON, COMISSAO = True, False          # ⭐ [Jonathan] considere RT também
BASE = M.base(parcelas=0, rt=RT_ON, vendedor=COMISSAO)

MC_ITEM = {}
for mov in MOVS:
    b = 0.38
    if 'painel' in mov:                            b = 0.35
    if any(k in mov for k in ('ripado', 'Prateleiras', 'bancada alta')): b = 0.40
    MC_ITEM[mov] = b

AMB   = {mov: mov.split(' · ')[0] for mov in MOVS}
AMBS  = list(dict.fromkeys(AMB[m] for m in MOVS))
ITENS = {am: [m for m in MOVS if AMB[m] == am] for am in AMBS}
AR_AMB = {am: sum(area_mov[m] for m in ITENS[am]) for am in AMBS}
PAV = {am: ('9° pavimento' if ('9°' in am) else '8° pavimento') for am in AMBS}

CD_AMB  = {am: sum(CDI[m] for m in ITENS[am]) for am in AMBS}
MC_ALVO = {am: sum(CDI[m]*MC_ITEM[m] for m in ITENS[am])/CD_AMB[am] for am in AMBS}
PV      = {am: round(CD_AMB[am]/(BASE - MC_ALVO[am])/10)*10 for am in AMBS}
TOT_MOV = sum(PV.values())
MC_REAL = {am: BASE - CD_AMB[am]/PV[am] for am in AMBS}
assert abs(sum(CD_AMB.values()) - CD_MOV) < 0.01

# ── MOBILIZAÇÃO E LOGÍSTICA DE OBRA ──────────────────────────────────────
# ⚠ Separar NÃO é descontar. A mobilização leva os mesmos encargos do resto
#   (a NF, o RT e o rateio de produção caem sobre ela do mesmo jeito) e a MC
#   do conjunto, para que tirar a logística de dentro do móvel seja uma
#   mudança de APRESENTAÇÃO e não um corte de preço silencioso.
#   Ver, no fim, a escada do que cada alternativa custaria.
CD_MOB  = LOG_TOT*(1 + M.EMBALAGEM)
MC_MOB  = sum(CDI[m]*MC_ITEM[m] for m in MOVS)/CD_MOV      # MC média do job
PV_MOB  = round(CD_MOB/(BASE - MC_MOB)/10)*10
TOT     = TOT_MOV + PV_MOB

# ══════════════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    br = lambda v: f'{v:,.0f}'.replace(',', '.')
    W = 92
    print('═'*W)
    print('UNITED SP — pavimentos 8 e 9 · VD Arquitetura · executivo R08')
    print('═'*W)
    print(f'\nBASE {BASE*100:.2f}%   à vista · COM RT · sem comissão de venda')
    print(f'Ferragem: Hettich Sensys R$ {DOBR_UN:.0f}/un · oculta Quadro '
          f'R$ {CORR_UN:.0f}/par   ★ FLAG 1')

    print('\nPLANO DE CORTE')
    for m in sorted(CH, key=lambda k: (k[:2], k)):
        n = CH[m]
        print(f'  {NOME[m]:<16}{area[m]:>7.2f} m² → {n:>3} chapa × R$ {PRECO[m]:>5.0f} '
              f'= R$ {br(n*PRECO[m]):>7}   aprov. {area[m]/(n*CH_AREA)*100:>3.0f}%')
    tch = sum(CH.values())
    print(f'  {"TOTAL":<16}{ar_tot:>7.2f} m² → {tch:>3} chapas'
          f'                R$ {br(custo_chapa):>7}   médio '
          f'{ar_tot/(tch*CH_AREA)*100:.0f}%')

    print('\nABERTURA DO CUSTO DIRETO')
    fer = sum(custo_fer(m) for m in MOVS)
    emb = CD - (custo_chapa + sum(fita_custo.values()) + sum(enc_custo.values())
                + consum + LOG_TOT + fer + sum(TER.values()))
    for rot, v in (('chapa', custo_chapa), ('fita de borda', sum(fita_custo.values())),
                   ('miolo encorpado', sum(enc_custo.values())),
                   ('consumíveis', consum),
                   ('ferragem', fer), ('serviços e usinagem', sum(TER.values())),
                   ('embalagem (2%)', emb)):
        print(f'  {rot:<22}{br(v):>12}')
    print(f'  {"custo dos móveis":<22}{br(CD_MOV):>12}')
    print(f'  {"mobilização (à parte)":<22}{br(CD_MOB):>12}')
    print(f'  {"CUSTO DIRETO":<22}{br(CD):>12}')
    print(f'\n  mobilização [Jonathan]: ' +
          ' · '.join(f'{k} {br(v)}' for k, v in LOG.items()))

    print('\n' + '─'*W)
    print(f'{"ITEM":<40}{"m²":>7}{"CUSTO":>12}{"VENDA":>12}{"MC":>8}')
    print('─'*W)
    for pv in ('8° pavimento', '9° pavimento'):
        print(f'\n  {pv.upper()}')
        for am in AMBS:
            if PAV[am] != pv: continue
            print(f'    {am:<36}{AR_AMB[am]:>7.1f}{br(CD_AMB[am]):>12}'
                  f'{br(PV[am]):>12}{MC_REAL[am]*100:>7.1f}%')
        cc = sum(CD_AMB[a] for a in AMBS if PAV[a] == pv)
        vv = sum(PV[a] for a in AMBS if PAV[a] == pv)
        ar = sum(AR_AMB[a] for a in AMBS if PAV[a] == pv)
        print(f'    {"subtotal":<36}{ar:>7.1f}{br(cc):>12}{br(vv):>12}'
              f'{(BASE-cc/vv)*100:>7.1f}%')
    print('─'*W)
    print(f'  {"MÓVEIS":<38}{ar_tot:>7.1f}{br(CD_MOV):>12}{br(TOT_MOV):>12}'
          f'{(BASE-CD_MOV/TOT_MOV)*100:>7.1f}%')
    print(f'  {"Mobilização e logística de obra":<38}{"":>7}{br(CD_MOB):>12}'
          f'{br(PV_MOB):>12}{(BASE-CD_MOB/PV_MOB)*100:>7.1f}%')
    print(f'  {"TOTAL":<38}{"":>7}{br(CD):>12}{br(TOT):>12}'
          f'{(BASE-CD/TOT)*100:>7.1f}%')
    print('─'*W)

    print('\n⚠ A MOBILIZAÇÃO PRECISA LEVAR MARGEM — separar não é descontar')
    print(f'  {"como a mobilização é precificada":<44}{"bloco":>10}{"TOTAL":>12}{"Δ":>12}')
    for rot, mc in (('a custo seco, sem encargo nenhum', None),
                    ('só com os encargos, MC zero',      0.0),
                    ('MC 20%',                           0.20),
                    ('MC 30%',                           0.30),
                    (f'MC do conjunto ({MC_MOB*100:.1f}%)  ← entregue', MC_MOB)):
        v = LOG_TOT if mc is None else round(CD_MOB/(BASE-mc)/10)*10
        print(f'  {rot:<44}{br(v):>10}{br(TOT_MOV+v):>12}'
              f'{br(TOT_MOV+v-TOT):>12}')
    print('  Os encargos caem sobre a mobilização igual: a NF, o RT e o rateio')
    print('  de produção não perguntam se a linha é móvel ou caminhão.')

    print('\n★ FLAG 1 — e se a ferragem fosse a linha de entrada?')
    nd = sum(FER[m]['dobr'] for m in MOVS); nc = sum(FER[m]['corr'] for m in MOVS)
    eco = nd*(35-10) + nc*(120-40)
    print(f'  {nd:.0f} dobradiças e {nc:.0f} pares de corrediça.')
    print(f'  Novisys + telescópica custaria R$ {br(eco)} a menos de custo direto,')
    print(f'  ≈ R$ {br(eco/(BASE-0.38))} de venda — e a garantia cai de 10 para 2 anos.')
