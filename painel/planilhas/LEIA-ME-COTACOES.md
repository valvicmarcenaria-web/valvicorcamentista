# Valvic — Cotação Comparativa de Fornecedores

Arquivo: `Valvic_Cotacao_Fornecedores.xlsx`
Gerador: `gerar-cotacao-fornecedores.py` (edite o script, nunca o `.xlsx` — regerar sobrescreve)

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
5. Por fornecedor, preencher: % de imposto adicional, frete, % de desconto à vista,
   condição e % de acréscimo a prazo, prazo de entrega e validade.
6. Ler o **Veredito** e registrar o desfecho no **Mapa de Cotações**.

### A regra que faz a planilha funcionar

**Fornecedor que não tem o item → deixar o preço EM BRANCO.** Não escrever zero, não
escrever traço. A célula fica avermelhada e o fornecedor passa a contar como PARCIAL.
É desse detalhe que sai o sinal de "quem entrega o pedido inteiro".

---

## O que é calculado

Por fornecedor:

```
Subtotal          = Σ (quantidade × valor unitário)   [só dos itens cotados]
Imposto           = Subtotal × % imposto adicional
Total bruto       = Subtotal + Imposto + Frete
TOTAL À VISTA     = Total bruto × (1 − % desconto à vista)
TOTAL A PRAZO     = Total bruto × (1 + % acréscimo a prazo)
Custo do prazo    = Total a prazo − Total à vista
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
- **Compra fracionada** — soma o melhor preço de cada item. **É sem imposto e sem
  frete** e implica várias entregas; a comparação é feita contra o subtotal do melhor
  fornecedor completo, e a planilha avisa quando não há ganho.

---

## Sinais visuais

| Cor | Onde | Significa |
|---|---|---|
| Creme | células de entrada | você preenche |
| Cinza-azulado | células calculadas | não digitar |
| Vermelho claro | preço unitário | item que aquele fornecedor não tem |
| Verde claro | preço unitário | menor preço daquela linha |
| Dourado | Total à vista / a prazo | menor total entre os quatro |
| Verde / âmbar / vermelho | Situação do pedido | COMPLETO / PARCIAL / NÃO COTOU |

---

## Limites conhecidos

- **Quatro fornecedores.** Para um quinto, abra uma segunda cotação e compare os vencedores.
- **30 itens por cotação.** Para listas maiores, quebre em duas (ex.: ferragens e chapas).
- **O % de imposto é único por fornecedor**, aplicado sobre o subtotal. Serve para ST, IPI
  ou DIFAL que venham **por fora** do preço. Se cada item tiver alíquota diferente, use o
  valor unitário já com imposto e deixe o campo zerado.
- **O `Pedido de Cotação` aponta para uma aba por vez** (campo do topo). Ele lê a aba cujo
  nome estiver digitado ali — troque o nome, muda o conteúdo.
- **A economia registrada no Mapa** é *maior proposta − valor fechado*. É a leitura de
  negociação, não a diferença contábil.

---

## Fórmulas

Só funções da base do Excel 2007 (`IF`, `MIN`, `COUNT`, `COUNTA`, `SUM`, `ROUND`, `TEXT`,
`INDIRECT`, `IFERROR`, `LEFT`). Nada de `XLOOKUP`, `FILTER`, `UNIQUE` ou `TEXTJOIN` — abre
em qualquer versão do Excel, no LibreOffice e no Google Planilhas.
