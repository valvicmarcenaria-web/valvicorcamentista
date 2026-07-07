# Planilhas & Geração de Relatórios

A Helena é fluente em **planilhas** (Google Sheets / Excel) e em transformar dado bruto em
**relatório que apoia decisão**. O padrão de saída visual da Valvic já existe (os documentos
`painel/*.html` → PDF) — a Helena liga o dado ao documento.

## Princípio: dado → planilha → relatório
1. **Dado bruto** vem do Calcme (financeiro, produção), do banco, ou de levantamento manual.
2. **Planilha** organiza, cruza e valida (a camada de trabalho — não é o entregável).
3. **Relatório** comunica: números-âncora, visual limpo, uma mensagem por página. Para
   entrega premium, vira documento no padrão Valvic (ver `gestao-documentos.md`).

## Boas práticas de planilha (que evitam erro)
- **Uma aba = um propósito** (dados brutos · cálculos · resumo). Não misturar.
- **Entrada separada do cálculo:** células de input identificadas; fórmulas não sobre dado digitado.
- **Fórmulas em vez de conta na mão:** `SOMASE`/`SUMIF`, `PROCV`/`XLOOKUP`, tabelas dinâmicas
  para agrupar por categoria/mês (foi assim que saíram os panoramas de contas a receber/pagar).
- **Validação de fechamento:** totais que batem por dois caminhos (linha × coluna); `assert`
  mental — "isto tem que dar X".
- **Formatação de número:** milhar, 2 casas, tabular; datas ISO na base, PT-BR na saída.
- **Rastreável:** fonte do dado e data no rodapé da aba. "De onde veio esse número?" sempre respondível.

## Relatórios recorrentes da Valvic
| Relatório | Fonte | Cadência | Vira documento? |
|---|---|---|---|
| Fluxo de caixa / contas a pagar-receber | Calcme financeiro | Semanal/mensal | Sim — `contas-receber-pagar-valvic.html` |
| Fechamento do mês (MC × custo fixo, break-even) | Calcme + custo fixo | Mensal | Análise do Rodrigo |
| Status de produção (pedidos por etapa) | Calcme PCP/Kanban | Semanal | Painel interno |
| Patrimônio / estrutura de custos | Levantamento | Sob demanda | Sim — docs do `painel/` |
| Panorama para investidor | Consolidação | Sob demanda | Sim — apresentação Walton |

## Do dado ao documento visual (o pipeline Valvic)
Quando o relatório precisa ser **entregável premium** (sócio, investidor, cliente):
1. Fechar os números na planilha (validados).
2. Levar para o HTML no padrão Valvic (navy/gold/cream, A4/A3, print-ready).
3. Gerar PDF (Playwright/Chromium) e **conferir cada página por screenshot**.
4. Registrar no `dados/mapa-documentos.md`.

> A planilha é o **motor**; o documento é a **carroceria**. O cliente/sócio vê a carroceria;
> a Helena garante que o motor (os números) esteja certo por baixo.

## Cuidados
- **Sigilo:** planilha com dado financeiro/folha é **restrita** — compartilhar só com quem deve,
  com permissão certa no Drive (ver `operacoes-drive.md`).
- **Fonte única:** a planilha canônica mora no Drive, no lugar certo; nada de versões soltas
  no desktop divergindo.
