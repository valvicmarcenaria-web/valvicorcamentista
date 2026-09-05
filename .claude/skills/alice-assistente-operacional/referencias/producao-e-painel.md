# Interface com a produção e o painel semanal

Duas coisas diferentes: **transmitir demanda** (todo dia) e **montar o painel da semana**
(toda segunda). A Karla é o fio entre o comercial e a fábrica — e a qualidade desse fio
determina se a obra sai no prazo.

## Transmitir com fidelidade

A regra do escopo é literal: **com fidelidade**. Significa que a Karla passa o que foi dito,
não a interpretação dela do que foi dito. Três hábitos:

1. **Repetir para confirmar.** "Entendi que o cliente quer a porta abrindo para a direita e
   que aceita a entrega dia 12. Confere?" — antes de levar para a fábrica.
2. **Registrar por escrito.** Combinado por telefone ou no corredor vira mensagem. O que não
   está escrito vira discussão de versão depois.
3. **Nunca alterar projeto no caminho.** Se o cliente pedir mudança, ela **não resolve** —
   registra e leva ao Jonathan (comercial) ou ao Paulo/Deivison (viabilidade). Alteração de
   projeto sem autorização é uma das regras que valem para todos na Valvic.

Modelo de repasse ao Deivison:
> Deivison, da obra da [cliente]: [o que foi pedido, com as palavras do cliente].
> Quem pediu: [cliente / Jonathan]. Quando: [dia]. Precisa de resposta até [dia]?

## O painel semanal de produção

O quadro A3 que fica na parede da fábrica. É o instrumento mais usado da casa — a semana
inteira da equipe numa folha.

**Modelo:** `painel/painel-producao-a3.html`
**Gerar o PDF:** `python3 ferramentas/gerar-pdf.py painel/painel-producao-a3.html`

### Como o painel é montado

Três folhas A3 paisagem: **a semana atual**, **a semana seguinte** e o **placar de
entregas**. Uma linha por pessoa, uma coluna por dia.

O conteúdo mora num objeto JavaScript no fim do arquivo — **edite ali, não no HTML de
cima**. A estrutura:

```js
const P = {                                  // um projeto = uma cor
  simony:{n:'Simony', c:'#0E2038'},
  augusto:{n:'Augusto', c:'#B0413F'}, ...
};

linha('Deivison','Coordenação de produção', 0, [   // 0 = não é freelancer
  card('simony','Banheiro social<br>e despensa'),  // segunda
  card('simony','Banho do casal'),                 // terça
  ...
], S1)                                             // S1 = os dias da semana
```

Recursos que já existem e economizam tempo:
- **`card(projeto, texto)`** — o bloco colorido do projeto. Dois cards na mesma célula =
  duas frentes no mesmo dia.
- **`card(projeto, texto, true)`** — marca **A CONFIRMAR** (tarja tracejada). Use para
  quem ainda não confirmou presença; é honesto e evita quadro que mente.
- **`off(texto)`** — pessoa sem frente definida. Não deixar a célula vazia sem explicar.
- **`{h: card(...), span: 4}`** — uma frente que ocupa vários dias vira **uma barra só**, em
  vez de quatro cards repetidos. Fica muito mais legível de longe.
- Cada card tem um **quadradinho para marcar ao concluir** — o painel é para riscar, não só
  para olhar.

### As perguntas que a Alice faz antes de montar

Nunca montar o painel adivinhando. O mínimo que precisa saber:
1. **Quem trabalha esta semana** e quem é freelancer ou está a confirmar.
2. **Que obras estão em montagem** e quais estão em fabricação.
3. **Quem coordena** cada frente.
4. **O que precisa chegar** (material) e em que dia — porque frente sem material é frente
   que não acontece.
5. **Sábado e domingo**: tem alguém? quem supervisiona?

Se faltar algo, perguntar — uma pergunta objetiva vale mais que um painel bonito e errado.

### Regras de leitura que fazem o painel funcionar

- **Fim de semana com fundo diferente** — o olho precisa achar sozinho.
- **Cor = projeto, não pessoa.** É assim que se enxerga, de longe, quantas frentes uma obra
  está consumindo.
- **Frase curta no card.** O painel é lido em pé, a dois metros. "Cozinha — parte de baixo"
  funciona; um parágrafo não.
- **A confirmar aparece como a confirmar.** Painel que finge certeza perde a confiança da
  equipe na primeira vez que fura.

### Depois de montar
Gerar o PDF, conferir que `over_sheet` deu **0**, imprimir em A3 e colar. E mandar a foto
do quadro no grupo — quem está em obra não passa na fábrica.

## Cobrar a produção sem entrar no mérito técnico

Isso tem regra própria e é o ponto onde a Karla mais pode se queimar. Ver
`cobranca-de-rotinas.md`.
