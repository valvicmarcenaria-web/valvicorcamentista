# -*- coding: utf-8 -*-
"""O FORMATO VISUAL DA PLANILHA DA CASA, linha por linha.

⭐ Este módulo é MAQUINÁRIO DA CASA, não orçamento de ninguém: os tokens
  saíram da aba-modelo (`Valvic · PLANILHA BASE`, aba "00 Ambiente"), lidos
  célula a célula. Copiado para cá para que o projeto seja autocontido.


⭐⭐ A ORGANIZAÇÃO VISUAL É PARTE DA ENTREGA, não enfeite [Jonathan,
  06/11/2026]: "a organização visual da planilha é de extrema importância
  pra mim". Eu tinha colado o conteúdo com `pasteData` por cima de uma aba
  duplicada — e **pasteData não leva formato**. O conteúdo ficou certo e a
  página ficou crua: cabeçalho sem fundo, dinheiro sem R$, percentual sem %,
  nota do mesmo tamanho do dado. Era isso a "desconformidade visual".

⭐ OS TOKENS SAÍRAM DA PRÓPRIA ABA-MODELO deste arquivo, lidos célula a
  célula, não inventados:

    fonte        Arial 10, #1A1A1A, à esquerda, centro vertical, CLIP
    colunas      A 28 · B 300 · C 430 · D a K 100
    página       congela 2 linhas · sem linhas de grade
    título       B1:K1 unido · fundo #1A1A1A · Arial 16 bold · branco
    subtítulo    B2:K2 unido · Arial 9 · #6B6B6B · quebra linha
    seção        B:K unido · Arial 11 bold · borda EMBAIXO
    cab. tabela  fundo #F7F7F7 · Arial 8 bold · #6B6B6B
    total        Arial 11 bold · borda EM CIMA
    nota         Arial 9 · #6B6B6B · quebra linha
    campo seu    fundo #FFF2CC · bold · à direita
    dinheiro     "R$" #,##0.00 · à direita
    percentual   0.0% · à direita
"""
import json, pathlib, sys

AQUI = pathlib.Path(__file__).resolve().parent

TINTA = {'red': 0.101960786, 'green': 0.101960786, 'blue': 0.101960786}
CINZA = {'red': 0.41960785, 'green': 0.41960785, 'blue': 0.41960785}
BRANCO = {'red': 1.0, 'green': 1.0, 'blue': 1.0}
FUNDO_CAB = {'red': 0.96862745, 'green': 0.96862745, 'blue': 0.96862745}
AMARELO = {'red': 1.0, 'green': 0.9490196, 'blue': 0.8}
MOEDA = {'type': 'CURRENCY', 'pattern': '"R$" #,##0.00'}
PCT = {'type': 'PERCENT', 'pattern': '0.0%'}
N0 = {'type': 'NUMBER', 'pattern': '0'}
N2 = {'type': 'NUMBER', 'pattern': '0.00'}
N3 = {'type': 'NUMBER', 'pattern': '0.000'}
#   ⭐ QUATRO CASAS para rendimento e área: é com a quarta casa que a
#     divisão área ÷ rendimento cai do lado certo do ROUNDUP. Exibir
#     duas esconderia a precisão que a conta usa.
N4 = {'type': 'NUMBER', 'pattern': '0.0000'}
# ⭐ LIDAS CÉLULA A CÉLULA DA ABA-MODELO DA CASA, 06/11/2026 · não são escolha
# minha: a SEÇÃO leva um fio PRETO embaixo, e o TOTAL uma barra DOURADA GROSSA
# em cima. Eu havia posto fio cinza nos dois, e as nove abas saíram diferentes
# do Painel e da aba Preço e Comissões, que já seguiam o modelo.
DOURADO = {'red': 0.68235296, 'green': 0.5137255, 'blue': 0.22745098}
BORDA = {'bottom': {'style': 'SOLID', 'width': 1,
                    'colorStyle': {'rgbColor': dict(TINTA)}},
         'top': {'style': 'SOLID_THICK', 'width': 3,
                 'colorStyle': {'rgbColor': DOURADO}}}


