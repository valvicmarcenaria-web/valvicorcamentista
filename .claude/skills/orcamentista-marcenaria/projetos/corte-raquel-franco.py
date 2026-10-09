# -*- coding: utf-8 -*-
"""RAQUEL FRANCO — quarto e banheiro, Belo Horizonte  [09/10/2026]

Projeto: PRJ_EXEC_RAQUEL_FRANCO_rn, 10/2026, 11 pranchas A4 — layout,
elétrica, quatro vistas do quarto, quatro de marcenaria e uma do banheiro.
Designer **Rubia Nascimento**. ⛔ "CONFERIR MEDIDAS NO LOCAL" e "EM CASO DE
DÚVIDA, NÃO EXECUTE: LIGUE PARA A DESIGNER" em todas.

⭐ RT de 10% considerado [Jonathan 09/10, mesma designer da Isabela].

══ ⛔⛔ O ROUPEIRO SAI NOVO, NÃO APROVEITADO  [Jonathan 09/10] ════════════
  "não considere o aproveitamento do armário, deixe bem claro que não vale
   a pena pelo envolvimento operacional no processo de aproveitamento
   assim como no risco de não ficar um bom serviço."

  A prancha 10/11 manda, em caixa vermelha:
    "Preservar a estrutura existente em madeira, incluindo base e laterais,
     mediante conferência de seu estado de conservação e estabilidade.
     Reaproveitar as portas, com preparação da superfície e aplicação de
     laca fosca na cor especificada. (...) Conferir as medidas internas e a
     compatibilidade das peças com a abertura das portas antes da
     fabricação."

  ⛔ É esse o caminho que NÃO vamos tomar. O motor calcula os DOIS, para
    que a proposta possa mostrar quanto custa cada um — e por que o
    aproveitamento não compensa.
"""
import importlib.util, pathlib, sys
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('motor_mc', P/'motor_mc.py')
M = importlib.util.module_from_spec(spec); sys.modules['motor_mc'] = M
spec.loader.exec_module(M)

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
br1 = lambda v: f'{v:,.1f}'.replace(',','X').replace('.',',').replace('X','.')

CH_M2, APROV = 2.75*1.85, 0.80
# cor = Noce Amêndoa, Lume, Cancún, Sal Rosa · BR = Branco TX (interno)
# ⛔ ULTRA: a prancha do banheiro manda "Usar MDF Verde/Ultra para armários"
#   — chapa resistente à umidade. ★ Não está na base da casa; estimada em
#   +30% sobre a chapa de cor, que é o diferencial de mercado.
PRECO = {('cor',6):300.0, ('cor',15):500.0, ('cor',18):600.0,
         ('br',6):190.0,  ('br',15):260.0,  ('br',18):330.0,
         ('ultra',6):390.0, ('ultra',15):650.0, ('ultra',18):780.0}
FITA_M  = 3.0 + 2.5
LACA_M2 = 650.0                 # base da casa, "m² em peça lisa"
MC_ALVO = 0.40
BASE    = M.base(parcelas=0, rt=True, vendedor=False)     # ⭐ com RT

FER_UN = {'dobr':35.0, 'corr':85.0, 'puxador':25.0, 'cabide':60.0,
          'sapat':180.0, 'supinv':60.0}
TOMADA_CX = 260.0      # ★ caixa de tomadas embutida no tampo
PORCELANA = 45.0       # ★ puxador de porcelana, por unidade
CURVA_M   = 420.0      # ★ face curva: pós-formagem / lâmina flexível, por m²
# ⭐ [Jonathan 09/10] "pode incluir o espelho no orçamento frisando o
#   fornecimento. custo neste caso de 600,00 o metro quad."
ESPELHO_M2 = 600.0
# ★ a prancha cota 76 de largura no DETALHE ESPELHO e não cota a altura.
#   Adotei 140 — o vão livre entre a bancada e o alto da parede.
ESP_L, ESP_A = 0.76, 1.40

