# -*- coding: utf-8 -*-
"""Reescreve `_chaves-base.json` A PARTIR DA PLANILHA — nunca de memória.

⭐⭐ POR QUE ISTO EXISTE [30/10/2026]. A lista `CHAVES_BASE` nasceu para
  impedir chave inventada — foi ela que pegou os R$ 15.600 da laca. ⛔ Mas
  eu a escrevi À MÃO, de cabeça, e ela mentia: declarava `MDF Cinza Fóssil
  15` e `MDF Cinza Fóssil 6`, que a Base NÃO TINHA. O Home Schooling
  (pranchas 72-74) é todo em Cinza Fóssil — ele passaria no auditor e sairia
  ZERO na aba, exatamente o defeito que a lista existia para pegar.
  ⭐ Guarda escrita de memória é a mesma memória, só com cara de código.

   uso:  1) ler  'Base (importada)'!A6:C200  pelo MCP do Sheets
         2) salvar a resposta crua em  _base-raw.json
         3) python3 -I chaves.py

⭐ A REGRA DE QUEM É CHAVE, e ela é da própria planilha, não minha:
     tem NOME (coluna A) e tem PREÇO ou UNIDADE (coluna B ou C).
  Título de seção tem só o nome — e por isso cai fora sozinho. ⛔ Foi para
  esta regra fechar que a 'Usinagem de encaixe meia-madeira' ganhou a
  unidade "encaixe" e o título "AS LINHAS CRAVADAS" perdeu o "chapa" que
  tinha na coluna C por engano.
"""
import json, pathlib
AQUI = pathlib.Path(__file__).resolve().parent
cru = json.loads((AQUI/'_base-raw.json').read_text())
linhas = cru['values'] if isinstance(cru, dict) else cru
chaves = sorted({l[0].strip() for l in linhas
                 if l and l[0].strip() and len(l) > 1
                 and any(str(c).strip() for c in l[1:3])})
(AQUI/'_chaves-base.json').write_text(
    json.dumps(chaves, ensure_ascii=False, indent=0), encoding='utf-8')
print(f'{len(chaves)} chaves lidas da Base')
for c in chaves: print('  ', c)
