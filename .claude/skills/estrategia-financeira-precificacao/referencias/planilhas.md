# Planilhas financeiras — padrão Valvic

Planilha financeira boa é **auditável**: qualquer pessoa consegue seguir um
número até a origem. Planilha ruim tem valor colado por cima de fórmula e
ninguém sabe de onde veio o total.

## 1. Arquitetura (separar dado, regra e relatório)

| Aba | Conteúdo | Quem edita |
|---|---|---|
| `Premissas` | % de NF, maquininha, comissões, RT, saldo mínimo, datas | só o Rodrigo/Jonathan, células em azul |
| `Plano_Contas` | categoria → grupo DRE → grupo fluxo → fixo/variável | raramente |
| `Lancamentos` | uma linha por movimento: data competência, data caixa, valor (+/−), categoria, projeto, cliente/fornecedor, conta, documento, status | operação |
| `Projetos` | contrato, valor, cronograma de parcelas, data de entrega, MC orçada | operação |
| `Fluxo_Mensal` / `Fluxo_13s` | **só fórmulas** (SOMASES sobre `Lancamentos` e `Projetos`) | ninguém digita |
| `DRE` | **só fórmulas** por competência | ninguém digita |
| `Recebiveis` | aging por cliente (fórmulas) | ninguém digita |
| `Checks` | testes de integridade (somas de controle, diferenças = 0) | ninguém digita |

O script `scripts/gerar_planilha_financeira.py` gera esse modelo pronto (xlsx,
com fórmulas vivas) — partir dele em vez de desenhar do zero.

## 2. Convenções

- **Uma linha = um fato.** Nada de "parcelas 1 a 3" numa célula só.
- **Duas datas** em cada lançamento: `data_competencia` e `data_caixa`
  (vencimento quando ainda não pago + status). É isso que permite tirar DRE e
  fluxo da mesma base.
- **Sinal único:** entradas positivas, saídas negativas. Nunca uma coluna de
  "tipo" com valores sempre positivos (gera soma errada em tabela dinâmica).
- **Cores:** azul = entrada manual; preto = fórmula; verde = vínculo de outra
  aba; fundo amarelo = premissa que precisa de validação.
- **Sem número mágico dentro de fórmula** (`=B5*0,07`) → referenciar
  `Premissas` (`=B5*Premissas!$C$4`).
- **Categorias fechadas** com validação de dados (lista suspensa) puxando do
  `Plano_Contas` — acaba com "Chapas", "chapa", "MDF" virando 3 categorias.
- **Valores em R$ com 2 casas**, formato `R$ #.##0,00;[Vermelho]-R$ #.##0,00`.
- **Datas como data**, não texto ("05/10" texto quebra SOMASES).
- Congelar cabeçalho, filtros na base, larguras legíveis.

## 3. Fórmulas que resolvem 90% (Excel PT-BR / Google Sheets)

| Necessidade | Fórmula |
|---|---|
| Soma por categoria e mês (caixa) | `=SOMASES(Lanc[valor];Lanc[grupo_fluxo];$A5;Lanc[data_caixa];">="&C$3;Lanc[data_caixa];"<"&FIMMÊS(C$3;0)+1)` |
| Mesma coisa por competência | trocar `data_caixa` por `data_competencia` |
| Buscar categoria → grupo | `=PROCX(D2;Plano[categoria];Plano[grupo_dre];"SEM CATEGORIA")` (Sheets: `XLOOKUP` ou `PROCV(...;FALSO)`) |
| Saldo acumulado | `=saldo_anterior + variação_do_mês` (nunca digitar o saldo) |
| Dias em atraso | `=SE(status="aberto";MÁXIMO(0;HOJE()-vencimento);0)` |
| Faixa de aging | `=SES(d=0;"a vencer";d<=30;"1-30";d<=60;"31-60";d<=90;"61-90";VERDADEIRO;">90")` |
| MC % | `=SEERRO(MC/Receita;0)` |
| Check (deve dar 0) | `=ARRED(saldo_calculado - saldo_extrato;2)` com formatação condicional vermelha se ≠ 0 |

Google Sheets aceita os nomes em PT-BR conforme a localidade; em `openpyxl`
grave as fórmulas **em inglês** com vírgula (`=SUMIFS(...)`, `=IFERROR(...)`) —
o Excel traduz ao abrir.

## 4. Revisando uma planilha recebida (auditoria de planilha)

1. Mapear abas e o fluxo de dados (o que alimenta o quê).
2. Procurar valores fixos em colunas de fórmula (em Python: `openpyxl` com
   `data_only=False`, checar `cell.data_type == 'f'` linha a linha).
3. Procurar `#REF!`, `#N/D`, `#DIV/0!` e intervalos de soma que não chegam à
   última linha.
4. Recalcular os totais por fora (pandas) e comparar.
5. Verificar se categorias e datas são consistentes (texto × data, grafias).
6. Reportar como achado de auditoria (formato em `auditoria-financeira.md`).

## 5. Lendo exports

- **Calcme**: exportar contas pagas/recebidas em xlsx/csv; conferir quais
  colunas de data existem (emissão, vencimento, pagamento). Categoria do Calcme
  → mapear para o `Plano_Contas`.
- **Extrato bancário**: OFX é o mais confiável (tem ID de transação); CSV muda
  de layout por banco (separador `;`, decimal `,`); PDF → extrair tabela com
  `pdfplumber` e conferir o saldo final antes de usar.
- **Maquininha**: o depósito é líquido e agrupado por dia — conciliar com o
  relatório de vendas da adquirente, não venda a venda.
- Ler CSV brasileiro: `pd.read_csv(f, sep=';', decimal=',', thousands='.', encoding='latin-1')`
  (tentar `utf-8-sig` se falhar).

## 6. Entregar

- Planilha nova → xlsx gerado com fórmulas (não valores), aba `Checks` zerada,
  e um parágrafo explicando como alimentar.
- Análise de planilha existente → relatório + planilha corrigida em **arquivo
  novo** (nunca sobrescrever o original do usuário).
- Se o usuário trabalha no Google Sheets, entregar o xlsx (importa sem perda)
  ou usar o conector do Google Drive quando disponível.
