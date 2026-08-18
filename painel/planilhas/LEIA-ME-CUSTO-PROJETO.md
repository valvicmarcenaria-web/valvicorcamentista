# Valvic — Custo Direto por Projeto

Arquivo: `Valvic_Custo_por_Projeto.xlsx`
Gerador: `gerar-custo-projeto.py` (edite o script, nunca o `.xlsx`)
Testes: `testar-custo-projeto.py` (143 verificações)

Uma lâmina por projeto, com todo o custo direto e indireto em **ORÇADO ×
REALIZADO × DESVIO**. É essa segunda coluna que transforma um controle de gasto
numa régua de eficiência do orçamento.

---

## Abas

| Aba | Para que serve |
|---|---|
| **Instruções** | Passo a passo, a cascata de cálculo e os cuidados. Imprimível em A4. |
| **Painel Geral** | Consolida todos os projetos. 6 KPIs, tabela de 40 slots, "onde o orçamento erra", leituras e 2 gráficos. |
| **Ficha Modelo** | O modelo. Duplique a cada projeto novo. |
| **Exemplo P-2026-041** | Ficha preenchida (R$ 90 mil, 4 ambientes) com o desfecho completo. |
| **Listas** | Equipe, vendedores e causas de retrabalho. |

---

## A cascata de cálculo

```
VALOR DE VENDA
(−) Impostos sobre a nota            % da venda
(−) Taxa de máquina de cartão        % da venda
(−) Taxas de transação (PIX/boleto)  R$
(−) Comissão de venda                % da venda
(−) Projeto / anteprojeto externo    R$
(−) RT do parceiro                   % de (venda − impostos − máquina − taxas)
(=) RECEITA LÍQUIDA          ← base das comissões operacionais
(−) Coordenação                      % da receita líquida
(−) Produção                         por ambiente, sobre a receita líquida
(−) Montagem                         por ambiente, sobre a receita líquida
(−) Material                         7 categorias
(−) Serviços terceirizados           4 linhas
(−) Logística                        5 linhas
(−) Retrabalho                       6 ocorrências
(=) MARGEM DE CONTRIBUIÇÃO DO PROJETO
```

Duas decisões que valem explicação:

**O RT tem base própria.** Incide sobre a venda menos impostos, máquina e taxas
de transação — como você especificou. No exemplo dá R$ 4.065,10 em vez dos
R$ 4.500 que sairiam de 5% sobre o bruto.

**As comissões operacionais são sobre a RECEITA LÍQUIDA, não sobre a venda.** O
marceneiro não é comissionado sobre o imposto nem sobre o RT do arquiteto. Isso
muda o número: 5% sobre R$ 90.000 seriam R$ 4.500; 5% sobre a líquida de
R$ 73.036,90 são R$ 3.651,85.

---

## Comissões por ambiente

Cada ambiente tem um valor em reais. A planilha calcula o peso dele no projeto e
aplica esse peso sobre a receita líquida — essa é a **base do ambiente**. Sobre
ela incidem dois percentuais independentes: o de quem produziu e o de quem montou.

O exemplo, exatamente como você descreveu:

| Ambiente | Valor | Peso | Produção | | Montagem | |
|---|---:|---:|---|---:|---|---:|
| Cozinha | 30.000 | 33,3% | Jackson 3% | 730,37 | Samuel 2% | 486,91 |
| Suíte | 20.000 | 22,2% | Samuel 3% | 486,91 | Cezar 2% | 324,61 |
| Lavanderia | 10.000 | 11,1% | Joelson 3% | 243,46 | Samuel 2% | 162,30 |
| Sala | 30.000 | 33,3% | Deivson 3% | 730,37 | Jackson 2% | 486,91 |

E o consolidado **por colaborador** sai sozinho, somando produção, montagem e
coordenação:

| Colaborador | Produção | Montagem | Coordenação | Total |
|---|---:|---:|---:|---:|
| Deivson | 730,37 | — | 730,37 | **1.460,74** |
| Jackson | 730,37 | 486,91 | — | **1.217,28** |
| Samuel | 486,91 | 649,21 | — | **1.136,12** |
| Cezar | — | 324,61 | — | **324,61** |
| Joelson | 243,46 | — | — | **243,46** |

A soma dos ambientes precisa fechar com o valor de venda — a linha de total
avisa quando não fecha.

---

## Retrabalho — a parte que mais ensina

Cada ocorrência tem **o que aconteceu · a causa (menu suspenso) · o custo
estimado · a providência**. O custo não precisa vir de nota fiscal; a sua
estimativa registrada vale mais que a exatidão não registrada.

No orçamento você lança a **contingência prevista**. O desvio entre ela e o
retrabalho real diz se a sua provisão está no tamanho certo.

Com o tempo a coluna Causa vira o dado mais valioso da planilha: se metade dos
retrabalhos é "erro de medição", o problema não é preço, é processo.

---

## O Painel Geral

Você duplica a Ficha Modelo, renomeia, e escreve **o nome da aba** numa linha
livre da coluna ABA. Todo o resto se preenche por `INDIRECT`. Nome errado ou aba
inexistente deixa a linha em branco — não quebra nada.

