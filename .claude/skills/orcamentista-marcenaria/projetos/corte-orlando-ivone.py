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

⛔ [Jonathan 13/10] O ARMÁRIO NÃO SUSTENTA A BANCADA. A pedra tem apoio e
   fixação próprios, de obra; o móvel entra por baixo dela.

⛔⛔ O QUE NÃO É NOSSO — e a proposta tem de dizer, porque num banheiro
   deste tamanho a marcenaria é a MENOR parte do que o cliente vê:
   · MARMORARIA: bancada e rodabanca em mármore branco (H=90, rodabanca 35,
     testeira 20), o APOIO E A FIXAÇÃO da bancada, acabamento do sóculo e o
     NICHO em mármore de toda a parede do box, com acabamento em 45°
   · SÓCULO em alvenaria (obra), que recebe a marcenaria
   · BOX de correr de 3 folhas 134×215, vidro temperado e perfis (vidraceiro)
   · LOUÇAS E METAIS Deca (VS.1, CB.1, TR.1, DH.1, BA.1/2, C.1, TO.1/2,
     PA.1, RA.1/2, RG) e o chuveiro CH.1, existente, a ser mantido
   · ARANDELAS, driver/fonte, luminárias, tomadas, forro e pintura
   · PORCELANATO 90 × 90 de piso e parede e as soleiras S1 em mármore

══ AS DUAS VERSÕES ═══════════════════════════════════════════════════════
⭐ [Jonathan 13/10] "interno branco e externo em amadeirado fosco" ·
   "traz a MC para 35% e inclui a RT"                     → PREMIUM
⭐ [Jonathan 13/10] "sem MDF Ultra, esquadria de alumínio com perfil comum,
   ferragens Bigfer, corrediças telescópicas sem amortecimento, 2 anos de
   garantia, MC de 32%"                                   → ESSENCIAL

⛔ As duas são o MESMO desenho e a MESMA mão de obra. O que muda é do que
   o móvel é feito — e a garantia segue o que ele é feito, não o contrário.
