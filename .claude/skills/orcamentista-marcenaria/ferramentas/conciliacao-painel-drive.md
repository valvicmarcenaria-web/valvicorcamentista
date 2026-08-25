# Conciliação — painel × repositório × Drive  [04/08/2026]

Auditoria de **todos** os orçamentos: o que está no painel, o que está no repositório
(`projetos/*.md`) e o que está no Drive (`valvicmarcenaria@gmail.com`).

> **A conta do Drive mudou.** Nas sessões anteriores o conector apontava para
> `clubedoplanejado@gmail.com` e nada da Valvic aparecia. Agora está em
> `valvicmarcenaria@gmail.com` e o acervo inteiro está acessível — foi o que permitiu
> esta conciliação.

## Estrutura do Drive

```
Orçamentos Valvic/
  └── Em aberto/          leonardo_mirante · romulo · Nura · hotel_ibis · juliana
                          junior - Lagoa santa · carla_dresller · projeto_fabio
CLIENTES VALVIC/          (compartilhada por producaovalvic@gmail.com)
  └── Tania · Cristiane · Ana Carolina · Alexandrina · Bernardo
      Carla dressler · Simony - Buritis
sistema_valvic/           apps · financeiro · fluxograma
```

## ✅ Adicionados ao painel — 7 orçamentos que existiam e não estavam lá

| Cliente | Ref. | Máx. | Onde estava | Observação |
|---|--:|--:|---|---|
| **Júnior — Lagoa Santa** | 370.000 | 395.000 | Drive (doc 18/06) | Casa completa, 9 ambientes, Res. Bouganville. **2º maior da carteira** |
| **Quartos Mateus & Manuela** | 93.800 | 104.200 | repo (fechado hoje) | A Urbanística · 11 móveis |
| **Rômulo** | 39.000 | 58.400 | Drive (PDF 09/07) | Apto 4 amb · 3 níveis de ferragem |
| **Simony — Buritis** | 34.850 | — | Drive (contrato) | **Contrato assinado** — não era orçamento, era venda fechada |
| **Karina Ramos** | 17.500 | 21.500 | repo + Drive | Estava em PARADOS "a consultar", mas a proposta Gold/Silver está fechada |
| **Regina Godinho** | 13.100 | — | Drive (doc 16/06) | Escritório · cliente recorrente, 3º projeto |

**Impacto:** 19 → **25 orçamentos** · R$ 1.641.166 → **R$ 2.209.416** (+R$ 568.250,
+35%).

> A **Clínica Nura** (R$ 85.150 / 92.550) foi levantada na auditoria e **retirada em
> seguida — proposta perdida** [Jonathan 04/08]. A proposta e os 3D continuam no Drive
> em `Orçamentos Valvic/Em aberto/Nura`; se o cliente voltar, o material está lá.

## 🚦 Status reais [Jonathan 04/08]

O painel passou a ter **três estados** em vez de dois. Antes só existia
`concluido` (verde) e `entregue` (azul); uma proposta parada ficava indistinguível de
uma em negociação ativa.

| Estado | Cor | Significado | Total |
|---|---|---|--:|
| `concluido` | verde | vendido / contrato assinado | 8 · R$ 757.645 |
| `entregue` | azul | proposta entregue, em negociação | 15 · R$ 1.395.271 |
| `parado` | âmbar | entregue, sem previsão ou sem retorno | 2 · R$ 56.500 |

Decisões desta rodada:

| Cliente | Antes | Agora |
|---|---|---|
| Clínica Nura | entregue | **removida** — perdida |
| Rômulo | entregue | **parado** — sem previsão |
| Simony — Buritis | concluido | **fechado** ✓ (confirmado) |
| Karina Ramos | entregue | **parado** — sem retorno |
| Regina Godinho | entregue | **fechado** ✓ |

A faixa de indicadores no topo agora mostra os três valores lado a lado, e a contagem
de pendências de Drive foi para o rodapé.

## 🔁 PARADOS reconstruído

Antes trazia só "Karina Ramos — a consultar", que na verdade tinha proposta fechada.
Agora lista os leads com **escopo de venda registrado no Drive e sem orçamento fechado**:

`Cristiane · Ana Carolina · Tania · Bernardo · Carla Dressler · Marina · Alexandrina`

São 7 pastas com projeto ou escopo recebido e nenhum número. É a fila real de trabalho.

## ✔️ Já existia e foi mantido — 19 entradas

