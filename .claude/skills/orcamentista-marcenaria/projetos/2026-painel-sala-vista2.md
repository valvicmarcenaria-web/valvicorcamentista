# Painel da Sala — VISTA 2 · ripado, nicho de pedra e portas mimetizadas

**Pranchas:** `SALA - VISTA 2` (1/50) e `NICHO RIPADO` (1/30, pág. 18).
**Entregue:** `projetos/painel-sala/` — `base.py`, `levantamento.py`,
`cenarios.py`. ⚠ **Proposta ainda não gerada.**

---

## ⛔⛔ A PRIMEIRA VERSÃO SAIU DAS CONSTANTES, NÃO DA BASE

> [Jonathan, 17/11/2026] *"o quantitativo de chapas esta errado / vc
> quantificou onde esta as chapas da base onde as ripas serão coladas? / fita
> de borda tem certeza que é so isso? / e o custo da filetagem? / iluminação nao
> é nossa / e as dobradiças da porta a esquerda? / **refaça com base nas
> planilhas**."*

Cinco erros, e a planilha tinha a resposta dos cinco. **Custo direto foi de
R$ 8.332,44 para R$ 11.339,71 — 36% a mais.**

### 1 · Porta de passagem é 42 mm, não 18
A aba MDF, em *"ESPESSURA PADRÃO POR APLICAÇÃO"*: **"Portas de passagem ·
42 mm"**. Eu orcei duas folhas de 18. Uma folha de 42 é **18 + 18 + 6** — a
mesma área três vezes, mais um miolo de Branco TX que eu não tinha comprado.
O item foi de R$ 1.419,28 para **R$ 2.738,57**.

### 2 · A fita das ripas não existia no orçamento
⛔ Eu cobrei a **filetagem** (a aplicação) e esqueci a **fita** (o material) nos
285 m de ripa. A Base tem o par pronto: *"Fita de cor com filetagem, preço cheio
da casa · R$ 5,50 · **já inclui a aplicação**"* — que é 3,00 de fita mais 2,50
de aplicação.

### 3 · A ripa de 2 cm não entra na coladeira automática
A Base separa *"Filetagem na coladeira automática · 15 e 18 mm · R$ 2,50"* de
*"Filetagem manual · ripa de 6 mm **e o que não entra na máquina** · R$ 5,00"*.
Coladeira automática não pega peça de 20 mm de largura. **É manual.**
Vale **R$ 744,50** (`RIPA_NA_MAQUINA=1` roda o cenário barato).

**Fita e filetagem somam R$ 2.818,15**, contra os R$ 713,70 que eu tinha.

### 4 · A borda de 42 mm pede fita de 50
*"Fita de borda cor · 50 mm · R$ 7,00 · para peça de 5 cm"*. Eu usei a de 22 em
tudo.

### 5 · A porta da esquerda não tinha dobradiça nenhuma
Ela é porta de **armário**, não de passagem: dobradiça, não pivô. E a tabela da
Base manda **cinco**, porque 277 passa de 200 cm. Mais a barra chata contra
empeno, que 2,77 m em 15 mm pede.

### E a iluminação saiu
*"iluminação nao é nossa"*. A prancha diz **PREVER** fita de LED, e prever é o
elétrico. **−R$ 613,93.**

---

## ① A ripa e a sua base

| banda | face | ripas | fita + filete | m² de face |
|---|--:|--:|--:|--:|
| Porta ripada do armário | 50 × 277 | 12 | 67,0 m | 1,39 |
| Banda superior do nicho | 302 × 75 | 75 | 115,5 m | 2,27 |
| Banda inferior do nicho | 302 × 71 | 75 | 109,5 m | 2,14 |
| **TOTAL** | | **162** | **292,0 m** | **5,79** |

**A base onde as ripas são coladas** — a pergunta dele:

| peça | medida | m² |
|---|---|--:|
| BASE do ripado · banda superior | 302 × 75 × 15 | 2,27 |
| BASE do ripado · banda inferior | 302 × 71 × 15 | 2,14 |
| BASE do ripado · folha da porta | 50 × 277 × 15 | 1,39 |
| **soma** | | **5,79** |

⚠ A trama é **20/20** — passo de 4 cm, contra os 6 do padrão da casa. 162 ripas
contra 108.

## ② O quantitativo de chapas

| padrão e espessura | área | fração | chapas | R$/chapa | custo |
|---|--:|--:|--:|--:|--:|
| MDF Branco TX 6 mm · miolo das portas | 3,21 m² | 0,79 | 1 | 250,00 | 250,00 |
| MDF Branco TX 18 mm · estrutura | 4,30 m² | 1,06 | 2 | 400,00 | 800,00 |
| MDF Gianduia 15 mm · base do ripado | 5,79 m² | 1,42 | 2 | 550,00 | 1.100,00 |
| MDF Gianduia 18 mm · liso, portas e ripa | 16,98 m² | 4,17 | 5 | 700,00 | 3.500,00 |
| **TOTAL** | **30,29 m²** | | **10** | | **5.650,00** |

