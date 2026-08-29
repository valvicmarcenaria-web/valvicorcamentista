# DEVA Veículos (IVECO) — projeto executivo de marcenaria

**Cliente** DEVA Veículos · concessionária IVECO
**Projeto** arq. **Beatriz Fernandez Gontijo** · CAU A 75464-1
Ofício Planejamento e Consultoria — Av. Prudente de Morais 44, BH
**Entrada** 4 pranchas A1, AGO/2026, revisão 00 · **motor** `corte-deva.py`

## O insumo

Quatro pranchas, todas **CASO A** (com camada de texto). São pranchas boas:
cotam tampo de 3 cm, friso de 1×1, recuo de 3, balcão a 105 e bancada a 75, e
trazem planta + vistas + seções de cada conjunto. Não têm quadro de peças —
então o levantamento é **leitura de cota**, não transcrição.

| Prancha | Setor | Conjuntos |
|---|---|---|
| EX01 | Comercial | balcão comercial + painel de parede |
| EX02 | Comercial | painel de TV + balcão café + bancada da janela |
| EX03 | Vendas | balcão da recepção + painel de parede |
| EX04 | Vendas | painel/expositor de vidro + espaço café |

## Números

| | |
|---|--:|
| Área de chapa | **89,85 m²** |
| Chapas | **30** · aproveitamento médio 59% |
| Custo direto | **R$ 28.757** |
| R$/m² de chapa (MC 38% s/ RT) | **761** ✅ dentro da faixa 626–834 |

| MC | sem RT | com RT 10% |
|---|--:|--:|
| 35% | R$ 63.900 | R$ 79.400 |
| **38%** | **R$ 68.400** | **R$ 86.600** |
| 40% | R$ 71.900 | R$ 92.100 |

Setor Comercial R$ 29.800 · Setor Vendas R$ 38.600 (rateio por área, MC 38% s/ RT).

## 🔴 BURACO DE ESCOPO

A planta da EX03 chama **"PAINEL EM MARCENARIA PADRÃO DA IVECO — VER DETALHE
ESPECÍFICO"**. Esse detalhe **não veio** nas quatro pranchas.

Painel de identidade de montadora tem especificação própria — material,
iluminação, aplicação de marca, às vezes fornecedor homologado. Sem a prancha
não há o que orçar, e **não está neste valor**. Precisa ser pedido à arquiteta
antes de a proposta sair.

## ⚠️ O que a leitura das pranchas revelou

1. **Painéis com divisão DIAGONAL** (EX01 e EX03). Branco e amadeirado se
   encontram numa diagonal — 90→130 no EX01, 145→100 no EX03. Calculei pela
   área do trapézio. **O corte diagonal desperdiça chapa** e a prancha não cota
   o ângulo: conferir no CAD antes do plano de corte definitivo.
2. **O balcão da recepção não fecha entre vistas.** A vista 02 cota 220 de
   frente; a vista 01 cota 171 + 176. Adotei o desenvolvimento da **planta**
   (250 de frente + dois retornos de 90), que é a cota mais confiável.
   CONFERIR em obra.
3. **A frente amadeirada do balcão comercial tem 5 faixas** (15/18/22/18/15 num
   vão de 102) e a prancha **não diz se é ripado decorativo ou gaveteiro**.
   Orcei como frente escalonada maciça. Se forem gavetas, entram 5 pares de
   corrediça e 5 caixas.
4. **Texto × render se contradizem no espaço café** (EX04). A prancha escreve
   "bancada em MDF branco com armário em MDF **amadeirado**", e o render da
   própria prancha mostra o armário **claro**. Segui o texto.
5. **Nicho do café com cantos R26.** Moldura branca de 4 cm acompanhando raio
   de 26 sai de peça usinada, não de chapa dobrada. Perda alta, não separada
   no plano de corte.

## ⚠️ Erro que o próprio motor pegou

A primeira rodada saiu com **7 peças maiores que a chapa** — o divisor de
painel partia pela largura e deixava faixas de 208 × 260, quando a chapa é
275 × 185. Painel de parede se pagina em **faixas verticais**: a altura vira o
comprimento (até 270) e a faixa vai até 180 de largura.

Corrigido com um divisor genérico (`_partir` / `peca`). O efeito no preço foi
real: **28 → 30 chapas**, R$ 11.180 → R$ 12.660 de chapa. O amadeirado de
15 mm caiu de 77% para 51% de aproveitamento — porque um painel de 4,16 m
paginado em faixas de 1,80 sobra material, e isso é verdade na fábrica também.