def mini(sid, r0, r1, c0, c1, **f):
    """⭐ Um pedido de formato com `fields` MÍNIMO — só o que muda.

    ⛔ O `estilo()` acima manda sempre fontFamily, tamanho, negrito e cor
      juntos, porque `fields` lista o grupo `textFormat` inteiro. Isso faz
      cada pedido pesar quatro vezes mais do que precisa, e o lote de
      formato desta aba passava de 100 KB em 132 pedidos. ⭐ Aqui cada
      chave vira o seu próprio caminho em `fields`, então pedir só
      `numberFormat` manda só `numberFormat`."""
    u, campos = {}, []
    if 'nf' in f:
        u['numberFormat'] = f['nf']; campos.append('numberFormat')
    if 'h' in f:
        u['horizontalAlignment'] = f['h']
        campos.append('horizontalAlignment')
    if 'w' in f:
        u['wrapStrategy'] = f['w']; campos.append('wrapStrategy')
    if 'bg' in f:
        u['backgroundColorStyle'] = {'rgbColor': dict(f['bg'])}
        campos.append('backgroundColorStyle')
    t = {}
    if 'fs' in f:
        t['fontSize'] = f['fs']; campos.append('textFormat.fontSize')
    if 'b' in f:
        t['bold'] = f['b']; campos.append('textFormat.bold')
    if 'fg' in f:
        t['foregroundColorStyle'] = {'rgbColor': dict(f['fg'])}
        campos.append('textFormat.foregroundColorStyle')
    if t:
        u['textFormat'] = t
    if 'lado' in f:
        u['borders'] = {f['lado']: {
            'style': 'SOLID_THICK' if f['lado'] == 'top' else 'SOLID',
            'width': 3 if f['lado'] == 'top' else 1,
            'colorStyle': {'rgbColor': dict(DOURADO if f['lado'] == 'top'
                                            else TINTA)}}}
        campos.append('borders')
    return {'repeatCell': {
        'range': {'sheetId': sid, 'startRowIndex': r0, 'endRowIndex': r1,
                  'startColumnIndex': c0, 'endColumnIndex': c1},
        'cell': {'userEnteredFormat': u},
        'fields': ','.join('userEnteredFormat.' + c for c in campos)}}


def fmt(**k):
    f = {'textFormat': dict(fontFamily='Arial',
                            fontSize=k.get('fs', 10),
                            bold=k.get('b', False),
                            foregroundColorStyle={'rgbColor': k.get('fg', TINTA)}),
         'horizontalAlignment': k.get('h', 'LEFT'),
         'verticalAlignment': 'MIDDLE',
         'wrapStrategy': k.get('w', 'CLIP')}
    if 'bg' in k:
        f['backgroundColorStyle'] = {'rgbColor': k['bg']}
    if 'nf' in k:
        f['numberFormat'] = k['nf']
    if 'borda' in k:
        f['borders'] = {k['borda']: BORDA[k['borda']]}
    return f


#   ⛔⛔ AQUI ESTAVA O DESPERDÍCIO. A primeira versão mandava o formato
#     INTEIRO em cada pedido, com a lista de campos escrita por extenso:
#     685 pedidos, 400 KB. ⭐ Mandando só a PROPRIEDADE QUE MUDA — e por
#     seção inteira em vez de faixa a faixa — o mesmo resultado cabe num
#     quarto disso. Célula vazia receber formato de número não aparece.
F_TUDO = 'userEnteredFormat'
F_NUM = 'userEnteredFormat.numberFormat,userEnteredFormat.horizontalAlignment'
F_TXT = 'userEnteredFormat.textFormat'
F_BG = 'userEnteredFormat.backgroundColorStyle'
F_BORDA = 'userEnteredFormat.borders'
F_QUEBRA = 'userEnteredFormat.wrapStrategy'


def rc(sid, r0, r1, c0, c1, f, campos):
    return {'repeatCell': {'range': {'sheetId': sid, 'startRowIndex': r0,
                                     'endRowIndex': r1, 'startColumnIndex': c0,
                                     'endColumnIndex': c1},
                           'cell': {'userEnteredFormat': f}, 'fields': campos}}


