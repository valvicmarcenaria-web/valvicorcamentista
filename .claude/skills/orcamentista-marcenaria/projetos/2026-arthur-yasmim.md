# ARTHUR & YASMIM — três versões de porta · levantamento ABERTO

**Arquivo:** `Apresentação de Projeto de Arthur & Yasmim.pdf`, Drive da casa,
pasta `projetos`, 13/10/2026. **181 MB.**

## O arquivo

O PDF do Drive tem **181 MB**, é apresentação em imagem sem camada de texto,
e não abre por aqui: o download direto cai em **403 da política de saída** da
sessão e o conector do Drive devolve conteúdo vazio. ⭐ **As páginas do
CLOSET chegaram pelo chat em 13/10** — é com elas que este levantamento foi
feito. O resto do caderno ainda falta.

## O pedido da cliente, lido

> "Vou querer orçar de três formas. Se não me engano são **17 portas**.
> · 5 portas no reflecta bronze, 11 portas no fendi e a porta da sapateira
>   seria uma porta inteiriça de espelho
> · Todas as portas no reflecta bronze como no projeto e a porta da
>   sapateira com espelho
> · Todas as portas no Fendi e a porta da sapateira no espelho
> · A parte de dentro das portas que serão no Fendi podem ser brancas por
>   dentro"

**A conta dela fecha:** 5 + 11 + 1 = 17. E as três versões mantêm a
**sapateira em espelho inteiriço**. O que varia são só as outras **16**.

| versão | reflecta bronze | Fendi | espelho |
|---|--:|--:|--:|
| **1 · mista** | 5 | 11 | 1 |
| **2 · como o projeto** | 16 | — | 1 |
| **3 · toda Fendi** | — | 16 | 1 |

### ⭐ As três versões são uma reta, não três orçamentos

V3 é o piso, V2 é o teto e **V1 cai a 5/16 do caminho** entre as duas. Basta
um número — **quanto uma porta de reflecta bronze custa a mais que uma de
Fendi** — e as três saem sozinhas:

```
V3 = base
V1 = V3 +  5 × Δ
V2 = V3 + 16 × Δ
```

Isso muda o jeito de orçar: preciso de **um** conjunto completo de móveis e
**um** delta por porta, não de três levantamentos.

E muda o jeito de apresentar. Em vez de três preços soltos, a proposta pode
dizer **o que cada porta de bronze custa** — e aí a cliente escolhe quantas
quer, inclusive um número que não está nas três opções dela.

---

---

## ⭐ Os parâmetros [Jonathan 13/10]

> "considere a versão principal com corrediças ocultas da Hettich e um
> downgrade para telescópica · sem RT e MC de 37%"

* **versão principal** — corrediça **oculta Hettich**
* **downgrade** — **telescópica**, e **só isso muda**: mesma chapa, mesmo
  vidro, mesma garantia
* **sem RT** — a cliente está falando direto com a casa, não há arquiteto
  na conversa
* **MC 37%** — acima do piso de 35%, base da casa **85,35%**
* **iluminação em linha separada** [Jonathan 13/10]

### ⭐ Seis preços que são um preço e dois deltas

Os dois eixos são independentes e cada um é uma reta:

```
porta    V3 (toda Fendi) → V1 (+5 bronze) → V2 (+16 bronze)
corrediça   telescópica  → oculta Hettich
```

Logo: **um levantamento completo, um Δ por porta de bronze e um Δ por
corrediça**. Seis números saem de três contas, e a proposta cabe numa
tabela só.

---

## O CLOSET, pelo que as páginas mostram

Walk-in de **410 cm** de largura, marcenaria de **260 cm** de altura
(piso ao teto). **Dez módulos numerados** em volta: 1 a 5 na parede do
fundo, 6 e 7 na lateral direita, 8 e 9 embaixo, 10 no canto inferior
esquerdo. Outras cotas soltas nas pranchas: 166 · 105 · 87 na planta;
200 · 185 · 98 · 79 · 102 · 85 · 60 · 21 na elevação. ⚠ São cotas de
apresentação, não de executivo — não fecham um corte.

