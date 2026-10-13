# -*- coding: utf-8 -*-
"""APTO ORLANDO E IVONE — banho suíte master, Belo Horizonte  [13/10/2026]

Projeto: [31] APTO ORLANDO E IVONE, Rua Passa Tempo, BH. Arquiteta
**ANA MARIA CASTRO · CAU A94939-6**. Arquivo 31_APTO IVONE E ORLANDO_DT_03.
Duas pranchas A3, revisão 00, 12/10/2026:
  31_.2  planta baixa térreo + marcenaria + acabamentos + legendas + render
  31_.6  BANHO SUITE_ELEVAÇÃO 01 e ELEVAÇÃO 04, escala 1:25

⛔ CARIMBO: "NÃO PLOTAR, ESTUDO ENVIADO PARA ANÁLISE" — é ESTUDO, revisão 00.
   Medida de obra ainda não conferida; orçamento sujeito a remedição.

O BANHEIRO: A = 3,43 m², pé-direito 2,48 (245,5 sob o forro),
            115 de largura por 295 de comprimento.

O ESCOPO DA MARCENARIA — a legenda da prancha 31_.2 traz só dois itens:
  01 · ARMÁRIO INFERIOR EM MDF A DEFINIR
  02 · ARMÁRIO SUPERIOR EM MDF BRANCO COM PORTAS DE GIRO COM PERFIL DE
       ALUMÍNIO E ESPELHO PRATA. PREVER PARTES FIXAS PARA ILUMINAÇÃO FRONTAL

⛔⛔ O QUE NÃO É NOSSO — e a proposta tem de dizer, porque num banheiro
   deste tamanho a marcenaria é a MENOR parte do que o cliente vê:
   · MARMORARIA: bancada e rodabanca em mármore branco (H=90, rodabanca 35,
     testeira 20), acabamento do sóculo e o NICHO em mármore de toda a
     parede do box, com acabamento em 45° (10 de profundidade, 35 de altura)
   · SÓCULO em alvenaria (obra), que recebe a marcenaria
   · BOX de correr de 3 folhas 134×215, vidro temperado e perfis (vidraceiro)
   · LOUÇAS E METAIS Deca (VS.1, CB.1, TR.1, DH.1, BA.1/2, C.1, TO.1/2,
     PA.1, RA.1/2, RG) e o chuveiro CH.1, existente, a ser mantido
   · ARANDELAS, driver/fonte, luminárias, tomadas, forro e pintura
   · PORCELANATO 90×90 de piso e parede e as soleiras S1 em mármore
"""
import importlib.util, pathlib, sys
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('motor_mc', P/'motor_mc.py')
M = importlib.util.module_from_spec(spec); sys.modules['motor_mc'] = M
spec.loader.exec_module(M)

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
br1 = lambda v: f'{v:,.1f}'.replace(',','X').replace('.',',').replace('X','.')

CH_M2, APROV = 2.75*1.85, 0.80
# ⛔ É BANHEIRO. A prancha diz só "MDF a definir" — não especifica chapa
#   resistente à umidade. A casa não entrega armário de banheiro em MDF
#   comum: debaixo de cuba e ao lado de box, o miolo incha. Orçado em
#   MDF ULTRA (verde, resistente à umidade), como a arquiteta da Raquel
#   Franco especificou no projeto dela.
#   ★ A chapa Ultra não está na base da casa; estimada em +30% sobre a cor.
PRECO = {('cor',6):300.0, ('cor',15):500.0, ('cor',18):600.0,
         ('br',6):190.0,  ('br',15):260.0,  ('br',18):330.0,
         ('ultra',6):390.0, ('ultra',15):650.0, ('ultra',18):780.0,
         ('ultrabr',6):247.0, ('ultrabr',15):338.0, ('ultrabr',18):429.0}
FITA_COR = 3.0 + 2.5           # fita amadeirada + filetagem na coladeira
FITA_BR  = 2.0 + 2.5           # fita branca + filetagem
MC_ALVO = 0.35                 # ⭐ [Jonathan 13/10] "traz a MC para 35%"
RT_ON   = True                 # ⭐ [Jonathan 13/10] "e inclui a RT"
BASE    = M.base(parcelas=0, rt=RT_ON, vendedor=False)

