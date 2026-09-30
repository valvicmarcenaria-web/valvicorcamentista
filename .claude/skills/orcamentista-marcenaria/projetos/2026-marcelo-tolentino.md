# MARCELO TOLENTINO — BRZ Nova Lima

Nova versão do SPE Nova Lima 1, rebatizada. Projeto **Zilda Santiago e
Anamaria Diniz** (colaboradoras Clara Valadares, Sara Bicalho, Martina
Grimaldi). Cliente final **BRZ**. Duas frentes no mesmo contrato:
**Estande de Vendas Nova Lima** e **Apto Decorado Bosque Residence**.

Levantamento: `levantamento-marcelo-tolentino.md` · motor:
`corte-marcelo-tolentino.py` · pranchas: `pranchas-marcelo-tolentino/`.

---

## 29/09/2026 — levantamento e primeira precificação

> *"Preciso fazer uma nova versão do orçamento do SPE Nova Lima, vamos
> chamá-lo de Marcelo Tolentino. Faça uma sincronia entre os projetos
> originais com os novos para obter valores correlacionados. As ferragens
> serão dobradiças Hettich Novisys, corrediças telescópicas, sistema de
> roupeiro RO65 Prime da Rometal."*
> *"Não é para manter nada do projeto antigo, considere apenas os itens no
> novo projeto."*

⛔ **Escopo novo, do zero.** O SPE Nova Lima 1 entra só como **referência de
custo unitário** — nenhum item do escopo antigo foi mantido.

### Como as pranchas chegaram

O container **não alcança o Drive** (`drive.google.com` recusado pela política
de rede da organização) e o conector do Drive só devolve o **carimbo** da
prancha — o desenho inteiro está em curvas, sem camada de texto. As 11
pranchas vieram anexadas na conversa e foram lidas por **rasterização a
110 dpi**, com recorte a 260 dpi onde a cota era miúda.

**54 folhas, todas em 1/25**, formatos A2 e A1.

### O que é nosso e o que não é

A leitura separou marcenaria de terceiro em todos os ambientes. Ficam **fora**:
mármore verde Alpi, granito cinza andorinha, granito branco Siena, granito
marrom tabaco, a **alvenaria pré-executada** da bancada gourmet, a **bancada e
o sóculo existentes** da copa (aproveitados do antigo decorado), o porcelanato
do nicho do aparador da sala de reunião, louças, metais, eletrodomésticos,
forro de gesso, pintura, papel de parede, persianas e o mobiliário solto
(Doimo, Calder, Erbanizada, Torquarto).

### O número

| | m² de chapa | custo direto | venda | MC |
|---|--:|--:|--:|--:|
| Stand (5 ambientes) | 154,4 | 30.948 | **78.360** | 37,0% |
| Decorado (6 ambientes) | 173,8 | 58.069 | **154.070** | 38,8% |
| **Total** | **328,1** | **89.017** | **232.430** | **38,2%** |

94 chapas, aproveitamento médio **69%**. BASE 76,52% (à vista, com RT, sem
vendedor). MC direcionada por complexidade: **35%** painelaria de parede e
forro · **38%** armários e gabinetes · **40%** itens especiais (estante,
bancadas de ativos, divisórias, roupeiros, muxarabi).

### A sincronia com o projeto antigo

| | m² de chapa | venda | R$/m² |
|---|--:|--:|--:|
| SPE decorado (versão técnica de 21/08) | 167,5 | 115.800 | 691 |
| **Marcelo Tolentino decorado** | 173,8 | 154.070 | **887** |
| | | | **+28,3%** |

A área de chapa é quase a mesma; o preço por m² sobe 28%. **A diferença não é
margem — é terceiro.** O decorado novo carrega R$ 20 mil de terceirizados
contra bem menos no antigo: divisória de correr em vidro canelado com perfil
preto fosco (4.799), espelho colado do banheiro social (2.904), laca fosca
verde nas frentes inferiores da cozinha (2.683), os dois roupeiros de vidro
com perfil bronze (2.484 + 2.394) e os três estofados. O antigo tinha portas
de espelho e laca, mas menos vidro e menos alumínio.

O stand fica em R$ 508/m², **abaixo da faixa da casa** (626–834), e isso está
certo: 78 dos 154 m² do stand são **painel liso de parede e forro** — chapa
plana, corte simples, sem ferragem. A faixa de R$/m² foi calibrada em jobs de
armário; painelaria legitimamente fica abaixo dela. O que vale conferir é a
**MC, que está em 37,0%** — dentro da faixa ideal.

---

## Em aberto

1. ★ **RO65 Prime não está na base.** `dados/materiais.json` só tem o RO65
   comum (R$ 60/porta + trilho 3 m R$ 80). Lancei o Prime a **R$ 120/porta +
   R$ 160/trilho** (o dobro), provisório. São 4 portas e 2 trilhos — se o
   Prime for o triplo, o custo sobe ~R$ 400 e a venda ~R$ 1.000. **Cotar.**
