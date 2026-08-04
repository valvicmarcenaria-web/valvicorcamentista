# Cristaleira — 100 × 205 × 40

**Entrada** prancha A3 cotada (`DETCristaleira.pdf`), 1:20, quatro vistas + 3 renders.
**Premissas [Jonathan 04/08/2026]** sem RT · MC 35% · 60 dias corridos · pagamento na
escada padrão · ferragens **Hardt**.
**Motor** `corte-cristaleira.py`

## Geometria lida da prancha

| | |
|---|---|
| Externa | **100 L × 205 A × 40 P** |
| Corpo | 201 A × 38 P · interno **96** |
| Superior **115** | tampo 2 + **4 vãos de 26,75** + 3 prateleiras |
| Divisória | 2 |
| Inferior **84** | **3 gavetas de 28** (25 de frente + 3 de folga) |
| Pé | **4**, com **recuo frontal de 2 cm** |
| Portas | **2 × 50 × 201**, moldura de **4 cm**, vidro incolor **42 × 193** |
| Puxador | a **110 do piso** |

Confere: 115 + 2 + 84 + 4 = **205** · 201 + 4 = **205**.

## Especificação

- **MDF Arauco Moscada Matt** (melamínico fosco) no corpo, interior, molduras das
  portas e frentes de gaveta.
- **Caixa de gaveta em MDF Branco TX** — a prancha pede interior branco.
- Puxador **Ponto Italyline Ales 118, cor cobre velho** nas portas ·
  **cava 45° usinada** nas gavetas.
- Vedação em **vidro incolor**.

> **Espessuras.** A prancha desenha tudo em 2 cm, que é convenção de prancheta.
> Apliquei a regra da casa: **15 mm na caixaria · 18 mm nas prateleiras (vão de 96),
> divisória, portas e frentes · 6 mm nos fundos.**

## Plano de corte — 5 chapas

| Material | Área | Chapas | Aproveitamento |
|---|--:|--:|--:|
| Moscada 15 | 2,36 m² | 1 | 46% |
| Moscada 18 | 2,51 m² | 1 | 49% |
| Moscada 6 | 1,95 m² | 1 | 38% |
| Branco TX 15 | 1,49 m² | 1 | 29% |
| Branco TX 6 | 0,95 m² | 1 | 19% |
| **Total** | **9,26 m²** | **5** | **36%** |

> **36% é baixo e eu conferi antes de aceitar** — o levantamento fecha peça a peça.
> Não é erro de nesting: é o piso de **peça única com 5 materiais**. Cada material
> exige uma chapa inteira, então 9,26 m² de peças consomem 25,4 m² de chapa. Num
> projeto de vários móveis isso diluiria; aqui não tem como.

## Custo e preço

| | |
|---|--:|
| Chapas | 1.850,00 |
| Fita (45,8 m) | 142,82 |
| Filetagem — 36,4 m na coladeira + 9,4 m manual | 128,65 |
| Ferragens, vidro e vidraceiro | 1.040,24 |
| Consumíveis (6%) | 119,57 |
| Logística · visita · instalação | 1.150,00 |
| **CUSTO DIRETO** | **4.431,28** |

**MC 35%, sem RT** — divisor `1 − 0,162 − 0,88×0,043 − 0,35` = **0,45016**.
R$ 4.431,28 ÷ 0,45016 = R$ 9.843,80 → **tabela R$ 9.800**. MC conferida: **34,8%**.

| Condição | | Valor |
|---|--:|--:|
| Entrada 30% + até 10× no cartão | — | **R$ 9.800** |
| Entrada 50% + até 8× no cartão | −3% | R$ 9.500 |
| Entrada 70% + até 6× no cartão | −5% | R$ 9.300 |
| Entrada 70% + restante em transferência | −7% | R$ 9.100 |

> **Sobre o "sem RT".** O conjunto `a=0,162 · liqF=0,88 · b=0,043` **já é o de fora
> de parceria** — RT são 10% do líquido e não estão embutidos aqui. Não precisei
> tirar nada; o pedido só confirma o conjunto certo.

## 💡 O interior branco da gaveta custa R$ 1.000

A prancha manda a caixa da gaveta em Branco TX. São **2,44 m² de peças que obrigam a
comprar duas chapas inteiras** (R$ 260 + R$ 190) — e as sobras do Moscada dariam conta
com folga: sobra 2,73 m² no 15 mm (preciso 1,49) e 3,14 m² no 6 mm (preciso 0,95).

| | Chapas | Custo direto | Tabela |
|---|--:|--:|--:|
| Como a prancha pede (gaveta branca) | 5 | 4.431,28 | **R$ 9.800** |
| Gaveta na sobra do Moscada | 3 | 3.954,28 | R$ 8.800 |

**Mantive o branco**, que é o que está especificado. Mas é uma escolha de projeto de
R$ 1.000, não uma exigência técnica — vale o cliente saber que ela existe.

## ⚠ Na margem, não no custo

Pelo método da casa a hora de bancada fica na margem. Neste móvel isso pesa mais que o
normal: são **8 encaixes de moldura** e **9,4 m de rebaixo** para assentar o vidro. Em
chapa a porta é barata — **R$ 45,85 de MDF** para as duas folhas. O custo dela é
bancada, exatamente como o ripado dos quartos do Mateus e da Manuela.

Se essa hora entrar na conta, os 35% viram ~33,5% reais. Para blindar,
**MC 37% → tabela R$ 10.300**.

## ⚠ A confirmar

1. **Puxador Ponto Italyline Ales 118, cobre velho** — não está na base. Lancei
   **R$ 60/un** por analogia com o Traço Metal/Couro (R$ 60, premium). São 2 unidades,
   então o erro máximo é pequeno, mas o preço real precisa ser levantado.
2. **Vidro.** Usei **incolor temperado 6 mm a R$ 200/m²** (1,62 m²). A prancha só diz
   "vidro incolor". Peça de **1,93 m de altura** dentro de casa — temperado é a escolha
   segura. Comum de 4 mm cairia para ~R$ 100 no total, mas não recomendo nessa altura.
3. **Profundidade da prateleira** não cotada. Adotei 36 (2 cm recuada da frente).
