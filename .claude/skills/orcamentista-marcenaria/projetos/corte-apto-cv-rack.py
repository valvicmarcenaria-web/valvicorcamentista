# -*- coding: utf-8 -*-
"""ANA CAROLINA — APTO CV · O RACK DA SALA, ORÇADO À PARTE  [22/10/2026]

Prancha **005_DET_Sala_Apto_CV_R00**, 3 folhas A3, **ESTÚDIO GRÁZA —
arquiteta BRUNA REZENDE**, cliente Ana Carolina Valente, Santo Antônio/BH,
12/02/2026, R00. Folha 13/3 = Elevação A, que é onde o rack está.

⛔⛔ **ESTE MÓVEL NÃO ESTÁ NO ESCOPO JÁ FECHADO.** A proposta de 02/07
   vendeu o item "Painel de TV — **liso** em madeirado fosco, com passagem
   de fiação", R$ 8.900 de tabela, **SEM RACK**; no rateio de 30/09 ele foi
   fundido em `Sala - painéis` (R$ 31.890). Aqui é item NOVO. ⭐ Pela regra
   de 21/10 — *"alterar valores apenas se expressamente solicitado"* — nada
   do que já foi fechado é tocado por este arquivo.

O QUE A ELEVAÇÃO A DIZ DO RACK (cotas lidas da prancha, escala 1:25)
  · largura na prancha ...... **307** = 51+51+51+51 · 51(nicho) · 49, com
                               juntas de 1 entre os módulos
  · altura do corpo ......... **32** — a cadeia da cota é 1 + 1 + **28** +
                               1 + 1, ou seja tampo, porta de 28 e base
  · suspenso do piso ........ **20** — o móvel não encosta no chão
  · face superior a ......... **52** do piso (20 + 32)
  · profundidade ............ **35** ★ escalado da planta (y 249,3 → 289,0
                               pt, 39,7 pt ÷ 1,1339 = 35,0 cm). ⚠ A planta
                               NÃO traz cota própria de profundidade.
  · frentes ................. **PORTA BASC.** ×5 e **NICHO** ×1, aberto,
                               entre a quarta e a quinta porta
  · acabamento .............. marcador **01** no quadro = **MDF MADEIRADO
                               À DEFINIR** (o `05`, MDF bege fosco, é o
                               armário da outra parede, não este móvel)

⭐⭐ [Jonathan 21/10] **"vamos orçar esse rack considerando o tamanho de
   2.30 / uma versão com as portas com acabamento em palha natural e outra
   sem."** → A largura sai de 307 para **230** e o móvel passa a ter
   **cinco módulos de 45,8: quatro portas basculantes e um nicho aberto**,
   o nicho no penúltimo módulo, como no desenho original.

⭐ O RENDER DA PRÓPRIA PRANCHA JÁ MOSTRA A PALHA. As duas imagens
  incorporadas na folha 13/3 (Elevação A e B) mostram as frentes do rack
  em **tela de palha dentro de moldura de madeira**. Ou seja: a versão com
  palha é o projeto; a sem palha é a alternativa.

LINHA: **Essencial**, a mesma do apartamento inteiro (proposta de 02/07) —
  ferragem oculta Hardt, **garantia de 5 anos**. ⛔ Não faria sentido criar
  uma garantia diferente dentro do mesmo apartamento.
"""
import importlib.util, pathlib, sys
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('motor_mc', P/'motor_mc.py')
M = importlib.util.module_from_spec(spec); sys.modules['motor_mc'] = M
spec.loader.exec_module(M)

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
vg  = lambda v, n=2: f'{v:.{n}f}'.replace('.', ',')

CH_M2   = 2.75*1.85                  # 5,0875 m² de chapa cheia
# ⚠ APROVEITAMENTO MENOR NO MADEIRADO. A casa trabalha com 0,80; no padrão
#   amadeirado todas as peças aparentes têm de sair com o VEIO no mesmo
#   sentido, e isso tira liberdade do nesting. Aqui vai 0,75.
APROV   = 0.75
MC_ALVO = 0.40                       # topo da faixa ideal da casa (35–40%)
RT_ON   = True                       # ⭐ projeto de arquiteta (Estúdio Gráza)
BASE    = M.base(parcelas=0, rt=RT_ON, vendedor=False)

