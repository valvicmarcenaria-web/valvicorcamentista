# TRÊS CENÁRIOS DE FERRAGEM — Gustavo Raposo [30/10/2026]

> *[Jonathan 30/10] "salve a planilha vamos trabalhar um novo cenario de
> orcamento. Partindo do pressuposto que esse primeiro orcamos em Blum. O
> segundo faremos em Hettich com a MC de 40% e vamos mudar o painel
> muxarabi, em vez das ripas, faremos uma peça plana usinada na CNC sem
> acabamento interno, ou seja, será o custo das chapas e de 500,00 de
> usinagem. e teremos uma terceira opção com corrediças telescopicas e as
> dobradiças mais baratas da base."*

**Planilha congelada antes de mexer:** `Gustavo Raposo · CENÁRIO 1 —
congelado em 30/10/2026`, id `1aF9D-prk4Ytqc4TUeS1NpMT1Olmume43rIs8tAysErY`.

## ⛔ DUAS PREMISSAS QUE NÃO SE SUSTENTAM, E AS DUAS SÃO DE DINHEIRO

**1 · O primeiro orçamento NÃO está em Blum — está em Hettich.** O Jonathan
cravou isso em 29/10 ("a casa inteira é Hettich, dez anos de garantia
uniformes") e em 30/10 mandou a Base mandar no preço. `base.py` traz
`CH_CORREDICA = 'Corrediça Hettich'` a R$ 150 o par e `CH_DOBRADICA =
'Dobradiça Hettich'` a R$ 50. ⭐ A linha genérica `Corrediça` da Base é que
é a BLUM, a R$ 300 — o dobro.

**2 · A Base não tem linha de telescópica, e a dobradiça já está no piso.**

| chave na Base | preço | unidade | produto, como a Base o chama | garantia |
| --- | --: | --- | --- | --- |
| Corrediça *(Blum)* | R$ 300,00 | **por gaveta** | Corrediça Blum | 30 anos |
| Corrediça Hettich | R$ 150,00 | par | Hettich Quadro V6 500 mm · oculta · 30 kg · 100 mil ciclos | 10 anos |
| **Corrediça Hardt** | **R$ 80,00** | par | **Hardt Invisível P-10 · ⭐ "o Padrão da casa"** | **5 anos** |
| Corrediça touch | R$ 500,00 | — | — | — |
| Dobradiça *(Blum)* | R$ 50,00 | un | Dobradiça Blum | 30 anos |
| Dobradiça Hettich | R$ 50,00 | un | Hettich Sensys Linha Gold | 10 anos |

**⭐⭐ A HARDT NÃO É TELESCÓPICA — É INVISÍVEL** [30/10/2026, perguntado pelo
Jonathan]. `base.py` não descreve a linha: ela vem importada da Base de
Custos e o código só pegou o preço. Lida na Base, ela é a **Hardt Invisível
P-10**, e a Base a chama de *"o Padrão da casa"*. ⭐ Então **os três cenários
são de corrediça OCULTA** — o cliente não vê trilho em nenhum deles. O que
muda é marca, carga, ciclos e garantia, não se o trilho aparece. ⛔ E a
telescópica, que seria o degrau de 2 anos, **não existe nesta Base**: pedi-la
é linha nova e cotação nova, para um produto PIOR que a Hardt.

**⚠ A HARDT NÃO TEM CARGA NEM CICLOS DECLARADOS.** A Hettich diz "30 kg ·
100 mil ciclos"; a P-10 não diz nada. ⛔ E este projeto tem gavetão — tanto
que a "Corrediça de carga" já está lançada a ZERO em 3 pares, na Suíte 01 e
na Suíte 02. Pôr R$ 80 debaixo de um gavetão que já pedia corrediça de carga
é o ponto técnico a cobrir antes de oferecer o cenário 3.

**⚠ A unidade da Blum é "por gaveta", não "par"** — a Base fala duas línguas
na mesma coluna. Dá no mesmo, porque uma gaveta leva um par, e os 87 × R$ 300
seguem corretos. Mas é armadilha esperando quem ler rápido.

⛔ **As duas dobradiças custam o mesmo R$ 50.** "A dobradiça mais barata da
Base" é a que já está lançada: o cenário 3 não economiza um centavo em
dobradiça. ⭐ E como o preço é igual, o cenário 3 deve especificar a
**Hettich** — não há razão para descer de linha de graça.

⛔ **E não existe telescópica na Base.** `base.py` é explícito: *"Nenhuma
telescópica comum entra: onde a prancha pede telescópica, SOBE para Hettich
oculta."* Montei o cenário 3 com a **Hardt a R$ 80**, que é a corrediça mais
barata que a Base tem de verdade — **oculta**, e com **5 anos** de garantia
em vez dos 2 da telescópica. ⭐ O senhor pediu pior e a Base só tem melhor.

## O que move entre os cenários, e só isso

Varrido da planilha gravada, não do meu modelo dela:

- **87 pares de corrediça** no projeto · **zero corrediça touch**
- **97 dobradiças** — que não movem, porque Blum e Hettich custam igual
- O **Office**, que troca o muxarabi inteiro nos cenários 2 e 3

⭐ **A ferragem só arrasta a EMBALAGEM.** Os consumíveis são 6% sobre
chapa + fita + filetagem, onde ferragem não entra; a embalagem é 2% sobre um
subtotal que inclui a ferragem. Então o delta de cada ambiente é
`pares × Δpreço × 1,02`, e o 1,02 foi conferido contra a Varanda: embalagem
de R$ 207,23 sobre um subtotal de R$ 10.361,67. Exato.

## O Office com o painel plano

O muxarabi de hoje são **170 réguas** de 5 cm entalhadas em meia-madeira:
6 chapas, 474,8 m de fita, 431,6 m de filetagem MANUAL e 7.144 encaixes que
saem ZERO. Custo direto **R$ 9.328,00**.

O painel plano, pelo custo que o Jonathan definiu (chapa + R$ 500):

| | |
| --- | --: |
| 3 chapas NC18 · 12,0324 m² de painel cheio | 2.100,00 |
| Usinagem CNC | 500,00 |
| Perfil de proteção de piso · 4,44 m | 66,60 |
| Corte por chapa | 6,00 |
| Consumíveis · 6% | 126,00 |
| Embalagem · 2% | 55,97 |
| Frete · 2 viagens | 400,00 |
| **CUSTO DIRETO** | **3.254,57** |

**Delta: −R$ 6.073,43.** Somem a fita, a filetagem manual, o corte por peça
de 170 peças e três chapas.

⚠ **E o painel plano tem emenda à vista.** 444 × 271 não cabe em chapa de
275 × 185 de jeito nenhum. Em 3 chapas são **6 peças e 5 juntas**; em 4
chapas são 4 peças e 3 juntas. ⛔ Na grade de réguas a emenda caía DENTRO de
um encaixe e não aparecia — num painel plano ela aparece. A conta acima usa
3 chapas, que é o que a fórmula da planilha devolve.

## OS TRÊS CENÁRIOS

`preço = custo ÷ (BASE − MC)`, BASE = 84,875% (encargos de 15,125%) — a
mesma fórmula da aba Preço e Comissões, não uma paralela.

| | **1 · BLUM** | **2 · HETTICH** | **3 · HARDT** |
| --- | --: | --: | --: |
| Corrediça | R$ 300/par | R$ 150/par | R$ 80/par |
| Dobradiça | R$ 50 | R$ 50 | R$ 50 |
| Muxarabi | 170 réguas | painel CNC | painel CNC |
| **Garantia** | **30 anos** | **10 anos** | **5 anos** |
| Linhas a zero na Base | 16 | 15 | 15 |
| **CUSTO DIRETO** | **175.119,24** | **155.734,81** | **149.523,01** |
| MC aplicada | 45% | 40% | 40% |
| **PREÇO** | **439.170,51** | **347.041,36** | **333.198,91** |
| Margem em R$ | 197.626,73 | 138.816,55 | 133.279,57 |

### ⭐ Quase metade do desconto do 1 para o 2 é margem, não custo

A mesma tabela com os três na MESMA MC separa as duas coisas:

| MC | 1 · Blum | 2 · Hettich | 3 · Hardt |
| --- | --: | --: | --: |
| a 45% | 439.170,51 | 390.557,52 | 374.979,34 |
| a 40% | 390.237,86 | 347.041,36 | 333.198,91 |

Do 1 para o 2 o preço cai **R$ 92.129,15**, e ele se parte em dois:
**R$ 48.613 de ferragem e muxarabi** · **R$ 43.516 de MC**, que é margem
abrindo mão. ⛔ São 47% do desconto saindo do lucro, não do custo.

## Custo direto, ambiente por ambiente

`*` = o ambiente muda entre os cenários.

| | pares | 1 · Blum | 2 · Hettich | 3 · Hardt |
| --- | --: | --: | --: | --: |
| \* 01 Varanda | 8 | 11.792,90 | 10.568,90 | 9.997,70 |
| 02 Lavabo | 0 | 1.082,32 | 1.082,32 | 1.082,32 |
| \* 03 Cozinha | 7 | 25.690,43 | 24.619,43 | 24.119,63 |
| 04 Despensa | 0 | 3.939,78 | 3.939,78 | 3.939,78 |
| \* 05 Lavanderia | 5 | 8.152,44 | 7.387,44 | 7.030,44 |
| 06 Rouparia | 0 | 5.619,80 | 5.619,80 | 5.619,80 |
| \* 07 Office | 0 | 9.328,00 | 3.254,57 | 3.254,57 |
| \* 08 Suíte Master | 4 | 11.318,53 | 10.706,53 | 10.420,93 |
| \* 09 Closet Master | 12 | 13.487,11 | 11.651,11 | 10.794,31 |
| \* 10 Banho Master | 2 | 5.933,02 | 5.627,02 | 5.484,22 |
| \* 11 Suíte 01 Filhos | 13 | 22.872,37 | 20.883,37 | 19.955,17 |
| \* 12 Banho Suíte 01 | 2 | 2.673,60 | 2.367,60 | 2.224,80 |
| \* 13 Suíte 02 Filhas | 14 | 19.676,94 | 17.534,94 | 16.535,34 |
| \* 14 Closet Suíte 02 | 4 | 8.860,74 | 8.248,74 | 7.963,14 |
| \* 15 Banho Suíte 02 | 2 | 2.680,36 | 2.374,36 | 2.231,56 |
| \* 16 Suíte Hóspedes | 8 | 8.713,49 | 7.489,49 | 6.918,29 |
| 17 Banho Hóspedes | 0 | 1.571,69 | 1.571,69 | 1.571,69 |
| 18 Banho Social | 0 | 1.603,93 | 1.603,93 | 1.603,93 |
| \* 19 Homeschooling | 6 | 10.121,79 | 9.203,79 | 8.775,39 |
| **TOTAL** | **87** | **175.119,24** | **155.734,81** | **149.523,01** |

## ⚠ O que a tabela não mostra e o leitor precisa saber

**⛔ O cenário 1 é o único que ainda carrega os 7.144 encaixes a ZERO.** Os
cenários 2 e 3 trocaram o muxarabi por um painel com usinagem precificada,
então o maior buraco do projeto se fecha neles. ⭐ Isso significa que **o
R$ 175.119,24 do cenário 1 está subestimado** e a comparação favorece ele.

**⛔ A usinagem CNC de R$ 500 não está na Base.** Entrou como valor declarado
pelo Jonathan. Enquanto não virar linha, o próximo projeto repete o buraco.

**⚠ A "Corrediça de carga" segue a zero (3 pares, Suíte 01 e Suíte 02).** No
cenário 3, com corrediça mais fraca, o gavetão precisa dela ainda mais.

**⚠ A MC do cenário 1 e do 3 é suposição minha.** O Jonathan só cravou os
40% do cenário 2. Pus o 1 nos 45% em que a planilha está hoje e o 3 nos
mesmos 40% do 2.

**⚠ As quinze linhas a zero continuam nos três.** Nenhum destes preços é
fechado enquanto elas existirem.
