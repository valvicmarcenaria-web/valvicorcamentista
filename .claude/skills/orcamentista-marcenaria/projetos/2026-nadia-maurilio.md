# Nádia e Maurílio — retomada de negociação

**Entrada** `nadia_v3.pdf` — *"Proposta especial para Nádia · reduzida versão 2"*.
Projeto no Drive: `1KFYG8_lzf7kVvn5dZ8MdpbcoAU3k_ije`.
**Motor** `build-nadia.py` — proposta em 6 páginas.

> ⚠️ **TAREFA ATÍPICA [Jonathan 06/08/2026] — não é padrão de método.** O escopo e os
> dois valores vieram prontos. Não houve levantamento, plano de corte nem conferência de
> MC. Meu papel foi **organizar e apresentar**, não orçar.

## As duas colunas

| Serviço | Com ferragens | Sem ferragens |
|---|--:|--:|
| Lavanderia térreo | 5.850 | 4.800 |
| Lavanderia superior | **5.850** ⚠ | **4.800** ⚠ |
| Hall dos dormitórios | 6.300 | 5.700 |
| Cozinha · ilha e geladeiras | 15.100 | 11.800 |
| Cozinha · cristaleira | 5.650 | 4.800 |
| Cozinha · bancada | 52.400 | 41.300 |
| Cozinha · painel de TV | 2.250 | 2.250 |
| Suíte master · closet v2 | 36.700 | 31.200 |
| **TOTAL** | **130.100** | **106.650** |

Diferença: **R$ 23.450** — é o que as ferragens custam com fornecimento, conferência e
garantia nossas.

> ⚠️ **O único número que não veio do documento.** No `nadia_v3.pdf` a linha
> **Lavanderia superior** traz a descrição *"Idem lavanderia"* e a **célula de valor em
> branco**. Adotei 5.850 / 4.800, igual ao térreo — leitura literal de "idem" para uma
> unidade idêntica. **Conferir antes de enviar:** se a superior tiver medida diferente ou
> se já estiver embutida no térreo, os totais mudam.

> O **painel de TV** repete R$ 2.250 nas duas colunas, e está dito na proposta: não tem
> ferragem, então não há o que retirar. Sem essa nota, a linha pareceria erro.

| | −5% · 4× boleto | −10% · à vista |
|---|--:|--:|
| Com ferragens | **123.595** (4 × 30.898,75) | **117.090** (entrada 81.963,00) |
| Sem ferragens | 101.317,50 (4 × 25.329,38) | 95.985 (entrada 67.189,50) |

Primeiro boleto para 60 dias · à vista = 70% de entrada + saldo na entrega final.

## A cláusula de responsabilidade (p.6)

Caixa escura, título próprio, quatro itens: **pedido e especificação · notas fiscais ·
logística · ocorrências** (falta, atraso, peça errada, avaria, defeito, troca e garantia
junto ao fabricante). Fecha com o **efeito no prazo e na garantia** — a instalação só
ocorre com as ferragens no local, e a garantia Valvic **não alcança ferragem de
terceiro** nem o que ela causar na peça. Está firme sem ser hostil: descreve o que passa
a ser dela, não o que ela vai errar.

## Decisões de layout

**Ferragens em SVG desenhado, não em foto de catálogo.** A política de rede do ambiente
bloqueia hosts externos — tentei e o proxy devolveu 403. Mas o desenho acabou sendo a
escolha melhor: os três blocos mostram **mecanismo**, que é o argumento. A corrediça
oculta aparece *por baixo* da gaveta; o Blum HK-S aparece com o **arco do curso e as
posições intermediárias**, que é exatamente o que se está vendendo; o RM280 aparece em
corte, mostrando a mão entrando no perfil. Foto de produto não diz nada disso.

**Estrutura em corte cotado** — 15 caixaria · 18 prateleira · 6 fundo · 18 porta, cada
espessura com o motivo. O argumento: *a diferença entre 15 e 18 numa prateleira não
aparece na entrega, aparece três anos depois — por isso está escrita, para poder ser
cobrada.*

**Capa tipográfica.** Os renders disponíveis são as 3 faixas da capa do `nadia_v3.pdf`,
recortadas em 8 imagens de **254×211 a 419×384 px**. Numa capa A4 sangrada isso daria
~30 dpi. Entraram em 52 mm na página de escopo, onde seguram. **O PDF do projeto
completo no Drive tem 1 GB** e não é transferível neste ambiente — se houver renders
soltos em resolução maior, a proposta melhora bastante.

## ✏️ Correções [Jonathan 06/08]

