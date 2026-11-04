# -*- coding: utf-8 -*-
"""ISABELA LEÃO — home office, Belo Horizonte  [09/10/2026]

Projeto: PRJ_EXEC_ISABELA_rn, 09/2026, 6 pranchas A4. Designer **Rubia
Nascimento** — a mesma do projeto da Raquel.
⛔ "CONFERIR MEDIDAS NO LOCAL" e "EM CASO DE DÚVIDA, NÃO EXECUTE: LIGUE
   PARA A DESIGNER" em todas as pranchas. Pé-direito 2,74.

⭐ [Jonathan 09/10] "considere RT na proposta viu" → RT de 10%, base 76,52%.

O ESCOPO — três peças
  1 · ESTANTE ..... 299 × 274 × 30, MDF Azul Vel Berneck, vinte e cinco
      nichos com prateleiras, arcos decorativos e portas na base
  2 · MESA EM L ... 249,5 × 200, tampo em MDF Peroba Guararapes de 3 cm,
      apoio em MDF Azul Vel Berneck
  3 · GAVETEIRO ... 52 × 50 × 65 sobre rodízio, Azul Vel Berneck, puxador
      Tinyhob, com gaveta-arquivo de pasta suspensa

⛔ FORA: poltrona, cadeira, luminárias, pendentes, quadro, plantas, livros
   e o tapete. ⚠ "Transferir tomadas p/ marcenaria" é ELÉTRICA — nossa é
   só a usinagem da passagem na peça.
"""
import importlib.util, pathlib, sys
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('motor_mc', P/'motor_mc.py')
M = importlib.util.module_from_spec(spec); sys.modules['motor_mc'] = M
spec.loader.exec_module(M)

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
br1 = lambda v: f'{v:,.1f}'.replace(',','X').replace('.',',').replace('X','.')

CH_M2, APROV = 2.75*1.85, 0.80
PRECO  = {6: 300.0, 15: 500.0, 18: 600.0}     # MDF cor — base da casa
FITA_M = 3.0 + 2.5                            # fita cor + filetagem
MC_ALVO = 0.40                                # ⭐ [Jonathan 08/10]
RT_ON   = True                                # ⭐ [Jonathan 09/10]
BASE    = M.base(parcelas=0, rt=RT_ON, vendedor=False)

FER_UN = {'dobr': 35.0, 'corr': 85.0, 'puxador': 25.0, 'rodizio': 25.0}
ARCO_UN   = 120.0     # ★ usinagem CNC do arco decorativo, por nicho
PASTA_SUSP = 180.0    # ★ quadro para pasta suspensa, terceiro

PCS, FER, TER = {}, {}, {}
def amb(k):
    PCS.setdefault(k, []); TER.setdefault(k, 0.0)
    FER.setdefault(k, dict.fromkeys(FER_UN, 0))
def a(k, esp, desc, c, l, q=1, fc=2):
    amb(k); PCS[k].append((esp, desc, c, l, q, fc))
def f(k, **kw):
    amb(k)
    for key, v in kw.items(): FER[k][key] += v
def ter(k, v): amb(k); TER[k] += v

# ── 1 · ESTANTE ───────────────────────────────────────────────────────────
# 299 × 274 × 30. Cinco colunas de 57 entre montantes de 2; cinco fileiras
# (52 × 4 + 54). Vinte e três prateleiras cotadas. Base com duas portas.
K = 'Estante'
a(K,15,'Lateral',                   274,  30, 2)
a(K,15,'Montante interno',          274,  30, 4)
a(K,15,'Base e topo',               293,  30, 2)
a(K,15,'Prateleira',                 57,  30, 23)
a(K, 6,'Fundo',                     299, 274, 1, 1)
a(K,18,'Porta da base',              66,  59, 2)
f(K, dobr=4, puxador=2)
ter(K, 8*ARCO_UN)        # ★ oito arcos decorativos usinados

