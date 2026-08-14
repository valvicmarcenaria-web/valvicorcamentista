# Valvic — Controle de Pagamentos de Projetos

Arquivo: `Valvic_Controle_Pagamentos.xlsx`
Gerador: `gerar-controle-pagamentos.py` (edite o script, nunca o `.xlsx`)
Extração: `extrair-pagamentos.py` · Testes: `testar-pagamentos.py` (1.422 verificações)

Reconstrução da planilha-mãe de faturamento e recebíveis. **O layout de digitação é o
mesmo de sempre** — um projeto por linha, os pagamentos à direita, uma aba por ano,
cinco pagamentos por projeto. O que mudou foi o que estava quebrado por baixo.

---

## Abas

| Aba | Para que serve |
|---|---|
| **Painel** | 6 KPIs, ano a ano, mês a mês com acumulado × meta, 12 maiores saldos e leituras automáticas. Dois gráficos. Não se digita nada aqui. |
| **Análise & Sazonalidade** | Fluxo de caixa pela data do pagamento, padrão sazonal de vendas com índice e dispersão, concentração da carteira. Três gráficos. |
| **2026 · 2025 · 2024 · 2023** | Uma aba por ano, no layout de sempre. É onde se lança. |
| **Aporte Walton** | Entradas, saídas e investimentos do aporte, com saldo calculado. |
| **Crédito Samuel** | Lançamentos e total acumulado. |
| **Listas** | Alimenta os menus e diz quais linhas são divisoras de mês. |
| **Notas de migração** | O que foi corrigido e o que ficou pendente. **Leia antes de usar.** |

---

## A correção mais importante: as datas

**67 datas estavam com o dia e o mês trocados.** Um pagamento de 5 de fevereiro estava
gravado como 2 de maio.

A causa: em algum momento o arquivo foi editado por uma ferramenta configurada em
inglês, que lê `05/02` como mês 05, dia 02.

A prova é que a separação é perfeita nas quatro abas:

| | quantidade | característica |
|---|---:|---|
| Viraram data | 67 | **todas** com dia ≤ 12 e mês ≤ 12 — as únicas que a ferramenta conseguia inverter |
| Ficaram texto | 113 | **todas** com o primeiro número > 12 — as que ela não conseguia converter |
| Data com dia > 12 | 0 | quebraria a hipótese |
| Texto com 1º número ≤ 12 | 0 | quebraria a hipótese |

Nenhuma exceção nos dois sentidos. As 67 foram desinvertidas e as 113 viraram data de
verdade — agora dá para ordenar, filtrar e somar por período. Uma única não pôde ser
recuperada: `23.0` na linha 17 de 2023 (Cristiane).

---

## O que mais foi corrigido

- **"Status atual" era o saldo.** Virou `Saldo a receber`, com `% recebido` e `Situação`
  (Quitado · Parcial · A receber · Recebido a mais) coloridos ao lado.
- **A fórmula do saldo** era `=SUM(C10-H10-L10-...)` e devolvia o valor do contrato em
  linha vazia. Agora fica em branco quando não há projeto.
- **O total do ano** era uma lista fixa de células (`=SUM(C9,C13,C20...)`) que passava a
  somar errado assim que alguém inserisse uma linha. Agora é calculado sobre todas as
  linhas de projeto, com uma **CONFERÊNCIA** no topo que avisa se alguma linha ficou
  fora de um bloco de mês.
- **2023 estava somando 10 meses de 12.** A lista fixa nunca incluiu dezembro. O total
  correto do ano é R$ 710.884, não os R$ 645.614 que vinham sendo usados.
- **A "Meta mensal"** era a meta anual dividida por 7 — um número que mudava sozinho.
  Saiu; entraram `% da meta` e `falta para a meta`.
- **22 células da coluna Data** continham a forma de pagamento (`pix`, `material`,
  `permuta`). O texto foi para a Descrição.
- **Linhas de resumo duplicadas** no meio das abas 2023 e 2024 (com fórmulas soltas em
  vez de dados) foram removidas.
- **De 33 para 24 colunas**, sem perder nada: as colunas vazias de separação saíram.
- **Linhas de sobra em branco** em cada bloco de mês, para lançar projeto novo sem
  precisar inserir linha.

---

## Divergências que continuam abertas

**Monte Negro (2024, casa completa, contrato de R$ 100.000).** Existem sete pagamentos
em linhas soltas somando R$ 97.800, mais R$ 22.200 no segundo bloco — R$ 120.000 contra
um contrato de R$ 100.000. A fórmula original somava só as cinco primeiras linhas
(`=SUM(H33:H37)` = R$ 77.800), o que fechava exatamente os R$ 100.000: dois pagamentos
de R$ 10.000 foram lançados depois e nunca entraram na conta.