# ── insumos ──────────────────────────────────────────────────────────────
# ⭐ "MDF MADEIRADO À DEFINIR" — a prancha não fecha o padrão. Orçado na
#   linha de COR da base da casa (R$ 600 a chapa de 18), que é onde caem os
#   amadeirados correntes (Carvalho e Freijó Guararapes, Itapuã, Gianduia).
#   ⚠ Se a arquiteta fechar num ESPECIAL (Freijó Puro Duratex, lâmina
#     natural), a chapa dobra para R$ 1.200 — o relatório mede esse salto.
MAD_18, MAD_6 = 600.0, 300.0
MAD_ESPECIAL  = 1200.0               # ★ o cenário caro, só para medir
FITA_M        = 3.0 + 2.5            # fita de cor + filetagem, por metro

# ⭐⭐ PALHA NATURAL — NÃO ESTÁ NA BASE DA CASA. A base só tem "palha
#   SINTÉTICA, R$ 600 a chapa", que é outro produto: chapa rígida com
#   desenho impresso. Palha natural é **tela de palhinha indiana**, vendida
#   em rolo, e o que custa nela NÃO é o rolo — é a mão.
PALHA_ROLO_M  = 350.0   # ★ rolo de 1,00 m de largura, por metro linear
PALHA_MIN_M   = 1.0     # ⛔ não se compra meio metro de rolo
# ⭐⭐ A CONSTRUÇÃO DA PORTA SAIU DO RENDER, NÃO DO MEU PALPITE. Ampliando
#   a imagem da própria prancha, a palha cobre QUASE TODA a face: sobra um
#   filete de madeirado de cerca de 1 cm correndo as quatro bordas. Não é
#   moldura larga com tela esticada no vão — é **rebaixo raso usinado na
#   face da porta, com a palha assentada dentro dele**, e o filete que
#   sobra funciona como moldura. A elevação confirma: cada "PORTA BASC."
#   está desenhada com linha dupla, que é exatamente esse filete.
#   ⛔ Eu havia orçado moldura de 3,5 cm com vão vazado. Era mais caro e
#     não era o que o projeto desenha.
FILETE        = 1.0     # ⭐ borda de madeirado que sobra à vista, em cm
PALHA_MO_PORTA= 110.0   # ★ rebaixo, assentamento, prensagem e aparo, por porta
PALHA_MO_BAIXA= 70.0    # ★ o mesmo serviço, na hipótese mais magra
ADESIVO       = 60.0    # ★ adesivo próprio para fibra natural, no conjunto

# ── ferragem · linha Essencial, a mesma do resto do apartamento ──────────
DOBR, BASCULA, TOQUE = 12.0, 60.0, 25.0
PASSA_CABO = 35.0
GARANTIA   = '5 anos'                # ferragem oculta Hardt, como na 02/07
# ⭐ O rack é SUSPENSO e vai pendurado no painel madeirado que já foi
#   vendido. Isso é estrutura, não marcenaria: barra contínua de metalon
#   40 × 20 nos 2,30 m mais duas travessas, chumbada na alvenaria por trás
#   do painel.
FIXA_M, FIXA_ACES = 85.0, 80.0
LED_M, LED_FONTE  = 65.0, 120.0      # ⚠ OPCIONAL — a prancha não pede LED

# ── geometria ────────────────────────────────────────────────────────────
L_TOT, H_CORPO, PROF = 230.0, 32.0, 35.0     # ⭐ 2,30 [Jonathan 21/10]
H_PORTA, SUSP        = 28.0, 20.0            # cotas da prancha
ESP, FOLGA           = 1.8, 0.3              # ⭐ 18 mm em TODO o corpo
N_MOD, N_PORTA       = 5, 4                  # 4 portas + 1 nicho

L_PORTA = (L_TOT - (N_MOD - 1)*FOLGA)/N_MOD  # 45,8 — frente de módulo
H_INT   = H_CORPO - 2*ESP                    # 28,4 — altura livre interna
L_VAO   = L_PORTA - 2*FILETE                 # campo de palha, na largura
H_VAO   = H_PORTA - 2*FILETE                 # campo de palha, na altura
L_NICHO = L_PORTA                            # o nicho é um módulo igual