#   ⭐ UM PEDIDO POR LINHA, não três. Texto, fundo, borda e quebra viajam
#     juntos quando mudam juntos — e a lista de campos se monta sozinha a
#     partir do que foi pedido, que é o jeito de ela nunca mentir.
def estilo(sid, r0, r1, c0, c1, fs=None, b=None, fg=None, bg=None,
           lado=None, w=None, nf=None, h=None):
    f, campos = {}, []
    if fs is not None or b is not None or fg is not None:
        f['textFormat'] = {'fontFamily': 'Arial', 'fontSize': fs or 10,
                           'bold': bool(b),
                           'foregroundColorStyle': {'rgbColor': fg or TINTA}}
        campos.append('userEnteredFormat.textFormat')
    if bg is not None:
        f['backgroundColorStyle'] = {'rgbColor': bg}
        campos.append('userEnteredFormat.backgroundColorStyle')
    if lado is not None:
        f['borders'] = {lado: BORDA[lado]}
        campos.append('userEnteredFormat.borders')
    if w is not None:
        f['wrapStrategy'] = w
        campos.append('userEnteredFormat.wrapStrategy')
    if nf is not None:
        f['numberFormat'] = nf
        campos.append('userEnteredFormat.numberFormat')
    if h is not None:
        f['horizontalAlignment'] = h
        campos.append('userEnteredFormat.horizontalAlignment')
    return rc(sid, r0, r1, c0, c1, f, ','.join(campos))


def une(sid, r):
    return {'mergeCells': {'mergeType': 'MERGE_ALL', 'range': {
        'sheetId': sid, 'startRowIndex': r, 'endRowIndex': r + 1,
        'startColumnIndex': 1, 'endColumnIndex': 11}}}


#   ⭐ AS UNIDADES QUE SIGNIFICAM "ESCREVA AQUI". Logística e mão de
#     obra são digitadas pelo ambiente; chapa, m, un, m² e peça vêm da
#     Base e eu derivo o unitário de custo ÷ quantidade.

# ═══════════════════════════════════════════════════════════════════════
#   A CLASSIFICAÇÃO, PARA O LAYOUT POR ITEM
# ═══════════════════════════════════════════════════════════════════════
#   ⛔⛔ ESTE ARQUIVO ESTAVA DUPLICADO — tudo de `SECOES` para baixo
#     aparecia DUAS VEZES, resíduo de uma edição minha. Em Python a
#     segunda definição vence em silêncio, então o arquivo funcionava e
#     qualquer correção na primeira metade não tinha efeito nenhum.
#     ⭐ Reescrito de uma vez, já no layout por item.
SECOES = ('  O AMBIENTE', '  OS ITENS', '  O QUE NÃO É MARCENARIA',
          '  AS PEÇAS', '  AS NOTAS', '  AS DÚVIDAS', '  OS PARÂMETROS')

#   ⭐ o cabeçalho e a SEÇÃO em que ele é válido · ⛔ no layout por item o
#     cabeçalho de cada bloco é MATERIAL, dentro da seção AS PEÇAS (4) — e
#     também é MATERIAL no painel do ambiente (1). O mesmo rótulo em duas
#     seções, de propósito: é a mesma ideia de coluna.
CAB = {'MATERIAL': (1, 4), 'ITEM': (2,), 'CHAVE': (7,)}

#   ⭐ as testeiras de item · elas abrem o bloco e levam a medida geral na I
TESTEIRA = 'ITEM '


def classifica(linhas):
    """⭐ Uma passada só, e cada linha sai com um nome. O que não tem nome
    não tem formato — e é isso que denuncia linha que eu não previ."""
    cl, secao = [], 0
    for i, r in enumerate(linhas):
        #   ⛔ A COLUNA B PODE SER NÚMERO: no bloco OS ITENS ela é o número
        #     do item, e `.startswith` em int explode. Converter sempre.
        b = str((r[0] if r else '') or '')
        c = str((r[1] if len(r) > 1 else '') or '')
        if i == 0:
            t = 'titulo'
        elif i == 1:
            t = 'subtitulo'
        elif any(b.startswith(s) for s in SECOES):
            t = 'secao'
            secao = SECOES.index(next(s for s in SECOES if b.startswith(s))) + 1
        elif b in CAB and secao in CAB[b]:
            t = 'cabecalho'
        elif b.startswith('TOTAL DO ITEM'):
            t = 'total_item'
        elif (b == 'CUSTO DIRETO DO AMBIENTE'
              or b.startswith('MATERIAL E FERRAGEM')
              or b.startswith('⭐ CONFERÊNCIA')):
            t = 'total'
        #   ⛔ AS LINHAS DA DUPLA CONFERÊNCIA NÃO SÃO LINHAS DE ITEM. Elas
        #     caíam em `dado2` e herdavam o formato do bloco OS ITENS —
        #     inclusive as duas células AMARELAS de dias, que convidariam
        #     a digitar em cima de uma conta de controle. ⭐ Classe própria.
        elif secao == 2 and b and (b.startswith('Soma dos itens')
                                   or b.startswith('Arredondamento')
                                   or b.startswith('Material e ferragem')):
            t = 'conferencia'
        elif b.startswith(TESTEIRA) and secao == 4:
            t = 'testeira'
        elif b == '' and c:
            t = 'nota'
        elif b == '' and not c:
            t = 'vazia'
        else:
            t = 'dado%d' % secao
        cl.append(t)
    return cl


