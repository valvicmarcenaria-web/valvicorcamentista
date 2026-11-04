# -*- coding: utf-8 -*-
"""ATTOS · Costa Laguna — GERA a aba de um ambiente, NO LAYOUT DA CASA.

⛔⛔ ESTE ARQUIVO FOI REESCRITO DEPOIS DE UM ERRO MEU, e o erro foi de
  método, não de conta. [Jonathan, 04/11/2026]
    > "a planilha do orcamento esta com configuracoes diferentes das demais"
    > "veja como é o layout das abas dos ambientes"
  Eu tinha inventado um layout. Funcionava, fechava no centavo — e era
  diferente de TODAS as outras planilhas da casa. ⭐ A lição não é "siga o
  padrão": é QUANDO O PEDIDO APONTA PARA UM DOCUMENTO, ABRA O DOCUMENTO.
  Bastava ter aberto uma aba do Gustavo Raposo antes de escrever a primeira
  linha. Em vez disso li o esqueleto da aba-modelo, que está incompleto, e
  completei de cabeça.

⭐ O QUE A CASA FAZ, lido célula a célula no orçamento do Gustavo Raposo:

  · PAINEL DE MATERIAL em SEIS colunas — B MATERIAL · C ESPECIFICAÇÃO ·
    D QUANTIDADE · E UN · F CUSTO · G % DO CUSTO. Sem coluna de FRETE e sem
    coluna de TOTAL: o frete é uma LINHA, e o valor dele vai em CUSTO.
  · A CHAPA SE CONTA INTEIRA EM CADA ABA, por cor × espessura. A sobra entre
    o rateio das peças (em fração) e a compra (em número cheio) aparece na
    linha "Arredondamento de chapa para número cheio".
  · A FERRAGEM É UMA LINHA SÓ — "Ferragem, terceirizados e iluminação" — e o
    custo dela é o RESTO: tudo que tem chave, menos chapa, menos acabamento,
    menos vidro. Assim nenhuma família nova escapa por eu não a ter listado.
  · CONSUMÍVEIS são 6% sobre chapa, fita E FILETAGEM.
  · O BLOCO DE PEÇAS É POR ITEM: faixa "ITEM nn", a descrição, o cabeçalho
    próprio, as peças, e "TOTAL DO ITEM nn". A chave da Base fica na coluna
    K, fora da tabela, e a coluna H mostra o R$ UN que veio da Base.
  · A FITA E A FILETAGEM SÃO LINHAS DE PEÇA dentro do item, com a metragem.
  · As DÚVIDAS são NUMERADAS: o número em B, o texto em C.

⛔ locale pt_BR: separador ';'. Nome de função em INGLÊS — a API normaliza.
⛔⛔ NUNCA UM DECIMAL DENTRO DE FÓRMULA: em pt_BR o literal é 0,01.

   uso:  python3 -I planilha.py Hall
         python3 -I planilha.py --todos
"""
import importlib.util, sys, pathlib, contextlib, io, json, re

P = pathlib.Path(__file__).resolve().parent


def _mod(nome, arq):
    s = importlib.util.spec_from_file_location(nome, P / arq)
    m = importlib.util.module_from_spec(s); sys.modules[nome] = m
    with contextlib.redirect_stdout(io.StringIO()): s.loader.exec_module(m)
    return m


b = _mod('b', 'base.py')
lv = _mod('lv', 'levantamento.py')
ch = _mod('ch', 'chaves.py')
cen = _mod('cen', 'cenarios.py')

ABAS = [('Hall', '01 Hall'), ('Jantar', '02 Jantar'), ('Cozinha', '03 Cozinha'),
        ('Gourmet', '04 Gourmet'), ('Escritório', '05 Escritório'),
        ('Sala de TV', '06 Sala de TV'), ('Suíte', '07 Suíte')]
SIDS = {'01': 101, '02': 102, '03': 103, '04': 104, '05': 105, '06': 106,
        '07': 107}