2. ⚠ **RO65 em folha de vidro de 234 cm.** Mesma dúvida de carga que ficou
   aberta no SPE. O Prime é linha acima e provavelmente resolve, mas
   **confirmar com a Rometal** antes de assinar.
3. ⚠ **Corrediça telescópica derruba a garantia para 2 anos** (`ferragens.md`).
   Se a proposta precisar sustentar 5 anos, a corrediça tem de mudar.
4. ★ **Fecho toque**: 21 frentes da cozinha e do aparador da sala de reunião
   são "fecho toque". A base só tem o **Pulsador Blum a R$ 100/un**
   (R$ 2.100 no total). A Hettich tem equivalente — cotar.
5. ★ Adoções minhas sem referência na base: **vidro canelado e vidro bronze
   R$ 420/m²** (40% acima do incolor), **perfil de alumínio R$ 85/m**,
   **usinagem do muxarabi R$ 380/m²**, **tubo de alumínio 2×2 R$ 60/m**.
6. ⚠ **Quem fornece o LED?** As pranchas trazem legenda de LED e a nota
   *"conferir projeto elétrico e luminotécnico do fornecedor"*. Lancei
   5,6 m por nossa conta (cozinha e os dois banheiros, R$ 840 de custo).
   No SPE anterior o LED ficou por conta do cliente — **decidir**.
7. ⚠ A **bancada do gourmet é alvenaria pré-executada** com granito por cima;
   a prancha manda "ajustar de acordo com a alvenaria". O armário interno é
   nosso e depende dessa medida — **conferir no local antes do corte**.

---

## 29/09/2026 (2º ajuste) — comissão de 5%, sem RT, fechamento por ambiente

> *"Vamos deixar apenas uma comissão de venda de 5%, sem considerar RT.
> Separe os custos por ambiente e não por item."*

### O que mudou no modelo

`motor_mc.py` ganhou `_taxa()`: `rt` e `vendedor` passam a aceitar **a
alíquota**, não só ligado/desligado. `True` mantém o padrão da casa, `False`
zera, e um número fixa a taxa. Aqui: `rt=False, vendedor=0.05`.

| | encargos | BASE |
|---|--:|--:|
| antes — com RT 10%, sem vendedor | 23,48% | 76,52% |
| **agora — sem RT, comissão 5%** | **19,07%** | **80,93%** |

São **+4,42 pontos** de base livre.

### O fechamento

| Ambiente | m² de chapa | custo | venda | MC |
|---|--:|--:|--:|--:|
| Copa | 27,1 | 4.591 | 10.370 | 36,7% |
| Sala de reunião | 8,5 | 2.837 | 6.610 | 38,0% |
| Sala de ativos | 44,4 | 7.931 | 19.230 | 39,7% |
| Lounge | 26,7 | 6.119 | 13.320 | 35,0% |
| Gourmet | 47,8 | 9.470 | 20.900 | 35,6% |
| **Stand** | **154,4** | **30.948** | **70.430** | **37,0%** |
| Cozinha e área de serviço | 69,6 | 21.976 | 51.720 | 38,4% |
| Sala e varanda | 40,9 | 9.854 | 23.270 | 38,6% |
| Quarto casal | 29,7 | 11.107 | 26.620 | 39,2% |
| Quarto solteiro | 25,2 | 9.461 | 22.770 | 39,4% |
| Banheiro social | 4,8 | 3.829 | 8.920 | 38,0% |
| Banheiro casal | 3,6 | 1.842 | 4.500 | 40,0% |
| **Decorado** | **173,8** | **58.069** | **137.800** | **38,8%** |
| **TOTAL** | **328,1** | **89.017** | **208.230** | **38,2%** |

O alvo de MC continua vindo da **complexidade da peça** — é onde a diferença
é real. O que mudou é o fechamento: cada ambiente recebe **um preço só**, com
o alvo ponderado pelo custo dos seus itens. Por isso a Copa fecha em 36,7%
(mistura painel a 35% com armário a 38%) e o Banheiro casal em 40% (só o
muxarabi).

### ⚠ O que os 4,42 pontos fizeram com a margem em reais

Segurar a **MC em percentual** faz o preço cair e **a margem em reais cair
junto** — o cliente fica com 100% do que o RT liberou:

| leitura | preço | MC % | MC R$ |
|---|--:|--:|--:|
| antes (com RT) | 232.430 | 38,2% | 88.826 |
| **segurando a MC% em 38,2%** | **208.230** | **38,2%** | **79.508** |
| segurando a MC em reais | 219.740 | 40,4% | 88.824 |
| mantendo o preço de antes | 232.430 | 42,6% | 99.094 |

**São R$ 9.318 a menos de contribuição em reais pelo mesmo trabalho.** O
método da casa direciona MC em percentual, então entreguei a primeira linha.
Mas a decisão de preço é do Jonathan: tirar o RT não torna o móvel mais
barato de fazer, e se a intenção era ficar com a folga em vez de repassá-la,
a linha certa é a terceira.

