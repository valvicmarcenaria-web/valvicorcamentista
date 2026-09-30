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