# ⛔⛔ 18 mm EM TUDO NÃO É LUXO, É O CORTE MAIS BARATO. A casa estrutura em
#   15 mm; aqui, 15 mm obrigaria a comprar uma CHAPA INTEIRA de 15 só para
#   0,6 m² de laterais e divisórias — R$ 500 por 12% de aproveitamento.
#   Em 18 mm essas peças saem da sobra da chapa que o tampo já paga. O
#   móvel fica mais rígido e R$ 500 mais barato. O relatório prova.


def pecas(palha):
    """(desc, c, l, q, esp_mm, fita_m_total) — o corpo não muda com a palha."""
    p = [
     ('Tampo · borda aparente na frente e nas duas pontas', L_TOT, PROF, 1, 18,
      (L_TOT + 2*PROF)/100),
     ('Base · borda aparente na frente e nas duas pontas',  L_TOT, PROF, 1, 18,
      (L_TOT + 2*PROF)/100),
     ('Lateral',                        H_INT, PROF, 2, 18, 2*H_INT/100),
     ('Divisória entre módulos',        H_INT, PROF, 4, 18, 4*H_INT/100),
     ('Fundo',                          L_TOT, H_INT, 1,  6, 0.0),  # ou 18
    ]
    d = ('Porta basculante · rebaixo raso na face, palha assentada, '
         'filete de madeirado à vista' if palha
         else 'Porta basculante · folha lisa')
    p.append((d, L_PORTA, H_PORTA, N_PORTA, 18,
              N_PORTA*2*(L_PORTA + H_PORTA)/100))
    return p


