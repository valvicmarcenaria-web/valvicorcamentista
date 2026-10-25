# Auditoria financeira — roteiro do Rodrigo

Auditoria aqui é **gerencial** (achar erro, vazamento e risco para o dono
decidir), não auditoria contábil com parecer. O objetivo é que cada número que
o Rodrigo usa para decidir preço e caixa **seja confiável**.

> Para a auditoria do **método de precificação** (régua de MC), ver
> `auditoria-metodo.md`. Este arquivo trata da auditoria dos **números**.

## 1. Fontes e o que cada uma prova

| Fonte | Prova | Cuidado |
|---|---|---|
| **Extrato bancário** (PDF/OFX/CSV) | o que **de fato** entrou e saiu — é a verdade do caixa | várias contas/bancos; maquininha deposita líquido e agrupado |
| **Calcme** (contas a pagar/receber, DRE) | o que foi **lançado** | data de vencimento × pagamento × competência; categorias mal escolhidas |
| **Planilhas** (fluxo mensal, backup de projetos, validação de orçamentos) | o que foi **planejado / orçado** | fórmulas quebradas, valores colados por cima, abas desatualizadas |
| **NF-e de compra** (chapas, ferragens) | custo de material e destino | NF sem projeto vinculado; NF em nome de PF |
| **NF de venda / NFS-e** | faturamento fiscal | valor da NF × valor do contrato |
| **Contratos / propostas** | o que o cliente deve e quando | aditivos e descontos verbais não registrados |
| **Boletos / comprovantes** | pagamento específico | pago duas vezes (boleto + PIX) |

Regra: **todo número do relatório aponta a fonte** (arquivo, aba, linha ou
lançamento). Número sem fonte é hipótese — marcar como tal.

## 2. Roteiro (executar na ordem; cada etapa depende da anterior)

