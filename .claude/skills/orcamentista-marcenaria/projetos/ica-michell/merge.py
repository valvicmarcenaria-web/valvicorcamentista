# -*- coding: utf-8 -*-
"""Junta o que planilha.py produz num único bloco B<blk0>:K<fim>.

⭐⭐ POR QUE ISTO EXISTE. Eu vinha fazendo esta junção À MÃO, ambiente por
  ambiente, dentro de um `python3 -c`. Deu certo quatro vezes e é exatamente
  o tipo de coisa que erra na quinta — a chave da Base mora no índice 6 do
  que o planilha.py devolve e tem de ir para o índice 9 da aba, e uma linha
  fora de lugar desloca a coluna inteira sem o orçamento reclamar.

  São 16 ambientes pela frente. A junção vira arquivo.

⭐ O formato da aba, coluna por coluna:
      B nome · C especificação · D comprimento · E largura · F qtd
      G unidade · H R$ unitário · I custo · J vazia · K chave na Base
  O planilha.py já devolve a linha nessas dez colunas, com H e I VAZIOS —
  ⛔ e é só isso que falta: `fml` traz as duas fórmulas por NÚMERO DE LINHA,
  não por posição na lista. Quem não tem fórmula — cabeçalho de ITEM, linha
  de leitura de cota, respiro — fica com H e I vazios, e é assim que tem
  de ser. Linhas curtas (o cabeçalho tem 8 colunas, a de cota tem 2) são
  completadas até dez, senão a coluna K cai no lugar errado.

   uso:  python3 merge.py <ambiente>
         → _<ambiente>-merge.json, pronto para update_formulas
"""
import sys, json, pathlib
P = pathlib.Path(__file__).resolve().parent
NOME = sys.argv[1]
R = json.load(open(P/f'_{NOME}-rows.json'))
A = json.load(open(P/f'_aba-{NOME}.json'))
BLK0 = A['layout']['blk0']
FML = {int(r[0]): (r[1], r[2]) for r in R['fml']}

OUT = []
for i, v in enumerate(R['val']):
    ln = BLK0 + i
    linha = (list(v) + [''] * 10)[:10]
    # ⛔⛔ SÓ ESCREVE ONDE HÁ FÓRMULA, e só a que não vem nula. A primeira
    #   versão deste arquivo sobrescrevia H e I sempre — e apagou, em teste,
    #   a medida geral que mora no I do cabeçalho de ITEM, os rótulos
    #   "R$ UN"/"CUSTO" do cabeçalho de MATERIAL e o =SOMA do TOTAL, que já
    #   vêm prontos do planilha.py. Dezoito linhas de 105, caladas.
    for col, v2 in zip((6, 7), FML.get(ln, (None, None))):
        if v2 is not None: linha[col] = v2
    OUT.append(linha)

# ⛔ a conferência que paga o preço de existir: se uma linha com fórmula
#   não tiver chave, o PROCV devolve vazio e o custo some sem erro nenhum.
mudos = [BLK0 + i for i, r in enumerate(OUT) if r[6] and not r[9]]
assert not mudos, f'⛔ linha com fórmula e sem chave: {mudos}'
orfas = sorted(set(FML) - set(range(BLK0, BLK0 + len(OUT))))
assert not orfas, f'⛔ fórmula fora do bloco: {orfas}'

json.dump(OUT, open(P/f'_{NOME}-merge.json', 'w'), ensure_ascii=False)
print(f'  {len(OUT)} linhas · B{BLK0}:K{BLK0 + len(OUT) - 1} · '
      f'{len(FML)} com fórmula')