⛔ Não confundir com a regra do cartão (12/09): lá o acréscimo **tem** de
segurar a MC em reais porque é repasse de taxa de terceiro. Aqui é o
contrário — é margem própria que ficou livre, e quem decide para quem ela
vai é a casa.

---

## 29/09/2026 (3º ajuste) — sem comissão, espelhos à parte, MC −5 pontos

> *"Vamos tirar a comissão de venda. Acrescentar os espelhos: coloque um
> custo separado, considere um custo de 650,00 o metro quadrado.
> Reduza 5% de MC também."*

### ⚠ Dois erros meus que os espelhos revelaram

Ir atrás dos espelhos me obrigou a abrir as **folhas 03 dos dois banheiros**,
que eu não tinha lido na primeira passada. As duas tinham correção:

| | eu tinha lido | a prancha diz |
|---|---|---|
| Espelho do banheiro social | parede inteira, **1,2 × 3,70 = 4,44 m²** | sobre a bancada, **0,85 × 1,20 = 1,02 m²** |
| Espelho do banheiro casal | **não existia na conta** | **espelho com moldura em MDF Tauari, 1,88 × 1,16 = 2,18 m²** |
| Armário do banheiro casal | 1 frente de 40 × 35 | **140 de largura, 4 portas de 35** |

O erro do social era de R$ 2,2 mil de custo a mais; o do casal, de R$ 1,4 mil
a menos. Quase se anulam no total, mas estavam os dois errados.

⛔ **A regra de 07/09 pegou de novo pelo avesso: eu parei de ler antes do fim.**
Quatro folhas ficaram fechadas (as "03" dos banheiros e as de imagens) porque
achei que banheiro é sempre gabinete e prateleira. Prancha que não foi aberta
não é prancha lida.

### Espelho vira linha própria

`ESP` entra ao lado de `FER` e `TER`, a **R$ 650/m²**. Não passa pelo rateio
de consumível e logística — é compra direta, como a ferragem.

| | m² | R$ |
|---|--:|--:|
| Banheiro social · espelho prata colado | 1,02 | 663 |
| Banheiro casal · espelho com moldura | 2,18 | 1.418 |
| **Total** | **3,20** | **2.081** |

### O modelo agora

`RT_ON, COMISSAO = False, False` → **BASE 85,35%**.

| | encargos | BASE |
|---|--:|--:|
| com RT 10% e vendedor 10% | 32,32% | 67,68% |
| sem RT, comissão 5% (rodada anterior) | 19,07% | 80,93% |
| **sem RT, sem comissão** | **14,65%** | **85,35%** |

### O corte de MC

Li *"reduza 5% de MC"* como **5 pontos percentuais**: os alvos por
complexidade saem de 35 / 38 / 40 para **30 / 33 / 35**.

| Ambiente | m² de chapa | custo | venda | MC |
|---|--:|--:|--:|--:|
| Copa | 27,1 | 4.623 | 8.610 | 31,7% |
| Sala de reunião | 8,5 | 2.830 | 5.410 | 33,0% |
| Sala de ativos | 44,4 | 7.862 | 15.520 | 34,7% |
| Lounge | 26,7 | 6.132 | 11.080 | 30,0% |
| Gourmet | 47,8 | 9.635 | 17.600 | 30,6% |
| **Stand** | **154,4** | **31.081** | **58.220** | **32,0%** |
| Cozinha e área de serviço | 69,6 | 22.036 | 42.450 | 33,4% |
| Sala e varanda | 40,9 | 9.994 | 19.300 | 33,6% |
| Quarto casal | 29,7 | 11.122 | 21.750 | 34,2% |
| Quarto solteiro | 25,2 | 9.497 | 18.630 | 34,4% |
| Banheiro social | 3,2 | 1.554 | 2.970 | 33,0% |
| Banheiro casal | 6,9 | 3.906 | 7.760 | 35,0% |
| **Decorado** | **175,5** | **58.108** | **112.860** | **33,9%** |
| **TOTAL** | **329,8** | **89.189** | **171.080** | **33,2%** |

### ⚠⚠ A MC de 33,2% está ABAIXO do piso da casa

`modelo-de-custo.md` crava piso em **35%**, faixa ideal 35–40%. Este
fechamento fica **1,8 ponto abaixo do piso**, e o Lounge (30,0%) e o Gourmet
(30,6%) ficam **5 pontos abaixo**.

| leitura | preço | MC | MC R$ |
|---|--:|--:|--:|
| **−5 pontos: 30 / 33 / 35** ← entregue | **171.080** | **33,2%** | **56.776** |
| −5% relativo: 33,3 / 36,1 / 38 | 181.830 | 36,3% | 66.003 |
| no piso da casa, MC 35% | 177.140 | 35,0% | 62.000 |
| sem corte (rodada anterior) | 189.160 | 38,2% | 72.259 |

