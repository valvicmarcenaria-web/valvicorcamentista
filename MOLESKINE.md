# Moleskine Digital — Valvic

Arquivo de tarefas e recados entre sessões. Qualquer agente (Lavinia, Rodrigo, Vitor…)
pode ler e escrever aqui. Formato livre — marcar data e agente responsável.

---

## Tarefas abertas

### [2026-09-05] POP-01 — Conferência de peça antes de sair da fábrica — Téo (Academy)
**Solicitante:** Jonathan
**Status:** 🟡 Escrito, aguardando aprovação da Direção e implantação

Jonathan relatou que a **Ficha de Conferência já existe mas ninguém usa direito**, e continua
saindo peça errada para a obra. Foi escrito o procedimento que faltava (o *como usar* a ficha):
- `painel/pop-conferencia-de-peca.html` + `painel/Valvic_POP_Conferencia_De_Peca.pdf` (2 folhas A4)
- Folha 1 = bancada, 10 passos, 3 min/módulo. Folha 2 = carga, 6 pontos de conferência com
  critério observável, "se der errado", registro e implantação.
- Fontes: `ficha-conferencia-producao.html` (portões 5-7), `matriz-conferencia.html`,
  `feedback-deivison-obra.html` (a ferramenta 02 e os 21 pontos da cozinha).

**Pendências para a próxima sessão:**
1. Aprovação da Direção (o campo de assinatura está no rodapé da folha 2).
2. Apresentar nos 10 minutos da manhã, com peça real na bancada.
3. Revisão em **30 dias** com a lista de retrabalhos do período — o indicador é retrabalho em
   obra por peça que saiu errada da fábrica.
4. Próximo POP da fila (prioridade 2): **recebimento de material** — a ficha também já existe.

---

### [2026-06-16] Novo layout de proposta — Vitor
**Solicitante:** Jonathan  
**Agente:** Vitor  
**Status:** 🔴 Pendente

**O que foi pedido:**  
Criar um novo layout/template de proposta para o Vitor — diferente dos modelos atuais
no Canva (MODELO e MODELO ENXUTO). Jonathan quer um design novo com:
- Nova linha do tempo visual
- Links para Instagram e YouTube da Valvic
- (outros detalhes a confirmar com Jonathan na próxima sessão)

**Contexto:**  
A demanda surgiu na sessão de 2026-06-16 mas foi interrompida antes de Jonathan
especificar o design completo. Retomar perguntando: "Quais seções quer no novo
layout? Referência visual? Links exatos do IG e YouTube?"

**Arquivos relacionados:**  
- Templates atuais: MODELO `DAHMsJxsuhE` · MODELO ENXUTO `DAHMsEfQNas`  
- Referência de identidade: `.claude/skills/closer-vendas/referencias/identidade-marca.md`

---

## Tarefas concluídas

*(mover aqui quando feito, com data de conclusão)*

---

## Base de dados atualizada

### [2026-06-25] custo-fixo.json — versão atualizada (Rodrigo)
**Arquivo:** `.claude/skills/estrategia-financeira-precificacao/dados/custo-fixo.json`  
**Faturamento de referência:** R$ 246.000/mês · MC% padrão: 43,5% · encargoCLT: 27,44%

**Folha bruta (sócios + produção + comercial):**
| Pessoa | Regime | Valor |
|---|---|---|
| Jonathan (pró-labore + ajuda) | — | R$ 7.700 |
| Paulo (pró-labore + ajuda) | — | R$ 7.700 |
| Jackson (marceneiro) | PJ | R$ 3.600 |
| Samuel (marceneiro) | PJ | R$ 3.900 |
| Joelson (operador CNC) | CLT | R$ 2.500 |
| Deivson (coordenador) | PJ | R$ 4.000 |
| Filipe (programador) | PJ | R$ 3.600 |
| Jomar (marceneiro jr.) | CLT | R$ 1.950 |
| Davi (ajudante) | CLT | R$ 1.950 |
| Assistente adm. | CLT | R$ 2.000 |
| **Total folha bruta** | | **R$ 38.900** |
| Encargos CLT (27,44% s/ R$8.400) | | + R$ 2.305 |
| VT R$3k + VA R$500 + EPIs R$150 | | + R$ 3.650 |
| **Total pessoal** | | **≈ R$ 44.855** |

**Custos estruturais mensais (sem dívidas):**
- Galpão (aluguel R$5k + utilidades + conservação): **R$ 8.280**
- Máquinas (manut. + consumíveis + software): **R$ 1.300** *(+ deprec. contábil R$2.633)*
- Logística (combustível + veículo): **R$ 5.050**
- Comercial/mktg (tráfego + social media): **R$ 2.900**
- Administrativo (contador + jurídico + sistemas): **R$ 4.250**
- Tributos (DAS est.): **R$ 1.500**
- **Total operacional (caixa, sem dívidas): ≈ R$ 68.135**

**Dívidas ativas (saída de caixa mensal):**
| Dívida | Total | Parcelas | Mensal est. |
|---|---|---|---|
| Financ. máquinas (CNC + ESQ · RAIZEN) | **R$ 36.600** | **6** | **R$ 6.100** |
| Capital de giro | R$ 37.000 | 4 | R$ 9.250 |
| Empréstimo Paulo | R$ 30.000 | 5 | R$ 6.000 |
| Aporte Paulo (CNC) | R$ 65.000 | 100 | R$ 650 |
| **Total dívidas/mês** | **R$ 156.000** | | **R$ 20.700** |

**Break-even (MC 43,5%):**
- Contábil (operacional): R$ 68.135 ÷ 43,5% ≈ **R$ 156.600/mês**
- De caixa (com dívidas): R$ 89.435 ÷ 43,5% ≈ **R$ 205.600/mês** *(corrigido: financ. máquinas real R$6.100/mês)*
- Fat. de referência no JSON: **R$ 246.000/mês** (teto necessário para gerar caixa positivo)

