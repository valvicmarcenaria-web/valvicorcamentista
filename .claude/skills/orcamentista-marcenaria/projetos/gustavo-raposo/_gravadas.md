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

## Ligado: Painel (24–42) e quadro ④ (41–59)

**⛔⛔ A UNIDADE É O QUE SEPARA O PAINEL DO BLOCO DE PEÇAS.** A coluna F quer
dizer CUSTO no painel de material e QUANTIDADE no bloco de peças, e há
rótulo que vive nos dois — "Fita cor" é linha de painel E é linha de peça.
Somar `F:F` só pelo rótulo mistura dinheiro com metro linear, e o total sai
maior sem ninguém reclamar. ⭐ No painel a UN mora em E; no bloco de peças E
é a largura. Casar E com a unidade é o filtro que separa os dois mundos:

```
MDF      SUMIFS(aba!$F:$F; aba!$B:$B;"MDF*";       aba!$E:$E;"chapas")
CHAPAS   SUMIFS(aba!$D:$D; aba!$B:$B;"MDF*";       aba!$E:$E;"chapas")
FITA     SUMIFS(aba!$F:$F; aba!$B:$B;"Fita*";      aba!$E:$E;"m")
FERRAGEM SUMIFS(aba!$F:$F; aba!$B:$B;"Ferragem*";  aba!$E:$E;"peças")
FRETE    SUMIFS(aba!$F:$F; aba!$B:$B;"Frete";      aba!$E:$E;"viagem")
ITENS    COUNTIF(aba!$B:$B;"ITEM *")
CUSTO    INDEX(aba!$F:$F; MATCH("CUSTO DIRETO*"; aba!$B:$B; 0))
```

**⭐ E A COLUNA J NÃO É UM RESTO CALCULADO POR SUBTRAÇÃO.** Ela soma pelo
nome a filetagem (automática e manual), o vidro e espelho, os dois cortes,
os consumíveis e a embalagem — e é por isso que a **linha 45 do Painel**
pode conferir se as colunas somam o CUSTO DIRETO. Se o painel de material
ganhar uma linha nova e ninguém a trouxer para o Painel, a linha 45 grita.
Com J definida por subtração, ela nunca gritaria — e um bucket esquecido
ficaria invisível para sempre.

**⛔⛔ DOIS DEFEITOS NO PREÇO E COMISSÕES, ACHADOS AO LIGAR [30/10/2026].**

**1 · Toda a coluna "EM R$" do bloco ② apontava para `$D$33`, e o PREÇO DE
VENDA mora em `$E$33`.** Também `E27` (BASE em R$), `D34` (MC média
realizada) e `E35` (a própria CONFERÊNCIA do bloco ③). ⭐ Estava invisível
enquanto o quadro ④ não tinha preço: zero vezes qualquer coisa é zero, e a
conferência lia 0 − 0 − 0 − 0 = zero. No instante em que o preço apareceu,
a conferência foi a −R$ 182.604,91 e denunciou o erro. **Guarda que só
funciona quando os números chegam ainda é guarda — mas não prova nada
enquanto a planilha está vazia.**

**2 · O VLOOKUP da DIFICULDADE lia `$B$66:$D$68` — e "Complexo" está na
linha 69.** Escolher o nível MAIS DIFÍCIL caía no IFERROR, voltava zero de
acréscimo e dava MC 40% — **menos que os 45% de "Médio"**. Isto é, pedir
mais dificuldade BAIXAVA o preço. Corrigido para `$B$67:$D$69` e provado na
18 Banho Social: Complexo passou a dar 60,0% e R$ 6.447,96 contra os
R$ 4.022,40 de Médio.

## ⛔ O PREÇO É PISO: 16 linhas saem ZERO por falta de preço na Base

A **linha 46 do Painel** conta isto sozinha, e a conta é MECÂNICA: varre as
dezenove abas e soma as linhas de peça cujo `R$ UN` não é número — as que o
PROCV não achou. ⭐⭐ Foi ela que achou a **Moldura provençal** da Cozinha e
a **Serralheria estrutural** da Suíte Master, que a minha varredura à mão
pelos levantamentos tinha deixado passar: eu só olhei os blocos OUTRAS e
VIDRO, e essas duas vêm de MOLDURA e SERRALHERIA. **A varredura que lê a
planilha achou mais do que a varredura que lê o meu modelo da planilha.**

