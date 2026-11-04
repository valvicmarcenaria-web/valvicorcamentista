# -*- coding: utf-8 -*-
"""ARTHUR & YASMIM — o CLOSET inteiro  [14/10/2026]

⭐⭐ A MODULAÇÃO FECHOU, e por três caminhos independentes:
  1 · a planta cota 410 de VÃO LIVRE entre as duas fileiras. Com fileira de
      60 de profundidade dos dois lados, a parede do fundo mede 530.
  2 · 530 dividido pelo MÓDULO TIPO de 105/106 dá CINCO módulos — e a
      elevação do fundo mostra exatamente cinco, com a penteadeira no meio.
  3 · tirando a penteadeira (sem porta) e a sapateira (porta de espelho),
      sobram OITO módulos de duas folhas = 16 folhas de vidro. É o número
      da cliente. E 4+1+2+2+1 = DEZ módulos, que é a numeração da prancha.

  Nada disso é chute isolado: os três fecham no mesmo arranjo.

⛔ Ainda assim é modulação ADOTADA de caderno de apresentação, não de
   executivo. Medição no local antes de cortar, como sempre.

AS COTAS DAS PRANCHAS
  410 vão livre · 166 fileira direita · 260 altura · 105 módulo tipo
  110 + 23 sapateira · 112 × 250 vão do espelho · 42/30/24 prateleiras
  200 · 185 · 98 · 79 · 102 · 85 · 60 · 21 · 87 · 32 · 37

⭐ [Jonathan 13-14/10]
   · porta COMPRADA PRONTA: fumê R$ 1.300 · espelho R$ 900, sem dobradiça
   · dobradiça nossa: R$ 12
   · portas pela política C — cascata de REVENDA + margem fixa por folha
   · marcenaria a MC 37%, sem RT
   · ILUMINAÇÃO EM LINHA SEPARADA
"""
import importlib.util, pathlib, sys
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('motor_mc', P/'motor_mc.py')
M = importlib.util.module_from_spec(spec); sys.modules['motor_mc'] = M
spec.loader.exec_module(M)

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
br1 = lambda v: f'{v:,.1f}'.replace(',','X').replace('.',',').replace('X','.')

CH_M2, APROV = 2.75*1.85, 0.80
PRECO = {6: 300.0, 15: 500.0, 18: 600.0}      # MDF cor — base da casa
FITA_M  = 3.0 + 2.5
# ⭐ [Jonathan 14/10] "vamos considerar a marcenaria com 30% de MC".
# ⛔ São 5 pontos ABAIXO do MC_PISO da casa (35%). Aplicado também à
#   iluminação, que é fabricação e instalação nossa como a marcenaria.
MC_ALVO = 0.30
MC_PORTA= 0.25
RT_ON   = False
BASE    = M.base(parcelas=0, rt=RT_ON, vendedor=False)
LIQ     = 1 - M.NF
BASE_REV = 1 - (M.NF + M.ERRO
                + LIQ*(M.PRODUCAO['coordenacao'] + M.PRODUCAO['montagem']))

# ── portas, item comprado ────────────────────────────────────────────────
PORTA_FU, PORTA_ES = 1300.0, 900.0
DOBR, N_DOBR, INSTALA = 12.0, 4, 60.0
MARG_FIXA = 400.0        # ★ por folha: receber, guardar, pendurar, garantir
CD_FU = (PORTA_FU + N_DOBR*DOBR + INSTALA)*(1 + M.EMBALAGEM)
CD_ES = (PORTA_ES + N_DOBR*DOBR + INSTALA)*(1 + M.EMBALAGEM)
PV_FU = round((CD_FU + MARG_FIXA)/BASE_REV/10)*10
PV_ES = round((CD_ES + MARG_FIXA)/BASE_REV/10)*10

# ── ferragem e terceiros da marcenaria ──────────────────────────────────
FER_UN = {'dobr':DOBR, 'corr_oc':190.0, 'corr_tel':85.0, 'cabide':60.0,
          'puxador':25.0}
