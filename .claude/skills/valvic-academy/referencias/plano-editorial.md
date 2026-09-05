# Plano editorial da Academy — como o núcleo vira apostila

O `escopo-do-nucleo.md` diz **o que** se escreve. Este diz **como isso vira papel e tela**:
em quantos volumes, o que é encadernado e o que não pode ser, quem recebe o quê, e como a
versão impressa não fica mentindo seis meses depois.

Decidido com o Jonathan em 09/2026: **apostila impressa e encadernada + versão digital.**

---

## 1 · A separação: por contexto, não por cargo

A pergunta original era se o material devia ser um só para todos ou separado por contexto.
**Separado — e o eixo da separação é o contexto de trabalho, nunca o cargo.**

O motivo é prático. Cargo muda: o ajudante vira marceneiro, o marceneiro vai para a obra, o
montador entra na CNC. Se o volume for "Apostila do Montador", cada promoção obriga a
reimprimir e a pessoa devolve um livro que já não serve. Contexto não muda: **material é
material**, para quem corta e para quem vende.

Então o material se separa por contexto, e a **trilha de formação** — que já existe e é o
modelo da casa (`trilhas-e-avaliacao.md`) — é quem diz **quais volumes cada pessoa recebe e
em que ordem**. Promoção muda a trilha; não muda a impressão.

---

## 2 · Os seis volumes

| Vol. | Título | Blocos | Fichas | Páginas est. |
|---|---|---|---|---|
| **0** | **O Livro da Casa** | INST · LING · SEG · ORG | 19 | ~48 |
| **1** | **Materiais** | MAT · BOR · QUI | 15 | ~60 |
| **2** | **Ferragens e Fixação** | FER · FIX | 16 | ~72 |
| **3** | **Do Projeto à Peça** | PRJ · FAB | 11 | ~56 |
| **4** | **Construção e Montagem** | CON | 6 | ~48 |
| **5** | **Obra e Entrega** | OBR | 5 | ~40 |
| **F** | **Fichário de Produção** | POP · padrões que mudam | 7+ | avulso |

### Volume 0 — O Livro da Casa
**Todo mundo recebe, no primeiro dia, sem exceção.** Do ajudante à arquiteta, do
administrativo ao sócio. É a história da Valvic, o que a empresa vende e promete, quem é
quem, o fluxograma da venda à entrega, as regras da casa, a segurança e o nome de cada peça
do móvel.

É o volume que cria **vocabulário comum**. Sem ele, todos os outros são ilegíveis para quem
chegou ontem — e é a razão pela qual ele vem antes de qualquer conteúdo técnico, mesmo para
quem já é marceneiro formado.

### Volumes 1 a 5 — o ofício
Cada um é o conjunto fechado de fichas do seu contexto. Um marceneiro pleno tem os cinco na
bancada; um comercial tem o 0 e lê a folha 1 das fichas que sustentam o discurso de venda.

### Fichário F — o que muda
Ver §3. **Não é encadernado, e isso é deliberado.**

---

## 3 · O que pode e o que não pode ser encadernado

Aqui está a decisão que mais protege o projeto, e ela vem direto das três camadas da ficha
(`escopo-do-nucleo.md` §1.3):

| Camada | Suporte | Troca a cada |
|---|---|---|
| **SABER** — o ofício: o que é um caneco de 35 mm, como cola de contato funciona | **Encadernado** | anos |
| **PADRÃO VALVIC** — "corrediça oculta Hardt soft-close é o padrão Gold" | **Fichário de argolas**, folha numerada e datada | meses |
| **POP** — como se executa, com critério de aceite | **Fichário**, mesma folha | meses |
| **Guia rápido** — a tabela que se consulta com a máquina ligada | **A4/A3 plastificado** na bancada | quando muda |

**Por que isso importa mais do que parece.** A Valvic tem meta declarada de subir de Hardt
para Blum. Tem POP-01 aguardando aprovação, com revisão marcada em 30 dias. Tem preço de
ferragem que mudou em agosto. Se tudo isso for encadernado junto com o ofício, em seis meses
a fábrica está lendo instrução errada num livro bonito — e basta **uma** página errada para
a equipe parar de confiar no material inteiro. Aí o projeto morre, e não por falta de
conteúdo.

Encaderna-se o que é estável. O que muda circula em folha que se troca.

---

## 4 · O QR: como o impresso não mente

Todo problema de apostila impressa é o mesmo — a versão de papel envelhece e ninguém sabe.
A solução é barata e resolve inteiro:

**Cada ficha impressa leva, no rodapé:**

```
FICHA FER-03 · Corrediças ocultas · rev. 2 · set/2026        [QR]
Dono: Deivison · Confira a versão atual no QR
```

O QR abre a ficha viva na versão digital. Se a folha na mão estiver velha, o QR mostra a
atual — e a pessoa vê a diferença sozinha, sem depender de ninguém avisar.

**Regra de validade:** folha impressa vale **12 meses**. Passou disso, o rodapé pede a
conferência pelo QR antes de executar. Ficha de POP: **6 meses**.

---

## 5 · Uma fonte, três saídas

