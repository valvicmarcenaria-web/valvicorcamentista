# -*- coding: utf-8 -*-
"""ATTOS · Costa Laguna — GERA a aba de um ambiente. Layout, texto e fórmula.

⭐⭐ A ABA NÃO SE FORMATA, ELA SE GERA. São sete ambientes, e o sétimo tem de
  sair igual ao primeiro sem eu lembrar de nada. Foi formatar à mão, duas
  vezes, que deixou a cozinha e o living do ICA diferentes em quinze pontos.

⛔ locale pt_BR: o separador de argumento é ';'. Nome de função vai em
  INGLÊS — a API normaliza. ⛔⛔ E NUNCA UM DECIMAL DENTRO DE FÓRMULA: em
  pt_BR o literal é 0,01 e a API recusa "0.01". `ROUND(x;2)<>0` diz o mesmo
  sem depender de locale.

⭐ O R$/m² JÁ VEM ARREDONDADO. O intervalo `chapa_m2`, no Painel, traz por padrão
  de chapa o R$/m² que sai da compra INTEIRA (29 chapas de MDF cor 15, não
  28,26). Assim cada peça custa a sua área × esse R$/m², e a soma das peças
  fecha EXATAMENTE com a chapa comprada — sem linha de "arredondamento"
  pendurada em lugar nenhum.

   uso:  python3 -I planilha.py Hall
         python3 -I planilha.py --todos
"""
import importlib.util, sys, pathlib, contextlib, io, json, math

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

CLIENTE = 'Attos · Costa Laguna · 11 pranchas A3 do executivo'
W = 10                                   # B..K
COLS = 'BCDEFGHIJK'
PRECO = 'precos;8;FALSE'                 # ⭐ coluna H: o PREÇO EFETIVO
NOTA_FIM = ('⛔ Enquanto houver linha a R$ 0,00 no painel de material acima, '
            'o custo deste ambiente é um PISO, nunca um preço fechado.')

NAO_MARCENARIA = [
 '⛔ PEDRA NUNCA É NOSSA. Neste projeto são 21 m² de TRAVERTINO ROMANO '
 'ESCOVADO: o painel da sala de jantar de 367 × 585, os 300 × 140 atrás da '
 'TV, os 190 × 64 atrás da bancada do escritório e o apoio da mesa. Fora do '
 'custo E fora da proposta.',
 '⛔ Também fora: louça, metal, eletrodoméstico, luminária, revestimento, '
 'móvel solto e box — box existe sem o móvel.',
 '⭐ MAS O VIDRO REFLECTA É NOSSO: são 8 folhas de porta de cristaleira e de '
 'armário, dentro da marcenaria, no mesmo caminhão e na mesma equipe.',
 '⛔ REGRA DOS DOIS ESTADOS: ou o item é nosso COM VALOR na linha, ou está '
 'NOMEADO aqui como fora. Não existe terceiro estado.',
]

DUVIDAS_GERAIS = [
 '⛔⛔ NÃO HÁ UMA ÚNICA INDICAÇÃO DE LED NAS ONZE PRANCHAS — nem na '
 'cristaleira, nem no painel da TV, nem sob o armário da cozinha. '
 'Cristaleira sem luz é incomum. Ou o projeto não previu, ou vem por fora.',
 '⚠ O ACABAMENTO NÃO FOI ESCOLHIDO: a prancha diz "MDF AMADEIRADO A '
 'DEFINIR". Está orçado como Melamínico Fosco de cor, a chapa padrão da '
 'casa. Lâmina natural DOBRA a chapa.',
]


def fmt(v):
    return v