Somando as três rodadas: o preço saiu de **R$ 232.430** para **R$ 171.080**,
−26%, com o **mesmo custo direto**. Dos R$ 61 mil, R$ 43 mil vieram de tirar
RT e comissão (encargo que a casa deixou de pagar) e **R$ 18 mil vieram da
margem**. É decisão de preço do Jonathan, registrada — não é consequência
técnica.

---

## 30/09/2026 — dois cenários de investimento

> *"Cenário 1 — linha standard: ferragens que já consideramos nessa proposta
> (aqui vamos reduzir MC em mais 3 pontos). Cenário 2 — linha gold: ferragens
> Hettich, MC de 8% acima da standard. Mantenha os valores dos espelhos
> separados."*

### Como o motor passou a rodar dois cenários

A ferragem deixou de ser lançada em **reais** e passou a ser lançada em
**quantidade**. `DOBR`, `CORR`, `TIPON`, `RO65P_PORTA`, `RO65P_TRILHO` e
`SUP_PRAT` viraram objetos `Q`, um dicionário com `__mul__` e `__add__` —
então `8*CORR + 4*DOBR` continua escrito igual nos itens, mas agora devolve
`{'corr':8, 'dobr':4}`. O preço entra depois, por cenário. **Nenhuma das 20
chamadas `f()` precisou ser reescrita.**

⛔ A guarda de 09/09 continua valendo e está no código:

```python
for mov in MOVS:
    if not FER[mov]:
        assert abs(CDI['standard'][mov] - CDI['gold'][mov]) < 0.01, mov
```

Chapa, fita, consumível, logística, terceirizados e **espelho** são idênticos
nos dois cenários. Só a ferragem muda — e a embalagem, que é 2% dela.

### As duas linhas

| | ferragem | garantia | alvos de MC |
|---|---|--:|--:|
| **Standard** | Hettich Novisys · corrediça telescópica · RO65 Prime | **2 anos** | 27 · 30 · 32 |
| **Gold** | Hettich Sensys · corrediça oculta Quadro · RO65 Prime | **10 anos** | 35 · 38 · 40 |

Li *"8% acima"* como **8 pontos**, coerente com o *"3 pontos"* que o Jonathan
escreveu na mesma frase. Some-se: a Gold devolve exatamente os alvos
35 / 38 / 40 com que este orçamento começou.

### O fechamento

| Ambiente | m² | custo std | **venda std** | MC | custo gold | **venda gold** | MC |
|---|--:|--:|--:|--:|--:|--:|--:|
| Copa | 27,1 | 4.623 | **8.150** | 28,6% | 5.480 | **11.290** | 36,8% |
| Sala de reunião | 8,5 | 2.830 | **5.110** | 30,0% | 3.085 | **6.510** | 38,0% |
| Sala de ativos | 44,4 | 7.862 | **14.650** | 31,7% | 8.066 | **17.640** | 39,6% |
| Lounge | 26,7 | 6.132 | **10.510** | 27,0% | 6.234 | **12.380** | 35,0% |
| Gourmet | 47,8 | 9.635 | **16.690** | 27,6% | 9.941 | **20.020** | 35,7% |
| **Stand** | **154,4** | **31.081** | **55.110** | **29,0%** | **32.805** | **67.840** | **37,0%** |
| Cozinha | 69,6 | 22.036 | **40.130** | 30,4% | 23.413 | **49.890** | 38,4% |
| Sala e varanda | 40,8 | 9.994 | **18.250** | 30,6% | 9.994 | **21.370** | 38,6% |
| Quarto casal | 29,7 | 11.122 | **20.540** | 31,2% | 11.745 | **25.460** | 39,2% |
| Quarto solteiro | 25,2 | 9.497 | **17.590** | 31,4% | 10.150 | **22.100** | 39,4% |
| Banheiro social | 3,2 | 1.554 | **2.810** | 30,1% | 1.656 | **3.500** | 38,0% |
| Banheiro casal | 6,9 | 3.906 | **7.320** | 32,0% | 4.110 | **9.060** | 40,0% |
| **Decorado** | **175,4** | **58.108** | **106.640** | **30,9%** | **61.066** | **131.380** | **38,9%** |
| **TOTAL** | **329,8** | **89.189** | **161.750** | **30,2%** | **93.871** | **199.220** | **38,2%** |

**Espelhos, linha à parte e igual nos dois:** banheiro social R$ 663 ·
banheiro casal R$ 1.418 · **total R$ 2.081**.

### A escada bate com o que a casa já sabia

| | |
|---|--:|
| Gold − Standard, no preço | **R$ 37.470** (+23,2%) |
| Gold − Standard, em ferragem de verdade | **R$ 4.590** |
| Quanto da diferença é margem | **87,7%** |

`ferragens.md` já registrava isso: *"84% da diferença entre o cenário mais
barato e o mais caro é margem e só 13% é ferragem a mais."* Aqui deu 87,7% e
12,3%. O que sustenta a escada comercialmente não é a peça — é a **garantia,
que dobra de 2 para 10 anos**.

### ⚠⚠ A Standard está 4,8 pontos abaixo do piso da casa

