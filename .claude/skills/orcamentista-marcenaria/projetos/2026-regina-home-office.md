# REGINA — home office

Briefing por **WhatsApp**, com uma imagem de referência (20/10/2026).

> mesa 2,30 comprimento · 0,80 largura · 0,75 altura
> 3 gavetas pequena e uma gaveta arquivo
> móvel para acoplar o PC (compoutador)
> painel no fundo com previsão de tomadas elétricas
> prateleira para finalizar o painel
> painel de 230 × 105 cm e prateleira de 230 × 25 cm, com **espessura
> visual de 5 cm**

⭐ [Jonathan 20/10] **"MDF melamínico, corrediça oculta da rede, sem RT e
uma margem de contribuição de 35%."**

MC **37%** · **sem RT** · base **85.35%**

---

## ⛔⛔ "Espessura visual de 5 cm" não é peça de 5 cm

**MDF não existe em 50 mm**, e colar três chapas para chegar lá seria
jogar dinheiro fora. A peça é uma **caixa**: face em 18 mm e **testeira
de 5 cm** nas bordas que aparecem, com sarrafo de alma por dentro. O
cliente vê 5 cm; a peça pesa o que pesa uma de 18.

São **0.67 m² de testeira** — e é isso que se vê. Pela leitura
literal seriam **mais 10.81 m² de MDF de cor**, cerca de
**R$ 1.800 só de chapa**, antes de fita e de mão de obra.

---

## O que cabe na chapa

A chapa é **2,75 × 1,85** e as três peças grandes têm 2,30 de
comprimento: mesa, painel e prateleira. **Todas cabem inteiras, sem
emenda.**

| cor · espessura | área m² | chapas | R$ |
|---|--:|--:|--:|
| Branco TX · 6 mm | 1.01 | 1 | 190 |
| Branco TX · 15 mm | 3.03 | 1 | 260 |
| Cor · 15 mm | 0.65 | 1 | 500 |
| Cor · 18 mm | 6.91 | 2 | 1.200 |
| **total** | **11.60** | **5** | **2.150** |

⚠ A **sobra** comprada e não usada é **R$ 811** — 38% da chapa. O painel de 2,30 ×
1,05 come metade de uma folha e deixa um **L** que não serve para outra
peça de 2,30. É o preço de um móvel comprido num ambiente pequeno.

---

## Móvel a móvel

| móvel | | custo | **preço** |
|---|---|--:|--:|
| **Mesa** | 2,30 × 0,80 × 0,75, tampo com espessura visual de 5 cm, apoiado no gaveteiro e numa lateral | 711 | **1.470** |
| **Gaveteiro** | três gavetas pequenas e uma gaveta arquivo, corrediça oculta, puxador cava | 1.478 | **3.060** |
| **Móvel do PC** | nicho acoplado sob o tampo para o computador | 166 | **340** |
| **Painel** | 2,30 × 1,05, espessura visual de 5 cm, com os recortes das tomadas | 719 | **1.490** |
| **Prateleira** | 2,30 × 0,25, espessura visual de 5 cm, sobre suporte oculto | 466 | **960** |
| | **custo direto** | **3.540** | |
| | **INVESTIMENTO** | | **R$ 7.320** |

---

## ★ Em aberto

1. ⚠ **A cor não veio.** A imagem é amadeirada; orçei **MDF melamínico de
   cor** (R$ 600 a chapa de 18) com caixaria em Branco TX. Amadeirado
   de linha especial muda o preço — confirmar o padrão.
2. ⚠ **A espessura da mesa não veio.** A cliente deu os 5 cm visuais para
   o **painel** e a **prateleira**. Adotei o mesmo no tampo da mesa, que é
   o que a imagem mostra. Com tampo liso de 18 mm a mesa cairia
   **R$ 100**, de R$ 1.470 para R$ 1.370.
3. ⚠ **"Previsão de tomadas elétricas":** os **recortes** no painel são
   nossos; a **tomada, o ponto e o circuito** são da elétrica. Se a
   cliente quiser **caixa de tomada embutida** na marcenaria, é item à
   parte (a base da casa traz R$ 260).
4. ⚠ **Como a mesa se apoia.** Orçei com o **gaveteiro de um lado e uma
   lateral do outro**, amarrados por travessa. Se a cliente quiser a mesa
   **flutuando na parede**, entra estrutura metálica e o preço muda.
5. ★ **"Corrediça oculta da rede"** — orçada a **R$ 190 o par**, a
   oculta de distribuição nacional. A Hettich sai a R$ 190.
   ⚠ Garantia da oculta na casa: **5 anos** (a telescópica dá 2).
6. ⚠ **O áudio de 6 segundos** que veio depois do briefing não foi
   transcrito para mim, e **a mensagem seguinte foi apagada**. Se houver
   escopo ali, não está neste preço.
7. ⛔ **Medir no local antes de cortar.** As três peças de 2,30 cabem
   inteiras na chapa, mas só se a parede confirmar os 2,30.
8. ⛔ **O puxador não está no briefing escrito**, mas a imagem da cliente
   mostra **barra preta** nas gavetas. Orçei barra a ★ R$ 35/un. Em
   puxador cava usinado na frente, a ferragem some e o gaveteiro cai.
9. ⚠ **A imagem mostra a mesa virando a quina**, com um retorno na parede
   da direita. O briefing escrito diz 2,30 × 0,80 e é isso que está
   orçado. **Se houver retorno, é outro módulo.**

---

## A proposta — `build-regina.py`

**`proposta-regina.pdf`, quatro páginas.** Segue a ordem que o Jonathan
fixou em 19/10: **nenhum preço antes de gerar valor**.

* **Capa** com a referência da cliente e faixa escura. Sem preço.
* **Quem faz** — marcenaria própria, as cinco etapas do processo, a
  garantia de **10 anos** atrelada à corrediça Hettich, e um bloco
  explicando a **espessura aparente construída em caixa**: o móvel
  entrega o desenho sem o peso.
* **O projeto, peça por peça**, com a referência de novo.
* **Investimento**, com o à vista em destaque e a escada de pagamento.
* ⛔ O build trava com `assert` se aparecer qualquer `R$` antes da última
  página, e se o motor e a proposta deixarem de falar dos mesmos móveis
  — foi essa segunda trava que pegou *"Painel"* × *"Painel do fundo"*.
* ⭐ A única imagem é a **referência da própria cliente**, recortada do
  print de WhatsApp e nomeada como tal. **Não é render nosso**, e a
  folha diz isso.
* Três passes do auditor: **tudo OK**.
