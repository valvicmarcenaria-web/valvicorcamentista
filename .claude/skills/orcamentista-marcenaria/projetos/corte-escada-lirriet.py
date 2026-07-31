# -*- coding: utf-8 -*-
"""
HOME OFFICE SOB A ESCADA — Lirriet Libório  [lead 31/07/2026, WhatsApp]

⚠️ ENTRADA É MOODBOARD, NÃO EXECUTIVO. Não há uma única cota no material recebido.
A geometria abaixo foi ESCALADA a partir do render, usando duas referências:
  · altura da bancada .............. 75 cm (padrão de projeto, confere no render)
  · porta ao lado do móvel ......... 210 cm de folha (topo da porta coincide, no
                                      render, com o ponto em que a escada encontra
                                      a parede → altura máxima do móvel = 210 cm)
O COMPRIMENTO da bancada NÃO fecha por escala: dois caminhos independentes deram
236 cm (pela largura da folha da porta) e 268 cm (pela inclinação da escada). A
diferença é distorção de perspectiva do render — não dá para cravar.
→ Por isso este script roda a MESMA composição em 3 comprimentos (200/250/300 cm).
  O número vira exato no minuto em que a Lirriet mandar as medidas pedidas no fim.

GEOMETRIA DERIVADA (premissa):
  altura no encontro com a parede ... 210 cm
  inclinação da escada ............... queda de 0,719 cm por cm na horizontal
  bancada ............................ h 75 cm · prof 55 cm
  prateleira 1 ....................... h 116 cm · o triângulo dá 131 cm de vão
  prateleira 2 ....................... h 161 cm · o triângulo dá  68 cm de vão
  fundo amadeirado acima da bancada .. triângulo 188 × 135 cm (NÃO cresce com L:
                                       além de 188 cm a escada já desceu abaixo
                                       da bancada e não há o que revestir)

ESCOPO LIDO NO MOODBOARD (tudo em MDF melamínico fosco amadeirado):
  1. painel de fundo amadeirado, acompanhando a diagonal da escada
  2. bancada com engrossamento de borda
  3. gaveteiro de 3 gavetas, puxador cava usinado
  4. painel ripado fechando a frente sob a bancada
  5. 2 prateleiras com fita de LED embutida em cava
  6. lateral direita fechando o vão junto à porta
  7. 3 linhas de LED: sob cada prateleira + sob a bancada
"""
from collections import defaultdict

# ═══════════════════════════════════ base de chapa [Jonathan 28/07]
CH_C, CH_L = 275.0, 185.0
CH_AREA = CH_C*CH_L/10000                      # 5,0875 m²
P = {'AMA15': 500.0, 'AMA6': 350.0,            # melamínico fosco amadeirado (carvalho)
     'BRC15': 300.0, 'BRC6': 200.0}            # caixaria interna do gaveteiro
FITA_COR, FITA_BRC = 3.0, 2.0                  # R$/m — insumo
FILET, FILET_MAN = 2.5, 4.0                    # aplicação: coladeira / manual (ripas)
LED_M = 150.0                                  # fita + perfil + usinagem, por metro
P_CORR_OCULTA = 70.0                           # par, Hardt
P_CAVA = 50.0                                  # puxador cava usinado, por peça

# ═══════════════════════════════════ geometria
H_APEX, INCL = 210.0, 0.719
H_BANC, PROF_BANC = 75.0, 55.0
H_PR1, H_PR2, PROF_PR = 116.0, 161.0, 25.0
GAV_L, GAV_P, GAV_H = 45.0, 55.0, 65.0
RIPA_L, RIPA_GAP = 2.0, 2.0                    # ripas de 2 cm espaçadas 2 cm

def vao(h):
    """comprimento livre na altura h, medido do encontro com a parede."""
    return max(0.0, (H_APEX - h)/INCL)

L_PR1, L_PR2 = vao(H_PR1), vao(H_PR2)          # 131 / 68 cm
L_FUNDO      = vao(H_BANC)                     # 188 cm — base do triângulo do fundo

# ═══════════════════════════════════ nesting real (mesmo motor dos outros projetos)
def fit_pieces(w, h, items):
    if not items: return []
    for i, (c, l) in enumerate(items):
        for (pc, pl) in ((c, l), (l, c)):
            if pc <= w and pl <= h:
                rest = items[:i] + items[i+1:]
                a = fit_pieces(w-pc, pl, [x for x in rest])
                b = fit_pieces(w, h-pl, [x for x in rest if x not in a])
                return [(c, l)] + a + b
    return []

