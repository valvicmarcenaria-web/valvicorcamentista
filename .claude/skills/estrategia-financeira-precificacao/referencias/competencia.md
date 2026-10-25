# Análise por competência × caixa

Dois relógios diferentes olhando o mesmo dinheiro:

- **Regime de caixa** — quando o dinheiro **entrou ou saiu** da conta. Responde:
  *"vou ter dinheiro para pagar a folha dia 5?"* → **fluxo de caixa**.
- **Regime de competência** — quando o fato **aconteceu** (móvel entregue,
  material consumido, salário trabalhado), não importa quando foi pago. Responde:
  *"este mês deu lucro?"* → **DRE**.

Misturar os dois é o erro mais comum (e mais caro) em marcenaria: o mês em que
entra a entrada de três contratos parece lucrativo, o mês em que se paga a chapa
parece prejuízo — e nenhum dos dois é verdade. **Sempre dizer em qual regime um
número está.**

## 1. Regras de competência para a Valvic

| Fato | Competência (DRE) | Caixa (fluxo) |
|---|---|---|
| Entrada/sinal recebido | **Não é receita.** Passivo "Adiantamento de clientes" | Entrada no dia do recebimento |
| Receita do projeto | **Mês da entrega/instalação** (regra Valvic). Projeto grande entregue em etapas → reconhecer por ambiente entregue | Conforme parcelas |
| Venda parcelada no cartão | Receita inteira na entrega; a taxa da maquininha é **dedução/custo de venda** no mesmo mês | Cada parcela em D+30, D+60… (ou antecipada com custo financeiro) |
| Compra de chapa/ferragem | **Estoque / obra em andamento** até o projeto ser entregue → aí vira CPV daquele projeto | Na data de pagamento do boleto |
| Chapa comprada e não usada (sobra) | Continua no estoque; não é custo do mês | Já saiu do caixa |
| Terceirizado (vidro, laca…) | Custo do projeto no mês da entrega do projeto | Sinal + saldo, nas datas pagas |
| Comissão do vendedor | Custo de venda na competência da **receita** do projeto | Quando paga |
| RT do arquiteto | Custo de venda na competência da receita | Quando paga ao arquiteto |
| NF / impostos sobre venda | Mês de **emissão da NF** | Mês seguinte (guia DAS) |
| Salários | Mês trabalhado | Até o 5º dia útil do mês seguinte |
| 13º e férias | **Provisão mensal** (≈ 1/12 do 13º + 1/12 de férias + 1/3 + encargos ≈ 11–12% da folha) | Nov/dez (13º) e no gozo das férias |
| Aluguel do galpão | Mês de uso | Data do boleto |
| Financiamento de máquina | **Só os juros** são despesa financeira; o principal reduz a dívida; a máquina vira **depreciação** (CNC ~10 anos) | Parcela inteira |
| Compra de máquina à vista | **Ativo imobilizado** + depreciação mensal | Saída integral no pagamento |
| Empréstimo do Paulo (sócio) | Entrada = passivo com sócio; devolução reduz passivo; nenhum dos dois é receita/despesa (só juros, se houver) | Entradas e saídas reais |
| Garantia/assistência | **Provisão** no mês da entrega (ex.: 1–2% da receita) | Quando o gasto ocorre |

## 2. DRE gerencial por competência (modelo Valvic)

```
(+) Receita bruta de projetos entregues no mês
(−) Deduções: impostos sobre NF, devoluções/abatimentos
(=) Receita líquida
(−) Custos variáveis do projeto (CPV): chapas, fita, ferragens, LED, vidro,
    terceirizados, frete, embalagem
(−) Custos variáveis de venda: comissões, RT, taxa de maquininha, visitas
(=) MARGEM DE CONTRIBUIÇÃO (R$ e %)            ← compara com a MC do orçamento
(−) Custos fixos de produção: salários + encargos + provisões da fábrica,
    energia, manutenção
(−) Despesas fixas administrativas/comerciais: pró-labore, contador,
    sistemas, aluguel, marketing
(=) RESULTADO OPERACIONAL (EBITDA gerencial)
(−) Depreciação (CNC, coladeira, veículos)
(−/+) Resultado financeiro: juros de financiamento, antecipação de recebíveis
(=) RESULTADO LÍQUIDO
```

Abaixo da DRE, **separado**, o que só afeta o caixa: amortização de principal
(máquinas, Paulo), investimentos em ativo, variação de adiantamentos de clientes
e de estoque. A "ponte DRE → caixa" do mês é:

```
Resultado líquido
+ depreciação e provisões (não saem do caixa no mês)
+ aumento de adiantamentos de clientes (sinais recebidos de projetos não entregues)
− aumento de contas a receber (entregue e ainda não pago)
− aumento de estoque/obra em andamento (chapa comprada para projeto futuro)
+ aumento de contas a pagar a fornecedor
− amortização de principal de dívidas − investimentos
= Variação do caixa do mês
```

Se a ponte não fecha com o extrato, há erro de lançamento — é ponto de auditoria.

## 3. As duas MCs da Valvic (não confundir)

O CENTRAL registra **MC 64,5% (DRE Calcme)** e **MC 43,5% (orçamento)**. A
diferença vem de **onde a mão de obra direta foi classificada**: no Calcme a
folha da fábrica está em "Despesas Administrativas" e o CPV só tem material; no
orçamento, comissões, terceirizados e encargos de venda entram como variáveis.

Ao comparar, **reclassificar para a mesma régua** antes de concluir qualquer
coisa. Regra prática: o Rodrigo decide preço com a **MC do orçamento**
(variáveis completos) e calcula o break-even da empresa com a mesma régua —
ou seja, se usar 43,5% de MC, o custo fixo é o que sobra **fora** do
orçamento (folha, galpão, admin), sem duplicar comissões.

## 4. MC orçada × MC realizada por projeto

A auditoria mais valiosa para uma marcenaria. Para cada projeto entregue:

| Linha | Orçado (Lavinia) | Realizado (NFs + pagamentos vinculados) | Δ |
|---|---|---|---|
| Preço / receita | | | |
| Material (chapas, fita, ferragens) | | | |
| Terceirizados | | | |
| Comissões + RT + NF + maquininha | | | |
| Logística / montagem | | | |
| **MC R$ / MC %** | | | |

Desvio > 3 pontos de MC → causa raiz (preço de chapa subiu? retrabalho? item
esquecido no quantitativo? desconto não registrado?) e **devolver a lição para
a Lavinia** (calibração em `orcamentista-marcenaria/projetos/treino/`).

## 5. Como trabalhar uma análise de competência

1. **Pergunte ou descubra o regime da fonte.** Export do Calcme de "contas
   pagas/recebidas" é caixa; DRE do Calcme costuma ser competência, mas
   confirme a configuração (data de vencimento? de pagamento? de emissão?).
2. **Liste os eventos que mudam de mês entre os regimes** (sinais, compras de
   chapa antecipadas, 13º, parcela de máquina, cartão parcelado).
3. **Reclassifique** linha a linha, deixando rastro (coluna "origem" e
   "ajuste de competência").
4. **Feche a ponte DRE → caixa.** Diferença não explicada = achado.
5. **Conclua em linguagem de dono**: "em outubro a empresa lucrou X por
   competência, mas o caixa caiu Y porque recebeu sinais de entregas futuras a
   menos do que pagou de chapas para elas".
