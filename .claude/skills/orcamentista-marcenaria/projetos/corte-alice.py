# -*- coding: utf-8 -*-
"""ALICE — marcenaria completa · TRÊS VERSÕES  [08/10/2026]

Projeto: DET_ALICE R00, 06/10/2026, 9 pranchas A3. Arquiteta Alícia
Vasconcelos. ⛔ "CONFERIR MEDIDAS NO LOCAL" em TODAS as pranchas.

⭐ [Jonathan 08/10] "esse preço está muito alto, reveja tudo · faça 3 versões,
   em compensado com e sem verniz e em MDF melamínico · nas versões em
   compensado não precisa considerar a fita de borda, porque aí não é
   aplicado fita"

⛔⛔ O QUE ESTAVA ERRADO NA v1 (R$ 110.950)
   Eu envernizava AS DUAS FACES DE TUDO — inclusive o fundo que encosta na
   parede e o interior das caixas de gaveta. 103,6 m² de superfície.
   A base de materiais da casa já dá a convenção certa: "Laca / Pintura —
   m² EM PEÇA LISA". Acabamento se mede na peça que aparece, não em toda
   superfície que existe. Peça que não aparece leva selo, não acabamento.
   ⭐ Agora cada peça declara quantas faces recebem acabamento (`fc`).

CUSTOS [Jonathan 08/10]
  · compensado naval: 400 / 500 / 600 — e o projeto usa exatamente três
    espessuras, 1,5 / 1,8 / 3,0 cm, então entram em ordem
  · verniz fosco: R$ 350,00 o m²
  · ⛔ compensado NÃO LEVA FITA DE BORDA — confirmado pelo Jonathan
MDF melamínico e fita: base de materiais da casa (`dados/materiais.json`).
"""
import importlib.util, pathlib, sys
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('motor_mc', P/'motor_mc.py')
M = importlib.util.module_from_spec(spec); sys.modules['motor_mc'] = M
spec.loader.exec_module(M)

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
br1 = lambda v: f'{v:,.1f}'.replace(',','X').replace('.',',').replace('X','.')
br2 = lambda v: f'{v:,.2f}'.replace(',','X').replace('.',',').replace('X','.')

# ── materiais ─────────────────────────────────────────────────────────────
CH_NAVAL = 2.20*1.60          # 3,52 m²  ★ conferir o formato da chapa naval
CH_MDF   = 2.75*1.85          # 5,0875 m² — padrão da casa
APROV    = 0.80

PRECO_CN  = {15: 400.0, 18: 500.0, 30: 600.0}   # [Jonathan 08/10]
PRECO_MDF = {15: 500.0, 18: 600.0}              # melamínico COR, base da casa
# ⭐ [Jonathan 08/10] "pode cortar o custo do verniz em 50%". O corte vale
#   sobre o CUSTO — some no preço, não na área: continuamos envernizando as
#   mesmas faces. É negociação com o verniciador, não redução de escopo.
VERNIZ_TAB   = 350.0                            # [Jonathan 08/10]
VERNIZ_CORTE = 0.50                             # [Jonathan 08/10]
VERNIZ_M2    = VERNIZ_TAB*(1 - VERNIZ_CORTE)    # R$ 175,00 o m²
FITA_M    = 3.0 + 2.5          # fita cor + filetagem na coladeira (base)

# ── ferragem ★ estimada — o Jonathan só passou chapa e verniz ─────────────
FER_UN = {'dobr': 35.0, 'dobr180': 55.0, 'corr': 85.0, 'puxador': 25.0,
          'supinv': 60.0, 'calcas': 220.0, 'sapat': 180.0, 'cabide': 60.0,
          'basc': 120.0}
ESPELHO = 450.0