FER_UN  = {'dobr':35.0, 'corr':85.0, 'puxador':55.0}
FER_NOME = {'dobr':'dobradiça com amortecedor',
            'corr':'corrediça telescópica',
            'puxador':'puxador Zen Phenix 20 cm'}
# ⭐ [Jonathan 09/10] espelho a R$ 600,00 o m², fornecimento nosso.
ESPELHO_M2 = 600.0
PERFIL_M   = 75.0     # ★ perfil de alumínio prata da porta de espelho, por m
ARANDELA_PC= 90.0     # ★ usinagem da passagem e berço do driver, por peça fixa

NOME_CH = {'ultra': 'Ultra amadeirado', 'ultrabr': 'Ultra branco',
           'cor': 'MDF cor', 'br': 'Branco TX'}

PCS, FER, TER = {}, {}, {}
def amb(k):
    PCS.setdefault(k, []); TER.setdefault(k, 0.0)
    FER.setdefault(k, dict.fromkeys(FER_UN, 0))
def a(k, cor, esp, desc, c, l, q=1, fc=2):
    amb(k); PCS[k].append((cor, esp, desc, c, l, q, fc))
def f(k, **kw):
    amb(k)
    for key, v in kw.items(): FER[k][key] += v
def ter(k, v): amb(k); TER[k] += v

# ⭐ [Jonathan 13/10] "considere interno branco e externo em amadeirado
#   fosco". A caixaria vai em MDF Ultra BRANCO e tudo o que se vê — portas,
#   frentes de gaveta, as três peças fixas da espelheira, a lateral direita
#   dos dois móveis (que fica solta, sem parede) e a base da espelheira
#   (que se enxerga por baixo) — vai em AMADEIRADO FOSCO.
#   ⭐ E todo o aparente foi para 18 mm de propósito: assim o amadeirado
#     cabe em UMA chapa só. Ver o quadro no fim.

# ══ 1 · ARMÁRIO INFERIOR ══════════════════════════════════════════════════
# 119 de frente × 63 de altura × 46 de profundidade, sobre sóculo de 15.
# Frente: 71,5 de portas de giro (2 folhas) + 47,5 de gavetas (4).
# Gavetas de cima para baixo: 10 · 17 · 17 · 17. A cuba cai sobre o vão
# das portas — por isso as gavetas não têm conflito com o sifão.
K = 'Armário inferior'
a(K,'ultra',  18,'Lateral aparente',        63,  46, 1)   # amadeirado
a(K,'ultrabr',15,'Lateral de parede',       63,  46, 1)
a(K,'ultrabr',15,'Divisória vertical',      63,  46, 1)
a(K,'ultrabr',15,'Base',                   115,  46, 1)
a(K,'ultrabr',15,'Travessa superior',      115,  10, 2)
a(K,'ultrabr', 6,'Fundo',                  119,  63, 1, 1)
a(K,'ultra',  18,'Porta de giro',           61,  36, 2)   # amadeirado
a(K,'ultra',  18,'Frente de gaveta',        48,  10, 1)   # amadeirado
a(K,'ultra',  18,'Frente de gaveta',        48,  17, 3)   # amadeirado
a(K,'ultrabr',15,'Gaveta · lateral',        42,  12, 8, 1)
a(K,'ultrabr',15,'Gaveta · frente e fundo', 44,  12, 8, 1)
a(K,'ultrabr',15,'Gaveta · fundo',          44,  42, 4, 1)
a(K,'ultrabr',15,'Prateleira interna',      68,  42, 1)   # ★ ver EM ABERTO
f(K, dobr=4, corr=4, puxador=6)   # puxador Zen Phenix 20 cm cromado

