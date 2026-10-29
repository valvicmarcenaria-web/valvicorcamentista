# -*- coding: utf-8 -*-
"""O DELTA de formato entre o que JÁ está na aba e o que ela precisa.

⭐ Existe porque reaplicar as 142 requests inteiras é caro, e quando o
   levantamento muda de tamanho por uma linha só, quase tudo já está certo:
   o que mudou é o rodapé, que desceu ou subiu. Este script compara o
   conjunto de requests ANTIGO com o NOVO e devolve só a diferença, mais
   um reset da faixa que se moveu — porque formato velho em linha que
   mudou de papel não se corrige sozinho.

   python3 _delta.py <nome> <blk1_antigo> <fim_antigo>
"""
import sys, json, pathlib

nome, blk1_ant, fim_ant = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
req = json.load(open(f'_c1-{nome}.txt')) + json.load(open(f'_c2-{nome}.txt'))

# a faixa que precisa de reset: do fim do bloco antigo OU novo (o menor)
# até o fim antigo OU novo (o maior) — tudo que pode ter papel trocado.
d = json.load(open(f'_aba-{nome}.json'))
L = d['layout']
corte = min(blk1_ant, L['blk1']) - 1          # 0-indexed
fim   = max(fim_ant, L['fim'])

base = req[6]['repeatCell']['cell']
col9 = req[7]['repeatCell']['cell']
col10 = req[8]['repeatCell']['cell']
sid = req[6]['repeatCell']['range']['sheetId']
R = lambda a, b, c0, c1: {'sheetId': sid, 'startRowIndex': a, 'endRowIndex': b,
                          'startColumnIndex': c0, 'endColumnIndex': c1}

out = [{'unmergeCells': {'range': R(corte, fim, 0, 11)}},
       {'repeatCell': {'range': R(corte, fim, 0, 11), 'cell': base,
                       'fields': 'userEnteredFormat'}},
       {'repeatCell': {'range': R(corte, fim, 9, 10), 'cell': col9,
                       'fields': 'userEnteredFormat'}},
       {'repeatCell': {'range': R(corte, fim, 10, 11), 'cell': col10,
                       'fields': 'userEnteredFormat'}},
       {'updateDimensionProperties': {
           'range': {'sheetId': sid, 'dimension': 'ROWS',
                     'startIndex': corte, 'endIndex': fim},
           'properties': {'pixelSize': 21}, 'fields': 'pixelSize'}}]

# e agora só o que o gerador manda PARA DENTRO dessa faixa, mais as
# regras condicionais, que carregam a faixa do bloco no corpo.
def dentro(r):
    k = list(r)[0]
    v = r[k]
    if k in ('deleteConditionalFormatRule', 'updateSheetProperties'):
        return False
    if k == 'addConditionalFormatRule':
        return True
    if k == 'deleteDimension':
        return True
    rg = v.get('range', {})
    a = rg.get('startRowIndex', rg.get('startIndex'))
    b = rg.get('endRowIndex', rg.get('endIndex'))
    if a is None:                      # largura de coluna
        return False
    if rg.get('dimension') == 'COLUMNS':
        return False
    return b > corte

ndel = sum(1 for r in req if 'addConditionalFormatRule' in r)
out = ([{'deleteConditionalFormatRule': {'sheetId': sid, 'index': 0}}] * ndel
       # ⛔ req[6:9] é o reset de base da aba INTEIRA. Num delta ele
       #    apagaria o topo, que já está certo — o reset aqui é só da faixa.
       + out + [r for r in req[9:] if dentro(r)])

pathlib.Path(f'_delta-{nome}.json').write_text(
    json.dumps(out, ensure_ascii=False, separators=(',', ':')))
print(f'  faixa de reset: linhas {corte+1} a {fim} · {len(out)} requests · '
      f'{len(json.dumps(out, ensure_ascii=False))} chars')