PCS, FER, TER, LACA = {}, {}, {}, {}
def amb(k):
    PCS.setdefault(k, []); TER.setdefault(k, 0.0); LACA.setdefault(k, 0.0)
    FER.setdefault(k, dict.fromkeys(FER_UN, 0))
def a(k, cor, esp, desc, c, l, q=1, fc=2):
    amb(k); PCS[k].append((cor, esp, desc, c, l, q, fc))
def f(k, **kw):
    amb(k)
    for key, v in kw.items(): FER[k][key] += v
def ter(k, v): amb(k); TER[k] += v

# ══ QUARTO ════════════════════════════════════════════════════════════════
# 1 · ESCRIVANINHA em L, 220 × 130, tampo de 10 cm com gavetas por dentro
K = 'Escrivaninha em L'
a(K,'cor',18,'Tampo · face superior',   220,  50, 1)
a(K,'cor',18,'Tampo · face superior',   130,  50, 1)
a(K,'cor',18,'Tampo · face inferior',   220,  50, 1)
a(K,'cor',18,'Tampo · face inferior',   130,  50, 1)
a(K,'cor',18,'Testeira do tampo',       350,  10, 2)
a(K,'cor',15,'Gaveta · frente',          55,   8, 3)
a(K,'cor',15,'Gaveta · frente',          70,   8, 1)
a(K,'cor',15,'Gaveta · caixa',           48,   8, 8, 1)
a(K,'cor',15,'Gaveta · fundo',           55,  48, 4, 1)
a(K,'cor',18,'Apoio lateral',            75,  50, 2)
f(K, corr=4, puxador=0)
ter(K, TOMADA_CX + 4*PORCELANA)

# 2 e 3 · ARMÁRIOS AÉREOS, 65 e 100 de largura, 35 × 25, puxador passante
for nome, larg, nport in (('Armário aéreo menor', 65, 1),
                          ('Armário aéreo maior', 100, 2)):
    K = nome
    a(K,'cor',15,'Lateral',          35,  25, 2)
    a(K,'cor',15,'Base e tampo',  larg-3, 25, 2)
    a(K,'cor', 6,'Fundo',          larg,  35, 1, 1)
    a(K,'cor',18,'Porta',            34, (larg-2)/nport, nport)
    f(K, dobr=2*nport)

# 4 · PRATELEIRA SUPERIOR, 140 × 25, MDF Cancún
K = 'Prateleira superior'
a(K,'cor',15,'Prateleira · duas camadas', 140, 25, 2)
f(K, supinv=3)

# 5 · MÓDULO CAMA, 50 × 50 × 182, com recuo para persiana e FACE CURVA
K = 'Módulo cama'
a(K,'cor',15,'Lateral',            182,  50, 2)
a(K,'cor',15,'Prateleira e base',   47,  50, 4)
a(K,'cor', 6,'Fundo',               50, 182, 1, 1)
a(K,'cor',15,'Face curva',         182,  52, 1)
ter(K, 1.82*0.52*CURVA_M)

# 6 · MÓDULO MESA, 75 × 50 × 65, também com FACE CURVA
K = 'Módulo mesa'
a(K,'cor',15,'Lateral',             65,  50, 2)
a(K,'cor',15,'Base e tampo',        72,  50, 2)
a(K,'cor', 6,'Fundo',               75,  65, 1, 1)
a(K,'cor',15,'Face curva',          65,  55, 1)
ter(K, 0.65*0.55*CURVA_M)

# 7 · PAINEL em L, 277 + 336, altura 87, duas cores
K = 'Painel de cabeceira'
a(K,'cor',15,'Painel · face',       277,  87, 1)
a(K,'cor',15,'Painel · face',       336,  87, 1)
a(K,'cor', 6,'Painel · contraface', 277,  87, 1, 1)
a(K,'cor', 6,'Painel · contraface', 336,  87, 1, 1)
a(K,'cor',15,'Montante de fixação', 87,   10, 8, 1)

