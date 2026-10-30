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

---

# ⚠ VERSÃO 2 — SUPERADA pela v3 no fim do arquivo [30/10/2026]

> *[Jonathan 30/10] "a linha hardt considere como telescopica: Corrediça
> telescopica: Custo da corrediça é 40,00 e dobradiça 10,00"* e, em
> seguida, *"a mc da blum sera 40% e dos demais em 35%"*

⭐⭐ **A DOBRADIÇA MOVE PELA PRIMEIRA VEZ.** Entre Blum e Hettich as duas
custam R$ 50 e o delta era ZERO — por isso Rouparia, Banho Hóspedes e Banho
Social, que não têm uma corrediça sequer, não mudavam de custo na v1. Com a
dobradiça a R$ 10 elas passam a mudar: são **97 dobradiças × R$ 40 =
R$ 3.880** de material, R$ 3.957,60 com a embalagem.

⛔ **E a MC de 35% é o PISO DA CASA.** Os cenários 2 e 3 pousam exatamente
nele. Abaixo disso não há desconto a dar sem furar a política.

## Resumo

| | **1 · BLUM** | **2 · HETTICH** | **3 · TELESCÓPICA** |
| --- | --: | --: | --: |
| Corrediça | R$ 300/par | R$ 150/par | R$ 40/par |
| Dobradiça | R$ 50 | R$ 50 | **R$ 10** |
| Muxarabi | 170 réguas | painel CNC | painel CNC |
| **Garantia** | **30 anos** | **10 anos** | **2 anos** |
| Custo direto | 175.119,24 | 155.734,81 | 142.015,81 |
| Encargos · 15,125% | 59.023,48 | 47.227,85 | 43.067,45 |
| MC aplicada | 40% | 35% | 35% |
| Margem | 156.095,14 | 109.287,59 | 99.660,22 |
| **PREÇO DE VENDA** | **390.237,86** | **312.250,25** | **284.743,48** |

## Valor de venda, ambiente por ambiente

`*` = o custo muda entre cenários

| | **1 · BLUM** | **2 · HETTICH** | **3 · TELESCÓPICA** | 1 → 3 |
| --- | --: | --: | --: | --: |
| \* 01 Varanda | 26.279,44 | 21.190,78 | 17.754,99 | −8.524,46 |
| 02 Lavabo | 2.411,86 | 2.170,07 | 2.170,07 | −241,79 |
| \* 03 Cozinha | 57.248,87 | 49.362,27 | 46.969,48 | −10.279,39 |
| 04 Despensa | 8.779,45 | 7.899,31 | 7.899,31 | −880,15 |
| \* 05 Lavanderia | 18.167,00 | 14.811,91 | 13.441,68 | −4.725,31 |
| \* 06 Rouparia | 12.523,23 | 11.267,77 | 9.631,68 | −2.891,55 |
| \* 07 Office | 20.786,63 | 6.525,46 | 6.525,46 | −14.261,17 |
| \* 08 Suíte Master | 25.222,35 | 21.466,73 | 19.912,44 | −5.309,91 |
| \* 09 Closet Master | 30.054,84 | 23.360,62 | 20.661,07 | −9.393,77 |
| \* 10 Banho Master | 13.221,21 | 11.282,25 | 10.505,10 | −2.716,11 |
| \* 11 Suíte 01 Filhos | 50.969,07 | 41.871,42 | 38.946,91 | −12.022,16 |
| \* 12 Banho Suíte 01 | 5.957,88 | 4.747,07 | 3.969,92 | −1.987,96 |
| \* 13 Suíte 02 Filhas | 43.848,33 | 35.157,77 | 32.008,30 | −11.840,03 |
| \* 14 Closet Suíte 02 | 19.745,38 | 16.538,83 | 15.638,98 | −4.106,40 |
| \* 15 Banho Suíte 02 | 5.972,95 | 4.760,62 | 3.983,48 | −1.989,47 |
| \* 16 Suíte Hóspedes | 19.417,25 | 15.016,52 | 13.216,82 | −6.200,43 |
| \* 17 Banho Hóspedes | 3.502,37 | 3.151,26 | 2.824,04 | −678,33 |
| \* 18 Banho Social | 3.574,22 | 3.215,90 | 2.888,68 | −685,54 |
| \* 19 Homeschooling | 22.555,52 | 18.453,71 | 15.795,07 | −6.760,45 |
| **PREÇO DE VENDA** | **390.237,86** | **312.250,25** | **284.743,48** | **−105.494,38** |

