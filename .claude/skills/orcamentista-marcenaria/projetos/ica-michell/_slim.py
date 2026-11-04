# -*- coding: utf-8 -*-
"""Esvazia H e I DENTRO de cada faixa, deixando só a primeira linha.

⭐ O resto vai por copyPaste PASTE_FORMULA, que é o que a planilha faz
  melhor do que eu: repetir fórmula ajustando a linha. ⛔ E é o que cabe
  no argumento do MCP — a Suíte Mariana inteira não cabia.

⛔⛔ MAS O copyPaste NÃO SABE DE EXCEÇÃO. Ele carimba a fórmula da
  primeira linha da faixa em todas as outras, e onde a linha trazia um
  R$ FECHADO do ambiente — a serralheria — o valor era destruído e a aba
  voltava a buscar na Base. A mesa da Suíte Hóspedes saiu R$ 2.500 em vez
  dos R$ 450 que o Jonathan fechou, e ninguém reclamou porque a célula
  continuava com cara de célula certa.

  Então o slim agora DEVOLVE as exceções: toda linha cuja H não é a PROCV
  padrão sai numa lista, para ser reescrita depois do copyPaste. O que o
  carimbo apaga, a lista repõe.
"""
import sys, json, pathlib
P = pathlib.Path(__file__).resolve().parent
nome = sys.argv[1]
A = json.load(open(P/f'_aba-{nome}.json'))
M = json.load(open(P/f'_{nome}-merge.json'))
blk0 = A['layout']['blk0']
faixas = A['faixas']
excecoes = []
for a, b in faixas:
    for ln in range(a + 1, b + 1):
        i = ln - blk0
        h = M[i][6]
        if h or M[i][7]:
            # uma H que não começa com '=' é valor fechado do ambiente
            if h != '' and not str(h).startswith('='):
                excecoes.append((ln, h))
            M[i][6] = M[i][7] = ''
json.dump(M, open(P/f'_{nome}-slim.json', 'w'), ensure_ascii=False)
json.dump(excecoes, open(P/f'_exc-{nome}.json', 'w'), ensure_ascii=False)
s = json.dumps(M, ensure_ascii=False, separators=(',', ':'))
open(P/'_blk.txt', 'w').write(s)
print(f'B{blk0}:K{blk0+len(M)-1} · {len(s)} chars · faixas {faixas}')
if excecoes:
    print(f'  ⛔ REPOR DEPOIS DO copyPaste: ' +
          ' · '.join(f'H{ln}={v}' for ln, v in excecoes))