def nest(items):
    """shelf-packing por faixas, com piso de aproveitamento de 80%."""
    if not items: return 0
    pcs = sorted(([max(c, l), min(c, l)] for c, l in items), key=lambda p: -p[1])
    chapas, atual = 0, []
    y = 0.0; faixa_h = 0.0; x = 0.0
    for c, l in pcs:
        if c > CH_C and l <= CH_C: c, l = l, c
        if c > CH_C or l > CH_L:
            chapas += 1; continue                       # peça grande = chapa dedicada
        if x + c > CH_C:                                # nova faixa
            y += faixa_h; x = 0.0; faixa_h = 0.0
        if y + l > CH_L:                                # nova chapa
            chapas += 1; y = 0.0; x = 0.0; faixa_h = 0.0
        x += c; faixa_h = max(faixa_h, l)
    chapas += 1
    area = sum(c*l for c, l in items)/10000
    return max(chapas, -(-int(area/(CH_AREA*0.80)*1000)//1000) or 1)

# ═══════════════════════════════════ lista de peças, por comprimento de bancada
def pecas_para(L, ripado=True):
    """L = comprimento útil da bancada, em cm. Devolve [(desc, material, c, l, q)]."""
    p = []
    a = p.append
    # 1 · fundo amadeirado acima da bancada — triângulo 188 × 135, cortado em 2 peças
    a(('fundo amadeirado — pano maior',  'AMA15', min(L, L_FUNDO), 135.0, 1))
    # 2 · bancada (tampo + tira de engrossamento na borda frontal)
    a(('bancada — tampo',                'AMA15', L, PROF_BANC, 1))
    a(('bancada — engrossamento frontal','AMA15', L,  8.0, 1))
    # 3 · gaveteiro: 2 laterais, base, tampo, fundo, 3 caixas de gaveta, 3 frentes
    a(('gaveteiro — laterais',           'BRC15', GAV_H, GAV_P, 2))
    a(('gaveteiro — base e tampo',       'BRC15', GAV_L, GAV_P, 2))
    a(('gaveteiro — fundo',              'BRC6',  GAV_L, GAV_H, 1))
    a(('gaveta — laterais',              'BRC15', GAV_P-5, 18.0, 6))
    a(('gaveta — frente e costas int.',  'BRC15', GAV_L-4, 18.0, 6))
    a(('gaveta — fundo',                 'BRC6',  GAV_L-4, GAV_P-5, 3))
    a(('gaveteiro — frentes',            'AMA15', GAV_L, 21.0, 3))
    # 4 · painel ripado frontal sob a bancada
    if ripado:
        n_rip = int((L - GAV_L)/(RIPA_L + RIPA_GAP))
        a(('ripado — base do painel',    'AMA6',  L-GAV_L, GAV_H, 1))
        a(('ripado — ripas 2 cm',        'AMA15', GAV_H, RIPA_L, n_rip))
    else:                                            # versão enxuta: painel liso
        n_rip = 0
        a(('painel frontal liso',        'AMA15', L-GAV_L, GAV_H, 1))
    # 5 · prateleiras (18mm seria o ideal >70cm; aqui 15mm + apoio contínuo no fundo)
    a(('prateleira 1',                   'AMA15', L_PR1, PROF_PR, 1))
    a(('prateleira 2',                   'AMA15', L_PR2, PROF_PR, 1))
    # 6 · lateral direita, fechando o vão sob a bancada
    a(('lateral direita',                'AMA15', H_BANC, PROF_BANC, 1))
    return p, n_rip

def orcar(L, MC=0.37, mostrar=True, ripado=True, led_bancada=True):
    pecas, n_rip = pecas_para(L, ripado)
    porm = defaultdict(list); area = defaultdict(float)
    for d, m, c, l, q in pecas:
        for _ in range(q):
            porm[m].append((c, l)); area[m] += c*l/10000
    chapas = {m: nest(v) for m, v in porm.items()}
    custo_chapa = sum(chapas[m]*P[m] for m in chapas)

    # fita: face aparente de cada peça. Ripas = 3 faces (frente + 2 laterais).
    fita_cor  = (min(L, L_FUNDO)*2 + 135*2)/100                      # fundo
    fita_cor += (L*2 + PROF_BANC*2)/100                              # bancada
    fita_cor += 3*(GAV_L*2 + 21*2)/100                               # frentes
    fita_cor += (L_PR1*2 + PROF_PR*2 + L_PR2*2 + PROF_PR*2)/100      # prateleiras
    fita_cor += (H_BANC*2 + PROF_BANC*2)/100                         # lateral
    fita_rip  = n_rip*(GAV_H*2 + RIPA_L)/100      # ripas: 2 bordas longas + topo
    if not ripado:
        fita_cor += ((L-GAV_L)*2 + GAV_H*2)/100   # painel liso: borda em volta
    fita_brc  = (2*(GAV_H+GAV_P) + 2*(GAV_L+GAV_P))*2/100 + 3*2*(GAV_L-4+GAV_P-5)/100
    custo_fita  = (fita_cor + fita_rip)*FITA_COR + fita_brc*FITA_BRC
    # ripa de 2 cm não entra na coladeira em pé → filetagem MANUAL, mais cara
    custo_filet = (fita_cor + fita_brc)*FILET + fita_rip*FILET_MAN

    led_m = (L_PR1 + L_PR2 + (L if led_bancada else 0))/100
    custo_ferr = 3*P_CORR_OCULTA + 3*P_CAVA + led_m*LED_M
    consum = (custo_chapa + custo_fita)*0.06
    MAT = custo_chapa + custo_fita + custo_filet + custo_ferr + consum

    LOGISTICA, VISITA, INSTALACAO = 350.0, 250.0, 450.0    # obra única, 1 ambiente
    fixedR = MAT + LOGISTICA + VISITA + INSTALACAO

    a_, liqF_, b_ = 0.162, 0.88, 0.043
    div = 1 - a_ - liqF_*b_ - MC
    inv = fixedR/div

    if mostrar:
        print('═'*78)
        print(f'BANCADA DE {L:.0f} cm')
        print('═'*78)
        print(f'  {"peça":<38}{"mat":>7}{"c×l cm":>16}{"qt":>4}')
        for d, m, c, l, q in pecas:
            print(f'  {d:<38}{m:>7}{c:>8.1f}×{l:<7.1f}{q:>4}')
        print('  ' + '─'*74)
        for m in sorted(chapas):
            print(f'  {m:<12} {area[m]:>6.2f} m²   →  {chapas[m]:>2} chapa(s) × R$ {P[m]:>6.0f}'
                  f'  = R$ {chapas[m]*P[m]:>8,.2f}')
        print(f'  {"ripas de 2 cm":<12} {n_rip:>6} un')
        print(f'  {"fita cor":<12} {fita_cor:>6.1f} m  ·  fita do ripado {fita_rip:.1f} m (manual)'
              f'  ·  branca {fita_brc:.1f} m  ·  LED {led_m:.2f} m')
        print('  ' + '─'*74)
        print(f'  {"Chapas":<44}R$ {custo_chapa:>10,.2f}')
        print(f'  {"Fita (insumo)":<44}R$ {custo_fita:>10,.2f}')
        print(f'  {"Filetagem (aplicação)":<44}R$ {custo_filet:>10,.2f}')
        print(f'  {"Ferragens + LED":<44}R$ {custo_ferr:>10,.2f}')
        print(f'  {"Consumíveis (6%)":<44}R$ {consum:>10,.2f}')
        print(f'  {"Logística · visita · instalação":<44}R$ {LOGISTICA+VISITA+INSTALACAO:>10,.2f}')
        print(f'  {"CUSTO DIRETO":<44}R$ {fixedR:>10,.2f}')
        print(f'  {"INVESTIMENTO (MC 37%)":<44}R$ {inv:>10,.2f}')
        print(f'  {"À vista (−10%)":<44}R$ {inv*0.9:>10,.2f}')
    return fixedR, inv

if __name__ == '__main__':
    res = {}
    for L in (200.0, 250.0, 300.0):
        res[L] = orcar(L)
        print()
    print('═'*78)
    print('FAIXA DE INVESTIMENTO — o comprimento da bancada é a única incógnita relevante')
    print('═'*78)
    print(f'  {"bancada":<14}{"custo direto":>16}{"investimento":>16}{"à vista":>14}')
    for L, (c, i) in res.items():
        print(f'  {L:>5.0f} cm      {c:>14,.2f}  {round(i/100)*100:>14,.0f}  {round(i*0.9/100)*100:>12,.0f}')
