# Painel da Sala — VISTA 2 · ripado, nicho de pedra e portas mimetizadas

**Pranchas:** `SALA - VISTA 2` (1/50) e `NICHO RIPADO` (1/30, pág. 18).
**Entregue:** `projetos/painel-sala/` — `base.py`, `levantamento.py`,
`cenarios.py`, `proposta.py` → `Painel da Sala · Proposta Valvic.pdf`, uma A4.

---

## ⭐⭐ FECHADO EM R$ 49.800 · obra em GOVERNADOR VALADARES

> [Jonathan, 17/11/2026] *"vamos vender por 53.000 esse projeto / deixe claro na
> proposta que é com a conferencia tecnica e instalação em Governador
> Valadares"* e, um minuto depois, *"alias, por 49.800"*. Vale o segundo.

### ⛔ "Governador Valadares" derrubou a minha linha de frete

Os **R$ 200 por viagem** que você cravou em 29/10 são número de **Belo
Horizonte**: o caminhão sai, entrega e volta no mesmo turno. **GV fica a 320 km**
— 640 de ida e volta — e a equipe dorme fora. Eu tinha **R$ 400 no projeto
inteiro**; só a instalação passa de quatro mil.

⚠ E a Base não me salvou desta: as **quatro** linhas de frete da aba MDF estão
vazias, de propósito — *"linha criada e vazia de propósito: assim o orçamento
mostra zero e grita"*. Ela gritou. Montei a logística linha a linha:

| | veículo | equipe | cama | comida | total |
|---|--:|--:|--:|--:|--:|
| Conferência técnica · 1 pessoa, 1,5 d, 1 noite | 768,00 | 432,00 | 180,00 | 120,00 | **1.500,00** |
| Instalação · 2 pessoas, 3 d, 2 noites | 1.152,00 | 1.728,00 | 720,00 | 480,00 | **4.080,00** |
| **TOTAL** | | | | | **R$ 5.580,00** |

⚠ Só a **hora de marceneiro (R$ 36 com encargos)** vem da Base. O resto é
estimativa minha — km a R$ 1,20 (utilitário) e R$ 1,80 (caminhão), hospedagem
R$ 180 por noite, alimentação R$ 80 por dia. **Trocar um desses números refaz o
bloco sozinho.**

### O fechamento

| | |
|---|--:|
| **PREÇO FECHADO** | **R$ 49.800,00** |
| custo direto | R$ 16.519,71 |
| — dos quais, logística de GV | R$ 5.580,00 |
| **MC lida · com RT de 10%** | **42,92%** |
| MC lida · se não houver RT | 51,70% |
| margem de contribuição | R$ 21.371,87 |
| empate em dias de fábrica | 5,3 d |

⛔⛔ **A LOGÍSTICA DE GV VALE 10,4 PONTOS DE MC.** Sem ela eu estaria reportando
**53,32%** e precificando sobre uma ficção.

⚠ **RT de 10% é leitura minha** — você não disse. São pranchas executivas de
arquiteto e a regra da casa é "RT quando há parceiro indicando". Sem RT a MC vai
a 51,70%.
⚠ **Prazo (60 dias) e pagamento (50% + 50%) também são leitura minha.**

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

## ⑦ A régua de preço

⚠ Nada fechado ainda. [Jonathan, 17/11/2026] perguntou **"e se a MC for de 50%?"**

| MC, com RT de 10% | preço | margem | empate em dias de fábrica |
|---|--:|--:|--:|
| 35% | R$ 27.598,92 | R$ 9.659,62 | 2,4 d |
| 40% | R$ 31.422,81 | R$ 12.569,12 | 3,1 d |
| 45% | R$ 36.476,74 | R$ 16.414,53 | 4,1 d |
| **50%** | **R$ 43.467,97** | **R$ 21.733,99** | **5,4 d** |
| 55% | R$ 53.774,54 | R$ 29.576,00 | 7,4 d |

| MC 50% | base | preço | margem | empate |
|---|--:|--:|--:|--:|
| sem RT | 84,87% | R$ 32.515,29 | R$ 16.257,64 | 4,1 d |
| com RT de 10% | 76,09% | R$ 43.467,97 | R$ 21.733,99 | 5,4 d |
| com RT e vendedor | 67,30% | R$ 65.547,44 | R$ 32.773,72 | 8,2 d |

⭐⭐ **E O EMPATE É QUEM JUSTIFICA OS 50%, não o posicionamento.** O empate é
margem ÷ R$ 4.000 de custo fixo por dia. A 40% ele dá **3,1 dias de fábrica
exclusiva** — e só a **filetagem manual** deste painel são 292 m, cerca de
**40 horas de bancada** a R$ 36/h de marceneiro com encargos (aba
Terceirizados). Somadas a colagem de 162 ripas, o tamponamento das duas
portas de 42 e a instalação de 6,82 m, o painel ocupa mais do que 3 dias.
A 50% o empate vai a 5,4 dias, que é mais perto do que ele realmente custa
em tempo de fábrica. ⛔ A 35% ou 40% este job específico fica apertado.

| a MC de 50% nas duas dúvidas vivas | custo | preço com RT |
|---|--:|--:|
| como orçado | R$ 11.339,71 | R$ 43.467,97 |
| Gianduia Trama for padrão especial | R$ 13.471,22 | R$ 51.638,58 |
| a ripa entrar na coladeira | R$ 10.595,21 | R$ 40.614,12 |

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