**O que se vê:**
* **portas de vidro em perfil de alumínio escuro**, com puxador vertical
  embutido no perfil — é o "reflecta bronze" do projeto
* ⭐ **as gavetas ficam ATRÁS do vidro**, visíveis de fora
* **módulo 3 é a penteadeira**: painel ripado escuro, espelho com LED
  perimetral, tampo e dois blocos de gavetas. **Sem porta**
* **LED em quase toda prateleira**, no espelho e na sapateira
* **a sapateira fica FORA do closet**, no corredor ao lado da porta:
  prateleiras **inclinadas**, todas iluminadas, com porta-botas em cima e
  uma coluna lateral estreita de prateleiras menores. **Hoje é aberta** —
  é nela que entra a porta inteiriça de espelho
* módulo de bolsas com **duas folhas de vidro** e prateleiras iluminadas

### ⭐ A conta das 17 portas fecha no closet

Dos dez módulos, a penteadeira não tem porta e a sapateira ganha a porta
de espelho. Sobram **oito módulos de duas folhas = 16 folhas de vidro**,
mais **1 espelho inteiriço = 17**. É exatamente o número da cliente — ou
seja, **as três versões são todas do closet**.

⚠ Mas ela diz "5 portas no reflecta bronze": 5 é ímpar e os módulos são de
duas folhas. Ou algum módulo tem folha única, ou ela está contando por
módulo em algum ponto. **A conferir com ela antes de orçar.**

---

## As cotas que chegaram  [13/10, segunda leva]

| | |
|---|---|
| closet | **410** de vão livre entre as duas fileiras · **260** de altura |
| penteadeira | **105** de largura, módulo 3, sem porta |
| módulo tipo | **105** de largura com **duas folhas** → folha de **52,5** |
| sapateira | **110** + coluna lateral de **23**, prateleiras **inclinadas**, porta-botas de **42** no alto, vãos de **24** e **30** |
| espelho | **112 × 250** |
| fileira direita | **166** de comprimento |
| outras | 200 · 185 · 98 · 79 · 102 · 85 · 60 · 21 · 87 na elevação e na planta |

⭐ A sapateira fica **fora do closet**, no corredor, ao lado da porta — e o
espelho de 112 × 250 está desenhado **ao lado dela**, não na frente.

---

## ⭐ O Δ que responde a pergunta da cliente — `corte-arthur-yasmim.py`

As três versões diferem **só nas folhas**. Então o Δ por folha responde a
pergunta sem depender da modulação, que ainda falta.

**As 16 folhas**, de 0,53 × 2,50 cada:

| | reflecta bronze | MDF Fendi |
|---|--:|--:|
| vidro / chapa | 5.880 | 3.600 |
| perfil de alumínio / fita | **10.648** | 532 |
| dobradiça | 3.040 | 1.120 |
| **custo direto** | **19.959** | **5.610** |
| **preço** | **41.281** | **11.604** |

⛔⛔ **O perfil de alumínio é a maior linha das duas colunas** — R$ 10.648,
mais que o próprio vidro. São **96,8 m de perfil** para fechar **21 m² de
vão**: folha estreita e alta é o pior caso, muito perímetro por m².

**Cada folha de bronze custa R$ 1.855 de preço a mais que uma de Fendi:**

| | folhas de bronze | a mais que a V3 |
|---|--:|--:|
| V3 · todas em Fendi | 0 | — |
| V1 · 5 bronze + 11 Fendi | 5 | **9.274** |
| V2 · todas em bronze, como o projeto | 16 | **29.677** |

⛔ Entre a V2 e a V3 há **R$ 29.677**, só nas portas. A escolha da cliente
não é de cor — é de dezenas de milhares.

### ⭐ A porta é COMPRADA PRONTA  [Jonathan 13/10]

> "nós adquirimos a porta pronta · me dê a relação das portas com as
> especificações para que eu faça a cotação com o fornecedor"