| chave | quanto | onde |
| --- | --- | --- |
| Usinagem de encaixe meia-madeira | 7.144 encaixes | 07 Office |
| Moldura provençal | 14 frentes | 03 Cozinha |
| Usinagem de friso | 62,7 m | 11 Suíte 01 (29,7) · 13 Suíte 02 (33) |
| Puxador NEO32 Bronze | 8 un | 01 Varanda (2) · 11 Suíte 01 (4) · 16 Hóspedes (2) |
| Corrediça de carga | 3 pares | 11 Suíte 01 (1) · 13 Suíte 02 (2) |
| Rodízio de gaveteiro | 4 un | 11 Suíte 01 |
| Vidro temperado incolor | 2,4963 m² | 01 Varanda |
| Puxador a definir | 2 un | 13 Suíte 02 |
| Serralheria estrutural | ⚠ nem a quantidade | 08 Suíte Master |

⛔⛔ Os **7.144 encaixes de meia-madeira do Office** são o maior buraco: são
os 76 × 47 cruzamentos da grade do muxarabi, dois entalhes por cruzamento. O
corte reto está pago (R$ 425); o entalhe, que É o móvel, não está pago de
jeito nenhum.

## ⭐ A varredura de vidro, que a CONFERÊNCIA não faz

A CONFERÊNCIA de uma aba compara total com total, então o espelho lançado
como FERRAGEM fecha igual: ela pega DUPLICATA, não pega TROCA. A única
prova é ler a linha de vidro de todas as abas, e ela fecha:

| aba | área | custo | a conta |
| --- | --- | --- | --- |
| 01 Varanda | 2,4963 m² | R$ 0,00 | 2 × 78,5 × 159 · sem preço na Base |
| 02 Lavabo | 1,7685 m² | R$ 1.061,10 | 65,5×210 + 65,5×60 · × R$ 600 |
| 10 Banho Master | 2,1504 m² | R$ 1.505,28 | 3 × 56 × 128 · × R$ 700 |
| 11 Suíte 01 Filhos | 4,0545 m² | R$ 2.432,70 | 67×255 + 92×255 · × R$ 600 |
| as outras quinze | 0 | R$ 0,00 | nenhuma declara vidro |

## Onde o projeto está, em números

| | |
| --- | --- |
| Custo direto, 19 ambientes | R$ 161.808,24 |
| Encargos, 15,13% do preço | R$ 61.375,54 |
| MC alvo escolhida | 40,0% |
| MC média realizada, com os 19 em "Médio" | 45,0% |
| **PREÇO DE VENDA** | **R$ 405.788,69** |
| Margem de contribuição | R$ 182.604,91 |

⚠ **"Médio" já soma 5 pontos sobre a alvo**, então a MC realizada nunca sai
igual à alvo: 45% é o PISO do projeto, não um desvio. Corrigi o texto da
linha 60 do Painel, que dizia o contrário.

## Falta decidir, e é do Jonathan

- **A DIFICULDADE dos 19 está toda em "Médio"**, que é o piso. O 07 Office
  (grade de 170 réguas entalhadas em meia-madeira, filetagem manual) não é
  "marcenaria de caixa" pela definição do quadro ⑤ — é Difícil ou Complexo.
  A 03 Cozinha com 14 frentes de moldura provençal, a mesma coisa. ⛔ Não
  mexi: a dificuldade é julgamento de quem produz.
- **Pergolado (prancha 11) e SPA (prancha 17)** entram no escopo?
- As três perguntas antigas: desempenador de porta, os espelhos de moldura
  dourada dos quatro banheiros, e as oito almas de 120,75 do Homeschooling
  contra uma divisória.
- ⚠ O bloco **O LUCRO DO PROJETO** (Painel, linhas 61–70) traz o custo fixo
  mensal da empresa. **Esconder antes de abrir a planilha ao cliente.**
