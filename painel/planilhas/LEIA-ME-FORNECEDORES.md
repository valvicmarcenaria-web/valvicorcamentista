# Gestão de Fornecedores — Valvic

Cadastro de fornecedores com avaliação medida, não opinada.

**Arquivo:** `Valvic_Gestao_Fornecedores.xlsx`
**Gerador:** `gerar-gestao-fornecedores.py` — editar o script, nunca o `.xlsx`.

---

## As 6 abas

| Aba | Para quê |
|---|---|
| **Dashboard** | Nove indicadores do período e três quadros: por segmento, por situação e ocorrências por tipo |
| **Fornecedores** | O cadastro — 60 linhas, 25 colunas. Fundo creme = preencher; cinza-azulado = calculado |
| **Compras** | Uma linha por compra, 300 linhas. Alimenta volume, percentual e pontualidade |
| **Ocorrências** | Uma linha por problema, 150 linhas. Alimenta o índice de problemas |
| **Ficha do Fornecedor** | Página A4 de um fornecedor: escolhe o código e o resto se preenche |
| **Listas** | Listas suspensas, o **período de análise** e a explicação do score |

## O que você digita e o que a planilha mede

**Você digita:** empresa, segmento, insumos, CNPJ, vendedor, contato, e-mail, chave PIX e tipo,
métodos de pagamento, condição padrão, situação, pontos de atenção — e três notas de **1 a 5**
para **preço**, **atendimento** e **qualidade**.

**A planilha mede:** compras no período, **% de compra**, número de compras, ocorrências,
**índice de problemas**, **entregas no prazo**, score geral e data da última compra.

Essa separação é o ponto do arquivo. Percentual de compra e índice de problemas não podem ser
estimados de cabeça — eles saem do que de fato aconteceu, e é isso que faz a avaliação valer
alguma coisa em negociação.

## O score

```
Score = (Preço × 35%  +  Atendimento × 35%  +  Qualidade × 30%) × (1 − índice de problemas)
```

Escala de 0 a 5. O julgamento é seu; o histórico é que pondera.

| Situação | Score |
|---|---|
| Nota 5 em tudo, sem problemas | 5,00 |
| Nota 5 em tudo, 20% de problemas | **4,00** |
| Nota 3/4/4, 10% de problemas | 3,28 |
| Preço 5, atendimento 2, qualidade 3, 5% de problemas | 3,18 |

A terceira e a quarta linhas mostram a utilidade: **o fornecedor mais barato da praça pode
pontuar abaixo de um mediano** quando atendimento e histórico entram na conta.

## Período de análise

Duas células na aba Listas (`L2` e `L3`) definem o recorte. Por padrão vão de 1º de janeiro até
hoje. Mudou lá, o cadastro e o painel inteiro se recortam — dá para comparar semestres, ou olhar
só os últimos 90 dias antes de uma negociação.

## Sinais automáticos

- **Score** ganha escala de cor, do vermelho ao verde.
- **Índice de problemas ≥ 20%** fica vermelho.
- **Concentração ≥ 40%** num único fornecedor fica âmbar — é dependência que vira risco de preço e de abastecimento.
- **Entrega fora do prazo** fica vermelha na aba Compras.
- **Ocorrência grave** fica vermelha na aba Ocorrências.

## Como operar

1. Cadastre o fornecedor com código `FOR-001` e preencha os dados de contato e pagamento.
2. A cada compra, lance uma linha na aba **Compras** — com prazo prometido e data de entrega,
   que é o que gera a pontualidade.
3. Todo problema vira uma linha em **Ocorrências**, com tipo e gravidade.
4. Revise as três notas de 1 a 5 periodicamente — sugestão: a cada trimestre.
5. Antes de negociar, abra a **Ficha do Fornecedor** e leve os números para a mesa.

## Cinco fornecedores já cadastrados

Vieram do extrato financeiro de 08/08: **MADEGEM**, **Bigfer**, **JR Ferragens**,
**MGV Distribuidora** e **Ferragens Ipê**. Falta completar CNPJ, vendedor, contato e chave PIX.

## Ressalva

**Não foi possível recalcular as fórmulas neste ambiente** — o LibreOffice do runner esgota o
tempo mesmo com arquivo trivial. As **1.332 fórmulas** foram auditadas manualmente: referências
entre abas conferidas, e todas do conjunto Excel 2007 (`SUMIFS`, `COUNTIFS`, `INDEX`, `MATCH`,
`IFERROR`, `SUMPRODUCT`). Abrem normalmente no Excel e no Google Sheets.

Um cuidado que essa auditoria pegou: o denominador de "entregas no prazo" contava as células
com fórmula vazia, o que inflaria a base com as 300 linhas em branco. Agora ele soma
explicitamente os "Sim" e os "Não".
