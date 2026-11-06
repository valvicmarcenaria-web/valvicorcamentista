# -*- coding: utf-8 -*-
"""HAVERSON SOARES — GERA as abas de ambiente no LAYOUT DA CASA (o mesmo da Ana
Carolina e André, que veio do Gustavo Raposo): painel de material B..G com
fórmulas que leem as peças pela CHAVE (coluna K) · os itens com conferência ·
o que não é marcenaria · as peças por item com R$ UN = VLOOKUP(chave; precos) ·
notas e dúvidas numeradas.
E calcula aqui, com os preços da Base de 06/11/2026, o que a planilha TEM de
mostrar — é a conferência dela.

⛔ locale pt_BR: separador ';' · nome de função em inglês · nada de decimal
   literal dentro de fórmula.
uso: python3 -I planilha.py  → grava _abas.json e imprime o resumo
"""
import json, math, sys, pathlib
P = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(P)); sys.path.insert(0, str(P.parent))
import levantamento as L
import motor_mc as MC

PRECO = {'MDF Azul 18': 700, 'MDF Azul 15': 550, 'MDF Freijó 18': 700, 'MDF Freijó 15': 550,
         'MDF Freijó 6': 350, 'MDF Branco TX 18': 400, 'MDF Branco TX 15': 350, 'MDF Branco TX 6': 250,
         'Fita cor': 3, 'Fita Branco TX': 2, 'Filetagem automática': 2.5,
         # ⭐ as três linhas da casa [Jonathan, 06/11/2026]: a aba mostra a HETTICH
         'Dobradiça Hettich': 50, 'Corrediça Hettich': 150,
         'Báscula HK-XS': 250, 'Pistão com amortecimento': 30, 'Cava usinada': 50,
         'Suporte de prateleira': 6.5, 'Perfil de proteção de piso': 15,
         'LED conjunto': 150, 'Fonte de LED': 120, 'Dobradiça vidro': 70,
         # ⭐ referência confirmada em obra (Kenia e Fábio): reflecta bronze, perfil bronze,
         #   puxador e furos, cerca de R$ 660 o m² · ⚠ cotar com o vidraceiro
         'Porta de vidro reflecta bronze': 660,
         'Corte por chapa': 2, 'Corte por peça': 2.5, 'Frete': 200}
AREA, APROV, CONS, EMB = 5.0875, 0.80, 0.06, 0.02
# ⭐ frete é a célula AMARELA, digitada pelo Jonathan na planilha [06/11/2026]
VIAGENS = {'Cozinha': 1, 'Gourmet': 1}
ABAS = [('Cozinha', '01 Cozinha', 102, 'Folhas 01 a 04 · planta e elevações A, B, C e D'),
        ('Gourmet', '02 Gourmet', 103, 'Folhas 05 a 07 · planta e elevações A e B')]