```
   ficha.md  (Markdown no repositório — A VERDADE)
       │
       ├──► HTML no modelo A4 da Academy  ──► PDF  ──► gráfica (volume encadernado)
       │        modelo-aula-a4.html              gerar-pdf.py
       │        modelo-pop-a4.html
       │
       ├──► folha avulsa do Fichário (mesma ficha, saída solta e datada)
       │
       └──► índice navegável em painel/  ──► a versão digital com o QR apontando pra cá
```

Correção entra **na ficha**, nunca no PDF e nunca no papel. Quem corrigir um PDF direto
quebra a fonte única, e a partir daí não há mais verdade — há duas.

---

## 6 · Especificação de impressão

Recomendação, para cotar com a gráfica:

- **Formato:** A4 retrato — é o formato dos modelos que já existem e do `gerar-pdf.py`.
- **Encadernação: wire-o (espiral duplo metálico).** Não é capricho: **abre plano na
  bancada e vira 360°.** Livro de lombada quadrada fecha sozinho quando a pessoa solta para
  pegar a peça — e aí ela para de usar. Wire-o é o que sobrevive ao chão de fábrica.
- **Capa:** 250 g, laminação fosca (aguenta mão suja e não marca digital).
- **Miolo:** 90 g offset. Papel fino amassa e transparece o desenho da folha de trás.
- **Cor:** 4/4 nos volumes com desenho técnico e foto de erro real (1, 2, 4, 5); 1/1 aceita
  no Volume 0 se o custo pesar — mas o fluxograma pede cor.
- **Fichário F:** capa dura com 4 argolas, folhas em 120 g perfuradas. Mais caro por folha,
  e vale: é a folha que sai e volta.
- **Guia de parede:** A3, plastificado, ilhós no canto.

**Tiragem:** imprimir por lote pequeno e reimprimir. Nunca estocar volume — o estoque é que
transforma revisão em desperdício, e é o que faz gerente adiar correção para "não perder as
cópias".

---

## 7 · Quem recebe o quê

`✅` recebe o volume · `f1` recebe só a folha 1 das fichas relevantes · `—` não recebe

| Cargo | V0 | V1 | V2 | V3 | V4 | V5 | Fichário |
|---|:--:|:--:|:--:|:--:|:--:|:--:|---|
| Ajudante de marcenaria | ✅ | f1 | f1 | — | ✅ | — | Fábrica |
| Marceneiro | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Fábrica |
| Montador | ✅ | f1 | ✅ | f1 | ✅ | ✅ | Obra |
| Operador de máquinas | ✅ | ✅ | f1 | ✅ | — | — | Fábrica |
| Programador CNC | ✅ | ✅ | ✅ | ✅ | ✅ | — | CNC |
| Projetos / arquitetura | ✅ | ✅ | ✅ | ✅ | f1 | f1 | — |
| Orçamentista | ✅ | ✅ | ✅ | ✅ | f1 | — | — |
| Comercial | ✅ | f1 | f1 | — | — | f1 | — |
| Assistente operacional | ✅ | f1 | — | — | — | — | Administrativo |

O **f1** é o que a arquitetura de ficha em camadas comprou: o comercial precisa saber o que
é corrediça oculta para sustentar a garantia de 10 anos na frente do cliente — e não precisa
do comprimento em milímetros. Uma ficha, dois leitores.

---

## 8 · Ordem de produção editorial

Não se imprime volume incompleto, e não se espera o volume inteiro para começar a circular:

1. **O Fichário começa na semana 1.** POP e guia de parede saem folha a folha, conforme
   ficam prontos e aprovados. É o material de retorno mais rápido e não depende de
   fechar nada.
2. **Volume 0 é o primeiro encadernado** — porque destrava a integração, que hoje é por
   osmose, e porque é pré-requisito de leitura de todos os outros.
3. **Volume 2 (Ferragens e Fixação) é o segundo** — tem 70% do texto já escrito
   (`ferragens.md`) e carrega a FIX-02, a ficha de maior retorno do núcleo.
4. Depois **1 → 3 → 4 → 5**, na ordem das ondas do `escopo-do-nucleo.md` §5.

**Regra de fechamento de volume:** só vai para a gráfica quando **todas** as suas fichas
estiverem escritas, com dono, revisadas por quem faz o serviço, e com o QR ativo. Volume com
ficha faltando vira volume que ninguém confia.

---

## 9 · O que ainda é decisão do Jonathan

- **Onde a versão digital fica hospedada** — hoje o `painel/` é HTML no repositório. Para o
  QR funcionar do celular da fábrica, precisa de endereço acessível. Opções a discutir:
  publicar o índice da Academy, ou apontar o QR para o PDF no Drive.
- **Quem valida tecnicamente cada volume** antes da gráfica. Sugestão: V0 Jonathan ·
  V1/V4 Paulo · V2 Deivison · V3 programador · V5 Samuel.
- **Se o Fichário fica com a pessoa ou fica no posto de trabalho.** Recomendo no posto: a
  folha atualizada chega a todo mundo de uma vez, e ninguém fica com versão velha na mochila.
