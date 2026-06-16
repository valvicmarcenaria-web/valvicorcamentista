# Central Financeira — Rodrigo (Valvic Marcenaria)

> **Leia este arquivo PRIMEIRO ao iniciar qualquer sessão com o Rodrigo.**
> É a fonte de verdade do estado financeiro atual + pipeline + pendências.
> Atualizar sempre que houver mudança relevante (novo projeto, dívida, caixa).

---

## 1. Quem é o Rodrigo

**Consultor de finanças e precificação estratégica da Valvic.** Eleva a decisão
de preço do tático (MC% por projeto, feito pela Lavinia) para o estratégico
(saúde financeira da empresa). Método baseado em Rodrigo Almeida (@rodrigofinancas).

> **Lema:** *"Faturamento é vaidade — aumente o lucro com os preços certos."*
> O problema da Valvic **não é venda** — é **preço**. A alavanca: cada +1 ponto
> de MC% = +R$1,62k de lucro/mês. Subir de 43,5% → 50% **quadruplica** o lucro.

Ver método completo: `referencias/metodo-rodrigo.md`

---

## 2. Quadro financeiro real (base 2025 — atualizar mensalmente)

| Indicador | Valor atual |
|---|---|
| Faturamento médio/mês | **R$ 162 mil** |
| MC% praticada | **43,5%** |
| MC R$/mês | **R$ 70,5 mil** |
| **Custo fixo mensal** | **≈ R$ 67 mil** |
| Ponto de equilíbrio (faturamento) | **R$ 154 mil** |
| Lucro médio/mês | **R$ 3,5 mil** (só 2,1%) |
| Margem de segurança | **4,9%** — opera colado no break-even |

> **Status (jun/2026):** caixa BAIXO. Maio e junho ficaram abaixo do break-even.
> Junho só não foi prejuízo por um projeto de R$92k que mascarou o mês.
> **Problema de preço, não de venda.**

### Dívidas ativas (valores a confirmar com Jonathan)
| Dívida | Status | Parcela/mês |
|---|---|---|
| Dívida antiga R$300k | ✅ **QUITADA** (história, não é passivo ativo) | — |
| Financiamento de máquinas (CNC, coladeira) | ativa | **a levantar** |
| Capital de giro / aperto crônico | recorrente | **a quantificar** |
| Empréstimo pessoal do Paulo (sócio) | ativa | **a levantar** |

> ⚠️ **Break-even de CAIXA é mais alto que o contábil** — o serviço das dívidas
> ativas (parcelas de máquinas + devolução ao Paulo) é saída adicional ao custo
> fixo de R$67k. Por isso a meta real de MC é **48–50%** (não "43%").

---

## 3. Metas calibradas (Rodrigo + Jonathan, jun/2026)

| Situação | MC mínima | Observação |
|---|---|---|
| Caixa crítico | 25% | Exceção máxima — só se capacidade ociosa |
| Caixa ruim | 30% | Exceção consciente |
| Caixa normal | 37% | Abaixo do break-even real — evitar como hábito |
| **Break-even contábil** | **~43%** | Piso operacional — padrão atual |
| **Alvo saudável** | **48–50%** | Gera lucro real + amortiza dívidas ativas |

> A meta de "35–40%" do método original está **abaixo do break-even real** e
> gera prejuízo estrutural — foi o padrão que gerou a dívida de R$300k (já
> quitada). **Não repetir.** Ver auditoria completa: `referencias/auditoria-metodo.md`

### A alavanca (mesmo faturamento R$162 mil/mês)
| MC% | Lucro/mês | Multiplicador |
|---|---|---|
| 43,5% (atual) | R$ 3,5 mil | 1,0× |
| 45% | R$ 5,9 mil | 1,7× |
| 48% | R$ 10,8 mil | 3,1× |
| **50%** | **R$ 14,0 mil** | **4,0×** |
| 55% | R$ 22,1 mil | 6,4× |

---

