# Valvic — Cotação Comparativa de Fornecedores

Arquivo: `Valvic_Cotacao_Fornecedores.xlsx`
Gerador: `gerar-cotacao-fornecedores.py` (edite o script, nunca o `.xlsx` — regerar sobrescreve)
Testes: `testar-cotacao.py` (184 verificações) · `simular-cotacao.py` (8 cenários de borda)

Planilha de apoio a **cotações pontuais**: uma demanda, até quatro fornecedores, decisão
em cima de número e não de memória de WhatsApp.

---

## Abas

| Aba | Para que serve |
|---|---|
| **Instruções** | Passo a passo, regras de leitura e cuidados. Imprimível em A4. |
| **Cotação** | O modelo. Duplique esta aba a cada nova demanda. |
| **Pedido de Cotação** | Formulário A4 para enviar ao fornecedor. Puxa os itens sozinho. |
| **Exemplo** | Cotação preenchida (ferragens da obra Cristiane) mostrando o comportamento. |
| **Mapa de Cotações** | Registro histórico: nº, demanda, quem venceu, quanto foi fechado, economia. |
| **Listas** | Alimenta os menus suspensos. Não apagar nem reordenar colunas. |

---

## Como usar

1. Botão direito na aba **Cotação** → *Mover ou copiar* → marcar **Criar uma cópia**.
   Renomear a cópia (ex.: `COT-2026-015 Chapas`).
2. Preencher identificação, itens (descrição, unidade, quantidade) e o nome dos quatro
   fornecedores.
3. Opcional: abrir **Pedido de Cotação**, digitar o nome da aba nova no campo do topo e
   salvar em PDF para enviar ao fornecedor.
4. Conforme as respostas chegam, digitar **só o valor unitário**. O total sai sozinho.
5. Na barra fixa, preencher o **% de imposto padrão** de quem cota sem imposto
   (o clássico "preços s/ IPI = 6,5%"). Item com alíquota diferente: digitar o %
   na coluna `% IMP.` daquela linha — o da linha manda, o padrão só vale quando a
   linha está vazia.
6. Por fornecedor, preencher: frete, % de desconto à vista, condição e % de
   acréscimo a prazo, prazo de entrega e validade.
7. Ler o **Veredito** e registrar o desfecho no **Mapa de Cotações**.

### A regra que faz a planilha funcionar

**Fornecedor que não tem o item → deixar o preço EM BRANCO.** Não escrever zero, não
escrever traço. A célula fica avermelhada e o fornecedor passa a contar como PARCIAL.
É desse detalhe que sai o sinal de "quem entrega o pedido inteiro".

---

## A barra fixa

As linhas até o cabeçalho da tabela ficam congeladas. Por mais que você desça na
lista de itens, a barra mostra de cada fornecedor:

| Célula | Conteúdo |
|---|---|
| sob `UNIT.` | quantos itens ele cotou (`7/8`) — verde quando completo, âmbar quando falta |
| sob `% IMP.` | o **% de imposto padrão** do fornecedor (entrada) |
| sob `TOTAL` | o **TOTAL DO PEDIDO**, já com imposto e frete, atualizando enquanto você digita |

O menor total do pedido fica com fundo dourado.

---

## Imposto por item

Cada fornecedor tem um `% imposto padrão` na barra fixa e cada item tem sua
coluna `% IMP.`. A regra é uma só:

```
% aplicado = % da linha do item, se preenchido
             senão, % padrão do fornecedor
             senão, zero
```

Assim o fornecedor que manda "PREÇOS S/ IPI = 6,5%" entra na comparação com o
preço que vai cobrar de verdade — e o item isento daquele mesmo fornecedor pode
ser corrigido sozinho, sem mexer nos outros.

**A comparação entre fornecedores é sempre pelo TOTAL do item, nunca pelo preço
de tabela.** Sem isso, quem cota sem imposto parece mais barato e não é.

---

## O que é calculado

Por item e fornecedor:

```
Total do item = quantidade × valor unitário × (1 + % imposto aplicado)
```

Por fornecedor:

```
Subtotal sem imposto = Σ (quantidade × valor unitário)   [só dos itens cotados]
Subtotal com imposto = Σ (totais dos itens)
Imposto              = subtotal com imposto − subtotal sem imposto
TOTAL DO PEDIDO      = Subtotal com imposto + Frete        ← é o da barra fixa
TOTAL À VISTA        = Total do pedido × (1 − % desconto à vista)
TOTAL A PRAZO        = Total do pedido × (1 + % acréscimo a prazo)
Custo do prazo       = Total a prazo − Total à vista
```

