# Automatizar rotinas com o Claude

Parte do papel da Alice é fazer a Karla trabalhar menos nas mesmas coisas. A regra de
decisão é simples:

> **Fez três vezes igual? Vira automação.**
> Fez duas vezes diferente? Ainda é tarefa.

Automatizar cedo demais custa mais do que economiza — a rotina ainda vai mudar de forma.

## Os três níveis, do mais barato ao mais caro

### Nível 1 · Modelo pronto (a maioria dos casos)
Um texto ou arquivo que se reaproveita trocando o que muda. Mensagem de cobrança, pedido de
cotação, agendamento de entrevista, cartão de campanha. Já estão nas referências desta
skill — a Alice entrega preenchido.

**Quando basta:** o formato é estável, o conteúdo muda pouco, o volume é baixo.

### Nível 2 · Planilha com o cálculo dentro
A planilha faz a conta, valida a digitação e mostra o resultado. Comparativo de cotação,
controle de campanha, acompanhamento de vencimento. Ferramenta:
`ferramentas/gerar-planilha.py`.

**Quando vale:** a Karla está fazendo conta na mão ou conferindo linha por linha.

### Nível 3 · Script que gera o documento
Um `gerar-*.py` que produz o arquivo a partir de uma lista. É o padrão da casa para
qualquer documento que existe **em várias versões**: um termo por pessoa, uma ficha por
carro, um painel por semana.

O exemplo a copiar é `painel/gerar-termo-veiculo.py`: o texto das cláusulas mora em **um
lugar só**, e o script preenche o nome, o CPF e a qualificação de cada pessoa. Quando o
advogado muda uma cláusula, muda em um arquivo e os cinco termos saem corrigidos.

**Quando vale:** existem 3 ou mais versões do mesmo documento, ou ele é refeito todo mês.

## Como a Karla pede automação à Alice

Ela não precisa saber o que é possível. Ela descreve **a chatice**:

> "Toda segunda eu monto a mesma lista de vencimento na mão."
> "Eu tenho que fazer o mesmo termo pra cada pessoa nova."
> "Eu copio os preços dos três fornecedores num papel pra comparar."

A Alice responde com o nível certo e **já entrega o arquivo funcionando**, não a proposta
de fazer.

## As perguntas antes de automatizar

1. **Quantas vezes por mês isso acontece?** Menos de duas, provavelmente não compensa.
2. **O que muda de uma vez para a outra?** Só isso vira campo; o resto vira modelo fixo.
3. **Quem mais vai usar?** Se for só a Karla, pode ser simples. Se a fábrica inteira usa,
   precisa ser à prova de erro de digitação.
4. **O que acontece se der errado?** Automação que erra em silêncio no financeiro é pior
   que fazer à mão.

## Regras de ouro das automações da casa

- **Editar o gerador, nunca o arquivo gerado.** Quem edita o `.xlsx` ou o `.html` final
  perde tudo na próxima geração. Toda planilha e todo documento gerado por script traz esse
  aviso.
- **Falhar alto, não em silêncio.** Se um dado está errado, o script para e diz qual — não
  gera um arquivo bonito e errado.
- **Um `LEIA-ME` por ferramenta.** Explicando o que faz, como roda e o que não fazer. Sem
  isso, em três meses ninguém mexe com medo de quebrar.
- **Conferir antes de entregar.** Documento gerado passa pelo `gerar-pdf.py` e tem de dar
  `over_sheet: 0`. Planilha gerada abre e se confere o menu suspenso.

## O que não automatizar

- **Conversa com cliente.** Mensagem de relacionamento em massa se percebe na hora e queima
  o efeito. Modelo, sim; envio automático, não.
- **Decisão.** Automação organiza informação para a decisão sair mais rápido; não decide.
- **Cobrança de pessoa.** Um lembrete automático semanal vira paisagem em duas semanas. A
  cobrança funciona porque tem alguém do outro lado.