## ③ Fita e filetagem

| onde | metros | R$/m | material | aplicação |
|---|--:|--:|--:|--:|
| Fita 22 mm · peças e portas | 47,9 | 5,80 | 158,17 | 119,83 |
| Fita 50 mm · borda de 42 das portas | 11,5 | 10,20 | 88,24 | 28,65 |
| Fita 22 mm · as duas faces da ripa | 292,0 | **8,30** | 963,47 | 1.459,80 |
| **TOTAL** | **351,4** | | **1.209,88** | **1.608,27** |

**R$ 2.818,15** de fita mais filetagem — 25% do custo direto.

## ④ Ferragem — R$ 690,00

5 dobradiças Hettich Sensys (R$ 250) · alma de aço (R$ 50) · 2 sistemas pivô
(R$ 240) · 2 fechos rolete (R$ 150).

| escada da Base, para a porta da esquerda | 5 × | total |
|---|--:|--:|
| Bigfer Inox Click | 10,00 | 50,00 |
| Bigfer Onix | 15,00 | 75,00 |
| Hettich Novisys | 20,00 | 100,00 |
| **Hettich Sensys ← orçado** | 50,00 | **250,00** |

## ⑤ O custo

| item | custo direto |
|---|--:|
| Painel ripado · base e ripas | R$ 4.406,40 |
| Duas portas mimetizadas de passagem · 42 mm | R$ 2.738,57 |
| Porta ripada do armário · 50 × 277 | R$ 1.693,88 |
| Painel liso com os vãos · 330 × 277 | R$ 1.546,41 |
| Estrutura de fixação | R$ 954,45 |
| **CUSTO DIRETO** | **R$ 11.339,71** |

| por natureza | |
|---|--:|
| Chapa · 10 chapas | R$ 5.650,00 |
| Filetagem · aplicação | R$ 1.608,27 |
| Fita de borda · 351 m, material | R$ 1.209,88 |
| Terceirizado · painel ripado 5,79 m² × 180 | R$ 1.042,96 |
| Ferragem | R$ 690,00 |
| Consumíveis 6% · corte · embalagem 2% | R$ 738,59 |
| Frete · 2 viagens | R$ 400,00 |

## ⑥ O que cada dúvida vale

| | custo direto | |
|---|--:|--:|
| **como orçado** | **R$ 11.339,71** | — |
| se o ripado corresse os 682 inteiros | R$ 17.745,54 | +R$ 6.405,83 |
| se Gianduia Trama for padrão especial | R$ 13.471,22 | +R$ 2.131,51 |
| se a ripa entrar na coladeira (R$ 2,50) | R$ 10.595,21 | −R$ 744,50 |
| se os montantes forem a cada 75 cm | R$ 10.900,09 | −R$ 439,62 |
| se a dobradiça cair para Bigfer Inox | R$ 11.135,71 | −R$ 204,00 |
| se a dobradiça cair para Novisys | R$ 11.186,71 | −R$ 153,00 |
| se a base do ripado sair em 18 | R$ 11.501,89 | **+R$ 162,18** |

⭐ A última eu achei que economizaria R$ 400 e **custa R$ 162**: em 18 mm a base
entra na pilha do liso e empurra a sexta chapa. Medir em vez de supor.

## ⑦ A régua de preço — nada fechado

| | MC 35% | MC 40% |
|---|--:|--:|
| sem RT | R$ 22.736,25 | R$ 25.269,54 |
| com RT de 10% | R$ 27.598,92 | R$ 31.422,81 |

---

## ⛔ Fora do escopo
Nicho de mármore travertino · sóculo em alvenaria · rodapé de mármore · janela
202 × 175 · **a iluminação do nicho**.

## Dúvidas abertas
1. ⭐ **O painel é pele sobre alvenaria, ou a marcenaria faz o volume de 50?**
2. ⭐ **O interior do "ARMÁRIO 50X274" não está desenhado** — não está orçado.
3. ⭐ **A face das portas de passagem voltada para o outro ambiente** — orcei
   Gianduia dos dois lados; as pranchas não mostram o outro lado.
4. ⚠ **Gianduia Trama é padrão especial?** R$ 2.131,51.
5. ⚠ **A ripa entra ou não na coladeira?** R$ 744,50.
6. ⚠ **Linha de dobradiça** — orcei Sensys; a Base deixa o Padrão "A DEFINIR".
7. ⚠ **Painel ripado a R$ 180/m²** — a Base avisa "faixa de 70 a 420, depende da
   largura da ripa e do vão". Trama de 20/20 é a mais fechada que já fizemos:
   estamos no lado caro da faixa, e R$ 180 pode ser otimista.
8. ⚠ **As quatro linhas de frete da Base estão vazias** ("A COTAR"). Usei os
   R$ 200 por viagem que você cravou em 29/10.
9. ⚠ **MC, RT, preço e nome do cliente.**
