# -*- coding: utf-8 -*-
"""ATTOS · Costa Laguna — a formatação das sete abas, GERADA, nunca à mão.

⭐⭐ A regra que o ICA pagou caro para aprender [Jonathan, 28/10/2026]:
  "a formatação do living e da cozinha estao diferentes". Estavam, e em
  quinze pontos — porque foram formatadas à mão, duas vezes. ⛔ Duas mãos,
  dois resultados. A aba não se formata, ela se GERA.

⛔⛔ E AGORA UMA SEGUNDA LIÇÃO, do mesmo dono [Jonathan, 04/11/2026]:
  "veja como é o layout das abas dos ambientes". O layout mudou — o painel
  de material passou a SEIS colunas (B..G), a chave da Base foi para a K e
  o custo do item para a I. Este arquivo foi reescrito inteiro para ele.
  ⛔ O formato velho NÃO SAI SOZINHO: a coluna I do bloco de itens herdou a
  PORCENTAGEM do layout antigo e mostrava "374548,9%" onde se lê
  "R$ 3.745,49". Por isso o pedido ①, o reset, existe e vem primeiro.

⛔ fontSize da API é INTEIRO: 9,5 derruba o lote todo com "Internal error",
  e o erro não diz qual request falhou.
⛔⛔ E NUNCA UM DECIMAL DENTRO DE FÓRMULA de formato condicional: em pt_BR o
  literal é 0,01 e a API recusa "0.01". `ROUND(x;2)<>0` diz o mesmo.
⭐ `fields` ESTREITO, e o caminho é relativo ao CellData — portanto
  "userEnteredFormat.numberFormat", nunca "numberFormat" sozinho. Com o
  reset feito uma vez, cada pedido seguinte manda só o SEU campo, nada
  herdado reaparece, e o lote cabe numa chamada que eu consigo conferir.
"""
import json, sys, pathlib, importlib.util, contextlib, io

P = pathlib.Path(__file__).resolve().parent
_s = importlib.util.spec_from_file_location('pl', P / 'planilha.py')
pl = importlib.util.module_from_spec(_s); sys.modules['pl'] = pl
with contextlib.redirect_stdout(io.StringIO()): _s.loader.exec_module(pl)

PRETO = {'red': .102, 'green': .102, 'blue': .102}
CINZA = {'red': .42, 'green': .42, 'blue': .42}
OURO = {'red': .686, 'green': .514, 'blue': .231}
VERM = {'red': .776, 'green': .157, 'blue': .157}
BRANCO = {'red': 1, 'green': 1, 'blue': 1}
F7 = {'red': .969, 'green': .969, 'blue': .969}
F5 = {'red': .945, 'green': .945, 'blue': .945}
AMARELO = {'red': 1, 'green': .949, 'blue': .8}
MOEDA = {'type': 'CURRENCY', 'pattern': '"R$" #,##0.00'}
PCT = {'type': 'PERCENT', 'pattern': '0.0%'}
NUM2 = {'type': 'NUMBER', 'pattern': '#,##0.00'}
COL = 'ABCDEFGHIJK'
SIDS = {'01': 101, '02': 102, '03': 103, '04': 104, '05': 105, '06': 106,
        '07': 107}
#   ⭐ a largura da coluna é o que decide a LEITURA, e ela segue o papel que
#     a coluna tem no layout da casa — não um número redondo qualquer.
LARG = [('A', 'A', 18), ('B', 'B', 250), ('C', 'C', 330), ('D', 'D', 78),
        ('E', 'E', 68), ('F', 'F', 96), ('G', 'G', 80), ('H', 'H', 90),
        ('I', 'I', 108), ('J', 'J', 24), ('K', 'K', 158)]
RUA = {'bottom': {'style': 'SOLID', 'width': 1, 'color': PRETO}}
TETO = {'top': {'style': 'SOLID_THICK', 'width': 3, 'color': OURO}}


