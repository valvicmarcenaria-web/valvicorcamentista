# -*- coding: utf-8 -*-
"""ALICE — marcenaria completa em COMPENSADO NAVAL  [08/10/2026]

Projeto: DET_ALICE R00, 06/10/2026, 9 pranchas A3.
Arquiteta: Alícia Vasconcelos. ⛔ "CONFERIR MEDIDAS NO LOCAL" em TODAS as
pranchas — este levantamento é estimativa que erra PARA CIMA.

CUSTOS DADOS PELO JONATHAN [08/10]
  · chapa de compensado: 400 / 500 / 600
  · verniz fosco: R$ 350,00 o metro quadrado
⭐ O projeto usa EXATAMENTE três espessuras — 1,5 / 1,8 / 3,0 cm — e os três
  preços entram em ordem. 1,8 cm só nas portas do quarto; 3,0 cm só nas
  prateleiras da sala.

⛔⛔ COMPENSADO NAVAL NÃO TEM FITA DE BORDA. O custo que o melamínico põe na
   fita, aqui está no VERNIZ — e o verniz não pega só a face: pega as DUAS
   faces de cada peça mais os cantos. É o maior item do orçamento.

⛔ O QUE NÃO VEIO e está estimado (marcado ★ no relatório): preço de
   ferragem, do espelho colado do banheiro e dos suportes invisíveis.
"""
import importlib.util, pathlib, sys
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('motor_mc', P/'motor_mc.py')
M = importlib.util.module_from_spec(spec); sys.modules['motor_mc'] = M
spec.loader.exec_module(M)

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
br1 = lambda v: f'{v:,.1f}'.replace(',','X').replace('.',',').replace('X','.')
br2 = lambda v: f'{v:,.2f}'.replace(',','X').replace('.',',').replace('X','.')

# ── material ──────────────────────────────────────────────────────────────
# chapa de compensado naval: 2,20 × 1,60 m = 3,52 m²  ★ conferir o formato
CH_C, CH_L = 220.0, 160.0
CH_M2      = CH_C*CH_L/1e4
APROV      = 0.80                      # aproveitamento de corte
PRECO = {'CN15': 400.0, 'CN18': 500.0, 'CN30': 600.0}   # [Jonathan 08/10]
VERNIZ_M2  = 350.0                                       # [Jonathan 08/10]

# ── ferragem ★ estimada — o Jonathan só passou chapa e verniz ─────────────
FER_UN = {
    'dobr':      35.0,   # dobradiça com amortecedor (OBS 2 do projeto)
    'dobr180':   55.0,   # abertura 180° — a cozinha pede
    'corr':      85.0,   # corrediça telescópica com amortecedor (OBS 3)
    'puxador':   25.0,   # ponto preto
    'supinv':    60.0,   # suporte invisível chumbado (prateleira de 3 cm)
    'calcas':   220.0,   # cabideiro deslizante para calças
    'sapat':    180.0,   # sapateira deslizante
    'cabide':    60.0,   # cabideiro convencional, barra + suportes
    'basc':     120.0,   # pistão da porta basculante do banheiro
}
ESPELHO = 450.0          # ★ espelho colado na porta do armário do banheiro

# ══════════════════════════════════════════════════════════════════════════
# PEÇAS — c × l em cm, por ambiente. Fonte: pranchas 01 a 09.
# ⛔ As larguras da cozinha são DESENVOLVIMENTO FRONTAL estimado: a planta
#   da folha 01 cota os módulos, não o corpo corrido. As demais são cotadas.
# ══════════════════════════════════════════════════════════════════════════
PCS, FER, TER = {}, {}, {}
def amb(k):
    PCS.setdefault(k, []); TER.setdefault(k, 0.0)
    FER.setdefault(k, dict.fromkeys(FER_UN, 0))
def a(k, mat, desc, c, l, q=1):
    amb(k); PCS[k].append((mat, desc, c, l, q))
def f(k, **kw):
    amb(k)
    for key, v in kw.items(): FER[k][key] += v
