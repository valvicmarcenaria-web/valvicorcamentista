# -*- coding: utf-8 -*-
"""RAQUEL OLIVEIRA — quarto infantil, Belo Horizonte  [09/10/2026]

Projeto: PRJ_EXEC_RAQUEL_O_rn, 10/2026, 6 pranchas A4 (layout, iluminação e
quatro vistas). Designer: **Rubia Nascimento**.
⛔ "CONFERIR MEDIDAS NO LOCAL" e "EM CASO DE DÚVIDA, NÃO EXECUTE: LIGUE PARA
   A DESIGNER" em todas as pranchas.

⛔⛔ A MAIOR PARTE DO QUE ESTÁ DESENHADO NÃO É MARCENARIA.
   Fora do nosso escopo: papel de parede, pendentes de bambu, luminária de
   parede, abajur, roupa de cama, cadeira infantil, mesa lateral, pufe,
   dossel, quadros, suporte para violão e os colchões.
   ⚠ O bandô/cortineiro da Vista 4 é "de gesso OU MDF" — só é nosso se for
     MDF. Fora do preço até a designer decidir.

O ESCOPO DE MARCENARIA — quatro itens
  1 · Cama com bicama ....... 200 × 125 × 70, MDF Itapuã, ripas na cabeceira,
      palha indiana, bicama de rodízio para colchão solteiro
  2 · Mesa .................. 100 × 50 × 80, tampo ripado Itapuã, laterais
      em Sal Rosa, bordas levemente arredondadas
  3 · Prateleiras de canto .. quadrante 59 × 59, 2 cm, cinco delas
  4 · Roupeiro EXISTENTE .... 250 × 268, revestimento da frente

⭐ O PRÓPRIO PROJETO OFERECE DOIS CAMINHOS DE ACABAMENTO, e é daí que saem
  os dois cenários: "Laca fosca Sayerlack J029 OU plotar conforme roupeiro".
"""
import importlib.util, pathlib, sys
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('motor_mc', P/'motor_mc.py')
M = importlib.util.module_from_spec(spec); sys.modules['motor_mc'] = M
spec.loader.exec_module(M)

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
br1 = lambda v: f'{v:,.1f}'.replace(',','X').replace('.',',').replace('X','.')

CH_M2, APROV = 2.75*1.85, 0.80          # chapa padrão da casa
PRECO = {15: 500.0, 18: 600.0}          # MDF cor (Itapuã, Sal Rosa) — base
FITA_M  = 3.0 + 2.5                     # fita cor + filetagem
LACA_M2 = 650.0                         # base da casa, "m² em peça lisa"
PLOT_M2 = 180.0                         # ★ adesivo + aplicação, estimado
# ⭐ [Jonathan 09/10] "palinha considere 950,00 o mt quadrado instalada"
#   ⚠ A R$ 950 INSTALADA, cada m² de palha vale R$ 2.095 de PREÇO. Onde ela
#     entra deixou de ser detalhe: a prancha traz a legenda apontando para a
#     cama, não o pano. Adotei as duas laterais (1,60 m²) e isso precisa de
#     confirmação da designer antes de fechar.
PALHA_M2 = 950.0                        # [Jonathan 09/10], instalada
MC_ALVO = 0.40                          # ⭐ [Jonathan 08/10]

FER_UN = {'rodizio': 25.0, 'corr': 85.0, 'supinv': 60.0}

PCS, FER, TER, LACA, PALHA = {}, {}, {}, {}, {}
def amb(k):
    PCS.setdefault(k, []); TER.setdefault(k, 0.0)
    LACA.setdefault(k, 0.0); PALHA.setdefault(k, 0.0)
    FER.setdefault(k, dict.fromkeys(FER_UN, 0))
def a(k, esp, desc, c, l, q=1, fc=2):
    amb(k); PCS[k].append((esp, desc, c, l, q, fc))
def f(k, **kw):
    amb(k)
    for key, v in kw.items(): FER[k][key] += v
def laca(k, m2): amb(k); LACA[k] += m2
def palha(k, m2): amb(k); PALHA[k] += m2