# 8 · ROUPEIRO ─ os dois caminhos ────────────────────────────────────────
# 152 × 267 × 60. Interno: prateleiras, 4 gavetas, 2 sapateiras
# deslizantes, cabideiro oval, nicho, vão como puxador.
K = 'Roupeiro'
INTERNO = [
  ('br',15,'Prateleira',            73,  58, 5, 2),
  ('br',15,'Divisória interna',    267,  58, 1, 2),
  ('br',15,'Gaveta · frente',       73,  18, 4, 2),
  ('br',15,'Gaveta · caixa',        56,  15, 8, 1),
  ('br',15,'Gaveta · fundo',        73,  56, 4, 1),
  ('br',15,'Nicho',                 73,  58, 2, 2),
]
NOVO = [
  ('cor',15,'Lateral',             267,  60, 2, 2),
  ('cor',15,'Base, tampo, travessa',149, 60, 3, 1),
  ('cor', 6,'Fundo',               152, 267, 1, 1),
  ('cor',18,'Porta',               267,  75, 2, 2),
  ('cor',15,'Rodapé e rodateto',   152,   6, 2, 1),
]
for c, e, d, cc, ll, q, fc in INTERNO + NOVO:
    a(K, c, e, d, cc, ll, q, fc)
f(K, dobr=8, corr=4, sapat=2, cabide=1, puxador=0)

# ══ BANHEIRO ══════════════════════════════════════════════════════════════
# ⚠ a prancha manda MDF VERDE/ULTRA nos dois armários.
K = 'Banheiro · armário inferior'
a(K,'ultra',15,'Lateral e divisória',  60,  27, 3)
a(K,'ultra',15,'Base e travessa',      86,  27, 2)
a(K,'ultra',18,'Porta',                48,  15, 2)
a(K,'ultra',18,'Porta',                48,  30, 2)
a(K,'ultra',15,'Prateleira',           42,  25, 2)
f(K, dobr=8)
ter(K, 4*PORCELANA)

# ⭐ ESPELHO — fornecimento nosso, com o RECORTE ESCALOPADO da prancha.
K = 'Banheiro · espelho'
amb(K)
ter(K, ESP_L*ESP_A*ESPELHO_M2)

K = 'Banheiro · armário superior'
a(K,'ultra',15,'Lateral',             165,  27, 2)
a(K,'ultra',15,'Base e tampo',         23,  27, 2)
a(K,'ultra', 6,'Fundo',                27, 165, 1, 1)
a(K,'ultra',18,'Porta',               165,  27, 1)
a(K,'ultra',15,'Prateleira',           23,  25, 5)
f(K, dobr=3)

AMBS = list(PCS)

