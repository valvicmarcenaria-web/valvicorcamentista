# Abas gravadas na planilha do Gustavo Raposo

Planilha: `1HovPv64ISuL-cnRUNyKpxoPdZqvkzMQyiAYBNYiexE8`

⭐ A CONFERÊNCIA DE CADA ABA TEM DE FECHAR EM R$ 0,00. É a única prova de que
nenhuma chave caiu fora da Base — ⛔ a divergência que não dá erro.

⛔ O MCP do Sheets não aceita arquivo: cada aba é gravada transcrevendo à mão
os ~35 KB de `_req-<amb>.json` (formato) e os ~20 KB de `_grava2-<amb>.json`
(conteúdo) dentro das chamadas. `gcloud auth print-access-token` foi negado pelo
classificador, então não há atalho por script.

## Pipeline por aba

1. `update_spreadsheet` com os requests de `_req-<amb>.json` — formato, grade,
   larguras, merges e formatação condicional. ⛔ CRESÇA A GRADE ANTES DE ESCREVER.
2. `update_formulas` faixa por faixa, com as matrizes de `_grava2-<amb>.json`.
3. `update_spreadsheet` com os `copyPaste` PASTE_FORMULA de `_copia-<amb>.json` —
   replica H/I para baixo em cada corrida de peças.
4. Os totais de item, por `updateCells` com `formulaValue`.
5. Ler a CONFERÊNCIA e só então passar para a aba seguinte.

| # | aba | sheetId | conferência | custo direto |
|---|-----|---------|-------------|--------------|
| 03 | Cozinha | 103 | R$ 0,00 | — |
| 04 | Despensa | 104 | R$ 0,00 | — |
| 05 | Lavanderia | 105 | R$ 0,00 | — |
| 06 | Rouparia | 106 | R$ 0,00 | — |
| 07 | Office | 107 | R$ 0,00 | — |
| 08 | Suíte Master | 108 | R$ 0,00 | R$ 10.706,53 |
| 09 | Closet Master | 109 | R$ 0,00 | — |
| 10 | Banho Master | 110 | R$ 0,00 | R$ 5.627,02 |
| 11 | Suíte 01 Filhos | 111 | R$ 0,00 | R$ 20.883,37 |
| 12 | Banho Suíte 01 | 112 | R$ 0,00 | R$ 2.367,60 |
| 13 | Suíte 02 Filhas | 113 | R$ 0,00 | R$ 17.534,94 |

## Falta gravar

- 14 Closet Suíte 02 (114)
- 15 Banho Suíte 02 (115)
- 16 Suíte Hóspedes (116)
- 17 Banho Hóspedes (117)
- 18 Banho Social (118)
- 19 Homeschooling (119)

## Falta refazer

- 02 Lavabo (102) — só o espelho mudou; `lavabo.py` já está pronto
- 01 Varanda (101) — ainda com preço Blum velho e a coluna de frete

## Falta ligar

- Painel, linhas 24–43, e o quadro ④ de Preço e Comissões.
  O frete de cada ambiente acha-se pelo rótulo: `SUMIF(B:B;"Frete";F:F)`.