def ter(k, v):
    amb(k); TER[k] += v

# ── COZINHA · armário inferior 01 ─────────────────────────────────────────
# L de 2,60 m de desenvolvimento (1,13 + 0,25 na elevação A, ~1,20 na B),
# H 75 + rodapé 10, prof 56. Sem fundo (o projeto manda).
K = 'Cozinha · armário inferior'
a(K,'CN15','Lateral e divisória',        75,  56, 6)
a(K,'CN15','Base',                      260,  56, 1)
a(K,'CN15','Travessa superior',         260,  10, 2)
a(K,'CN15','Frente de porta',            75,  45, 3)
a(K,'CN15','Frente de gaveta',           19,  45, 4)
a(K,'CN15','Frente de gaveta alta',      33,  45, 3)
a(K,'CN15','Gaveta · lateral',           50,  15, 14)
a(K,'CN15','Gaveta · frente e fundo',    42,  15, 14)
a(K,'CN15','Gaveta · fundo horizontal',  50,  42, 7)
a(K,'CN15','Gaveta de temperos · corpo', 75,  25, 2)
a(K,'CN15','Prateleira',                 50,  50, 2)
a(K,'CN15','Rodapé',                    260,  10, 1)
f(K, dobr180=6, corr=7, puxador=10)

# ── COZINHA · armário superior 02 ─────────────────────────────────────────
# 1,25 na elevação B (3 portas de 41,7) + retorno de 0,35 na A. H 90, prof 31.
K = 'Cozinha · armário superior'
a(K,'CN15','Lateral e divisória',        90,  31, 5)
a(K,'CN15','Base e tampo',              160,  31, 2)
a(K,'CN15','Fundo',                     160,  90, 1)
a(K,'CN15','Frente de porta',            90,  41, 4)
a(K,'CN15','Prateleira',                 41,  30, 6)
a(K,'CN15','Rodateto recuado',          160,   2, 1)   # OBS 1
f(K, dobr=8, puxador=4)

# ── ÁREA DE SERVIÇO · armário sob bancada 01 ──────────────────────────────
# 175,3 de largura, 4 portas (46,3 + 46,3 + 41,3 + 41,3), H 75 + 10, prof 57,5.
# Sem fundo em compensado (o projeto manda).
K = 'Área de serviço · armário sob bancada'
a(K,'CN15','Lateral e divisória',        75,  58, 4)
a(K,'CN15','Base',                      175,  58, 1)
a(K,'CN15','Travessa superior',         175,  10, 2)
a(K,'CN15','Frente de porta',            75,  46, 2)
a(K,'CN15','Frente de porta',            75,  41, 2)
a(K,'CN15','Prateleira',                 86,  55, 2)
a(K,'CN15','Rodapé',                    175,  10, 1)
f(K, dobr=8, puxador=4)

# ── BANHEIRO · armário sob bancada 01 ─────────────────────────────────────
# 58 × 63, prof 40. Porta basculante + gaveta. Sem fundo.
K = 'Banheiro · armário sob bancada'
a(K,'CN15','Lateral',                    63,  40, 2)
a(K,'CN15','Base e travessa',            55,  40, 2)
a(K,'CN15','Frente basculante',          30,  58, 1)
a(K,'CN15','Frente de gaveta',           25,  58, 1)
a(K,'CN15','Gaveta · lateral',           38,  20, 2)
a(K,'CN15','Gaveta · frente e fundo',    52,  20, 2)
a(K,'CN15','Gaveta · fundo horizontal',  52,  38, 1)
f(K, basc=1, corr=1, puxador=2)

# ── BANHEIRO · armário-espelho 02 ─────────────────────────────────────────
# 58 × 79, prof 15. Porta de giro com espelho colado, puxador passante.
K = 'Banheiro · armário-espelho'
a(K,'CN15','Lateral',                    79,  15, 2)
a(K,'CN15','Base e tampo',               55,  15, 2)
a(K,'CN15','Fundo',                      55,  79, 1)
a(K,'CN15','Frente de porta',            79,  58, 1)
a(K,'CN15','Prateleira',                 55,  14, 2)
f(K, dobr=2)
ter(K, ESPELHO)

