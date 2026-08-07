# Orçamento — Cozinha (consultoria Rizzi Interiores)

> **Status:** 🟢 Precificado em 07/08/2026 — **R$ 43.400** (MC 35% · COM RT · Hardt).
> Aguarda medição no local e as duas linhas ilegíveis do documento.
> Fontes: `DOC-2026...A0017.pdf` · `RI - CONSUL...ELENA.pdf` · `Casa Sil.pdf` (capturas).
> Script: `corte-cozinha-elena.py`

## ⚠️ A fonte é CONSULTORIA, não executivo

O próprio documento diz, na página de observações:

> *"Todas as medidas especificadas neste documento foram tiradas de planta baixa ou
> medidas básicas in loco, **não servindo como referência para compra final**... na
> consultoria não tem detalhamentos, ou seja, medidas detalhadas do espaço, layout e
> Planejados."*

Mesmo caso do Kairon & Juliana: estimar por envelope + render, sinalizar o que precisa
de conferência. **Medição no local é pré-requisito do contrato, não formalidade.**

## O documento fecha sozinho — e isso vale muito

Diferente de um anteprojeto solto, as cotas da Rizzi são coerentes entre si:

| Verificação | Conta | Resultado |
|---|---|---|
| Altura da bancada | 77 (armário) + 10 (sóculo recuado) + 3 (granito) | **90** ✓ o doc diz "instalada a 90cm" |
| Pé-direito pela pilha | 90 + 110 (nicho freijó) + 70 (aéreo azul) | **270** = altura da torre ✓ |
| Parede 2 | 150 (bancada B) + 70 (torre) + 80 (geladeira) | **300** = cota da planta ✓ |
| Parede 1 | 272 (bancada A) + 60 (retorno) | **332** = cota da planta ✓ |

A janela ocupa os 122 cm restantes da bancada A — é por isso que o aéreo azul tem
só 150 e não 272.

**Dois planos de profundidade outra vez:** 60 cm em tudo (bancada, aéreos, torre) e
**45 cm** só no aéreo de básculas em freijó — o que fica em altura de trabalho.

## Escopo — 9 móveis, 3 cores + branco interno

| # | Móvel | A×L×P | Cor |
|---|---|---|---|
| 1 | Armário bancada A | 77×272×60 | Azul Ardósia |
| 2 | Armário bancada B (fecha o "L") | 77×150×60 | Azul Ardósia |
| 3 | Nicho | 110×150 | Freijó |
| 4 | Aéreo de básculas | 40×147×45 | Freijó |
| 5 | Aéreo | 70×150×60 | Azul Ardósia |
| 6 | Torre quente (tomadas embutidas na lateral) | 270×70×60 | Cinza Urban |
| 7 | Aéreo da geladeira | 70×80×60 | Cinza Urban |
| 8 | Painel ripado ⚠ | estimado 270×120 | Freijó |
| 9 | Mesa ⚠ | estimado 150×60 | Freijó |

**Fora do escopo:** granito Itaúnas, porcelanato Portinari, cooktop, cuba, misturador,
purificador, forno, micro-ondas, geladeira, luminária de embutir, cadeiras, rebaixo de gesso.

## Quantitativo

| Material | Área | Chapas | Aprov. |
|---|--:|--:|--:|
| Branco 15 (caixaria) | 26,40 m² | 7 | 74% |
| Branco 6 (fundos) | 12,25 m² | 4 | 60% |
| Branco 18 (prateleiras) | 2,11 m² | 1 | 41% |
| Azul Ardósia 18 | 4,67 m² | 2 | 46% |
| Cinza Urban 18 | 3,58 m² | 1 | 70% |
| Freijó 15 | 4,40 m² | 2 | 43% |
| Freijó 18 | 5,22 m² | 2 | 51% |
| **Total** | **58,64 m²** | **19** | **61%** |

Fita **257,11 m** · 18 dobradiças · 14 corrediças ocultas · 5 articuladores ·
16,94 m de cava usinada.