# ── 2 · MESA EM L ─────────────────────────────────────────────────────────
# Braço de 249,5 × 62 e retorno de 138 × 108, com ponta arredondada.
# ⛔ Tampo de 3 cm: não existe chapa. São duas de 15 coladas.
K = 'Mesa em L'
a(K,15,'Tampo · braço, duas camadas',    250,  62, 2)
a(K,15,'Tampo · retorno, duas camadas',  138, 108, 2)
a(K,18,'Apoio em Azul Vel Berneck',       90,  62, 1)
a(K,18,'Apoio · travessa',               138,  12, 1, 1)

# ── 3 · GAVETEIRO ─────────────────────────────────────────────────────────
# 52 × 50 × 65 sobre rodízio. Gaveta de 15 e gaveta-arquivo de 45.
K = 'Gaveteiro com arquivo'
a(K,15,'Lateral',                    65,  50, 2)
a(K,15,'Base e tampo',               49,  50, 2)
a(K, 6,'Fundo',                      49,  65, 1, 1)
a(K,18,'Frente de gaveta',           15,  52, 1)
a(K,18,'Frente da gaveta-arquivo',   45,  52, 1)
a(K,15,'Gaveta · lateral',           45,  12, 4, 1)
a(K,15,'Gaveta · frente e fundo',    45,  12, 4, 1)
a(K,15,'Gaveta · fundo horizontal',  45,  45, 2, 1)
f(K, corr=2, puxador=2, rodizio=4)
ter(K, PASTA_SUSP)

AMBS = list(PCS)

# ══════════════════════════════════════════════════════════════════════════
area_mat, ch_amb, fita_amb, area_k = {}, {}, {}, {}
for k in AMBS:
    ch_amb[k] = fita_amb[k] = 0.0
    for esp, _, c, l, q, fc in PCS[k]:
        area_mat[esp] = area_mat.get(esp, 0.0) + c*l*q/1e4
        fita_amb[k]  += 2*(c+l)*q/100*(0.75 if fc == 2 else 0.4)*FITA_M