"""
import importlib.util, pathlib, sys
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('motor_mc', P/'motor_mc.py')
M = importlib.util.module_from_spec(spec); sys.modules['motor_mc'] = M
spec.loader.exec_module(M)

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
br1 = lambda v: f'{v:,.1f}'.replace(',','X').replace('.',',').replace('X','.')
vg  = lambda v: f'{v:.2f}'.replace('.', ',')

CH_M2, APROV = 2.75*1.85, 0.80
# ★ A chapa Ultra (resistente à umidade) não está na base da casa;
#   estimada em +30% sobre a equivalente comum, como na Raquel Franco.
PRECO = {('cor',6):300.0, ('cor',15):500.0, ('cor',18):600.0,
         ('br',6):190.0,  ('br',15):260.0,  ('br',18):330.0,
         ('ultra',6):390.0, ('ultra',15):650.0, ('ultra',18):780.0,
         ('ultrabr',6):247.0, ('ultrabr',15):338.0, ('ultrabr',18):429.0}
NOME_CH = {'ultra':'Ultra amadeirado', 'ultrabr':'Ultra branco',
           'cor':'MDF amadeirado', 'br':'MDF Branco TX'}
FITA_COR = 3.0 + 2.5           # fita amadeirada + filetagem na coladeira
FITA_BR  = 2.0 + 2.5           # fita branca + filetagem
RT_ON    = True                # ⭐ [Jonathan 13/10] "e inclui a RT"
BASE     = M.base(parcelas=0, rt=RT_ON, vendedor=False)

# ⭐ [Jonathan 09/10] espelho a R$ 600,00 o m², fornecimento nosso.
ESPELHO_M2  = 600.0
ARANDELA_PC = 90.0    # ★ usinagem da passagem e berço do driver, por peça fixa

# ══ AS DUAS VERSÕES ══════════════════════════════════════════════════════
# ⚠⚠ PREMIUM · a corrediça OCULTA Hettich está pelo preço da telescópica da
#   casa, por instrução do Jonathan de não mexer no valor. Ver EM ABERTO.
# ★ ESSENCIAL · ferragem Bigfer e perfil de alumínio comum, preços
#   estimados — nenhum dos dois está na base da casa.
VERSAO = {
 'premium': dict(
    nome='Premium', mc=0.35, garantia='10 anos',
    chapa={'ext':'ultra', 'int':'ultrabr'},
    fer={'dobr':35.0, 'corr':85.0, 'puxador':55.0},
    fer_nome={'dobr':'dobradiça com amortecedor',
              'corr':'corrediça OCULTA Hettich',
              'puxador':'puxador Zen Phenix cromado'},
    perfil=75.0, perfil_nome='perfil de alumínio, linha de esquadria'),
 'essencial': dict(
    nome='Essencial', mc=0.32, garantia='2 anos',
    chapa={'ext':'cor', 'int':'br'},
    fer={'dobr':15.0, 'corr':45.0, 'puxador':30.0},
    fer_nome={'dobr':'dobradiça Bigfer',
              'corr':'corrediça telescópica Bigfer, sem amortecimento',
              'puxador':'puxador cromado Bigfer'},
    perfil=45.0, perfil_nome='perfil de alumínio comum'),
}

PCS, FER, TER_FIX = {}, {}, {}
def amb(k):
    PCS.setdefault(k, []); TER_FIX.setdefault(k, 0.0)
    FER.setdefault(k, dict.fromkeys(('dobr','corr','puxador'), 0))
def a(k, mat, esp, desc, c, l, q=1, fc=2):
    """mat = 'ext' (aparente, amadeirado) ou 'int' (caixaria, branco)."""
    amb(k); PCS[k].append((mat, esp, desc, c, l, q, fc))
def f(k, **kw):
    amb(k)
    for key, v in kw.items(): FER[k][key] += v
def ter(k, v): amb(k); TER_FIX[k] += v

# ⭐ [Jonathan 13/10] "considere interno branco e externo em amadeirado
#   fosco". A caixaria vai em branco e tudo o que se vê — portas, frentes
#   de gaveta, as três peças fixas da espelheira, a lateral direita dos
#   dois móveis (que fica solta, sem parede) e a base da espelheira (que
#   se enxerga por baixo) — vai em AMADEIRADO FOSCO.
#   ⭐ E todo o aparente foi para 18 mm de propósito: assim o amadeirado
#     cabe em UMA chapa só. Ver o quadro no fim.

# ══ 1 · ARMÁRIO INFERIOR ══════════════════════════════════════════════════
# 119 de frente × 63 de altura × 46 de profundidade, sobre sóculo de 15.
# Frente: 71,5 de portas de giro (2 folhas) + 47,5 de gavetas (4).
# Gavetas de cima para baixo: 10 · 17 · 17 · 17. A cuba cai sobre o vão
# das portas — por isso as gavetas não têm conflito com o sifão.
K = 'Armário inferior'
a(K,'ext',18,'Lateral aparente',        63,  46, 1)
a(K,'int',15,'Lateral de parede',       63,  46, 1)
a(K,'int',15,'Divisória vertical',      63,  46, 1)
a(K,'int',15,'Base',                   115,  46, 1)
a(K,'int',15,'Travessa superior',      115,  10, 2)
a(K,'int', 6,'Fundo',                  119,  63, 1, 1)
a(K,'ext',18,'Porta de giro',           61,  36, 2)
a(K,'ext',18,'Frente de gaveta',        48,  10, 1)
a(K,'ext',18,'Frente de gaveta',        48,  17, 3)
a(K,'int',15,'Gaveta · lateral',        42,  12, 8, 1)
a(K,'int',15,'Gaveta · frente e fundo', 44,  12, 8, 1)
a(K,'int',15,'Gaveta · fundo',          44,  42, 4, 1)
a(K,'int',15,'Prateleira interna',      68,  42, 1)     # ★ ver EM ABERTO
f(K, dobr=4, corr=4, puxador=6)

# ══ 2 · ARMÁRIO SUPERIOR · ESPELHEIRA ═════════════════════════════════════
# 195 × 90 × 15, 30,5 abaixo do forro e 35 acima da bancada.
# Frente: 10 + 82,5 + 10 + 82,5 + 10. As três peças de 10 são FIXAS e é
# nelas que vão as arandelas e, por dentro, o driver. Cada vão de 82,5
# fecha com DUAS folhas de espelho em perfil de alumínio, com trespasse
# de 1 cm sobre a peça fixa fazendo as vezes de puxador.
# Por dentro, duas prateleiras por vão (23 · 30 · 30 na elevação 04).
K = 'Armário superior'
ESP_L, ESP_A, ESP_N = 0.4225, 0.90, 4
a(K,'ext',18,'Lateral aparente',        90,  15, 1)
a(K,'int',15,'Lateral de parede',       90,  15, 1)
a(K,'int',15,'Divisória vertical',      90,  15, 1)
a(K,'ext',18,'Base · vista por baixo', 191,  15, 1)
a(K,'int',15,'Tampo',                  191,  15, 1)
a(K,'int', 6,'Fundo',                  195,  90, 1, 1)
a(K,'int',15,'Prateleira',              95,  13, 4)
a(K,'ext',18,'Peça fixa frontal',       90,  10, 3)
f(K, dobr=8)
ter(K, ESP_N*ESP_L*ESP_A*ESPELHO_M2 + 3*ARANDELA_PC)   # espelho + preparo
ESPELHO_RS = ESP_N*ESP_L*ESP_A*ESPELHO_M2
PERFIL_ML  = ESP_N*2*(ESP_L+ESP_A)                     # metros de perfil

AMBS = list(PCS)

# ══════════════════════════════════════════════════════════════════════════
def calcula(v):
    """v = uma entrada de VERSAO. Devolve custo e preço por ambiente."""
    mapa = v['chapa']
    ter_ = {k: TER_FIX[k] for k in AMBS}
    ter_['Armário superior'] += PERFIL_ML*v['perfil']
    area_mat, ch, fita, area_k = {}, {}, {}, {}
    for k in AMBS:
        ch[k] = fita[k] = 0.0
        for mat, esp, _, c, l, q, fc in PCS[k]:
            m = (mapa[mat], esp)
            area_mat[m] = area_mat.get(m, 0.0) + c*l*q/1e4
            fm = FITA_BR if m[0].endswith('br') else FITA_COR
            fita[k] += 2*(c+l)*q/100*(0.75 if fc == 2 else 0.4)*fm
    chapas   = {m: -(-x/(CH_M2*APROV)//1) for m, x in area_mat.items()}
    custo_ch = {m: chapas[m]*PRECO[m] for m in chapas}
    # ⛔ cada peça paga a própria taxa; a sobra de corte rateia pela área
    #   total (lição da Alice — ratear chapa inteira inverte cenário).
    taxa = {m: PRECO[m]/(CH_M2*APROV) for m in area_mat}
    for k in AMBS:
        area_k[k] = sum(c*l*q/1e4 for _,_,_,c,l,q,_ in PCS[k])
        ch[k] = sum(c*l*q/1e4*taxa[(mapa[mat], esp)]
                    for mat, esp, _, c, l, q, _ in PCS[k])
    sobra = sum(custo_ch.values()) - sum(area_mat[m]*taxa[m] for m in area_mat)
    at = sum(area_k.values())
    for k in AMBS: ch[k] += sobra*area_k[k]/at
    fer_c = {k: sum(FER[k][x]*v['fer'][x] for x in v['fer']) for k in AMBS}
    cons  = {k: (ch[k]+fita[k])*0.06 for k in AMBS}
    CDI = {k: (ch[k] + fita[k] + cons[k] + fer_c[k] + ter_[k])*(1 + M.EMBALAGEM)
           for k in AMBS}
    PV  = {k: round(CDI[k]/(BASE - v['mc'])/10)*10 for k in AMBS}
    emb = {k: CDI[k]/(1 + M.EMBALAGEM)*M.EMBALAGEM for k in AMBS}
    return dict(v=v, ch=ch, fita=fita, cons=cons, fer=fer_c, ter=ter_, emb=emb,
                CDI=CDI, PV=PV, chapas=chapas, custo_ch=custo_ch, area=area_mat,
                sobra=sobra, CD=sum(CDI.values()), TOT=sum(PV.values()))

PREMIUM   = calcula(VERSAO['premium'])
ESSENCIAL = calcula(VERSAO['essencial'])

# compatibilidade com o build da versão 1
ch, fita, fer_custo = PREMIUM['ch'], PREMIUM['fita'], PREMIUM['fer']
CDI, PV, TOT, CD = PREMIUM['CDI'], PREMIUM['PV'], PREMIUM['TOT'], PREMIUM['CD']
area_mat, chapas, custo_ch = PREMIUM['area'], PREMIUM['chapas'], PREMIUM['custo_ch']
MC_ALVO = VERSAO['premium']['mc']

# ── para comparar: TUDO amadeirado, interno inclusive ───────────────────
def _tudo_ext(v):
    g = dict(v); g['chapa'] = {'ext': v['chapa']['ext'], 'int': v['chapa']['ext']}
    return calcula(g)
TUDOCOR = _tudo_ext(VERSAO['premium'])


def quadro(R, W=90):
    """Composição de custo e de preço de uma versão."""
    v = R['v']
    print(f'\n{"═"*W}')
    print(f'VERSÃO {v["nome"].upper()}  ·  MC {v["mc"]*100:.0f}%  ·  '
          f'garantia de {v["garantia"]}  ·  R$ {br(R["TOT"])}')
    print(f'{"═"*W}')
    print(f'{"CHAPA":<24}{"área líq.":>12}{"chapas":>9}{"R$/chapa":>11}{"custo":>11}')
    print('─'*W)
    for m in sorted(R['area'], key=str):
        print(f'{(NOME_CH[m[0]] + "  " + str(m[1]) + " mm"):<24}'
              f'{br1(R["area"][m]):>10} m²{R["chapas"][m]:>9.0f}'
              f'{br(PRECO[m]):>11}{br(R["custo_ch"][m]):>11}')
    print('─'*W)
    print(f'{"TOTAL":<24}{br1(sum(R["area"].values())):>10} m²'
          f'{sum(R["chapas"].values()):>9.0f}{"":>11}'
          f'{br(sum(R["custo_ch"].values())):>11}')

    print(f'\n{"":<38}{"inferior":>11}{"superior":>11}{"total":>11}{"%":>8}')
    print('─'*W)
    _am = int(sum(x for m, x in R['chapas'].items() if m[0] == v['chapa']['ext']))
    _bo = int(sum(R['chapas'].values())) - _am
    LIN = [(f'chapa  ·  {_am} amadeirada + {_bo} brancas', R['ch']),
           ('fita de borda e filetagem',          R['fita']),
           ('consumíveis  ·  6% de chapa e fita', R['cons']),
           ('ferragem',                           R['fer']),
           ('terceiros  ·  espelho e perfil',     R['ter']),
           ('embalagem  ·  2% do custo',          R['emb'])]
    for nome, d in LIN:
        t = sum(d.values())
        print(f'{nome:<38}{br(d[AMBS[0]]):>11}{br(d[AMBS[1]]):>11}'
              f'{br(t):>11}{t/R["CD"]*100:>7.1f}%')
    print('─'*W)
    print(f'{"CUSTO DIRETO":<38}{br(R["CDI"][AMBS[0]]):>11}'
          f'{br(R["CDI"][AMBS[1]]):>11}{br(R["CD"]):>11}{100.0:>7.1f}%')
    print('\n  a ferragem, aberta:')
    for x in v['fer']:
        n = sum(FER[k][x] for k in AMBS)
        if n: print(f'    {v["fer_nome"][x]:<44}{n:>3} × R$ {br(v["fer"][x]):>5}'
                    f'  =  R$ {br(n*v["fer"][x])}')
    print('  os terceiros, abertos:')
    print(f'    espelho prata, {ESP_N} folhas a R$ {br(ESPELHO_M2)}/m²'
          f'{"":<13}=  R$ {br(ESPELHO_RS)}')
    print(f'    {v["perfil_nome"]:<44}★ R$ {br(v["perfil"])}/m  =  '
          f'R$ {br(PERFIL_ML*v["perfil"])}')
    print(f'    {"preparo das 3 peças fixas, berço e passagem":<44}'
          f'{"":>13}=  R$ {br(3*ARANDELA_PC)}')

    enc = M.encargos(parcelas=0, rt=RT_ON, vendedor=False)
    print(f'\n{"":<38}{"R$":>12}{"% do preço":>14}')
    print('─'*W)
    print(f'{"custo direto":<38}{br(R["CD"]):>12}{R["CD"]/R["TOT"]*100:>13.2f}%')
    for nome, x in enc.items():
        if x: print(f'{nome:<38}{br(R["TOT"]*x):>12}{x*100:>13.2f}%')
    print('─'*W)
    mc_r = R['TOT'] - R['CD'] - sum(R['TOT']*x for x in enc.values())
    print(f'{"MARGEM DE CONTRIBUIÇÃO":<38}{br(mc_r):>12}{mc_r/R["TOT"]*100:>13.2f}%')
    print(f'{"PREÇO":<38}{br(R["TOT"]):>12}{100.0:>13.2f}%')
    return mc_r


if __name__ == '__main__':
    W = 90
    print('═'*W)
    print('APTO ORLANDO E IVONE — banho suíte master  ·  [31] rev. 00')
    print('arquiteta Ana Maria Castro · CAU A94939-6 · 12/10/2026')
    print('═'*W)

    mcP = quadro(PREMIUM, W)
    mcE = quadro(ESSENCIAL, W)

    print(f'\n{"═"*W}')
    print('⭐ AS DUAS VERSÕES, LADO A LADO')
    print(f'{"═"*W}')
    print(f'  {"":<34}{"Premium":>13}{"Essencial":>13}{"diferença":>13}')
    print('  ' + '─'*72)
    for k in AMBS:
        print(f'  {k:<34}{br(PREMIUM["PV"][k]):>13}{br(ESSENCIAL["PV"][k]):>13}'
              f'{br(ESSENCIAL["PV"][k]-PREMIUM["PV"][k]):>13}')
    print(f'  {"INVESTIMENTO":<34}{br(PREMIUM["TOT"]):>13}{br(ESSENCIAL["TOT"]):>13}'
          f'{br(ESSENCIAL["TOT"]-PREMIUM["TOT"]):>13}')
    print(f'  {"custo direto":<34}{br(PREMIUM["CD"]):>13}{br(ESSENCIAL["CD"]):>13}'
          f'{br(ESSENCIAL["CD"]-PREMIUM["CD"]):>13}')
    print(f'  {"margem de contribuição":<34}{br(mcP):>13}{br(mcE):>13}'
          f'{br(mcE-mcP):>13}')
    print(f'  {"MC":<34}{VERSAO["premium"]["mc"]*100:>12.0f}%'
          f'{VERSAO["essencial"]["mc"]*100:>12.0f}%{"":>13}')
    print(f'  {"garantia":<34}{VERSAO["premium"]["garantia"]:>13}'
          f'{VERSAO["essencial"]["garantia"]:>13}')
    print(f'\n  A Essencial é {(1-ESSENCIAL["TOT"]/PREMIUM["TOT"])*100:.0f}% '
          f'mais barata — R$ {br(PREMIUM["TOT"]-ESSENCIAL["TOT"])} a menos.')
    _dt = PREMIUM['TOT'] - ESSENCIAL['TOT']
    _dc = PREMIUM['CD'] - ESSENCIAL['CD']
    _dm = mcP - mcE
    _de = _dt - _dc - _dm          # encargos que caem junto com o preço
    print(f'  ⛔ De onde vêm os R$ {br(_dt)} de diferença:')
    print(f'    R$ {br(_dc)} ({_dc/_dt*100:.0f}%) saem do CUSTO — chapa comum, ferragem')
    print('             Bigfer, perfil comum, corrediça sem amortecimento;')
    print(f'    R$ {br(_dm)} ({_dm/_dt*100:.0f}%) saem da NOSSA MARGEM;')
    print(f'    R$ {br(_de)} ({_de/_dt*100:.0f}%) são nota fiscal, RT e comissões, que caem')
    print('             junto porque correm sobre o preço.')
    print('    ⛔ Só um terço do desconto é material. O resto é margem e')
    print('      imposto. O cliente não leva o mesmo móvel mais barato — é')
    print('      outro móvel — e ainda assim a casa ganha R$ '
          f'{br(_dm)} a menos')
    print('      pela MESMA mão de obra: mesmo desenho, mesmo corte, mesma')
    print('      montagem, mesmas duas idas à obra.')
    _p35 = sum(round(ESSENCIAL['CDI'][k]/(BASE-M.MC_PISO)/10)*10 for k in AMBS)
    print(f'\n  ⛔⛔ 32% ESTÁ ABAIXO DO PISO DA CASA (MC_PISO = '
          f'{M.MC_PISO*100:.0f}%).')
    print(f'    No piso, a mesma Essencial sairia a R$ {br(_p35)} — '
          f'abrir 3 pontos')
    print(f'    custou R$ {br(_p35-ESSENCIAL["TOT"])} de preço e '
          f'R$ {br(_p35*(BASE-ESSENCIAL["CD"]/_p35)-mcE)} de margem. A MC ainda tem de')
    print('    pagar o custo fixo da fábrica: aceitável se este banheiro for')
    print('    a porta de entrada do resto do apartamento, caro se for um')
    print('    serviço solto.')
    print('    ⚠ E a garantia de 2 anos é o que torna a Essencial honesta:')
    print('      sem Ultra, sem amortecimento e com ferragem de entrada,')
    print('      10 anos seria promessa que o móvel não sustenta.')

    print(f'\n{"═"*W}')
    print('⭐ A ESPELHEIRA É A MAIOR PARTE DAS DUAS')
    print(f'{"═"*W}')
    for R in (PREMIUM, ESSENCIAL):
        ks = 'Armário superior'
        print(f'  {R["v"]["nome"]:<11} R$ {br(R["PV"][ks])} de R$ {br(R["TOT"])}'
              f' — {R["PV"][ks]/R["TOT"]*100:.0f}%')
    print('  Espelho, perfil de alumínio e as dobradiças que carregam folha')
    print('  de espelho não são madeira — e é por isso que ela não barateia')
    print('  tanto quanto o armário de baixo.')

    print(f'\n{"═"*W}')
    print('⛔ O QUE A PROPOSTA PRECISA DIZER QUE NÃO É NOSSO')
    print(f'{"═"*W}')
    print('  bancada, APOIO E FIXAÇÃO da bancada, rodabanca, testeira, sóculo')
    print('  e o nicho do box — marmoraria e obra. Box de correr — vidraceiro.')
    print('  Louças e metais Deca, arandelas e driver, tomadas, forro, pintura')
    print('  e porcelanato — obra. Num banheiro de 3,43 m² o cliente olha o')
    print('  conjunto e compara com o preço da marcenaria. Se a proposta não')
    print('  separa, a marcenaria leva a culpa do orçamento inteiro.')

    print(f'\n{"═"*W}')
    print('⛔ METADE DA CHAPA DESTE ORÇAMENTO É SOBRA')
    print(f'{"═"*W}')
    for R in (PREMIUM, ESSENCIAL):
        liq = sum(R['area'][m]*(PRECO[m]/(CH_M2*APROV)) for m in R['area'])
        print(f'  {R["v"]["nome"]:<11}{sum(R["chapas"].values()):.0f} chapas, '
              f'R$ {br(sum(R["custo_ch"].values()))} — usa R$ {br(liq)}, '
              f'sobra R$ {br(R["sobra"])} '
              f'({R["sobra"]/sum(R["custo_ch"].values())*100:.0f}%)')
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
    print('  [Jonathan 13/10] Caixaria em branco; portas, frentes de gaveta,')
    print('  as três peças fixas da espelheira, a lateral direita dos dois')
    print('  móveis e a base da espelheira em amadeirado fosco.')
    print(f'\n  {"":<36}{"Premium":>14}{"tudo amadeirado":>18}')
    print('  ' + '─'*68)
    for k in AMBS:
        print(f'  {k:<36}{br(PREMIUM["PV"][k]):>14}{br(TUDOCOR["PV"][k]):>18}')
    print(f'  {"INVESTIMENTO":<36}{br(PREMIUM["TOT"]):>14}{br(TUDOCOR["TOT"]):>18}')
    print(f'  {"chapas compradas":<36}{sum(PREMIUM["chapas"].values()):>14.0f}'
          f'{sum(TUDOCOR["chapas"].values()):>18.0f}')
    print(f'\n  Economia de R$ {br(TUDOCOR["TOT"]-PREMIUM["TOT"])} '
          f'({(1-PREMIUM["TOT"]/TUDOCOR["TOT"])*100:.0f}%) sem tirar nada do que se vê.')
    print('\n  ⭐ E deu certo por um motivo que não é óbvio: TODO O APARENTE')
    print('    FOI PARA 18 mm. Numa obra deste tamanho, misturar duas cores')
    print('    normalmente ENCARECE — cada cor obriga a comprar o mínimo de')
    print('    uma chapa em cada espessura, e sobra quase tudo. Concentrando')
    print(f'    o amadeirado numa espessura só, ele cabe em UMA chapa '
          f'({vg(PREMIUM["area"][("ultra",18)])} m²')
    print('    de 4,07 aproveitáveis) e as outras três saem brancas.')
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
    print('  · ⛔ RESISTÊNCIA À UMIDADE. A arquiteta não pediu chapa Ultra;')
    print('    nós pusemos na Premium. ★ +30% estimado sobre a comum. A')
    print('    ESSENCIAL sai em MDF comum, por instrução do Jonathan — e é')
    print('    exatamente por isso que a garantia dela é de 2 anos.')
    print('  · ⚠ AMADEIRADO EM CHAPA ULTRA. A linha resistente à umidade tem')
    print('    MENOS padrões amadeirados que a comum. Se o decor escolhido')
    print('    não existir em Ultra, a peça aparente da Premium sai em chapa')
    print('    comum — e é a que menos sofre, porque o que molha é a caixaria.')
    print('  · ⭐ RT DE 10% INCLUÍDO NAS DUAS [Jonathan 13/10], para Ana Maria')
    print(f'    Castro. São R$ {br(PREMIUM["TOT"]*M.encargos(0, RT_ON, False)["RT"])} '
          f'na Premium e R$ {br(ESSENCIAL["TOT"]*M.encargos(0, RT_ON, False)["RT"])} '
          f'na Essencial. ⚠ Falta combinar')
    print('    com ela o que o RT cobre e quando é pago.')
    print('  · ⚠⚠ PREMIUM · CORREDIÇA OCULTA HETTICH pelo preço da telescópica.')
    print('    [Jonathan 13/10] mandou não mexer no valor. A linha está em')
    print(f'    R$ {br(4*VERSAO["premium"]["fer"]["corr"])}; oculta Hettich com amortecimento custa de duas a')
    print('    três vezes isso. Se for 2,5×, são cerca de R$ 510 de custo a')
    print(f'    mais, R$ {br(510/(BASE-VERSAO["premium"]["mc"]))} de preço que não estão aqui — e saem da')
    print('    margem. Fica registrado: a decisão é do Jonathan, a conta é esta.')
    print('  · ★ ESSENCIAL · ferragem BIGFER e PERFIL DE ALUMÍNIO COMUM estão')
    print('    ESTIMADOS — nenhum dos dois está na base da casa. Dobradiça a')
    _fe = VERSAO['essencial']
    print(f'    R$ {br(_fe["fer"]["dobr"])}, corrediça a R$ {br(_fe["fer"]["corr"])}, '
          f'puxador a R$ {br(_fe["fer"]["puxador"])} e perfil a '
          f'R$ {br(_fe["perfil"])}/m.')
    print('    ⚠ O puxador especificado é o ZEN PHENIX — na Essencial ele sai')
    print('      e entra um cromado de linha. Isso muda o que o cliente vê e')
    print('      a arquiteta precisa saber.')
    print('  · O interior do armário inferior não está desenhado. Adotei uma')
    print('    prateleira recortada no vão das portas. Se vier divisória,')
    print('    cesto ou gaveta interna, é acréscimo.')
    print('  · "PREVER INSTALAÇÃO DO DRIVE NA PARTE FIXA DA MARCENARIA":')
    print('    fazemos o berço e a passagem. A fonte, a arandela e a ligação')
    print('    são da elétrica.')
    print('  · O SÓCULO é alvenaria da obra. ⚠ Tem de estar pronto, nivelado')
    print('    e revestido antes da montagem.')
    print('  · A elevação cota 15 de testeira sob a bancada e a nota da')
    print('    planta diz TESTEIRA = 20. ⚠ Divergência da prancha.')
    print('  · Revisão 00, carimbada "NÃO PLOTAR, ESTUDO ENVIADO PARA')
    print('    ANÁLISE". Medida de obra por nossa conta antes de produzir.')