| rodada | preço | MC |
|---|--:|--:|
| 29/09 · com RT e comissão | 232.430 | 38,2% |
| 29/09 · sem RT, comissão 5% | 208.230 | 38,2% |
| 29/09 · sem comissão, −5 pontos | 171.080 | 33,2% |
| **30/09 · standard, −3 pontos a mais** | **161.750** | **30,2%** |
| **30/09 · gold, +8 pontos** | **199.220** | **38,2%** |

O piso da casa é **35%**. A Standard fecha em 30,2%, e dentro dela o **Lounge
(27,0%)**, o **Gourmet (27,6%)** e a **Copa (28,6%)** ficam perto de 7 pontos
abaixo. A Gold volta exatamente ao 38,2% de onde o orçamento partiu.

Não é problema técnico — é a escada funcionando: a Standard é a linha de
entrada e a Gold é a que paga a casa. Mas **se o cliente fechar a Standard, o
contrato inteiro roda abaixo do piso**, e isso precisa ser decisão consciente,
não consequência da escada.

---

## 30/09/2026 (2º) — Dominus na gold, LED nosso, espessura por cenário

> *"1 - ok. 2 - mude o sistema para o Dominus. LED é fornecimento nosso.
> Outra coisa que vale apontar na proposta é a espessura das chapas: na
> standard estrutura, porta e prateleiras de 15; na gold as portas e
> prateleiras passam para 18 mm."*

### O que mudou

**Roupeiro.** `ROUPEIRO_2P` virou item único de ferragem, precificado por
cenário: standard **RO65 Prime** (★ provisório, R$ 400 o conjunto de duas
portas com trilho) · gold **Dominus Rometal** (R$ 700 + trilho de 2 m R$ 300
= R$ 1.000). São dois roupeiros, então a gold paga R$ 1.200 a mais aqui.

**LED entra no nosso escopo.** Fui atrás das marcas de LED nas elevações e
achei uma que tinha passado: **a estante da sala leva LED sob os nichos em
Carvalho Munique** — as setas aparecem na E01 e na E04. Lancei 4,5 m.
Conferi o quarto casal e o solteiro: **não têm nenhuma marca de LED.**
Total no escopo: **10,1 m** — cozinha (sob os suspensos), estante da sala,
banheiro social (lateral das prateleiras) e banheiro casal. R$ 1.515.

**Espessura por cenário.** As peças passaram a ser classificadas por papel —
`FUNDO` (6 mm nos dois), `PORTA/PRAT` e `ESTRUTURA` — e a espessura é
resolvida na hora do corte:

| | estrutura | porta e prateleira | fundo |
|---|--:|--:|--:|
| standard | 15 | **15** | 6 |
| gold | 15 | **18** | 6 |

O plano de corte agora sai **um por cenário**: 94 chapas nos dois, mas a
standard usa 88,8 m² de Tauari 15 e a gold reparte em 63 m² de 15 e 26 m²
de 18.

### ⛔ O rateio vazou de novo — e a causa era nova

O `assert` de item-sem-ferragem quebrou no *"Gourmet · painéis e forro"*. A
regra de 29/08 mandava ratear por custo com a base tomada **antes da
ferragem**, e isso bastava enquanto só a ferragem diferia entre versões. Com
a espessura variando, **a própria chapa entrou na base do rateio** e um item
100% estrutura passou a pegar uma fatia diferente em cada cenário.

Duas correções no motor:

```python
⛔ antes:  consumível e logística rateados por CUSTO (base contaminada)
✅ agora:  consumível = 6% da chapa e fita DO PRÓPRIO item, sem rateio
           logística  = rateada pela ÁREA de chapa, que não muda entre cenários
```

Sobrou um desvio de até **2,07%** nos itens só-estrutura, e ele é legítimo:
no gold parte da chapa de 15 migra para 18, o número de chapas de 15 cai e o
aproveitamento muda, então o m² de 15 custa um pouco diferente. É plano de
corte compartilhado, não vazamento — os itens sem chapa própria fecham em
0,00%. A guarda passou a tolerar 3% e o motivo está escrito no código.

### O fechamento

