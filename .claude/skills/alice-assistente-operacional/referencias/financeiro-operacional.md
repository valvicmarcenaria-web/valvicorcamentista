# Financeiro operacional

A Karla **opera** o financeiro: emite, lança, alerta, cobra e concilia. Ela **não decide**
— desconto, prazo novo, renegociação e prioridade de pagamento são do Jonathan.

## As quatro rotinas fixas

### 1 · Alerta de vencimento — 5 dias antes
Obrigação do cargo. Toda segunda, olhar os 5 dias seguintes e mandar ao Jonathan uma lista
única, não uma mensagem por conta:

> Jonathan, vencem até [dia]:
> • [fornecedor] — R$ [valor] — [dia] — [obra/finalidade]
> • [fornecedor] — R$ [valor] — [dia]
> Total: R$ [soma]. Me confirma quais eu pago e quais seguram?

Uma lista com total é decisão de 30 segundos. Cinco mensagens soltas é decisão adiada.

### 2 · Emissão — boleto e nota fiscal
- Emitir **na data combinada em contrato**, não quando lembrar. Nota atrasada atrasa
  recebimento e desorganiza o mês.
- Conferir antes de enviar: razão social, CNPJ/CPF, endereço, descrição do serviço, valor e
  vencimento. Nota errada volta e queima uma semana.
- Enviar sempre com uma linha de contexto, nunca o arquivo sozinho:
  > [nome], segue a nota fiscal e o boleto da parcela [n] de [total], no valor de R$ [valor],
  > com vencimento em [dia]. Qualquer coisa é só me chamar.

### 3 · Cobrança de cliente
Escalonamento, sempre no mesmo tom cordial:
- **No vencimento** — lembrete gentil (roteiro 6 em `atendimento-whatsapp.md`).
- **D+3** — segundo contato, oferecendo falar com o Jonathan sobre a data.
- **D+7** — para o Jonathan. A partir daqui não é mais tarefa da Karla, e insistir sozinha
  só desgasta a relação dela com o cliente, que ela vai precisar depois.

Nunca: negociar valor, dar desconto por pagamento antecipado, prometer nova data, ameaçar
parar a obra. Tudo isso é decisão comercial.

### 4 · Conciliação
Fechamento nos dias 1 a 5: o que entrou × o que era previsto, o que saiu × o que foi
autorizado. O que não bater vira uma lista de divergências para o Jonathan — não uma
correção feita por conta própria. Planilha:
`painel/planilhas/Valvic_Controle_Pagamentos.xlsx`.

## O que a Karla nunca faz sozinha

| Situação | O que ela faz |
|---|---|
| Cliente pede desconto | Registra e leva ao Jonathan. Não sinaliza que "talvez dê" |
| Cliente pede parcelar diferente | Mesma coisa. A condição de pagamento é comercial |
| Fornecedor oferece condição melhor à vista | Leva ao Jonathan com os números — é decisão de caixa |
| Pagamento acima do limite da fase | Pede autorização por escrito antes |
| Sobrou ou faltou dinheiro na conciliação | Aponta a divergência, não ajusta o lançamento |

## Onde estão as coisas

- `painel/planilhas/Valvic_Controle_Pagamentos.xlsx` — controle de pagamentos
- `painel/planilhas/Valvic_Custo_por_Projeto.xlsx` — custo por projeto
- `painel/contas-receber-pagar-valvic.html` — panorama de contas
- `painel/planilhas/LEIA-ME-PAGAMENTOS.md` — como a planilha funciona

Quando a pergunta for de **saúde financeira** — margem, break-even, se o preço fecha, se o
mês está saudável — isso não é da Alice: é do **Rodrigo** (skill
`estrategia-financeira-precificacao`). A Alice opera o dia a dia; o Rodrigo lê o conjunto.