# ── SALA DE ESTAR · prateleiras 01 ────────────────────────────────────────
# ⛔ 3 cm de compensado, com ponta arredondada (R20 e R12) e suporte
#   invisível CHUMBADO NA PAREDE — não é prateleira de apoio, é balanço.
K = 'Sala de estar · prateleiras'
a(K,'CN30','Prateleira maior',          293,  30, 1)
a(K,'CN30','Prateleira menor',          120,  12, 1)
f(K, supinv=7)          # ~1 a cada 50 cm nos 4,13 m somados

# ── QUARTO · roupeiro 01 ──────────────────────────────────────────────────
# 144 × 277 × 60. Corpo 1,5 cm, PORTAS 1,8 cm. Maleiro de 55, corpo de 216,
# rodapé 4, rodateto recuado 2. Colunas internas de 52 e 88,8.
K = 'Quarto · roupeiro'
a(K,'CN15','Lateral e divisória',       277,  60, 3)
a(K,'CN15','Base, tampo e travessa',    141,  60, 4)
a(K,'CN15','Fundo',                     144, 277, 1)
a(K,'CN18','Porta do corpo',            216,  48, 3)   # ⭐ 1,8 cm
a(K,'CN18','Porta do maleiro',           55,  48, 3)   # ⭐ 1,8 cm
a(K,'CN15','Prateleira',                 52,  58, 4)
a(K,'CN15','Prateleira do maleiro',      88,  58, 1)
a(K,'CN15','Frente de gaveta',           17,  88, 3)
a(K,'CN15','Frente de gaveta fina',      14,  88, 1)
a(K,'CN15','Gaveta · lateral',           55,  15, 8)
a(K,'CN15','Gaveta · frente e fundo',    85,  15, 8)
a(K,'CN15','Gaveta · fundo horizontal',  85,  55, 4)
a(K,'CN15','Rodapé',                    144,   4, 1)
a(K,'CN15','Rodateto recuado',          144,   2, 1)
f(K, dobr=12, corr=4, puxador=6, calcas=1, sapat=1, cabide=1)

# ══════════════════════════════════════════════════════════════════════════
# CÁLCULO
# ══════════════════════════════════════════════════════════════════════════
AMBS = list(PCS)
area   = {k: sum(c*l*q/1e4      for _, _, c, l, q in PCS[k]) for k in AMBS}
# ⛔ o verniz pega as DUAS faces e os cantos. O canto entra pelo perímetro
#   × espessura, que em peça de 3 cm não é desprezível.
ESP_CM = {'CN15': 1.5, 'CN18': 1.8, 'CN30': 3.0}
def _canto(mat, c, l, q):
    return 2*(c + l)*ESP_CM[mat]*q/1e4
vern_m2 = {k: sum(c*l*q*2/1e4 + _canto(m, c, l, q)
                  for m, _, c, l, q in PCS[k]) for k in AMBS}

area_mat = {}
for k in AMBS:
    for m, _, c, l, q in PCS[k]:
        area_mat[m] = area_mat.get(m, 0.0) + c*l*q/1e4
