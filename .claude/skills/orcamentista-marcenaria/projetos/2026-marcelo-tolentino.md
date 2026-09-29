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