SUB = {
 'Cozinha': 'armários inferiores sob a bancada existente, torre quente, superiores, bancada em MDF com nicho da adega, armário e máscara da geladeira, painel do piso ao teto e colmeia de vinhos na ilha · MDF Azul a definir por fora, Branco por dentro · três linhas de ferragem: a aba mostra a Hettich',
 'Gourmet': 'cristaleira de vidro reflecta bronze, torre quente, nicho e superior com básculas em Freijó Puro · inferiores em Azul sob a bancada existente · três linhas de ferragem: a aba mostra a Hettich',
}
FORA = {
 'Cozinha': ['⛔ PEDRA: a bancada existente, o complemento de bancada, a ilha e a FRENTE dos sóculos ("no mesmo material da bancada")',
             'Cooktop, coifa, cubas, geladeira, micro-ondas, forno e a adega de 33 garrafas',
             'O sóculo existente sob as bancadas de pedra'],
 'Gourmet': ['⛔ PEDRA: as bancadas existentes, o frontão e a FRENTE dos sóculos',
             'Churrasqueira, cubas, micro-ondas, forno e a adega existente',
             'A bancada de alvenaria existente da parede da direita'],
}
COMUNS = [
 '⭐ PRANCHAS COTADAS: o executivo da Luiza Pacheco cota larguras e alturas; o que não está cotado (profundidade dos superiores, da colmeia) vai como dúvida.',
 '⚠ MDF AZUL A DEFINIR: orçado como Melamínico Fosco de cor (550 a de 15, 700 a de 18). Freijó Puro, Essencial Wood da Duratex, é a mesma linha de preço.',
 '⭐ AS TRÊS LINHAS DA CASA [Jonathan, 06/11/2026]: Telescópica, Hettich e Blum. Esta aba mostra a HETTICH (Sensys R$ 50, Quadro V6 R$ 150 o par), a de referência; a Telescópica e a Blum saem do precos.py, e só a corrediça e a dobradiça mudam.',
 '⭐ CAVA NA MARCENARIA: R$ 50 o metro, pela largura de cada frente.',
]
GIRO = ''
DUV = {
 'Cozinha': ['⚠ AS BÁSCULAS DA PIA ABREM PARA BAIXO: a pedra está logo acima. Lançadas com duas dobradiças e dois pistões com amortecimento cada.',
             '⚠ OS GAVETÕES SOB AS CUBAS pedem recorte para o sifão: a caixa sai em U, sem custo extra de chapa.',
             '⚠ OS SUPERIORES SOBRE A BANCADA têm 60 de profundidade, lidos do corte B. Se forem de 35, a chapa cai.',
             '⚠ COLMEIA DE VINHOS: a ilha tem 44 de profundidade e a prancha não cota a colmeia; lançada com 40. A meia-madeira das divisórias é usinagem de CNC sem preço na Base. ⚠ A regra dos 80% compra DUAS chapas de Freijó 18 só para ela, mas o plano de corte mostra que cabe em UMA: quatro tiras de 40, três horizontais ou quatro verticais em cada. Se a produção confirmar, saem R$ 700 e o corte de uma chapa.',
             '⚠ PORTA-TEMPEROS: lançado como gaveta estreita de MDF com três bandejas. Se for aramado, é outro preço.'],
 'Gourmet': ['⚠ PORTA DE VIDRO REFLECTA BRONZE com perfil bronze: R$ 660 o m², a referência confirmada em obra (Kenia e Fábio). ⛔ Cotar com o vidraceiro, com o puxador bronze a definir.',
             '⚠ AS BÁSCULAS DO SUPERIOR ABREM PARA CIMA: articulador da casa (AVENTOS HK-XS, R$ 250). O mesmo nas três linhas.',
             '⚠ AS BÁSCULAS DA PIA ABREM PARA BAIXO, como na cozinha.',
             '⚠ LED DA CRISTALEIRA: perfil com abas sob o teto e sob as três prateleiras, conjunto completo a R$ 150 o metro, mais uma fonte. As prateleiras saem FIXAS para o fio passar.'],
}


def chapa_custo(c, l, q, k):
    return c * l / 1e4 * q / (AREA * APROV) * PRECO[k]


