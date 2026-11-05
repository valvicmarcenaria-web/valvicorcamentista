# -*- coding: utf-8 -*-
"""ANA CAROLINA E ANDRÉ — GERA as abas de ambiente no LAYOUT DA CASA (o do
Gustavo Raposo, lido célula a célula em '04 Despensa'):
  painel de material B..G com fórmulas que leem as peças pela CHAVE (coluna K)
  · os itens com conferência · o que não é marcenaria · as peças por item com
  R$ UN = VLOOKUP(chave; precos) · notas e dúvidas numeradas.
E calcula aqui, com os preços da Base de 05/11/2026, o que a planilha TEM de
mostrar depois que o IMPORTRANGE for autorizado — é a conferência dela.

⛔ locale pt_BR: separador ';' · nome de função em inglês · nada de decimal
   literal dentro de fórmula.
uso: python3 -I planilha.py  → grava _abas.json e imprime o resumo
"""
import json, math, sys, pathlib
P = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(P)); sys.path.insert(0, str(P.parent))
import levantamento as L
import motor_mc as MC

PRECO = {'MDF cor 18': 700, 'MDF cor 15': 550, 'MDF cor 6': 350, 'MDF Branco TX 18': 400,
         'MDF Branco TX 15': 350, 'MDF Branco TX 6': 250, 'Fita cor': 3, 'Fita Branco TX': 2,
         'Filetagem automática': 2.5, 'Corrediça': 300, 'Suporte de prateleira': 6.5,
         'Cabideiro': 120, 'Sistema de correr Dominus': 800, 'Trilho Dominus 2 m': 350,
         'Desempenador de porta': 100, 'Perfil de proteção de piso': 15, 'Cava usinada': 50,
         'Corte por chapa': 2, 'Corte por peça': 2.5, 'Frete': 200}
AREA, APROV, CONS, EMB = 5.0875, 0.80, 0.06, 0.02
ABAS = [('Suíte master', '01 Suíte master', 101, 'SUITE MASTER_E1'),
        ('Closet suíte master', '02 Closet suíte master', 102, 'CLOSET SUITE MASTER_E1 e E2'),
        ('Quarto Gabriel', '03 Quarto Gabriel', 103, 'QUARTO GABRIEL · ELEVAÇÃO E1'),
        ('Closet Isabella', '04 Closet Isabella', 104, 'CLOSET ISABELLA · ELEVAÇÃO E01 e E2')]
