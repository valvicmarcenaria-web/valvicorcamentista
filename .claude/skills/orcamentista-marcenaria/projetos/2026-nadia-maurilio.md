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
| Desconto especial · 12% | −15.342,00 |
| **TOTAL** | **R$ 112.508,00** |

**Pagamento 20 · 20 · 20 · 40** — fechamento · 60 dias · início das montagens ·
**entrega final**. Três de R$ 22.501,60 e a última de **R$ 45.003,20**.
Ferragens **Blum** · garantia **20 anos** · entrega **90 a 120 dias** ·
validade **sexta, 14/08/2026** (emitida terça, 11 — janela de 3 dias).

## As 8 páginas
capa (colagem) · **a oportunidade** (página escura, as 4 alavancas + faixa de preço) ·
**ferragem Blum** (3 SVGs de mecanismo) · lavanderias e corredor · cozinha ·
closet · construção (espessuras cotadas) · investimento.

## 2ª rodada de ajustes [Jonathan 11/08]

| | De | Para |
|---|---|---|
| Desconto | 15% | **12%** |
| Parcelas | 5 × 20% | **20 · 20 · 20 · 40** |
| Corrediça | MOVENTO | **TANDEM com BLUMOTION** |
| Armário do corredor | — | **sem Blum** |

> ⚠️ **"Última parcela com os 40% restantes" não disse em qual marco.** Adotei
> **ENTREGA FINAL** — a parcela pós-obra sai do contrato. Leitura conservadora: os
> 40% ficam amarrados à nossa entrega, não ao cronograma de obra do cliente. Se a
> intenção era manter o marco pós-obra, é trocar uma linha em `PARCELAS`.

### O armário do corredor não leva Blum — e isso é construtivo, não corte
As portas de espelho correm na **esquadria de alumínio**, que tem sistema próprio.
Não há ferragem Blum a aplicar ali. A proposta diz isso em três lugares (descritivo
do item, página da ferragem e nota de inclusos) e o selo da capa deixou de dizer
"100% Blum" — passou a dizer só **"Blum"**.

> **Aprendizado:** um selo de "100% X" na capa vira dívida na hora em que aparece
> a exceção. Nomear a exceção custa uma linha; ser pego custa a confiança da peça.

## ⛔ O QUE EU NÃO CONSIGO GARANTIR

**Não existe levantamento para este job.** Não há `corte-nadia.py`, não há plano de
corte, não há MC conferida — os valores vieram prontos do `nadia_v3.pdf`.

### O que o desconto custa, em pontos de MC
`div_novo = div_antigo / (1 − desconto)` — a receita cai, o custo não.

| MC de partida | após −15% *(1ª rodada)* | após −12% *(atual)* |
|--:|--:|--:|
| 30% | 21,2% ⛔ | **23,2%** ⛔ |
| 35% | 27,1% ⛔ | **28,9%** |
| 40% | 32,9% | **34,5%** |
| 45% | 38,8% | **40,2%** |

> **Para sobrar 28% (o piso da casa), o job precisava ter sido precificado a no
> mínimo MC 34,2%** — era 35,8% com os 15%. Os três pontos de desconto a menos
> compraram 1,6 ponto de folga.

### As duas mudanças aliviaram a exposição
- **TANDEM em vez de MOVENTO** é a corrediça oculta clássica da Blum, bem abaixo da
  MOVENTO no custo. Mesma família, mesmo argumento de mecanismo (undermount,
  extração total, BLUMOTION).
- **Sai a parcela pós-obra.** Os R$ 45.003,20 passam a vencer na **nossa** entrega,
  numa data que controlamos.

Continua valendo: o Blum é custo por cima de um número não auditado. No documento de
origem a diferença entre as colunas *com* e *sem* ferragens era **R$ 23.450**, a
preço de venda. Cada R$ 10 mil de custo a mais tira ~9 pontos de MC sobre os
R$ 112.508.

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
3. **O marco da parcela de 40%** — entrega final (adotado) ou pós-obra.


---

# 📋 MEMORIAL DESCRITIVO PARA VALIDAÇÃO [Jonathan 11/08/2026, 3ª rodada]

**Motor** `build-nadia-memorial.py` → `memorial-nadia.pdf`, **4 páginas**.
Documento **técnico**, sem marketing, para a cliente conferir item a item e assinar
o aceite. É peça separada do folder comercial.

**4 páginas:** escopo parte 1 (lavanderias + hall) · escopo parte 2 (cozinha + suíte) ·
padrões construtivos (acabamentos, espessuras, ferragens, LED, não-incluso) ·
investimento, pagamento e **bloco de aceite com assinatura**.

## O que mudou no escopo

| | |
|---|---|
| ➕ **Cristaleira 2** | ao lado da torre da geladeira · **2 portas em vidro reflecta bronze** |
| ➕ **Painel de TV** | volta ao projeto, em MDF Itapuã |
| 🔄 **Closet** | Areia → **100% MDF Gianduia Trama** |
| 🔄 **Cozinha** | detalhes amadeirados nomeados: **MDF Itapuã** |
| ➕ **LED** | **fornecimento e instalação Valvic**, declarado |
| 💰 **Valor** | **R$ 112.500** · pagamento 20 · 20 · 20 · 40 |

> ⚠️ O Jonathan escreveu "reflecta **fumê**" e corrigiu em seguida para **reflecta
> bronze**. Vale bronze — e é coerente: a Cristaleira 1 já é reflecta bronze com
> esquadria de alumínio bronze. Fumê teria criado dois vidros diferentes na mesma
> cozinha.

## ⚠️ O ESCOPO CRESCEU E O PREÇO NÃO

| | |
|---|--:|
| 7 conjuntos (tabela) | 127.850 |
| + painel de TV (volta) | 2.250 |
| **= tabela conhecida** | **130.100** |
| + cristaleira 2 | **não orçada** |
| + closet Areia → Gianduia Trama | **delta não orçado** |
| **Preço** | **112.500** |

**O desconto efetivo sobe de 12,0% para 13,5% só com o painel de TV.** Com a
cristaleira nova a um valor coerente com a Cristaleira 1 (R$ 5.650 por 80 cm e
3 portas → ~R$ 4.000 por 2 portas), vai para **~16%**. E ainda falta o delta do
Gianduia Trama sobre o closet inteiro, que é o segundo maior item da proposta
(R$ 36.700 de tabela em Areia).

> Continua valendo o de sempre neste job: **não há levantamento**, então nada disso
> é auditável. Cada acréscimo entra sobre um número que não conheço por dentro.

## 🚨 O FOLDER COMERCIAL FICOU DESATUALIZADO

`proposta-nadia-premium.pdf` ainda traz **7 conjuntos, R$ 112.508 e closet em Areia**.
O memorial traz **9 conjuntos, R$ 112.500 e closet em Gianduia Trama**. **Os dois não
podem circular juntos.**

Não realinhei o folder porque a página de investimento dele é construída sobre a
**tabela item a item + desconto**, e eu teria que inventar valor para a Cristaleira 2
e para o upgrade do closet. Precisa do valor de tabela dos dois — ou autorização para
o folder passar a mostrar só o total, como o memorial faz.

## Segue aberto
1. **Levantamento.** Continua sendo o que resolveria a questão da margem.
2. **Largura da Cristaleira 2** — o memorial declara "a confirmar na medição".
3. **Lavanderia superior** — a célula em branco do documento de origem.
4. **Realinhar o folder comercial** com o escopo novo.