| | |
|---|---|
| **Capa** | ganhou colagem de fotos — cascata assimétrica sangrando na borda direita, com réguas douradas e véu para a tipografia. Assinatura no topo, nome no pé |
| Fornecimento | *"Pedido e especificação — modelo, linha e quantidade exatos"* → só **"Pedido."** |
| Logística | saiu *"das peças na data da montagem"* |
| Garantia terceiros | saiu *"inadequada"* — ficou "os desdobramentos **delas** sobre a peça" |
| **Garantia** | **10 anos** (era 5) |
| Fundo 6 mm | **em todo o mobiliário**, não só na lavanderia — lá é o *duplo revestimento* que é exclusivo |
| Hall dos dormitórios | esquadria em **alumínio** (não bronze), para acompanhar o tom do espelho |

> A cristaleira **mantém alumínio bronze** — lá o perfil acompanha o vidro reflecta
> bronze, não o espelho prata. São dois critérios diferentes na mesma proposta.

## ⚠️ A confirmar

1. **Lavanderia superior** — o valor em branco no documento de origem.
2. ~~Garantia~~ — **resolvido: 10 anos** [Jonathan 06/08]. Fica o registro de que
   Dr. Luiz e cristaleira saíram com **5**. Definir qual é o padrão da casa.
3. **Renders em resolução maior**, se existirem fora do PDF de 1 GB.


---

# 🔥 FOLDER PREMIUM — proposta comercialmente agressiva [Jonathan 11/08/2026]

**Motor** `build-nadia-premium.py` → `proposta-nadia-premium.pdf`, **8 páginas**,
layout do folder do Apto CJ (`/tmp/css_premium.txt`).

## Escopo — 7 conjuntos (sai o painel de TV)

| Conjunto | Tabela |
|---|--:|
| Lavanderia do térreo | 5.850 |
| Lavanderia superior | 5.850 |
| Armário do corredor *(hall dos dormitórios)* | 6.300 |
| Cozinha · ilha e geladeiras | 15.100 |
| Cozinha · cristaleira | 5.650 |
| Cozinha · bancada | 52.400 |
| Closet do casal | 36.700 |
| **Tabela** | **127.850** |
| Desconto especial · 15% | −19.177,50 |
| **TOTAL** | **R$ 108.672,50** |

**5 × R$ 21.734,50** — fechamento · 60 dias · início da montagem · entrega final ·
**após a entrega da obra**. Ferragens **100% Blum** · garantia **20 anos** ·
entrega **90 a 120 dias** · validade **sexta, 14/08/2026** (emitida terça, 11 —
janela de 3 dias).

## As 8 páginas
capa (colagem) · **a oportunidade** (página escura, as 4 alavancas + faixa de preço) ·
**ferragem 100% Blum** (3 SVGs de mecanismo) · lavanderias e corredor · cozinha ·
closet · construção (espessuras cotadas) · investimento.

## ⛔ O QUE EU NÃO CONSIGO GARANTIR

**Não existe levantamento para este job.** Não há `corte-nadia.py`, não há plano de
corte, não há MC conferida — os valores vieram prontos do `nadia_v3.pdf`. Agora há
**três compressões empilhadas** sobre um número que não posso auditar: o desconto de
15%, o upgrade para 100% Blum e o alongamento do recebimento.

### O que o desconto de 15% custa, em pontos de MC

`div_novo = div_antigo / 0,85` — a receita cai 15%, o custo não.

| MC de partida | MC depois do −15% |
|--:|--:|
| 30% | **21,2%** ⛔ |
| 35% | **27,1%** ⛔ |
| 40% | 32,9% |
| 45% | 38,8% |

> **Para sobrar 28% (o piso da casa) depois do desconto, este job precisava ter sido
> precificado a no mínimo MC 35,8%. E isso ANTES do Blum.**

### E o Blum é custo por cima disso

No documento de origem, a diferença entre as colunas *com* e *sem* ferragens era
**R$ 23.450** — é a linha inteira de ferragem, a preço de venda. Trocar uma
especificação mista por **100% Blum** sobe esse custo de forma relevante, e sem
contagem de ferragem eu não sei quanto. Cada R$ 10 mil de custo a mais tira ~9
pontos de MC sobre os R$ 108.672,50.

### O 5º pagamento

20% = **R$ 21.734,50** entram **depois da entrega da obra** — uma data que não é
nossa. É a parcela mais exposta do contrato.

## Como a garantia de 20 anos foi tratada

`referencias/ferragens.md` proíbe vender ferragem **por garantia**. Na proposta os
20 anos aparecem como **garantia Valvic** — termo nosso, sobre o conjunto que nós
fornecemos e instalamos — e **nunca** como garantia da Blum. A ferragem, na página 3,
é argumentada por **ciclos testados, amortecimento e regulagem em três eixos**,
exatamente como a referência manda.

> ⚠️ Ainda assim: **20 anos é 4× o melhor número da tabela corrigida da casa**
> (telescópica 2 · oculta Hardt 5). Decisão comercial do Jonathan, registrada.

## Segue aberto
1. **Levantamento.** É o que resolveria tudo acima. Proposto ao Jonathan.
2. **Lavanderia superior** — a célula em branco do documento de origem. A proposta já
   declara que o valor é revisto se a medida diferir.
