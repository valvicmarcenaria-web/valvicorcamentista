# Marcenaria sob encomenda vista pelo financeiro

Para auditar ou projetar o caixa de uma marcenaria de planejados é preciso saber
**onde, no ciclo físico do móvel, cada real entra e sai**. Sem isso, o fluxo de
caixa vira chute e a DRE mistura meses. Este arquivo é o "olhar de marceneiro"
do Rodrigo.

## 1. Ciclo de um projeto e onde cai o dinheiro

| # | Etapa física | Prazo típico (desde a venda) | Entrada de caixa | Saída de caixa | Competência |
|---|---|---|---|---|---|
| 1 | Venda / contrato assinado | D0 | **Entrada/sinal** (política: ≥ 40%) | comissão do vendedor (se paga na assinatura), brindes, visitas, projeto | sinal = **adiantamento de cliente (passivo)**, não receita |
| 2 | Medição fina + projeto executivo | D+5 a D+20 | — | visitas, uber, impressão | despesa do período (ou custo do projeto se rastreado) |
| 3 | Compra de chapas, fita e ferragens | D+10 a D+30 | — | fornecedor de chapa (à vista, 28 ou 28/56 dd), ferragens (Blum/Hettich/Häfele/FGV: 28–60 dd) | entra como **estoque / obra em andamento**; vira custo quando consumido no projeto entregue |
| 4 | Corte CNC, fita (coladeira), usinagem | D+20 a D+45 | parcela de "início de produção" (se contratada) | desgaste de serra/fresa, energia (fixo), hora extra | custo do projeto |
| 5 | Terceirizados (vidro, serralheria, pintura/laca, estofado, pedra) | D+30 a D+60 | — | sinal ao terceirizado + saldo na entrega | custo do projeto |
| 6 | Pré-montagem e embalagem | D+40 a D+60 | — | strech, cantoneira, embalagem | custo do projeto |
| 7 | Entrega + instalação | D+45 a D+75 | **parcela de entrega** (a maior, se o contrato não tiver entrada forte) | carreto/frete, equipe de montagem, alimentação, comissão de produção/montagem | **reconhecimento da receita** (regra Valvic: na entrega/instalação) |
| 8 | Vistoria / ajustes finais | D+60 a D+90 | **saldo final** (se ficou retido) | retrabalho, reposição de peça | custo do projeto (ou provisão de garantia) |
| 9 | Assistência / garantia | até 5 anos | — | visita técnica, ferragem trocada | **provisão de garantia** (despesa estimada na competência da entrega) |

Leituras que saem dessa tabela:
- **O caixa sai antes do dinheiro entrar** (etapas 3–6). Por isso projeto com
  pagamento "tudo na entrega" financia o cliente com o capital de giro da Valvic
  — é a causa dos meses de recebimento zero (jul, ago, nov/2025).
- **Material ≈ 30–40% do preço** e sai entre D+10 e D+30. A entrada mínima
  saudável é a que cobre **material + terceirizados + comissões pagas na
  assinatura** → na Valvic, 40% é o número que fecha essa conta.
- **Mão de obra da fábrica é fixa** (7 salários): ela não "aparece" no projeto,
  mas consome **hora-fábrica**. Atrasar um projeto não economiza salário; só
  empurra a receita para frente.

## 2. Custos — classificação que o financeiro precisa respeitar

**Variáveis (por projeto, entram no orçamento da Lavinia):** chapas (por
cor/espessura), fita de borda, cola, ferragens, iluminação LED, vidros,
terceirizados, comissões (vendedor, produção, programador, montador), RT do
arquiteto, NF (≈7%), taxa da maquininha/parcelamento (7–8%), frete/carreto,
embalagem, visitas, margem de erro (2%).

**Fixos (a soma das MCs paga):** salários + encargos dos 7 fixos e pró-labore,
galpão (~500 m²), energia, internet, sistemas (Calcme, SketchUp/Promob, Canva),
contador, manutenção preventiva das máquinas, administrativo, marketing base.

**Não operacionais (fora da DRE operacional, mas pesam no caixa):** parcela do
financiamento de máquinas (CNC, coladeira), devolução do empréstimo do Paulo,
investimento em ativo (máquina nova, ferramental), juros de capital de giro.