RIPADO_M2 = 420.0      # ★ painel ripado da penteadeira
ESP_PENT  = 600.0      # espelho da penteadeira, R$/m² — base do Jonathan
# ⭐ ILUMINAÇÃO — LINHA SEPARADA [Jonathan 14/10]
LED_M = 85.0           # ★ fita + perfil + usinagem + instalação, por metro

PCS, FER, TER, LED = {}, {}, {}, {}
def amb(k):
    PCS.setdefault(k, []); TER.setdefault(k, 0.0); LED.setdefault(k, 0.0)
    FER.setdefault(k, dict.fromkeys(FER_UN, 0))
def a(k, esp, desc, c, l, q=1, fc=2):
    amb(k); PCS[k].append((esp, desc, c, l, q, fc))
def f(k, **kw):
    amb(k)
    for key, v in kw.items(): FER[k][key] += v
def ter(k, v): amb(k); TER[k] += v
def led(k, m): amb(k); LED[k] += m

ALT, PROF = 260, 60

def modulo(k, larg, gavetas=0, prof=PROF):
    """Módulo de roupeiro: duas laterais, quatro horizontais, fundo,
    maleiro, cabideiro e, quando há, o gaveteiro interno."""
    i = larg - 3.6
    a(k,15,'Lateral',              ALT, prof, 2)
    a(k,15,'Base e tampo',           i, prof, 2)
    a(k,15,'Prateleira divisória',   i, prof, 1)
    a(k,15,'Maleiro',                i, prof, 1)
    a(k, 6,'Fundo',               larg,  ALT, 1, 1)
    f(k, cabide=1)
    led(k, 2.0)                      # ⭐ fita no maleiro e na divisória
    if gavetas:
        a(k,18,'Frente de gaveta',   i-2, 18, gavetas)
        a(k,15,'Gaveta · lateral',  prof-6, 14, 2*gavetas, 1)
        a(k,15,'Gaveta · frente e fundo', i-8, 14, 2*gavetas, 1)
        a(k,15,'Gaveta · fundo',     i-8, prof-8, gavetas, 1)
        f(k, puxador=gavetas)

# ══ os dez módulos ════════════════════════════════════════════════════════
# parede do fundo — cinco de 106, a do meio é a penteadeira
for n in (1, 2, 4, 5):
    modulo(f'Módulo {n}', 106, gavetas=4 if n in (2, 4) else 0)
# fileira direita — 166 em dois de 83
for n in (6, 7):
    modulo(f'Módulo {n}', 83, gavetas=4)
# parede da porta — o de bolsas (105) e o vizinho
for n in (8, 9):
    modulo(f'Módulo {n}', 105, gavetas=4)

# ── 3 · PENTEADEIRA, 106 de largura ─────────────────────────────────────
K = 'Penteadeira'
a(K,15,'Lateral',                 ALT, PROF, 2)
a(K,15,'Base e tampo',            102, PROF, 2)
a(K, 6,'Fundo',                   106,  ALT, 1, 1)
a(K,18,'Bancada · duas camadas',  102,   50, 2)
a(K,18,'Frente de gaveta',         40,   15, 6)
a(K,15,'Gaveta · lateral',         45,   12, 12, 1)
a(K,15,'Gaveta · frente e fundo',  38,   12, 12, 1)
a(K,15,'Gaveta · fundo',           38,   45, 6, 1)
a(K,15,'Painel ripado · base',    106,  120, 1, 1)
f(K, corr_oc=6, corr_tel=6, puxador=6)
ter(K, 1.06*1.20*RIPADO_M2 + 0.70*1.00*ESP_PENT)   # ripado + espelho
led(K, 3.4)                         # ⭐ perímetro do espelho

# ── 10 · SAPATEIRA, 110 + coluna de 23, fora do closet ──────────────────
K = 'Sapateira'
SAP_P = 38
a(K,15,'Lateral',                 ALT, SAP_P, 2)
a(K,15,'Lateral da coluna',       ALT,    25, 2)
a(K,15,'Base e tampo',            107, SAP_P, 2)
a(K,15,'Prateleira inclinada',    107, SAP_P, 8)
a(K,15,'Divisória do porta-botas',  42, SAP_P, 2)
a(K,15,'Prateleira da coluna',     20,    25, 7)
a(K, 6,'Fundo',                   133,  ALT, 1, 1)
led(K, 8*1.07 + 1.0)                # ⭐ fita em toda prateleira