## Quanto da queda é custo e quanto é margem

| MC igual para os três | 1 · BLUM | 2 · HETTICH | 3 · TELESCÓPICA |
| --- | --: | --: | --: |
| a 40% | 390.237,86 | 347.041,36 | 316.469,78 |
| a 35% | 351.116,27 | 312.250,25 | 284.743,48 |

- **1 → 2:** queda de 77.987,61 = **43.196,50 de custo** + 34.791,11 de MC
- **1 → 3:** queda de 105.494,38 = **73.768,08 de custo** + 31.726,29 de MC

⭐ Ao contrário da v1, agora o CUSTO domina: na v1 quase metade do desconto
era margem abrindo mão; aqui são 70% de custo de verdade.

## ⚠ O que ainda não fecha no cenário 3

**⛔ Ele continua carregando R$ 2.750 de ferragem BLUM.** Varrido da
planilha: **7 articuladores AVENTOS HK-XS a R$ 250** (Cozinha 2, Lavanderia
5) e **10 pulsadores a R$ 100** (Suíte 02 Filhas). ⛔ Um articulador Blum de
R$ 250 ao lado de uma corrediça de R$ 40 é incoerente — e pela regra da casa
báscula e pulsador **não sobem o tier**, então ele paga caro sem comprar
garantia nenhuma. A garantia do cenário 3 segue 2 anos.

**⚠ Agora o trilho APARECE.** A v1 usava a Hardt Invisível; telescópica de
verdade é trilho lateral à vista e sem amortecedor. É a primeira vez que a
diferença entre os cenários é visível para o cliente com a gaveta aberta.

**⚠ As quinze linhas a zero continuam nos três.** Nenhum destes preços é
fechado.

---

# ⚠ VERSÃO 3 — SUPERADA pela v4 no fim do arquivo [30/10/2026]

> *[Jonathan 30/10] "vamos voltar a blum para 42% · garantias 30 anos blum
> - 10 anos hettich - 2 anos telescopica"*

⭐ As garantias já eram essas; a mudança é só a **MC da Blum, de 40% para
42%**. Os custos diretos não se movem — só o preço do cenário 1.

⭐⭐ **E 42% na Blum tem fundamento, não é capricho.** A `garantia.md` diz
que garantia tem CUSTO DE PROVISÃO e que subir o tier impacta a MC. Trinta
anos é a maior provisão da tabela da casa: é o tier que mais precisa de
margem. ⚠ Só note que a própria planilha escreve *"faixa ideal 35 a 40%"*
ao lado — 42% fica acima da faixa que ela mesma anuncia.

## Resumo

| | **1 · BLUM** | **2 · HETTICH** | **3 · TELESCÓPICA** |
| --- | --: | --: | --: |
| Corrediça | R$ 300/par | R$ 150/par | R$ 40/par |
| Dobradiça | R$ 50 | R$ 50 | R$ 10 |
| Muxarabi | 170 réguas | painel CNC | painel CNC |
| **Garantia** | **30 anos** | **10 anos** | **2 anos** |
| Custo direto | 175.119,24 | 155.734,81 | 142.015,81 |
| Encargos · 15,125% | 61.776,76 | 47.227,85 | 43.067,45 |
| MC aplicada | **42%** | **35%** | **35%** |
| Margem | 171.545,38 | 109.287,59 | 99.660,22 |
| **PREÇO DE VENDA** | **408.441,38** | **312.250,25** | **284.743,48** |

## Valor de venda, ambiente por ambiente

`*` = o custo muda entre cenários · só Lavabo e Despensa são idênticos

