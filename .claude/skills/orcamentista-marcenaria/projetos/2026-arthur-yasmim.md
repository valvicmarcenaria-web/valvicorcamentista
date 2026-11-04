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

---

## ⭐⭐ Os cenários · valor de venda das portas  [Jonathan 14/10]

> "considere uma MC de 25% para as portas, senão o preço vai ficar inviável
> para o cliente"

Faz sentido além do preço: **a porta pronta é revenda.** Chega montada do
fornecedor e nós só penduramos. Margem segue trabalho agregado, e aqui ele
é pouco. O resto do closet segue a 37%.

| unitário | custo | **venda** |
|---|--:|--:|
| porta fumê | 1.436 | **2.380** |
| porta de espelho · sapateira | 1.028 | **1.700** |
| porta em MDF Fendi | 328 | **540** |

| cenário | fumê | Fendi | espelho | **VENDA** | custo | MC R$ |
|---|--:|--:|--:|--:|--:|--:|
| **1 · mista** | 5 | 11 | 2 | **21.240** | 12.847 | 5.281 |
| **2 · como o projeto** | 16 | — | 2 | **41.480** | 25.035 | 10.368 |
| **3 · toda em Fendi** | — | 16 | 2 | **12.040** | 7.308 | 2.969 |

A V2 custa **R$ 29.440** a mais que a V3. A V1, **R$ 9.200**.

⚠ São os valores **das portas**, não do closet — o resto depende da
modulação, que ainda falta.

### O que a MC de 25% fez com o preço

| | a 37% seria | a 25% é | diferença |
|---|--:|--:|--:|
| 1 · mista | 26.590 | **21.240** | −5.350 |
| 2 · como o projeto | 51.780 | **41.480** | −10.300 |
| 3 · toda em Fendi | 15.140 | **12.040** | −3.100 |

Na V2 a casa abre **R$ 8.791 de margem** — de R$ 19.159 para R$ 10.368.
Não é desconto, é decisão de preço: a porta chega montada e a margem de
revenda não é a de fabricação.

### ⛔⛔ Mas isso puxa a MC do projeto para baixo do piso

Com porta a 25% e o resto a 37%, para a MC cheia voltar aos **35%** da casa
o **resto do closet precisa valer 5× as portas**:

| | portas | resto precisa valer |
|---|--:|--:|
| 1 · mista | 21.240 | ≥ 106.200 |
| 2 · como o projeto | 41.480 | **≥ 207.400** |
| 3 · toda em Fendi | 12.040 | ≥ 60.200 |

⛔ Na V2 isso é improvável. **A versão que o projeto desenhou é a que mais
dilui a nossa margem** — e é bom saber antes de a cliente escolher.

⚠ Apliquei os 25% a **todas** as portas, como pedido. Se a intenção era só
as **compradas**, a de Fendi volta a R$ 870 e a V3 sobe para R$ 18.120 —
diga e eu troco uma linha.

---

## ⭐⭐ Como não superfaturar a porta  [Jonathan 14/10]

> "dessa forma o orçamento está ficando superfaturado. Como seria um outro
> cenário onde o custo do item não seja repassado ao cliente com tanto
> aumento de margens?"

Custo R$ 1.673, venda R$ 2.770 — **1,66× o custo**. É muito, e **o motivo
não é a margem: é a cascata.** A porta está pagando desgaste de serra,
manutenção de máquina, programação e fabricação. Ela não encosta na serra:
chega montada.

| encargo | | a porta usa? |
|---|--:|---|
| nota fiscal | 5,00% | sim, é faturada |
| margem de erro | 2,00% | sim, quebra acontece |
| desgaste de serra | 0,50% | ⛔ não passa na serra |
| manutenção de máquinas | 0,50% | ⛔ não usa máquina |
| produção · coordenação | 0,95% | sim, alguém compra e confere |
| produção · programação | 0,95% | ⛔ não há o que programar |
| produção · fabricação | 2,38% | ⛔ não fabricamos |
| produção · montagem | 2,38% | sim, nós penduramos |

⭐ **base da casa 85,35% → base de REVENDA 89,67%**

### As três políticas

| | fumê | espelho | × custo |
|---|--:|--:|--:|
| **A · hoje** — cascata cheia, MC 25% | 2.380 | 1.700 | 1,66× |
| **B · cascata de revenda**, MC 25% | 2.220 | 1.590 | 1,55× |
| **C · cascata de revenda + R$ 400/folha** | **2.050** | **1.590** | **1,43×** |

| | V1 | V2 | V3 |
|---|--:|--:|--:|
| **A · hoje** | 21.240 | 41.480 | 12.040 |
| **B · cascata de revenda** | 20.220 | 38.700 | 11.820 |
| **C · R$ 400 por folha** | **19.370** | **35.980** | **11.820** |
| MC da casa na V2 | 10.368 | 9.669 | 7.200 |

### ⭐⭐ A C é a honesta, e não só por ser mais barata

**Margem em percentual sobre item comprado premia comprar caro** — se o
fornecedor sobe o preço, a nossa margem em reais sobe junto, pelo mesmo
trabalho. Em **reais por folha** isso não acontece: receber, guardar,
pendurar, alinhar e garantir uma porta custa o mesmo, valha ela R$ 900 ou
R$ 1.300.

E ela se apresenta em duas linhas. Na V2:

```
fornecimento das portas · 18 folhas   R$ 25.710
ferragem, instalação e garantia ....  R$ 10.240
                                      ─────────
                                      R$ 35.950
```

⛔ **Correção [Jonathan 14/10]:** a primeira versão desta linha dizia
R$ 32.670 e estava errada — tinha **dobradiça e mão de obra dentro**.
Fornecimento é só a folha comprada.

**A nota do fornecedor é R$ 22.600** (16 fumê a 1.300 + 2 espelho a 900).
A nossa linha de fornecimento fica R$ 25.710, **14% acima** — e isso não é
margem: é nota fiscal, margem de erro e as duas comissões que o item de
fato usa. Se a cliente ligar para o vidraceiro, acha os R$ 22.600 e a
diferença se explica em uma frase.

⭐ **[Jonathan 14/10] a nossa dobradiça custa R$ 12, não os R$ 70 que eu
estimei.** Com isso ela virou miudeza: R$ 864 de compra, 4% do valor das
portas, contra os R$ 5.040 do meu palpite. A separação das duas linhas
continua valendo — mas pela **clareza**, não pelo valor: "fornecimento"
tem de conter só a folha comprada.

⚠ Os R$ 400 por folha são ★ meus:

| por folha | V1 | V2 | V3 |
|---|--:|--:|--:|
| R$ 300 | 18.580 | 37.000 | 11.580 |
| **R$ 400** | **19.370** | **35.980** | **11.820** |
| R$ 500 | 20.140 | 37.960 | 12.040 |

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

## ⚠⚠ A dobradiça da base da casa pode estar triplicada

[Jonathan 14/10] **"nossa dobradiça custa 12,00, não 70,00".** Aqui ela
entrou a R$ 12. ⛔ Mas a **base da casa usa R$ 35** em `dobr`, e foi com
ela que saíram a **Isabela**, as **duas Raquéis** e o **Orlando e Ivone**.

Ou são itens diferentes — com e sem amortecedor —, ou aqueles orçamentos
estão com a linha de dobradiça **três vezes maior**. No Orlando e Ivone são
12 dobradiças: **R$ 420 lançados contra R$ 144 reais**.

**Não mexi em nada por conta própria.** Precisa da palavra do Jonathan.

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