Situação do pedido:

```
COMPLETO   → cotou todos os itens da lista
PARCIAL    → mostra quantos itens faltam
NÃO COTOU  → não respondeu nada
```

Veredito (rodapé):

- **Melhor preço à vista** — o menor de todos, com a situação do pedido ao lado
  (pode ser um PARCIAL barato, e isso precisa aparecer).
- **Melhor à vista entre os completos** — na prática, o número que decide.
- **Melhor preço a prazo** — com a condição oferecida.
- **Compra fracionada** — soma o melhor preço de cada item (já com imposto). **É sem
  frete** e implica várias entregas; a comparação é contra o subtotal do melhor
  fornecedor completo, com três respostas possíveis: economia de R$ X, "não compensa
  dividir" (empate) ou "sem ganho: sai R$ X mais caro".

**Desempate:** dois fornecedores com o mesmo preço → a planilha aponta o que está
mais à esquerda. O desempate real é seu: prazo, histórico, relacionamento.

---

## Sinais visuais

| Cor | Onde | Significa |
|---|---|---|
| Creme | células de entrada | você preenche |
| Cinza-azulado | células calculadas | não digitar |
| Vermelho claro | preço unitário | item que aquele fornecedor não tem |
| Verde claro | total do item | menor total daquela linha |
| Verde / âmbar sólido | barra fixa (`7/8`) | pedido completo / parcial |
| Dourado | Total à vista / a prazo | menor total entre os quatro |
| Verde / âmbar / vermelho | Situação do pedido | COMPLETO / PARCIAL / NÃO COTOU |

---

## Limites conhecidos

- **Quatro fornecedores.** Para um quinto, abra uma segunda cotação e compare os vencedores.
- **30 itens por cotação.** Para listas maiores, quebre em duas (ex.: ferragens e chapas).
- **Item sem quantidade, ou que ninguém cotou**, fica fora da conta. A planilha avisa
  na linha da compra fracionada ("X item(ns) fora da comparação").
- **O `Pedido de Cotação` aponta para uma aba por vez** (campo do topo). Ele lê a aba cujo
  nome estiver digitado ali — troque o nome, muda o conteúdo.
- **A economia registrada no Mapa** é *maior proposta − valor fechado*. É a leitura de
  negociação, não a diferença contábil.

---

## Fórmulas

Só funções da base do Excel 2007 (`IF`, `MIN`, `COUNT`, `COUNTA`, `SUM`, `SUMPRODUCT`,
`ROUND`, `TEXT`, `INDIRECT`, `IFERROR`, `LEFT`, `OR`). Nada de `XLOOKUP`, `FILTER`,
`UNIQUE` ou `TEXTJOIN` — abre em qualquer versão do Excel, no LibreOffice e no Google
Planilhas.

Uma ressalva de idioma: o texto da compra fracionada usa `TEXT(...,"R$ #,##0.00")`, que
respeita a configuração regional da máquina. Em pt-BR sai `R$ 103,80`; num Excel em
inglês sairia `R$ 103.80`. Não afeta nenhum cálculo, só esse texto.

---

## Testes

```
python3 gerar-cotacao-fornecedores.py    # gera o .xlsx
python3 testar-cotacao.py                # 184 verificações, 0 falha
python3 simular-cotacao.py               # 8 cenários de borda
```

`testar-cotacao.py` calcula as fórmulas de verdade (biblioteca `formulas`) e confere
contra um modelo independente escrito em Python — totais por item, menor preço,
vencedor de cada linha, apuração, barra fixa, veredito, planilha em branco e o Mapa.

`simular-cotacao.py` monta variantes e mostra a resposta da planilha em: fornecedor
que não respondeu · empate exato · item que ninguém cotou · os quatro completos ·
fracionar sem ganho · IPI só na linha · linha sobrepondo o padrão do fornecedor ·
item sem quantidade.

O arredondamento segue o do Excel (meio para cima, com normalização de 15 dígitos
significativos), não o arredondamento bancário do Python — a diferença aparece em
casos como `6 × 125,50 × 1,065`, que dá 801,95 e não 801,94.