### O ripado é 42% de toda a fita

108 dos 257 m de fita são as **ripas do painel** — 20 ripas × 2 faces longas × 2,70 m.
É onde o item se paga em fita e em coladeira, não em chapa. Se as "ripas de 1cm" do
documento forem literais, são ~60 ripas e a fita vai a **324 m só nesse item**.

## Custo direto

| | |
|---|--:|
| Chapas — 19 | R$ 6.700,00 |
| Fita (material) — 257,11 m | R$ 771,43 |
| Filetagem | R$ 642,78 |
| Ferragens, cava e usinagem | R$ 2.959,00 |
| Consumíveis (6%) | R$ 448,29 |
| Logística · 2 visitas · instalação | R$ 4.200,00 |
| **CUSTO DIRETO** | **R$ 15.721,49** |

## Preço — parâmetros travados [Jonathan 07/08]

**MC 35% · COM RT (10% do líquido) · ferragem Hardt** → divisor **0,36216**.

| Linha | Custo direto | Tabela |
|---|--:|--:|
| **Armários inferiores da bancada** (móveis 1 e 2) | R$ 5.501,35 | **R$ 15.200** |
| Demais móveis (aéreos, nicho, torre, ripado, mesa) | R$ 10.220,14 | **R$ 28.200** |
| **Total** | **R$ 15.721,49** | **R$ 43.400** |

MC conferida **35,0%**. RT ao parceiro: **R$ 3.819**.
Escada: −3% 42.100 · −5% 41.200 · −7% **40.400**.

### Como a bancada foi separada

Rateio **por área dentro de cada material**, não re-nesting. BR15, BR18, BR6 e AZ18
são compartilhados com os aéreos — nestar os dois grupos em separado somaria mais
chapas que o conjunto, por causa do piso de 1 chapa por cor × espessura. O rateio faz
as duas linhas fecharem no total.

| Material | Bancada | Restante | Chapas |
|---|--:|--:|--:|
| AZ18 | 3,20 m² | 1,47 m² | 2 |
| BR15 | 11,76 m² | 14,65 m² | 7 |
| BR18 | 0,83 m² | 1,28 m² | 1 |
| BR6 | 7,08 m² | 5,18 m² | 4 |
| CZ18 · FR15 · FR18 | — | 13,20 m² | 5 |

Fita, filetagem e ferragens saem **exatos** (cada linha tem tag de grupo);
consumíveis e logística seguem a proporção do material.

### ⚠️ O rateio não é a economia de tirar o bloco

Se a bancada inferior sair do escopo, o restante **nestado sozinho** dá 13 chapas
(R$ 4.990) contra os R$ 4.572 do rateio, e a instalação da cozinha não cai 28%.

| | |
|---|--:|
| Custo do restante sozinho | R$ 10.961,04 |
| Preço | **R$ 30.300** |
| **Economia real de tirar a bancada** | **R$ 13.100** |
| *A linha rateada mostra* | *R$ 15.200* |

**São R$ 2.100 de diferença.** Se a conversa virar "e sem os armários de baixo?",
o número a defender é 30.300 — não 43.400 − 15.200.

## ⚠️ Aberto

1. **Duas linhas do documento estão cobertas pela barra de rolagem na captura** —
   o painel ripado e a mesa. Dimensões usadas são leitura do render.
2. **"Ripas de 1cm"** — usei ripa de 4 cm com vão de 2 (20 ripas). Se for literal,
   são ~60 ripas e a fita desse item vai de **108 m para 324 m**.
3. **Interno branco** assumido — a consultoria não especifica o interno de nenhum móvel.
4. **Divisão interna dos módulos da bancada** é minha leitura da elevação etiquetada
   (GIRO / BASC / GAV / PORTA), não cota do documento.
5. **Medição no local é pré-requisito do contrato** — o próprio documento diz que as
   cotas dele "não servem como referência para compra final".