# ════════════════════════════════════════════════════════════════════════
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
                if k in ('Filetagem manual',):      # já tem linha própria
                    continue
                ferr[k] = ferr.get(k, 0.0) + q
    chaves_chapa = sorted(chapas, key=lambda k: -int(k.split()[-1]))
    tem_mao = any(m.fita_ripa > 0 for m in moveis)
    # ⭐ ordem de PESO: a linha que manda no custo aparece primeiro
    chaves_ferr = sorted(ferr, key=lambda k: -ferr[k] * ch.MOTOR[k][0])

    # ── 1 · O LAYOUT, calculado antes de uma única fórmula ──────────────
    nmat = (len(chaves_chapa) + 2 + (1 if tem_mao else 0) + len(chaves_ferr)
            + 2 + 2 + 1)                 # +corte(2) +cons/emb(2) +frete(1)
    L = {'tit': 1, 'sub': 2, 's_amb': 4, 'cab_mat': 6}
    L['mat0'] = 7
    L['mat1'] = L['mat0'] + nmat - 1
    L['direto'] = L['mat1'] + 1
    L['nota'] = L['direto'] + 1
    L['s_it'] = L['nota'] + 2
    L['cab_it'] = L['s_it'] + 2
    L['it0'] = L['cab_it'] + 1
    L['it1'] = L['it0'] + len(moveis) - 1
    L['f0'] = L['it1'] + 2
    L['s_ni'] = L['f0'] + 5 + 1
    L['ni0'] = L['s_ni'] + 2
    L['ni1'] = L['ni0'] + len(NAO_MARCENARIA) - 1
    L['s_pec'] = L['ni1'] + 2
    L['cab_pec'] = L['s_pec'] + 2
    L['blk0'] = L['cab_pec'] + 1

    # ── 2 · o bloco de peças, para saber onde ele acaba ─────────────────
    blocos, r = [], L['blk0']
    for i, m in enumerate(moveis, 1):
        hdr = r; r += 1
        p0 = r
        linhas = []
        for pc in m.pecas:
            linhas.append(('peca', pc)); r += 1
        for attr in ('ferr', 'terc', 'vidro'):
            for item in getattr(m, attr):
                if ch.chave(item[0]) == 'Filetagem manual':
                    continue             # ⭐ a linha própria de filetagem já cobra
                linhas.append((attr, item)); r += 1
        blocos.append(dict(i=i, m=m, hdr=hdr, p0=p0, p1=r - 1, linhas=linhas))
    L['blk1'] = r - 1
    a, z = L['blk0'], L['blk1']
    L['s_nt'] = L['blk1'] + 2
    L['nt0'] = L['s_nt'] + 2

    notas = [m.nota for m in moveis if m.nota]
    NOTAS = [f'⭐ {m.nome} — {m.nota}' for m in moveis if m.nota]
    L['nt1'] = L['nt0'] + len(NOTAS) - 1
    L['s_dv'] = L['nt1'] + 2
    L['dv0'] = L['s_dv'] + 2
    DUV = list(DUVIDAS_GERAIS)
    for k in chaves_chapa + chaves_ferr:
        if k in ch.A_COTAR:
            DUV.append(f'⚠ {k} — {ch.A_COTAR[k]}')
    L['dv1'] = L['dv0'] + len(DUV) - 1
    L['fim'] = L['dv1']

    # ── 3 · A MATRIZ ────────────────────────────────────────────────────
    G = [[''] * W for _ in range(L['fim'])]

    def põe(row, **kw):
        for c, v in kw.items():
            G[row - 1][COLS.index(c)] = v

    M2 = (lambda alvo: f'SUMPRODUCT(($H${a}:$H${z}={alvo})*IF(ISNUMBER('
                       f'$D${a}:$D${z});$D${a}:$D${z}*$E${a}:$E${z}*'
                       f'$F${a}:$F${z};0))/10000')

    põe(L['tit'], B=f'  VALVIC MARCENARIA        {aba[3:].upper()}')
    põe(L['sub'], B=f'  {CLIENTE} · {len(moveis)} '
                    f'{"móvel" if len(moveis) == 1 else "móveis"} · '
                    f'{sum(len(x["linhas"]) for x in blocos)} linhas de peça e '
                    f'ferragem · ⛔ o executivo está TODO vetorizado: nenhuma '
                    f'cota saiu por texto, tudo foi lido ampliando a prancha')
    põe(L['s_amb'], B='  O AMBIENTE   ·   chapa 275 × 185 com 80% de '
                      'aproveitamento · ⭐ o R$/m² já vem do Painel com a '
                      'chapa arredondada para número cheio')
    põe(L['cab_mat'], B='MATERIAL', C='ESPECIFICAÇÃO', D='QUANTIDADE', E='UN',
        F='CUSTO', G='FRETE', H='TOTAL', I='% DO CUSTO')

    r = L['mat0']
    chapa_rows = {}
    for k in chaves_chapa:
        chapa_rows[k] = r
        põe(r, B=k,
            C=f'="Melamínico Fosco de cor · "&ROUND(D{r}*VLOOKUP($B{r};chapa_m2;3;'
              f'FALSE);2)&" chapas, em fração da compra do projeto"',
            D=f'={M2(f"$B{r}")}', E='m² de peças',
            F=f'=D{r}*VLOOKUP($B{r};chapa_m2;2;FALSE)')
        r += 1
    L['fita'] = r
    põe(r, B='Fita cor',
        C='22 mm na cor da frente · declarada aresta a aresta na peça, mais os '
          '10% de desperdício que a própria Base manda somar',
        D=f'=(SUM($J${a}:$J${z})+SUM($K${a}:$K${z}))*VLOOKUP('
          f'"Desperdício de fita";{PRECO})', E='m',
        F=f'=D{r}*VLOOKUP($B{r};{PRECO})')
    r += 1
    põe(r, B='Filetagem automática',
        C='Coladeira · peça de 15 e 18 mm · ⭐ serviço por metro de aresta '
          'feita, sem desperdício',
        D=f'=SUM($J${a}:$J${z})', E='m',
        F=f'=D{r}*VLOOKUP($B{r};{PRECO})')
    r += 1
    if tem_mao:
        põe(r, B='Filetagem manual',
            C='⛔ RIPA NÃO ENTRA NA COLADEIRA: vai à mão, a R$ 5,00 — o dobro '
              'da automática. ⭐ E é o maior metro deste projeto',
            D=f'=SUM($K${a}:$K${z})', E='m',
            F=f'=D{r}*VLOOKUP($B{r};{PRECO})')
        r += 1
    for k in chaves_ferr:
        v, un, _imp = ch.MOTOR[k]
        põe(r, B=k, C=ESPEC.get(k, ''),
            D=f'=SUMIF($H${a}:$H${z};$B{r};$F${a}:$F${z})', E=un,
            F=f'=D{r}*VLOOKUP($B{r};{PRECO})')
        r += 1
    L['ult_mat'] = r - 1
    põe(r, B='Corte por chapa',
        C='Serviço de corte, por chapa COMPRADA · ⭐ a chapa deste ambiente é '
          'a sua fração da compra do projeto, nunca um arredondamento próprio',
        D='=' + '+'.join(f'D{cr}*VLOOKUP($B{cr};chapa_m2;3;FALSE)'
                         for cr in chapa_rows.values()), E='chapas',
        F=f'=D{r}*VLOOKUP($B{r};{PRECO})')
    r += 1
    põe(r, B='Corte por peça',
        C='⛔ Conta a PEÇA, não a linha: uma linha de 4 prateleiras são 4 '
          'peças na serra, e a serra cobra por peça',
        D=f'=SUMPRODUCT((LEFT($H${a}:$H${z};4)="MDF ")*IF(ISNUMBER('
          f'$F${a}:$F${z});$F${a}:$F${z};0))', E='peças',
        F=f'=D{r}*VLOOKUP($B{r};{PRECO})')
    r += 1
    põe(r, B='Consumíveis',
        C='Cola, lixa, parafuso, cavilha, tapa-furo, fundo e verniz · 6% sobre '
          'CHAPA E FITA · ⛔ a filetagem fica FORA: é serviço de coladeira, '
          'não material, e cola não se gasta por metro de aresta',
        #   ⛔⛔ E ESTA FÓRMULA JÁ ESTEVE ERRADA: somava até a linha de
        #     filetagem, enquanto o motor em Python somava só chapa e fita.
        #     A Base diz, com todas as letras, "6% sobre chapa e fita".
        F=f'=SUM(H{L["mat0"]}:H{L["fita"]})*VLOOKUP($B{r};{PRECO})')
    L['cons'] = r; r += 1
    põe(r, B='Embalagem', C='Papelão, filme e cantoneira · 2% sobre o subtotal',
        F=f'=SUM(H{L["mat0"]}:H{L["cons"]})*VLOOKUP($B{r};{PRECO})')
    r += 1
    põe(r, B='Frete',
        C='⭐ R$ 200 a viagem · ⛔ A QUANTIDADE É SUA: digite quantas viagens '
          'este ambiente leva e o frete aparece aqui e no Painel · a única '
          'célula amarela da aba, e ela sai ZERO e espera',
        D=0, E='viagem', G=f'=D{r}*VLOOKUP($B{r};{PRECO})')
    L['frete'] = r
    assert r == L['mat1'], f'⛔ layout: material acabou em {r}, previsto {L["mat1"]}'

    for i in range(L['mat0'], L['mat1'] + 1):
        põe(i, H=f'=F{i}+G{i}', I=f'=IFERROR(H{i}/$H${L["direto"]};"")')
    d = L['direto']
    põe(d, B='CUSTO DIRETO DO AMBIENTE',
        F=f'=SUM(F{L["mat0"]}:F{L["mat1"]})',
        G=f'=SUM(G{L["mat0"]}:G{L["mat1"]})',
        H=f'=SUM(H{L["mat0"]}:H{L["mat1"]})', I=f'=IFERROR(H{d}/$H${d};"")')
    põe(L['nota'], C=NOTA_FIM)

    # ── OS ITENS ────────────────────────────────────────────────────────
    põe(L['s_it'], B='  OS ITENS   ·   cada item é um móvel, e é assim que '
                     'ele vai para a proposta')
    põe(L['cab_it'], B='ITEM', C='MÓVEL', D='MEDIDA GERAL', I='CUSTO')
    for x in blocos:
        põe(L['it0'] + x['i'] - 1, B=x['i'], C=x['m'].nome, D=x['m'].nota,
            I=f'=I{x["hdr"]}')
    f0 = L['f0']
    põe(f0, B='Soma dos itens', I=f'=SUM(I{L["it0"]}:I{L["it1"]})')
    põe(f0 + 1, B='Material e ferragem, pelo painel do ambiente',
        I=f'=SUM(F{L["mat0"]}:F{L["ult_mat"]})')
    põe(f0 + 2, B='⭐ CONFERÊNCIA INTERNA — as duas contas acima têm de dar a '
                  'mesma coisa', I=f'=I{f0}-I{f0+1}')
    põe(f0 + 3, B='⭐⭐ O QUE O MOTOR EM PYTHON CALCULOU para este ambiente '
                  '(custo direto, linha Hettich)', I=None)   # preenchido fora
    põe(f0 + 4, B='⭐⭐ CONFERÊNCIA CONTRA O MOTOR — ⛔ esta é a que importa: a '
                  'de cima compara a aba com ela mesma, e uma chave que a '
                  'Base não tem passa por ela sem acusar nada',
        I=f'=H{d}-I{f0+3}')

    põe(L['s_ni'], B='  O QUE NÃO É MARCENARIA   ·   está na prancha, não '
                     'está nesta conta')
    for i, t in enumerate(NAO_MARCENARIA):
        põe(L['ni0'] + i, B=t)

    # ── AS PEÇAS ────────────────────────────────────────────────────────
    põe(L['s_pec'], B='  AS PEÇAS, ITEM POR ITEM   ·   cada linha é uma peça '
                      'que vai para o plano de corte')
    põe(L['cab_pec'], B='PEÇA', C='OBSERVAÇÃO', D='C (cm)', E='L (cm)',
        F='QTD', G='UN', H='CHAVE DA BASE', I='CUSTO', J='FITA MÁQ (m)',
        K='FITA MÃO (m)')
    for x in blocos:
        p0, p1 = x['p0'], x['p1']
        fita = (f'(SUM(J{p0}:J{p1})+SUM(K{p0}:K{p1}))*VLOOKUP('
                f'"Desperdício de fita";{PRECO})*VLOOKUP("Fita cor";{PRECO})'
                f'+SUM(J{p0}:J{p1})*VLOOKUP("Filetagem automática";{PRECO})'
                f'+SUM(K{p0}:K{p1})*VLOOKUP("Filetagem manual";{PRECO})')
        põe(x['hdr'], B=f'{x["i"]}. {x["m"].nome}', C=x['m'].nota,
            I=f'=SUM(I{p0}:I{p1})+{fita}')
        rr = p0
        for tipo, item in x['linhas']:
            if tipo == 'peca':
                nome, Lc, Ac, esp, mat, qtd, fita_m, obs, mao = item
                k = f'{mat} {esp}'
                #   ⭐ a largura da ripa sai de 2 × n × 1,10 e traz ruído de
                #     ponto flutuante — 332,20000000000005. Arredondar aqui é
                #     a TELA arredondando, que é onde se arredonda.
                põe(rr, B=nome, C=obs, D=round(Lc, 2), E=round(Ac, 2),
                    F=qtd, G='m²', H=k,
                    I=f'=D{rr}*E{rr}*F{rr}/10000*VLOOKUP($H{rr};chapa_m2;2;FALSE)',
                    **{('K' if mao else 'J'): round(fita_m * qtd, 4)} if fita_m else {})
            else:
                nome, q, _u = item
                k = ch.chave(nome)
                põe(rr, B=nome, F=round(q, 4), G=ch.MOTOR[k][1], H=k,
                    I=f'=F{rr}*VLOOKUP($H{rr};{PRECO})')
            rr += 1
        assert rr == p1 + 1

    põe(L['s_nt'], B='  AS NOTAS   ·   o que a leitura da prancha ensinou, e '
                     'que a próxima pessoa precisa saber')
    for i, t in enumerate(NOTAS):
        põe(L['nt0'] + i, B=t)
    põe(L['s_dv'], B='  AS DÚVIDAS   ·   ⛔ cada uma é dinheiro parado')
    for i, t in enumerate(DUV):
        põe(L['dv0'] + i, B=t)

    return G, L, blocos, chapa_rows, chaves_chapa, chaves_ferr