# ── 1 · CAMA COM BICAMA ───────────────────────────────────────────────────
# 200 × 125, altura 70 na cabeceira e 40 no corpo. Palha nas laterais,
# ripas de 7 na cabeceira. Bicama de rodízio por baixo, colchão 88 × 188.
K = 'Cama com bicama'
a(K,18,'Lateral da caixa',           200,  40, 2)
a(K,18,'Peseira',                    125,  40, 1)
a(K,18,'Cabeceira · moldura',        125,  70, 1)
a(K,18,'Cabeceira · ripa',            70,   7, 16)   # ripado vertical
a(K,15,'Estrado · longarina',        195,  10, 2, 1)
a(K,15,'Estrado · ripa',             120,  10, 9, 1)
a(K,18,'Bicama · lateral',           190,  18, 2)
a(K,18,'Bicama · cabeceira e pé',     90,  18, 2)
a(K,15,'Bicama · estrado',           190,  90, 1, 1)
palha(K, 2*(2.00*0.40))                      # as duas laterais, em palha
f(K, rodizio=4)

# ── 2 · MESA ──────────────────────────────────────────────────────────────
# 100 × 50 × 80. Tampo ripado em Itapuã; laterais em Sal Rosa; o projeto
# pede BORDAS LEVEMENTE ARREDONDADAS — usinagem, não fita reta.
K = 'Mesa'
a(K,18,'Lateral · Sal Rosa',          80,  50, 2)
a(K,18,'Tampo · ripa de Itapuã',     100,   4, 11)
a(K,18,'Tampo · travessa',            92,  10, 2, 1)
a(K,18,'Fundo · Sal Rosa',            92,  44, 1)

# ── 3 · PRATELEIRAS DE CANTO ──────────────────────────────────────────────
# Quadrante de 59 × 59, 2 cm de espessura. Cinco, nas Vistas 3 e 4.
# ⛔ 2 cm não é chapa: são duas de 15 coladas e usinadas no raio.
K = 'Prateleiras de canto'
a(K,15,'Quadrante · duas camadas',    59,  59, 10)
# ⛔ 10 peças = 5 prateleiras de 2 camadas coladas. A prateleira PRONTA tem
#   duas faces, não quatro — e o quadrante é π/4 do quadrado, não metade.
import math
QUAD_M2 = math.pi*0.59**2/4                  # 0,273 m² cada
laca(K, 5*QUAD_M2*2 + 5*(math.pi*0.59/2 + 2*0.59)*0.02)   # faces + canto
f(K, supinv=10)

# ── 4 · ROUPEIRO EXISTENTE · revestimento ─────────────────────────────────
# ⛔ NÃO É MÓVEL NOVO. 250 × 268 de frente, revestida.
#   O projeto admite laca OU adesivo — é o eixo dos dois cenários.
K = 'Roupeiro existente · revestimento'
amb(K)
laca(K, 2.50*2.68)

# ── 4b · ROUPEIRO NOVO — cenário de TROCA  ⭐ [Jonathan 09/10] ────────────
# "crie uma versão com troca das peças atuais por outro MDF melamínico."
# ⛔⛔ O PROJETO NÃO DETALHA O INTERIOR DO ROUPEIRO. A Vista 3 mostra o móvel
#   existente como um PLANO de 250 × 268 — não há planta, não há corte, não
#   há legenda de gavetas nem de cabideiro. Fazer um novo é PROJETAR um,
#   e a configuração interna é que manda no preço.
#   ⭐ A configuração abaixo é MINHA, não da designer. Precisa do aval dela.
ROUPEIRO_NOVO = [
    (15,'Lateral e divisória',   268,  60, 4, 2),
    (15,'Base, tampo e travessa',247,  60, 3, 1),
    (15,'Fundo',                 250, 268, 1, 1),
    (18,'Porta',                 268,  62, 4, 2),
    (15,'Prateleira',             60,  58, 6, 2),
    (18,'Frente de gaveta',       20,  60, 4, 2),
    (15,'Gaveta · lateral',       55,  18, 8, 1),
    (15,'Gaveta · frente e fundo',57,  18, 8, 1),
    (15,'Gaveta · fundo',         57,  55, 4, 1),
    (15,'Rodapé',                250,   4, 1, 1),
    (15,'Rodateto recuado',      250,   2, 1, 1),
]
FER_NOVO = dict(dobr=12, corr=4, cabide=2)
FER_UN.update({'dobr': 35.0, 'cabide': 60.0})
# ⚠ e a retirada do móvel que está lá — desmontagem, descida e descarte.
RETIRADA = 450.0                        # ★ estimado