W, COLS = 10, 'BCDEFGHIJK'
PR = 'precos;2;FALSE'                    # ⭐ coluna B — o padrão da casa
ACAB = ['Fita cor', 'Filetagem automática', 'Filetagem manual']
VIDRO = ['Vidro reflecta prata com perfil']

NAO_MARCENARIA = [
 '⛔ PEDRA NUNCA É NOSSA. Neste projeto são 21 m² de TRAVERTINO ROMANO '
 'ESCOVADO: o painel da sala de jantar de 367 × 585, os 300 × 140 atrás da '
 'TV, os 190 × 64 atrás da bancada do escritório e o apoio da mesa.',
 '⛔ Também fora: louça, metal, eletrodoméstico, luminária, revestimento, '
 'móvel solto e box — box existe sem o móvel.',
 '⭐ MAS O VIDRO REFLECTA É NOSSO: 8 folhas de porta de cristaleira e de '
 'armário, dentro da marcenaria, no mesmo caminhão e na mesma equipe.',
 '⛔ REGRA DOS DOIS ESTADOS: ou o item é nosso COM VALOR na linha, ou está '
 'NOMEADO aqui como fora. Não existe terceiro estado.',
]
DUVIDAS = [
 '⛔⛔ NÃO HÁ UMA ÚNICA INDICAÇÃO DE LED NAS ONZE PRANCHAS — nem na '
 'cristaleira, nem no painel da TV, nem sob o armário da cozinha. '
 'Cristaleira sem luz é incomum. Ou o projeto não previu, ou vem por fora.',
 '⚠ O ACABAMENTO NÃO FOI ESCOLHIDO: a prancha diz "MDF AMADEIRADO A '
 'DEFINIR". Está orçado como Melamínico Fosco de cor, a chapa padrão da '
 'casa. Lâmina natural DOBRA a chapa.',
]
ESPEC = {
 'Fita cor': 'Aresta a aresta, mais 10% de desperdício',
 'Filetagem automática': 'Coladeira · 15 e 18 mm · serviço, sem desperdício',
 'Filetagem manual': '⛔ Ripa de 2 cm não entra na coladeira: vai à mão, a '
                     'R$ 5,00 — o dobro da automática',
}
ROTULO = {
 'Dobradiça': 'dobradiça', 'Dobradiça vidro': 'dobradiça de porta de vidro',
 'Corrediça Hettich': 'corrediça', 'Báscula HK-XS': 'articulador HK-XS',
 'Desempenador de porta': 'desempenador de porta',
 'Sistema de correr Dominus': 'sistema de correr',
 'Sistema pivô': 'sistema pivô', 'Alma de aço': 'alma de aço',
 'Suporte de prateleira': 'suporte de prateleira',
 'Cava usinada': 'cava usinada', 'Painel ripado': 'painel ripado',
}