# ══ 2 · ARMÁRIO SUPERIOR · ESPELHEIRA ═════════════════════════════════════
# 195 × 90 × 15, 30,5 abaixo do forro e 35 acima da bancada.
# Frente: 10 + 82,5 + 10 + 82,5 + 10. As três peças de 10 são FIXAS e é
# nelas que vão as arandelas e, por dentro, o driver. Cada vão de 82,5
# fecha com DUAS folhas de espelho em perfil de alumínio, com trespasse
# de 1 cm sobre a peça fixa fazendo as vezes de puxador.
# Por dentro, duas prateleiras por vão (23 · 30 · 30 na elevação 04).
K = 'Armário superior'
ESP_L, ESP_A, ESP_N = 0.4225, 0.90, 4
a(K,'ultra',  18,'Lateral aparente',        90,  15, 1)   # amadeirado
a(K,'ultrabr',15,'Lateral de parede',       90,  15, 1)
a(K,'ultrabr',15,'Divisória vertical',      90,  15, 1)
a(K,'ultra',  18,'Base · vista por baixo', 191,  15, 1)   # amadeirado
a(K,'ultrabr',15,'Tampo',                  191,  15, 1)
a(K,'ultrabr', 6,'Fundo',                  195,  90, 1, 1)
a(K,'ultrabr',15,'Prateleira',              95,  13, 4)
a(K,'ultra',  18,'Peça fixa frontal',       90,  10, 3)   # amadeirado
f(K, dobr=8)
ter(K, ESP_N*ESP_L*ESP_A*ESPELHO_M2                      # espelho prata
     + ESP_N*2*(ESP_L+ESP_A)*PERFIL_M                    # perfil de alumínio
     + 3*ARANDELA_PC)                                    # preparo das fixas

AMBS = list(PCS)

