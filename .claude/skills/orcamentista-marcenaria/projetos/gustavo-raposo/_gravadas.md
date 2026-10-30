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
| 01 | Varanda | 101 | R$ 0,00 | R$ 10.568,90 |
| 02 | Lavabo | 102 | R$ 0,00 | R$ 1.082,32 |
| 03 | Cozinha | 103 | R$ 0,00 | R$ 24.619,43 |
| 04 | Despensa | 104 | R$ 0,00 | R$ 3.939,78 |
| 05 | Lavanderia | 105 | R$ 0,00 | R$ 7.387,44 |
| 06 | Rouparia | 106 | R$ 0,00 | R$ 5.619,80 |
| 07 | Office | 107 | R$ 0,00 | R$ 9.328,00 |
| 08 | Suíte Master | 108 | R$ 0,00 | R$ 10.706,53 |
| 09 | Closet Master | 109 | R$ 0,00 | R$ 11.651,11 |
| 10 | Banho Master | 110 | R$ 0,00 | R$ 5.627,02 |
| 11 | Suíte 01 Filhos | 111 | R$ 0,00 | R$ 20.883,37 |
| 12 | Banho Suíte 01 | 112 | R$ 0,00 | R$ 2.367,60 |
| 13 | Suíte 02 Filhas | 113 | R$ 0,00 | R$ 17.534,94 |
| 14 | Closet Suíte 02 | 114 | R$ 0,00 | R$ 8.248,74 |
| 15 | Banho Suíte 02 | 115 | R$ 0,00 | R$ 2.374,36 |
| 16 | Suíte Hóspedes | 116 | R$ 0,00 | R$ 7.489,49 |
| 17 | Banho Hóspedes | 117 | R$ 0,00 | R$ 1.571,69 |
| 18 | Banho Social | 118 | R$ 0,00 | R$ 1.603,93 |
| 19 | Homeschooling | 119 | R$ 0,00 | R$ 9.203,79 |
| | **CUSTO DIRETO DO PROJETO** | | | **R$ 161.808,24** |

⭐ AS DEZENOVE ABAS ESTÃO GRAVADAS e as dezenove fecham em R$ 0,00.

## Como conferir as dezenove de uma vez

⭐ Não se confere aba por aba: põe-se UMA fórmula numa célula de rascunho
(usei `Painel!K110`), lê-se e apaga-se. Ela acha a linha da conferência pelo
RÓTULO, não pelo endereço — e por isso continua valendo quando a aba muda de
tamanho:

```
=TEXTJOIN(" | ";1;
  "01="&TEXT(INDEX('01 Varanda'!I:I;MATCH("⭐ CONFER*";'01 Varanda'!B:B;0));"0.00");
  … uma parcela por aba …
)
```

Trocando `I:I` por `F:F` e `"⭐ CONFER*"` por `"CUSTO DIRETO*"`, a mesma
fórmula devolve o custo direto dos dezenove ambientes de uma vez.

## ⛔ DUAS ARMADILHAS QUE A REGRAVAÇÃO DO LAVABO ENSINOU [30/10]

**1 · DESMESCLE ANTES DE ESCREVER, não depois.** A ordem do `aba.py` é
"grade → conteúdo → formato", e ela está certa para aba NOVA. ⛔ Para aba
que se REESCREVE com outro layout, falta um passo: as MESCLAGENS ANTIGAS
ainda estão de pé na hora do conteúdo, e escrever dentro de uma mesclagem
grava só a célula do canto — o resto é descartado em silêncio, com o write
voltando "success". No Lavabo a linha do item caiu dentro da mesclagem
B:I de uma seção do layout velho: o "1" entrou, o nome do móvel, a medida
e o custo não, e a CONFERÊNCIA deu −R$ 1.061,10. ⭐ É a irmã gêmea do
"cresça a grade antes de escrever fórmula": o endereço falha, o write não.
⭐⭐ A receita: limpe os VALORES, mande o lote de FORMATO (que começa por
`unmergeCells`), e só então grave o conteúdo. Ou grave o conteúdo duas
vezes — a segunda já cai na grade nova.

**2 · A LINHA DE VIDRO LIA DUAS CHAVES FIXAS.** A ferragem é o RESTO —
tudo que tem chave, menos chapa, menos acabamento, menos vidro — e o
"menos vidro" subtraía literalmente `Vidro reflecta` e `Espelho`. ⛔ Mas a
chave do Lavabo é `Espelho prata colado`, a do Banho Master é `Porta de
espelho em alumínio` e a da Varanda é `Vidro temperado incolor`. Nenhuma
era subtraída: o espelho aparecia na linha de FERRAGEM e a linha "Vidro e
espelho" lia ZERO. ⭐ O total fechava — resto não perde dinheiro — mas a
CLASSIFICAÇÃO mentia, e é ela que o Painel soma por ambiente. Corrigido
no `aba.py`: a chave de vidro é a que o levantamento DECLARA.

**3 · E O AVISO QUE GRITAVA SEM MOTIVO.** Toda linha de vidro saía com
"⛔ A COTAR, segue sem preço na Base", inclusive as que TÊM preço — o
espelho prata colado custa R$ 600/m². ⭐ Aviso que grita onde não há nada
errado é aviso que o leitor aprende a não ler, e este é o único aviso que
a planilha tem para dizer que um total é PISO. Agora só sai se faltar.

## As dezenove estão gravadas e as dezenove conferem

Conferido pela fórmula de uma linha acima, em 30/10/2026: as dezenove
CONFERÊNCIAS leem **R$ 0,00**. ⭐ É a única prova de que nenhuma chave caiu
fora da Base — a aba sozinha não denuncia, porque compara ela consigo mesma.

**⛔⛔ DESMESCLE ANTES DE ESCREVER, NÃO DEPOIS.** O gerador manda na ordem
"grade → conteúdo → formato", e isso está certo para uma aba NOVA. Para uma
aba que se REESCREVE com layout diferente, as mesclagens VELHAS ainda estão
de pé quando o conteúdo entra — e escrever dentro de uma mesclagem guarda
só a célula de cima à esquerda e joga o resto fora, **com a gravação
devolvendo "success"**. É a gêmea de "cresça a grade antes de escrever
fórmula": o endereço falha, a escrita não. ⭐⭐ A receita: limpe os VALORES,
mande o lote de FORMATO (que começa por `unmergeCells`), e só então grave o
conteúdo. Foi assim que a Varanda entrou sem perder uma célula; o Lavabo,
gravado na ordem contrária, perdeu três e a CONFERÊNCIA deu −R$ 1.061,10.

**⛔ E O AVISO AINDA DIZIA A MESMA COISA DUAS VEZES.** O rótulo do vidro da
cristaleira trazia "⛔ A COTAR com o vidraceiro" escrito à mão no
levantamento, e o gerador acrescentava "⛔ A COTAR, segue sem preço na
Base". ⭐ A regra: o rótulo diz o que a peça É; o que falta na Base é o
gerador que conta. Tirei o texto à mão do `varanda.py`.

## Falta ligar

- Painel, linhas 24–43, e o quadro ④ de Preço e Comissões.
  O frete de cada ambiente acha-se pelo rótulo: `SUMIF(B:B;"Frete";F:F)`.