## 4. Pipeline de projetos ativos (atualizar por sessão)

| Cliente | Projeto | Investimento | MC% | Status | Observação |
|---|---|---|---|---|---|
| Regina Godinho | Escritório / Home Office | R$ 13.100 | 43% | ✅ Proposta enviada | Cliente recorrente (3º projeto). Piso negociação MC 37% = R$11.150. Sem RT. |
| Kênia & Fábio | Banheiro (M35+M36) | R$ 10.735 | 35% | ✅ Cotado | MC abaixo do break-even — aprovado como exceção (caixa baixo). Confirmar escopo final. |
| Kênia & Fábio | **Casa completa** (3 pav.) | **a calcular** | **a definir** | 🔴 Em levantamento | Projeto GRANDE. 29 pranchas DET MARC em extração. **Rodrigo precisa definir o piso de MC — Jonathan vai passar projeção de caixa.** |

---

## 5. Pendências abertas para o Rodrigo

### 🔴 URGENTE — Piso de MC para Kênia & Fábio (casa completa)
Projeto grande (casa de alto padrão, 3 pavimentos, marcenaria completa).
**Jonathan vai apresentar uma projeção de caixa** para o Rodrigo avaliar:
- Qual MC% mínima aceitar neste projeto?
- O projeto grande justifica ocupar a fábrica por meses → qual o impacto no break-even do período?
- A Valvic tem capacidade produtiva para absorver sem comprometer outros projetos?

### 🟠 A levantar — Composição do custo fixo e dívidas
Para o break-even de CAIXA real (mais preciso que o contábil):
- Parcelas mensais: financiamento de máquinas + devolução Paulo
- Composição detalhada do custo fixo (~R$67k) por rubrica
- Ciclo de caixa: prazo médio recebimento × pagamento de fornecedores

> Ferramenta para isso: `ferramentas/custo-operacao.html` — o Jonathan preenche
> e exporta JSON; o Rodrigo recebe e faz os cruzamentos.

### 🟡 Painel do mês (recorrente)
Verificar mensalmente: Σ MC dos projetos faturados vs custo fixo R$67k.
- Maio/junho: **abaixo do break-even** (alerta)
- Julho: ??? (a monitorar)
- Regra: nenhum mês deve depender de um único projeto grande para não fechar no vermelho

---

## 6. Handoff com os outros agentes

| De / Para | O que passa | Formato |
|---|---|---|
| **Lavinia → Rodrigo** | MC% + MC R$ + custo total de cada projeto | JSON do app (`validacao-orcamento.html`) ou briefing em texto |
| **Rodrigo → Lavinia** | Piso de MC do mês + situação de caixa | Texto: "caixa BAIXO, piso 37%" ou "normal, piso 43%" |
| **Rodrigo → Vitor** | Margem de negociação + condições de pagamento (escada de antecipação) | Texto: "piso R$X, cortesia de R$Y para negociação" |
| **Jonathan → Rodrigo** | Projeção de caixa do mês / dados de dívidas | Texto livre ou JSON do `custo-operacao.html` |

---

## 7. Referências

| Arquivo | O que é |
|---|---|
| `referencias/metodo-rodrigo.md` | Método Rodrigo Almeida completo (4 pilares, sequência, "poucos números") |
| `referencias/auditoria-metodo.md` | Auditoria da meta de MC (achado crítico: 35–40% está abaixo do break-even) |
| `dados/custo-fixo.md` | Números reais da Valvic + dívidas + alavanca do preço |
| `ferramentas/custo-operacao.html` | App de levantamento de custos operacionais (dashboard, break-even, custo fixo×variável) |
| `SKILL.md` | Persona completa do Rodrigo (princípios, fluxo de decisão, conexão com Valvic OS) |
| `../../GUIA-ORCAMENTOS.md` | Guia da Lavinia (metas de MC, parâmetros, aprendizados) |
| `../../MOLESKINE.md` | Notas e tarefas entre sessões (raiz do repositório) |
