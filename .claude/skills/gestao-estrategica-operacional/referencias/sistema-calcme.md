# Operação do Sistema Calcme (ERP da Valvic)

> A Valvic usa o **Calcme** (calcme.com.br) — ERP especializado em marcenaria/móveis
> planejados. Internamente às vezes é chamado de **"Calme"** — é o mesmo sistema.
> A Helena é **operadora experiente** do Calcme: sabe o que cada módulo faz, como manter
> o dado limpo e que relatório puxar para cada decisão. *(Nomes exatos de tela/menu:
> confirmar na conta da empresa — este guia é por fluxo, não por botão.)*

## Módulos e para que servem

**1 · Orçamento & Projetos**
- Biblioteca de módulos → monta o projeto → **transforma em orçamento e pedido em poucos
  cliques** (sem retrabalho). Gera propostas.
- É a porta de entrada do cliente no sistema. A **Lavinia** (skill de orçamento) é quem
  domina a montagem do orçamento; a Helena garante que ele **entre no Calcme** e vire pedido.

**2 · PCP & Kanban (produção)**
- Planeja e controla a produção; **Kanban por pedido e por ambiente**.
- Acompanha o **status de cada projeto**: medição → projeto técnico → produção → montagem.
- A Helena usa para responder "onde está o projeto do cliente X?" e antecipar gargalos.

**3 · Estoque & Compras**
- **Ordens de compra** enviadas a fornecedores; controle de recebimento **integrado ao estoque**.
- Status do material: **em trânsito · provisionado · disponível**.
- A Helena cruza pedido × material provisionado para não parar obra por falta de chapa/ferragem.

**4 · Financeiro**
- **Contas a pagar e a receber**, **integração bancária**, **fluxo de caixa**, conciliação,
  controle de saldos, gestão de pagamentos.
- **Boletos** emitidos direto do pedido; **NF-e** (produto) e **NFS-e** (serviço) integradas
  ao orçamento/venda.
- **Dono da análise é o Rodrigo** (finanças); a Helena garante o **lançamento correto e no
  prazo** e puxa os relatórios.

**5 · Relatórios**
- Relatórios financeiros detalhados: faturas, cobranças, boletos, custos, lucro, fluxo.
- Base para o fechamento mensal (ver `planilhas-e-relatorios.md`).

## Rotinas da Helena no Calcme

| Quando | O que fazer no Calcme |
|---|---|
| Cliente fechou | Pedido criado a partir do orçamento; **pasta do cliente** aberta no Drive em 24h |
| Semana | Conferir Kanban (status por ambiente); alertar vencimentos de contas com **5 dias** |
| Recebimento de material | Baixa no estoque; conferência da mercadoria contra a ordem de compra |
| Marco do projeto | Atualizar status no PCP (medição/projeto/produção/montagem) |
| Cobrança | Emitir boleto do pedido; acompanhar recebimento; conciliar |
| Fechamento do mês | Puxar relatórios financeiros → planilha → entregar ao Rodrigo |

## Higiene do dado (o que faz o Calcme confiável)
- **Cadastrar na hora** — cliente/projeto/pedido no ato do fechamento; nada "depois".
- **Status sempre real** — o Kanban só serve se refletir o chão de fábrica de fato.
- **Um pedido = uma verdade** — evitar duplicidade; corrigir na origem, não em cópia.
- **Lançamento financeiro no prazo** — atraso de lançamento distorce o fluxo de caixa e
  engana a decisão do Rodrigo.
- **Conciliação bancária em dia** — saldo do sistema = saldo do banco.

## Divisão de responsabilidade
- **Lavinia** monta o orçamento (o quê e por quanto). **Helena** garante que vire pedido e
  ande no Calcme (produção + financeiro lançados). **Rodrigo** lê os relatórios e decide
  preço/caixa. **Assistente Operacional** faz o lançamento rotineiro do dia a dia sob a
  cadência que a Helena mantém.

> **Se um recurso específico não estiver claro** (nome de menu, permissão, passo exato),
> a Helena diz "confirmo na conta" em vez de afirmar — nunca inventa a operação do sistema.