O motor foi invertido: a porta de vidro deixou de ser vidro + perfil +
dobradiça somados aqui e virou **item comprado, folha a folha**. Só a porta
em MDF Fendi continua sendo de fabricação nossa.

**A relação para cotar está pronta** em `relacao-portas-arthur-yasmim.md`
e `relacao-portas-arthur-yasmim.pdf` — folhas, medidas, especificação e as
nove perguntas para o fornecedor.

### O custo de cada porta, uma a uma

Folha de 0,53 × 2,50 — 1,31 m² de vão e **6,05 m de perímetro**.

| | fumê ⚠ | Fendi |
|---|--:|--:|
| porta pronta ⭐ · chapa de 18 | **1.300** | 225 |
| fita de borda | — | 33 |
| 4 dobradiças ★ | 280 | 140 |
| fixação e regulagem ★ · consumíveis | 60 | 24 |
| **custo direto por porta** | **1.673** | **422** |
| **preço por porta** · MC 37%, sem RT | **3.460** | **873** |

⭐ **[Jonathan 14/10] A cotação chegou:** porta fumê **R$ 1.300** e porta de
espelho **R$ 900** a folha, valores unitários, **sem dobradiça**. A
dobradiça virou compra nossa — ★ R$ 70, **quatro por folha** a 2,50 de
altura (⚠ alguns fabricantes pedem cinco), e tem de ser a que o **perfil**
aceita: ela fixa no alumínio, não se encaixota no vidro.

⚠⚠ **A cotação voltou como "fumê" e o projeto pede "reflecta bronze".** Não
é a mesma coisa: fumê é vidro **tingido na massa**, translúcido; reflecta é
vidro com **camada refletiva**, que espelha e custa mais. O render da
arquiteta mostra as portas **refletindo o ambiente** — é reflecta. ⛔ Ou o
fornecedor trocou o produto, ou a palavra foi nossa. **Confirmar antes de
fechar**: se for reflecta, o preço da folha sobe e todo o quadro anda.

⚠ **A porta de Fendi tem 2,50 de altura em 18 mm.** Folha alta e estreita
em melamínico empena com o tempo. A de vidro não tem esse problema — o
perfil de alumínio é o que a mantém reta. Na versão toda em Fendi isso
precisa ser dito à cliente.

### Os três cenários, com a cotação real

| | folhas de vidro | a mais que a V3 |
|---|--:|--:|
| V3 · todas em Fendi | 0 | — |
| V1 · 5 fumê + 11 Fendi | 5 | **12.934** |
| V2 · todas em fumê, como o projeto | 16 | **41.390** |

### O espelho da sapateira · igual nas três

⭐ [Jonathan 13/10] **o vão de 1,12 leva DUAS folhas**, de 0,56 cada.
Custo R$ 2.530, **preço R$ 5.232** — duas folhas prontas R$ 1.800
(R$ 900 cada ⭐) · oito dobradiças R$ 560 ★ · fixação R$ 120 ★.

⭐ **O espelho é mais barato que o fumê** — R$ 900 contra R$ 1.300 a folha.
Contraintuitivo e útil: a porta que a cliente quer na sapateira é a mais
barata das três, não a mais cara.

⭐ **Dividir resolve o peso.** Em folha única eram 2,80 m² — mais de 25 kg
só de vidro, de giro, em balanço numa folha de 2,50 de altura: descairia.
Em duas de 0,56, cada folha fica com 1,40 m² e a dobradiça trabalha dentro
do que aguenta. **De giro passa a ser viável** — não precisa ser de correr.

⚠ Dividir custa R$ 755 de custo a mais (R$ 1.561 de preço): mais metro de
perfil e mais duas dobradiças. É o preço de o móvel não descair.

⚠⚠ **Mas a cliente pediu "uma porta inteiriça de espelho".** Em duas folhas
aparece uma **junta vertical** no meio do espelho, na altura do rosto. Ela
precisa saber antes, não depois — e, se insistir em folha única, o caminho
é de correr. ⚠ A conta de portas também muda: 16 + 2 = **18 folhas**, não
as 17 que ela contou.

