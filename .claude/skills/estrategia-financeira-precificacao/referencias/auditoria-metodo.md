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
> média, afunda a operação** — foi a doença que gerou a dívida antiga de R$300k
> (já quitada) e que **não pode se repetir** com as dívidas atuais (máquinas,
> capital de giro, empréstimo do Paulo).

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

## 🟠 Achado nº 3 — o "painel do mês" é escopo do Valvic OS, não do app

**Sintoma.** O app mede MC% **por projeto**, mas não acumula o **mês** (Σ MC vs
custo fixo R$67k). Maio/junho furaram o equilíbrio **sem alarme**.

**Causa raiz.** Esse é um indicador **de empresa**, não de um orçamento isolado.

**Tratamento.** Fica **no Valvic OS**, onde o Rodrigo audita a empresa toda e
cruza: Σ MC do mês vs custo fixo, nº de projetos, caixa. O **app de orçamento
segue focado em precificação**; ele só **alimenta** o OS com a MC de cada projeto.

## 🟡 Achado nº 4 — ciclo de caixa: também no Valvic OS

**Sintoma.** O método precifica bem (custo→MC), mas só captura o **custo** do
parcelamento (8%), não o **tempo** entre receber e pagar — nem o serviço das
dívidas atuais (máquinas, Paulo).

**Causa raiz.** Capital de giro / fluxo é o **pilar 3** do Rodrigo; é dado de
empresa, não de orçamento.

**Tratamento.** Modelar **recebimento × pagamento** e **caixa projetado** **no
Valvic OS** (com os cruzamentos da empresa), não no app de orçamento.

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
lucro/mês em R$11–14k **sem vender nada a mais** — caixa que sustenta a operação e
amortiza as dívidas atuais (máquinas, giro, Paulo), sem repetir o erro que gerou
a dívida (já quitada) de R$300k.

## Ações priorizadas
**No app de orçamento (precificação):**
1. **Recalibrar a meta de MC**: piso ~43%, alvo 48–50%.
2. **Linha de break-even** por orçamento (alerta visual quando MC < equilíbrio).
3. **Preço mínimo por projeto** (não depender de contrato grande).

**No Valvic OS (auditoria de empresa — o Rodrigo cruza tudo):**
4. **Painel do mês** (Σ MC vs custo fixo R$67k + caixa).
5. **Ciclo de caixa** e **serviço das dívidas atuais** (break-even de caixa real).
6. **Composição do custo fixo** e **capacidade produtiva**.