**Seis KPIs:** projetos, vendido, custo total, MC em reais, MC média e
**percentual de entrega no prazo**.

**Tabela de 40 projetos** com entrada, prevista, entregue, dias de atraso,
situação da entrega, venda, custo, MC em R$ e %, MC % orçada, o desvio em pontos
percentuais, o desvio de custo em reais e um diagnóstico automático
(Margem boa ≥ 35% · Margem apertada 25–35% · Margem crítica < 25%).

**"Onde o orçamento erra"** soma todos os projetos por categoria e mostra em qual
delas você mais estoura. É o retorno direto para ajustar a base de orçamento.

**Dois gráficos:** margem por projeto e desvio do orçamento por categoria.

---

## O que o exemplo conta

| | Orçado | Realizado | Desvio |
|---|---:|---:|---:|
| Custos de venda | 16.936,50 | 16.963,10 | +26,60 |
| Comissões operacionais | 4.383,81 | 4.382,21 | −1,60 |
| Material | 28.700,00 | 31.415,00 | **+2.715,00** |
| Serviços terceirizados | 7.200,00 | 8.150,00 | +950,00 |
| Logística | 2.000,00 | 2.715,00 | +715,00 |
| Retrabalho | 1.500,00 | 2.370,00 | +870,00 |
| **Custo total** | **60.720,31** | **65.995,31** | **+5.275,00** |
| **Margem de contribuição** | **29.279,69 (32,5%)** | **24.004,69 (26,7%)** | **−5.275,00** |

O orçamento previa 32,5% e o projeto entregou 26,7%. Quase metade do estouro veio
de **material** — e é exatamente esse tipo de conclusão que a planilha existe para
produzir. Entrega prevista 30/07, real 06/08: **7 dias de atraso**.

---

## Sinais visuais

| Cor | Significa |
|---|---|
| Creme | você preenche |
| Cinza-azulado | calculado — não digite |
| Faixa navy | subtotal ou linha-chave (receita líquida, custo total, MC) |
| Desvio em vermelho | gastou mais que o orçado |
| Desvio em verde | gastou menos que o orçado |
| Verde / âmbar / vermelho no Painel | margem boa / apertada / crítica · entrega no prazo / atrasada |

---

## Limites conhecidos

- **Não insira nem apague linhas dentro da ficha.** O Painel procura os números
  em endereços fixos (`A13`, `C13`, `E13`, `G13`, `H13`, `I13`, `A7`, `A9`, `F7`,
  `H7`, `J7`, `H9`, `J9`, `C107:D112`). Mudou a forma da ficha, o painel lê a
  célula errada. Use as linhas de sobra de cada bloco.
- **40 projetos no Painel.** Para mais, é preciso regerar pelo script.
- **10 ambientes, 12 colaboradores e 6 retrabalhos** por ficha.
- **A ficha não tem gráfico de propósito.** Gráfico dentro de aba duplicada tende
  a continuar apontando para a aba original; a composição de custo já está na
  tabela de resumo, com o % da venda ao lado de cada categoria.
- **Nome de aba com apóstrofo quebra o `INDIRECT`.** Evite `Projeto d'Ávila`.
- **A margem aqui é de CONTRIBUIÇÃO** — ainda não paga o custo fixo da empresa.
  Um projeto com 30% de MC não deu 30% de lucro.

---

## Fórmulas

Só funções da base do Excel 2007 (`IF`, `AND`, `OR`, `SUM`, `SUMIF`, `COUNTA`,
`COUNTIF`, `COUNT`, `AVERAGE`, `ROUND`, `MAX`, `MIN`, `INDEX`, `MATCH`, `TEXT`,
`LEFT`, `TODAY`, `INDIRECT`, `IFERROR`). Sem macro. Abre em qualquer versão do
Excel, no LibreOffice e no Google Planilhas.

---

## Testes

```
python3 gerar-custo-projeto.py     # gera o .xlsx
python3 testar-custo-projeto.py    # 143 verificações, 0 falha
```

O teste calcula as fórmulas de verdade (biblioteca `formulas`) e confere a ficha
inteira contra um modelo independente escrito em Python: a cascata de custos de
venda, a receita líquida, a comissão de cada ambiente, o consolidado por
colaborador, o resumo por categoria, a margem, a faixa de resultado do topo e o
cálculo de atraso na entrega. Confere também que a ficha em branco não gera lixo
e que o modelo e o exemplo têm **exatamente as mesmas fórmulas**.

Para o Painel Geral, o teste resolve o `INDIRECT` à mão — o motor não avalia nome
de aba dinâmico — e confirma que **cada coluna aponta para o endereço certo** da
ficha, que é onde mora o risco real.

Uma nota sobre centavos: quando o `ROUND` cai sobre um produto em ponto flutuante
cujo 16º dígito decide o arredondamento (`0,03 × 73.063,50` = `2191.9049999999997`),
o motor de teste e o Excel podem divergir em R$ 0,01. Os testes desses valores
aceitam essa tolerância, e em compensação verificam **exatamente** que o custo
total é a soma das seis categorias e que o consolidado por pessoa fecha com o
subtotal das comissões.