def corridas(cl, alvo):
    """as faixas contíguas de um tipo — uma requisição no lugar de dez"""
    out, i = [], 0
    while i < len(cl):
        if cl[i] in alvo:
            j = i
            while j + 1 < len(cl) and cl[j + 1] in alvo:
                j += 1
            out.append((cl[i], i, j + 1))
            i = j + 1
        else:
            i += 1
    return out


# ═══════════════════════════════════════════════════════════════════════
#   ⭐ O MAPA DE COLUNAS, POR SEÇÃO · (índice no vetor, formato, alinhar)
# ═══════════════════════════════════════════════════════════════════════
#   ⛔⛔ CONFERIR O ÍNDICE CONTRA O CABEÇALHO IMPRESSO, SEMPRE. O vetor
#     começa na coluna B, então índice 0 é B, 7 é I e 9 é K. Já pintei
#     moeda na J vazia e número de três casas no custo por contar errado —
#     e foi o Jonathan quem viu, não eu.
#   ⭐ Os cabeçalhos deste layout, para conferir:
#       1  MATERIAL ESPECIFICAÇÃO QUANTIDADE UN CUSTO %DO_CUSTO
#          0        1             2          3  4     5
#       2  ITEM MÓVEL MEDIDA DIAS_FABR DIAS_MONT . . CUSTO
#          0    1     2      3         4         5 6 7
#       4  MATERIAL ESPECIFICAÇÃO C L QTD UN R$_UN CUSTO . chave
#          0        1             2 3 4   5  6     7     8 9
#       7  CHAVE DE_ONDE_VEM FOLHA_C FOLHA_L ÁREA APROV RENDIM R$ UN
#          0     1           2       3       4    5     6      7  8
COLUNAS = {
    1: [(2, N2, 'RIGHT'), (3, None, 'CENTER'), (4, MOEDA, 'RIGHT'),
        (5, PCT, 'RIGHT')],
    2: [(7, MOEDA, 'RIGHT')],
    4: [(2, N2, 'RIGHT'), (3, N2, 'RIGHT'), (4, N2, 'RIGHT'),
        (5, None, 'CENTER'), (6, MOEDA, 'RIGHT'), (7, MOEDA, 'RIGHT')],
    7: [(2, N2, 'RIGHT'), (3, N2, 'RIGHT'), (4, N4, 'RIGHT'),
        (5, PCT, 'RIGHT'), (6, N4, 'RIGHT'), (7, MOEDA, 'RIGHT'),
        (8, None, 'CENTER')],
}

#   ⭐ AMARELO = "digite aqui" · só OS PARÂMETROS e as colunas de dias
AMARELAS = {7: (2, 3, 5, 7)}      # folha C, folha L, aproveitamento, preço