Os sete pagamentos foram trazidos — apagar dinheiro recebido é pior do que mostrar a
inconsistência. O projeto aparece como **Recebido a mais** e 2024 fecha com saldo de
−R$ 20.000. Decidir: o contrato subiu, ou esses lançamentos são de outro projeto?

**Os 12 projetos no topo de 2023** são contratos de 2022 ainda em cobrança. Ficaram num
bloco `Anterior (2022)` e continuam **fora** do total de 2023, como já era no original.

---

## Números depois da migração

| Ano | Vendido | Recebido | A receber | % recebido |
|---|---:|---:|---:|---:|
| 2026 | 1.302.747 | 612.795 | **689.952** | 47% |
| 2025 | 1.566.491 | 1.522.391 | 44.100 | 97% |
| 2024 | 1.072.980 | 1.092.980 | −20.000 | — |
| 2023 | 710.884 | 710.884 | 0 | 100% |

210 projetos migrados. Nenhum valor de contrato ou de pagamento foi alterado — só data,
posição de texto e fórmula.

---

## O Painel

**Seis KPIs** do ano corrente: vendido, recebido, a receber, % recebido, nº de projetos e
ticket médio.

**Ano a ano** — os quatro anos lado a lado, com ticket médio, mais um gráfico de barras
comparando vendido × recebido.

**Mês a mês** — vendas, recebimentos e saldo de cada mês, mais duas colunas que decidem o
ano: `Acum. vendido` e `Meta acum.` (meta anual ÷ 12 × mês). O acumulado fica verde
quando está à frente da meta e vermelho quando está atrás, e **para no mês corrente** —
não estica uma linha falsa até dezembro. O gráfico combina as barras de venda e
recebimento com as duas linhas de acumulado.

**Maiores saldos em aberto** — os 12 maiores, com o % que cada um representa do total a
receber.

**Leitura do quadro** — três frases montadas pelas próprias fórmulas, que se reescrevem
quando os números mudam:

- concentração dos 3 maiores saldos sobre o total a receber;
- ritmo do ano contra a meta acumulada **até o mês corrente** (usa `TODAY()`);
- quantos projetos não receberam nada e quanto somam de contrato.

---

## A aba Análise & Sazonalidade

### Fluxo de caixa realizado

Doze meses × quatro anos, somando os pagamentos **pela data do pagamento**, não pela data
do contrato. É a pergunta "quanto dinheiro entrou em outubro?", que a planilha antiga não
conseguia responder porque as datas estavam corrompidas.

A coluna `Peso no ano` mostra quanto cada mês representa do caixa médio anual. O padrão
que aparece:

| Mês | Peso no caixa |
|---|---:|
| Outubro | 20,5% |
| Julho | 13,4% |
| Setembro | 12,1% |
| Janeiro | 1,8% |
| Dezembro | 1,9% |

O cálculo varre as cinco colunas de pagamento das quatro abas de ano — 20 `SUMIFS` por
célula — e inclui o bloco `Anterior (2022)`, porque contrato de 2022 pago em 2023 é caixa
de 2023.

### Padrão sazonal de vendas

Mesma matriz, mas por data de contrato, com quatro colunas de análise:

```
Média 23–25   → média dos três anos fechados (2026 fica de fora, o ano não acabou)
Índice        → média do mês ÷ média geral mensal.  1,00 = mês médio
Dispersão     → desvio padrão ÷ média dos três anos
Classificação → Forte (≥1,20) · Fraco (≤0,80) · Normal · Irregular (dispersão > 0,70)
```

**A coluna Dispersão é o que separa padrão de ruído.** Setembro tem o maior índice do ano
(2,43) e mesmo assim é marcado como Irregular: os três anos foram R$ 63k, R$ 43k e
R$ 573k. Não é sazonalidade, é o setembro de 2025 sozinho.

O que sobra depois desse filtro:

| Mês | Índice | Dispersão | Classificação |
|---|---:|---:|---|
| Março | 1,38 | **0,12** | Forte |
| Junho | 1,07 | 0,55 | Normal |
| Outubro | 1,15 | 0,63 | Normal |
| Agosto | 0,35 | 0,50 | Fraco |

Março é o único mês com padrão realmente sólido: R$ 130k, R$ 141k e R$ 112k em três anos
seguidos. Seis dos doze meses são Irregulares.

