# PÓRTICO E MÓVEL RIPADO — proposta de uma folha

★ **Cliente sem nome.** O Jonathan passou escopo, preço e prazo, não o nome.
A folha saiu com o cabeçalho "Proposta · 7 de outubro de 2026", sem
destinatário. **Falta preencher antes de enviar.**

Build: `build-portico-ripado.py` → `proposta-portico-ripado.pdf`.
Imagens: `img/portico-vao.jpg` e `img/movel-ripado.jpg`.

---

## 07/10/2026 — a folha

> *"monte uma proposta de uma página usando essas imagens para compor o
> layout descrevendo o seguinte serviço: pórtico de acabamento em vão da
> sala · estrutura de móvel ripado com duas portas de giro e laterais, sendo
> ambas vazadas com usinagem em Router CNC. Réguas de 50mm de largura com
> espaçamento de 15mm, sem laminação nos vãos internos das usinagens. Em mdf
> amadeirado ultra (mais resistente a umidade) · investimento R$ 6.500,
> prazo 60 dias, entrada de 40% restante na entrega do projeto"*

### O escopo e o preço

| | |
|---|--:|
| investimento | **R$ 6.500** |
| entrada, 40% | R$ 2.600 |
| na entrega | R$ 3.900 |
| prazo | 60 dias |

⛔ **Não há motor de custo aqui.** O preço veio pronto do Jonathan — não dá
para dizer a MC. Se o ripado for grande, R$ 6.500 pelos dois serviços é
pouco: o vazado em Router CNC é hora de máquina, e o MDF Ultra custa mais
que o amadeirado comum.

### O layout

Um bloco por serviço, com a foto alternando de lado. A foto manda na altura
do bloco — foi reduzir a do ripado de 56 para 48 mm de largura que devolveu
a maior parte do espaço quando a folha estourou.

### ⛔ As imagens vieram sujas

A do ripado era um **gráfico comparativo de outra fonte**, com rótulos
("1. ARMÁRIO RIPADO (MADEIRA) · Ventilado, elegante e moderno") e dois
painéis cortados à direita. Recortada para `(0,100)-(633,980)`, sai tudo.

A do pórtico tinha a mesa do almoço em primeiro plano — garrafas, pratos,
um quadro na parede. Recortada para `(70,118)-(1180,628)`, fica só o vão.

★ **Não sei se as fotos são do apartamento do cliente ou de obra anterior.**
As legendas foram escritas para funcionar nos dois casos — descrevem o que
se vê, não de onde vem. Se forem de outra obra, vale marcar "referência",
senão o cliente lê como se fosse a casa dele.

### ⛔⛔ Metragem autorizada

"Réguas de **50 mm** com espaçamento de **15 mm**" entra na proposta por
pedido explícito do Jonathan. É **especificação, não quantitativo** — o
passo do ripado é o produto. Registrado na tabela de exceções em
`referencias/proposta-comercial.md`. "Duas portas de giro" idem: delimita o
escopo do móvel.

### ⛔⛔ O rodapé sumiu e os três passes disseram "ok"

A folha estourou, o rodapé foi empurrado para fora, e nenhum passe pegou:

* o passe 2 só avisava `if not fb and i > 1` — e numa folha única `i` é
  sempre 1, justamente o caso em que a página 1 **tem** rodapé;
* o passe 1 procurava **presença**, e "Valvic Marcenaria" sobreviveu no
  cabeçalho.

Os dois consertos são o mesmo: **contar, não procurar.** O auditor também
saiu do `/tmp` e passou a morar em `ferramentas/auditor-proposta.py`.

Depois da compactação: folga 36,1 pt, três passes limpos.

---

## Em aberto

1. ★ **O nome do cliente** — a folha está sem destinatário.
2. ★ **As fotos são da obra dele ou de referência?** Muda a legenda.
3. ★ **R$ 6.500 cobre os dois serviços?** Sem motor de custo não dá para
   dizer. O vazado em Router CNC é hora de máquina e o MDF Ultra é mais
   caro que o amadeirado comum.
4. **O pórtico já aparece instalado na foto.** Se a foto é do apartamento
   do cliente, o item 01 já estaria feito — vale confirmar.