AMBS = list(PCS)
MOD_PORTA = [k for k in AMBS if k.startswith('Módulo')]   # oito, duas folhas

# ══════════════════════════════════════════════════════════════════════════
def calcula(corr):
    """corr = 'corr_oc' (principal) ou 'corr_tel' (downgrade)."""
    area, ch, fita, area_k = {}, {}, {}, {}
    for k in AMBS:
        ch[k] = fita[k] = 0.0
        for esp, _, c, l, q, fc in PCS[k]:
            area[esp] = area.get(esp, 0.0) + c*l*q/1e4
            fita[k] += 2*(c+l)*q/100*(0.75 if fc == 2 else 0.4)*FITA_M
    chapas   = {e: -(-v/(CH_M2*APROV)//1) for e, v in area.items()}
    custo_ch = {e: chapas[e]*PRECO[e] for e in chapas}
    taxa = {e: PRECO[e]/(CH_M2*APROV) for e in area}
    for k in AMBS:
        area_k[k] = sum(c*l*q/1e4 for _, _, c, l, q, _ in PCS[k])
        ch[k] = sum(c*l*q/1e4*taxa[esp] for esp, _, c, l, q, _ in PCS[k])
    sobra = sum(custo_ch.values()) - sum(area[e]*taxa[e] for e in area)
    at = sum(area_k.values())
    for k in AMBS: ch[k] += sobra*area_k[k]/at
    # ⭐ a corrediça do cenário escolhido, nas gavetas de cada módulo
    fer_c = {}
    for k in AMBS:
        n_g = sum(q for esp, d, c, l, q, fc in PCS[k] if d == 'Frente de gaveta')
        base_f = sum(FER[k][x]*FER_UN[x] for x in ('dobr','cabide','puxador'))
        fer_c[k] = base_f + n_g*FER_UN[corr]
    CDI = {k: ((ch[k] + fita[k])*1.06 + fer_c[k] + TER[k])*(1 + M.EMBALAGEM)
           for k in AMBS}
    PV  = {k: round(CDI[k]/(BASE - MC_ALVO)/10)*10 for k in AMBS}
    n_gav = sum(sum(q for esp, d, c, l, q, fc in PCS[k] if d == 'Frente de gaveta')
                for k in AMBS)
    return dict(ch=ch, fita=fita, fer=fer_c, CDI=CDI, PV=PV, chapas=chapas,
                area=area, custo_ch=custo_ch, sobra=sobra, n_gav=n_gav,
                CD=sum(CDI.values()), TOT=sum(PV.values()))

OCULTA = calcula('corr_oc')
TELESC = calcula('corr_tel')

# ── iluminação, LINHA SEPARADA ──────────────────────────────────────────
LED_TOT_M = sum(LED.values())
LED_CD    = LED_TOT_M*LED_M*(1 + M.EMBALAGEM)
LED_PV    = round(LED_CD/(BASE - MC_ALVO)/10)*10

# ── os três cenários de porta ───────────────────────────────────────────
N_FOLHAS_VIDRO, N_FOLHAS_ESP = 16, 2
CEN = [('1 · mista',            5, 11),
       ('2 · como o projeto',  16,  0),
       ('3 · toda em Fendi',    0, 16)]
# a folha em MDF Fendi é FABRICAÇÃO nossa — paga a cascata cheia
CD_FE = ((0.525*2.50/(CH_M2*APROV)*PRECO[18] + 2*(0.525+2.50)*FITA_M)*1.06
         + N_DOBR*DOBR)*(1 + M.EMBALAGEM)
PV_FE = round(CD_FE/(BASE - MC_PORTA)/10)*10

def portas(nf, nd):
    return nf*PV_FU + nd*PV_FE + N_FOLHAS_ESP*PV_ES

if __name__ == '__main__':
    W = 92
    print('═'*W)
    print('ARTHUR & YASMIM — CLOSET  ·  orçamento fechado')
    print(f'marcenaria MC {MC_ALVO*100:.0f}% · portas pela política C · sem RT')
    print('═'*W)

    print(f'\n{"CHAPA":<12}{"área líq.":>12}{"chapas":>9}{"R$/chapa":>11}{"custo":>11}')
    print('─'*W)
    for e in sorted(OCULTA['area']):
        print(f'{e:>3} mm{"":<6}{br1(OCULTA["area"][e]):>10} m²'
              f'{OCULTA["chapas"][e]:>9.0f}{br(PRECO[e]):>11}'
              f'{br(OCULTA["custo_ch"][e]):>11}')
    print('─'*W)
    print(f'{"TOTAL":<12}{br1(sum(OCULTA["area"].values())):>10} m²'
          f'{sum(OCULTA["chapas"].values()):>9.0f}{"":>11}'
          f'{br(sum(OCULTA["custo_ch"].values())):>11}')

    print(f'\n{"═"*W}')
    print('A MARCENARIA, MÓDULO A MÓDULO  —  sem portas e sem iluminação')
    print(f'{"═"*W}')
    print(f'{"":<22}{"chapa":>9}{"fita":>8}{"ferr.+terc.":>13}'
          f'{"custo":>10}{"oculta":>10}{"telescóp.":>11}')
    print('─'*W)
    for k in AMBS:
        print(f'{k:<22}{br(OCULTA["ch"][k]):>9}{br(OCULTA["fita"][k]):>8}'
              f'{br(OCULTA["fer"][k]+TER[k]):>13}{br(OCULTA["CDI"][k]):>10}'
              f'{br(OCULTA["PV"][k]):>10}{br(TELESC["PV"][k]):>11}')
    print('─'*W)
    print(f'{"MARCENARIA":<22}{"":>9}{"":>8}{"":>13}{br(OCULTA["CD"]):>10}'
          f'{br(OCULTA["TOT"]):>10}{br(TELESC["TOT"]):>11}')
    print(f'  {OCULTA["n_gav"]} gavetas  ·  corrediça oculta Hettich '
          f'R$ {br(FER_UN["corr_oc"])} ★ × telescópica R$ {br(FER_UN["corr_tel"])}')
    print(f'  ⭐ o downgrade economiza R$ {br(OCULTA["TOT"]-TELESC["TOT"])} '
          f'({(1-TELESC["TOT"]/OCULTA["TOT"])*100:.1f}%)')
    print(f'\n  ⚠⚠ OS R$ {br(FER_UN["corr_oc"])} DA OCULTA SÃO ★ MEUS, e é o maior palpite')
    print('    que sobrou no orçamento. A dobradiça eu errei em quase seis')
    print('    vezes; não há razão para a corrediça ser diferente. E ela')
    print('    carrega SOZINHA a diferença entre principal e downgrade:')
    for c in (120, 150, 190, 240):
        d = OCULTA['n_gav']*(c - FER_UN['corr_tel'])*(1 + M.EMBALAGEM)
        print(f'      oculta a R$ {br(c)}  →  o downgrade economiza '
              f'R$ {br(round(d/(BASE-MC_ALVO)/10)*10)}')
    print('    ⛔ Antes de a proposta sair, vale o preço real da Hettich.')

    print(f'\n{"═"*W}')
    print('⭐ ILUMINAÇÃO — LINHA SEPARADA  [Jonathan 14/10]')
    print(f'{"═"*W}')
    print(f'  {br1(LED_TOT_M)} m de fita em perfil, a R$ {br(LED_M)}/m ★ — '
          f'custo R$ {br(LED_CD)}, preço R$ {br(LED_PV)}')
    for k in AMBS:
        if LED[k]: print(f'    {k:<24}{br1(LED[k]):>7} m')
    print('  ⚠ Fita, perfil, usinagem e instalação são nossos. FONTE, driver,')
    print('    circuito e interruptor são da elétrica — não estão aqui.')

    print(f'\n{"═"*W}')
    print('⭐⭐ O QUADRO DA PROPOSTA')
    print(f'{"═"*W}')
    print(f'  porta fumê R$ {br(PV_FU)}  ·  porta de espelho R$ {br(PV_ES)}  ·  '
          f'porta em Fendi R$ {br(PV_FE)}')
    for corr, R in (('corrediça OCULTA Hettich', OCULTA),
                    ('corrediça TELESCÓPICA', TELESC)):
        print(f'\n  ── {corr} ' + '─'*(W-len(corr)-7))
        print(f'  {"":<34}{"marcenaria":>12}{"portas":>11}{"iluminação":>12}'
              f'{"TOTAL":>12}')
        for nome, nf, nd in CEN:
            pt = portas(nf, nd)
            print(f'  {nome:<34}{br(R["TOT"]):>12}{br(pt):>11}{br(LED_PV):>12}'
                  f'{br(R["TOT"] + pt + LED_PV):>12}')

    print(f'\n{"═"*W}')
    print(f'⛔⛔ A MC DE {MC_ALVO*100:.0f}% ESTÁ ABAIXO DO PISO DA CASA '
          f'({M.MC_PISO*100:.0f}%)')
    print(f'{"═"*W}')
    _p37 = sum(round(OCULTA['CDI'][k]/(BASE-0.37)/10)*10 for k in AMBS)
    _p35 = sum(round(OCULTA['CDI'][k]/(BASE-M.MC_PISO)/10)*10 for k in AMBS)
    print(f'  a marcenaria, com corrediça oculta:')
    print(f'    a 37% ....... R$ {br(_p37)}')
    print(f'    a 35%, piso . R$ {br(_p35)}')
    print(f'    a {MC_ALVO*100:.0f}% ....... R$ {br(OCULTA["TOT"])}   '
          f'−R$ {br(_p37-OCULTA["TOT"])} contra os 37%')
    # MC cheia do projeto, cenário 2 com oculta
    # ⛔ a MC cheia NÃO se tira de uma base só: marcenaria e iluminação
    #   correm na cascata da casa, a porta na de revenda. Cada parte paga
    #   os encargos dela.
    _pv_m = OCULTA['TOT'] + LED_PV
    _pv_p = portas(16, 0)
    _cd2  = OCULTA['CD'] + LED_CD + 16*CD_FU + 2*CD_ES
    _enc  = _pv_m*(1 - BASE) + _pv_p*(1 - BASE_REV)
    _mc2  = (_pv_m + _pv_p) - _cd2 - _enc
    _mcp  = _mc2/(_pv_m + _pv_p)
    print(f'\n  ⛔ E a MC CHEIA do projeto no cenário 2 — marcenaria e')
    print(f'    iluminação na cascata da casa, porta na de revenda — fica em')
    print(f'    R$ {br(_mc2)} sobre R$ {br(_pv_m+_pv_p)}, ou seja {_mcp*100:.1f}%.')
    print('    Quem paga o custo fixo da fábrica é a MC, e ela está')
    print(f'    {M.MC_PISO*100 - _mcp*100:.1f} pontos abaixo do piso.')
    print('    ⭐ Não é um erro: é uma decisão de preço para ganhar a obra.')
    print('      Só precisa ser tomada sabendo que, nesta, a fábrica não')
    print('      cobre a estrutura — e a próxima tem de cobrir pelas duas.')

    print(f'\n{"═"*W}')
    print('★ A MODULAÇÃO ADOTADA — e por que ela fecha')
    print(f'{"═"*W}')
    print('  410 de vão livre + 60 + 60 de fileira = 530 na parede do fundo')
    print('  530 ÷ 5 = 106, que é o módulo tipo de 105 cotado na prancha')
    print('  oito módulos de duas folhas = 16 folhas + 1 espelho = a conta')
    print('  da cliente · e 4 + penteadeira + 2 + 2 + sapateira = DEZ módulos,')
    print('  que é a numeração da prancha. Os três caminhos fecham igual.')
    print('\n  ⛔ Ainda é caderno de apresentação, não executivo: MEDIÇÃO NO')
    print('    LOCAL antes de cortar, e o preço se confirma na medida.')
    print('  ★ Também adotados: profundidade 60 nos módulos e 38 na sapateira,')
    print(f'    {OCULTA["n_gav"]} gavetas, maleiro e cabideiro em cada módulo, e')
    print(f'    {br1(LED_TOT_M)} m de fita de LED.')