SUB = {
 'Suíte master': 'roupeiro de 200 na parede da entrada, dois módulos — cabideiro longo e sete nichos — atrás de portas de correr',
 'Closet suíte master': 'closet aberto em duas paredes, do piso a 265 · ⭐ dez gavetas e sapateiras, o teto que o Jonathan deu',
 'Quarto Gabriel': 'a única prancha COTADA do projeto · roupeiro de 195 com maleiro, cabideiro e oito gavetas e sapateiros, atrás de portas de correr',
 'Closet Isabella': 'closet aberto em duas paredes · seis colunas, quatorze gavetas e sapateiros',
}
FORA = {
 'Suíte master': ['A bancada de 386 × 30 sob a janela, as duas mesinhas de 60 × 50 e o painel de cabeceira APARECEM SÓ NA PLANTA, sem elevação: estão fora desta conta e entraram nas dúvidas',
                  'Banho da suíte: bancada, cubas, box, louças e metais — pedra e louça nunca são nossas',
                  'Cama, poltrona e cadeira'],
 'Closet suíte master': ['Portas de passagem do closet (60 × 210)', 'Iluminação de forro'],
 'Quarto Gabriel': ['Berço, poltrona, cômoda e cama EXISTENTES', 'Porta de passagem e ar-condicionado'],
 'Closet Isabella': ['O QUARTO da Isabella — cama montessori, cômoda, estante, nicho de livros, quadro de desenho e puff — está na planta mas não tem elevação: fora desta conta',
                     'Banho: bancada, cuba, box, louças e metais'],
}
COMUNS = [
 '⛔ AS ELEVAÇÕES NÃO TÊM COTA NEM NOTA DE MATERIAL (só a do Quarto Gabriel é cotada). Largura e profundidade vêm da planta; ALTURAS E DIVISÕES foram MEDIDAS NA ESCALA 1:25. Conferir na medição.',
 '⚠ ACABAMENTO SEM ESPECIFICAÇÃO: orçado como MELAMÍNICO DE COR (chave MDF cor) em tudo que se vê, e Branco TX dentro dos roupeiros com porta. Lâmina natural dobra a chapa.',
]
DUV = {
 'Suíte master': ['⚠ A FRENTE DO ROUPEIRO NÃO ESTÁ DESENHADA. Pelos 65 de profundidade, orçado com DUAS PORTAS DE CORRER no sistema Dominus. Se forem portas de giro, troca o sistema por dobradiças Blum.',
                  '⛔ BANCADA, MESINHAS E CABECEIRA da planta não têm elevação nem nota. Se entram, preciso das vistas.',
                  '⚠ O MÓDULO DA DIREITA tem sete compartimentos com frente desenhada por dentro — lidos como NICHOS COM PRATELEIRA. Se forem gavetas, são seis corrediças Blum a mais.'],
 'Closet suíte master': ['⭐ DEZ GAVETAS E SAPATEIRAS [Jonathan, 05/11/2026]: a E1 desenha três gavetas; distribuí dez — três sapateiras no módulo 1, quatro gavetas no módulo 3 e três sapateiras no módulo A da E2. Cada uma leva corrediça Blum.',
                         '⚠ CLOSET ABERTO, SEM PORTAS: a prancha não desenha frente. Se tiver porta, entra sistema e folha.',
                         '⚠ BASE E TETO DE 331 NÃO SAEM DE CHAPA: emenda sobre a divisória do meio.'],
 'Quarto Gabriel': ['⚠ A FRENTE DO ROUPEIRO NÃO ESTÁ DESENHADA. Pelos 65 de profundidade, orçado com DUAS PORTAS DE CORRER Dominus.',
                    '⚠ SAPATEIRO lido como GAVETA BAIXA com corrediça Blum, igual à gaveta. Se for prateleira inclinada fixa, saem quatro corrediças.'],
 'Closet Isabella': ['⚠ AS COLUNAS 3 E 4 DA E2 estão desenhadas com CONTORNO PRETO, diferente das outras. Se forem portas, entra frente e dobradiça Blum.',
                     '⚠ BASE E TETO DE 281 NÃO SAEM DE CHAPA: emenda sobre a divisória do meio.'],
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
    put(2, f'  Ana Carolina e André · projeto [35] de Ana Maria, prancha {prancha} · {SUB[amb]}')
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
            put(rr, k, ('22 mm na caixaria · R$ 2,00 o metro' if 'Branco' in k else '22 mm nas peças de cor · R$ 3,00 o metro') + ' · mais 10% de desperdício',
                f'=SUMIF({K};"{k}";{F_})', 'm', f'=D{rr}*VLOOKUP("{k}";precos;2;FALSE)', f'=IFERROR(F{rr}/$F${rcd};"")')
        else:
            put(rr, k, 'Coladeira · 15 e 18 mm · serviço por metro de aresta feita, sem desperdício',
                f'=SUMIF({K};"{k}";{F_})', 'm', f'=D{rr}*VLOOKUP("{k}";precos;2;FALSE)', f'=IFERROR(F{rr}/$F${rcd};"")')
    put(rf, 'Ferragem, terceirizados e iluminação', 'Linha BLUM · corrediça, sistema de correr, desempenador, cabideiro, suporte, cava e perfil de piso · o resto de tudo que tem chave',
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
    put(rfr, 'Frete', '⭐ R$ 200 a viagem · a QUANTIDADE é digitada: uma viagem por ambiente', 1, 'viagem',
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
            else:
                ferr += q * PRECO[k]; c_it += q * PRECO[k]
        it_custo.append(c_it)
    nch = {k: math.ceil(a / (AREA * APROV)) for k, a in area.items()}
    c_ch = sum(nch[k] * PRECO[k] for k in nch); c_ft = sum(q * PRECO[k] for k, q in ftot.items())
    corte = sum(nch.values()) * 2 + npc * 2.5
    cons = (c_ch + c_ft) * CONS
    emb = (c_ch + c_ft + ferr + corte + cons) * EMB
    cd = c_ch + c_ft + ferr + corte + cons + emb + 200
    linhas = [[R.get(x, [''] * 10)[j] for j in range(10)] for x in range(1, r + 1)]
    pblocos = [(rl[0], rl[-1]) for *_, rl, rt in pos]
    FH = '=IFERROR(VLOOKUP($K{r};precos;2;FALSE);"")'
    FI = ('=IFERROR(IF(LEFT($K{r};4)="MDF ";$D{r}*$E{r}/10000*$F{r}/(' + CH + ')*$H{r};'
          'IF($D{r}="";$F{r}*$H{r};$D{r}*$E{r}/10000*$F{r}*$H{r}));"")')
    kinds = {'secao': [1 + x for x in (rsec_it, rsec_fora, rsec_pc, rsec_nd, 4)] and [rsec_it, rsec_fora, rsec_pc, rsec_nd, 4],
             'head': [6, rhead_it] + [p[5] for p in pos],
             'tot': [rcd, rconf] + [p[7] for p in pos],
             'item': [p[3] for p in pos], 'frete': [rfr], 'nlin': r}
    return dict(amb=amb, aba=aba, sid=sid, linhas=linhas, nlin=r, pblocos=pblocos, FH=FH, FI=FI, kinds=kinds, chapas=nch, cd=cd,
                partes=dict(chapa=c_ch, fita=c_ft, ferr=ferr, corte=corte, cons=cons, emb=emb, frete=200),
                itens=[(i['movel'], c) for (n, i, *_), c in zip(pos, it_custo)],
                arred=c_ch - sum(chapa_custo(x[3], x[4], x[5], x[7]) for _, lin in blocos for x in lin if x[0] == 'peca'),
                gavetas=sum(f[2] for i in itens for f in i['ferr'] if f[4] == 'Corrediça'))


if __name__ == '__main__':
    out = [monta(*a) for a in ABAS]
    (P / '_abas.json').write_text(json.dumps(out, ensure_ascii=False), encoding='utf-8')
    B = MC.base(0, rt=True, vendedor=False); MCA = 0.45
    tot_cd = tot_pv = 0
    for o in out:
        pv = o['cd'] / (B - MCA); tot_cd += o['cd']; tot_pv += pv
        print(f"{o['aba']:24s} {o['nlin']:3d} linhas · chapas {o['chapas']} · gavetas {o['gavetas']}")
        print(f"   custo direto R$ {o['cd']:,.2f} · preço a MC 45% (base {B*100:.2f}%) R$ {pv:,.2f} · partes {{{', '.join(f'{k}: {v:,.0f}' for k, v in o['partes'].items())}}}")
        for m, c in o['itens']: print(f"      {m:40s} R$ {c:,.2f}")
        print(f"      arredondamento de chapa R$ {o['arred']:,.2f}")
    print(f'TOTAL custo R$ {tot_cd:,.2f} · preço R$ {tot_pv:,.2f}')