CHAPAS  = {m: -(-v/(CH_M2*APROV)//1) for m, v in area_mat.items()}   # teto
CUSTO_CH = {m: CHAPAS[m]*PRECO[m] for m in CHAPAS}

# rateio da chapa por ambiente, proporcional à área de cada material
ch_amb = {k: 0.0 for k in AMBS}
for m in area_mat:
    for k in AMBS:
        ak = sum(c*l*q/1e4 for mm, _, c, l, q in PCS[k] if mm == m)
        if ak: ch_amb[k] += CUSTO_CH[m]*ak/area_mat[m]

vern_custo = {k: vern_m2[k]*VERNIZ_M2 for k in AMBS}
fer_custo  = {k: sum(FER[k][x]*FER_UN[x] for x in FER_UN) for k in AMBS}

CDI = {}
for k in AMBS:
    proprio = ch_amb[k] + vern_custo[k]
    cons    = proprio*0.06                      # cola, lixa, parafuso, fixação
    CDI[k]  = (proprio + cons + fer_custo[k] + TER[k])*(1 + M.EMBALAGEM)
CD = sum(CDI.values())

# ── margem ────────────────────────────────────────────────────────────────
# ★ RT não informado. Sem RT e sem comissão — o cenário que mais aperta o
#   preço é COM RT, e ele está no quadro do fim.
RT_ON, COMISSAO = False, False
BASE = M.base(parcelas=0, rt=RT_ON, vendedor=COMISSAO)

MC_ITEM = {}
for k in AMBS:
    b = 0.38
    if 'prateleira' in k.lower(): b = 0.40      # item especial, balanço
    if 'roupeiro'   in k.lower(): b = 0.38
    MC_ITEM[k] = b
PV = {k: round(CDI[k]/(BASE - MC_ITEM[k])/10)*10 for k in AMBS}
TOT = sum(PV.values())
MC_REAL = {k: BASE - CDI[k]/PV[k] for k in AMBS}

if __name__ == '__main__':
    W = 92
    print('═'*W); print('ALICE — marcenaria em compensado naval  ·  DET_ALICE R00')
    print('═'*W)
    print(f'\n{"CHAPA":<8}{"espessura":>11}{"área líq.":>12}{"chapas":>9}'
          f'{"R$/chapa":>11}{"custo":>11}')
    print('─'*W)
    for m in sorted(area_mat):
        print(f'{m:<8}{ESP_CM[m]:>9.1f} cm{br1(area_mat[m]):>10} m²'
              f'{CHAPAS[m]:>9.0f}{br(PRECO[m]):>11}{br(CUSTO_CH[m]):>11}')
    print('─'*W)
    print(f'{"TOTAL":<8}{"":>11}{br1(sum(area_mat.values())):>10} m²'
          f'{sum(CHAPAS.values()):>9.0f}{"":>11}{br(sum(CUSTO_CH.values())):>11}')
    print(f'  chapa de {CH_C:.0f} × {CH_L:.0f} = {br2(CH_M2)} m², aproveitamento '
          f'{APROV*100:.0f}%   ★ conferir o formato da chapa')

    tv = sum(vern_m2.values())
    print(f'\n{"═"*W}')
    print('⛔ O VERNIZ É O MAIOR ITEM DO ORÇAMENTO')
    print(f'{"═"*W}')
    print(f'  área de peça .......................... {br1(sum(area.values())):>8} m²')
    print(f'  área a envernizar (2 faces + cantos) .. {br1(tv):>8} m²'
          f'   = {tv/sum(area.values()):.2f}×')
    print(f'  a R$ {br(VERNIZ_M2)}/m² .............................. '
          f'R$ {br(tv*VERNIZ_M2)}')
    print(f'  contra R$ {br(sum(CUSTO_CH.values()))} de chapa — o verniz é '
          f'{tv*VERNIZ_M2/sum(CUSTO_CH.values()):.1f}× a chapa.')
    print('  ⚠ Compensado naval não leva fita de borda: o acabamento TODO')
    print('    está no verniz, nas duas faces e nos cantos. Se o combinado')
    print('    for envernizar só a face aparente, o custo cai pela metade —')
    print('    mas o interior fica sem selo, e compensado sem selo incha.')

    print(f'\n{"═"*W}')
    print(f'{"AMBIENTE":<38}{"chapa":>9}{"verniz":>10}{"ferr.":>8}'
          f'{"custo":>10}{"preço":>10}{"MC":>7}')
    print('─'*W)
    for k in AMBS:
        print(f'{k:<38}{br(ch_amb[k]):>9}{br(vern_custo[k]):>10}'
              f'{br(fer_custo[k]+TER[k]):>8}{br(CDI[k]):>10}{br(PV[k]):>10}'
              f'{MC_REAL[k]*100:>6.1f}%')
    print('─'*W)
    print(f'{"TOTAL":<38}{br(sum(ch_amb.values())):>9}'
          f'{br(sum(vern_custo.values())):>10}'
          f'{br(sum(fer_custo.values())+sum(TER.values())):>8}'
          f'{br(CD):>10}{br(TOT):>10}{(BASE-CD/TOT)*100:>6.1f}%')
    print(f'  base {BASE*100:.2f}% — sem RT e sem comissão')

    print(f'\n{"═"*W}')
    print('E SE HOUVER RT DE 10%')
    print(f'{"═"*W}')
    b2 = M.base(parcelas=0, rt=True, vendedor=False)
    t2 = sum(round(CDI[k]/(b2 - MC_ITEM[k])/10)*10 for k in AMBS)
    print(f'  mesmo custo, mesma MC, base cai de {BASE*100:.2f}% para {b2*100:.2f}%')
    print(f'  preço sobe de R$ {br(TOT)} para R$ {br(t2)}'
          f'   (+{(t2/TOT-1)*100:.1f}%, R$ {br(t2-TOT)})')
    print('  ★ O projeto é da Alícia Vasconcelos. Se houver RT, é este o preço.')

    print(f'\n{"═"*W}')
    print('⛔⛔ AS DUAS PERGUNTAS QUE VALEM R$ 38 MIL')
    print(f'{"═"*W}')
    print('  1 · Os R$ 350/m² são por m² de SUPERFÍCIE envernizada (as duas')
    print('      faces) ou por m² de PEÇA (a face, com o verso junto)?')
    print('  2 · Há RT da arquiteta? O projeto é da Alícia Vasconcelos.')
    print()
    print(f'  {"":<26}{"sem RT":>13}{"com RT 10%":>14}')
    for rot, f2 in (('verniz nas 2 faces', 1.0), ('verniz só na face', 0.5)):
        linha = f'  {rot:<26}'
        for rt in (False, True):
            b  = M.base(parcelas=0, rt=rt, vendedor=False)
            t  = 0
            for k in AMBS:
                pr = ch_amb[k] + vern_custo[k]*f2
                cd = (pr + pr*0.06 + fer_custo[k] + TER[k])*(1 + M.EMBALAGEM)
                t += round(cd/(b - MC_ITEM[k])/10)*10
            linha += f'{br(t):>13}' if not rt else f'{br(t):>14}'
        print(linha)
    print()
    print('  ⭐ ENTREGUE: verniz nas 2 faces, sem RT — o canto conservador de')
    print('     cada eixo. Compensado naval SEM SELO NO INTERIOR incha, então')
    print('     as duas faces é o que a peça pede, não o que encarece à toa.')
    print('     Se o acerto com o verniciador for por m² de peça, o preço cai')
    print('     para o segundo valor da coluna — é uma linha no motor.')

    print(f'\n{"═"*W}')
    print('★ O QUE NÃO VEIO — e que o preço está carregando por estimativa')
    print(f'{"═"*W}')
    print(f'  ferragem, toda ......................... R$ {br(sum(fer_custo.values()))}')
    print(f'  espelho colado do banheiro ............. R$ {br(ESPELHO)}')
    print(f'  ────────────────────────────────────────────────')
    print(f'  soma estimada .......................... R$ '
          f'{br(sum(fer_custo.values()) + sum(TER.values()))}'
          f'  = {(sum(fer_custo.values())+sum(TER.values()))/CD*100:.0f}% do custo')
    print('  ⛔ Também não veio o FORMATO DA CHAPA naval. Adotei 2,20 × 1,60.')
    print('     Se a chapa for 2,44 × 1,22 (2,98 m²), são mais chapas pelo')
    print('     mesmo preço unitário — e o custo de chapa sobe ~18%.')
