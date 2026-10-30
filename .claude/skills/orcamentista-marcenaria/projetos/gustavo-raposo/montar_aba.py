# -*- coding: utf-8 -*-
"""Junta o que o aba.py e o planilha.py produzem em MATRIZES prontas para
uma só gravação por faixa — em vez de uma chamada por linha de fórmula.

⭐ POR QUE: o `fml` sai como (linha, fórmula de H, fórmula de I) e o `val`
  como as dez colunas B..K. Escritos separados, são 73 chamadas numa aba de
  varanda. Juntos, são UMA.

⛔ `update_formulas` escreve com USER_ENTERED, então literal e fórmula
  convivem na mesma matriz — é o que permite a junção.

   uso:  python3 montar_aba.py varanda
         → imprime, em JSON, a lista de (faixa, matriz) na ordem de gravação
"""
import sys, json, pathlib
P = pathlib.Path(__file__).resolve().parent
NOME = sys.argv[1]
D = json.load(open(P/f'_aba-{NOME}.json'))
R = json.load(open(P/f'_{NOME}-rows.json'))
L = D['layout']

def dez(linha):
    """Dez colunas, B..K, sem None (o Sheets recusa) e sem buraco."""
    return [('' if v is None else v) for v in linha] + [''] * (10 - len(linha))

# ── o bloco de peças: val com as fórmulas de H e de I encaixadas ────────
blk0 = L['blk0']
M = [dez(v) for v in R['val']]
for r, fh, fi in R['fml']:
    i = r - blk0
    if fh is not None: M[i][6] = fh
    if fi is not None: M[i][7] = fi

faixas = [(D['top_range'], [dez(l) for l in D['top']]),
          (f"B{blk0}:K{blk0 + len(M) - 1}", M),
          (D['notas_range'], [dez(l) for l in D['notas']]),
          (D['duvidas_range'], [dez(l) for l in D['duvidas']])]

if __name__ == '__main__':
    out = [{'faixa': f, 'matriz': m} for f, m in faixas]
    for o in out:
        print(f"{o['faixa']:14} {len(o['matriz'])} linhas  "
              f"{len(json.dumps(o['matriz'], ensure_ascii=False)):7} chars",
              file=sys.stderr)
    json.dump(out, open(P/f'_grava-{NOME}.json', 'w'), ensure_ascii=False)