def pedidos(sid, linhas):
    cl = classifica(linhas)
    R = [rc(sid, 0, len(linhas), 1, 11, fmt(), F_TUDO)]
    E = lambda *a, **k: R.append(mini(sid, *a, **k))

    #   ⭐ o que se repete em muitas linhas vai por FAIXA CONTÍGUA; o que
    #     é único vai linha a linha. Testeira, cabeçalho e total de item
    #     são 21 linhas espalhadas, logo ficam no laço.
    for i, c in enumerate(cl):
        if c == 'titulo':
            E(i, i + 1, 1, 11, fs=16, b=True, fg=BRANCO, bg=TINTA)
        elif c == 'subtitulo':
            E(i, i + 1, 1, 11, fs=9, fg=CINZA, w='WRAP')
        elif c == 'secao':
            E(i, i + 1, 1, 11, fs=11, b=True, lado='bottom')
        elif c == 'cabecalho':
            E(i, i + 1, 1, 11, fs=8, b=True, fg=CINZA, bg=FUNDO_CAB)
        elif c == 'total':
            E(i, i + 1, 1, 11, fs=11, b=True, lado='top')
            E(i, i + 1, 8, 9, fs=11, b=True, nf=MOEDA, h='RIGHT')
        elif c == 'total_item':
            #   ⭐ o TOTAL DO ITEM fecha o bloco: negrito, linha em cima e
            #     o custo em moeda na coluna I
            E(i, i + 1, 1, 11, fs=10, b=True, lado='top')
            E(i, i + 1, 8, 9, b=True, nf=MOEDA, h='RIGHT')
        elif c == 'conferencia':
            #   ⭐ conta de controle: discreta, mas com o dinheiro legível
            E(i, i + 1, 1, 8, fs=9, fg=CINZA, w='WRAP')
            E(i, i + 1, 8, 9, fs=10, nf=MOEDA, h='RIGHT')
        elif c == 'testeira':
            #   ⭐⭐ A TESTEIRA DO ITEM é o que faz o bloco ser visível como
            #     bloco: fundo claro, nome em negrito e a medida geral à
            #     direita. Sem ela o olho não acha onde um item começa.
            E(i, i + 1, 1, 11, bg=FUNDO_CAB)
            E(i, i + 1, 1, 2, fs=11, b=True)
            E(i, i + 1, 2, 3, fs=11, b=True, w='OVERFLOW_CELL')
            E(i, i + 1, 7, 11, fs=9, fg=CINZA, h='RIGHT')

    for _c, a, z in corridas(cl, {'nota'}):
        E(a, z, 2, 11, fs=9, fg=CINZA, w='WRAP')

    #   ── os números, seção por seção ──
    for s, cols in COLUNAS.items():
        d = [i for i, c in enumerate(cl) if c == 'dado%d' % s]
        if not d:
            continue
        a, z = min(d), max(d) + 1
        for idx, nf, h in cols:
            if nf:
                E(a, z, idx + 1, idx + 2, nf=nf, h=h)
            else:
                E(a, z, idx + 1, idx + 2, h=h)
        #   a ESPECIFICAÇÃO é texto longo e cinza em toda seção
        E(a, z, 2, 3, fs=9, fg=CINZA, w='WRAP')
        #   ⭐ a CHAVE NA BASE, coluna K: é ela que liga a linha ao preço
        if s == 4:
            E(a, z, 10, 11, fs=8, fg=CINZA, h='LEFT')
        #   ⭐⭐ AS CÉLULAS QUE SE DIGITAM, POR FAIXA E NÃO LINHA A LINHA.
        #     Linha a linha davam 76 pedidos só para OS PARÂMETROS, e o
        #     lote de formato passava de 100 KB. ⭐ As linhas de uma seção
        #     são contíguas, então a faixa diz a mesma coisa em 1 pedido.
        #   ⛔ E as de folha só valem para as linhas de CHAPA: pintar de
        #     amarelo a célula vazia de um insumo convidaria a digitar
        #     largura de folha onde não existe folha.
        if s == 7:
            ch = [i for i in d if str((linhas[i][8] if len(linhas[i]) > 8
                                       else '') or '') == 'folha']
            un = [i for i in d if i not in ch]
            if ch:
                a1, z1 = min(ch), max(ch) + 1
                E(a1, z1, 3, 5, b=True, bg=AMARELO, nf=N2, h='RIGHT')
                E(a1, z1, 6, 7, b=True, bg=AMARELO, nf=PCT, h='RIGHT')
            for _c, a2, z2 in corridas(['x' if i in un else '.'
                                        for i in range(len(linhas))], {'x'}):
                E(a2, z2, 8, 9, b=True, bg=AMARELO, nf=MOEDA, h='RIGHT')
            if ch:
                E(min(ch), max(ch) + 1, 8, 9, b=True, bg=AMARELO, nf=MOEDA,
                  h='RIGHT')

    #   ── o bloco OS ITENS: medida em cinza e as duas colunas de dias ──
    d2 = [i for i, c in enumerate(cl) if c == 'dado2']
    if d2:
        a, z = min(d2), max(d2) + 1
        E(a, z, 1, 2, nf={'type': 'NUMBER', 'pattern': '00'}, h='LEFT')
        E(a, z, 3, 4, fs=9, fg=CINZA, w='WRAP')
        #   ⭐⭐ AS DUAS COLUNAS DE DIAS, AMARELAS porque são digitadas, e o
        #     Jonathan escolheu DIA DE DUPLA com fabricação e montagem
        #     separadas · ⛔ elas NÃO somam ao custo, por decisão dele: a
        #     cascata já cobra comissão de produção e de montagem.
        #   ⭐ as 6 linhas de item são contíguas: uma faixa basta
        E(a, z, 4, 6, b=True, bg=AMARELO,
          nf={'type': 'NUMBER', 'pattern': '0.0'}, h='CENTER')

    #   ── a linha do CUSTO DIRETO tem o dinheiro em F e o percentual em G ──
    for i, r in enumerate(linhas):
        b = str((r[0] if r else '') or '')
        if b == 'CUSTO DIRETO DO AMBIENTE':
            E(i, i + 1, 5, 6, fs=12, b=True, nf=MOEDA, h='RIGHT')
            E(i, i + 1, 6, 7, fs=10, b=True, nf=PCT, h='RIGHT')
        elif b in ('Consumíveis', 'Embalagem'):
            #   ⭐ o percentual aqui é TEXTO vindo de TEXT(), e texto não
            #     tem formato de número: só centralizar.
            E(i, i + 1, 4, 5, h='CENTER')
    return R, cl


