# Quantitativo de materiais — metodologia (em revisão)

> ⚠ **PRELIMINAR — aguardando explicação da Valvic.** Este documento registra
> os **artefatos reais** lidos (plano de corte e lista de materiais do projeto
> Maria – Vale dos Cristais). As **interpretações de metodologia** abaixo
> (especialmente "dois níveis" e a regra de estimativa) podem estar incorretas
> e serão corrigidas. Os *dados* são fiéis; as *conclusões*, não confirmadas.

## O cerne é a LISTA DE PEÇAS — extraída à mão (método tradicional)

> **Correção da Valvic:** a lista de peças **não sai de software**. Ela é tirada
> **manualmente**, do jeito tradicional da marcenaria — *"riscando na régua"*:
> olhando o projeto e **decompondo o móvel peça por peça**, definindo as
> dimensões (C × L) e a espessura de cada uma. **Essa é a habilidade central a
> destilar.** O software de plano de corte só entra **depois**, para encaixar
> (nesting) a lista já pronta nas chapas.

### Como a Valvic faz (a aprender em detalhe)

> 🟡 **A SER ENSINADO pela Valvic.** Registrar aqui o método de leitura do
> projeto e de quebra do móvel em peças (caixaria, fundos, frentes, prateleiras,
> gavetas...), as folgas, os critérios de dimensão e como se anota.

## Depois: o software faz o nesting (plano de corte)

Com a lista de peças pronta, o **otimizador de corte** encaixa as peças em
chapas de **2750 × 1850 mm** e devolve, por chapa:

- **Tipo / espessura / cor** (ex.: MDF Branco 15, Nuvem Matt 15mm, Nuvem Matt 6mm);
- **Qtd de peças** encaixadas e o layout do corte;
- **% utilizado** (aproveitamento) — varia de ~7% a ~92% por chapa;
- **Metros de filetamento** (fita de borda) daquela chapa.

O **nº de chapas** do projeto = nº de chapas que o nesting precisou. Exemplo
real (Maria – Vale dos Cristais, Ambiente 1, código 0ED321): **7 chapas MDF
Branco 15 + 4 chapas Nuvem Matt 15mm + 1 chapa Nuvem Matt 6mm = 12 chapas**.

### Taxonomia de peças (papel de cada peça no corte)

Cada peça carrega seu papel: `Função - Grupo - Módulo`. Vistos no plano de corte:

- **Estrutura:** Painel / Cabeceira, Lateral Direita/Esquerda, Base (passante),
  Batedor Topo (traseiro), Fundo.
- **Prateleiras:** Prateleira.
- **Gaveta:** Fundo interno, Contra-frente, Posterior, Lateral.

> Espessuras seguem o padrão Valvic (estrutura 15mm, fundos 6mm, etc. — ver
> `chapas.md`).

## ⛔ Itens que NUNCA entram por "área de painel" — orçar como ITEM PRÓPRIO (cravado 17/06/2026)

> **Erro cravado:** na estimativa Fase-1 do Junior (Lagoa Santa) eu diluí as
> **portas de passagem** na área de painel raso (multiplicador genérico). Subdimensiona.
> Porta de passagem **não é painel liso** — é um conjunto à parte.

**Porta de passagem (giro/pivotante/correr embutida no painel) = 1 item por porta:**
- **Folha** ~72×210 (ou piso-teto até 273), **espessura ~4 cm** (quadro
  sarrafeado/2 faces) — consome mais que chapa única;
- **Marco (~3 cm) + alizar (~5 cm)** em todo o vão;
- **Laminada nas 2 faces** (aparece dos dois ambientes) → fita nos 4 lados × 2 faces;
- **Ferragem própria:** kit/dobradiça **pivotante** (especial) ou trilho se correr;
  **puxador cava**; **tranca + chave** quando o projeto pede;
- Montagem no local.

> Custo típico **~R$ 1,5–2,5k/porta** (material+ferragem), não ~R$ 0,8k de painel.
> O **painel** piso-teto em volta é orçado **à parte** (a folha é item separado).
> Mesma lógica para qualquer item com ferragem/estrutura especial embutida num
> painel (ex.: báscula de vidro, nicho-cofre): **destacar como item, não diluir em m²**.


## Lista de materiais — auto-gerada a partir do corte

Do mesmo projeto sai a **lista de materiais/ferragens** (com códigos de SKU),
organizada por categoria. Exemplo real (Maria, Ambiente 1):