# ══════════════════════════════════════════════════════════════════════════
# PEÇAS  ·  a(ambiente, esp, descrição, c, l, q, fc)
#   fc = faces que RECEBEM ACABAMENTO (verniz, ou fita no caso do melamínico)
#   fc=1 → a peça só aparece de um lado: fundo contra a parede, caixa de
#          gaveta por dentro, rodapé, rodateto, travessa.
#   ⛔ Nenhuma peça leva fc=0: compensado sem selo nenhum incha.
# ══════════════════════════════════════════════════════════════════════════
PCS, FER, TER = {}, {}, {}
def amb(k):
    PCS.setdefault(k, []); TER.setdefault(k, 0.0)
    FER.setdefault(k, dict.fromkeys(FER_UN, 0))
def a(k, esp, desc, c, l, q=1, fc=2):
    amb(k); PCS[k].append((esp, desc, c, l, q, fc))
def f(k, **kw):
    amb(k)
    for key, v in kw.items(): FER[k][key] += v
def ter(k, v):
    amb(k); TER[k] += v

# ── COZINHA · armário inferior 01 ── 2,60 de desenvolvimento, sem fundo ───
K = 'Cozinha · armário inferior'
a(K,15,'Lateral e divisória',        75,  56, 6)
a(K,15,'Base',                      260,  56, 1)
a(K,15,'Travessa superior',         260,  10, 2, 1)
a(K,15,'Frente de porta',            75,  45, 3)
a(K,15,'Frente de gaveta',           19,  45, 4)
a(K,15,'Frente de gaveta alta',      33,  45, 3)
a(K,15,'Gaveta · lateral',           50,  15, 14, 1)
a(K,15,'Gaveta · frente e fundo',    42,  15, 14, 1)
a(K,15,'Gaveta · fundo horizontal',  50,  42, 7, 1)
a(K,15,'Gaveta de temperos · corpo', 75,  25, 2)
a(K,15,'Prateleira',                 50,  50, 2)
a(K,15,'Rodapé',                    260,  10, 1, 1)
f(K, dobr180=6, corr=7, puxador=10)

# ── COZINHA · armário superior 02 ── 1,25 + retorno de 0,35 ──────────────
K = 'Cozinha · armário superior'
a(K,15,'Lateral e divisória',        90,  31, 5)
a(K,15,'Base e tampo',              160,  31, 2)
a(K,15,'Fundo',                     160,  90, 1, 1)
a(K,15,'Frente de porta',            90,  41, 4)
a(K,15,'Prateleira',                 41,  30, 6)
a(K,15,'Rodateto recuado',          160,   2, 1, 1)
f(K, dobr=8, puxador=4)

# ── ÁREA DE SERVIÇO 01 ── 175,3, quatro portas, sem fundo ────────────────
K = 'Área de serviço · armário sob bancada'
a(K,15,'Lateral e divisória',        75,  58, 4)
a(K,15,'Base',                      175,  58, 1)
a(K,15,'Travessa superior',         175,  10, 2, 1)
a(K,15,'Frente de porta',            75,  46, 2)
a(K,15,'Frente de porta',            75,  41, 2)
a(K,15,'Prateleira',                 86,  55, 2)
a(K,15,'Rodapé',                    175,  10, 1, 1)
f(K, dobr=8, puxador=4)

# ── BANHEIRO 01 ── 58 × 63 × 40, basculante + gaveta, sem fundo ──────────
K = 'Banheiro · armário sob bancada'
a(K,15,'Lateral',                    63,  40, 2)
a(K,15,'Base e travessa',            55,  40, 2)
a(K,15,'Frente basculante',          30,  58, 1)
a(K,15,'Frente de gaveta',           25,  58, 1)
a(K,15,'Gaveta · lateral',           38,  20, 2, 1)
a(K,15,'Gaveta · frente e fundo',    52,  20, 2, 1)
a(K,15,'Gaveta · fundo horizontal',  52,  38, 1, 1)
f(K, basc=1, corr=1, puxador=2)