def monta(amb, aba, sid, prancha):
    itens = [i for i in L.ITENS if i['amb'] == amb]
    # ── as linhas de peça de cada item (com fita, filetagem e ferragem) ──
    blocos = []
    for i in itens:
        lin = []
        fita = {}
        for nome, obs, c, l, q, k, fm, tipo in i['pecas']:
            lin.append(('peca', nome, obs, c, l, q, 'm²', k))
            if fm: fita[tipo] = fita.get(tipo, 0) + fm * q
        for nome, obs, c, l, q, un, k in i.get('terc', []):
            lin.append(('terc', nome, obs, c, l, q, un, k))
        for tipo, m in fita.items():
            lin.append(('fita', tipo, '22 mm · aresta a aresta, mais 10% de desperdício', '', '', round(m * 1.1, 1), 'm', tipo))
        tot = sum(fita.values())
        if tot:
            lin.append(('fita', 'Filetagem automática', 'Coladeira · 15 e 18 mm · serviço, sem desperdício', '', '', round(tot, 1), 'm', 'Filetagem automática'))
        for nome, obs, q, un, k in i['ferr']:
            lin.append(('ferr', nome, obs, '', '', q, un, k))
        blocos.append((i, lin))
    chaves_mdf = sorted({k for _, lin in blocos for t, *_, k in lin if t == 'peca'})
    fitas = [t for t in ('Fita cor', 'Fita Branco TX') if any(x[7] == t for _, lin in blocos for x in lin)]
    # ── o layout ─────────────────────────────────────────────────────────
    R = {}                                   # linha (1-based) → lista B..K
    def put(r, *v): R[r] = list(v) + [''] * (10 - len(v))
    put(1, f'  VALVIC MARCENARIA        {amb.upper()}')
    put(2, f'  Haverson Soares · executivo Luiza Pacheco Rev.00, {prancha} · {SUB[amb]}')
    put(4, '  O AMBIENTE   ·   chapa 275 × 185 com 80% de aproveitamento · e ela se conta em número cheio, por cor × espessura')
    put(6, 'MATERIAL', 'ESPECIFICAÇÃO', 'QUANTIDADE', 'UN', 'CUSTO', '% DO CUSTO')
    r = 7
    rows_mat = {}
    for k in chaves_mdf: rows_mat[k] = r; r += 1
    for t in fitas: rows_mat[t] = r; r += 1
    rows_mat['Filetagem automática'] = r; r += 1
    rf = r; r += 1                           # ferragem
    rcc, rcp, rcons, remb, rfr, rcd = r, r + 1, r + 2, r + 3, r + 4, r + 5
    r = rcd + 1
    rnota = r; r += 2
    rsec_it = r; r += 2
    rhead_it = r; r += 1
    rows_it = list(range(r, r + len(itens))); r += len(itens) + 1
    rsoma, rarr, rrat, rpai, rconf = r, r + 1, r + 2, r + 3, r + 4; r += 6
    rsec_fora = r; r += 2
    fora = FORA[amb] + ['⛔ PEDRA NUNCA É NOSSA, e também fora: louça, metal, eletrodoméstico, luminária, revestimento, móvel solto e box.',
                        '⛔ REGRA DOS DOIS ESTADOS: ou o item é nosso COM VALOR na linha, ou está NOMEADO aqui como fora.']
    rows_fora = list(range(r, r + len(fora))); r += len(fora) + 1
    rsec_pc = r; r += 2
    pos = []
    for n, (i, lin) in enumerate(blocos, 1):
        rh = r; rc = r + 1; rhd = r + 2; r += 3
        rl = list(range(r, r + len(lin))); r += len(lin)
        rt = r; r += 2
        pos.append((n, i, lin, rh, rc, rhd, rl, rt))
    p0, p1 = pos[0][6][0], pos[-1][7]
    rsec_nd = r; r += 2
    duv = COMUNS + DUV[amb]
    rows_duv = list(range(r, r + len(duv))); r += len(duv)
    K = f'$K${p0}:$K${p1}'; D_ = f'$D${p0}:$D${p1}'; E_ = f'$E${p0}:$E${p1}'
    F_ = f'$F${p0}:$F${p1}'; I_ = f'$I${p0}:$I${p1}'
    CH = 'VLOOKUP("Área da chapa";precos;2;FALSE)*VLOOKUP("Aproveitamento";precos;2;FALSE)'
    # painel de material
    for k, rr in rows_mat.items():
        if k.startswith('MDF'):
            area = sum(x[3] * x[4] * x[5] for _, lin in blocos for x in lin if x[0] == 'peca' and x[7] == k) / 1e4
            put(rr, k, f'{area:.1f} m² de peças · comprada inteira, por cor × espessura'.replace('.', ','),
                f'=ROUNDUP(SUMPRODUCT(({K}=$B{rr})*IF(ISNUMBER({D_});{D_}*{E_}*{F_};0))/10000/({CH}))',
                'chapas', f'=D{rr}*VLOOKUP($B{rr};precos;2;FALSE)', f'=IFERROR(F{rr}/$F${rcd};"")')
        elif k.startswith('Fita'):
            put(rr, k, ('22 mm na caixaria · R$ 2,00 o metro' if 'Branco' in k else '22 mm de cor · R$ 3,00 o metro') + ' · mais 10% de desperdício',
                f'=SUMIF({K};"{k}";{F_})', 'm', f'=D{rr}*VLOOKUP("{k}";precos;2;FALSE)', f'=IFERROR(F{rr}/$F${rcd};"")')
        else:
            put(rr, k, 'Coladeira · 15 e 18 mm · serviço por metro de aresta feita, sem desperdício',
                f'=SUMIF({K};"{k}";{F_})', 'm', f'=D{rr}*VLOOKUP("{k}";precos;2;FALSE)', f'=IFERROR(F{rr}/$F${rcd};"")')
    put(rf, 'Ferragem, terceirizados e iluminação', 'Linha HETTICH, a de referência · corrediça, dobradiça, báscula, pistão, suporte, cava, perfil de piso, LED e a porta de vidro · o resto de tudo que tem chave',
        f'=SUMPRODUCT((LEFT({K};4)<>"MDF ")*(LEFT({K};4)<>"Fita")*(LEFT({K};9)<>"Filetagem")*({K}<>"")*IF(ISNUMBER({F_});{F_};0))', 'peças',
        f'=SUMIF({K};"<>";{I_})-SUMIF({K};"MDF *";{I_})-SUMIF({K};"Fita*";{I_})-SUMIF({K};"Filetagem*";{I_})', f'=IFERROR(F{rf}/$F${rcd};"")')
    mdf_rows = [rows_mat[k] for k in chaves_mdf]
    put(rcc, 'Corte · por chapa', 'Serviço de corte, por chapa comprada · R$ 2,00', '=' + '+'.join(f'D{x}' for x in mdf_rows), 'chapas',
        f'=D{rcc}*VLOOKUP("Corte por chapa";precos;2;FALSE)', f'=IFERROR(F{rcc}/$F${rcd};"")')
    put(rcp, 'Corte · por peça', 'Serviço de corte, por peça cortada · R$ 2,50 · conta a PEÇA, não a linha',
        f'=SUMPRODUCT((LEFT({K};4)="MDF ")*IF(ISNUMBER({F_});{F_};0))', 'peças',
        f'=D{rcp}*VLOOKUP("Corte por peça";precos;2;FALSE)', f'=IFERROR(F{rcp}/$F${rcd};"")')
    put(rcons, 'Consumíveis', 'Cola, lixa, parafuso, cavilha, tapa-furo · 6% sobre chapa, fita e filetagem', '', '',
        f'=SUM(F7:F{rf - 1})*VLOOKUP("Consumíveis";precos;2;FALSE)', f'=IFERROR(F{rcons}/$F${rcd};"")')
    put(remb, 'Embalagem', 'Papelão, filme e cantoneira · 2% sobre o subtotal', '', '',
        f'=SUM(F7:F{rcons})*VLOOKUP("Embalagem";precos;2;FALSE)', f'=IFERROR(F{remb}/$F${rcd};"")')
    put(rfr, 'Frete', '⭐ R$ 200 a viagem · a QUANTIDADE é digitada: uma viagem por ambiente', VIAGENS.get(amb, 1), 'viagem',
        f'=D{rfr}*VLOOKUP("Frete";precos;2;FALSE)', f'=IFERROR(F{rfr}/$F${rcd};"")')
    put(rcd, 'CUSTO DIRETO DO AMBIENTE', '', '', '', f'=SUM(F7:F{rfr})', f'=IFERROR(F{rcd}/$F${rcd};"")')
    put(rnota, '', '⭐ Preço por NOME: a coluna K de cada peça é a chave da aba "Base (importada)", e o R$ UN vem dela. ⛔ Enquanto o #REF! da Base não for autorizado (célula D3 de lá), tudo aqui sai vazio.')
    put(rsec_it, '  OS ITENS   ·   cada móvel com o seu custo, porque é assim que a fábrica produz e o cliente confere')
    put(rhead_it, 'ITEM', 'MÓVEL', 'MEDIDA GERAL', '', '', '', '', 'CUSTO')
    for rr, (n, i, lin, rh, rc, rhd, rl, rt) in zip(rows_it, pos):
        put(rr, n, i['movel'], i['medida'], '', '', '', '', f'=I{rt}')
    put(rsoma, 'Soma dos itens · chapa rateada em fração', '', '', '', '', '', '', f'=SUM(I{rows_it[0]}:I{rows_it[-1]})')
    put(rarr, 'Arredondamento de chapa para número cheio · ⛔ a regra de ferro', '', '', '', '', '', '',
        f'=SUM(F{mdf_rows[0]}:F{mdf_rows[-1]})-SUMIF({K};"MDF *";{I_})')
    put(rrat, 'MATERIAL E FERRAGEM, PELO RATEIO DOS ITENS', '', '', '', '', '', '', f'=I{rsoma}+I{rarr}')
    put(rpai, 'Material e ferragem, pelo painel do ambiente', '', '', '', '', '', '', f'=SUM(F7:F{rf})')
    put(rconf, '⭐ CONFERÊNCIA — as duas contas têm de dar a mesma coisa', '', '', '', '', '', '', f'=I{rrat}-I{rpai}')
    put(rsec_fora, '  O QUE NÃO É MARCENARIA   ·   está na prancha, não está nesta conta')
    for rr, t in zip(rows_fora, fora): put(rr, t)
    put(rsec_pc, '  AS PEÇAS, ITEM POR ITEM   ·   cada linha é uma peça que vai para o plano de corte')
    for n, i, lin, rh, rc, rhd, rl, rt in pos:
        put(rh, f'ITEM {n:02d}', i['movel'], '', '', '', '', '', i['medida'])
        put(rc, '', i['cadeia'])
        put(rhd, 'MATERIAL', 'ESPECIFICAÇÃO', 'C', 'L', 'QTD', 'UN', 'R$ UN', 'CUSTO', '', 'chave na Base')
        for rr, (t, nome, obs, c, l, q, un, k) in zip(rl, lin):
            # ⭐ H e I das peças vão por repeatCell, um bloco por item (BLOCOS),
            #   com a fórmula da primeira linha: o Sheets ajusta a linha sozinho
            put(rr, nome, obs, c, l, q, un, '', '', '', k)
        put(rt, f'TOTAL DO ITEM {n:02d}', '', '', '', '', '', '', f'=SUM(I{rl[0]}:I{rl[-1]})')
    put(rsec_nd, '  NOTAS E PONTOS EM ABERTO   ·   cada dúvida é dinheiro parado, em ordem de quanto vale')
    for n, (rr, t) in enumerate(zip(rows_duv, duv), 1): put(rr, n, t)
    # ── a conta, aqui, com os preços da Base ─────────────────────────────
    area = {k: 0.0 for k in chaves_mdf}; ftot = {}; ferr = 0.0; npc = 0; it_custo = []
    for n, i, lin, *_ in pos:
        c_it = 0.0
        for t, nome, obs, c, l, q, un, k in lin:
            if t == 'peca':
                area[k] += c * l * q / 1e4; npc += q; c_it += chapa_custo(c, l, q, k)
            elif t == 'fita':
                ftot[k] = ftot.get(k, 0) + q; c_it += q * PRECO[k]
            elif t == 'terc':
                v = c * l / 1e4 * q * PRECO[k]; ferr += v; c_it += v
            else:
                ferr += q * PRECO[k]; c_it += q * PRECO[k]
        it_custo.append(c_it)
    nch = {k: math.ceil(a / (AREA * APROV)) for k, a in area.items()}
    c_ch = sum(nch[k] * PRECO[k] for k in nch); c_ft = sum(q * PRECO[k] for k, q in ftot.items())
    corte = sum(nch.values()) * 2 + npc * 2.5
    cons = (c_ch + c_ft) * CONS
    emb = (c_ch + c_ft + ferr + corte + cons) * EMB
    cd = c_ch + c_ft + ferr + corte + cons + emb + 200 * VIAGENS.get(amb, 1)
    linhas = [[R.get(x, [''] * 10)[j] for j in range(10)] for x in range(1, r + 1)]
    for row in linhas:                       # sem célula vazia no fim da linha
        while row and row[-1] == '': row.pop()
    pblocos = [(rl[0], rl[-1]) for *_, rl, rt in pos]
    FH = '=IFERROR(VLOOKUP($K{r};precos;2;FALSE);"")'
    FI = ('=IFERROR(IF(LEFT($K{r};4)="MDF ";$D{r}*$E{r}/10000*$F{r}/(' + CH + ')*$H{r};'
          'IF($D{r}="";$F{r}*$H{r};$D{r}*$E{r}/10000*$F{r}*$H{r}));"")')
    kinds = {'secao': [1 + x for x in (rsec_it, rsec_fora, rsec_pc, rsec_nd, 4)] and [rsec_it, rsec_fora, rsec_pc, rsec_nd, 4],
             'head': [6, rhead_it] + [p[5] for p in pos],
             'tot': [rcd, rconf] + [p[7] for p in pos],
             'item': [p[3] for p in pos], 'frete': [rfr], 'nlin': r}
    return dict(amb=amb, aba=aba, sid=sid, linhas=linhas, nlin=r, pblocos=pblocos, FH=FH, FI=FI, kinds=kinds, chapas=nch, cd=cd,
                partes=dict(chapa=c_ch, fita=c_ft, ferr=ferr, corte=corte, cons=cons, emb=emb, frete=200 * VIAGENS.get(amb, 1)),
                itens=[(i['movel'], c) for (n, i, *_), c in zip(pos, it_custo)],
                arred=c_ch - sum(chapa_custo(x[3], x[4], x[5], x[7]) for _, lin in blocos for x in lin if x[0] == 'peca'),
                gavetas=sum(f[2] for i in itens for f in i['ferr'] if f[4].startswith('Corrediça')),
                lay=dict(rcd=rcd, rnota=rnota, rfr=rfr, rsec_it=rsec_it, rhead_it=rhead_it, rrat=rrat,
                         rconf=rconf, rsec_fora=rsec_fora, rsec_pc=rsec_pc, rsec_nd=rsec_nd,
                         duv0=rows_duv[0], duv1=rows_duv[-1],
                         blocos=[(rh, rc, rhd, rl[0], rl[-1], rt) for _n, _i, _l, rh, rc, rhd, rl, rt in pos]))