| Ambiente | m² | custo std | **venda std** | MC | custo gold | **venda gold** | MC |
|---|--:|--:|--:|--:|--:|--:|--:|
| Copa | 27,1 | 4.630 | **8.190** | 28,8% | 5.477 | **11.320** | 37,0% |
| Sala de reunião | 8,5 | 2.496 | **4.510** | 30,0% | 2.892 | **6.110** | 38,0% |
| Sala de ativos | 44,4 | 7.297 | **13.590** | 31,7% | 8.046 | **17.550** | 39,5% |
| Lounge | 26,7 | 5.267 | **9.030** | 27,0% | 5.481 | **10.890** | 35,0% |
| Gourmet | 47,8 | 8.554 | **14.850** | 27,7% | 8.798 | **17.770** | 35,8% |
| **Stand** | **154,4** | **28.243** | **50.170** | **29,1%** | **30.693** | **63.640** | **37,1%** |
| Cozinha | 69,6 | 22.107 | **40.260** | 30,4% | 23.764 | **50.630** | 38,4% |
| Sala e varanda | 40,8 | 9.257 | **16.940** | 30,7% | 9.314 | **19.980** | 38,7% |
| Quarto casal | 29,7 | 10.555 | **19.490** | 31,2% | 11.899 | **25.820** | 39,3% |
| Quarto solteiro | 25,2 | 8.797 | **16.310** | 31,4% | 10.150 | **22.130** | 39,5% |
| Banheiro social | 3,2 | 1.488 | **2.690** | 30,0% | 1.599 | **3.380** | 38,0% |
| Banheiro casal | 6,9 | 3.269 | **6.130** | 32,0% | 3.477 | **7.670** | 40,0% |
| **Decorado** | **175,4** | **55.472** | **101.820** | **30,9%** | **60.203** | **129.610** | **38,9%** |
| **TOTAL** | **329,8** | **83.715** | **R$ 151.990** | **30,3%** | **90.897** | **R$ 193.250** | **38,3%** |

Gold − standard: **R$ 41.260** (+27,1%), com **R$ 5.790** de ferragem e chapa
a mais. Espelhos seguem à parte e iguais: **R$ 2.081**.

### ⚠⚠ A espessura de 15 mm cria dois riscos técnicos

**1 · Vinte e cinco prateleiras longas ficam em 15 mm na standard.**
Vãos de 76 a 118 cm nos aparadores, na cozinha e nos dois roupeiros.
`roupeiros.md` é explícito: *"prateleira com comprimento > 70 cm → 18 mm
(evita empeno; ≤ 70 cm fica 15 mm)"*. Em 15 mm elas barrigam com carga.

**2 · Painel de parede piso/teto e o forro do gourmet ficam em 15 mm nos
DOIS cenários**, porque painel não é porta nem prateleira. São 31 peças de
210 a 262 cm de altura, incluindo o **forro suspenso do gourmet**. Painel
alto e forro suspenso em 15 mm flexionam.

| | standard | gold |
|---|--:|--:|
| como pedido | 151.990 | 193.250 |
| com painel, forro e prateleira longa em 18 | **158.030** | **197.550** |
| custo da exceção | **+6.040** | **+4.300** |

Não mexi — a especificação foi explícita. Mas os dois pontos são de
durabilidade, não de acabamento, e aparecem depois da entrega.

---

## 30/09/2026 (3º) — a proposta

> *"O painel e forro pode manter de 15 mm. Agora pode gerar a proposta.
> Forma de pagamento: entrada de 40% + 20% no início das montagens + 20% na
> entrega final + 20% em boleto [30] dias após a entrega."*

`build-marcelo-tolentino.py` → `proposta-marcelo-tolentino.pdf`, **10 páginas**,
com os dois cenários lado a lado. Painel e forro ficam em 15 mm, como decidido.

| | |
|---|--:|
| **Linha Standard** · 2 anos de garantia | **R$ 151.990** |
| **Linha Gold** · 10 anos de garantia | **R$ 193.250** |

Espelhos em **linha própria** na tabela, como pedido: R$ 3.860 na Standard e
R$ 4.530 na Gold — saem do valor do ambiente e aparecem destacados.

### A exceção de metragem

A regra de 12/09 proíbe qualquer medida na proposta. O Jonathan pediu em
30/09 que a **espessura da chapa apareça**, porque é o que separa as duas
linhas. O auditor passou a ter uma **lista de exceção fechada — `15 mm` e
`18 mm` — e barra todo o resto**. Resultado: limpo nos dois regex, com as
duas exceções usadas e nenhuma outra medida no documento.

### ⛔⛔ A escada de pagamento sumiu e o auditor disse "ok"

A página de investimento estourou, o `overflow:hidden` engoliu o bloco
inteiro da escada, e o auditor de transbordo **não viu**: ele mede a posição
do último bloco *que renderizou*, e não havia o que medir.

Duas coisas foram gravadas na skill:

1. **Auditor de conteúdo perdido (HTML → PDF)**, que passou a rodar antes do
   de transbordo. Normaliza os dois lados tirando espaço e acento e confere
   que cada frase do HTML saiu no PDF.
2. **Colisão de classe CSS pela segunda vez.** `css-proposta.css` já define
   `.inv`, `.pay`, `.esc` e `.cnd`, e o `.inv td` dele força
   `text-align:right`. Mordeu na Luiza em 12/09 e mordeu aqui. Agora toda
   classe nova leva sufixo: `.invA`, `.escP`, `.cndP`.

### Assumido, à espera de confirmação

| | |
|---|---|
| **Boleto** | *"20% em boleto para dias após a entrega"* — assumi **30 dias** |
| **Prazo** | não foi dado: propus **estande 60 dias · decorado 90 dias** |
| **Validade** | **10 dias corridos** |


---

## 30/09/2026 (4º) — a proposta enxugada