def orcar(palha, chapa18=MAD_18, esp_corpo=18, mo=PALHA_MO_PORTA,
          fundo6=True):
    """Custo direto aberto. `esp_corpo` = 15 força o cenário da casa."""
    PCS = pecas(palha)
    if not fundo6:                   # ⭐ o fundo sai da sobra da chapa de 18
        PCS = [(d, c, l, q, (18 if d.startswith('Fundo') else e), f)
               for d, c, l, q, e, f in PCS]
    if esp_corpo == 15:              # laterais e divisórias em 15 mm
        PCS = [(d, c, l, q, (15 if d.startswith(('Lateral', 'Divisória'))
                             else e), f) for d, c, l, q, e, f in PCS]
    area = {}
    for _d, c, l, q, e, _f in PCS:
        area[e] = area.get(e, 0.0) + c*l*q/1e4
    PRECO_ESP = {18: chapa18, 15: chapa18*500/600, 6: MAD_6}
    chapas = {e: -(-a/(CH_M2*APROV)//1) for e, a in area.items()}
    ch_custo = sum(n*PRECO_ESP[e] for e, n in chapas.items())
    fita_m   = sum(f for *_x, f in PCS)
    fita     = fita_m*FITA_M

    fer = {'Dobradiça com amortecedor':  N_PORTA*2*DOBR,
           'Báscula · pistão a gás':     N_PORTA*BASCULA,
           'Fecho-toque':                N_PORTA*TOQUE,
           'Passa-cabo':                 2*PASSA_CABO}
    est = {'Metalon 40 × 20 · barra contínua e travessas':
           (L_TOT + 2*PROF)/100*FIXA_M,
           'Chumbamento, buchas e parafusos': FIXA_ACES}

    pal = {}
    if palha:
        # ⛔ A TELA NÃO SE COMPRA POR m². Vem em rolo de 1,00 m de largura e
        #   se paga por metro CORRIDO. Cada porta precisa de uma peça de
        #   (L_VAO+3) × (H_VAO+3) para sobrar aparo; duas cabem lado a lado
        #   na largura do rolo, então são duas fileiras.
        pc_l, pc_h = L_VAO + 3, H_VAO + 3
        p_fila  = max(1, int(100//pc_l))                   # peças por fileira
        filas   = -(-N_PORTA//p_fila)
        rolo_m  = max(PALHA_MIN_M, round(filas*pc_h/100 + 0.049, 1))
        pal = {'Tela de palhinha indiana natural · rolo de 1,00 m':
               rolo_m*PALHA_ROLO_M,
               'Adesivo próprio para fibra natural': ADESIVO,
               'Rebaixo, assentamento, prensagem e aparo · por porta':
               N_PORTA*mo}

    cons = (ch_custo + fita)*0.06
    sub  = ch_custo + fita + cons + sum(fer.values()) + sum(est.values()) \
           + sum(pal.values())
    emb  = sub*M.EMBALAGEM
    cd   = sub + emb
    return dict(pcs=PCS, area=area, chapas=chapas, ch=ch_custo, fita_m=fita_m,
                fita=fita, cons=cons, fer=fer, est=est, pal=pal, emb=emb,
                cd=cd, preco=lambda mc=MC_ALVO, b=BASE: round(cd/(b - mc)/10)*10)


PALHA = orcar(True)
LISA  = orcar(False)
PV_PALHA, PV_LISA = PALHA['preco'](), LISA['preco']()
DELTA = PV_PALHA - PV_LISA

# ── os cenários que o relatório mede ────────────────────────────────────
BASE_SEM_RT = M.base(parcelas=0, rt=False, vendedor=False)
PV_PALHA_SRT = PALHA['preco'](MC_ALVO, BASE_SEM_RT)
PV_LISA_SRT  = LISA['preco'](MC_ALVO,  BASE_SEM_RT)
ESP15_LISA   = orcar(False, esp_corpo=15)
UMA_CHAPA    = orcar(True,  fundo6=False)     # ⭐ o móvel inteiro em 1 chapa
MO_BAIXA     = orcar(True,  mo=PALHA_MO_BAIXA)
EXTRA_PALHA  = PALHA['cd'] - LISA['cd']       # o acréscimo real, já com 2%
ESPECIAL     = orcar(True, chapa18=MAD_ESPECIAL)
LED_CD = (L_TOT/100*LED_M + LED_FONTE)*(1 + M.EMBALAGEM)
LED_PV = round(LED_CD/(BASE - MC_ALVO)/10)*10

# ── trava: o preço tem de vir do motor ──────────────────────────────────
assert abs(PV_LISA - round(LISA['cd']/(BASE - MC_ALVO)/10)*10) < 0.5
assert PV_PALHA > PV_LISA > 0, '⛔ A PALHA TEM DE CUSTAR MAIS QUE A LISA'
assert abs(L_PORTA*N_MOD + (N_MOD - 1)*FOLGA - L_TOT) < 0.01, \
    '⛔ AS CINCO FRENTES NÃO FECHAM OS 2,30 m'

if __name__ == '__main__':
    W = 86
    print('═'*W)
    print('ANA CAROLINA · APTO CV — RACK DA SALA DE ESTAR, À PARTE')
    print('arquiteta Bruna Rezende · Estúdio Gráza · prancha 005_DET R00')
    print(f'linha Essencial · garantia {GARANTIA} · MC {MC_ALVO:.0%} · '
          f'{"COM" if RT_ON else "sem"} RT · base {BASE*100:.2f}%')
    print('═'*W)

    print(f'\n⭐ O MÓVEL, A 2,30 m  [Jonathan 21/10]')
    print('─'*W)
    print(f'  {"largura":<30}{vg(L_TOT/100)} m   ⭐ pedido dele · '
          f'a prancha traz 3,07')
    print(f'  {"altura do corpo":<30}{H_CORPO:.0f} cm   cota da prancha '
          f'(1 + 1 + 28 + 1 + 1)')
    print(f'  {"altura da porta":<30}{H_PORTA:.0f} cm   cota da prancha')
    print(f'  {"profundidade":<30}{PROF:.0f} cm   ★ escalado da planta, '
          f'sem cota própria')
    print(f'  {"suspenso do piso":<30}{SUSP:.0f} cm   cota da prancha — '
          f'o móvel não toca o chão')
    print(f'\n  CINCO MÓDULOS DE {vg(L_PORTA)} cm — quatro portas basculantes')
    print(f'  e um nicho aberto no penúltimo, como no desenho de 3,07.')
    print(f'  ⚠ A prancha tem SEIS módulos de ~51. Mantive a largura de')
    print(f'    módulo perto dos 51 e perdi um módulo; manter seis a 2,30')
    print(f'    daria frentes de {vg((L_TOT-5*FOLGA)/6)} cm — outra proporção. Decide ele.')

    print(f'\n{"═"*W}')
    print('O QUANTITATIVO')
    print(f'{"═"*W}')
    print(f'{"PEÇA":<54}{"medida":>13}{"q":>3}{"mm":>5}{"m²":>8}')
    print('─'*W)
    for d, c, l, q, e, _f in PALHA['pcs']:
        print(f'{d[:54]:<54}{f"{c:.0f} × {l:.0f}":>13}{q:>3}{e:>5}'
              f'{c*l*q/1e4:>8.2f}')
    print('─'*W)
    for e in sorted(PALHA['area'], reverse=True):
        print(f'  {f"MDF madeirado {e} mm":<40}{PALHA["area"][e]:>6.2f} m²'
              f'   →  {PALHA["chapas"][e]:.0f} chapa(s)')
    print(f'  {"fita de borda e filetagem":<40}{PALHA["fita_m"]:>6.1f} m'
          f'    (lisa: {LISA["fita_m"]:.1f} m)')
    print(f'\n  ⛔⛔ 18 mm EM TODO O CORPO — E É O CORTE MAIS BARATO.')
    print(f'    A casa estrutura em 15 mm. Aqui as laterais e divisórias dão')
    print(f'    {sum(c*l*q for d,c,l,q,e,_ in pecas(False) if d.startswith(("Lateral","Divis")))/1e4:.2f} m², e uma chapa de 15 custa R$ {br(MAD_18*500/600)} inteira —')
    print(f'    {sum(c*l*q for d,c,l,q,e,_ in pecas(False) if d.startswith(("Lateral","Divis")))/1e4/(CH_M2*APROV)*100:.0f}% de aproveitamento. Em 18 mm elas saem da SOBRA da')
    print(f'    chapa que o tampo já pagou. Custo direto da versão lisa:')
    print(f'      em 15 mm na estrutura ....... R$ {br(ESP15_LISA["cd"])}')
    print(f'      tudo em 18 mm ............... R$ {br(LISA["cd"])}   ⭐ '
          f'R$ {br(ESP15_LISA["cd"]-LISA["cd"])} a menos, e mais rígido')

    print(f'\n{"═"*W}')
    print('⭐⭐ A PALHA NATURAL — O QUE ELA É E O QUE ELA CUSTA')
    print(f'{"═"*W}')
    print(f'  ⭐⭐ A CONSTRUÇÃO SAIU DO RENDER DA PRÓPRIA PRANCHA. Ampliando a')
    print(f'    imagem, a palha cobre QUASE TODA a face da porta e sobra um')
    print(f'    filete de madeirado de cerca de {vg(FILETE,0)} cm nas quatro bordas. Não')
    print(f'    é moldura larga com vão vazado: é REBAIXO RASO usinado na face')
    print(f'    e a palha assentada dentro dele. A elevação confirma — cada')
    print(f'    "PORTA BASC." está desenhada com LINHA DUPLA, que é o filete.')
    print(f'    ⛔ Eu havia orçado moldura de 3,5 cm. Era mais caro e não era')
    print(f'      o que o projeto desenha. Corrigido.')
    print(f'\n  ⛔ A BASE DA CASA NÃO TEM PALHA NATURAL. Tem "palha sintética,')
    print(f'    R$ 600 a chapa", que é outro produto — chapa rígida com o')
    print(f'    desenho impresso, sem trama e sem vazado. Tudo abaixo é ★.')
    for k, v in PALHA['pal'].items():
        print(f'    {k:<58}R$ {br(v):>6}')
    _ex = sum(PALHA['pal'].values())
    print(f'    {"consumíveis e embalagem sobre o acréscimo":<58}'
          f'R$ {br(EXTRA_PALHA-_ex):>6}')
    print(f'    {"":<58}{"─"*9}')
    print(f'    {"A MAIS, DE CUSTO DIRETO":<58}R$ {br(EXTRA_PALHA):>6}')
    _tela = list(PALHA['pal'].values())[0]
    print(f'\n  ⭐⭐ O QUE PESA NÃO É O ROLO, É A MÃO. A tela custa R$ {br(_tela)} —')
    print(f'    {_tela/EXTRA_PALHA*100:.0f}% do acréscimo. Os outros '
          f'{100-_tela/EXTRA_PALHA*100:.0f}% são serviço: a porta lisa')
    print(f'    sai pronta da CNC e vai para a montagem; a de palha volta')
    print(f'    para a bancada — a tela é hidratada, assentada no rebaixo,')
    print(f'    prensada até secar e aparada rente ao filete, uma a uma.')
    print(f'    É a mesma lógica da malha de corda da brinquedoteca: o')
    print(f'    insumo é barato, a mão é que custa.')
    print(f'    ⚠ E é por isso que ele é ★: se o serviço for '
          f'R$ {br(PALHA_MO_BAIXA)} por porta')
    print(f'      em vez de R$ {br(PALHA_MO_PORTA)}, a versão com palha cai para '
          f'R$ {br(MO_BAIXA["preco"]())}')
    print(f'      — R$ {br(PV_PALHA-MO_BAIXA["preco"]())} abaixo do que estou declarando.')
    print(f'\n  ⚠⚠ E ATENÇÃO AO QUE A PALHA ASSENTADA **NÃO** FAZ: ela não')
    print(f'    ventila. Palha esticada em vão vazado respira; palha colada')
    print(f'    sobre a folha de MDF é uma superfície fechada como qualquer')
    print(f'    outra. ⛔ Rack de TV guarda receiver e conversor, que')
    print(f'    esquentam atrás de porta fechada — nas DUAS versões o fundo')
    print(f'    precisa de rasgo de ventilação. É usinagem no fundo, que a')
    print(f'    fabricação já carrega; o que não pode é a proposta vender')
    print(f'    "frente que respira", porque esta não respira.')
    print(f'  ⚠ E A FIBRA NATURAL TRABALHA. Palha colada em superfície plana')
    print(f'    pode soltar na borda com a variação de umidade, e aqui ela')
    print(f'    fica numa porta que bate dezenas de vezes por semana. ⭐ Por')
    print(f'    isso o rebaixo: a palha fica CONTIDA pelo filete em todo o')
    print(f'    perímetro, e não só colada na superfície. É o detalhe que')
    print(f'    decide se a frente ainda está inteira no quinto ano.')
    print(f'\n  ⭐ O MIOLO VAI TODO EM MADEIRADO, nas duas versões — e de')
    print(f'    graça. O nicho é aberto: num móvel aberto a caixaria É o')
    print(f'    acabamento, então as duas divisórias e o fundo do nicho já')
    print(f'    teriam de ser madeirado. Pôr Branco TX no resto obrigaria a')
    print(f'    comprar uma chapa inteira de branco por {sum(c*l*q for d,c,l,q,e,_ in pecas(False) if d.startswith(("Divis","Fundo")))/1e4:.2f} m² — e as')
    print(f'    peças de madeirado cabem na sobra da chapa já paga. ⛔ Aqui')
    print(f'    misturar cor é MAIS caro, não mais barato.')

    print(f'\n{"═"*W}')
    print('O CUSTO DIRETO, LADO A LADO')
    print(f'{"═"*W}')
    lin = [('chapa de MDF madeirado', 'ch'), ('fita de borda e filetagem', 'fita'),
           ('consumíveis · 6%', 'cons')]
    print(f'  {"":<44}{"com palha":>12}{"lisa":>12}')
    print('  ' + '─'*58)
    for rot, k in lin:
        print(f'  {rot:<44}R$ {br(PALHA[k]):>8}  R$ {br(LISA[k]):>8}')
    for rot, k in [('ferragem', 'fer'), ('estrutura de suspensão', 'est'),
                   ('palha natural · tela, adesivo e mão', 'pal')]:
        a, b = sum(PALHA[k].values()), sum(LISA[k].values())
        print(f'  {rot:<44}R$ {br(a):>8}  R$ {br(b) if b else "—":>8}')
    print(f'  {"embalagem · 2%":<44}R$ {br(PALHA["emb"]):>8}  '
          f'R$ {br(LISA["emb"]):>8}')
    print('  ' + '─'*58)
    print(f'  {"CUSTO DIRETO":<44}R$ {br(PALHA["cd"]):>8}  '
          f'R$ {br(LISA["cd"]):>8}')
    print(f'  {f"PREÇO · MC {MC_ALVO:.0%}, com RT":<44}'
          f'R$ {br(PV_PALHA):>8}  R$ {br(PV_LISA):>8}')

    print(f'\n{"═"*W}')
    print('⭐ AS DUAS VERSÕES')
    print(f'{"═"*W}')
    print(f'  A · PORTAS COM PALHA NATURAL ............ R$ {br(PV_PALHA):>7}')
    print(f'      rebaixo raso usinado na face e tela de palhinha indiana')
    print(f'      assentada dentro dele, com filete de madeirado à vista')
    print(f'  B · PORTAS LISAS ........................ R$ {br(PV_LISA):>7}')
    print(f'      a mesma folha, sem o rebaixo e sem a tela')
    print(f'\n  DIFERENÇA ............................... R$ {br(DELTA):>7}'
          f'   ({DELTA/PV_LISA*100:+.0f}%)')
    print(f'  ⭐ São R$ {br(DELTA/N_PORTA)} por porta. A palha é o que o render da')
    print(f'    própria prancha mostra — a versão B é a alternativa, não o')
    print(f'    projeto.')

    print(f'\n{"═"*W}')
    print('A MARGEM, E O QUE MUDA SE A DECISÃO FOR OUTRA')
    print(f'{"═"*W}')
    print(f'  {"":<30}{"com palha":>12}{"lisa":>12}')
    print('  ' + '─'*44)
    for mc in (0.35, 0.38, 0.40, 0.43):
        mk = ' ⭐' if abs(mc - MC_ALVO) < 1e-9 else ''
        print(f'  MC {mc:.0%}{mk:<24}R$ {br(PALHA["preco"](mc)):>8}'
              f'  R$ {br(LISA["preco"](mc)):>8}')
    print('  ' + '─'*44)
    print(f'  {"sem RT, mesma MC":<30}R$ {br(PV_PALHA_SRT):>8}  '
          f'R$ {br(PV_LISA_SRT):>8}')
    print(f'    ⚠ A RT é a decisão que mais mexe no preço: '
          f'R$ {br(PV_PALHA-PV_PALHA_SRT)} na versão')
    print(f'      com palha. Orçei COM RT porque a prancha é da Bruna')
    print(f'      Rezende e o apartamento inteiro é projeto dela. ⛔ Se a')
    print(f'      proposta de 02/07 foi fechada SEM RT, este item tem de')
    print(f'      sair sem também — senão o mesmo apartamento tem duas')
    print(f'      regras. **Isso eu não consigo conferir no dossiê.**')
    print(f'\n  {"⭐ fundo em 18, e não em 6":<30}R$ '
          f'{br(UMA_CHAPA["preco"]()):>8}   (com palha)')
    print(f'    ⭐⭐ O MÓVEL INTEIRO CABE EM UMA CHAPA SÓ. Com o fundo em 6 mm')
    print(f'      são duas chapas: a de 18 usa {PALHA["area"][18]/(CH_M2*APROV)*100:.0f}% do que dá para')
    print(f'      aproveitar e a de 6 usa {PALHA["area"][6]/(CH_M2*APROV)*100:.0f}% — e a de 6 custa R$ {br(MAD_6)}')
    print(f'      inteira. Levando o fundo para 18 mm ele sai da SOBRA da')
    print(f'      primeira: {UMA_CHAPA["area"][18]:.2f} m² contra os {CH_M2*APROV:.2f} m² que a chapa dá.')
    print(f'      Economiza R$ {br(PALHA["cd"]-UMA_CHAPA["cd"])} de custo e R$ {br(PV_PALHA-UMA_CHAPA["preco"]())} de preço, e o fundo')
    print(f'      de 18 mm ainda enrijece um móvel que fica pendurado.')
    print(f'      ⚠ Declarei o fundo em 6 mm, que é a construção padrão da')
    print(f'        casa. A troca é um ganho limpo — mas é decisão dele.')
    print(f'\n  {"se o madeirado for ESPECIAL":<30}R$ '
          f'{br(ESPECIAL["preco"]()):>8}')
    print(f'    ⚠ "MDF MADEIRADO À DEFINIR" — a prancha não fecha o padrão.')
    print(f'      Orçado na linha de cor (R$ {br(MAD_18)}/chapa). Num especial')
    print(f'      — Freijó Puro Duratex, lâmina natural — a chapa vai a')
    print(f'      R$ {br(MAD_ESPECIAL)} e o preço sobe R$ {br(ESPECIAL["preco"]()-PV_PALHA)}.')

    print(f'\n{"═"*W}')
    print('OPCIONAL QUE A PRANCHA NÃO PEDE')
    print(f'{"═"*W}')
    print(f'  LED inferior · fita 2700 K em perfil com difusor, na face')
    print(f'  de baixo do rack, lavando o piso ........ R$ {br(LED_PV):>7}')
    print(f'  ⭐ O móvel é suspenso {SUSP:.0f} cm do piso: é exatamente o móvel')
    print(f'    que o LED inferior valoriza. Não está no total.')

    print(f'\n{"═"*W}')
    print('⛔ O QUE ESTE ORÇAMENTO NÃO TOCA')
    print(f'{"═"*W}')
    print('  · O PAINEL DE TV JÁ VENDIDO — "liso em madeirado fosco, com')
    print('    passagem de fiação", R$ 8.900 de tabela, dentro de')
    print('    `Sala - painéis` (R$ 31.890) no fechamento de 30/09. Este')
    print('    rack é item NOVO e SOMA; nada do que já foi fechado muda.')
    print('    ⭐ [regra de 21/10] valor só se alterar quando pedido.')
    print('  · A televisão, o receiver e o cabeamento.')
    print('  · Ponto de tomada, circuito e interruptor — elétrica de obra.')
    print('  · Alvenaria, pintura e o forro.')

    print(f'\n{"═"*W}')
    print('★ EM ABERTO')
    print(f'{"═"*W}')
    print(f'  · ★★ PREÇO DA PALHA NATURAL. Não está na base da casa. Tela a')
    print(f'    R$ {br(PALHA_ROLO_M)}/m de rolo e R$ {br(PALHA_MO_PORTA)} de mão por porta são '
          f'estimativa minha.')
    print(f'    É o maior ★ deste orçamento — vale uma cotação antes de ir.')
    print(f'  · ⚠ RT, SIM OU NÃO. Ver acima: R$ {br(PV_PALHA-PV_PALHA_SRT)} de diferença.')
    print(f'  · ⚠ O PADRÃO DO MADEIRADO não está definido na prancha.')
    print(f'  · ⚠ A PROFUNDIDADE de {PROF:.0f} cm foi ESCALADA da planta, que não')
    print(f'    traz cota. A prancha manda conferir tudo no local (obs. 01).')
    print(f'  · ⚠ PUXADOR. A Elevação A não diz nada do rack; a Elevação B')
    print(f'    usa "PUXADOR CAVA Ø = 8 CM", mas é no armário bege da outra')
    print(f'    parede. O render não mostra puxador nenhum na frente de')
    print(f'    palha — por isso orçei FECHO-TOQUE, que é o que o desenho')
    print(f'    mostra. Cava na palha não existe: não há onde usinar.')
    print(f'  · ⚠ COMO A PORTA BASCULANTE ABRE. "PORTA BASC." numa frente de')
    print(f'    {H_PORTA:.0f} cm a {SUSP:.0f} cm do piso só abre PARA BAIXO — para cima ela')
    print(f'    bateria no painel. Orçado com pistão a gás e amortecimento.')
    print(f'  · ⚠ FIXAÇÃO ATRAVÉS DO PAINEL. O rack pendura no painel que já')
    print(f'    foi vendido. O metalon tem de chumbar na ALVENARIA por trás,')
    print(f'    e isso exige furar o painel. ⛔ Se o painel já estiver')
    print(f'    instalado quando o rack for produzido, é serviço em obra')
    print(f'    pronta — confirmar a ordem das duas entregas.')
    print(f'  · ⭐ A LARGURA DE MÓDULO. Cinco de {vg(L_PORTA)} (adotado) ou seis de')
    print(f'    {vg((L_TOT-5*FOLGA)/6)}. Seis módulos acrescentam uma porta: '
          f'mais ferragem,')
    print(f'    mais palha, mais fita. Se ele preferir seis, eu refaço.')