# ── a identidade da casa: os mesmos 17 estilos da aba da Ana Carolina ──────
PRETO, CINZA, OURO = ({'red': .102, 'green': .102, 'blue': .102}, {'red': .42, 'green': .42, 'blue': .42},
                      {'red': .682, 'green': .514, 'blue': .227})
def _tf(sz, cor, b=False, it=False):
    t = {'fontSize': sz, 'foregroundColorStyle': {'rgbColor': cor}}
    if b: t['bold'] = True
    if it: t['italic'] = True
    return t
MOEDA = {'type': 'CURRENCY', 'pattern': '"R$" #,##0.00'}
EST = {
 'base': ({'horizontalAlignment': 'LEFT', 'verticalAlignment': 'MIDDLE', 'wrapStrategy': 'OVERFLOW_CELL',
           'textFormat': _tf(10, PRETO)}, 'userEnteredFormat'),
 'obs': ({'textFormat': _tf(9, CINZA)}, 'userEnteredFormat.textFormat'),
 'dir': ({'horizontalAlignment': 'RIGHT'}, 'userEnteredFormat.horizontalAlignment'),
 'un': ({'horizontalAlignment': 'CENTER', 'textFormat': _tf(9, CINZA)},
        'userEnteredFormat.horizontalAlignment,userEnteredFormat.textFormat'),
 'rs': ({'horizontalAlignment': 'RIGHT', 'numberFormat': MOEDA},
        'userEnteredFormat.horizontalAlignment,userEnteredFormat.numberFormat'),
 'pct': ({'horizontalAlignment': 'RIGHT', 'numberFormat': {'type': 'PERCENT', 'pattern': '0.0%'},
          'textFormat': _tf(10, CINZA)},
         'userEnteredFormat.horizontalAlignment,userEnteredFormat.numberFormat,userEnteredFormat.textFormat'),
 'ital': ({'textFormat': _tf(9, CINZA, it=True)}, 'userEnteredFormat.textFormat'),
 'cen': ({'horizontalAlignment': 'CENTER'}, 'userEnteredFormat.horizontalAlignment'),
 'chave': ({'textFormat': _tf(8, CINZA)}, 'userEnteredFormat.textFormat'),
 'itemh': ({'backgroundColorStyle': {'rgbColor': {'red': .992, 'green': .98, 'blue': .957}},
            'textFormat': _tf(11, PRETO, b=True)},
           'userEnteredFormat.textFormat,userEnteredFormat.backgroundColorStyle'),
 'itemn': ({'textFormat': _tf(11, OURO, b=True)}, 'userEnteredFormat.textFormat'),
 'duvn': ({'horizontalAlignment': 'CENTER', 'textFormat': _tf(10, OURO, b=True)},
          'userEnteredFormat.horizontalAlignment,userEnteredFormat.textFormat'),
 'secao': ({'textFormat': _tf(11, OURO, b=True),
            'borders': {'bottom': {'style': 'SOLID', 'colorStyle': {'rgbColor': PRETO}}}},
           'userEnteredFormat.textFormat,userEnteredFormat.borders'),
 'head': ({'backgroundColorStyle': {'rgbColor': {'red': .969, 'green': .969, 'blue': .969}},
           'textFormat': _tf(8, CINZA, b=True)},
          'userEnteredFormat.textFormat,userEnteredFormat.backgroundColorStyle'),
 'tot': ({'backgroundColorStyle': {'rgbColor': {'red': .961, 'green': .961, 'blue': .961}},
          'borders': {'top': {'style': 'SOLID_THICK', 'colorStyle': {'rgbColor': OURO}}},
          'textFormat': _tf(11, PRETO, b=True)},
         'userEnteredFormat.textFormat,userEnteredFormat.backgroundColorStyle,userEnteredFormat.borders'),
 'negr': ({'textFormat': _tf(10, PRETO, b=True)}, 'userEnteredFormat.textFormat'),
 'amarelo': ({'backgroundColorStyle': {'rgbColor': {'red': 1, 'green': .949, 'blue': .8}}},
             'userEnteredFormat.backgroundColorStyle'),
}