> *"A página 2 é completamente dispensável. Os textos ficaram muito longos,
> não precisa se ater para o que compra e para o que vende não. Fale apenas
> da marcenaria, pode ser mais sucinto nos textos. Estamos vendendo
> marcenaria, não stand, não decorado. Reduza a quantidade de página
> significativamente."*

**De 10 páginas para 5.** Saiu a página "O contrato" inteira e saiu toda a
narrativa comercial — *"um estande que vende e um decorado que convence"*,
*"é o ambiente que o comprador olha primeiro"*, *"o estande recebe quem
chega"*. Nada disso é marcenaria.

| antes | agora |
|---|---|
| 1 capa · 2 o contrato · 3–4 estande · 5–7 decorado · 8 as linhas · 9 investimento · 10 condições | **1 capa · 2 estande · 3 decorado · 4 as linhas · 5 investimento e condições** |

Os onze ambientes passaram a caber em duas páginas, cada um em **duas ou
três linhas** dizendo só o que é o móvel, em que material e com que detalhe
construtivo. A capa perdeu o slogan e ficou em **"Marcenaria sob medida."**

⛔ **O auditor de conteúdo perdido, criado nesta mesma rodada, ganhou o dia
duas vezes.** Ao compactar a página de investimento, a escada de pagamento
perdeu primeiro duas linhas e depois uma — e nas duas vezes o auditor de
transbordo continuou dizendo "ok", porque o bloco cortado não existe para
ele. Sem o auditor novo a proposta teria ido sem a condição de pagamento
completa, pela segunda vez no mesmo dia.

Valores inalterados: **Standard R$ 151.990 · Gold R$ 193.250**, espelhos em
linha própria.

---

## 30/09/2026 (5º) — entra o salão principal

> *"Agora, vamos voltar ao orçamento do Marcelo Tolentino e adicionar esses
> itens. Se atente para os armários com portas ripadas, considere abertura
> por toque, com fecho toque da Blum."*

Prancha **BRZ Estande de Vendas - Nova Lima_Salão principal**, 3 folhas A1,
rev. 01 de 30/09. Chegou depois das outras onze. Levantamento completo em
`levantamento-marcelo-tolentino.md`.

### O que entrou

| item | m² de chapa | custo std | custo gold |
|---|--:|--:|--:|
| armário ripado com abertura por toque | 83.1 | 17.957 | 20.419 |
| armário liso da entrada | 4.9 | 946 | 1.138 |
| painel liso piso/teto | 6.0 | 1.162 | 1.170 |
| pilar revestido em painel preto | 14.4 | 3.952 | 3.999 |
| bancada da secretária | 12.6 | 1.818 | 1.896 |
| **Salão principal** | **120.9** | **25.835** | **28.622** |

O salão sozinho tem **121 m² de chapa** — mais que a Cozinha (69,6) e
quase o dobro do Gourmet (47,8). Passa a ser **o maior ambiente do contrato**.

### ⭐ O armário ripado — o que o desenho realmente diz

A elevação 01 é uma parede de **690 × 220**, com **14 portas de 49,4**. Não
contei as ripas no olho: extraí os vetores da prancha e medi o passo.

| | |
|---|--:|
| verticais longas na elevação | 161 |
| passo dominante | **9,3 cm** (ripa 6,2 · vão 3,1) |
| ripas ao longo dos 690 | **73** |
| por porta | **5** |

Daí o lançamento: **porta base + 5 ripas de 6,2 × 220 coladas**, com a fita
de borda das ripas entrando no corte como peça de verdade. São **316 m de
fita** só nas ripas — é isso que faz frente ripada custar o que custa, não a
usinagem.

### ⛔ Três decisões técnicas que o "abertura por toque" obriga

**1 · A dobradiça tem de ser sem mola.** Tip-on mecânico e mola trabalham um
contra o outro: a mola empurra a porta de volta contra o pulsador e ela
reabre sozinha. Novisys e Sensys têm versão sem mola — é ela que tem de
entrar na compra. **Está na cotação como condição, não como preferência.**

**2 · Dois pulsadores por porta.** A Blum especifica duas unidades acima de
1,20 m de altura de porta. Estas têm 2,20 m. São **28 pulsadores**, não 14 —
**R$ 2.800**, o item de ferragem mais caro do contrato inteiro, e ele **não
muda entre standard e gold**.

**3 · A porta ripada trava em 18 mm nos DOIS cenários.** Ripa colada numa
face só faz par bimetálico: a porta encurva para o lado das ripas. Em
49,4 × 220 e 15 mm ela empena, e **porta empenada não fecha no toque** — o
pulsador não engata. Aqui a espessura é requisito de funcionamento, não
nível de acabamento, então `papel()` ganhou o papel `E18` e a regra de
cenário não alcança essa peça.

Ferragem do salão: **R$ 3.862** na standard, **R$ 5.786** na gold —
a diferença é só a dobradiça, porque o pulsador é o mesmo.

### Uma correção de arrasto