ESPEC = {
 'Dobradiça': '⭐ Hettich e Blum custam o MESMO, R$ 50 · a dobradiça não é o '
              'que separa as duas linhas',
 'Dobradiça vidro': '⚠ A COTAR na Base, faixa de 30 a 85 · ⛔ é outro produto, '
                    'fora da escada de linha',
 'Corrediça Hettich': '⭐ Quadro V6, oculta, 30 kg · ⛔ É A ÚNICA FERRAGEM DE '
                      'GAVETA QUE MUDA DE LINHA: na Blum são R$ 300',
 'Báscula HK-XS': '⭐ Blum AVENTOS HK-XS, de molas · ⛔ não é a gás',
 'Desempenador de porta': '⭐⭐ Padrão em TODA porta deslizante · folha de 70 cm '
                          'ou mais leva DOIS',
 'Sistema de correr Dominus': '⭐ [Jonathan] Rometal R$ 600 na Hettich, SI Forma '
                              'R$ 900 na Blum · ⚠ a Base diz "2 portas"',
 'Sistema pivô': 'Só o sistema, sem a folha',
 'Alma de aço': '⭐ Prateleira de vão acima de 1,20 m · contra FLECHA, não '
                'contra empeno',
 'Suporte de prateleira': '⭐ [Jonathan] Toda prateleira INTERNA leva composição '
                          'de 4 · ⛔ NÃO é o suporte oculto de R$ 30',
 'Cava usinada': 'Por metro de frente · ⚠ a Base briga consigo: R$ 50/m em '
                 'Ferragens e R$ 25/m em Terceirizados',
 'Painel ripado': '⭐ O ITEM DESTE PROJETO · ripa de 2 cm, vão de 1, passo de 3 '
                  '· ⚠ R$ 180/m² numa faixa de 70 a 420',
 'Vidro reflecta prata com perfil': '⚠ PREMISSA: o executivo pede REFLECTA '
                                    'CRISTAL e esse padrão não existe na Base',
}

if __name__ == '__main__':
    alvos = [x for x in ABAS if sys.argv[1:] in ([], ['--todos'])
             or x[0] in sys.argv[1:]]
    linhas = cen.custo_por_ambiente('Hettich')
    tot = 0.0
    for amb, aba in alvos:
        G, L, blocos, cr, cc, cf = monta(amb, aba)
        # ⭐ o número do motor entra na linha de conferência
        G[L['f0'] + 2][COLS.index('I')] = round(linhas[amb]['direto'], 2)
        tot += linhas[amb]['direto']
        out = P / f'_aba-{aba.split()[0]}.json'
        out.write_text(json.dumps(G, ensure_ascii=False))
        print(f'{aba:<16} {L["fim"]:>4} linhas · {len(blocos)} móveis · '
              f'peças {L["blk0"]}–{L["blk1"]} · motor R$ '
              f'{linhas[amb]["direto"]:>11,.2f} · {len(json.dumps(G)) // 1024} KB')
    print(f'{"TOTAL":<16} {"":>4}          {"":>9}              '
          f'       R$ {tot:>11,.2f}')