| | **1 · BLUM** | **2 · HETTICH** | **3 · TELESCÓPICA** | 1 → 3 |
| --- | --: | --: | --: | --: |
| \* 01 Varanda | 27.505,31 | 21.190,78 | 17.754,99 | −9.750,32 |
| 02 Lavabo | 2.524,36 | 2.170,07 | 2.170,07 | −354,30 |
| \* 03 Cozinha | 59.919,37 | 49.362,27 | 46.969,48 | −12.949,89 |
| 04 Despensa | 9.188,99 | 7.899,31 | 7.899,31 | −1.289,68 |
| \* 05 Lavanderia | 19.014,44 | 14.811,91 | 13.441,68 | −5.572,75 |
| \* 06 Rouparia | 13.107,41 | 11.267,77 | 9.631,68 | −3.475,73 |
| \* 07 Office | 21.756,27 | 6.525,46 | 6.525,46 | −15.230,81 |
| \* 08 Suíte Master | 26.398,90 | 21.466,73 | 19.912,44 | −6.486,46 |
| \* 09 Closet Master | 31.456,82 | 23.360,62 | 20.661,07 | −10.795,74 |
| \* 10 Banho Master | 13.837,95 | 11.282,25 | 10.505,10 | −3.332,84 |
| \* 11 Suíte 01 Filhos | 53.346,64 | 41.871,42 | 38.946,91 | −14.399,73 |
| \* 12 Banho Suíte 01 | 6.235,80 | 4.747,07 | 3.969,92 | −2.265,88 |
| \* 13 Suíte 02 Filhas | 45.893,74 | 35.157,77 | 32.008,30 | −13.885,44 |
| \* 14 Closet Suíte 02 | 20.666,45 | 16.538,83 | 15.638,98 | −5.027,47 |
| \* 15 Banho Suíte 02 | 6.251,57 | 4.760,62 | 3.983,48 | −2.268,09 |
| \* 16 Suíte Hóspedes | 20.323,01 | 15.016,52 | 13.216,82 | −7.106,19 |
| \* 17 Banho Hóspedes | 3.665,75 | 3.151,26 | 2.824,04 | −841,71 |
| \* 18 Banho Social | 3.740,94 | 3.215,90 | 2.888,68 | −852,26 |
| \* 19 Homeschooling | 23.607,67 | 18.453,71 | 15.795,07 | −7.812,61 |
| **PREÇO DE VENDA** | **408.441,38** | **312.250,25** | **284.743,48** | **−123.697,89** |

## Quanto da queda é custo e quanto é margem

| com os três na mesma MC | 1 · BLUM | 2 · HETTICH | 3 · TELESCÓPICA |
| --- | --: | --: | --: |
| a 42% | 408.441,38 | 363.229,88 | 331.232,21 |
| a 35% | 351.116,27 | 312.250,25 | 284.743,48 |

- **1 → 2:** queda de 96.191,13 = 45.211,49 de custo + **50.979,63 de MC**
- **1 → 3:** queda de 123.697,89 = **77.209,16 de custo** + 46.488,73 de MC

⛔⛔ **ATENÇÃO À INVERSÃO.** Na v2, com 40/35, eu disse que o custo passara a
dominar a queda. Com 42/35 o vão de MC subiu de 5 para 7 pontos e o 1 → 2
VOLTOU a ser mais margem (53%) do que custo (47%). ⭐ No 1 → 3 o custo segue
mandando, com 62%. **Dois pontos de MC na Blum movem R$ 18.203,52 de preço
e nenhum centavo de custo.**

## O que segue em aberto

- ⛔ O cenário 3 carrega **R$ 2.750 de ferragem Blum**: 7 articuladores
  AVENTOS HK-XS a R$ 250 (Cozinha 2, Lavanderia 5) e 10 pulsadores a R$ 100
  (Suíte 02). Pela regra da casa não sobem o tier — paga caro sem comprar
  garantia. A garantia do 3 segue 2 anos.
- ⚠ **No cenário 3 o trilho APARECE** na lateral da gaveta, e não há
  amortecedor. É a única diferença entre os cenários que o cliente vê com a
  gaveta aberta, e tem de estar escrita na proposta.
- ⚠ **As quinze linhas a zero continuam nos três.** Nenhum preço é fechado.

---

# ⭐ VERSÃO 4, A VALER — e com duas TROCAS de ambiente [30/10/2026]

> *[Jonathan 30/10] "vamos trabalhar com blum e hettich em 42% e
> telescopica em 35%. e vamos criar dois novos cenarios em dois ambientes
> peculiares. cozinha esta em laca, vamos apresentar o valor com ela em
> melaminico tbm · o office que tem o painel de muxarabi vamos apresentar
> outro cenario com ele em usinagem, ou seja, sera as chapas com usinagem,
> nao vai ter as peças filetadas."*

⛔⛔ **RESTRUTUREI, E É PRECISO SABER DISSO.** Nas v2 e v3 o painel plano do
Office estava EMBUTIDO nos cenários 2 e 3. Agora que ele virou troca
independente, os três cenários passam a carregar a configuração ATUAL —
**Cozinha em laca e Office em réguas** — e as duas trocas se aplicam por
cima de qualquer um deles. ⭐ A prova de que a base está certa: o cenário 2
devolve exatamente R$ 161.808,24, que é o custo direto da planilha de hoje.