1. **Escopo e período.** Qual conta, qual período, qual pergunta ("por que
   dezembro deu −R$ 54k?"). Definir materialidade: na Valvic, diferenças
   abaixo de **R$ 200 por lançamento** ou **0,5% do mês** só se agregadas.
2. **Integridade das bases.** Saldo inicial do período = saldo final do período
   anterior? Totais do export batem com o relatório do sistema? Há datas fora
   do período, valores zerados, duplicados exatos (mesma data, valor e
   favorecido)? Em planilha: células com valor fixo onde deveria haver fórmula,
   referências `#REF!`, somas que não pegam a última linha.
3. **Conciliação bancária.** Extrato × lançamentos (usar
   `scripts/conciliar_extrato.py`). Casar por valor + janela de data (± 3 dias
   úteis) + texto. Resultado: conciliados / só no banco / só no sistema. Todo
   item não conciliado é explicado ou vira achado.
4. **Contas a receber.** Aging (a vencer, 1–30, 31–60, 61–90, > 90 dias) por
   cliente; conferir cada saldo contra o contrato (valor total − recebido no
   extrato). Distinguir **parcela futura** de **inadimplência** (caso Andre
   Alphaville / Marcelo e Simony). Projetos entregues com saldo aberto > 30 d
   = prioridade de cobrança.
5. **Contas a pagar e compras.** Toda compra de chapa/ferragem tem projeto
   destino? Preço unitário bate com `orcamentista-marcenaria/dados/materiais.json`
   (desvio > 10% = verificar)? Pagamentos duplicados? Fornecedor novo sem
   cadastro? Pagamento a PF sem contrato?
6. **Competência.** Reclassificar o que estiver no mês errado (ver
   `competencia.md`) e fechar a **ponte DRE → caixa**.
7. **Por projeto.** MC orçada × realizada nos projetos entregues no período;
   consumo de chapa real × plano de corte.
8. **Pessoal e sócios.** Folha × lançamentos; comissões calculadas sobre a base
   certa (receita recebida? contratada?); retiradas dos sócios e empréstimo do
   Paulo registrados como movimentação com sócio, não como despesa/receita.
9. **Relatório** (formato abaixo).

## 3. Red flags específicos de marcenaria

- **Chapa comprada > plano de corte** sem retrabalho registrado → desperdício,
  erro de projeto ou desvio de material.
- **Compras de material sem projeto** vinculado ou em véspera de feriado/fim de
  ano, ou entregues em endereço diferente da fábrica.
- **Sobras acumuladas** de chapas de cor/especiais (valor alto, giro baixo).
- **RT paga sem receita** correspondente, paga duas vezes, ou paga sobre valor
  bruto quando a regra é sobre o líquido.
- **Comissão de vendedor/produção** paga sobre contrato que ainda não recebeu
  (se a regra for sobre recebido) ou sobre valor com desconto não registrado.
- **Desconto concedido na entrega** e não registrado — receita do sistema maior
  que o recebido.
- **NF de venda menor que o contrato** ou venda sem NF → risco fiscal
  (apontar o risco; nunca sugerir como esconder).
- **Maquininha:** taxa efetiva acima da contratada; antecipação automática não
  percebida; chargebacks.
- **Terceirizado pago integralmente antes da entrega** do serviço.
- **Mistura PF × PJ:** despesas pessoais pagas pela empresa, empréstimo do
  sócio entrando como "receita", retirada como "despesa administrativa".
- **Investimento em ativo** lançado como despesa operacional (distorce o fixo)
  — ou o contrário.
- Lançamentos com descrição genérica ("diversos", "ajuste", "acerto") acima da
  materialidade.

## 4. Testes rápidos que valem rodar sempre

- **Soma de controle:** Σ entradas − Σ saídas + saldo inicial = saldo final do
  extrato (centavo a centavo).
- **Duplicidade:** mesmo valor + mesmo favorecido em ≤ 5 dias.
- **Números redondos** grandes (R$ 5.000,00, R$ 10.000,00) sem documento.
- **Lançamentos em fim de semana/feriado** em conta que não opera nesses dias.
- **Sequência de NFs** com saltos.
- **Benford** só faz sentido com centenas de lançamentos — não forçar.

## 5. Formato do relatório de auditoria

```
# Auditoria — <escopo> — <período>
Fontes: <lista de arquivos com período>   Materialidade: <R$>

## Resumo para o dono (3–5 linhas)
O que está certo, o que está errado, quanto dinheiro está em jogo, o que fazer primeiro.

## Achados  (ordem: impacto em R$, maior primeiro)
### 🔴/🟠/🟡 Nº — título curto
- Sintoma: o que se vê no número
- Evidência: fonte + linha/lançamento + valores
- Causa raiz (provável / confirmada)
- Impacto: R$ e em qual regime (caixa / competência)
- Tratamento: ação, responsável sugerido (Jonathan, Paulo, Vitor, contador), prazo

## Conciliação / números ajustados
Tabela antes × depois dos ajustes.

## Pendências de informação
O que não deu para concluir e o que precisa ser enviado.
```

Escala: 🔴 crítico (dinheiro saindo ou risco fiscal/legal, ou > 5% do mês),
🟠 relevante (distorce decisão de preço/caixa), 🟡 melhoria de controle.

## 6. Checklist de fechamento mensal (rotina)

1. Baixar extratos de todas as contas + relatório da maquininha.
2. Conciliar banco × Calcme (zero pendências acima da materialidade).
3. Atualizar recebíveis (aging) e cobrar > 30 dias.
4. Vincular todas as NF-e de compra a projetos.
5. Fechar DRE por competência (projetos entregues no mês) + ponte DRE → caixa.
6. MC realizada × orçada dos projetos entregues → lição para a Lavinia.
7. Atualizar fluxo projetado 13 semanas e o `CENTRAL-RODRIGO.md`.
8. Recado do mês: piso de MC (Lavinia) e prioridade comercial (Vitor).