def pedidos(amb, aba):
    """O lote de uma aba. Os pedidos saem na ordem em que se aplicam:
       o reset por baixo, depois cada camada por cima dele."""
    sid = SIDS[aba.split()[0]]
    G, L, blocos, chapa_rows, cc, cf = pl.monta(amb, aba)
    R = []

    def rng(r0, r1, c0, c1):
        return {'sheetId': sid, 'startRowIndex': r0 - 1, 'endRowIndex': r1,
                'startColumnIndex': COL.index(c0),
                'endColumnIndex': COL.index(c1) + 1}

    def cel(r0, r1, c0, c1, sz=None, bd=None, fg=None, bg=None, al=None,
            wr=None, num=None, bor=None):
        """⭐⭐ UM PEDIDO POR INTERVALO, e isto não é economia de bytes: é o
           que me deixa CONFERIR o lote. Em quatro pedidos separados —
           fonte, cor, alinhamento, moeda — o mesmo intervalo aparecia
           quatro vezes e as sete abas davam 903 pedidos e 206 KB. 206 KB
           de JSON aninhado é mais do que eu consigo transcrever sem errar,
           e um lote que eu não consigo conferir é um lote que entra torto.
           ⛔ `fields` é relativo ao CellData: "userEnteredFormat.textFormat",
           nunca "textFormat". E só o DELTA viaja — o reset já deixou a
           folha em Arial 10, preta, branca, à esquerda e sem moeda, então
           o que for igual a isso NÃO é mandado."""
        f, m = {}, []
        t = {}
        if sz is not None: t['fontSize'] = int(sz)
        if bd is not None: t['bold'] = bool(bd)
        if fg is not None: t['foregroundColor'] = fg
        if t:
            f['textFormat'] = t; m.append('textFormat')
        if bg is not None:
            f['backgroundColor'] = bg
            m.append('backgroundColor')
        if al is not None:
            f['horizontalAlignment'] = al
            m.append('horizontalAlignment')
        if wr is not None:
            f['wrapStrategy'] = wr; m.append('wrapStrategy')
        if num is not None:
            f['numberFormat'] = num; m.append('numberFormat')
        if bor is not None:
            f['borders'] = bor; m.append('borders')
        #   ⛔⛔ E A MÁSCARA AGRUPADA NÃO EXISTE AQUI. Eu tentei
        #     "userEnteredFormat(textFormat,numberFormat)" para poupar 18
        #     caracteres por campo, e a API recusou o lote inteiro com
        #     "Invalid field: user_entered_format(text_format". O caminho
        #     tem de vir COMPLETO em cada campo, separado por vírgula.
        #     ⭐ Nada se aplicou, porque batchUpdate é tudo ou nada — foi o
        #     único motivo de o erro ter saído barato.
        R.append({'repeatCell': {'range': rng(r0, r1, c0, c1),
                  'cell': {'userEnteredFormat': f},
                  'fields': ','.join(f'userEnteredFormat.{k}' for k in m)}})

    def mesc(r0, r1, c0, c1):
        """⭐ MERGE_ROWS mescla CADA LINHA do intervalo por si. Uma mesclagem
           por linha eram 15 pedidos por aba; assim são 3."""
        R.append({'mergeCells': {'range': rng(r0, r1, c0, c1),
                                 'mergeType': 'MERGE_ROWS'}})

    # ① ⛔⛔ O RESET, e ele VEM PRIMEIRO. `fields: userEnteredFormat` troca
    #    o formato INTEIRO: o que não vem aqui volta ao padrão — e é
    #    exatamente isso que apaga a porcentagem herdada do layout antigo.
    R.append({'repeatCell': {'range': rng(1, L['fim'], 'A', 'K'),
              'cell': {'userEnteredFormat': {
                  'textFormat': {'fontSize': 10, 'bold': False,
                                 'italic': False, 'foregroundColor': PRETO},
                  'backgroundColor': BRANCO, 'horizontalAlignment': 'LEFT',
                  'verticalAlignment': 'MIDDLE', 'wrapStrategy': 'CLIP'}},
              'fields': 'userEnteredFormat'}})
    #   ⛔⛔ E A MESCLAGEM VELHA TEM DE SAIR ANTES. `mergeCells` sobre célula
    #     já mesclada em OUTRO recorte é erro da API, e erro num lote de
    #     batchUpdate derruba o lote INTEIRO — nada se aplica. O layout
    #     antigo mesclava B..K em linhas que agora são outra coisa.
    R.append({'unmergeCells': {'range': rng(1, L['fim'], 'A', 'K')}})
    for c0, c1, px in LARG:
        R.append({'updateDimensionProperties': {'range': {
            'sheetId': sid, 'dimension': 'COLUMNS',
            'startIndex': COL.index(c0), 'endIndex': COL.index(c1) + 1},
            'properties': {'pixelSize': px}, 'fields': 'pixelSize'}})

    # ② a cabeça
    cel(1, 1, 'B', 'K', 15, True, BRANCO, bg=PRETO); mesc(1, 1, 'B', 'K')
    cel(2, 2, 'B', 'K', 9, fg=CINZA, wr='WRAP'); mesc(2, 2, 'B', 'K')

    # ③ as seis seções — a de DÚVIDAS em vermelho, que é a que pede resposta
    for k in ('s_amb', 's_it', 's_ni', 's_pec', 's_nt', 's_dv'):
        cel(L[k], L[k], 'B', 'K', 11, True,
            VERM if k == 's_dv' else None, bor=RUA)
        mesc(L[k], L[k], 'B', 'K')

    # ④ o painel de material · B MATERIAL C ESPEC. D QTD E UN F CUSTO G %
    cel(L['cab_mat'], L['cab_mat'], 'B', 'G', 8, True, CINZA, bg=F7)
    a, z, d = L['mat0'], L['mat1'], L['direto']
    cel(a, z, 'C', 'C', 8, fg=CINZA, wr='WRAP')
    cel(a, z, 'D', 'D', al='RIGHT', num=NUM2)
    cel(a, z, 'E', 'E', 8, fg=CINZA, al='CENTER')
    cel(a, d, 'F', 'F', al='RIGHT', num=MOEDA)
    cel(a, d, 'G', 'G', 9, fg=CINZA, al='RIGHT', num=PCT)
    #   ⭐ a célula amarela do frete: a ÚNICA que se digita na aba
    cel(L['frete'], L['frete'], 'D', 'D', bd=True, bg=AMARELO, al='RIGHT',
        num=NUM2)
    cel(d, d, 'B', 'B', 11, True, bor=TETO)
    cel(d, d, 'C', 'E', bor=TETO)
    cel(d, d, 'F', 'F', 11, True, al='RIGHT', num=MOEDA, bor=TETO)
    cel(d, d, 'G', 'G', 9, fg=CINZA, al='RIGHT', num=PCT, bor=TETO)
    cel(L['nota'], L['nota'], 'C', 'K', 8, fg=CINZA, wr='WRAP')
    mesc(L['nota'], L['nota'], 'C', 'K')

    # ⑤ os itens · B ITEM C MÓVEL D MEDIDA GERAL I CUSTO
    cel(L['cab_it'], L['cab_it'], 'B', 'I', 8, True, CINZA, bg=F7)
    a, z, f0 = L['it0'], L['it1'], L['f0']
    cel(a, z, 'B', 'B', bd=True, al='CENTER')
    cel(a, z, 'D', 'H', 8, fg=CINZA, wr='WRAP')
    #   as cinco linhas de conferência da casa, e a última é a que vale
    cel(a, f0 + 4, 'I', 'I', al='RIGHT', num=MOEDA)
    cel(f0, f0 + 4, 'B', 'B', 9, fg=CINZA)
    cel(f0, f0 + 4, 'I', 'I', 9)
    cel(f0 + 2, f0 + 2, 'B', 'I', 10, True)
    cel(f0 + 4, f0 + 4, 'B', 'I', 10, True, OURO)
    #   ⭐⭐ E A CONFERÊNCIA FICA VERMELHA SOZINHA se sair de zero. É a trava
    #     que não depende de eu lembrar de olhar.
    R.append({'addConditionalFormatRule': {'rule': {
        'ranges': [rng(f0 + 4, f0 + 4, 'I', 'I')],
        'booleanRule': {'condition': {'type': 'CUSTOM_FORMULA', 'values': [
            {'userEnteredValue': f'=ROUND($I${f0 + 4};2)<>0'}]},
            'format': {'backgroundColor': VERM, 'textFormat': {
                'bold': True, 'foregroundColor': BRANCO}}}}, 'index': 0}})

    # ⑥ o que não é marcenaria
    a, z = L['ni0'], L['ni1']
    cel(a, z, 'B', 'K', 8, fg=CINZA, wr='WRAP'); mesc(a, z, 'B', 'K')

    # ⑦ as peças, item por item
    a, z = L['blk0'], L['blk1']
    cel(a, z, 'B', 'B', 9)
    cel(a, z, 'C', 'C', 8, fg=CINZA, wr='WRAP')
    cel(a, z, 'D', 'F', 9, al='RIGHT', num=NUM2)
    cel(a, z, 'G', 'G', 8, fg=CINZA, al='CENTER')
    cel(a, z, 'H', 'H', 8, fg=CINZA, al='RIGHT', num=MOEDA)
    cel(a, z, 'I', 'I', 9, al='RIGHT', num=MOEDA)
    cel(a, z, 'K', 'K', 8, fg=CINZA)
    for x in blocos:
        #   ⛔ a faixa do item leva a MEDIDA GERAL na I, que é TEXTO: sem
        #     desfazer a moeda, "353,5 × 272 × 3" viraria R$ 0,00.
        cel(x['faixa'], x['faixa'], 'B', 'K', 10, True, bg=F5, al='LEFT',
            num={'type': 'TEXT'})
        cel(x['desc'], x['desc'], 'C', 'C', 8, fg=CINZA, wr='WRAP')
        cel(x['cab'], x['cab'], 'B', 'K', 8, True, CINZA, bg=F7)
        cel(x['cab'], x['cab'], 'D', 'I', 8, True, CINZA, bg=F7, al='RIGHT')
        cel(x['tot'], x['tot'], 'B', 'I', 10, True)

    # ⑧ notas em C, dúvidas numeradas em B com o texto em C
    a, z = L['nt0'], L['nt1']
    cel(a, z, 'C', 'K', 9, fg=CINZA, wr='WRAP'); mesc(a, z, 'C', 'K')
    a, z = L['dv0'], L['dv1']
    cel(a, z, 'B', 'B', 10, True, VERM, al='CENTER')
    cel(a, z, 'C', 'K', 9, wr='WRAP'); mesc(a, z, 'C', 'K')

    # ⑨ ⛔⛔ ALTURA FIXA CORTA TEXTO, E CORTA EM SILÊNCIO — e o auto-ajuste
    #    vem POR ÚLTIMO, porque ele MEDE o que está na célula no instante em
    #    que roda. Posto antes da fonte e da mesclagem, mede o formato velho.
    R.append({'autoResizeDimensions': {'dimensions': {
        'sheetId': sid, 'dimension': 'ROWS',
        'startIndex': 1, 'endIndex': L['fim']}}})
    R.append({'updateDimensionProperties': {'range': {
        'sheetId': sid, 'dimension': 'ROWS', 'startIndex': 0, 'endIndex': 1},
        'properties': {'pixelSize': 46}, 'fields': 'pixelSize'}})
    return R


if __name__ == '__main__':
    alvos = [x for x in pl.ABAS if sys.argv[1:] in ([], ['--todos'])
             or x[0] in sys.argv[1:]]
    todos = []
    for amb, aba in alvos:
        R = pedidos(amb, aba)
        (P / f'_fmt-{aba.split()[0]}.json').write_text(
            json.dumps(R, ensure_ascii=False, separators=(',', ':')))
        todos += R
        print(f'{aba:<16} {len(R):>4} pedidos · '
              f'{len(json.dumps(R, separators=(",", ":"))) // 1024} KB')
    (P / '_fmt-todos.json').write_text(
        json.dumps(todos, ensure_ascii=False, separators=(',', ':')))
    print(f'{"TOTAL":<16} {len(todos):>4} pedidos · '
          f'{len(json.dumps(todos, separators=(",", ":"))) // 1024} KB')