LARGURAS = [('A', 0, 1, 28), ('B', 1, 2, 300), ('C', 2, 3, 430),
            ('D-K', 3, 11, 94)]


def zera(sid, n):
    """Devolve a folha inteira ao estilo base ANTES de qualquer pedido de
    formato. Sem isto, formatar é pintar por cima.

    ⛔⛔⛔ E O `unmergeCells` AQUI É O MAIS IMPORTANTE DESTE ARQUIVO. Merge
      é FORMATO, e formato sobrevive ao clear de valores: uma célula
      mesclada de B a K, sobrada do layout anterior, aceita valor só na
      âncora e DESCARTA o resto da linha em silêncio — com a API
      respondendo "success" e contando as células como gravadas. Foi o que
      engoliu três linhas em 23/11/2026, inclusive dois TOTAIS DE ITEM, e
      o que me fez diagnosticar "gravação em bloco perde linha" duas vezes
      antes de ir olhar os merges."""
    faixa = {'sheetId': sid, 'startRowIndex': 0, 'endRowIndex': n,
             'startColumnIndex': 0, 'endColumnIndex': 11}
    return [{'unmergeCells': {'range': faixa}},
            {'repeatCell': {'range': faixa, 'fields': 'userEnteredFormat',
                            'cell': {'userEnteredFormat': {
                'textFormat': {'fontFamily': 'Arial', 'fontSize': 10,
                               'bold': False,
                               'foregroundColorStyle': {'rgbColor': dict(TINTA)}},
                'backgroundColorStyle': {'rgbColor': dict(BRANCO)},
                'horizontalAlignment': 'LEFT', 'verticalAlignment': 'MIDDLE',
                'wrapStrategy': 'CLIP'}}}}]


def pagina(sid, n):
    R = zera(sid, n)
    R += [{'updateSheetProperties': {'properties': {
        'sheetId': sid, 'gridProperties': {'frozenRowCount': 2,
                                           'hideGridlines': True}},
        'fields': 'gridProperties.frozenRowCount,gridProperties.hideGridlines'}}]
    for _n, c0, c1, px in LARGURAS:
        R.append({'updateDimensionProperties': {
            'range': {'sheetId': sid, 'dimension': 'COLUMNS',
                      'startIndex': c0, 'endIndex': c1},
            'properties': {'pixelSize': px}, 'fields': 'pixelSize'}})
    return R


#   ⭐ e as linhas de texto corrido voltam a ser mescladas DEPOIS de tudo
def mescla(sid, cl):
    return [{'mergeCells': {'mergeType': 'MERGE_ALL',
             'range': {'sheetId': sid, 'startRowIndex': i, 'endRowIndex': i + 1,
                       'startColumnIndex': 1, 'endColumnIndex': 11}}}
            for i, c in enumerate(cl)
            if c in ('titulo', 'subtitulo', 'secao')]