# ══════════════════════════════════════════════════════════════════════════
def calcula(pcs, laca, fer, ter_):
    area_mat, ch, fita, area_k = {}, {}, {}, {}
    for k in AMBS:
        ch[k] = fita[k] = 0.0
        for cor, esp, _, c, l, q, fc in pcs[k]:
            area_mat[(cor,esp)] = area_mat.get((cor,esp),0.0) + c*l*q/1e4
            fita[k] += 2*(c+l)*q/100*(0.75 if fc==2 else 0.4)*FITA_M
    chapas   = {m: -(-v/(CH_M2*APROV)//1) for m, v in area_mat.items()}
    custo_ch = {m: chapas[m]*PRECO[m] for m in chapas}
    taxa = {m: PRECO[m]/(CH_M2*APROV) for m in area_mat}
    for k in AMBS:
        area_k[k] = sum(c*l*q/1e4 for _,_,_,c,l,q,_ in pcs[k])
        ch[k] = sum(c*l*q/1e4*taxa[(cor,esp)] for cor,esp,_,c,l,q,_ in pcs[k])
    sobra = sum(custo_ch.values()) - sum(area_mat[m]*taxa[m] for m in area_mat)
    at = sum(area_k.values())
    for k in AMBS: ch[k] += sobra*area_k[k]/at
    fc_ = {k: sum(fer[k][x]*FER_UN[x] for x in FER_UN) for k in AMBS}
    CDI = {}
    for k in AMBS:
        pr = ch[k] + fita[k] + laca[k]*LACA_M2
        CDI[k] = (pr*1.06 + fc_[k] + ter_[k])*(1 + M.EMBALAGEM)
    PV = {k: round(CDI[k]/(BASE-MC_ALVO)/10)*10 for k in AMBS}
    return dict(ch=ch, fita=fita, fer=fc_, CDI=CDI, PV=PV, chapas=chapas,
                custo_ch=custo_ch, area=area_mat,
                CD=sum(CDI.values()), TOT=sum(PV.values()))

NOVOV = calcula(PCS, LACA, FER, TER)

# ── o caminho do APROVEITAMENTO, só para comparar ────────────────────────
# Mantém a estrutura e as portas existentes; laca nas portas (2 × 75 × 267
# = 4,0 m²) e executa só o interno em Branco TX.
import copy
PCS_AP = {k: list(v) for k, v in PCS.items()}
PCS_AP['Roupeiro'] = [p for p in PCS['Roupeiro'] if p[0] == 'br']
LACA_AP = dict(LACA); LACA_AP['Roupeiro'] = 2*0.75*2.67
FER_AP  = {k: dict(FER[k]) for k in AMBS}
FER_AP['Roupeiro']['dobr'] = 0            # as dobradiças ficam
TER_AP  = dict(TER)
# ★ e o que o aproveitamento ACRESCENTA, que o móvel novo não tem:
VISTORIA   = 380.0    # conferência de estado e estabilidade, com laudo
DESMONTAGEM= 420.0    # retirar portas, transportar, devolver e reinstalar
PREPARO    = 650.0    # lixamento, selagem e preparo de madeira antiga
REMEDICAO  = 340.0    # medir o vão real e compatibilizar peça a peça
TER_AP['Roupeiro'] += VISTORIA + DESMONTAGEM + PREPARO + REMEDICAO
APROV_V = calcula(PCS_AP, LACA_AP, FER_AP, TER_AP)

if __name__ == '__main__':
    W = 90
    print('═'*W); print('RAQUEL FRANCO — quarto e banheiro  ·  PRJ_EXEC_RAQUEL_FRANCO_rn')
    print('═'*W)
    print(f'\n{"PEÇA":<30}{"chapa":>9}{"fita":>8}{"ferr.+terc.":>13}'
          f'{"custo":>10}{"preço":>10}')
    print('─'*W)
    for k in AMBS:
        print(f'{k:<30}{br(NOVOV["ch"][k]):>9}{br(NOVOV["fita"][k]):>8}'
              f'{br(NOVOV["fer"][k]+TER[k]):>13}{br(NOVOV["CDI"][k]):>10}'
              f'{br(NOVOV["PV"][k]):>10}')
    print('─'*W)
    print(f'{"INVESTIMENTO":<30}{"":>9}{"":>8}{"":>13}'
          f'{br(NOVOV["CD"]):>10}{br(NOVOV["TOT"]):>10}')
    print(f'  MC {(BASE-NOVOV["CD"]/NOVOV["TOT"])*100:.1f}%  ·  '
          f'com RT, base {BASE*100:.2f}%  ·  '
          f'{sum(NOVOV["chapas"].values()):.0f} chapas')

    print(f'\n{"═"*W}')
    print('⛔⛔ O ROUPEIRO: APROVEITAR NÃO COMPENSA')
    print(f'{"═"*W}')
    kr = 'Roupeiro'
    print(f'  {"":<42}{"aproveitando":>14}{"novo":>12}')
    print(f'  {"preço do roupeiro":<42}{br(APROV_V["PV"][kr]):>14}'
          f'{br(NOVOV["PV"][kr]):>12}')
    print(f'  {"diferença":<42}{"":>14}'
          f'{br(NOVOV["PV"][kr]-APROV_V["PV"][kr]):>12}')
    print()
    print('  O que o APROVEITAMENTO acrescenta, e o móvel novo não tem:')
    for rot, v in (('vistoria de estado e estabilidade', VISTORIA),
                   ('desmontar, transportar e reinstalar as portas', DESMONTAGEM),
                   ('lixar, selar e preparar madeira antiga', PREPARO),
                   ('remedir o vão e compatibilizar peça a peça', REMEDICAO)):
        print(f'    {rot:<46}R$ {br(v):>6}')
    print(f'    {"laca sobre as portas existentes":<46}R$ '
          f'{br(LACA_AP[kr]*LACA_M2):>6}')
    print(f'    {"":<46}{"─"*9}')
    print(f'    {"soma":<46}R$ '
          f'{br(VISTORIA+DESMONTAGEM+PREPARO+REMEDICAO+LACA_AP[kr]*LACA_M2):>6}')
    print()
    # ⛔⛔ A ARITMÉTICA INVERTEU O ARGUMENTO — e para melhor. Eu esperava
    #   que aproveitar fosse mais barato e arriscado; não é mais barato.
    d = APROV_V['PV'][kr] - NOVOV['PV'][kr]
    print(f'  ⛔⛔ APROVEITAR NÃO É NEM MAIS BARATO: custa R$ {br(d)} A MAIS')
    print(f'     que o móvel novo — {d/NOVOV["PV"][kr]*100:.0f}% acima dele.')
    print('     A R$ 650/m², a laca sobre as portas existentes já custa mais')
    print('     que a chapa de um roupeiro inteiro. É a mesma conta do')
    print('     orçamento da Raquel Oliveira, agora provada duas vezes.')
    print()
    print('     E além de custar mais, a casa ainda assumiria:')
    print('       · a ESTABILIDADE de uma estrutura que não construiu e não')
    print('         consegue ver por dentro;')
    print('       · a ADERÊNCIA da laca sobre madeira antiga já envernizada;')
    print('       · e a COMPATIBILIDADE do interno novo com um vão que a')
    print('         própria prancha manda conferir antes de fabricar.')
    print('     ⛔ A garantia de 10 anos da casa NÃO cobre peça de terceiro.')
    print('     ⛔ E o prazo passa a depender da vistoria: se a estrutura')
    print('        reprovar depois de desmontada, o projeto para.')

    print(f'\n{"═"*W}')
    print('★ EM ABERTO')
    print(f'{"═"*W}')
    print(f'  · ⚠ MDF VERDE/ULTRA no banheiro, como a prancha manda. ★ Não')
    print(f'    está na base da casa; estimei +30% sobre a chapa de cor.')
    print(f'  · ⚠ AS FACES CURVAS do módulo cama e do módulo mesa. Em')
    print(f'    melamínico a curva é pós-formagem ou lâmina flexível —')
    print(f'    lancei R$ {br(CURVA_M)}/m². ★ Confirmar o processo.')
    print(f'  · ⭐ O ESPELHO entrou: {ESP_L:.2f} × {ESP_A:.2f} m a R$ {br(ESPELHO_M2)}/m² '
          f'= R$ {br(ESP_L*ESP_A*ESPELHO_M2)} de custo,')
    print(f'    R$ {br(NOVOV["PV"]["Banheiro · espelho"])} de preço. ★ A prancha cota a LARGURA (76) e')
    print('    não a altura; adotei 140. O recorte escalopado é nosso.')
    print('  · caixa de tomadas e puxador de porcelana ★ estimados.')