**Confirmação RAIZEN Financeiro (25/06/2026 via WhatsApp):**
- NF 2509 (Esquadrejadeira): **6 títulos restantes** · 07/06/26 → 07/11/26 · R$2.350/mês = R$14.100 total
- NF 2403 (CNC Solid Taf): **6 títulos restantes** · 17/06/26 → 17/11/26 · R$3.750/mês = R$22.500 total
- **Saldo total confirmado: R$36.600** (quitação: nov/2026)
- Raizen **não pratica desconto por antecipação**
- Parcela de jun/26 de ambas agendada p/ pagamento em 01/07

**Depreciações contábeis registradas:**
- CNC/ESQ/COL: bem R$220k, residual R$80k, vida 60m → **R$2.333/mês**
- Carro: bem R$50k, residual R$35k, vida 50m → **R$300/mês**

---

## Voz & Estilo — Jonathan (dono)

*(perfil de como o Jonathan escreve pra clientes/parceiros no WhatsApp — usar como referência
quando um agente for redigir mensagem em nome dele, ex. Vitor)*

**Como ele naturalmente escreve** (base: conversa com Paula Galante, decoradora parceira,
2026-07):
- Abre com afeto genuíno antes do assunto ("Boa tarde Paula, como vai? espero que bem.") —
  nunca entra direto no pedido.
- Texto corrido, tom de conversa real: minúscula no início de frase às vezes, acentos
  soltos em mensagens rápidas de acompanhamento — mas as frases "importantes" (o pedido em
  si) saem bem escritas, com "por gentileza", educado.
- Uma pergunta por mensagem, direta e sem rodeio ("existe alguma alteração de projeto que
  eu preciso ser atualizado?").
- **Não deixa resposta vaga passar.** Quando a resposta não confirma o essencial, ele repete
  a pergunta central sem se alongar ("mas o projeto sera atualizado?") — firme, mas sem
  espaçar frase de mais nem soar irritado.
- Emoji raro, só reação pontual (não no corpo do texto).

**Pequenos aprimoramentos sugeridos** (o que os agentes devem adicionar ao redigir por ele,
sem descaracterizar o tom):
1. Quando for cobrar/alertar algo recorrente, **nomear o "porquê"** antes do pedido (ex.
   "pra eu conseguir entregar com qualidade e no prazo..."), separando o problema pontual do
   padrão de processo — evita que a cobrança pareça pessoal.
2. Fechar pedidos em aberto com algo concreto e de baixo esforço pro outro lado (prazo curto,
   formato leve tipo "resumo por aqui") — sem isso o pedido tende a ser adiado de novo.
3. Manter o calor humano no início/fim mesmo quando o meio da mensagem é uma cobrança —
   é o que sustenta a relação com parceiros como a Paula.

**Aprendizado registrado (2026-07-16):** falta de definição técnica fechada *antes* da
conferência é **recorrente na obra Vale dos Cristais** — já ocorreu no painel da sala e na
lavanderia (ambos só resolvidos in loco/depois). Contraste: o quarto do Rael, com projeto
100% fechado antes, fluiu "maravilhosamente bem". Vale usar esse contraste como argumento
concreto (não abstrato) quando for reforçar com Paula ou outros parceiros a importância de
travar definição antes da visita técnica.

## Recados rápidos

*(notas passageiras — podem ser apagadas após lidas)*

### [2026-06-16] Rodrigo → Lavinia — RECADO URGENTE (atualizado com dados reais)

**O PROBLEMA NÃO É MC% — É VOLUME.**

Com os dados reais do custo-operacao.html:
- Break-even real da empresa: **R$ 246.000/mês de faturamento**
- Com média atual de R$ 148k/mês: prejuízo de **R$ 33.200/mês** (inevitável)
- Com MC% = 43,5% mas faturamento = R$ 148k: ainda no vermelho em R$ 33k
- Não existe MC% que conserte isso: só VOLUME fecha a conta

**O que isso muda para a Lavinia:**
- Piso de MC mantém 43.5% — não dar desconto que piore mais ainda
- MAS: o foco principal é FECHAR projetos, não otimizar MC décimo a décimo
- Cada projeto fechado em R$ 50k (com 43,5% MC) = reduz o prejuízo do mês em ~R$ 7.500
- Kênia & Fábio (casa completa) é PRIORITÁRIO — é o que pode virar o mês

**Pisos de MC operacionais:**
- Situação de caixa CRÍTICA (atual): mínimo 43,5% — abaixo disso, só em caso extremíssimo
- Projetos grandes (>R$ 80k): 43,5% e ENTRADA obrigatória de 40% antes de iniciar
- NUNCA aceitar projeto que reduza a MC média abaixo de 40% no mês

**Meta de faturamento a transmitir no fechamento:**
- Alvo por mês: R$ 246k em projetos novos (break-even)
- Faturamento H1/2026 médio: R$ 148k → ainda falta R$ 98k/mês para empatar
- H2/2026 está ZERADO — toda venda nova agora vai para o segundo semestre

### [2026-06-16] Rodrigo → Vitor
**Pipeline H2/2026 zerado — emergência comercial.**
Prioridade 1: fechar Kênia & Fábio (casa completa, MC ≥ 40%, entrada 40%).
Prioridade 2: reativar orçamentos parados nos últimos 90 dias.
Sem margem para desconto de preço. Sem desconto = sem negociação de preço.
Cobrar Marcelo e Simony (R$ 21.700) e demais recebíveis em aberto.
(Andre Alphaville R$ 70.800 NÃO é cobrança: é projeto de investimento dos sócios.)

