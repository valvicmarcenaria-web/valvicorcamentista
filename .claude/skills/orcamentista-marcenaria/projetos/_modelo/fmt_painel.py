# -*- coding: utf-8 -*-
"""O formato do Painel, no layout do Michell. ⛔ layout não é cor."""
import sys, json
sys.path.insert(0, '.')
from formatar import *

def requests(SID=0):
  rng, rc, alt, mesc, larg = mk(SID)
  Q = cabeca(rc, alt, mesc, 110)
  Q += [larg('A', 28), larg('B', 300), larg('C', 110), larg('D', 70),
      larg('E', 70), larg('F', 110), larg('G', 120), larg('H', 110),
      larg('I', 170), larg('J', 120), larg('K', 130)]
  for r in (4, 11, 48, 61, 74, 81, 85):
    Q += secao(rc, mesc, r)
    Q += [alt(r, r, 26)]
  # ⭐ O CONJUNTO · cinco indicadores em pares de colunas
  Q += cabtab(rc, 6)
  Q += [rc(7, 7, 'B', 'K', fm(16, True)), alt(7, 7, 36)]
  Q += texto(rc, alt, mesc, 9, px=118)
  # ⭐ ONDE ESTÁ O DINHEIRO
  Q += cabtab(rc, 13)
  Q += [rc(14, 19, 'B', 'F', fm(10)),
      rc(14, 19, 'G', 'G', fm(10, al='RIGHT', num=MOEDA)),
      rc(14, 19, 'H', 'H', fm(10, fg=CINZA, al='RIGHT', num=PCT)),
      rc(14, 19, 'I', 'K', fm(9, fg=OURO)),
      rc(19, 19, 'B', 'K', fm(11, True, bor=TETO)),
      rc(19, 19, 'G', 'G', fm(11, True, al='RIGHT', num=MOEDA, bor=TETO)),
      rc(19, 19, 'H', 'H', fm(11, True, al='RIGHT', num=PCT, bor=TETO)),
      alt(14, 19, 22)]
  # ⭐ POR AMBIENTE · dez colunas, como no Michell
  Q += cabtab(rc, 23)
  Q += [rc(24, 44, 'B', 'B', fm(10)),
      rc(24, 44, 'C', 'C', fm(9, fg=CINZA, al='CENTER')),
      rc(24, 44, 'D', 'E', fm(10, fg=CINZA, al='CENTER', num=INT)),
      rc(24, 44, 'F', 'K', fm(10, al='RIGHT', num=MOEDA)),
      rc(44, 44, 'B', 'K', fm(11, True, bor=TETO)),
      rc(44, 44, 'D', 'E', fm(11, True, al='CENTER', num=INT, bor=TETO)),
      rc(44, 44, 'F', 'K', fm(11, True, al='RIGHT', num=MOEDA, bor=TETO)),
      alt(24, 44, 22)]
  # ⭐ O PREÇO DO PROJETO
  Q += [rc(50, 50, 'C', 'K', fm(9, fg=CINZA, wr='WRAP')), mesc(50, 'C', 'K'),
      alt(50, 50, 60)]
  Q += cabtab(rc, 52)
  Q += [rc(53, 59, 'B', 'B', fm(10, True)),
      rc(53, 59, 'G', 'G', fm(11, True, al='RIGHT', num=MOEDA)),
      rc(54, 56, 'G', 'G', fm(11, True, al='RIGHT', num=PCT2)),
      rc(59, 59, 'G', 'G', fm(11, True, al='RIGHT', num=PCT2)),
      rc(57, 57, 'B', 'G', fm(13, True)),
      rc(57, 57, 'G', 'G', fm(14, True, al='RIGHT', num=MOEDA)),
      rc(53, 59, 'H', 'K', fm(9, fg=CINZA, wr='WRAP')),
      alt(53, 59, 28)]
  for r in range(53, 60): Q.append(mesc(r, 'H', 'K'))
  # ⭐ O LUCRO DO PROJETO · as duas células amarelas são as únicas digitáveis
  Q += cabtab(rc, 63)
  Q += [rc(64, 69, 'B', 'B', fm(10, True)),
      rc(64, 69, 'G', 'G', fm(11, True, al='RIGHT', num=MOEDA)),
      rc(65, 65, 'G', 'G', fm(11, True, al='RIGHT', num=MOEDA, bg=AMARELO)),
      rc(67, 67, 'G', 'G', fm(11, True, al='RIGHT', num=INT, bg=AMARELO)),
      rc(69, 69, 'B', 'G', fm(13, True, fg=OURO, bor=TETO)),
      rc(69, 69, 'G', 'G', fm(14, True, fg=OURO, al='RIGHT', num=MOEDA,
                              bor=TETO)),
      rc(64, 69, 'H', 'K', fm(9, fg=CINZA, wr='WRAP')),
      alt(64, 69, 28)]
  for r in range(64, 70): Q.append(mesc(r, 'H', 'K'))
  Q += [rc(70, 70, 'C', 'K', fm(9, fg=VERM, wr='WRAP')), mesc(70, 'C', 'K'),
      alt(70, 70, 60)]
  # ⭐ as duas listas
  Q += [rc(75, 79, 'C', 'K', fm(9, fg=CINZA, wr='WRAP')),
      rc(82, 82, 'C', 'K', fm(9, fg=CINZA, wr='WRAP')), alt(82, 82, 44)]
  for r in list(range(75, 80)) + [82]: Q.append(mesc(r, 'C', 'K'))
  # ⭐ AS REGRAS DA CASA
  Q += [rc(87, 103, 'B', 'B', fm(11, True, fg=OURO, al='CENTER', num=INT)),
      rc(87, 103, 'C', 'K', fm(9, fg=CINZA, wr='WRAP')), alt(87, 103, 54)]
  for r in range(87, 104): Q.append(mesc(r, 'C', 'K'))

  return Q

if __name__ == '__main__':
    Q = requests()
    print(len(Q), 'requests', file=sys.stderr)
    print(json.dumps(Q, ensure_ascii=False, separators=(',', ':')))
