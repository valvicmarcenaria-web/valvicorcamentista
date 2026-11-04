# -*- coding: utf-8 -*-
"""Prepara a gravação de uma aba em DUAS partes, para não repetir fórmula.

⭐⭐ POR QUE EXISTE [30/10/2026]: as fórmulas de H e de I do bloco de peças
  são a MESMA fórmula em toda linha — só o número da linha muda, e ele é
  relativo ($K43 → $K44 sozinho). Escrever as catorze cópias à mão custa
  dez vezes mais que escrever uma e mandar o Sheets replicar.

  ⛔ E não é só custo: cada cópia digitada é uma chance de erro de uma
    linha, que é o erro mais caro que existe nesta planilha — ele não dá
    #VALOR!, ele dá um número errado que fecha a conferência.

   saída:  _grava2-<amb>.json  faixas com H e I VAZIOS, menos a primeira
                               linha de peça de cada item
           _copia-<amb>.json   os copyPaste que descem a fórmula
                               e as linhas de TOTAL, que são à parte

   uso:  python3 gravar.py lavanderia 105
"""
import sys, json, pathlib
P = pathlib.Path(__file__).resolve().parent
NOME, SID = sys.argv[1], int(sys.argv[2])
G = json.load(open(P/f'_grava-{NOME}.json'))
L = json.load(open(P/f'_aba-{NOME}.json'))['layout']
blk0 = L['blk0']

# ── acha, no bloco, onde começa e acaba cada corrida de peças ───────────
#   ⭐ pelo CONTEÚDO, não por contagem: 'MATERIAL' abre o cabeçalho e
#     'TOTAL' fecha o item. É o que a aba mostra, então não há o que
#     divergir.
blo = next(o for o in G if o['faixa'] == f"B{blk0}:K{blk0+len(o['matriz'])-1}")
M = blo['matriz']
corridas, i = [], 0
while i < len(M):
    if str(M[i][0]) == 'MATERIAL':
        a = i + 1
        b = a
        while b < len(M) and not str(M[b][0]).startswith('TOTAL'): b += 1
        corridas.append((a, b - 1, b))        # primeira peça, última, total
        i = b
    i += 1

copia, totais = [], []
for a, b, t in corridas:
    r0, r1, rt = blk0 + a, blk0 + b, blk0 + t
    if r1 > r0:
        copia.append({'copyPaste': {
            'source': {'sheetId': SID, 'startRowIndex': r0 - 1,
                       'endRowIndex': r0, 'startColumnIndex': 7,
                       'endColumnIndex': 9},
            'destination': {'sheetId': SID, 'startRowIndex': r0,
                            'endRowIndex': r1, 'startColumnIndex': 7,
                            'endColumnIndex': 9},
            'pasteType': 'PASTE_FORMULA'}})
    totais.append((rt, M[t][7]))              # a fórmula de I da linha TOTAL
    # ⭐ apaga H e I de TODA peça menos a primeira: é ela que vai ser copiada
    for k in range(a + 1, b + 1): M[k][6] = M[k][7] = ''
    M[t][6] = M[t][7] = ''                    # o TOTAL vai à parte

json.dump(G, open(P/f'_grava2-{NOME}.json', 'w'), ensure_ascii=False)
json.dump({'copia': copia, 'totais': totais},
          open(P/f'_copia-{NOME}.json', 'w'), ensure_ascii=False)
for a, b, t in corridas:
    print(f'   peças {blk0+a:3}..{blk0+b:3} · total {blk0+t:3} · '
          f'{b-a} cópias', file=sys.stderr)
antes = len(json.dumps(json.load(open(P/f'_grava-{NOME}.json')),
                       ensure_ascii=False))
print(f'   {antes} → {len(json.dumps(G, ensure_ascii=False))} chars  '
      f'({len(copia)} copyPaste, {len(totais)} totais)', file=sys.stderr)