# ══════════════════════════════════════════════════════════════════════════
def calcula(pcs):
    area_mat, ch, fita, area_k = {}, {}, {}, {}
    for k in AMBS:
        ch[k] = fita[k] = 0.0
        for cor, esp, _, c, l, q, fc in pcs[k]:
            m = (cor, esp)
            area_mat[m] = area_mat.get(m, 0.0) + c*l*q/1e4
            fm = FITA_BR if cor.endswith('br') else FITA_COR
            fita[k] += 2*(c+l)*q/100*(0.75 if fc == 2 else 0.4)*fm
    chapas   = {m: -(-v/(CH_M2*APROV)//1) for m, v in area_mat.items()}
    custo_ch = {m: chapas[m]*PRECO[m] for m in chapas}
    # ⛔ cada peça paga a própria taxa; a sobra de corte rateia pela área
    #   total (lição da Alice — ratear chapa inteira inverte cenário).
    taxa = {m: PRECO[m]/(CH_M2*APROV) for m in area_mat}
    for k in AMBS:
        area_k[k] = sum(c*l*q/1e4 for _,_,_,c,l,q,_ in pcs[k])
        ch[k] = sum(c*l*q/1e4*taxa[(cor,esp)] for cor,esp,_,c,l,q,_ in pcs[k])
    sobra = sum(custo_ch.values()) - sum(area_mat[m]*taxa[m] for m in area_mat)
    at = sum(area_k.values())
    for k in AMBS: ch[k] += sobra*area_k[k]/at
    fer_c = {k: sum(FER[k][x]*FER_UN[x] for x in FER_UN) for k in AMBS}
    CDI = {k: ((ch[k] + fita[k])*1.06 + fer_c[k] + TER[k])*(1 + M.EMBALAGEM)
           for k in AMBS}
    PV  = {k: round(CDI[k]/(BASE - MC_ALVO)/10)*10 for k in AMBS}
    return dict(ch=ch, fita=fita, fer=fer_c, CDI=CDI, PV=PV, chapas=chapas,
                custo_ch=custo_ch, area=area_mat, sobra=sobra,
                CD=sum(CDI.values()), TOT=sum(PV.values()))

COR = calcula(PCS)
ch, fita, fer_custo, CDI = COR['ch'], COR['fita'], COR['fer'], COR['CDI']
area_mat, chapas, custo_ch = COR['area'], COR['chapas'], COR['custo_ch']
CD, PV, TOT = COR['CD'], COR['PV'], COR['TOT']

# ── para comparar: TUDO amadeirado, interno inclusive, que era o orçamento
#   de antes da instrução do Jonathan de 13/10.
PCS_TC = {k: [('ultra', e, d, c, l, q, fc) for _, e, d, c, l, q, fc in v]
          for k, v in PCS.items()}
TUDOCOR = calcula(PCS_TC)

# ── o que o mesmo custo daria nas outras duas combinações ───────────────
BASE_SRT = M.base(parcelas=0, rt=False, vendedor=False)
PV_SRT   = {k: round(CDI[k]/(BASE_SRT - MC_ALVO)/10)*10 for k in AMBS}
TOT_SRT  = sum(PV_SRT.values())          # mesma MC, sem RT
PV_40    = {k: round(CDI[k]/(BASE - 0.40)/10)*10 for k in AMBS}
TOT_40   = sum(PV_40.values())           # com RT, na MC de 40% de antes

if __name__ == '__main__':
    W = 90
    print('═'*W)
    print('APTO ORLANDO E IVONE — banho suíte master  ·  [31] rev. 00')
    print('arquiteta Ana Maria Castro · CAU A94939-6 · 12/10/2026')
    print('═'*W)

    print(f'\n{"CHAPA":<22}{"área líq.":>12}{"chapas":>9}{"R$/chapa":>11}{"custo":>11}')
    print('─'*W)
    for m in sorted(area_mat, key=lambda x: (x[0], x[1])):
        print(f'{(NOME_CH[m[0]] + "  " + str(m[1]) + " mm"):<22}'
              f'{br1(area_mat[m]):>10} m²{chapas[m]:>9.0f}'
              f'{br(PRECO[m]):>11}{br(custo_ch[m]):>11}')
    print('─'*W)
    print(f'{"TOTAL":<22}{br1(sum(area_mat.values())):>10} m²'
          f'{sum(chapas.values()):>9.0f}{"":>11}{br(sum(custo_ch.values())):>11}')

    print(f'\n{"═"*W}')
    print(f'{"PEÇA":<24}{"chapa":>9}{"fita":>8}{"ferr.+terc.":>13}'
          f'{"custo":>10}{"preço":>10}{"MC":>8}')
    print('─'*W)
    for k in AMBS:
        print(f'{k:<24}{br(ch[k]):>9}{br(fita[k]):>8}'
              f'{br(fer_custo[k]+TER[k]):>13}{br(CDI[k]):>10}{br(PV[k]):>10}'
              f'{(BASE-CDI[k]/PV[k])*100:>7.1f}%')
    print('─'*W)
    print(f'{"INVESTIMENTO":<24}{br(sum(ch.values())):>9}'
          f'{br(sum(fita.values())):>8}'
          f'{br(sum(fer_custo.values())+sum(TER.values())):>13}'
          f'{br(CD):>10}{br(TOT):>10}{(BASE-CD/TOT)*100:>7.1f}%')
    print(f'  ⭐ MC de 35% COM RT de 10% — base {BASE*100:.2f}%  ·  '
          f'{sum(chapas.values()):.0f} chapas  [Jonathan 13/10]')
    print(f'  · o MESMO custo SEM RT daria R$ {br(TOT_SRT)} — '
          f'o RT custa R$ {br(TOT-TOT_SRT)} ao cliente ({(TOT/TOT_SRT-1)*100:.1f}%)')
    print(f'  · na MC de 40% de antes, com RT, seria R$ {br(TOT_40)} — '
          f'descemos R$ {br(TOT_40-TOT)} ({(1-TOT/TOT_40)*100:.1f}%)')
    print(f'  ⛔ 35% é o PISO da casa (MC_PISO). Abaixo disto não há negociação,')
    print(f'    há prejuízo de estrutura: a MC ainda tem de pagar o custo fixo.')

    # ══ COMPOSIÇÃO DE CUSTO ════════════════════════════════════════════
    print(f'\n{"═"*W}')
    print('COMPOSIÇÃO DO CUSTO DIRETO — de onde vem o R$ ' + br(CD))
    print(f'{"═"*W}')
    cons = {k: (ch[k]+fita[k])*0.06 for k in AMBS}
    emb  = {k: CDI[k]/(1+M.EMBALAGEM)*M.EMBALAGEM for k in AMBS}
    _am = int(sum(v for m, v in chapas.items() if m[0] == 'ultra'))
    _bo = int(sum(chapas.values())) - _am
    LIN = [(f'chapa  ·  {_am} amadeirada + {_bo} brancas', {k: ch[k] for k in AMBS}),
           ('fita de borda e filetagem',      dict(fita)),
           ('consumíveis  ·  6% de chapa e fita', cons),
           ('ferragem',                       dict(fer_custo)),
           ('terceiros  ·  espelho e perfil', dict(TER)),
           ('embalagem  ·  2% do custo',      emb)]
    print(f'{"":<38}{"inferior":>11}{"superior":>11}{"total":>11}{"%":>8}')
    print('─'*W)
    for nome, d in LIN:
        t = sum(d.values())
        print(f'{nome:<38}{br(d[AMBS[0]]):>11}{br(d[AMBS[1]]):>11}'
              f'{br(t):>11}{t/CD*100:>7.1f}%')
    print('─'*W)
    print(f'{"CUSTO DIRETO":<38}{br(CDI[AMBS[0]]):>11}{br(CDI[AMBS[1]]):>11}'
          f'{br(CD):>11}{100.0:>7.1f}%')

    print(f'\n  a ferragem, aberta:')
    for x in FER_UN:
        n = sum(FER[k][x] for k in AMBS)
        if n: print(f'    {FER_NOME[x]:<28}{n:>3} × R$ {br(FER_UN[x]):>5}'
                    f'  =  R$ {br(n*FER_UN[x])}')
    print(f'  os terceiros, abertos:')
    print(f'    espelho prata        {ESP_N} folhas a R$ {br(ESPELHO_M2)}/m²  =  '
          f'R$ {br(ESP_N*ESP_L*ESP_A*ESPELHO_M2)}')
    print(f'    perfil de alumínio   ★ R$ {br(PERFIL_M)}/m              =  '
          f'R$ {br(ESP_N*2*(ESP_L+ESP_A)*PERFIL_M)}')
    print(f'    preparo das 3 fixas  ★ berço e passagem do driver  =  '
          f'R$ {br(3*ARANDELA_PC)}')

    # ══ COMPOSIÇÃO DO PREÇO ════════════════════════════════════════════
    print(f'\n{"═"*W}')
    print('COMPOSIÇÃO DO PREÇO — para onde vai o R$ ' + br(TOT))
    print(f'{"═"*W}')
    enc = M.encargos(parcelas=0, rt=RT_ON, vendedor=False)
    print(f'{"":<38}{"R$":>12}{"% do preço":>14}')
    print('─'*W)
    print(f'{"custo direto":<38}{br(CD):>12}{CD/TOT*100:>13.2f}%')
    for nome, v in enc.items():
        if v: print(f'{nome:<38}{br(TOT*v):>12}{v*100:>13.2f}%')
    print('─'*W)
    mc_r = TOT - CD - sum(TOT*v for v in enc.values())
    print(f'{"MARGEM DE CONTRIBUIÇÃO":<38}{br(mc_r):>12}{mc_r/TOT*100:>13.2f}%')
    print(f'{"PREÇO":<38}{br(TOT):>12}{100.0:>13.2f}%')
    print(f'\n  base da casa {BASE*100:.2f}% — com RT de 10%, sem comissão de vendedor.')
    print(f'  ⚠ A MC não é lucro: dela ainda sai o custo fixo da fábrica.')
    print(f'\n  ⛔⛔ A MC CAIU 5 PONTOS E O CLIENTE PAGA MAIS CARO.')
    _mc40 = TOT_40*(BASE-CD/TOT_40)
    _ant  = sum(round(CDI[k]/(BASE_SRT-0.40)/10)*10 for k in AMBS)
    _mcan = _ant*(BASE_SRT-CD/_ant)
    print(f'    MC 40% sem RT (ontem) ...... preço R$ {br(_ant)}  ·  MC R$ {br(_mcan)}')
    print(f'    MC 35% com RT (hoje) ....... preço R$ {br(TOT)}  ·  MC R$ {br(TOT-CD-sum(TOT*v for v in enc.values()))}')
    print(f'    O cliente paga R$ {br(TOT-_ant)} A MAIS e a casa ganha '
          f'R$ {br(_mcan-(TOT-CD-sum(TOT*v for v in enc.values()))):} A MENOS.')
    print(f'    No meio ficam R$ {br(TOT*enc["RT"])} de RT. Os 5 pontos de margem que')
    print('    abrimos não chegam ao cliente — pagam a arquiteta, e sobra')
    print('    conta para ele. ⚠ Se a ideia era baixar o preço, o caminho é')
    print('    tirar o RT, não a margem.')
    print(f'  ⛔ E dentro do custo direto há R$ {br(COR["sobra"])} de SOBRA de chapa,')
    print(f'    {COR["sobra"]/CD*100:.0f}% do custo direto — ver o quadro da sobra adiante.')

    print(f'\n{"═"*W}')
    print('⭐ A ESPELHEIRA É QUASE METADE DO ORÇAMENTO')
    print(f'{"═"*W}')
    ks = 'Armário superior'
    print(f'  R$ {br(PV[ks])} de R$ {br(TOT)} — {PV[ks]/TOT*100:.0f}%. '
          f'E dois terços disso não é')
    print('  madeira: é espelho prata, perfil de alumínio e oito dobradiças')
    print('  carregando folha de espelho, que não perdoa desalinho.')
    esp = ESP_N*ESP_L*ESP_A*ESPELHO_M2
    per = ESP_N*2*(ESP_L+ESP_A)*PERFIL_M
    print(f'    espelho prata ........ R$ {br(esp)}')
    print(f'    perfil de alumínio ... R$ {br(per)}   ★ estimado a R$ {br(PERFIL_M)}/m')
    print(f'    preparo das fixas .... R$ {br(3*ARANDELA_PC)}   ★ passagem e berço do driver')

    print(f'\n{"═"*W}')
    print('⛔ O QUE A PROPOSTA PRECISA DIZER QUE NÃO É NOSSO')
    print(f'{"═"*W}')
    print('  bancada, rodabanca, testeira, sóculo e o nicho do box — tudo')
    print('  MARMORARIA. Box de correr — vidraceiro. Louças e metais Deca,')
    print('  arandelas e driver, tomadas, forro, pintura e porcelanato —')
    print('  obra. Num banheiro de 3,43 m² o cliente olha o conjunto e')
    print('  compara com o preço da marcenaria. Se a proposta não separa,')
    print('  a marcenaria leva a culpa do orçamento inteiro.')

    print(f'\n{"═"*W}')
    print('⛔ METADE DA CHAPA DESTE ORÇAMENTO É SOBRA')
    print(f'{"═"*W}')
    liq = sum(area_mat[m]*(PRECO[m]/(CH_M2*APROV)) for m in area_mat)
    print(f'  Pagamos {sum(chapas.values()):.0f} chapas, R$ {br(sum(custo_ch.values()))}, para usar o')
    print(f'  equivalente a R$ {br(liq)}. A sobra é R$ {br(COR["sobra"])} — '
          f'{COR["sobra"]/sum(custo_ch.values())*100:.0f}% da chapa,')
    print(f'  {COR["sobra"]/CD*100:.0f}% do custo direto, R$ {br(COR["sobra"]/(BASE-MC_ALVO))} de preço.')
    print('  Não é erro: num banheiro de 3,43 m² a chapa inteira não cabe no')
    print('  móvel. O pior é o 15 mm branco: 4,2 m² obrigam a comprar duas')
    print('  chapas de 4,07 e a segunda entra quase inteira para sobrar.')
    print('  ⭐ SE VIER O RESTO DO APARTAMENTO JUNTO, a sobra se dilui nos')
    print('    outros ambientes e este banheiro fica mais barato. É [31]')
    print('    APTO ORLANDO E IVONE, prancha 31_.2 e 31_.6 — há mais')
    print('    pranchas nesse projeto. Vale perguntar à arquiteta o que mais')
    print('    tem de marcenaria antes de fechar só o banheiro.')

    print(f'\n{"═"*W}')
    print('⭐ INTERNO BRANCO E EXTERNO AMADEIRADO — E POR QUE DEU CERTO')
    print(f'{"═"*W}')
    print('  [Jonathan 13/10] Caixaria em MDF Ultra branco; portas, frentes')
    print('  de gaveta, as três peças fixas da espelheira, a lateral direita')
    print('  dos dois móveis e a base da espelheira em amadeirado fosco.')
    print(f'\n  {"":<36}{"como pedido":>14}{"tudo amadeirado":>18}')
    print('  ' + '─'*68)
    for k in AMBS:
        print(f'  {k:<36}{br(PV[k]):>14}{br(TUDOCOR["PV"][k]):>18}')
    print(f'  {"INVESTIMENTO":<36}{br(TOT):>14}{br(TUDOCOR["TOT"]):>18}')
    print(f'  {"chapa":<36}{br(sum(custo_ch.values())):>14}'
          f'{br(sum(TUDOCOR["custo_ch"].values())):>18}')
    print(f'  {"chapas compradas":<36}{sum(chapas.values()):>14.0f}'
          f'{sum(TUDOCOR["chapas"].values()):>18.0f}')
    print(f'\n  Economia de R$ {br(TUDOCOR["TOT"]-TOT)} '
          f'({(1-TOT/TUDOCOR["TOT"])*100:.0f}%) sem tirar nada do que se vê.')
    print('\n  ⭐ E deu certo por um motivo que não é óbvio: TODO O APARENTE')
    print('    FOI PARA 18 mm. Numa obra deste tamanho, misturar duas cores')
    print('    normalmente ENCARECE — cada cor obriga a comprar o mínimo de')
    print('    uma chapa em cada espessura, e sobra quase tudo. Concentrando')
    print(f'    o amadeirado numa espessura só, ele cabe em UMA chapa '
          f'({area_mat[("ultra",18)]:.2f}'.replace('.', ',') + ' m²')
    print('    de 4,07 aproveitáveis) e as outras três saem brancas, 35%')
    print('    mais baratas. Mesmas 4 chapas de antes, R$ '
          f'{br(sum(TUDOCOR["custo_ch"].values())-sum(custo_ch.values()))} a menos.')
    print('    ⛔ Se alguma peça aparente voltar para 15 mm, entra uma QUINTA')
    print('      chapa e a economia encolhe. Vale a pena segurar o 18.')

    print(f'\n{"═"*W}')
    print('★ EM ABERTO')
    print(f'{"═"*W}')
    print('  · ⛔ A COR. A prancha diz "MDF A DEFINIR" embaixo e "MDF BRANCO"')
    print('    em cima; o render mostra os dois amadeirados. Fechado como o')
    print('    Jonathan mandou em 13/10: interno branco, externo amadeirado')
    print('    fosco. ⚠ Falta o NOME do padrão — a arquiteta não especificou')
    print('    decor nenhum, e o preço de chapa muda de fornecedor para')
    print('    fornecedor dentro do amadeirado.')
    print('  · ⚠ AMADEIRADO EM CHAPA ULTRA. A linha resistente à umidade tem')
    print('    MENOS padrões amadeirados que a linha comum. Se o decor')
    print('    escolhido não existir em Ultra, ou se troca o padrão, ou a')
    print('    peça aparente sai em chapa comum — e aí ela é a que menos')
    print('    sofre, porque o que molha é a caixaria, que fica em Ultra.')
    print('  · ⛔ RESISTÊNCIA À UMIDADE. A arquiteta não pediu chapa Ultra.')
    print('    Nós colocamos. ★ +30% estimado sobre a cor — se o cliente')
    print('    quiser MDF comum, sai mais barato e sai sem a nossa garantia')
    print('    de 10 anos na parte que molha.')
    print('  · ⭐ RT DE 10% INCLUÍDO [Jonathan 13/10], para Ana Maria Castro.')
    print(f'    São R$ {br(TOT*enc["RT"])} dentro do preço. ⚠ Falta combinar com ela o')
    print('    que o RT cobre: acompanhamento de obra, conferência de medida')
    print('    e aprovação de amostra entram? E quando é pago — na assinatura')
    print('    ou na entrega? A parceria de RT da casa tem essa página; vale')
    print('    mandar antes de a proposta sair.')
    print('  · PUXADOR ZEN PHENIX 20 cm cromado — especificado por nome na')
    print('    prancha. ★ Entrou a R$ 55 a unidade, estimado. Na Raquel o')
    print('    Jonathan mandou TIRAR puxador e dobradiça; aqui mantive,')
    print('    porque a prancha especifica o modelo.')
    print('  · O interior do armário inferior não está desenhado. Adotei uma')
    print('    prateleira recortada no vão das portas. Se vier divisória,')
    print('    cesto ou gaveta interna, é acréscimo.')
    print('  · "PREVER INSTALAÇÃO DO DRIVE NA PARTE FIXA DA MARCENARIA":')
    print('    fazemos o berço e a passagem. A fonte, a arandela e a ligação')
    print('    são da elétrica.')
    print('  · O SÓCULO é alvenaria da obra (0,41 m² de pedra na legenda de')
    print('    piso). ⚠ Ele tem de estar pronto, nivelado e revestido antes')
    print('    da montagem. Se não estiver, ou o móvel espera ou vai em pé')
    print('    regulável — e aí muda o desenho.')
    print('  · A elevação cota 15 de testeira sob a bancada e a nota da')
    print('    planta diz TESTEIRA = 20. ⚠ Divergência da prancha. Muda o')
    print('    recuo da frente do armário; a conferir com a arquiteta.')
    print('  · Revisão 00, carimbada "NÃO PLOTAR, ESTUDO ENVIADO PARA')
    print('    ANÁLISE". Medida de obra por nossa conta antes de produzir.')