> Armadilha clássica: o **marceneiro tem salário (fixo) e comissão (variável)**.
> Na auditoria, conferir se a comissão está em "custo do projeto" e o salário em
> "despesa com pessoal" — misturar os dois distorce tanto a MC do projeto quanto
> o custo fixo.

## 3. Indicadores físicos que viram indicadores financeiros

| Indicador | Como medir | Referência / alerta |
|---|---|---|
| **Consumo de chapa real × orçado** | chapas compradas para o projeto ÷ chapas do plano de corte | > 110% = desperdício, erro de corte ou desvio |
| **Aproveitamento da chapa** | área das peças ÷ área das chapas consumidas | 80–88% é bom em CNC com nesting; < 75% investigar |
| **Sobras / retalhos** | chapas em estoque sem projeto vinculado | sobra é dinheiro parado — reaproveitar em fundo/gaveta |
| **Ferragem por projeto** | NF de ferragem vinculada ao projeto × lista da Lavinia | ferragem comprada sem projeto = pedir justificativa |
| **Retrabalho** | peças refeitas / chapas extras após o corte | custo direto; cada chapa de cor 18 mm ≈ R$ 580 |
| **Prazo de produção** | assinatura → entrega | quanto maior, maior o capital de giro consumido |
| **Assistência técnica** | visitas pós-entrega e custo | base para a provisão de garantia (sugestão: 1–2% da receita) |
| **Hora-fábrica por R$ de MC** | MC do projeto ÷ dias de fábrica ocupados | decide o mix quando a capacidade está cheia |

## 4. Fornecedores e prazos (como pensar)

- **Chapas MDF** (Duratex/Eucatex/Arauco/Guararapes via distribuidor): compra
  geralmente à vista ou 28 dd; promoções exigem volume — comprar por projeto
  evita estoque parado, comprar em lote reduz preço mas consome caixa.
- **Ferragens** (Blum, Hettich, Häfele, FGV, Grass): prazos de 28/56 dd são
  comuns — é o **melhor financiamento barato** da operação; negociar sempre.
- **Terceirizados** (vidraceiro, serralheiro, laca, estofador, marmoraria):
  sinal + saldo na entrega; casar o saldo com a parcela de entrega do cliente.
- **Maquininha**: recebimento parcelado (D+30 por parcela) ou antecipado (com
  taxa). Antecipação é **custo financeiro**, não custo de venda — separar.

## 5. Impostos e documentos (validar sempre com o contador)

- A Valvic considera **≈7% de NF** sobre o faturado. Fabricação de móveis sob
  encomenda costuma ser tributada como **indústria/comércio** (no Simples,
  geralmente Anexo II), e montagem/instalação pode ser **serviço**; a alíquota
  efetiva muda com o faturamento acumulado de 12 meses (RBT12). Ao auditar, a
  pergunta é: **o imposto pago bate com o faturamento emitido no mês?**
- Competência do imposto = **mês da emissão da NF**, não do pagamento da guia.
- NF-e de compra (chapas, ferragens) é a prova do custo de material — cruzar com
  o projeto destino. NF emitida a menor que o contrato é **risco fiscal**;
  apontar, sem orientar como contornar.
- **RT (reserva técnica do arquiteto):** ≈10% do líquido. Registrar como custo
  de venda do projeto, com a obrigação reconhecida na competência da receita,
  mesmo que o pagamento ao arquiteto seja depois.

## 6. Sazonalidade típica

- **Out–dez:** pico de entrega (cliente quer tudo pronto até o Natal) → muitos
  recebimentos de entrega, mas também pico de compras e hora extra; dezembro tem
  **13º + férias** → saída de caixa alta (ver o buraco de R$ 107k em dez/2025).
- **Jan–fev:** vendas fracas e fábrica executando o backlog; **é o mês em que o
  pipeline vazio de nov/dez cobra a conta**.
- **Mar–mai:** retomada de vendas (obras novas, apartamentos entregues).
- Planejar a **reserva de caixa** para cobrir o vale de jan–fev e o 13º.