A **porta de 230 × 100 do Lounge** estava com 4 dobradiças. Para essa altura
são 5, como as do salão. Corrigido — custa R$ 10 na standard e R$ 35 na gold,
e o preço do ambiente nem se mexeu no arredondamento.

### O que ficou de fora, de propósito

Granito cinza andorinha escovado (marmoraria) · rodapé cinza Santa Luzia
H=15 (perfil comercial, corre também nas paredes que não são nossas) ·
divisória e porta pivotante em vidro temperado · porta de entrada em vidro
com perfil de 10 · molduras das fotos 85×150 e TVs touch (comunicação
visual) · pintura · mobiliário solto.

### O fechamento

| Ambiente | m² | custo std | **venda std** | MC | custo gold | **venda gold** | MC |
|---|--:|--:|--:|--:|--:|--:|--:|
| Salão principal | 120.9 | 25.835 | **47.360** | 30.8% | 28.622 | **61.600** | 38.9% |
| Copa | 27.1 | 4.577 | **8.100** | 28.8% | 5.477 | **11.310** | 36.9% |
| Sala de reunião | 8.5 | 2.480 | **4.480** | 30.0% | 2.870 | **6.060** | 38.0% |
| Sala de ativos | 44.4 | 7.222 | **13.450** | 31.7% | 7.959 | **17.360** | 39.5% |
| Lounge | 26.7 | 5.226 | **8.960** | 27.0% | 5.521 | **10.970** | 35.0% |
| Gourmet | 47.8 | 8.452 | **14.670** | 27.7% | 8.873 | **17.920** | 35.8% |
| **Stand** | **275.3** | **53.791** | **97.020** | **29.9%** | **59.323** | **125.220** | **38.0%** |
| Cozinha | 69.6 | 21.972 | **40.020** | 30.4% | 23.804 | **50.710** | 38.4% |
| Sala e varanda | 40.8 | 9.167 | **16.780** | 30.7% | 9.448 | **20.270** | 38.7% |
| Quarto casal | 29.7 | 10.491 | **19.370** | 31.2% | 11.900 | **25.830** | 39.3% |
| Quarto solteiro | 25.2 | 8.739 | **16.200** | 31.4% | 10.170 | **22.180** | 39.5% |
| Banheiro social | 3.2 | 1.482 | **2.680** | 30.1% | 1.611 | **3.400** | 38.0% |
| Banheiro casal | 6.9 | 3.256 | **6.100** | 32.0% | 3.489 | **7.690** | 40.0% |
| **Decorado** | **175.4** | **55.106** | **101.150** | **30.9%** | **60.421** | **130.080** | **38.9%** |
| **TOTAL** | **450.7** | **108.898** | **R$ 198.170** | **30.4%** | **119.744** | **R$ 255.300** | **38.4%** |

Gold − standard: **R$ 57.130** (+28.8%).
Espelhos seguem à parte e iguais: **R$ 2.081**.

A MC não se mexeu (standard 30,3 → 30.4%,
gold 38,3 → 38.4%): **o alerta de
30/09 continua de pé — se o cliente fechar a Standard, o contrato inteiro
roda abaixo do piso de 35% da casa.** Com o salão dentro, agora são
R$ 198.170 rodando a 30.4%.

### ⛔⛔ A proposta perdeu conteúdo DUAS vezes, e o auditor de transbordo achou tudo ok

Ao caber o sexto ambiente na página 2 e a décima-terceira linha na tabela da
página 5, duas coisas sumiram: **o bloco inteiro da Copa** e, pela quarta
vez, **a última parcela da escada de pagamento**.

**A causa raiz, enfim identificada:** `.pad` é coluna flex. Uma caixa com
`overflow:hidden` e `flex-shrink` padrão **encolhe** quando a coluna estoura,
e o conteúdo que sobra é cortado **sem empurrar o rodapé**. O auditor de
transbordo mede a distância até o rodapé e responde "folga 27 pt, ok".

Duas correções, as duas gravadas:

```css
.escP{ ... overflow:hidden; flex:none; }   /* sem isto, a caixa encolhe em silêncio */
```

E o auditor de transbordo ganhou a checagem que faltava: **rodapé ausente é
transbordo.** Na página 2 o estouro tinha empurrado o rodapé para fora da
folha; o auditor caía em `pg.rect.y1` e dizia "folga 28 pt" com duas linhas
de texto escritas por cima de onde o rodapé deveria estar.

```python
fb = [b for b in bl if 'valvicmarcenaria' in norm(b[4])]
if not fb and i > 1: print('⛔ RODAPÉ PERDIDO — a página estourou')
```

### A proposta

`proposta-marcelo-tolentino.pdf`, **5 páginas**. O salão principal abre o
estande como item **01** e o decorado renumera para 07–11.

| | |
|---|--:|
| **Linha Standard** · 2 anos de garantia | **R$ 198.170** |
| **Linha Gold** · 10 anos de garantia | **R$ 255.300** |

Três passes limpos: conteúdo perdido · transbordo · metragem e contagem.