## Os três cenários, na configuração atual

| | **1 · BLUM** | **2 · HETTICH** | **3 · TELESCÓPICA** |
| --- | --: | --: | --: |
| Corrediça / dobradiça | R$ 300 / R$ 50 | R$ 150 / R$ 50 | R$ 40 / R$ 10 |
| **Garantia** | **30 anos** | **10 anos** | **2 anos** |
| MC aplicada | 42% | 42% | 35% |
| Custo direto | 175.119,24 | 161.808,24 | 148.089,24 |
| **PREÇO DE VENDA** | **408.441,38** | **377.395,31** | **296.920,78** |

## ⭐⭐ 57% DA COZINHA É TINTA

A laca são **21,67 m² × R$ 650 = R$ 14.085,50** num ambiente de
R$ 24.619,43. ⭐ E ela se conta das peças, nas DUAS FACES, porque peça
lacada de um lado só empena.

| Cozinha | custo direto | economia |
| --- | --: | --: |
| em laca, como está | 24.619,43 | — |
| em melamínico Diamante/Caiena | 10.482,90 | −14.136,53 |
| em melamínico Branco TX | 9.726,06 | −14.893,37 |

⭐ A escolha do melamínico quase não muda o resultado — R$ 757 entre o mais
caro e o mais barato, contra R$ 14.085 de laca. **A tinta é que manda.**

**⛔⛔ E O MELAMÍNICO MATA A MOLDURA PROVENÇAL.** São 14 frentes. A moldura
é peça INTEIRA de 6 mm usinada na router e colada sobre a base de 15: em
laca pinta-se o conjunto e a junta some; em melamínico o rebaixo da router
**expõe o miolo cru de MDF** e não há como acabar. ⭐ Melamínico aqui não é
a mesma cozinha mais barata — é **frente lisa**, e a prancha cota os 5 cm de
moldura em cada folha. É decisão de projeto, não de orçamento.
⭐ Por isso a conta já tira as 14 molduras: 2 chapas de cru 6 viram 1 (só o
fundo do nicho, que não é moldura), somem 14 peças de corte, 1,58 m de fita
e a filetagem manual. Reconstruí o painel inteiro e **conferi contra os
R$ 24.619,43 da planilha antes de confiar nele na variante**.

## O Office em usinagem

De R$ 9.328,00 em réguas para R$ 3.254,57 em painel plano usinado — **−6.073,43**. Somem a fita (474,8 m), a
filetagem manual (431,6 m), o corte de 170 peças e três chapas. ⭐ E some o
maior buraco do projeto: os 7.144 encaixes de meia-madeira que saíam ZERO.

## As duas trocas, em PREÇO, por cenário

| | Cozinha → melamínico | Office → usinagem | as duas | PREÇO final |
| --- | --: | --: | --: | --: |
| **1 · BLUM** | −32.971,50 | −14.165,43 | −47.136,93 | **361.304,44** |
| **2 · HETTICH** | −32.971,50 | −14.165,43 | −47.136,93 | **330.258,38** |
| **3 · TELESCÓPICA** | −28.343,92 | −12.177,30 | −40.521,22 | **256.399,56** |

⭐⭐ **A LACA TIRA MAIS DO PREÇO DO QUE A FERRAGEM INTEIRA.** Trocar a
cozinha para melamínico vale **R$ 32.971,50** de preço; trocar a casa toda
de Blum para Hettich vale **R$ 31.046,07**. Um ambiente pesa mais que as 87
corrediças e as 97 dobradiças somadas.

## ⚠ Segue em aberto

- ⛔ **A moldura provençal.** Melamínico = frente lisa. Decisão de projeto.
- ⚠ **Qual melamínico**, se for. Diamante/Caiena a R$ 550 ou Branco TX a
  R$ 350 — são R$ 757 de diferença no ambiente inteiro.
- ⚠ O preço da chapa de **MDF Cru é DERIVADO**, não lido: a própria aba diz
  *"derivado da razão cru/fosco de 0,76 da Base antiga, não lido"*. É o
  mesmo defeito que a corrediça Hettich tinha. Vale ler na Base.
- ⛔ O cenário 3 ainda carrega **R$ 2.750 de ferragem Blum** (7 articuladores
  e 10 pulsadores) que não compram garantia nenhuma.
- ⚠ As quinze linhas a zero continuam. Com o Office em usinagem caem para
  catorze, e com a cozinha em melamínico caem mais três (as molduras).
