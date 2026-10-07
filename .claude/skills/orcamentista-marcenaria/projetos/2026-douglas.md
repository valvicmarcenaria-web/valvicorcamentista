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

## ⛔⛔ A TAXA NÃO SOME POR NÃO SER COBRADA — SÓ MUDA DE DONO

> *"refaça os valores considerando o valor cheio do orçamento, sem considerar
> acréscimo"* — Jonathan, 07/10

**Decisão: valor cheio nos dois cenários.** Caiu o acréscimo de 12% que a
versão anterior punha sobre a parte parcelada. A parcela passa de
R$ 6.079,36 para **R$ 5.428,00** e o cliente paga, nos dois cenários,
exatamente os R$ 67.850.

⚠ O que mudou de verdade não foi o preço: foi **quem paga a taxa do cartão**.
1,2% × 10 parcelas = 12% sobre R$ 54.280 = **R$ 6.513,60**, agora por conta
da casa. É **9,6% do total** — mais caro que os 7% da melhor oferta de
desconto da v1.

É o mesmo princípio do `modelo-de-custo.md` §3.1 de cabeça para baixo:
separar uma linha não é descontá-la; **não cobrar a taxa não a apaga.**

**Registro aritmético, para quando se quiser repassar:** o acréscimo neutro é
**÷ 0,88 (+13,64%)**, nunca +12% — a taxa incide sobre o valor já acrescido,
então +12% deixaria R$ 781,63 na mesa. Parcela neutra: R$ 6.168,18.

---

## Os dois cenários, lado a lado

| | cenário 1 · cartão | cenário 2 · boleto |
|---|--:|--:|
| o cliente paga | 67.850,00 | 67.850,00 |
| entrada | 13.570,00 | 13.570,00 |
| e depois | 10 × **5.428,00** | 4 × 13.570,00 |
| taxa que a casa paga | 6.513,60 | — |
| **a casa recebe, líquido** | 61.336,40 | **67.850,00** |
| último recebimento | dia 300 | dia 150 |
| **VP · o que a casa recebe** | 58.329,43 | **65.635,10** |
| VP · o que o cliente paga | **64.432,99** | 65.635,10 |

Para a casa, o cenário 1 custa **R$ 7.305,66 de valor presente**.

### ⛔ E o cliente tem razão econômica para escolher o cenário 1

A valor cheio o nominal é o mesmo, mas o cartão espalha o desembolso por dez
meses: em valor presente **o cliente paga R$ 1.202,10 a menos no cartão**.
Quem decide racionalmente escolhe justamente o cenário que custa
R$ 6.513,60 à casa. **O cartão virou a escolha padrão.**

Oferecer os dois lado a lado e contar com o cenário 2 é torcer, não
precificar. Três formas de corrigir sem mexer no preço:

1. **Menos parcelas no cartão** — 6× custa 7,2% em vez de 12% (R$ 2.606 a
   menos de taxa) e ainda deixa parcela de R$ 9.047.
2. **Dar ao cenário 2 algo que custe menos que R$ 6.513,60** — um brinde de
   escopo, um prazo melhor, uma garantia estendida.
3. **Repassar a taxa**, com o acréscimo neutro de +13,64%.

Entregue como pedido — valor cheio nos dois, cenário 2 marcado como
**recomendado**. A decisão é de mesa, não de planilha.

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

1. ★ **O cenário 1 vai ser o escolhido** — é o mais barato para o cliente em
   valor presente e custa R$ 6.513,60 à casa. Ver as três saídas acima.
2. ★ **A produção começa quando?** Dia 0 ou dia 60. Muda o caixa e o texto
   do prazo.
3. ★ **Os cinco itens marcados "até dia 20"** na v1 — M01, M02, M05, M06 e
   M10/11/13 — continuam com data? São **R$ 33.000 de produção imediata
   contra R$ 13.570 de entrada**. Se a data valer, o cenário de adiamento
   não fecha sem ajuste.
4. ★ **M10/11/13 a R$ 4.900 é o lote ou cada um?** Só o M07 dizia "cada
   unidade"; assumi lote. Se for cada, o total vai a R$ 77.650.
5. **Validade de 5 dias úteis** é proposta minha; a v1 usava 2.
