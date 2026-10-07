# DOUGLAS — proposta de fechamento

Empreendimento comercial. Proposta v1 de apresentação já enviada (balcão,
painéis, escaninho, copa). O cliente está **abrindo o empreendimento e
decidiu esperar para investir na marcenaria** — esta proposta existe para
**segurar o serviço**.

Cálculo: `calculo-douglas.py` · proposta: `build-douglas.py`.

---

## 07/10/2026 — a estrutura, e os dois cenários

> *"refaça o orçamento do Douglas em nosso padrão premium · antes, considere
> o item M07 Painel e móvel como um total de 3 itens · o documento tem que
> ser uma proposta de fechamento, não de apresentação da marcenaria ·
> entrada para reserva de agenda 20%, o restante em 4 boletos sem juros
> (valor cheio) a partir de 60 dias · me apresente a estrutura de cálculo
> antes de montar a proposta"*

### A base

**M07 "Painel e móvel" passa a contar 3 unidades** — o PDF v1 já dizia
"cada unidade" e cobrava R$ 4.900. O investimento sai de **R$ 58.050** para
**R$ 67.850** (+R$ 9.800).

⛔ Não há motor de custo deste projeto. A v1 não saiu de um motor da casa —
**só temos os preços de venda por item**. Dá para calcular o total, a escada
e o perfil de caixa; **não dá para calcular MC**.

### ⭐ A escada cai redonda

20% de 67.850 = **R$ 13.570**. E 80% ÷ 4 = **R$ 13.570**.
**Os cinco pagamentos são idênticos** — o que dá ao fechamento uma frase que
não precisa de explicação: *cinco parcelas iguais, a primeira reserva a
agenda e as outras quatro só começam em 60 dias.*

### ⭐ O achado que sustenta o cenário 2

A valor presente, **à mesma taxa de 1,2% ao mês que a casa já cobra por
parcela de cartão** — a taxa da própria casa, de propósito, para não
escolher um número conveniente:

| | nominal | valor presente |
|---|--:|--:|
| 30% + 10× cartão | 67.850 | 64.860 |
| 50% + 8× cartão (3% desc.) | 65.814 | 64.106 |
| 70% + 6× cartão (5% desc.) | 64.458 | 63.671 |
| 70% + transferência (7% desc.) | 63.100 | 62.654 |
| **20% + 4 boletos a partir de 60d** | **67.850** | **65.635** |

**Esperar sai mais barato que descontar.** O cenário de adiamento é o melhor
de todas as formas de pagamento que a v1 oferecia — R$ 2.981 acima da opção
de 7% de desconto.

### ⚠ O que o valor presente não mostra

**Caixa não é valor presente.** No dia 0 entram R$ 13.570, que pela régua da
casa cobre mais ou menos só a chapa. E são **boletos, sem a garantia do
cartão**: 80% é recebível depois do trabalho feito.

A estrutura que resolve sem mexer no preço é **amarrar a produção ao
primeiro boleto, não à entrada** — que é o que "entrada para reserva de
agenda" já diz. Produção começa no dia 60, 60 dias de execução, entrega no
dia 120: na entrega a casa já recebeu 80%.

Na proposta isso virou: *"a entrada reserva sua vaga na produção; a data de
início é combinada na assinatura"*.

---

## ⛔⛔ 12% POR CIMA NÃO REPÕE 12% DE TAXA

> *"vamos acrescentar 12% no percentual a ser dividido no cartão"*

A taxa incide sobre o valor **já acrescido**:

| | como pedido (+12%) | neutro (÷ 0,88) |
|---|--:|--:|
| total parcelado | 60.793,60 | 61.681,82 |
| **10 parcelas de** | **6.079,36** | **6.168,18** |
| taxa de cartão (12%) | 7.295,23 | 7.401,82 |
| líquido da parte parcelada | 53.498,37 | **54.280,00** |
| a casa recebe | 67.068,37 | **67.850,00** |

**Faltam R$ 781,63.** O acréscimo que repõe a taxa é **+13,64%**, não +12% —
a diferença para o cliente é de **R$ 88,82 na parcela**, 1,4%.

Entregue como pedido (+12%, parcela de R$ 6.079,36). **Trocar é uma linha.**

---

## Os dois cenários, lado a lado

| | cenário 1 · cartão | cenário 2 · boleto |
|---|--:|--:|
| o cliente paga | 74.363,60 | **67.850,00** |
| entrada | 13.570,00 | 13.570,00 |
| e depois | 10 × 6.079,36 | 4 × 13.570,00 |
| taxa que a casa paga | 7.295,23 | — |
| **a casa recebe, líquido** | **67.068,37** | **67.850,00** |
| último recebimento | dia 300 | dia 150 |
| **valor presente** | **63.700,56** | **65.635,10** |

⚠ **O cenário 1 custa R$ 6.513,60 a mais ao cliente e ainda entrega
R$ 1.934,53 a MENOS de valor presente para a casa.** Os dois servem, mas não
pelo mesmo motivo: o 1 é para quem precisa de parcela baixa, o 2 é o melhor
negócio para os dois lados. Por isso o cenário 2 está marcado como
**recomendado** na proposta.

---

## A proposta

`proposta-douglas.pdf`, **3 páginas** — capa, o investimento, como fechar.

⛔ **É fechamento, não apresentação.** Saíram os cases, a linha do tempo, o
"por que a Valvic" e a página de configuração técnica: o cliente já viu tudo
isso na v1. O que sobrou é o que fecha — o que é, quanto é, e como pagar.

No cenário 1, **a parcela é o número grande** e o total não aparece, como
pedido.

Três passes de auditoria limpos.

---

## Em aberto

1. ★ **+12% ou +13,64%?** Ver o quadro acima — R$ 781,63.
2. ★ **A produção começa quando?** Dia 0 ou dia 60. Muda o caixa e o texto
   do prazo.
3. ★ **Os cinco itens marcados "até dia 20"** na v1 — M01, M02, M05, M06 e
   M10/11/13 — continuam com data? São **R$ 33.000 de produção imediata
   contra R$ 13.570 de entrada**. Se a data valer, o cenário de adiamento
   não fecha sem ajuste.
4. ★ **M10/11/13 a R$ 4.900 é o lote ou cada um?** Só o M07 dizia "cada
   unidade"; assumi lote. Se for cada, o total vai a R$ 77.650.
5. **Validade de 5 dias úteis** é proposta minha; a v1 usava 2.