Kênia & Fábio · Casa L&M · Resolve Consórcio · Lilian Lee · Kairon & Juliana ·
SPE Nova Lima 1 · Aline Sanches · Apto CJ · TRT 3ª Região · Jairo Samuel ·
Porto Verde · Ed. Luxemburgo · Raquel · Camila · Graça · Hotel Ibis ·
Flávia Moacir · Lirriet Libório · Maria.

## ⚠️ Achados que precisam de decisão

1. **O HANDOFF do Juninho estava errado.** `HANDOFF-juninho-lagoa-santa.md` diz que
   *"o orçamento do Juninho não foi encontrado neste repositório"* e manda localizá-lo.
   Ele **existe no Drive desde 18/06** — R$ 395.000, com breakdown por ambiente,
   condições fechadas e proposta em 6 páginas. As três instruções pendentes do handoff
   (serralheria da cozinha ~R$ 900, ferragens Hettich, sem versão Hardt) **já estão
   aplicadas** no documento do Drive. O handoff pode ser encerrado.

2. **Lucas e Ana — Apto 101 (2025), R$ 181.800 Gold.** Não foi adicionado. O material
   está em `fontes/` com prefixo `exemplo_` e o dossiê o descreve como o caso que ensina
   o método. Se for cliente real e não material de treino, entra e move o total para
   R$ 2.476.366. **A confirmar.**

3. **Rômulo tem três colunas de preço** (43.300 / 48.300 / 58.400, e −10% no fechamento
   dos 4 ambientes: 39.000 / 43.500 / 52.600). Lancei o piso à vista (39.000) e o teto
   de tabela (58.400). Se ele fechou numa coluna específica, corrigir.

4. **Coluna `drive`.** Marquei `ok` para tudo que tem pasta com proposta no Drive.
   Os quartos Mateus & Manuela e os demais projetos recentes do repositório seguem
   `ausente` — os PDFs estão só no Git.

---

## Rodada 2 — 04/08/2026 (fim do dia)

| Cliente | Antes | Agora | Motivo |
|---|--:|--:|---|
| **Cristaleira** | — | **7.500** | Nova. Peça única, preço fechado |
| **Apto CJ** | 76.100 / 84.600 | **48.700** | Cliente escolheu a **opção 4** — o leque de 6 virou um número |
| **Quartos Mateus & Manuela** | 93.800 / 104.200 | **88.800 / 98.700** | MC 40→35% e o painel da Manuela que faltava |

**26 → 27 orçamentos** · R$ 2.236.416 → **R$ 2.211.516**. O total caiu R$ 24.900 e isso
é bom: era pipeline que não existia. O Apto CJ estava lançado pelo cenário integral
(R$ 76.100) e a cliente fechou no de R$ 48.700 — carregar os R$ 27.400 de diferença
seria inflar a carteira com uma venda que não vai acontecer naquele valor.

## ⚠️ Ainda pendente — a pasta "Em aberto" tem 20 pastas, não 8

A rodada 1 registrou só o que apareceu na primeira página da listagem do Drive.
Listando por `parentId`, a pasta tem **20 subpastas**. Estas **não estão no painel** e
não têm valor levantado:

`Clínica Dermato-Nutrologia (Dra. Esther / Dra. Sarah)` · `Mônica Cristina — Banheiros
(Social + Suíte)` · `Cabeceira em couro — Valdenir & Maria (Paula Galante)` ·
`Sala Bia & Matheus (arq. Giovanna Camisassa)` · `Samara — Quarto dos Irmãos
(consultoria Rizzi)`

Algumas têm proposta pronta lá dentro (a da Mônica tem `Proposta-Monica-Banheiros.html`
e `orcamento-monica-v2-mc37.json`). **Vale abrir uma a uma e lançar** — é a mesma
situação que na rodada 1 revelou R$ 568 mil de carteira não registrada.

---

## Rodada 3 — 25/08/2026 · a pendência da rodada 2 foi fechada

A rodada 2 terminou com um aviso em aberto: *"a pasta Em aberto tem 20 pastas,
não 8 — vale abrir uma a uma e lançar"*. Abri. São **23 subpastas**, e cinco
delas tinham orçamento levantado e nunca entraram no painel.