# ── BANHEIRO 02 · armário-espelho ── porta com espelho colado ────────────
K = 'Banheiro · armário-espelho'
a(K,15,'Lateral',                    79,  15, 2)
a(K,15,'Base e tampo',               55,  15, 2)
a(K,15,'Fundo',                      55,  79, 1, 1)
a(K,15,'Frente de porta',            79,  58, 1, 1)   # a outra face é espelho
a(K,15,'Prateleira',                 55,  14, 2)
f(K, dobr=2)
ter(K, ESPELHO)

# ── SALA · prateleiras de 3 cm, suporte invisível chumbado ───────────────
K = 'Sala de estar · prateleiras'
a(K,30,'Prateleira maior',          293,  30, 1)
a(K,30,'Prateleira menor',          120,  12, 1)
f(K, supinv=7)

# ── QUARTO · roupeiro 144 × 277 × 60, portas de 1,8 ──────────────────────
K = 'Quarto · roupeiro'
a(K,15,'Lateral e divisória',       277,  60, 3)
a(K,15,'Base, tampo e travessa',    141,  60, 3)
a(K,15,'Fundo',                     144, 277, 1, 1)
a(K,18,'Porta do corpo',            216,  48, 3)
a(K,18,'Porta do maleiro',           55,  48, 3)
a(K,15,'Prateleira',                 52,  58, 4)
a(K,15,'Prateleira do maleiro',      88,  58, 1)
a(K,15,'Frente de gaveta',           17,  88, 3)
a(K,15,'Frente de gaveta fina',      14,  88, 1)
a(K,15,'Gaveta · lateral',           55,  15, 8, 1)
a(K,15,'Gaveta · frente e fundo',    85,  15, 8, 1)
a(K,15,'Gaveta · fundo horizontal',  85,  55, 4, 1)
a(K,15,'Rodapé',                    144,   4, 1, 1)
a(K,15,'Rodateto recuado',          144,   2, 1, 1)
f(K, dobr=12, corr=4, puxador=6, calcas=1, sapat=1, cabide=1)

AMBS = list(PCS)

