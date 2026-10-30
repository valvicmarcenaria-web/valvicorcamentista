# -*- coding: utf-8 -*-
"""Tira a coluna de FRETE (e a de TOTAL) do painel de material de uma aba
JÁ GRAVADA, sem reescrever a aba inteira.

⭐ POR QUE EXISTE: o aba.py já nasce sem as duas colunas, mas as abas que
  foram gravadas antes continuam com elas na tela. Reescrever a aba toda
  por causa de duas colunas é caro; o painel de material são quinze linhas.

⛔ O cabeçalho cinza ia de B até I. Repintar B..G não limpa H6:I6 — a faixa
  cinza fica pendurada nas duas colunas mortas. Por isso H e I são
  explicitamente devolvidas ao padrão, no cabeçalho e na linha de total.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent/'_modelo'))
from formatar import mk, fm, MOEDA, PCT, INT, AMARELO, CINZA, F5, F7, TETO

NOME, SID = sys.argv[1], int(sys.argv[2])
P = pathlib.Path(__file__).resolve().parent
L = json.load(open(P/f'_aba-{NOME}.json'))['layout']
c, m0, m1, d = L['cab_mat'], L['mat0'], L['mat1'], L['direto']
rng, rc, alt, mesc, larg = mk(SID)
Q = [rc(c, c, 'B', 'G', fm(8, True, fg=CINZA, bg=F7)),
     rc(c, c, 'D', 'D', fm(8, True, fg=CINZA, bg=F7, al='RIGHT')),
     rc(c, c, 'E', 'E', fm(8, True, fg=CINZA, bg=F7, al='CENTER')),
     rc(c, c, 'F', 'G', fm(8, True, fg=CINZA, bg=F7, al='RIGHT')),
     rc(c, c, 'H', 'I', fm()),                     # ⛔ a faixa cinza morre aqui
     rc(m0, m1, 'F', 'F', fm(10, al='RIGHT', num=MOEDA)),
     rc(m0, m1, 'G', 'G', fm(10, fg=CINZA, al='RIGHT', num=PCT)),
     rc(m0, m1, 'H', 'I', fm()),
     rc(L['frete'], L['frete'], 'D', 'D',
        fm(10, True, al='RIGHT', bg=AMARELO, num=INT)),
     rc(d, d, 'B', 'G', fm(11, True, bg=F5, bor=TETO)),
     rc(d, d, 'F', 'F', fm(11, True, bg=F5, bor=TETO, al='RIGHT', num=MOEDA)),
     rc(d, d, 'G', 'G', fm(11, True, bg=F5, bor=TETO, al='RIGHT', num=PCT)),
     rc(d, d, 'H', 'I', fm(11, True))]
print(f'{NOME}: painel {c}..{d} · {len(Q)} requests', file=sys.stderr)
print(json.dumps(Q, ensure_ascii=False, separators=(',', ':')))
