# Auditoria do Rodrigo sobre o método de orçamento — 14/06/2026

Auditoria do **método de orçamento (Lavinia + app)** pela lente do **Rodrigo**
(financeiro estratégico), cruzando com os números reais da Valvic
(`dados/custo-fixo.md`). Formato: **sintoma → causa raiz → tratamento.**

## 🔴 Achado nº 1 (CRÍTICO) — a meta de MC do método está ABAIXO do break-even

**Sintoma.** O método/app trata **"MC ideal 35–40%"** e libera pisos de **25–30%**
pela situação de caixa.

**Causa raiz.** A Valvic precisa de **MC% médio ≥ 41,4%** só para **empatar**
(custo fixo R$67k ÷ faturamento R$162k). Ou seja, **a meta "ideal" do método
(35–40%) gera prejuízo estrutural**:

| MC% praticada | MC R$/mês | Resultado |
|---|---|---|
| 35% (normal do app) | R$ 56,7k | **−R$ 10,3k/mês** |
| 38% (ideal do app) | R$ 61,6k | **−R$ 5,4k/mês** |
| 40% | R$ 64,8k | **−R$ 2,2k/mês** |
| **41,4% (equilíbrio)** | R$ 67,0k | **R$ 0** |
| 43,5% (histórico) | R$ 70,5k | +R$ 3,5k |
| **48–50% (saudável)** | R$ 78–81k | **+R$ 11–14k** |

> Em uma frase do Rodrigo: *o método está calibrado para uma empresa que não
> existe.* O "35–40%" é resquício de uma referência antiga e **se for seguido na
> média, afunda a operação** — exatamente a doença que gerou os R$300k de dívida.

**Tratamento.**
1. **Resetar a meta de MC** no método e no app: **piso = equilíbrio (~43%)**,
   **alvo saudável = 48–50%** (lucro real + abater dívida).
2. **Linha de break-even visível** em cada orçamento: mostrar a MC% do projeto
   **contra a MC de equilíbrio da empresa (~43%)** — alerta quando abaixo.

## 🟠 Achado nº 2 — "situação de caixa" pode virar a própria doença

**Sintoma.** As faixas de caixa permitem aceitar MC **25–30%** "para gerar fluxo".

**Causa raiz.** Vender abaixo do equilíbrio **aumenta faturamento e aprofunda o
prejuízo** — é "faturamento é vaidade" na veia. Tática pontual (encher capacidade
ociosa, MC ainda positiva ajuda a pagar o fixo já incorrido) é válida; **como
hábito, é o buraco**.

**Tratamento.** Manter o piso de caixa como **exceção consciente** (capacidade
ociosa), nunca como padrão. O **default** do mês deve ser **≥ equilíbrio**.
Calibrar **preço mínimo por projeto** para nenhum mês depender de um contrato
grande (foi o que mascarou junho com 1 projeto de R$92k).

## 🟠 Achado nº 3 — falta o "painel do mês" (os poucos números que importam)

**Sintoma.** O app mede MC% **por projeto**, mas não acumula o **mês**.

**Causa raiz.** Sem ver a **soma das MCs do mês vs o custo fixo (R$67k)**, não há
previsibilidade — decide-se projeto a projeto sem saber se o mês já pagou o fixo.
Maio/junho ficaram abaixo do equilíbrio **sem alarme**.

**Tratamento.** Adicionar um **painel mensal**: Σ MC do mês vs R$67k (ponto de
equilíbrio mensal) + nº de projetos fechados. Os 3 números do Rodrigo: **MC%**,
**equilíbrio do mês**, **caixa**.

## 🟡 Achado nº 4 — ciclo de caixa não está no modelo

**Sintoma.** O método precifica bem (custo→MC), mas só captura o **custo** do
parcelamento (8%), não o **tempo** entre receber e pagar.

**Causa raiz.** Capital de giro / fluxo é o **pilar 3** do Rodrigo e a origem do
aperto de caixa mesmo vendendo bem. Hoje invisível no método.

**Tratamento (próximo passo).** Modelar **prazo de recebimento × pagamento**
(chapa, ferragem, terceirizados) e um **caixa projetado**.

## ✅ O que o método já faz CERTO (manter)
- **Preço projeto a projeto, vivo, com MC em cada venda** = pilar 2 do Rodrigo na
  veia. O app é exatamente "os poucos números que importam" em ferramenta.
- **Separação custo fixo × variável** correta (fixo não entra no orçamento; a MC
  é o que o cobre).
- **Rastreabilidade + base única de preços** (disciplina de custo).
- **Diretrizes + direcionamentos do Rodrigo** no histórico de cada orçamento.

## Veredito
O **motor de precificação é bom**; a **régua de margem está errada**. Não é
problema de ferramenta nem de venda — é de **meta**. Subir a meta de MC de
"35–40%" para **piso 43% / alvo 48–50%** é a alavanca que transforma ~R$3,5k de
lucro/mês em R$11–14k **sem vender nada a mais** — e começa a matar os R$300k.

## Ações priorizadas
1. **Recalibrar a meta de MC** (método + app): piso ~43%, alvo 48–50%.
2. **Linha de break-even** por orçamento (alerta visual).
3. **Painel do mês** (Σ MC vs R$67k).
4. **Preço mínimo por projeto** (não depender de contrato grande).
5. **Ciclo de caixa** (próxima fronteira).