# ══════════════════════════════════════════════════════════════════════════
# AS TRÊS VERSÕES
# ══════════════════════════════════════════════════════════════════════════
def versao(nome, material, acabamento):
    """material: 'naval' ou 'mdf' · acabamento: 'verniz', 'natural' ou 'fita'"""
    ch_amb, acab_amb, area_mat = {}, {}, {}
    for k in AMBS:
        ch_amb[k] = acab_amb[k] = 0.0
    for k in AMBS:
        for esp, _, c, l, q, fc in PCS[k]:
            m2 = c*l*q/1e4
            e  = esp
            if material == 'mdf' and esp == 30:
                # ⛔ melamínico não existe em 30 mm: a prateleira é encorpada,
                #   duas chapas de 15 coladas. Dobra a área, não a espessura.
                e, m2 = 15, m2*2
            area_mat[e] = area_mat.get(e, 0.0) + m2
            if acabamento == 'verniz-peca':
                # ⭐ convenção da base da casa: "Laca/Pintura — m² EM PEÇA
                #   LISA". Cobra-se a peça, com o verso junto no serviço.
                acab_amb[k] += m2*VERNIZ_M2
            elif acabamento == 'verniz':
                # ⭐ só as faces que recebem acabamento, mais os cantos delas
                acab_amb[k] += (m2*fc + 2*(c+l)*esp/10*q/1e4*(fc/2))*VERNIZ_M2
            elif acabamento == 'fita':
                # fita nas bordas aparentes; peça de face única leva metade
                acab_amb[k] += 2*(c+l)*q/100*(0.75 if fc == 2 else 0.4)*FITA_M
    preco = PRECO_CN if material == 'naval' else PRECO_MDF
    chm2  = CH_NAVAL if material == 'naval' else CH_MDF
    chapas = {e: -(-v/(chm2*APROV)//1) for e, v in area_mat.items()}
    custo_ch = {e: chapas[e]*preco[e] for e in chapas}
    for e in area_mat:
        for k in AMBS:
            ak = sum(c*l*q/1e4*(2 if (material=='mdf' and esp==30 and e==15) else 1)
                     for esp, _, c, l, q, _ in PCS[k]
                     if (15 if (material=='mdf' and esp==30) else esp) == e)
            if ak: ch_amb[k] += custo_ch[e]*ak/area_mat[e]
    fer_custo = {k: sum(FER[k][x]*FER_UN[x] for x in FER_UN) for k in AMBS}
    CDI = {}
    for k in AMBS:
        proprio = ch_amb[k] + acab_amb[k]
        CDI[k] = (proprio*1.06 + fer_custo[k] + TER[k])*(1 + M.EMBALAGEM)
    BASE = M.base(parcelas=0, rt=False, vendedor=False)
    MC = {k: (0.40 if 'prateleira' in k.lower() else 0.38) for k in AMBS}
    PV = {k: round(CDI[k]/(BASE - MC[k])/10)*10 for k in AMBS}
    return dict(nome=nome, chapas=chapas, custo_ch=custo_ch, area_mat=area_mat,
                ch_amb=ch_amb, acab=acab_amb, fer=fer_custo, CDI=CDI, PV=PV,
                CD=sum(CDI.values()), TOT=sum(PV.values()), BASE=BASE)

VP_ = versao('Compensado · verniz medido EM PEÇA', 'naval', 'verniz-peca')
V = [versao('Compensado naval com verniz',  'naval', 'verniz'),
     versao('Compensado naval natural',     'naval', 'natural'),
     versao('MDF melamínico',               'mdf',   'fita')]

if __name__ == '__main__':
    W = 92
    area_pc = sum(c*l*q/1e4 for k in AMBS for _, _, c, l, q, _ in PCS[k])
    acab_m2 = sum(c*l*q/1e4*fc for k in AMBS for _, _, c, l, q, fc in PCS[k])
    print('═'*W); print('ALICE — DET_ALICE R00  ·  três versões'); print('═'*W)

    print(f'\n⛔ A CORREÇÃO: ÁREA DE ACABAMENTO')
    print(f'  área de peça ............................ {br1(area_pc):>7} m²')
    print(f'  v1 — as duas faces de TUDO, a R$ {br(VERNIZ_TAB)}/m² .. '
          f'{br1(103.6):>7} m²   R$ {br(103.6*VERNIZ_TAB)}')
    print(f'  só as faces que aparecem, a R$ {br(VERNIZ_TAB)}/m² ... '
          f'{br1(acab_m2):>7} m²   R$ {br(acab_m2*VERNIZ_TAB)}')
    print(f'  ⭐ e com o corte de {VERNIZ_CORTE*100:.0f}%, a R$ {br(VERNIZ_M2)}/m² ...... '
          f'{br1(acab_m2):>7} m²   R$ {br(sum(V[0]["acab"].values()))}')
    print('  Saíram do acabamento: o verso do fundo (encosta na parede), o')
    print('  interior das caixas de gaveta, o rodapé, o rodateto e as')
    print('  travessas. ⭐ A base da casa já dizia: "Laca/Pintura, m² EM PEÇA".')

    print(f'\n{"═"*W}')
    print(f'{"":<38}{"compensado":>14}{"compensado":>14}{"MDF":>14}')
    print(f'{"AMBIENTE":<38}{"com verniz":>14}{"natural":>14}{"melamínico":>14}')
    print('─'*W)
    for k in AMBS:
        print(f'{k:<38}' + ''.join(f'{br(v["PV"][k]):>14}' for v in V))
    print('─'*W)
    print(f'{"INVESTIMENTO":<38}' + ''.join(f'{br(v["TOT"]):>14}' for v in V))
    print(f'{"  custo direto":<38}' + ''.join(f'{br(v["CD"]):>14}' for v in V))
    print(f'{"  MC":<38}' + ''.join(
        f'{(v["BASE"]-v["CD"]/v["TOT"])*100:>13.1f}%' for v in V))
    print(f'{"  vs a versão com verniz":<38}' + ''.join(
        f'{(v["TOT"]/V[0]["TOT"]-1)*100:>13.0f}%' for v in V))

    print(f'\n{"═"*W}')
    print('⛔⛔ E A SEGUNDA LEITURA DO VERNIZ, QUE VALE R$ '
          + br(V[0]['TOT'] - VP_['TOT']))
    print(f'{"═"*W}')
    print('  A base de materiais da casa cobra acabamento assim:')
    print('      "Laca / Pintura — m² EM PEÇA LISA — R$ 650"')
    print('  Não por superfície: POR PEÇA, com o verso junto no serviço. Se')
    print('  os R$ 350 do verniz seguirem a mesma régua — e é a régua da')
    print('  casa — a conta muda:')
    print()
    print(f'  {"":<34}{"área":>10}{"verniz":>11}{"preço":>11}')
    print(f'  {"por face aparente (entregue)":<34}{br1(acab_m2):>8} m²'
          f'{br(sum(V[0]["acab"].values())):>11}{br(V[0]["TOT"]):>11}')
    print(f'  {"por peça (convenção da base)":<34}{br1(area_pc):>8} m²'
          f'{br(sum(VP_["acab"].values())):>11}{br(VP_["TOT"]):>11}')
    print()
    print('  ⭐ Você respondeu "por superfície" antes de ver o total. Como')
    print('     mandou rever tudo, deixo as duas: a diferença é R$ '
          + br(V[0]['TOT'] - VP_['TOT']) + ',')
    print('     e quem decide é o acerto com o verniciador, não eu.')

    print(f'\n{"═"*W}')
    print('ONDE CADA REAL ESTÁ')
    print(f'{"═"*W}')
    print(f'  {"":<22}' + ''.join(f'{v["nome"][:13]:>14}' for v in V))
    for rot, campo in (('chapa', 'ch_amb'), ('acabamento', 'acab'),
                       ('ferragem ★', 'fer')):
        print(f'  {rot:<22}' + ''.join(
            f'{br(sum(v[campo].values())):>14}' for v in V))
    print(f'  {"chapas (un)":<22}' + ''.join(
        f'{sum(v["chapas"].values()):>14.0f}' for v in V))

    print(f'\n{"═"*W}')
    print('O QUE CADA VERSÃO É — e o que ela custa depois')
    print(f'{"═"*W}')
    print('  ⭐ COM VERNIZ · o projeto como desenhado. Compensado naval é')
    print('     madeira exposta: o verniz é o que sela a peça contra umidade.')
    print('     Em cozinha, área de serviço e banheiro isso não é estética.')
    print()
    print('  ⚠ NATURAL · a economia é real, mas o compensado fica CRU. Em')
    print('     ambiente seco envelhece bem; em cozinha, área de serviço e')
    print('     banheiro mancha no primeiro respingo e incha na primeira')
    print('     infiltração. ⛔ A casa não dá 10 anos de garantia em')
    print('     compensado sem selo — e esse é o custo que não aparece aqui.')
    print()
    print('  ⭐ MELAMÍNICO · troca o acabamento por revestimento de fábrica:')
    print('     não mancha, não incha e dispensa manutenção. Perde a madeira')
    print('     aparente que o projeto desenha — é outra conversa com a')
    print('     arquiteta, não só outro preço.')

    print(f'\n{"═"*W}')
    print('★ EM ABERTO')
    print(f'{"═"*W}')
    print('  · RT da arquiteta — ⭐ [Jonathan 08/10] SEM RT. Com RT de 10% a')
    print('    base cai de 85,35% para 76,52% e todo preço sobe 23%.')
    print('  · ferragem e espelho ★ estimados — o Jonathan passou chapa e')
    print('    verniz, não ferragem.')
    print('  · formato da chapa naval: adotei 2,20 × 1,60. Se for 2,44 × 1,22,')
    print('    são mais chapas pelo mesmo preço e a chapa sobe ~18%.')
    print('  · ⛔ compensado naval de 3 cm (prateleiras da sala) existe em')
    print('    chapa? Se não, são duas de 1,5 coladas — e o custo dobra ali.')