| Categoria        | Item                                           | Qtd      |
|------------------|------------------------------------------------|----------|
| MDF (chapas)     | MDF Branco 15                                  | 7 chapas |
|                  | Nuvem Matt 15mm                                | 4 chapas |
|                  | Nuvem Matt 6mm                                 | 1 chapa  |
| Fita             | Borda Branco TX 22×0,45 **+10% desperdício**   | 60 m     |
|                  | Fita Borda Nuvem Matt 22×0,45 **+10% desperdício** | 80 m |
| Corrediças       | Corrediça BLUM Invisível 500mm (amortecimento) | 6 pares  |
| Suporte prat.    | Suporte "queijinho" (PCT 100)                  | 1 pacote |
| Acessórios       | Cantoneira reforçada 3 furos c/ capa           | 16       |
| Parafusos        | 4×16mm / 4×40mm                                | 1 / 2 pct|
| Tapa-furo        | 12mm Branco Ártico TX / Nuvem Matt             | 7 / 4    |
| **Serviços**     | Filetamento                                    | 120,90 m |
|                  | Furação                                        | 388 furos|
|                  | Marcação                                       | 80       |
|                  | Rasgo                                          | 5,95 m   |
|                  | Peças cortadas                                 | 85       |
|                  | Embalagem                                      | 12       |

### Regras que isso revela

- **Fita de borda = metros de filetamento do nesting + 10% de desperdício**,
  na bitola **22 × 0,45 mm**, por cor de chapa.
- **Serviços de produção são quantificados** (filetamento em m, furação em
  nº de furos, marcação, rasgo, peças cortadas, embalagem) — alimentam o custo
  operacional / tempo de máquina.
- Ferragens vêm da **especificação do item** (no escopo), não do nesting.

## Dois níveis de quantitativo

| Momento     | Como conta as chapas                              | Onde            |
|-------------|---------------------------------------------------|-----------------|
| **Orçamento** | Estimativa (inclui frações: 0,5 chapa) p/ precificar rápido | `validacao-orcamento.md` (planilha) |
| **Produção**  | Exato, via plano de corte (nesting) em chapas inteiras + aproveitamento + filetamento | software de corte |

> O agente orçamentista deve produzir a **lista de peças** (cut list) a partir
> do projeto; o nesting converte em chapas. Para orçar rápido, estima por área/
> aproveitamento (a confirmar a regra de estimativa com a Valvic).

## Fluxo de documentos por projeto (Google Drive → CLIENTES VALVIC)

`Escopo de venda → Projeto 3D → Plano de corte → Lista de materiais →
Etiquetas → Registros de entrega`. Apps internos em `sistema_valvic/apps/`
(ex.: `Valvic_Escopo_Venda_App.html`) geram esses documentos.

## Calibração com projetos reais (Marcenária Diferente)

Aprendido com 2 projetos completos (`projetos/treino/`): modelo maior (cozinha,
17 chapas, cliente luiz) e modelo menor (aéreos+balcão, 6 chapas, cliente aline).

### Regras de estimativa de chapas

1. **Chapa = 2750 × 1850 mm** (área útil ~5,09 m²), sempre.
2. **Agrupar peças por cor × espessura.** Cada combinação consome suas próprias
   chapas.
3. **Aproveitamento real:** chapas "principais" de uma cor rendem **85–92%**.
   Mas há chapas de **cauda** (sobra de uma cor com poucas peças) que rendem
   **2–35%**.
4. **Cada cor distinta puxa ≥ 1 chapa**, mesmo para 1 peça só. ⇒ Projetos com
   **muitas cores** gastam mais chapa do que a área pura sugere.
5. **Estimativa prática:** por cor/espessura,
   `chapas ≈ arredonda_para_cima( Σ área das peças ÷ (5,09 m² × 0,85) )`,
   com **mínimo de 1 chapa por cor**. Para a chapa de cauda, não esperar bom
   aproveitamento.

### Fita de borda
- Calcular o **filetamento** (metros das faces que levam fita — regras em
  `laminacao-e-construcao.md`), por cor.
- A **fita-material é arredondada pra cima por cor** (ex.: 40/60/140 m), acima
  do filetamento e além dos +10% — margem de estoque. Usar múltiplos
  generosos por cor.

### Ferragens — proporções observadas
- **Corrediça oculta = 1 par por gaveta** (Hardt Invisível P-10, no comprimento
  da profundidade: 400/450/550mm).
- **Dobradiças:** ~2 por porta de giro; mix Reta/Curva c/ amortecedor + Reta
  comum (interno). Cozinha grande: 59; conjunto pequeno: 24.
- **Pistão a gás** (60–100N) por báscula/aéreo basculante.
- **Sistema Dominus** (correr): kit + trilho inferior RM-265 + superior RM-264
  (barras de 3m) + amortecedores.
- **Puxador cava:** medido em **metro** (usinado), pela extensão das frentes.
- **Suporte de prateleira:** VB Zamac Uniblock (furo 18mm), ~4 por prateleira.
- **Cantoneira reforçada 3 furos c/ capa** e **parafusos** (4×16/25/40mm) por
  módulo/montagem; **tapa-furo por cor**.

### Serviços de produção (sempre quantificados)
Filetamento (m), **Rasgo (m)** — sulco do fundo por encaixe —, Furação (nº de
furos), Marcação, Peças Cortadas, Embalagem. Úteis para dimensionar tempo de
máquina/operação.

> **Próximo passo de calibração:** comparar a estimativa manual do Marcos
> (a partir de medidas/render) com esses números reais e ajustar os fatores
> (aproveitamento por tipo, fita por gaveta/porta, furação por módulo).