| Cliente | Ref. | Máx. | Onde estava | O que é |
|---|--:|--:|---|---|
| **Lucas e Ana · apto 101** | 169.950 | 181.800 | `fontes/` (2025) | Apto 168,61 m², executivo de 84 pranchas A3 · Silver/Gold · **⚠ a confirmar, ver abaixo** |
| **Clínica Dermato-Nutrologia** | 43.200 | 47.000 | Drive · 2 JSON + proposta | 6 ambientes · cenário HPL × cenário Itapuã com paredes revestidas |
| **Samara · quarto dos irmãos** | 37.500 | — | Drive · JSON v3 travado | Consultoria Luana Rizzi · MC real ~40,4% |
| **Sala Bia & Matheus** | 36.000 | 70.000 | Drive · BASE.md + 2 JSON | arq. Giovanna Camisassa · melamínico × lâmina natural Freijó |
| **Valdenir & Maria** | 8.500 | 20.000 | Drive · 3 JSON | designer Paula Galante · cabeceira em 3 acabamentos + lavanderia |
| **Mônica Cristina · banheiros** | 15.400 | — | Drive · JSON v2 + proposta | parceira Rubia · social + suíte, otimizados juntos |

**35 → 41 orçamentos** · R$ 3.000.816 → **R$ 3.311.366** (+R$ 310.550).

### Duas correções ao mapa da rodada 2

1. **A "Cabeceira em couro — Valdenir & Maria" não tem pasta própria.** Ela mora
   dentro da pasta chamada **`Maria`** — a mesma que o painel já usava para o
   job "Maria · Lavanderia R$ 7.850". São **coisas diferentes** com nome
   parecido: o `orcamento-cabeceira-couro-valdenir-maria.json` é de Valdenir &
   Maria via Paula Galante, no Vale dos Cristais, e traz cabeceira **e** uma
   lavanderia de R$ 6.500 fechada pelo fundador. Lancei como linha própria.
   ⚠ **Confirmar se a "Maria · Lavanderia" do painel não é essa mesma lavanderia
   lançada duas vezes.**
2. **A Samara tem duas propostas no Drive**, não uma: `Quarto-dos-Irmaos` e
   `Bancada-e-Guarda-roupa`. O JSON travado (R$ 37.500) é do escopo cheio. O da
   bancada é escopo reduzido e **o valor não foi capturado** — o conector não lê
   HTML e o snippet do Drive para em 5.000 caracteres, que o CSS consome inteiro.

### Como os valores foram extraídos sem baixar arquivo

O conector devolve base64 (inútil aqui) e `read_file_content` não aceita
`application/json` nem `text/html`. O caminho que funcionou:

```
search_files SEM excludeContentSnippets → contentSnippet de ~5.000 caracteres
```

Os JSON de orçamento começam por `cliente / projeto / versao / inv / mcAlvo`,
então o snippet pega o valor logo na primeira linha. **Com HTML não funciona:**
o `<style>` come os 5.000 caracteres antes de chegar no corpo. Quando o
resultado estoura o limite de tokens, ele é salvo em arquivo — e aí `jq`/python
local resolve. Foi assim que li os snippets todos de uma vez.

### ⚠️ A linha do Lucas e Ana é a única decisão em aberto

A pendência nº 2 da rodada 1 dizia *"se for cliente real e não material de
treino, entra"*. Lancei porque o pedido foi lançar **todos**, mas com o alerta
escrito na própria linha e status **`parado`**, não `entregue` — é proposta de
nov/2025 sem retorno registrado. **Se for caso de treino, a linha sai e a
carteira cai R$ 169.950.**

### Faixa do cabeçalho: faltava um quarto estado

O painel tinha quatro status (`concluido` · `entregue` · `orcado` · `parado`) e
a faixa só mostrava três. Os **R$ 495 mil em `orcado`** — Eliuton, Carla,
Vinícius e Luciana, o trabalho mais recente da casa — entravam no total e
sumiam da leitura por estado. Criei o slot e, junto, um guarda:

```js
const _porEstado = ["concluido","entregue","orcado","parado"].reduce((a,st)=>a+soma(st),0);
if (_porEstado !== total) console.warn("painel: faixa não fecha com o total", …);
```

Se amanhã alguém criar um status novo e esquecer o slot, o console avisa em vez
de o dinheiro sumir em silêncio. Hoje fecha: 758 + 1.832 + 495 + 226 = 3.311.

### O que ficou de fora, de propósito

- **Clínica Nura** (85.150 / 92.550) — proposta perdida, retirada em 04/08 pelo
  Jonathan. Continua no Drive; se o cliente voltar, o material está lá.
- **Os 7 de PARADOS** (Cristiane · Ana Carolina · Tania · Bernardo ·
  Carla Dressler · Marina · Alexandrina) — têm escopo no Drive e **nenhum
  número**. Varri a pasta atrás de `orcamento*.json` e de propostas: não há.
  Entrar no painel com valor zero seria inventar carteira.
- **O rótulo do topo** continua dizendo *"Valor total fechado"* sobre um número
  que soma fechado + negociação + orçado + parado. Está errado desde antes desta
  rodada e não mexi por conta própria — é leitura de decisão do fundador.