def formato(o):
    sid, L = o['sid'], o['lay']
    R = []
    def f(est, r0, r1, c0, c1):          # linhas 1-based inclusivas, colunas 0-based [c0, c1)
        fmt, campos = EST[est]
        R.append({'repeatCell': {'range': {'sheetId': sid, 'startRowIndex': r0 - 1, 'endRowIndex': r1,
                                           'startColumnIndex': c0, 'endColumnIndex': c1},
                                 'cell': {'userEnteredFormat': fmt}, 'fields': campos}})
    f('base', 3, max(160, o['nlin'] + 5), 1, 12)
    f('obs', 6, L['rcd'], 2, 3); f('dir', 6, L['rcd'], 3, 4); f('un', 6, L['rcd'], 4, 5)
    f('rs', 6, L['rcd'], 5, 6); f('pct', 6, L['rcd'], 6, 7)
    f('ital', L['rnota'], L['rnota'], 2, 3)
    f('cen', L['rhead_it'], L['rconf'], 1, 2); f('obs', L['rhead_it'], L['rconf'], 3, 4)
    f('rs', L['rhead_it'], L['rconf'], 8, 9)
    #   ⭐ as colunas das peças, numa faixa só do primeiro ao último item: nas
    #     linhas de cabeçalho de item essas colunas estão vazias, e o estilo
    #     específico delas vem depois e ganha
    B = L['blocos']; p0, p1 = B[0][0], B[-1][5]
    f('dir', p0, p1, 3, 6); f('un', p0, p1, 6, 7); f('rs', p0, p1, 7, 9); f('chave', p0, p1, 10, 11)
    f('obs', p0, p1, 2, 3)
    for rh, rc, rhd, l0, l1, rt in B:
        f('itemh', rh, rh, 1, 11); f('itemn', rh, rh, 1, 2); f('dir', rh, rh, 8, 9)
        f('ital', rc, rc, 2, 3)
    f('duvn', L['duv0'], L['duv1'], 1, 2)
    for r in (4, L['rsec_it'], L['rsec_fora'], L['rsec_pc'], L['rsec_nd']):
        f('secao', r, r, 1, 11)
    for r in [6, L['rhead_it']] + [b[2] for b in L['blocos']]:
        f('head', r, r, 1, 11)
    for r in [L['rcd'], L['rconf']] + [b[5] for b in L['blocos']]:
        f('tot', r, r, 1, 11)
    f('negr', L['rrat'], L['rrat'], 1, 11)
    f('amarelo', L['rfr'], L['rfr'], 3, 4)
    return R


if __name__ == '__main__':
    out = [monta(*a) for a in ABAS]
    for o in out:
        o['formato'] = formato(o)
    (P / '_abas.json').write_text(json.dumps(out, ensure_ascii=False), encoding='utf-8')
    tot_cd = 0
    for o in out:
        tot_cd += o['cd']
        print(f"{o['aba']:14s} {o['nlin']:3d} linhas · chapas {o['chapas']} · gavetas {o['gavetas']}")
        print(f"   custo direto R$ {o['cd']:,.2f} · partes {{{', '.join(f'{k}: {v:,.0f}' for k, v in o['partes'].items())}}}")
        for m, c in o['itens']: print(f"      {m:52s} R$ {c:,.2f}")
        print(f"      arredondamento de chapa R$ {o['arred']:,.2f}")
    print(f'TOTAL custo direto R$ {tot_cd:,.2f}')