chapas   = {e: -(-v/(CH_M2*APROV)//1) for e, v in area_mat.items()}
custo_ch = {e: chapas[e]*PRECO[e] for e in chapas}
# ⛔ cada peça paga a própria taxa; a sobra de corte rateia pela área total,
#   porque a sobra é do corte e não do ambiente (lição do orçamento da Alice).
taxa = {e: PRECO[e]/(CH_M2*APROV) for e in area_mat}
for k in AMBS:
    area_k[k] = sum(c*l*q/1e4 for _, _, c, l, q, _ in PCS[k])
    ch_amb[k] = sum(c*l*q/1e4*taxa[esp] for esp, _, c, l, q, _ in PCS[k])
sobra = sum(custo_ch.values()) - sum(area_mat[e]*taxa[e] for e in area_mat)
at = sum(area_k.values())
for k in AMBS: ch_amb[k] += sobra*area_k[k]/at

fer_custo = {k: sum(FER[k][x]*FER_UN[x] for x in FER_UN) for k in AMBS}
CDI = {}
for k in AMBS:
    proprio = ch_amb[k] + fita_amb[k]
    CDI[k] = (proprio*1.06 + fer_custo[k] + TER[k])*(1 + M.EMBALAGEM)
CD  = sum(CDI.values())
PV  = {k: round(CDI[k]/(BASE - MC_ALVO)/10)*10 for k in AMBS}
TOT = sum(PV.values())

if __name__ == '__main__':
    W = 86
    print('═'*W); print('ISABELA LEÃO — home office  ·  PRJ_EXEC_ISABELA_rn')
    print('═'*W)
    print(f'\n{"CHAPA":<10}{"área líq.":>12}{"chapas":>9}{"R$/chapa":>11}{"custo":>11}')
    print('─'*W)
    for e in sorted(area_mat):
        print(f'{e:>3} mm{"":<4}{br1(area_mat[e]):>10} m²{chapas[e]:>9.0f}'
              f'{br(PRECO[e]):>11}{br(custo_ch[e]):>11}')
    print('─'*W)
    print(f'{"TOTAL":<10}{br1(sum(area_mat.values())):>10} m²'
          f'{sum(chapas.values()):>9.0f}{"":>11}{br(sum(custo_ch.values())):>11}')

    print(f'\n{"═"*W}')
    print(f'{"PEÇA":<26}{"chapa":>9}{"fita":>8}{"ferr.+terc.":>13}'
          f'{"custo":>10}{"preço":>10}{"MC":>8}')
    print('─'*W)
    for k in AMBS:
        print(f'{k:<26}{br(ch_amb[k]):>9}{br(fita_amb[k]):>8}'
              f'{br(fer_custo[k]+TER[k]):>13}{br(CDI[k]):>10}{br(PV[k]):>10}'
              f'{(BASE-CDI[k]/PV[k])*100:>7.1f}%')
    print('─'*W)
    print(f'{"INVESTIMENTO":<26}{br(sum(ch_amb.values())):>9}'
          f'{br(sum(fita_amb.values())):>8}'
          f'{br(sum(fer_custo.values())+sum(TER.values())):>13}'
          f'{br(CD):>10}{br(TOT):>10}{(BASE-CD/TOT)*100:>7.1f}%')
    print(f'  ⭐ COM RT de 10% — base {BASE*100:.2f}%  [Jonathan 09/10]')
    b0 = M.base(parcelas=0, rt=False, vendedor=False)
    t0 = sum(round(CDI[k]/(b0 - MC_ALVO)/10)*10 for k in AMBS)
    print(f'     sem RT o mesmo custo daria R$ {br(t0)} — o RT vale '
          f'R$ {br(TOT-t0)} ({(TOT/t0-1)*100:.1f}%)')

    print(f'\n{"═"*W}')
    print('⛔ A ESTANTE É O PROJETO')
    print(f'{"═"*W}')
    print(f'  Ela sozinha é R$ {br(PV["Estante"])} de R$ {br(TOT)} — '
          f'{PV["Estante"]/TOT*100:.0f}% do orçamento.')
    print('  Parede inteira, do piso ao teto, com vinte e cinco nichos e')
    print('  vinte e três prateleiras. É onde está o risco e é onde está')
    print('  a margem.')
    print(f'\n  ⚠ OS ARCOS. O desenho mostra arcos dentro de oito nichos.')
    print(f'    Lancei usinagem CNC a R$ {br(ARCO_UN)} cada = R$ {br(8*ARCO_UN)}.')
    print('    ★ Se forem arcos VAZADOS (recorte passante) é isso; se forem')
    print('      só desenhados no render, sai do preço; se forem molduras')
    print('      aplicadas, é outro custo. A prancha não diz qual.')
    print(f'\n  ⚠ O FUNDO de 6 mm em cor custa R$ {br(custo_ch.get(6,0))} — '
          f'{chapas.get(6,0):.0f} chapas para')
    print('    8,19 m² de fundo. Em peça azul o fundo tem de ser azul.')

    print(f'\n{"═"*W}')
    print('★ EM ABERTO')
    print(f'{"═"*W}')
    print('  · os arcos: vazados, aplicados ou só do render?')
    print('  · a mesa tem tampo de 3 cm — duas chapas coladas, e a PONTA')
    print('    ARREDONDADA do retorno pede usinagem e fita flexível.')
    print('    ⛔ Em melamínico a QUINA não abaúla: a aresta sai reta.')
    print('  · ferragem: dobradiça, corrediça telescópica, puxador Tinyhob e')
    print('    rodízio estão ★ estimados e INCLUSOS aqui — ao contrário do')
    print('    orçamento da Raquel, onde o Jonathan mandou tirar.')
    print('  · "transferir tomadas p/ marcenaria" é elétrica de terceiro;')
    print('    nossa é só a usinagem da passagem.')
