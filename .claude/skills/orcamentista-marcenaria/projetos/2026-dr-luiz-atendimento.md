# Dr. Luiz — novo espaço de atendimento (advocacia)

**Entrada** 04/08/2026 · escopo, valores e estruturação **ditados pelo Jonathan**.
**Motor** `build-dr-luiz.py` — proposta em 4 páginas.

> ⚠️ **EXCEÇÃO DE MÉTODO, como no Porto Verde V2.** Este orçamento **não passou pelo
> motor**. Não há projeto executivo, não há render e não há uma única cota. O preço
> (R$ 27.000) e as condições foram definidos comercialmente; o meu papel foi montar a
> proposta. Não existe conferência de MC porque não existe quantitativo.

## Escopo — 5 ambientes, 11 elementos

| Ambiente | Elementos | Qtd |
|---|---|--:|
| Salas de atendimento compactas (2) | revestimento parcial de bancada de pedra existente + bancada acoplada | 4 |
| Sala principal | revestimento da bancada existente + bancada nova | 2 |
| Sala de apoio | 2 bancadas suspensas | 2 |
| Copa | armário inferior sob a pia + armário superior + torre de apoio | 3 |
| | **Total** | **11** |

A torre da copa tem vãos dedicados a **frigobar · cafeteira · micro-ondas · armazenagem**.

## Especificação

- **Revestimento:** MDF melamínico fosco — **sem a linha acetinato e sem a linha Aris**.
- **Bancadas:** tampo de **45 mm**, borda **arredondada**, raio usinado na peça,
  **sem acabamento chanfrado**.
- **Estrutura:** pé em **serralheria** com **pintura eletrostática fosca**.
- **Pedras existentes:** mantidas. A marcenaria reveste as faces aparentes.

## Comercial

| | |
|---|---|
| **Investimento** | **R$ 27.000** |
| Pagamento | **50% na assinatura + 50% na entrega** |
| Prazo | **45 dias corridos** |
| Garantia | **5 anos** em contrato — estrutura, montagem, acabamento e instalação |
| Validade | 15 dias corridos |

## 📄 Proposta — 4 páginas

`capa tipográfica · escopo · técnico · investimento`

**Capa tipográfica** (`.cover-t`), reaproveitada do Porto Verde V2 — não há render nem
foto do espaço. Gradientes radiais dourados sobre fundo escuro, com a régua vertical.

**Página 2** fecha com o argumento do conjunto: *são 11 elementos em cinco ambientes, e
quem atravessa o espaço precisa enxergar um conjunto, não cinco compras separadas.* É o
que justifica a repetição de cor, borda e pé em todos os móveis.

**Página 3** transforma cada exigência técnica em benefício: a borda arredondada é a
quina que não machuca nem lasca; a pintura eletrostática é curada em estufa e não
descasca no encosto da cadeira. Fecha com a observação de que num espaço de atendimento
**a bancada é a primeira coisa que o cliente toca ao sentar**.

**Página 4** traz o valor, o 50/50 desdobrado (o que cada metade libera) e os três
passos até a entrega.

## ✏️ Correções [Jonathan 04/08]

| # | Correção | Onde |
|---|---|---|
| 1 | **Garantia vitalícia da ferragem — fora.** *"Nunca fez parte do nosso escopo."* | tabela técnica, p.3 |
| 2 | Bloco **Incluso / Não incluso / Medição** removido inteiro | p.4 |
| 3 | Garantia **10 anos → 5 anos** | `.warr` p.3 + `.cond` p.4 |
| 4 | **Expor 45 mm** de espessura da bancada | `.det` p.2 + tabela técnica p.3 |
| 5 | **"Cor única nos cinco ambientes"** removido | tabela técnica, p.3 |

> A correção 1 **não era só desta proposta.** A mesma frase estava no **Apto CJ**
> (4 ocorrências) e nos **quartos Mateus & Manuela** (2) — os dois já entregues.
> Corrigi os geradores e reemiti os PDFs; o argumento de ferragem agora se apoia em
> **ciclos testados, amortecimento e regulagem**, não em garantia. A regra ficou
> registrada em `referencias/ferragens.md` para não voltar.

> A remoção do bloco Incluso/Não incluso abriu 30 mm na p.4. Em vez de deixar o vazio,
> redistribuí: caixa de investimento maior (número a 54pt), respiro maior entre as
> condições e os três passos.

## 🖼️ A única imagem — detalhe da borda [Jonathan 04/08]

`img/borda-arredondada-45mm.png` · pé da **p.3**, **92 × 58 mm**, ao lado do texto que
argumenta a borda.

A proposta era 100% tipográfica por falta de material. A imagem entrou na p.3 — que é
exatamente a página do assunto — emparelhada com o parágrafo *"a bancada é a primeira
coisa que o cliente toca"*. A legenda foi para a coluna de texto, não embaixo da foto:
como `figcaption` ela descia **6,7 mm dentro do rodapé**.

**Duas versões.** A primeira tinha 153 × 154 px e só aguentava 34 mm. A segunda
(1024 × 1031) permitiu subir para **92 mm** e mostra *duas* especificações de uma vez:
a **borda arredondada com o tampo espesso** e o **pé cilíndrico em pintura fosca**.

### Tratamento da imagem

Recortada para `(0, 225) → (1024, 872)` — 1024 × 647, proporção 1,58:1. O corte é de
composição (aperta no encontro tampo/pé e corta piso vazio), e resolve dois defeitos
de brinde:

| Defeito | Onde estava | Saiu por |
|---|---|---|
| **Marca d'água ✦ do Gemini** | x 880–925, y 885–935 | corte inferior (y < 872) |
| 3 blocos quadrados de artefato sobre o tampo | y 48–64, 171–176, 208–218 | corte superior (y > 225) |

> ⚠️ **A imagem é gerada por IA, não é foto de peça nossa.** A marca d'água do Gemini
> estava lá; ela saiu no recorte de composição, mas **o fato não sai** — vale saber o
> que está indo para o cliente. Como ilustração de especificação (é o que a legenda diz)
> funciona; como "olha um móvel que fizemos", não é verdade.

> ⚠️ **A mesa da foto é preta e a cor do projeto ainda não está definida** (item 2 do
> *Aberto*). A foto pode ser lida como compromisso de cor. Se o padrão escolhido não for
> escuro, trocar a imagem antes de enviar.

Folgas finais: 17,2 / 10,3 / 12,5 / 29,9 mm.

## ⚠️ Aberto

1. **Nenhuma medida.** Não há cota de bancada, de vão da copa nem de altura. A proposta
   traz a ressalva de medição no corpo do texto, mas **o preço está travado antes do
   levantamento** — se o espaço for maior que o imaginado, não há proteção contratual
   além dessa frase.
2. **Cor não definida.** A especificação diz "melamínico fosco, sem acetinato e sem
   Aris" — falta o padrão exato. Não muda o custo de chapa (mesma linha), mas precisa
   ser fixado antes da compra.
3. **Sem MC apurada.** Sem quantitativo não dá para dizer se R$ 27.000 cabe. Para
   referência: são 11 elementos, e o piso de MC do Rodrigo é 37%.