AMBS = list(PCS)

# ══════════════════════════════════════════════════════════════════════════
def versao(nome, acab_m2, roupeiro_novo=False):
    """acab_m2: preço do m² de acabamento — laca (650) ou plotagem (180).
    roupeiro_novo: troca o móvel existente por um NOVO em melamínico, e aí
    as prateleiras também saem em melamínico com fita, sem laca."""
    KR = 'Roupeiro existente · revestimento'
    KP = 'Prateleiras de canto'
    pcs  = {k: list(v) for k, v in PCS.items()}
    lac  = dict(LACA)
    fer_ = {k: dict(FER[k]) for k in AMBS}
    ter_ = dict(TER)
    if roupeiro_novo:
        pcs[KR] = list(ROUPEIRO_NOVO)       # vira móvel, deixa de ser pintura
        lac[KR] = 0.0
        lac[KP] = 0.0                       # prateleira acompanha: melamínico
        for x, v in FER_NOVO.items(): fer_[KR][x] = fer_[KR].get(x, 0) + v
        ter_[KR] += RETIRADA
    area_mat, ch_amb, fita_amb = {}, {}, {}
    for k in AMBS: ch_amb[k] = fita_amb[k] = 0.0
    for k in AMBS:
        for esp, _, c, l, q, fc in pcs[k]:
            area_mat[esp] = area_mat.get(esp, 0.0) + c*l*q/1e4
            fita_amb[k]  += 2*(c+l)*q/100*(0.75 if fc == 2 else 0.4)*FITA_M
    chapas   = {e: -(-v/(CH_M2*APROV)//1) for e, v in area_mat.items()}
    custo_ch = {e: chapas[e]*PRECO[e] for e in chapas}
    taxa = {e: PRECO[e]/(CH_M2*APROV) for e in area_mat}
    area_k = {}
    for k in AMBS:
        area_k[k] = sum(c*l*q/1e4 for _, _, c, l, q, _ in pcs[k])
        ch_amb[k] = sum(c*l*q/1e4*taxa[esp] for esp, _, c, l, q, _ in pcs[k])
    sobra = sum(custo_ch.values()) - sum(area_mat[e]*taxa[e] for e in area_mat)
    at = sum(area_k.values())
    for k in AMBS:
        if at: ch_amb[k] += sobra*area_k[k]/at
    acab = {k: lac[k]*acab_m2 for k in AMBS}
    palh = {k: PALHA[k]*PALHA_M2 for k in AMBS}
    fer  = {k: sum(fer_[k].get(x, 0)*FER_UN[x] for x in FER_UN) for k in AMBS}
    CDI = {}
    for k in AMBS:
        proprio = ch_amb[k] + fita_amb[k] + acab[k] + palh[k]
        CDI[k] = (proprio*1.06 + fer[k] + ter_[k])*(1 + M.EMBALAGEM)
    BASE = M.base(parcelas=0, rt=False, vendedor=False)
    PV = {k: round(CDI[k]/(BASE - MC_ALVO)/10)*10 for k in AMBS}
    return dict(nome=nome, chapas=chapas, ch=ch_amb, fita=fita_amb, acab=acab,
                palha=palh, fer=fer, CDI=CDI, PV=PV, CD=sum(CDI.values()),
                TOT=sum(PV.values()), BASE=BASE)

V_LACA = versao('Laca fosca Sayerlack J029', LACA_M2)
V_PLOT = versao('Plotagem em adesivo',       PLOT_M2)
V_TROCA = versao('Troca por melamínico novo', LACA_M2, roupeiro_novo=True)

if __name__ == '__main__':
    W = 86
    print('═'*W); print('RAQUEL OLIVEIRA — quarto infantil  ·  PRJ_EXEC_RAQUEL_O_rn')
    print('═'*W)
    print(f'\n{"ITEM":<38}{"laca":>13}{"plotagem":>13}{"dif.":>11}')
    print('─'*W)
    for k in AMBS:
        print(f'{k:<38}{br(V_LACA["PV"][k]):>13}{br(V_PLOT["PV"][k]):>13}'
              f'{br(V_LACA["PV"][k]-V_PLOT["PV"][k]):>11}')
    print('─'*W)
    print(f'{"INVESTIMENTO":<38}{br(V_LACA["TOT"]):>13}{br(V_PLOT["TOT"]):>13}'
          f'{br(V_LACA["TOT"]-V_PLOT["TOT"]):>11}')
    print(f'{"  custo direto":<38}{br(V_LACA["CD"]):>13}{br(V_PLOT["CD"]):>13}')
    print(f'{"  MC":<38}'
          f'{(V_LACA["BASE"]-V_LACA["CD"]/V_LACA["TOT"])*100:>12.1f}%'
          f'{(V_PLOT["BASE"]-V_PLOT["CD"]/V_PLOT["TOT"])*100:>12.1f}%')

    print(f'\n{"═"*W}')
    print('ONDE CADA REAL ESTÁ')
    print(f'{"═"*W}')
    print(f'  {"":<24}{"laca":>13}{"plotagem":>13}')
    for rot, c in (('chapa','ch'), ('fita','fita'), ('acabamento','acab'),
                   ('palha indiana ★','palha'), ('ferragem ★','fer')):
        print(f'  {rot:<24}{br(sum(V_LACA[c].values())):>13}'
              f'{br(sum(V_PLOT[c].values())):>13}')
    print(f'  {"chapas (un)":<24}{sum(V_LACA["chapas"].values()):>13.0f}'
          f'{sum(V_PLOT["chapas"].values()):>13.0f}')

    print(f'\n{"═"*W}')
    print('⛔⛔ TESTE DE MÃO DE OBRA — o modelo da casa precifica MATERIAL')
    print(f'{"═"*W}')
    print('  Este projeto é leve em chapa e pesado em hora: só 4 chapas, mas')
    print('  onze ripas para cortar e arredondar na mesa, cinco quadrantes')
    print('  com raio usinado, um caixilho de palha e uma bicama com rodízio.')
    print('  A MC cobre NF, RT, produção E a mão de obra de bancada.')
    HORAS = 78          # ★ estimativa de bancada + montagem + instalação
    print(f'\n  {"":<30}{"laca":>13}{"plotagem":>13}')
    for rot, fn in (('margem bruta (R$)', lambda v: v['TOT'] - v['CD']),
                    ('menos NF e produção', lambda v: (v['TOT'] - v['CD'])
                        - v['TOT']*(M.NF + sum(M.PRODUCAO.values()))),):
        print(f'  {rot:<30}{br(fn(V_LACA)):>13}{br(fn(V_PLOT)):>13}')
    liq = lambda v: (v['TOT']-v['CD']) - v['TOT']*(M.NF + sum(M.PRODUCAO.values()))
    print(f'  {"por hora, em ~%d h ★" % HORAS:<30}'
          f'{br(liq(V_LACA)/HORAS):>13}{br(liq(V_PLOT)/HORAS):>13}')
    print()
    print('  ⚠ Na versão PLOTAGEM sobram R$ %s por hora de bancada para pagar'
          % br(liq(V_PLOT)/HORAS))
    print('    salário, encargos, galpão e máquina. ⛔ É o item a conferir')
    print(f'    antes de fechar: num projeto assim, a MC de {MC_ALVO*100:.0f}% engana —')
    print('    ela é alta sobre um material barato, e o trabalho é o custo.')

    print(f'\n{"═"*W}')
    print('⛔⛔ A LACA NO EXISTENTE NÃO FECHA CONTRA UM ROUPEIRO NOVO')
    print(f'{"═"*W}')
    KR = 'Roupeiro existente · revestimento'
    _un = LACA_M2*1.06*(1+M.EMBALAGEM)/(V_LACA['BASE']-MC_ALVO)
    print(f'  O roupeiro NOVO completo sai por R$ {br(V_TROCA["PV"][KR])} —')
    print('  número que o Jonathan confirmou como preço de mercado (09/10).')
    print(f'  Pintar só a FRENTE do que já está lá custa R$ {br(V_LACA["PV"][KR])}.')
    print()
    print(f'  {"o que a laca cobre":<34}{"área":>9}{"preço":>11}')
    for rot, m2 in (('só a frente (o lançado)',        2.50*2.68),
                    ('frente + verso das portas',      2.50*2.68 + 5.00),
                    ('frente, verso, laterais e miolo', 16.0)):
        print(f'  {rot:<34}{br1(m2):>7} m²{br(m2*_un):>11}')
    print()
    print(f'  ⛔ Já na hipótese mais enxuta a pintura custa {V_LACA["PV"][KR]/V_TROCA["PV"][KR]*100:.0f}% de um')
    print('     roupeiro novo INTEIRO. E se a laca pegar o verso das portas —')
    print('     que é o mínimo para não abrir a porta e ver o móvel velho —')
    print('     ela passa do preço do novo.')
    print(f'  ⭐ No TOTAL o cenário da troca já é mais barato: R$ {br(V_TROCA["TOT"])}')
    print(f'     contra R$ {br(V_LACA["TOT"])}, porque as prateleiras em melamínico')
    print(f'     custam R$ {br(V_LACA["PV"]["Prateleiras de canto"]-V_TROCA["PV"]["Prateleiras de canto"])} a menos que lacadas.')
    print('     A laca entrega tinta sobre móvel de terceiro, sem garantia de')
    print('     estrutura. A troca entrega móvel novo com 10 anos. Mesmo')
    print('     dinheiro, outro produto.')

    print(f'\n{"═"*W}')
    print('⛔ O ITEM DE RISCO: LACA SOBRE ROUPEIRO EXISTENTE')
    print(f'{"═"*W}')
    print(f'  O roupeiro JÁ EXISTE e provavelmente é melamínico. Laca sobre')
    print(f'  melamínico SÓ PEGA com preparo certo — lixa, primer de')
    print(f'  aderência e cura. Feito errado, descasca em meses, e a garantia')
    print(f'  de 10 anos da casa NÃO cobre repintura de móvel de terceiro.')
    print(f'  ⭐ A plotagem não tem esse risco: adesivo sobre melamínico é')
    print(f'     colagem, não aderência química. E o projeto já a admite —')
    print(f'     "ou plotar conforme roupeiro" está escrito na prancha.')
    print(f'  Só nesse item a diferença é R$ '
          f'{br(V_LACA["PV"]["Roupeiro existente · revestimento"] - V_PLOT["PV"]["Roupeiro existente · revestimento"])}.')

    print(f'\n{"═"*W}')
    print('★ O QUE NÃO VEIO')
    print(f'{"═"*W}')
    print('  · RT da designer Rubia Nascimento. Sem RT no preço acima; com')
    b2 = M.base(parcelas=0, rt=True, vendedor=False)
    for v in (V_LACA, V_PLOT):
        t2 = sum(round(v['CDI'][k]/(b2 - MC_ALVO)/10)*10 for k in AMBS)
        print(f'    RT de 10%, {v["nome"][:28]:<28} R$ {br(v["TOT"])} → R$ {br(t2)}')
    _pm2 = sum(PALHA.values())
    _un  = PALHA_M2*1.06*(1+M.EMBALAGEM)/(V_LACA['BASE']-MC_ALVO)
    print(f'  · ⛔ ONDE ENTRA A PALHA. A R$ {br(PALHA_M2)}/m² instalada, cada m²')
    print(f'    vale R$ {br(_un)} de PREÇO. Adotei {br1(_pm2)} m² (as duas')
    print(f'    laterais da cama) = R$ {br(_pm2*_un)}. A prancha mostra a')
    print('    legenda, não o pano — a designer tem de confirmar o pano.')
    print('  · preço dos rodízios da bicama — não veio.')
    print('  · preço da PLOTAGEM (estimada a R$ '+br(PLOT_M2)+'/m²).')
    print('  · ⛔ o bandô/cortineiro da Vista 4 é "de gesso OU MDF". Se for')
    print('    MDF é nosso, e não está no preço: são ~2,97 m de frente.')
    print('  · ⛔ onde exatamente entra a palha: a prancha mostra a legenda,')
    print('    não o pano. Adotei as duas laterais da cama.')