### Concentração da carteira

Por ano: nº de projetos, ticket médio, maior projeto e seu peso, top 3 e seu peso, com
classificação automática (Distribuído · Concentrado · Muito concentrado).

### Ressalvas

Estão escritas dentro da aba, e são para levar a sério:

1. Três anos fechados é pouco para afirmar sazonalidade — o índice é sinal, não previsão.
2. A operação começou em março de 2023; janeiro e fevereiro daquele ano puxam a média
   para baixo.
3. Setembro de 2025 (R$ 572 mil em dois mega-projetos) distorce o mês inteiro.
4. 2026 aparece nas tabelas mas fica fora do cálculo da média.

---

## Como usar

1. Abrir a aba do ano e achar o bloco do mês.
2. Preencher **Cliente · Projeto · Investimento · Forma de pagamento** nas quatro
   primeiras colunas (fundo creme).
3. Conforme o dinheiro entra, lançar **valor · data · descrição** no próximo bloco de
   pagamento livre.
4. `Recebido`, `Saldo a receber`, `% recebido` e `Situação` saem sozinhos.
5. Se o bloco do mês acabar as linhas de sobra, inserir linha **dentro** do bloco (nunca
   na primeira nem na última) — a conferência do topo avisa se algo escapar.

### Cores

| Cor | Onde | Significa |
|---|---|---|
| Creme | Cliente, Projeto, Investimento, Forma, pagamentos | você digita |
| Cinza-azulado | Recebido, Saldo, %, Situação | calculado |
| Verde | Situação | Quitado |
| Âmbar | Situação | Parcial |
| Vermelho | Situação e a linha inteira | nada recebido |
| Azul | Situação | Recebido a mais — conferir |

---

## Limites conhecidos

- **Cinco pagamentos por projeto.** Um projeto de 2024 (Monte Negro) tinha oito; os três
  últimos foram somados no 5º bloco, com o detalhe na Descrição.
- **A conferência cobre a coluna Investimento**, não os pagamentos. Uma linha de
  pagamento fora de um bloco de mês ainda entra no total do ano (o recebido é somado
  pelas colunas de pagamento inteiras), mas não aparecerá no mês certo.
- **O ranking de maiores saldos** usa `LARGE`; com dois saldos exatamente iguais, mostra
  o primeiro da lista duas vezes.
- **As colunas X e Y estão ocultas** — são auxiliares do ranking e da concentração
  (repetem saldo e valor do contrato só nas linhas de projeto). Não apagar.
- **Os gráficos apontam para faixas fixas** do Painel e da Análise. Se você inserir linhas
  nessas duas abas, os gráficos não acompanham — regere pelo script.
- **A sazonalidade usa 2023, 2024 e 2025.** Quando 2026 fechar, ajuste `ANOS_CHEIOS` no
  gerador para incluí-lo.
- **A meta de cada ano** é digitada (célula I7 da aba do ano). 2024 e 2023 estão zeradas.

---

## Fórmulas

Só funções da base do Excel 2007 (`IF`, `SUM`, `SUMPRODUCT`, `COUNT`, `COUNTIF`,
`SUMIF`, `SUMIFS`, `AVERAGE`, `STDEV`, `ROUND`, `MAX`, `MIN`, `LARGE`, `INDEX`, `MATCH`,
`TEXT`, `DATE`, `TODAY`, `MONTH`, `OR`, `AND`). Abre em qualquer versão do Excel, no
LibreOffice e no Google Planilhas.

Os gráficos são nativos do Excel (`barChart` / `lineChart`), sem imagem e sem macro.

---

## Testes

```
python3 extrair-pagamentos.py       # relatório da extração e das correções
python3 gerar-controle-pagamentos.py
python3 testar-pagamentos.py        # 1.422 verificações, 0 falha
```

`testar-pagamentos.py` calcula as fórmulas de verdade e reconcilia contra a planilha
original: cliente por cliente confere contrato e pagamentos, linha por linha confere
Recebido/Saldo/%/Situação, mês a mês e ano a ano confere os totais, confere o espelho do
Painel, o ranking dos maiores saldos, se sobrou alguma data como texto e os totais do
Aporte Walton e do Crédito Samuel.

Cobre também as tabelas novas: cada célula do fluxo de caixa contra a soma independente
dos pagamentos por data, cada célula da sazonalidade contra as vendas por mês, o cálculo
do índice, e se os cinco gráficos apontam para faixas de categorias e valores do mesmo
tamanho.