> A lição: **`add()` sem conferir a chapa mente para baixo.** O aviso de
> "peças que não cabem" existia desde o motor do Carla e foi ele que pegou.

## ★ Preços adotados, sem linha na base

| Item | Adotado | Risco |
|---|--:|---|
| **Perfil em INOX** (rodapé/recuo) | R$ 85/m | a base só tem rodapé de **alumínio** a R$ 20/m, que é outro produto. São ~14 m: se o custo real dobrar, o preço sobe ~R$ 3.000 |
| **Logo IVECO aplicada** | R$ 850/un, 3 no projeto | é comunicação visual, não marcenaria. Provavelmente vem da montadora — **confirmar se entra no nosso escopo** |
| **Metalon** da bancada da janela | R$ 95/m | a prancha manda "prever estrutura em metalon interna" e não dimensiona |
| **MDF cor 25 mm** | R$ 900/chapa | a base para em 18 mm (600). Aqui pesa: são vários tampos de 3 cm |

## Fora do escopo

TVs (50" e 85") · forro modular mineral acústico · divisórias de vidro
existentes e o reforço delas · estrutura interna do dry wall · pontos elétrico,
de rede e de água · alvenaria, gesso e pintura.

## 🔒 Fechado em 25/08 [Jonathan]

> "as logos nao precisa considerar / MC de 35 com rt"

| | |
|---|--:|
| **Margem** | **MC 35%, COM RT de 10%** |
| Logos IVECO | **fora do custo** — quem fornece é a montadora |
| Custo direto | R$ 28.757 → **R$ 26.207** |
| **Investimento** | **R$ 72.400** |
| Setor Comercial · Setor Vendas | R$ 31.600 · R$ 40.800 |
| R$/m² de chapa | 648 sem RT · 806 com RT ✅ dentro da faixa |

**As três linhas de logo continuam no levantamento, a custo zero.** Zerar e
apagar são coisas diferentes: apagada, a logo sumiria do escopo e ninguém
preveria o recorte e o reforço no painel para receber a marca. A proposta diz
que o painel **prevê** a aplicação — sem cobrar por ela.

## Em aberto

1. **A prancha do painel padrão IVECO** — pedir à arquiteta. É o único buraco
   de escopo conhecido.
2. **Perfil em inox** — R$ 85/m adotado, ~14 m no projeto. Confirmar a compra.
3. **A frente de 5 faixas do balcão comercial** — ripado ou gaveteiro.

---

## 📄 Proposta gerada — 25/08

`build-deva.py` → `proposta-deva.pdf`, **4 páginas A4**.

| Página | Conteúdo |
|---|---|
| 1 | Capa — 9 conjuntos em 2 setores, prazo, validade |
| 2 | Escopo do setor Comercial (5 conjuntos) |
| 3 | Escopo do setor Vendas (4) + totais por setor + investimento |
| 4 | Especificação técnica, pagamento e não incluso |

**Os valores são LIDOS DO MOTOR, não transcritos.** O `build-` roda o
`corte-deva.py`, extrai por regex o investimento, os dois setores e o valor de
cada conjunto, e falha na hora se a soma não fechar. Transcrever nove valores à
mão entre dois arquivos é como um número erra sem ninguém perceber.

### Auditoria antes de entregar

| Verificação | Resultado |
|---|---|
| Geometria — nada colado no rodapé | ok |
| Numeração dos conjuntos 01–09, sem repetir | ok — a 1ª rodada saiu 01,01,02,02,02 porque eu usava o código da prancha |
| Total com moeda | ok — a 1ª rodada imprimia "72.400" sem R$ |
| Soma dos conjuntos = investimento | ok, por `assert` |
| **Regra 2** — sem chapa, aproveitamento, custo, margem | LIMPA |
| **Buraco de escopo nomeado no "não incluso"** | ok, é o 1º item da lista |

### Regra 1 — duas exceções registradas

O auditor pegou **"frisos usinados de 1 cm"** e **"bit de 1 cm no encontro com
a alvenaria"**. Mantive as duas: são **especificação de acabamento**, da mesma
natureza que "fita ABS", "LED 3000 K" ou "vidro temperado" — não são cota de
móvel, que é o que a regra proíbe. As duas estão nomeadas no auditor como
exceção, para que uma cota de verdade não passe amanhã sob a mesma desculpa.

⚠ **PRAZO (75 dias) e PAGAMENTO são premissas minhas** — o Jonathan não fechou
nenhum dos dois para este job.
