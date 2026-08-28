# -*- coding: utf-8 -*-
"""DEVA VEÍCULOS (IVECO) — LEVANTAMENTO E PREÇO.

PROJETO EXECUTIVO DE MARCENARIA · AGO/2026 · revisão 00
Arquiteta BEATRIZ FERNANDEZ GONTIJO · CAU A 75464-1
Ofício Planejamento e Consultoria — Av. Prudente de Morais 44, BH

QUATRO PRANCHAS A1, TODAS CASO A (com camada de texto):
  EX01 · SETOR COMERCIAL · Balcão comercial ....... balcão + painel de parede
  EX02 · SETOR COMERCIAL · Sala dos motoristas .... painel TV + balcão café +
                                                    bancada janela
  EX03 · SETOR VENDAS ···· Marcenaria recepção .... balcão + painel de parede
  EX04 · SETOR VENDAS ···· Marcenaria vendas ...... painel/expositor de vidro +
                                                    espaço café

MÉTODO: cotas lidas das pranchas (planta, vistas e seções), não estimadas. As
pranchas cotam bem — tampos de 3 cm, frisos de 1×1, recuos de 3, alturas de
balcão 105 e bancada 75. Onde a prancha não fecha, está nas DÚVIDAS.

⚠️ BURACO DE ESCOPO CONHECIDO
   A planta da EX03 chama "PAINEL EM MARCENARIA PADRÃO DA IVECO. VER DETALHE
   ESPECÍFICO" — e esse detalhe NÃO está nas quatro pranchas. É painel de
   identidade de montadora, que costuma ter especificação própria (material,
   iluminação, aplicação de logo). NÃO ESTÁ NESTE ORÇAMENTO.

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

# ── nesting da casa ───────────────────────────────────────────────────────
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
PRC_COR = {6: 300.0, 15: 500.0, 18: 600.0, 25: 900.0}   # Melamínico Fosco
PRC_BRA = {6: 190.0, 15: 260.0, 18: 330.0, 25: 420.0}   # Branco TX
# ★ COR 25 mm não existe na base (para em 18 = 600). Adotado 900, como nos
#   motores anteriores da casa. Aqui pesa: são vários tampos de 3 cm.
NOME_MAT = {'AM': 'MDF amadeirado', 'BR': 'MDF Branco TX'}
def prc(m, e): return PRC_BRA[e] if m == 'BR' else PRC_COR[e]

FITA_M, FILET_M, DESPERD = 3.00, 2.50, 1.10
FRISO_M   = 2.50                   # usinagem de friso/bit decorativo, por metro
SUP_PRAT  = 1.50
LED_M     = 28.0 + 38.0            # fita 28 + perfil de alumínio 38
SARRAFO_M2 = 25.0                  # estrutura niveladora atrás dos painéis
PERFIL_INOX_M = 85.0               # ★ rodapé/recuo com perfil em INOX, por metro
                                   #   Não está na base. A base tem rodapé de
                                   #   alumínio a R$ 20/m; inox é outro produto.
                                   #   CONFIRMAR — são ~24 m no projeto.
VIDRO_PORTA_UN = 475.0             # porta de giro em vidro, perfil e ferragem
VIDRO_FIXO_M2  = 250.0             # vidro incolor temperado 8 mm
# ── LOGOS FORA DO ESCOPO  [Jonathan 25/08] "as logos nao precisa considerar"
#   As três logos IVECO saem do CUSTO. A LINHA CONTINUA no levantamento, com
#   valor zero, para que a proposta possa dizer que o painel PREVÊ a aplicação
#   da marca sem cobrar por ela — quem fornece é a montadora. Zerar e apagar
#   são coisas diferentes: apagada, a logo some do escopo e ninguém prevê o
#   recorte e o reforço no painel.
LOGO_UN = 0.0
METALON_M = 95.0                   # ★ estrutura de metalon interna, por metro

P, FITA, TERC, LED, FRISO, DUV = [], [], [], [], [], []
FER = defaultdict(lambda: [0, 0, 0])       # dobradiças · gavetas · básculas
SET = {}                                   # ambiente → setor
def add(mat, esp, amb, desc, c, l, q=1): P.append((mat, esp, amb, desc, c, l, q))
def fer(a, dobr=0, gav=0, basc=0):
    FER[a][0] += dobr; FER[a][1] += gav; FER[a][2] += basc
def fita(a, d, m): FITA.append((a, d, m))
def terc(a, d, v, est=False): TERC.append((a, d, v, est))
def led(a, d, m): LED.append((a, d, m))
def friso(a, m): FRISO.append((a, m))
def duv(a, t): DUV.append((a, t))
def setor(a, s): SET[a] = s
# A chapa é 275 × 185. Painel de parede se pagina em FAIXAS VERTICAIS: a
# altura vira o comprimento da peça (até 270) e a largura da faixa vai até 180.
# Painel mais alto que 270 precisa de duas bandas horizontais, com emenda.
LIM_C, LIM_L = 270.0, 180.0

def _partir(c, l):
    """Devolve as peças em que um retângulo c × l precisa ser dividido para
       caber na chapa. Sempre orienta o maior lado no comprimento."""
    if c < l: c, l = l, c
    nc = max(1, math.ceil(c/LIM_C))
    nl = max(1, math.ceil(l/LIM_L))
    return [(c/nc, l/nl)]*(nc*nl)

def peca(mat, esp, amb, desc, c, l, q=1):
    """add() que parte a peça se ela não couber na chapa."""
    ps = _partir(c, l)
    if len(ps) == 1:
        add(mat, esp, amb, desc, ps[0][0], ps[0][1], q)
    else:
        cc, ll = ps[0]
        add(mat, esp, amb, f'{desc} · {len(ps)} peças de {cc*10:.0f} × {ll*10:.0f}',
            cc, ll, q*len(ps))

def painel(mat, amb, desc, larg, alt, esp=15, sarrafo=True):
    """Painel de parede: chapa paginada em faixas + estrutura niveladora."""
    peca(mat, esp, amb, desc, larg, alt, 1)
    if sarrafo:
        terc(amb, f'{desc} · estrutura niveladora',
             larg/100*alt/100*SARRAFO_M2)

# ═══════════════════════════════════════════════════════════════════════════
# GEOMETRIA — cotas das pranchas. Tudo em cm.
# ═══════════════════════════════════════════════════════════════════════════

# ───────────────────────────────────────────────────────────────────────────
# EX01 · SETOR COMERCIAL — PAINEL DE PAREDE DO BALCÃO
#   206 × 260. Divisão DIAGONAL: branco 90 no topo → 130 na base;
#   amadeirado 116 no topo → 76 na base. Logo IVECO. LED a H=120.
# ───────────────────────────────────────────────────────────────────────────
A = 'EX01 · Painel do balcão comercial'; setor(A, 'Comercial')
painel('BR', A, 'painel branco (trecho diagonal)', 110, 260)   # média 90–130
painel('AM', A, 'painel amadeirado (trecho diagonal)', 96, 260)  # média 116–76
peca('BR', 15, A, 'rodapé recuado', 206, 8, 1)
fita(A, 'painel · bordas aparentes e diagonal', 2*2.60 + 2*2.06 + 3.20)
led(A, 'fita LED 5W 3000K embutida no painel (H=120)', 2.06)
terc(A, 'Perfil em INOX no recuo junto ao piso', 2.06*PERFIL_INOX_M, est=True)
terc(A, 'Logo IVECO aplicada no painel', LOGO_UN, est=True)
duv(A, 'a divisão entre branco e amadeirado é DIAGONAL (90→130 no branco, '
       '116→76 no amadeirado). Calculei pela área do trapézio. O corte '
       'diagonal desperdiça chapa e a prancha não cota o ângulo: conferir no '
       'CAD antes do plano de corte definitivo.')

# ───────────────────────────────────────────────────────────────────────────
# EX01 · BALCÃO COMERCIAL — H=105 com bancada interna H=75
#   Frente 191 (161+30) · profundidade em planta 124 · bancada de 45
#   Frente: 129 branco + 58 amadeirado escalonado (faixas 15/18/22/18/15)
# ───────────────────────────────────────────────────────────────────────────
A = 'EX01 · Balcão comercial'; setor(A, 'Comercial')
add('BR', 25, A, 'tampo do balcão 1910 × 750',        191, 75, 1)
add('BR', 18, A, 'frente branca 1290 × 1050',         129, 105, 1)
add('AM', 18, A, 'frente amadeirada escalonada 580 × 1050', 58, 105, 1)
add('AM', 18, A, 'lateral amadeirada 750 × 1050',      75, 105, 1)
add('BR', 15, A, 'lateral com fundo falso p/ tomadas', 75, 105, 1)
add('BR', 15, A, 'fundo do balcão 1760 × 820',        176, 82, 1)
add('BR', 25, A, 'bancada interna H=75 · tampo 1610 × 450', 161, 45, 1)
add('BR', 15, A, 'bancada interna · apoio vertical',   45, 72, 2)
add('BR', 15, A, 'travessa estrutural do balcão',     176, 15, 3)
peca('BR', 15, A, 'rodapé recuado',                   191, 8, 1)
fita(A, 'balcão · tampo, frentes e laterais',
     2*(1.91+0.75) + 2*(1.29+1.05) + 2*(0.58+1.05) + 2*(0.75+1.05)
     + 2*(1.61+0.45))
led(A, 'fita LED 5W 3000K embutida no balcão (H=60)', 1.91)
terc(A, 'Perfil em INOX no recuo junto ao piso', (1.91+2*0.75)*PERFIL_INOX_M, est=True)
duv(A, 'a frente amadeirada de 58 tem 5 faixas (15/18/22/18/15) num vão de '
       '102. A prancha não diz se é RIPADO decorativo ou frente de gavetas — '
       'orcei como frente escalonada MACIÇA, sem gaveta. Se forem gavetas, '
       'entram 5 pares de corrediça e 5 caixas.')
duv(A, 'a lateral com FUNDO FALSO para transferência das tomadas aparece em '
       'duas vistas mas não é cotada em profundidade. Adotei 75, igual ao '
       'tampo.')

# ───────────────────────────────────────────────────────────────────────────
# EX02 · SALA DOS MOTORISTAS — PAINEL TV
#   416 × 260, MDF padrão madeirado com FRISOS de 1×1 cm usinados.
#   Faixas horizontais de 75 / 99 / 85. Rack de apoio suspenso 120 × 22.
# ───────────────────────────────────────────────────────────────────────────
A = 'EX02 · Painel de TV'; setor(A, 'Comercial')
painel('AM', A, 'painel amadeirado com frisos', 416, 260)
peca('BR', 15, A, 'rodapé recuado', 416, 8, 1)
# frisos 1×1: 3 linhas horizontais em toda a largura + as verticais das faixas
friso(A, 3*4.16 + 2*2.60)
fita(A, 'painel · bordas aparentes', 2*2.60 + 2*4.16)
# rack de apoio suspenso em laminado branco 120 × 25 × 22
add('BR', 18, A, 'rack de apoio · tampo e base 1200 × 250', 120, 25, 2)
add('BR', 18, A, 'rack de apoio · laterais 250 × 220',       25, 22, 2)
add('BR', 6,  A, 'rack de apoio · fundo',                   120, 22, 1)
fita(A, 'rack · frentes e topos', 2*(1.20+2*0.25) + 2*(0.22+0.25))
terc(A, 'Perfil em ALUMÍNIO POLIDO no rodapé recuado', 4.16*45.0, est=True)
duv(A, 'a prancha manda "PREVER ESTRUTURA INTERNA NO DRY WALL" — a estrutura é '
       'da obra, não nossa. Mas o painel de 4,16 m precisa de sarrafeamento '
       'nosso por trás, que está no valor.')

# ───────────────────────────────────────────────────────────────────────────
# EX02 · BALCÃO CAFÉ — 250 × 50 × 90, MDF TX branco
#   Armário inferior com 6 portas de giro · bancada + rodabanca de 30
#   Puxador: DET.01, cava usinada de 2,5 cm
# ───────────────────────────────────────────────────────────────────────────
A = 'EX02 · Balcão café'; setor(A, 'Comercial')
add('BR', 25, A, 'bancada 2500 × 500',            250, 50, 1)
add('BR', 15, A, 'rodabanca 2500 × 300',          250, 30, 1)
add('BR', 15, A, 'lateral do armário 500 × 900',   50, 90, 2)
add('BR', 15, A, 'divisória do armário',           50, 78, 5)
add('BR', 15, A, 'base do armário',               242, 50, 1)
add('BR', 6,  A, 'fundo do armário',              242, 78, 1)
add('BR', 18, A, 'prateleira interna',             40, 46, 6)
add('BR', 18, A, 'porta de giro 410 × 620',        41, 62, 6)
peca('BR', 15, A, 'rodapé recuado',               250, 10, 1)
fer(A, dobr=12)
fita(A, 'balcão café · bancada, rodabanca, portas e prateleiras',
     2*(2.50+0.50) + 2*2.50 + 6*2*(0.41+0.62) + 6*(0.40+2*0.46))
terc(A, 'Perfil em INOX no rodapé recuado', 2.50*PERFIL_INOX_M, est=True)
friso(A, 6*0.41)                         # cava usinada de 2,5 cm (DET.01)

# ───────────────────────────────────────────────────────────────────────────
# EX02 · BANCADA JANELA — 250 × 45 × 90, MDF padrão amadeirado
#   Estrutura em METALON interna. Laterais de 6. Vão livre 238.
# ───────────────────────────────────────────────────────────────────────────
A = 'EX02 · Bancada da janela'; setor(A, 'Comercial')
add('AM', 25, A, 'tampo 2500 × 450',      250, 45, 1)
add('AM', 18, A, 'lateral 450 × 900',      45, 90, 2)
add('AM', 18, A, 'saia frontal 2380 × 60', 238, 6, 1)
fita(A, 'bancada · tampo, laterais e saia', 2*(2.50+0.45) + 2*2*(0.45+0.90) + 2.38)
terc(A, 'Estrutura em metalon interna (serralheria)',
     (2*2.50 + 3*0.45)*METALON_M, est=True)
duv(A, 'a prancha manda "PREVER ESTRUTURA EM METALON INTERNA" e não a '
       'dimensiona. Orcei um quadro perimetral com três travessas. Se a '
       'serralheria pedir seção maior, o item sobe.')

# ───────────────────────────────────────────────────────────────────────────
# EX03 · SETOR VENDAS — PAINEL DA RECEPÇÃO
#   258 × 260, diagonal: amadeirado 145→100, branco 113→158. Logo IVECO.
#   Projeção de TV 50" no trecho branco (TV do cliente). LED a H=120.
#   Mais um painel branco lateral de 230 de altura.
# ───────────────────────────────────────────────────────────────────────────
A = 'EX03 · Painel da recepção'; setor(A, 'Vendas')
painel('AM', A, 'painel amadeirado (trecho diagonal)', 122, 260)  # média 145–100
painel('BR', A, 'painel branco (trecho diagonal)',     136, 260)  # média 113–158
painel('BR', A, 'painel branco lateral',               100, 230)
peca('BR', 15, A, 'rodapé recuado', 358, 8, 1)
fita(A, 'painéis · bordas aparentes e diagonal', 4*2.60 + 2*3.58 + 3.20)
led(A, 'fita LED 5W 3000K embutida no painel (H=120)', 2.58)
terc(A, 'Perfil em INOX no recuo junto ao piso', 3.58*PERFIL_INOX_M, est=True)
terc(A, 'Logo IVECO aplicada no painel', LOGO_UN, est=True)

# ───────────────────────────────────────────────────────────────────────────
# EX03 · BALCÃO DA RECEPÇÃO — em U, H=105 com bancada interna H=75
#   Planta: 250 (30 + 190 + 30) · bancada de 45 · profundidade 90/75
#   Vista 02: frente 105 + 10 + 105 = 220, frentes de 44/66/66/44
#   Vista 01: trecho amadeirado ripado + brancos de 171 e 176
# ───────────────────────────────────────────────────────────────────────────
A = 'EX03 · Balcão da recepção'; setor(A, 'Vendas')
add('BR', 25, A, 'tampo do balcão 2500 × 900',        250, 90, 1)
add('BR', 25, A, 'tampo do retorno 900 × 900',         90, 90, 2)
add('BR', 18, A, 'frente branca 1710 × 1050',         171, 105, 1)
add('BR', 18, A, 'frente branca 1760 × 1050',         176, 105, 1)
add('AM', 18, A, 'frente amadeirada ripada 440 × 1050', 44, 105, 2)
add('AM', 18, A, 'lateral amadeirada 900 × 1050',      90, 105, 2)
add('BR', 15, A, 'montante com fundo falso p/ tomadas', 90, 105, 2)
add('BR', 25, A, 'bancada interna H=75 · tampo 1900 × 450', 190, 45, 1)
add('BR', 15, A, 'bancada interna · apoio vertical',   45, 72, 3)
add('BR', 15, A, 'fundo do balcão',                   190, 82, 1)
add('BR', 15, A, 'travessa estrutural',               190, 15, 4)
peca('BR', 15, A, 'rodapé recuado',                   430, 8, 1)
fita(A, 'balcão · tampos, frentes e laterais',
     2*(2.50+0.90) + 2*2*(0.90+0.90) + 2*(1.71+1.05) + 2*(1.76+1.05)
     + 2*2*(0.44+1.05) + 2*2*(0.90+1.05) + 2*(1.90+0.45))
led(A, 'fita LED 5W 3000K embutida no balcão', 2.50 + 2*0.90)
terc(A, 'Perfil em INOX no recuo junto ao piso', 4.30*PERFIL_INOX_M, est=True)
terc(A, 'Porta baixa de acesso em vidro temperado, de correr',
     VIDRO_PORTA_UN, est=True)
duv(A, 'o balcão da recepção é em U e as vistas 01 e 02 cotam trechos que não '
       'fecham entre si (220 na vista 02 contra 171+176 na vista 01). Adotei o '
       'desenvolvimento da PLANTA — 250 de frente com dois retornos de 90 — '
       'que é a cota mais confiável. CONFERIR em obra.')

# ───────────────────────────────────────────────────────────────────────────
# EX04 · PAINEL/EXPOSITOR — SETOR VENDAS
#   Painel amadeirado 270 × 276 com reforço estrutural (TV 85" do cliente)
#   Expositor suspenso 220 × 60 × 72, a 109 do piso:
#     5 portas de giro em VIDRO INCOLOR (43/43/44/43/43)
#     fechamento lateral em vidro fixo · montante interno vertical em vidro
# ───────────────────────────────────────────────────────────────────────────
A = 'EX04 · Painel e expositor'; setor(A, 'Vendas')
painel('AM', A, 'painel amadeirado com reforço estrutural', 270, 276)
peca('BR', 15, A, 'rodapé recuado', 270, 8, 1)
fita(A, 'painel · bordas aparentes', 2*2.76 + 2*2.70)
add('AM', 25, A, 'expositor · tampo 2200 × 600',   220, 60, 1)
add('AM', 25, A, 'expositor · base suspensa 2200 × 600', 220, 60, 1)
add('AM', 18, A, 'expositor · lateral 600 × 640',   60, 64, 2)
add('AM', 6,  A, 'expositor · fundo aparente',     220, 64, 1)
fita(A, 'expositor · todas as bordas à vista',
     2*2*(2.20+0.60) + 2*2*(0.60+0.64))
terc(A, 'Cinco portas de giro em vidro incolor, com ferragem',
     5*VIDRO_PORTA_UN, est=True)
terc(A, 'Fechamento lateral e montante interno em vidro fixo',
     (2*0.60*0.64 + 0.64*0.60)*VIDRO_FIXO_M2, est=True)
terc(A, 'Logo IVECO aplicada na divisória', LOGO_UN, est=True)
duv(A, 'o expositor é SUSPENSO e fecha em vidro nos cinco vãos. A prancha '
       'manda "PREVER REFORÇO NA DIVISÓRIA PARA FIXAÇÃO DO MÓVEL" — a '
       'divisória de vidro é EXISTENTE e o reforço dela é da obra, não nosso. '
       'CONFIRMAR quem executa.')

# ───────────────────────────────────────────────────────────────────────────
# EX04 · ESPAÇO CAFÉ — SETOR VENDAS
#   Painel amadeirado de cantos arredondados R26: 229 × 218, moldura branca
#   de 4 cm. Fundo em MDF amadeirado. Bancada branca com armário amadeirado
#   de 4 portas (42/43/42/42), H=90. Ponto de água para filtro a H=130.
# ───────────────────────────────────────────────────────────────────────────
A = 'EX04 · Espaço café'; setor(A, 'Vendas')
painel('AM', A, 'fundo amadeirado do nicho (cantos R26)', 229, 218)
add('BR', 18, A, 'moldura branca do nicho · vertical', 4, 218, 2)
add('BR', 18, A, 'moldura branca do nicho · horizontal', 229, 4, 2)
fita(A, 'nicho · moldura e curvas', 2*(2.29+2.18) + 2*(2.29+2.18))
add('BR', 25, A, 'bancada 1690 × 450',            169, 45, 1)
add('AM', 15, A, 'lateral do armário 450 × 830',   45, 83, 2)
add('AM', 15, A, 'divisória do armário',           45, 71, 3)
add('AM', 15, A, 'base do armário',               161, 45, 1)
add('AM', 6,  A, 'fundo do armário',              161, 71, 1)
add('AM', 18, A, 'prateleira interna',             40, 41, 4)
add('AM', 18, A, 'porta de giro 420 × 710',        42, 71, 4)
peca('BR', 15, A, 'rodapé recuado',               169, 10, 1)
fer(A, dobr=8)
fita(A, 'espaço café · bancada, portas e prateleiras',
     2*(1.69+0.45) + 4*2*(0.42+0.71) + 4*(0.40+2*0.41))
terc(A, 'Perfil em INOX no rodapé recuado', 1.69*PERFIL_INOX_M, est=True)
duv(A, 'a prancha escreve "BANCADA EM MDF BRANCO COM ARMÁRIO EM MDF '
       'AMADEIRADO", mas o RENDER da própria prancha mostra o armário CLARO, '
       'não amadeirado. Segui o texto (armário amadeirado). Se o render é que '
       'vale, o armário vai para branco e o custo cai.')
duv(A, 'os cantos do nicho são arredondados em R26 e a moldura branca '
       'acompanha a curva. Curva de raio 26 em moldura de 4 cm de largura sai '
       'de peça usinada, não de chapa dobrada — o corte tem perda alta e não '
       'está separado no plano.')

# ═══════════════════════════════════════════════════════════════════════════
# CÁLCULO
# ═══════════════════════════════════════════════════════════════════════════
FER_LINHA = dict(nome='Hettich', dobr=10.0, corr=120.0, basc=250.0)
N_CARRETO, R_CARRETO = 5, 600.0
N_VISITA,  R_VISITA  = 4, 250.0
LOG = N_CARRETO*R_CARRETO + N_VISITA*R_VISITA
ESCADA = [0.35, 0.38, 0.40]
MC_FECHADA, RT_FECHADO = 0.35, True   # [Jonathan 25/08] MC 35% COM RT

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
m_friso = sum(m for _, m in FRISO); custo_friso = m_friso*FRISO_M
m_led = sum(m for _, _, m in LED); custo_led = m_led*LED_M
N_PRAT = sum(q for m, e, a, d, c, l, q in P if 'prateleira' in d.lower())
custo_sup = N_PRAT*4*SUP_PRAT
custo_terc = sum(v for _, _, v, _ in TERC)
TOT_D = sum(f[0] for f in FER.values())
TOT_G = sum(f[1] for f in FER.values())
TOT_B = sum(f[2] for f in FER.values())
custo_ferr = TOT_D*FER_LINHA['dobr'] + TOT_G*FER_LINHA['corr'] + TOT_B*FER_LINHA['basc']
consum = (custo_chapa + custo_fita)*0.06
CD = (custo_chapa + custo_fita + custo_filet + custo_friso + custo_led + custo_sup
      + custo_terc + consum + custo_ferr + LOG)

def brl(v, n=2):
    return f'{v:,.{n}f}'.replace(',', '§').replace('.', ',').replace('§', '.')

_fora = [(m, e, a, d, c, l) for m, e, a, d, c, l, q in P
         if max(c, l) > CH_C or min(c, l) > CH_L]
if _fora:
    print('\n' + '!'*W + '\nPEÇAS QUE NÃO CABEM NA CHAPA DE 275 × 185')
    for m, e, a, d, c, l in _fora:
        print(f'  {NOME_MAT[m]} {e} mm · {a} · {d}: {c:.0f} × {l:.0f} cm')
    print('!'*W + '\n')

print('═'*W)
print('DEVA VEÍCULOS (IVECO) — LEVANTAMENTO DE MATERIAL E CUSTO')
print('═'*W)
print('Projeto executivo de marcenaria · arq. Beatriz Fernandez Gontijo · AGO/2026 rev.00')
print('4 pranchas A1 · 2 setores · 9 conjuntos · cotas lidas das pranchas')

print('\nESCOPO POR CONJUNTO')
_st = None
for a in ordem:
    if SET[a] != _st:
        _st = SET[a]; print(f'  ── SETOR {_st.upper()}')
    d, g, b = FER[a]
    ex = [f'{d} dobr.' if d else '', f'{g} gav.' if g else '', f'{b} básc.' if b else '']
    print(f'    {a:<38}{area_amb[a]:>7.2f} m²   {" · ".join(x for x in ex if x)}')
print(f'    {"TOTAL":<38}{area_tot:>7.2f} m²')

print('\nPLANO DE CORTE  (nesting por cor × espessura)')
for k in sorted(CH, key=lambda k: (k[0], -k[1])):
    m, e = k; n = CH[k]; pr = prc(m, e); ap = area_ch[k]/(n*CH_AREA)*100
    print(f'  {NOME_MAT[m]+" "+str(e)+" mm":<26}{area_ch[k]:>7.2f} m²  →  {n:>2} ch. × '
          f'R$ {brl(pr):>8} = R$ {brl(n*pr):>10}   aprov. {ap:>3.0f}%')
print(f'  {"TOTAL":<26}{area_tot:>7.2f} m²  →  {tot_ch:>2} chapas{"":>20}'
      f'R$ {brl(custo_chapa):>10}   médio {area_tot/(tot_ch*CH_AREA)*100:.0f}%')

print(f'\nFITA E FILETAGEM   {m_fita:.2f} m  ·  material R$ {brl(custo_fita)}'
      f'  ·  filetagem R$ {brl(custo_filet)}')
print(f'  (borda peça a peça: {m_fita_expl:.1f} m = {m_fita_expl/area_tot:.2f} m/m²'
      f' · fator da casa 2,6 — o maior manda)')
print(f'FRISOS E CAVAS     {m_friso:.2f} m × R$ {brl(FRISO_M)}/m  ·  R$ {brl(custo_friso)}')
print(f'ILUMINAÇÃO         {m_led:.2f} m × R$ {brl(LED_M)}/m  ·  R$ {brl(custo_led)}')

print('\nTERCEIRIZADOS E ITENS ESPECIAIS   (★ = sem preço fechado na base)')
for a, d, v, est in TERC:
    print(f' {"★" if est else " "}{a:<32}{d[:44]:<45}R$ {brl(v):>10}')
print(f'  {"TOTAL":<78}R$ {brl(custo_terc):>10}')
print(f'\nFERRAGEM {FER_LINHA["nome"]} — {TOT_D} dobradiças · {TOT_G} corrediças · '
      f'{TOT_B} articuladores · {N_PRAT} prateleiras')

print('\n' + '═'*W)
print('CUSTO DIRETO')
print('═'*W)
for rot, v in (('Chapas', custo_chapa), ('Fita (material)', custo_fita),
               ('Filetagem', custo_filet), ('Frisos e cavas usinados', custo_friso),
               ('Iluminação em LED', custo_led),
               ('Suportes de prateleira', custo_sup),
               ('Terceirizados (vidro, inox, metalon, logos, sarrafo)', custo_terc),
               ('Consumíveis (6% de chapa + fita)', consum),
               ('Ferragem', custo_ferr),
               (f'Logística — {N_CARRETO} carretos + {N_VISITA} visitas '
                f'(montagem NÃO entra: é custo fixo)', LOG)):
    print(f'    {rot:<76}R$ {brl(v):>10}')
print(f'    {"CUSTO DIRETO":<76}R$ {brl(CD):>10}')

print('\n' + '═'*W)
print('PREÇO — escada de MC, com e sem RT')
print('═'*W)
print(f'  {"MC":<6}{"sem RT":>14}{"MC real":>10}   {"com RT 10%":>14}{"MC real":>10}')
PRECOS = {}
for mc in ESCADA:
    s = round(CD/div(mc, False)/100)*100
    r = round(CD/div(mc, True)/100)*100
    PRECOS[mc] = (s, r)
    print(f'  {mc*100:>4.0f}%{"R$ "+brl(s,0):>14}{mc_conferida(s, CD)*100:>9.1f}%   '
          f'{"R$ "+brl(r,0):>14}{mc_conferida(r, CD)*100:>9.1f}%')
REC = MC_FECHADA
INV_SEM, INV = PRECOS[REC]
if not RT_FECHADO: INV, INV_SEM = INV_SEM, INV
print(f'\n  ► FECHADO · MC {REC*100:.0f}% {"COM" if RT_FECHADO else "SEM"} RT '
      f'......... R$ {brl(INV,0)}     [Jonathan 25/08]')
print(f'    sem RT, referência interna ........... R$ {brl(INV_SEM,0)}')
rm = INV_SEM/area_tot
print(f'  R$/m² de chapa: {rm:.0f} sem RT · {INV/area_tot:.0f} com RT'
      f'   (faixa da casa sem RT: 626–834)')
if not 626 <= rm <= 834:
    print('  ⚠ FORA DA FAIXA — conferir o levantamento.')

print('\n' + '─'*W)
print(f'INVESTIMENTO POR CONJUNTO   (MC {REC*100:.0f}% COM RT · rateio por área de chapa)')
tots, linhas = 0, []
for a in ordem:
    v = round(INV*area_amb[a]/area_tot/100)*100
    linhas.append([a, area_amb[a], v]); tots += v
linhas[max(range(len(linhas)), key=lambda i: linhas[i][1])][2] += INV - tots
_st = None
for a, ar, v in linhas:
    if SET[a] != _st:
        _st = SET[a]; print(f'  ── SETOR {_st.upper()}')
    print(f'    {a:<38}{ar:>8.2f} m²{"R$ "+brl(v,0):>14}')
print(f'    {"TOTAL":<38}{area_tot:>8.2f} m²{"R$ "+brl(INV,0):>14}')
for s in ('Comercial', 'Vendas'):
    v = sum(x[2] for x in linhas if SET[x[0]] == s)
    print(f'  Setor {s:<12}{"R$ "+brl(v,0):>20}')

print('\n' + '─'*W)
print(f'DÚVIDAS E CONFERÊNCIAS — {len(DUV)} itens')
for i, (a, t) in enumerate(DUV, 1):
    print(f'  {i:>2}. [{a}]\n      {t}')

print('\n' + '!'*W)
print('BURACO DE ESCOPO — NÃO ESTÁ NESTE VALOR')
print('!'*W)
print('  A planta da EX03 chama "PAINEL EM MARCENARIA PADRÃO DA IVECO — VER')
print('  DETALHE ESPECÍFICO". Esse detalhe NÃO veio nas quatro pranchas.')
print('  Painel de identidade de montadora tem especificação própria de')
print('  material, iluminação e aplicação de marca. Sem a prancha, não há o')
print('  que orçar — e sem avisar, vira falta descoberta na obra.')

print('\n  ★ Preços sem linha fechada na base de materiais:')
print(f'     · PERFIL EM INOX — adotei R$ {brl(PERFIL_INOX_M,0)}/m. A base só tem')
print('       rodapé de ALUMÍNIO a R$ 20/m, que é outro produto. São ~14 m de')
print('       inox no projeto: se o custo real for o dobro, o preço sobe ~R$ 3.000.')
print('     · LOGO IVECO — FORA DO CUSTO [Jonathan 25/08]. As três linhas')
print('       ficam no levantamento a zero, para que o painel preveja a')
print('       aplicação da marca sem cobrar por ela.')
print(f'     · METALON da bancada da janela — R$ {brl(METALON_M,0)}/m, quadro')
print('       perimetral com três travessas. A prancha não dimensiona.')
print('     · MDF cor 25 mm — a base para em 18 mm (600). Adotei 900. Aqui pesa:')
print('       são vários tampos de 3 cm.')
print('\n⛔ FORA DO ESCOPO: TVs (50" e 85"), forro modular mineral acústico,')
print('   divisórias de vidro existentes e seu reforço, estrutura interna do')
print('   dry wall, pontos elétricos, de rede e de água, alvenaria e pintura.')
print('═'*W)
