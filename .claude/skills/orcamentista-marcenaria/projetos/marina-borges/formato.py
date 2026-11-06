# -*- coding: utf-8 -*-
"""CHARBEL CHELALA — o formato visual da planilha, linha por linha.

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
# ⭐ LIDAS CÉLULA A CÉLULA DA ABA-MODELO DA CASA, 06/11/2026 · não são escolha
# minha: a SEÇÃO leva um fio PRETO embaixo, e o TOTAL uma barra DOURADA GROSSA
# em cima. Eu havia posto fio cinza nos dois, e as nove abas saíram diferentes
# do Painel e da aba Preço e Comissões, que já seguiam o modelo.
DOURADO = {'red': 0.68235296, 'green': 0.5137255, 'blue': 0.22745098}
BORDA = {'bottom': {'style': 'SOLID', 'width': 1,
                    'colorStyle': {'rgbColor': dict(TINTA)}},
         'top': {'style': 'SOLID_THICK', 'width': 3,
                 'colorStyle': {'rgbColor': DOURADO}}}


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


SECOES = ('  O AMBIENTE', '  OS ITENS', '  O QUE NÃO É MARCENARIA',
          '  AS PEÇAS', '  AS NOTAS', '  AS DÚVIDAS')
CAB = {'MATERIAL': 1, 'ITEM': 2, 'PEÇA': 4}


def classifica(linhas):
    """⭐ Uma passada só, e cada linha sai com um nome. O que não tem nome
    não tem formato — e é isso que denuncia linha que eu não previ."""
    cl, secao = [], 0
    for i, r in enumerate(linhas):
        b = (r[0] if r else '') or ''
        c = (r[1] if len(r) > 1 else '') or ''
        if i == 0:
            t = 'titulo'
        elif i == 1:
            t = 'subtitulo'
        elif any(b.startswith(s) for s in SECOES):
            t = 'secao'
            secao = SECOES.index(next(s for s in SECOES if b.startswith(s))) + 1
        elif b in CAB and secao == CAB[b]:
            t = 'cabecalho'
        elif b == 'CUSTO DIRETO DO AMBIENTE' or b.startswith('⭐ CONFERÊNCIA'):
            t = 'total'
        elif b.startswith('■'):
            t = 'grupo'
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
            while j + 1 < len(cl) and cl[j + 1] == cl[i]:
                j += 1
            out.append((cl[i], i, j + 1))
            i = j + 1
        else:
            i += 1
    return out


def pedidos(sid, linhas):
    cl = classifica(linhas)
    R = [rc(sid, 0, max(len(linhas), 120), 1, 11, fmt(), F_TUDO)]
    E = lambda *a, **k: R.append(estilo(sid, *a, **k))

    for i, c in enumerate(cl):
        if c == 'titulo':
            E(i, i + 1, 1, 11, fs=16, b=True, fg=BRANCO, bg=TINTA); R.append(une(sid, i))
        elif c == 'subtitulo':
            E(i, i + 1, 1, 11, fs=9, fg=CINZA, w='WRAP'); R.append(une(sid, i))
        elif c == 'secao':
            E(i, i + 1, 1, 11, fs=11, b=True, lado='bottom'); R.append(une(sid, i))
        elif c == 'cabecalho':
            E(i, i + 1, 1, 11, fs=8, b=True, fg=CINZA, bg=FUNDO_CAB)
        elif c == 'total':
            E(i, i + 1, 1, 11, fs=11, b=True, lado='top')
        elif c == 'grupo':
            E(i, i + 1, 1, 2, b=True)
            E(i, i + 1, 2, 11, fs=9, fg=CINZA, w='OVERFLOW_CELL')

    for _c, a, z in corridas(cl, {'nota'}):
        E(a, z, 2, 11, fs=9, fg=CINZA, w='WRAP')

    #   ⭐ OS NÚMEROS, POR SEÇÃO INTEIRA. As faixas de dado se quebram em
    #     toda linha de grupo; a seção não se quebra.
    COL = {
        1: [(2, 3, N2, 'RIGHT'), (4, 5, MOEDA, 'RIGHT'), (5, 6, PCT, 'RIGHT')],
        #   ⛔ PREÇO é o índice 7 do vetor e CUSTO o 8 — e o vetor começa
        #     na coluna B. Eu tinha escrito 8 e 9, que joga os dois uma
        #     coluna à direita, em cima de J e K. Conferir índice contra
        #     o cabeçalho impresso é o que pega isso.
        2: [(7, 8, MOEDA, 'RIGHT'), (8, 9, MOEDA, 'RIGHT')],
        4: [(2, 4, N2, 'RIGHT'), (4, 5, N0, 'CENTER'), (5, 6, None, 'CENTER'),
            (7, 8, N3, 'RIGHT'), (8, 9, MOEDA, 'RIGHT')],
    }
    for s in (1, 2, 4):
        d = [i for i, c in enumerate(cl) if c == 'dado%d' % s]
        if not d:
            continue
        a, z = min(d), max(d) + 1
        for c0, c1, nf, h in COL[s]:
            E(a, z, c0 + 1, c1 + 1, nf=nf, h=h) if nf else E(a, z, c0 + 1, c1 + 1, h=h)
        if s == 1:
            E(a, z, 2, 3, fs=9, fg=CINZA, w='OVERFLOW_CELL')
        if s == 2:
            E(a, z, 3, 8, fs=9, fg=CINZA, w='OVERFLOW_CELL')
            #   ⭐ "01" colado vira o número 1. O formato "00" devolve o
            #     zero à esquerda sem transformar o número em texto.
            E(a, z, 1, 2, nf={'type': 'NUMBER', 'pattern': '00'}, h='LEFT')

    for i, r in enumerate(linhas):
        b = (r[0] if r else '') or ''
        if b == 'CUSTO DIRETO DO AMBIENTE':
            E(i, i + 1, 5, 6, nf=MOEDA, h='RIGHT')
            E(i, i + 1, 6, 7, nf=PCT, h='RIGHT')
        elif b.startswith('\u2b50 CONFER'):
            E(i, i + 1, 8, 10, nf=MOEDA, h='RIGHT')
        elif b in ('Consum\u00edveis', 'Embalagem'):
            #   ⭐ 0,06 e 0,02 na coluna QUANTIDADE são 6% e 2%, e com
            #     formato de número apareciam como "0,06". Percentual.
            E(i, i + 1, 3, 4, nf=PCT, h='RIGHT')
        elif b.startswith('Frete \u00b7 R$'):
            E(i, i + 1, 3, 4, b=True, bg=AMARELO, nf=N0, h='RIGHT')
    return R, cl


LARGURAS = [('A', 0, 1, 28), ('B', 1, 2, 300), ('C', 2, 3, 430), ('D-K', 3, 11, 100)]


def pagina(sid, n):
    R = [{'updateSheetProperties': {'properties': {
        'sheetId': sid, 'gridProperties': {'frozenRowCount': 2,
                                           'hideGridlines': True}},
        'fields': 'gridProperties.frozenRowCount,gridProperties.hideGridlines'}}]
    for _n, c0, c1, px in LARGURAS:
        R.append({'updateDimensionProperties': {
            'range': {'sheetId': sid, 'dimension': 'COLUMNS',
                      'startIndex': c0, 'endIndex': c1},
            'properties': {'pixelSize': px}, 'fields': 'pixelSize'}})
    return R


IDS = {'01 Cozinha': 301, '02 Hall e Jantar': 302, '03 Estar e TV': 303,
       '04 Acessos e Corredor': 304, '05 Suíte': 305, '06 Closet': 306,
       '07 Banho da Suíte': 307, '08 Banheiro Social': 308, '09 Quarto': 309}

if __name__ == '__main__':
    d = json.loads((AQUI / 'planilha.json').read_text(encoding='utf-8'))
    alvo = sys.argv[1:] or list(IDS)
    saida = {}
    for a in alvo:
        R, cl = pedidos(IDS[a], d[a])
        R = pagina(IDS[a], len(d[a])) + R
        saida[a] = R
        sem = sorted({t for t in cl if t == 'vazia'})
        print('%-24s %4d linhas · %3d pedidos · tipos: %s'
              % (a, len(d[a]), len(R),
                 ', '.join('%s×%d' % (t, cl.count(t))
                           for t in sorted(set(cl)))))
    (AQUI / 'formato.json').write_text(json.dumps(saida, ensure_ascii=False,
                                                  separators=(',', ':')),
                                       encoding='utf-8')
    print('\ntotal de pedidos:', sum(len(v) for v in saida.values()))
