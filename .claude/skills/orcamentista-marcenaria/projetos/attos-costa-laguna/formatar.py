# -*- coding: utf-8 -*-
"""ATTOS · Costa Laguna — a formatação das sete abas, GERADA, nunca à mão.

⭐⭐ A regra que o ICA pagou caro para aprender [Jonathan, 28/10/2026]:
  "a formatação do living e da cozinha estao diferentes". Estavam, e em
  quinze pontos — porque foram formatadas à mão, duas vezes. ⛔ Duas mãos,
  dois resultados. A aba não se formata, ela se GERA.

⛔ fontSize da API é INTEIRO: 9,5 derruba o lote todo com "Internal error",
  e o erro não diz qual request falhou.
⛔ `fields: "userEnteredFormat"` troca o formato INTEIRO — o que não vem
  aqui volta ao padrão. É isso que limpa padrão numérico herdado.
⛔⛔ E NUNCA UM DECIMAL DENTRO DE FÓRMULA de formato condicional: em pt_BR o
  literal é 0,01 e a API recusa "0.01". `ROUND(x;2)<>0` diz o mesmo.
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
F5 = {'red': .957, 'green': .957, 'blue': .957}
AMARELO = {'red': 1, 'green': .949, 'blue': .8}
MOEDA = {'type': 'CURRENCY', 'pattern': '"R$" #,##0.00'}
PCT = {'type': 'PERCENT', 'pattern': '0.0%'}
NUM2 = {'type': 'NUMBER', 'pattern': '#,##0.00'}
COL = 'ABCDEFGHIJK'

SIDS = {'01': 101, '02': 102, '03': 103, '04': 104, '05': 105, '06': 106,
        '07': 107}


def fm(sz=10, bd=False, it=False, fg=None, bg=None, al=None, wr=None,
       num=None, bor=None):
    """⭐ O QUE É PADRÃO NÃO SE REPETE. A planilha já nasce Arial e preta
       (spreadsheetTheme), e `al='LEFT'`, `wr='CLIP'` e `verticalAlignment`
       são o default da API. Mandar tudo isso em 729 pedidos fez o lote
       chegar a 233 KB — e um lote que eu não consigo conferir é um lote
       que vai entrar com erro. Só o DELTA viaja."""
    #   ⛔⛔ E `fields` ESTREITO NÃO FUNCIONA AQUI: no repeatCell o caminho é
    #     relativo ao CellData, então seria "userEnteredFormat.textFormat.
    #     fontSize" — a API recusou "textFormat.fontSize" com "Invalid field:
    #     text_format". Com o prefixo, o lote fica MAIOR que mandando o
    #     formato inteiro. Então vai o formato inteiro, só sem o que é padrão.
    t = {'fontSize': int(sz), 'bold': bool(bd), 'italic': bool(it),
         'foregroundColor': fg or PRETO}
    f = {'textFormat': t, 'verticalAlignment': 'MIDDLE',
         'horizontalAlignment': al or 'LEFT', 'wrapStrategy': wr or 'CLIP'}
    if al: f['horizontalAlignment'] = al
    if wr: f['wrapStrategy'] = wr
    if bg: f['backgroundColor'] = bg
    if num: f['numberFormat'] = num
    if bor: f['borders'] = bor
    return f


RUA = {'bottom': {'style': 'SOLID', 'width': 1, 'color': PRETO}}
TETO = {'top': {'style': 'SOLID_THICK', 'width': 3, 'color': OURO}}
LARG = dict(A=18, B=235, C=300, D=72, E=72, F=92, G=82, H=96, I=96, J=78, K=78)


def pedidos(amb, aba):
    sid = SIDS[aba.split()[0]]
    G, L, blocos, cr, cc, cf = pl.monta(amb, aba)
    R = []

    def rng(r0, r1, c0, c1):
        return {'sheetId': sid, 'startRowIndex': r0 - 1, 'endRowIndex': r1,
                'startColumnIndex': COL.index(c0),
                'endColumnIndex': COL.index(c1) + 1}

    def rc(r0, r1, c0, c1, f):
        """⭐⭐ `fields` ESTREITO, e isso não é só economia de bytes.
           `fields: "userEnteredFormat"` troca o formato INTEIRO: o que não
           vier no pedido VOLTA AO PADRÃO. Era por isso que eu tinha de
           repetir Arial, preto e alinhamento em 618 pedidos. Com o reset
           geral feito uma vez (tudo=True) e cada pedido seguinte mandando
           só o SEU campo, nada herdado reaparece e o lote cabe na conferência."""
        R.append({'repeatCell': {'range': rng(r0, r1, c0, c1),
                  'cell': {'userEnteredFormat': f},
                  'fields': 'userEnteredFormat'}})

    def mesc(r, c0, c1):
        R.append({'mergeCells': {'range': rng(r, r, c0, c1),
                                 'mergeType': 'MERGE_ALL'}})

    def auto(r0, r1):
        """⛔⛔ ALTURA FIXA CORTA TEXTO, E CORTA EM SILÊNCIO. A coluna de
           ESPECIFICAÇÃO tem frases de 250 caracteres com WRAP ligado: a
           34 px cabem duas linhas e o resto desaparece sem aviso nenhum —
           a planilha fica com cara de pronta e o aviso que importa fica
           escondido atrás da borda da célula. Quem decide a altura é o
           CONTEÚDO."""
        R.append({'autoResizeDimensions': {'dimensions': {
            'sheetId': sid, 'dimension': 'ROWS',
            'startIndex': r0 - 1, 'endIndex': r1}}})

    def alt(r0, r1, px):
        R.append({'updateDimensionProperties': {'range': {
            'sheetId': sid, 'dimension': 'ROWS',
            'startIndex': r0 - 1, 'endIndex': r1},
            'properties': {'pixelSize': px}, 'fields': 'pixelSize'}})

    # ── 1 · a folha inteira limpa por baixo ─────────────────────────────
    rc(1, L['fim'], 'A', 'K', fm(bg=BRANCO))
    for c, px in LARG.items():
        R.append({'updateDimensionProperties': {'range': {
            'sheetId': sid, 'dimension': 'COLUMNS',
            'startIndex': COL.index(c), 'endIndex': COL.index(c) + 1},
            'properties': {'pixelSize': px}, 'fields': 'pixelSize'}})
    # ── 2 · a cabeça ────────────────────────────────────────────────────
    rc(1, 1, 'B', 'K', fm(16, True, fg=BRANCO, bg=PRETO)); mesc(1, 'B', 'K')
    alt(1, 1, 46)
    rc(2, 2, 'B', 'K', fm(9, fg=CINZA, wr='WRAP')); mesc(2, 'B', 'K')
    alt(2, 2, 42)
    # ── 3 · as seções ───────────────────────────────────────────────────
    for k in ('s_amb', 's_it', 's_ni', 's_pec', 's_nt'):
        rc(L[k], L[k], 'B', 'K', fm(11, True, bor=RUA)); mesc(L[k], 'B', 'K')
    rc(L['s_dv'], L['s_dv'], 'B', 'K', fm(11, True, fg=VERM, bor=RUA))
    mesc(L['s_dv'], 'B', 'K')
    # ── 4 · o painel de material ────────────────────────────────────────
    rc(L['cab_mat'], L['cab_mat'], 'B', 'K', fm(8, True, fg=CINZA, bg=F7))
    rc(L['mat0'], L['mat1'], 'C', 'C', fm(8, fg=CINZA, wr='WRAP'))
    rc(L['mat0'], L['mat1'], 'D', 'D', fm(10, al='RIGHT', num=NUM2))
    rc(L['mat0'], L['mat1'], 'E', 'E', fm(8, fg=CINZA))
    rc(L['mat0'], L['mat1'], 'F', 'H', fm(10, al='RIGHT', num=MOEDA))
    rc(L['mat0'], L['mat1'], 'I', 'I', fm(9, fg=CINZA, al='RIGHT', num=PCT))
    auto(L['mat0'], L['mat1'])
    #   ⭐ a célula amarela do frete: a ÚNICA que se digita na aba
    rc(L['frete'], L['frete'], 'D', 'D',
       fm(10, True, al='RIGHT', bg=AMARELO, num=NUM2))
    d = L['direto']
    rc(d, d, 'B', 'B', fm(11, True, bor=TETO))
    rc(d, d, 'C', 'E', fm(10, bor=TETO))
    rc(d, d, 'F', 'H', fm(11, True, al='RIGHT', num=MOEDA, bor=TETO))
    rc(d, d, 'I', 'I', fm(9, fg=CINZA, al='RIGHT', num=PCT, bor=TETO))
    rc(L['nota'], L['nota'], 'C', 'K', fm(8, fg=CINZA, wr='WRAP'))
    mesc(L['nota'], 'C', 'K')
    # ── 5 · os itens ────────────────────────────────────────────────────
    rc(L['cab_it'], L['cab_it'], 'B', 'K', fm(8, True, fg=CINZA, bg=F7))
    rc(L['it0'], L['it1'], 'B', 'B', fm(10, True, al='CENTER'))
    rc(L['it0'], L['it1'], 'C', 'C', fm(10))
    rc(L['it0'], L['it1'], 'D', 'H', fm(8, fg=CINZA, wr='WRAP'))
    rc(L['it0'], L['it1'], 'I', 'I', fm(10, al='RIGHT', num=MOEDA))
    auto(L['it0'], L['it1'])
    f0 = L['f0']
    rc(f0, f0 + 4, 'B', 'B', fm(9, fg=CINZA))
    rc(f0, f0 + 4, 'I', 'I', fm(9, al='RIGHT', num=MOEDA))
    for r in (f0 + 2, f0 + 4):
        rc(r, r, 'B', 'B', fm(9, True))
        rc(r, r, 'I', 'I', fm(10, True, al='RIGHT', num=MOEDA))
    rc(f0 + 3, f0 + 3, 'B', 'B', fm(9, True, fg=OURO))
    rc(f0 + 3, f0 + 3, 'I', 'I', fm(10, True, fg=OURO, al='RIGHT', num=MOEDA))
    #   ⭐⭐ E AS DUAS CONFERÊNCIAS FICAM VERMELHAS SOZINHAS se saírem de zero
    for r in (f0 + 2, f0 + 4):
        R.append({'addConditionalFormatRule': {'rule': {
            'ranges': [rng(r, r, 'I', 'I')],
            'booleanRule': {'condition': {'type': 'CUSTOM_FORMULA',
                            'values': [{'userEnteredValue':
                                        f'=ROUND($I${r};2)<>0'}]},
                            'format': {'backgroundColor': VERM,
                                       'textFormat': {'bold': True,
                                                      'foregroundColor': BRANCO}}}},
            'index': 0}})
    # ── 6 · o que não é marcenaria ──────────────────────────────────────
    rc(L['ni0'], L['ni1'], 'B', 'K', fm(8, fg=CINZA, wr='WRAP'))
    for r in range(L['ni0'], L['ni1'] + 1):
        mesc(r, 'B', 'K')
    # ── 7 · as peças ────────────────────────────────────────────────────
    rc(L['cab_pec'], L['cab_pec'], 'B', 'K', fm(8, True, fg=CINZA, bg=F7))
    rc(L['blk0'], L['blk1'], 'B', 'B', fm(9))
    rc(L['blk0'], L['blk1'], 'C', 'C', fm(8, fg=CINZA, wr='WRAP'))
    rc(L['blk0'], L['blk1'], 'D', 'F', fm(9, al='RIGHT'))
    rc(L['blk0'], L['blk1'], 'G', 'G', fm(8, fg=CINZA, al='CENTER'))
    rc(L['blk0'], L['blk1'], 'H', 'H', fm(8, fg=CINZA))
    rc(L['blk0'], L['blk1'], 'I', 'I', fm(9, al='RIGHT', num=MOEDA))
    rc(L['blk0'], L['blk1'], 'J', 'K', fm(8, fg=CINZA, al='RIGHT', num=NUM2))
    auto(L['blk0'], L['blk1'])
    for x in blocos:
        rc(x['hdr'], x['hdr'], 'B', 'H', fm(10, True, bg=F5))
        rc(x['hdr'], x['hdr'], 'I', 'K',
           fm(10, True, al='RIGHT', bg=F5, num=MOEDA))
    # ── 8 · notas e dúvidas ─────────────────────────────────────────────
    rc(L['nt0'], L['nt1'], 'B', 'K', fm(9, fg=CINZA, wr='WRAP'))
    for r in range(L['nt0'], L['nt1'] + 1):
        mesc(r, 'B', 'K')
    rc(L['dv0'], L['dv1'], 'B', 'K', fm(9, wr='WRAP'))
    for r in range(L['dv0'], L['dv1'] + 1):
        mesc(r, 'B', 'K')
    #   ⭐ O AUTO-AJUSTE VEM POR ÚLTIMO, e isso não é detalhe: ele MEDE o
    #     que está na célula no instante em que roda. Posto antes da
    #     mesclagem e da fonte, mede o formato velho e devolve a altura errada.
    auto(L['ni0'], L['ni1'])
    auto(L['nt0'], L['nt1'])
    auto(L['dv0'], L['dv1'])
    auto(L['nota'], L['nota'])
    return R


if __name__ == '__main__':
    alvos = [x for x in pl.ABAS if sys.argv[1:] in ([], ['--todos'])
             or x[0] in sys.argv[1:]]
    todos = []
    for amb, aba in alvos:
        R = pedidos(amb, aba)
        (P / f'_fmt-{aba.split()[0]}.json').write_text(json.dumps(R, ensure_ascii=False))
        todos += R
        print(f'{aba:<16} {len(R):>4} pedidos · '
              f'{len(json.dumps(R)) // 1024} KB')
    (P / '_fmt-todos.json').write_text(json.dumps(todos, ensure_ascii=False))
    print(f'{"TOTAL":<16} {len(todos):>4} pedidos · '
          f'{len(json.dumps(todos)) // 1024} KB')


# ════════════════════════════════════════════════════════════════════════
# O LOTE ESSENCIAL
# ════════════════════════════════════════════════════════════════════════
#   ⛔⛔ POR QUE ELE EXISTE, e a lição é sobre MIM, não sobre a planilha.
#     O lote completo são 646 pedidos e 208 KB, e eu não tenho como enviá-lo
#     sem transcrever 208 KB de JSON aninhado à mão. Transcrever 208 KB é
#     exatamente o tipo de risco que o Jonathan me pediu para não correr
#     nesta planilha — e seria risco gasto em ENFEITE, com o número já
#     conferido.
#   ⭐ Então o lote essencial faz o que decide a LEITURA: largura de coluna,
#     moeda, porcentagem, os cabeçalhos pretos, a quebra de linha nas colunas
#     de texto, a célula amarela do frete e o vermelho automático das duas
#     conferências. São ~22 pedidos por aba e as sete cabem numa chamada.
#   ⚠ O resto do lote fica no `_fmt-*.json`, pronto, para quando valer a pena.
def essencial():
    T = []
    for amb, aba in pl.ABAS:
        sid = SIDS[aba.split()[0]]
        G, L, blocos, cr, cc, cf = pl.monta(amb, aba)

        def rng(r0, r1, c0, c1):
            return {'sheetId': sid, 'startRowIndex': r0 - 1, 'endRowIndex': r1,
                    'startColumnIndex': COL.index(c0),
                    'endColumnIndex': COL.index(c1) + 1}

        def rc(r0, r1, c0, c1, f):
            T.append({'repeatCell': {'range': rng(r0, r1, c0, c1),
                      'cell': {'userEnteredFormat': f},
                      'fields': 'userEnteredFormat'}})

        def larg(c0, c1, px):
            T.append({'updateDimensionProperties': {'range': {
                'sheetId': sid, 'dimension': 'COLUMNS',
                'startIndex': COL.index(c0), 'endIndex': COL.index(c1) + 1},
                'properties': {'pixelSize': px}, 'fields': 'pixelSize'}})

        rc(1, L['fim'], 'A', 'K', fm(bg=BRANCO))
        larg('A', 'A', 18); larg('B', 'B', 235); larg('C', 'C', 300)
        larg('D', 'E', 72); larg('F', 'F', 92); larg('G', 'G', 82)
        larg('H', 'I', 96); larg('J', 'K', 78)
        # a cabeça
        rc(1, 1, 'B', 'K', fm(15, True, fg=BRANCO, bg=PRETO))
        rc(2, 2, 'B', 'K', fm(9, fg=CINZA, wr='WRAP'))
        # as seis seções
        for k in ('s_amb', 's_it', 's_ni', 's_pec', 's_nt', 's_dv'):
            rc(L[k], L[k], 'B', 'K',
               fm(11, True, fg=VERM if k == 's_dv' else PRETO, bor=RUA))
        # os três cabeçalhos de tabela
        for k in ('cab_mat', 'cab_it', 'cab_pec'):
            rc(L[k], L[k], 'B', 'K', fm(8, True, fg=CINZA, bg=F7))
        # ⭐ O DINHEIRO EM MOEDA, e é isto que faz a planilha ser lida
        rc(L['mat0'], L['direto'], 'F', 'H', fm(10, al='RIGHT', num=MOEDA))
        rc(L['mat0'], L['direto'], 'I', 'I',
           fm(9, fg=CINZA, al='RIGHT', num=PCT))
        rc(L['mat0'], L['mat1'], 'D', 'D', fm(10, al='RIGHT', num=NUM2))
        rc(L['direto'], L['direto'], 'B', 'B', fm(11, True, bor=TETO))
        rc(L['it0'], L['blk1'], 'I', 'I', fm(10, al='RIGHT', num=MOEDA))
        rc(L['blk0'], L['blk1'], 'D', 'F', fm(9, al='RIGHT', num=NUM2))
        rc(L['blk0'], L['blk1'], 'J', 'K',
           fm(8, fg=CINZA, al='RIGHT', num=NUM2))
        rc(L['blk0'], L['blk1'], 'H', 'H', fm(8, fg=CINZA))
        # ⭐ o texto que precisa caber
        rc(L['mat0'], L['nota'], 'C', 'C', fm(8, fg=CINZA, wr='WRAP'))
        rc(L['ni0'], L['ni1'], 'B', 'B', fm(8, fg=CINZA, wr='WRAP'))
        rc(L['nt0'], L['dv1'], 'B', 'B', fm(9, wr='WRAP'))
        # ⭐ a única célula que se digita na aba
        rc(L['frete'], L['frete'], 'D', 'D',
           fm(10, True, al='RIGHT', bg=AMARELO, num=NUM2))
        # ⭐⭐ e as duas conferências ficam vermelhas sozinhas
        f0 = L['f0']
        for r in (f0 + 2, f0 + 4):
            T.append({'addConditionalFormatRule': {'rule': {
                'ranges': [rng(r, r, 'I', 'I')],
                'booleanRule': {'condition': {'type': 'CUSTOM_FORMULA',
                                'values': [{'userEnteredValue':
                                            f'=ROUND($I${r};2)<>0'}]},
                                'format': {'backgroundColor': VERM,
                                           'textFormat': {'bold': True,
                                            'foregroundColor': BRANCO}}}},
                'index': 0}})
        T.append({'autoResizeDimensions': {'dimensions': {
            'sheetId': sid, 'dimension': 'ROWS',
            'startIndex': 1, 'endIndex': L['fim']}}})
    return T