### Principal × downgrade · só a corrediça

Oculta Hettich R$ 190 o par ★ contra telescópica R$ 85 (base da casa),
sobre ★ 24 gavetas: **R$ 5.316 de preço**.

⭐ **As gavetas ficam atrás do vidro.** Com telescópica vê-se o trilho pela
lateral da gaveta, o dia inteiro, através da porta. Com a oculta não se vê
nada. Num closet envidraçado é esse o argumento — não o amortecimento.

### ⛔⛔ Por que ainda não há três preços

**Nem o vidro nem o perfil estão na base da casa.** Os dois são ★ estimados
(R$ 280/m² e R$ 110/m) e juntos são **83% do custo da versão bronze**.
Antes de mandar três números, precisamos de **um orçamento de vidraceiro e
um de alumínio** — sem isso as três versões são três palpites.

⭐ **A quantidade para cotar já está pronta:** 21,0 m² de reflecta bronze,
2,80 m² de espelho e 104,0 m de perfil.

## ★ O que já dá para antecipar

1. **Não é troca de cor, é troca de construção.** Reflecta bronze é
   **vidro**: vai em perfil de alumínio, com dobradiça para peso de vidro.
   Fendi é **chapa**: vai em MDF com fita de borda. São dois móveis
   diferentes na mesma caixa — por isso o Δ por porta tende a ser grande e
   as três versões ficam bem espalhadas.
2. **"Brancas por dentro" só economiza se o fornecedor tiver a chapa de
   duas faces** (Fendi de um lado, branco do outro). Se o Fendi só vier
   duas faces iguais, branco por dentro custa o mesmo — e o pedido vira
   só uma preferência estética, não desconto. ⚠ A conferir com o
   fornecedor antes de prometer.
3. **A porta da sapateira é o item de risco das três versões.** Espelho
   inteiriço é peso concentrado em dobradiça: pede reforço, dobradiça
   dimensionada e tolerância zero a empeno. Ela aparece igual nas três, o
   que é bom — não polui a comparação.
4. ⭐ **A corrediça aparece através do vidro.** As gavetas ficam atrás das
   portas de vidro. Com telescópica, vê-se o trilho pela lateral da gaveta;
   com a **oculta Hettich**, não se vê nada e a gaveta parece flutuar. Num
   closet todo envidraçado isso não é detalhe de catálogo — é o que o
   cliente olha todo dia. É o melhor argumento da versão principal.
5. ⚠ **A iluminação é metade do que o render vende.** LED em quase toda
   prateleira, no espelho da penteadeira e em toda a sapateira. Precisa
   ficar claro o que é nosso (perfil, fita, usinagem) e o que é da
   elétrica (fonte, driver, circuito).
6. ⛔ **Dezessete portas não são o orçamento.** O que está atrás delas —
   caixaria, prateleiras, gavetas, cabideiros, iluminação — costuma pesar
   mais. A cliente está pedindo três versões do que **se vê**; o preço vai
   ser decidido pelo que **não se vê**.

---

## ★ O que ainda preciso para orçar

1. ⭐ **As páginas dos módulos 1 a 10** — a prancha "Numeração" numera os
   dez, e em caderno assim vem uma página por módulo com o interno e as
   medidas. **São elas que faltam.**
2. A **largura e a profundidade** de cada módulo.
3. A **sapateira**: largura, profundidade, altura livre e quantas
   prateleiras inclinadas. É ela que recebe a porta inteiriça de espelho.
4. Se o reflecta bronze vai em **perfil de alumínio** — e qual perfil e
   qual puxador (o render mostra puxador embutido no próprio perfil).
5. **Ferragem**: dobradiça (porta de vidro pede dobradiça própria) e o
   modelo de corrediça oculta Hettich a considerar.
6. **Iluminação**: quantos metros de fita, em que prateleiras, e de quem é
   a fonte.
7. Se há **marcenaria fora do closet** no mesmo orçamento — o caderno é do
   apartamento inteiro.