def monta(amb, aba):
    moveis = [m for m in lv.M if m.amb == amb]
    assert moveis, f'⛔ ambiente sem móvel: {amb}'

    # ── que chaves este ambiente usa ────────────────────────────────────
    chapas, ferr = {}, {}
    for m in moveis:
        for k, ar in m.areas().items():
            chapas[f'{k[0]} {k[1]}'] = chapas.get(f'{k[0]} {k[1]}', 0) + ar
        for attr in ('ferr', 'terc', 'vidro'):
            for nome, q, _u in getattr(m, attr):
                k = ch.chave(nome)
                if k in ACAB:
                    continue
                ferr[k] = ferr.get(k, 0.0) + q
    cc = sorted(chapas, key=lambda k: -int(k.split()[-1]))
    tem_mao = any(m.fita_ripa > 0 for m in moveis)
    vid = [k for k in VIDRO if k in ferr]
    cf = sorted([k for k in ferr if k not in VIDRO],
                key=lambda k: -ferr[k] * ch.MOTOR[k][0])

    # ── 1 · O LAYOUT, antes de uma única fórmula ────────────────────────
    nmat = len(cc) + 2 + (1 if tem_mao else 0) + (1 if vid else 0) + 1 + 2 + 2 + 1
    L = {'tit': 1, 'sub': 2, 's_amb': 4, 'cab_mat': 6, 'mat0': 7}
    L['mat1'] = L['mat0'] + nmat - 1
    L['direto'] = L['mat1'] + 1
    L['nota'] = L['direto'] + 1
    L['s_it'] = L['nota'] + 2
    L['cab_it'] = L['s_it'] + 2
    L['it0'] = L['cab_it'] + 1
    L['it1'] = L['it0'] + len(moveis) - 1
    L['f0'] = L['it1'] + 2                      # as cinco linhas da casa
    L['s_ni'] = L['f0'] + 5 + 1
    L['ni0'] = L['s_ni'] + 2
    L['ni1'] = L['ni0'] + len(NAO_MARCENARIA) - 1
    L['s_pec'] = L['ni1'] + 2
    L['blk0'] = L['s_pec'] + 2

    # ── 2 · os blocos de item ───────────────────────────────────────────
    blocos, r = [], L['blk0']
    for i, m in enumerate(moveis, 1):
        faixa, desc, cab = r, r + 1, r + 2
        r += 3
        p0 = r
        linhas = []
        for pc in m.pecas:
            linhas.append(('peca', pc)); r += 1
        if m.fita:
            linhas.append(('acab', ('Fita cor', m.fita * b.FITA_PERDA, 'm')))
            r += 1
        if m.fita - m.fita_ripa > 1e-9:
            linhas.append(('acab', ('Filetagem automática',
                                    m.fita - m.fita_ripa, 'm'))); r += 1
        if m.fita_ripa > 1e-9:
            linhas.append(('acab', ('Filetagem manual', m.fita_ripa, 'm')))
            r += 1
        for attr in ('ferr', 'terc', 'vidro'):
            for item in getattr(m, attr):
                if ch.chave(item[0]) in ACAB:
                    continue
                linhas.append((attr, item)); r += 1
        blocos.append(dict(i=i, m=m, faixa=faixa, desc=desc, cab=cab,
                           p0=p0, p1=r - 1, tot=r, linhas=linhas))
        r += 2                                   # TOTAL DO ITEM + respiro
    L['blk1'] = r - 2
    a, z = L['blk0'], L['blk1']
    L['s_nt'] = L['blk1'] + 2
    L['nt0'] = L['s_nt'] + 2
    NOTAS = [f'⭐ {m.nome} — {m.nota}' for m in moveis if m.nota]
    L['nt1'] = L['nt0'] + len(NOTAS) - 1
    L['s_dv'] = L['nt1'] + 2
    L['dv0'] = L['s_dv'] + 2
    DUV = list(DUVIDAS) + [f'⚠ {k} — {ch.A_COTAR[k]}' for k in cc + vid + cf
                           if k in ch.A_COTAR]
    L['dv1'] = L['dv0'] + len(DUV) - 1
    L['fim'] = L['dv1']

    # ── 3 · A MATRIZ ────────────────────────────────────────────────────
    G = [[''] * W for _ in range(L['fim'])]

    def põe(row, **kw):
        for c, v in kw.items():
            G[row - 1][COLS.index(c)] = v

    AREA = f'VLOOKUP("Área da chapa";{PR})*VLOOKUP("Aproveitamento";{PR})'
    M2 = (lambda alvo: f'SUMPRODUCT(($K${a}:$K${z}={alvo})*IF(ISNUMBER('
                       f'$D${a}:$D${z});$D${a}:$D${z}*$E${a}:$E${z}*'
                       f'$F${a}:$F${z};0))/10000')
    SOMA_I = lambda alvo: f'SUMIF($K${a}:$K${z};{alvo};$I${a}:$I${z})'
    SOMA_F = lambda alvo: f'SUMIF($K${a}:$K${z};{alvo};$F${a}:$F${z})'

    põe(L['tit'], B=f'  VALVIC MARCENARIA        {aba[3:].upper()}')
    põe(L['sub'], B=f'  Attos · Costa Laguna · executivo vetorizado, 11 '
                    f'pranchas A3 · {len(moveis)} '
                    f'{"item" if len(moveis) == 1 else "itens"} de móvel · '
                    f'⛔ nenhuma cota saiu por texto: tudo foi lido ampliando '
                    f'a prancha')
    põe(L['s_amb'], B='  O AMBIENTE   ·   chapa 275 × 185 com 80% de '
                      'aproveitamento · e ela se conta em número cheio, por '
                      'cor × espessura')
    põe(L['cab_mat'], B='MATERIAL', C='ESPECIFICAÇÃO', D='QUANTIDADE', E='UN',
        F='CUSTO', G='% DO CUSTO')

    r, chapa_rows = L['mat0'], {}
    for k in cc:
        chapa_rows[k] = r
        põe(r, B=k,
            C=f'="Melamínico Fosco de cor · "&ROUND({M2(f"$B{r}")};1)&'
              f'" m² de peças"',
            D=f'=ROUNDUP({M2(f"$B{r}")}/({AREA}))', E='chapas',
            F=f'=D{r}*VLOOKUP($B{r};{PR})')
        r += 1
    L['acab0'] = r
    for k in ACAB[:2] + (['Filetagem manual'] if tem_mao else []):
        põe(r, B=k, C=ESPEC[k], D=f'={SOMA_F(chr(34)+k+chr(34))}', E='m',
            F=f'=D{r}*VLOOKUP($B{r};{PR})')
        r += 1
    L['acab1'] = r - 1
    if vid:
        põe(r, B='Vidro e espelho',
            C='Vidraçaria · reflecta prata com perfil preto · ⚠ PREMISSA: o '
              'executivo pede REFLECTA CRISTAL, que não existe na Base',
            D=f'={SOMA_F(chr(34)+vid[0]+chr(34))}', E='folhas',
            F=f'={SOMA_I(chr(34)+vid[0]+chr(34))}')
        r += 1
    rots = [ROTULO.get(k, k.lower()) for k in cf]
    frase = ', '.join(rots[:-1]) + (' e ' + rots[-1] if len(rots) > 1 else
                                    (rots[0] if rots else ''))
    põe(r, B='Ferragem, terceirizados e iluminação',
        C=(frase[:1].upper() + frase[1:] if frase else 'Nenhuma') +
          ' · linha Hettich · ⛔ sem iluminação: não há uma única indicação '
          'de LED nas onze pranchas',
        D='=' + ('+'.join(SOMA_F(f'"{k}"') for k in cf) if cf else '0'),
        E='peças',
        #   ⭐ o custo da ferragem é O RESTO: tudo que tem chave, menos
        #     chapa, menos acabamento, menos vidro. Família nova não escapa.
        F=f'={SOMA_I(chr(34)+"<>"+chr(34))}'
          + ''.join(f'-{SOMA_I(f"$B{chapa_rows[k]}")}' for k in cc)
          + ''.join('-' + SOMA_I(f'$B{rr}')
                    for rr in range(L['acab0'], L['acab1'] + 1))
          + (f'-{SOMA_I(chr(34)+vid[0]+chr(34))}' if vid else ''))
    L['ferr'] = r; r += 1
    põe(r, B='Corte · por chapa',
        C='Serviço de corte, por chapa comprada · R$ 2,00',
        D='=' + '+'.join(f'D{cr}' for cr in chapa_rows.values()), E='chapas',
        F=f'=D{r}*VLOOKUP("Corte por chapa";{PR})')
    r += 1
    põe(r, B='Corte · por peça',
        C='Serviço de corte, por peça cortada · R$ 2,50 · ⛔ conta a PEÇA, '
          'não a linha: uma linha de 4 prateleiras são 4 peças',
        D=f'=SUMPRODUCT((LEFT($K${a}:$K${z};4)="MDF ")*IF(ISNUMBER('
          f'$F${a}:$F${z});$F${a}:$F${z};0))', E='peças',
        F=f'=D{r}*VLOOKUP("Corte por peça";{PR})')
    r += 1
    põe(r, B='Consumíveis',
        C='Cola, lixa, parafuso, cavilha, tapa-furo, fundo e verniz · 6% '
          'sobre chapa, fita e filetagem',
        F=f'=SUM(F{L["mat0"]}:F{L["acab1"]})*VLOOKUP($B{r};{PR})')
    L['cons'] = r; r += 1
    põe(r, B='Embalagem', C='Papelão, filme e cantoneira · 2% sobre o subtotal',
        F=f'=SUM(F{L["mat0"]}:F{L["cons"]})*VLOOKUP($B{r};{PR})')
    r += 1
    põe(r, B='Frete',
        C='⭐ Frete do ambiente · R$ 200 a viagem · ⛔ A QUANTIDADE É SUA: '
          'digite quantas viagens este ambiente leva, e o frete aparece aqui '
          'e no Painel · sai ZERO e espera',
        D=0, E='viagem', F=f'=D{r}*VLOOKUP($B{r};{PR})')
    L['frete'] = r
    assert r == L['mat1'], f'⛔ layout: material em {r}, previsto {L["mat1"]}'

    d = L['direto']
    for i in range(L['mat0'], L['mat1'] + 1):
        põe(i, G=f'=IFERROR(F{i}/$F${d};"")')
    põe(d, B='CUSTO DIRETO DO AMBIENTE',
        F=f'=SUM(F{L["mat0"]}:F{L["mat1"]})', G=f'=IFERROR(F{d}/$F${d};"")')
    põe(L['nota'], C='⭐ O FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem: a '
                     'QUANTIDADE é a célula AMARELA no fim do painel de '
                     'material, e ela sai ZERO.   ⛔ Enquanto houver linha a '
                     'R$ 0,00 por falta de preço na Base, o custo deste '
                     'ambiente é um PISO, nunca um preço fechado.')

    # ── OS ITENS ────────────────────────────────────────────────────────
    põe(L['s_it'], B='  OS ITENS   ·   cada móvel com o seu custo, porque é '
                     'assim que a fábrica produz e o cliente confere')
    põe(L['cab_it'], B='ITEM', C='MÓVEL', D='MEDIDA GERAL', I='CUSTO')
    for x in blocos:
        põe(L['it0'] + x['i'] - 1, B=x['i'], C=x['m'].nome, D=x['m'].nota,
            I=f'=I{x["tot"]}')
    f0 = L['f0']
    põe(f0, B='Soma dos itens · chapa rateada em fração',
        I=f'=SUM(I{L["it0"]}:I{L["it1"]})')
    põe(f0 + 1, B='Arredondamento de chapa para número cheio · ⛔ a regra de '
                  'ferro',
        I='=' + '+'.join(f'F{cr}' for cr in chapa_rows.values())
          + ''.join(f'-{SOMA_I(f"$B{cr}")}' for cr in chapa_rows.values()))
    põe(f0 + 2, B='MATERIAL E FERRAGEM, PELO RATEIO DOS ITENS',
        I=f'=I{f0}+I{f0+1}')
    põe(f0 + 3, B='Material e ferragem, pelo painel do ambiente',
        I=f'=SUM(F{L["mat0"]}:F{L["ferr"]})')
    põe(f0 + 4, B='⭐ CONFERÊNCIA — as duas contas têm de dar a mesma coisa',
        I=f'=I{f0+2}-I{f0+3}')

    põe(L['s_ni'], B='  O QUE NÃO É MARCENARIA   ·   está na prancha, não '
                     'está nesta conta')
    for i, t in enumerate(NAO_MARCENARIA):
        põe(L['ni0'] + i, B=t)

    # ── AS PEÇAS, ITEM POR ITEM ─────────────────────────────────────────
    põe(L['s_pec'], B='  AS PEÇAS, ITEM POR ITEM   ·   cada linha é uma peça '
                      'que vai para o plano de corte')
    for x in blocos:
        #   ⭐ a MEDIDA GERAL é o primeiro segmento da nota; o resto é a
        #     descrição. Antes eu punha a nota inteira nos DOIS lugares, e a
        #     faixa do item repetia palavra por palavra a linha de baixo.
        med = re.split(r'\s+·\s+|,\s+|\s+—\s+', x['m'].nota or '—', 1)
        põe(x['faixa'], B=f'ITEM {x["i"]:02d}', C=x['m'].nome, I=med[0])
        põe(x['desc'], C=x['m'].nota or '—')
        põe(x['cab'], B='MATERIAL', C='ESPECIFICAÇÃO', D='C', E='L', F='QTD',
            G='UN', H='R$ UN', I='CUSTO', K='chave na Base')
        rr = x['p0']
        for tipo, item in x['linhas']:
            if tipo == 'peca':
                nome, Lc, Ac, esp, mat, qtd, fita_m, obs, mao = item
                k = f'{mat} {esp}'
                põe(rr, B=nome, C=obs or '—', D=round(Lc, 2), E=round(Ac, 2),
                    F=qtd, G='m²', H=f'=IFERROR(VLOOKUP($K{rr};{PR});"")',
                    I=f'=D{rr}*E{rr}*F{rr}/10000*H{rr}/({AREA})', K=k)
            elif tipo == 'acab':
                k, q, un = item
                põe(rr, B=k, C=ESPEC[k], F=round(q, 2), G=un,
                    H=f'=IFERROR(VLOOKUP($K{rr};{PR});"")',
                    I=f'=F{rr}*H{rr}', K=k)
            else:
                nome, q, _u = item
                k = ch.chave(nome)
                põe(rr, B=nome, C='—', F=round(q, 4), G=ch.MOTOR[k][1],
                    H=f'=IFERROR(VLOOKUP($K{rr};{PR});"")',
                    I=f'=F{rr}*H{rr}', K=k)
            rr += 1
        assert rr == x['p1'] + 1
        põe(x['tot'], B=f'TOTAL DO ITEM {x["i"]:02d}',
            I=f'=SUM(I{x["p0"]}:I{x["p1"]})')

    põe(L['s_nt'], B='  NOTAS E PONTOS EM ABERTO   ·   o que ainda precisa de '
                     'decisão antes de virar preço')
    for i, t in enumerate(NOTAS):
        põe(L['nt0'] + i, C=t)
    põe(L['s_dv'], B='  ⚠ DÚVIDAS DE ORÇAMENTO   ·   numeradas, para o senhor '
                     'responder em cima · nenhuma delas trava o preço')
    for i, t in enumerate(DUV):
        põe(L['dv0'] + i, B=i + 1, C=t)

    return G, L, blocos, chapa_rows, cc, cf


if __name__ == '__main__':
    alvos = [x for x in ABAS if sys.argv[1:] in ([], ['--todos'])
             or x[0] in sys.argv[1:]]
    linhas = cen.custo_por_ambiente('Hettich')
    tot = 0.0
    for amb, aba in alvos:
        G, L, blocos, cr, cc, cf = monta(amb, aba)
        (P / f'_aba-{aba.split()[0]}.json').write_text(
            json.dumps(G, ensure_ascii=False))
        tot += linhas[amb]['direto']
        print(f'{aba:<16} {L["fim"]:>4} linhas · {len(blocos)} itens · '
              f'peças {L["blk0"]}–{L["blk1"]} · motor R$ '
              f'{linhas[amb]["direto"]:>11,.2f} · '
              f'{len(json.dumps(G)) // 1024} KB')
    print(f'{"TOTAL":<16} {"":>34} R$ {tot:>11,.2f}')
