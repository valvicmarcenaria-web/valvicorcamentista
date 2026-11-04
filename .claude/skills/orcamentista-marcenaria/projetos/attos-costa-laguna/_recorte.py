# -*- coding: utf-8 -*-
"""⭐ O RECORTE DO LOTE DE FORMATO.

⛔⛔ POR QUE ELE EXISTE. Quando uma aba cresce quatro linhas, o lote de
  formato inteiro (72 pedidos, 19 KB) tem de ser transcrito de novo à mão —
  e eu transcrevo errado em algum lugar. Mas o que MUDOU foi só a região do
  bloco de peças para baixo: o painel de material, as seções de cima e o
  quadro de itens ficaram na mesma linha.
⭐ Então o recorte manda: desmesclar e RESETAR a região que mudou, mais
  todo pedido cujo intervalo começa dentro dela, mais a regra condicional da
  conferência (que eu apaguei de propósito antes de regravar) e o
  auto-ajuste. Rows de cima ficam como estão, que é certo.
⛔ E o reset vem com a REGIÃO, não com a folha: resetar a folha inteira
  obrigaria a remandar tudo.
"""
import json, sys, pathlib, importlib.util, contextlib, io

P = pathlib.Path(__file__).resolve().parent
_s = importlib.util.spec_from_file_location('fm', P / 'formatar.py')
fm = importlib.util.module_from_spec(_s); sys.modules['fm'] = fm
with contextlib.redirect_stdout(io.StringIO()): _s.loader.exec_module(fm)
pl = fm.pl

PRETO, BRANCO = fm.PRETO, fm.BRANCO


def recorte(amb, aba):
    sid = fm.SIDS[aba.split()[0]]
    G, L, blocos, cr, cc, cf = pl.monta(amb, aba)
    corte = L['blk0'] - 1          # a primeira linha que pode ter mudado
    fim = L['fim']
    todos = fm.pedidos(amb, aba)

    def inicio(r):
        k = list(r)[0]
        g = r[k].get('range') or r[k].get('dimensions') or {}
        if 'startRowIndex' in g: return g['startRowIndex']
        if 'startIndex' in g: return g['startIndex']
        if k == 'addConditionalFormatRule':
            return r[k]['rule']['ranges'][0]['startRowIndex']
        return None

    out = [
        {'unmergeCells': {'range': {
            'sheetId': sid, 'startRowIndex': corte - 1, 'endRowIndex': fim,
            'startColumnIndex': 0, 'endColumnIndex': 11}}},
        {'repeatCell': {'range': {
            'sheetId': sid, 'startRowIndex': corte - 1, 'endRowIndex': fim,
            'startColumnIndex': 0, 'endColumnIndex': 11},
            'cell': {'userEnteredFormat': {
                'textFormat': {'fontSize': 10, 'bold': False, 'italic': False,
                               'foregroundColor': PRETO},
                'backgroundColor': BRANCO, 'horizontalAlignment': 'LEFT',
                'verticalAlignment': 'MIDDLE', 'wrapStrategy': 'CLIP'}},
            'fields': 'userEnteredFormat'}},
    ]
    for r in todos:
        k = list(r)[0]
        if k in ('updateDimensionProperties', 'autoResizeDimensions'):
            continue
        i = inicio(r)
        #   ⭐ a regra condicional entra SEMPRE: eu apaguei a antiga antes de
        #     regravar, para não acumular duas apontando para linhas diferentes.
        if k == 'addConditionalFormatRule' or (i is not None and i >= corte - 1):
            out.append(r)
    out.append({'autoResizeDimensions': {'dimensions': {
        'sheetId': sid, 'dimension': 'ROWS',
        'startIndex': corte - 1, 'endIndex': fim}}})
    return out, corte, fim


if __name__ == '__main__':
    alvos = [x for x in pl.ABAS if x[1].split()[0] in sys.argv[1:]]
    for amb, aba in alvos:
        R, corte, fim = recorte(amb, aba)
        (P / f'_rec-{aba.split()[0]}.json').write_text(
            json.dumps(R, ensure_ascii=False))
        print(f'{aba:<16} {len(R):>3} pedidos · região {corte}–{fim} · '
              f'{len(json.dumps(R)) // 1024} KB')
