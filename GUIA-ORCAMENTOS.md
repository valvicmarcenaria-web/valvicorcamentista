# Guia de Orçamentos — Valvic (Lavinia)

Consultar antes de orçar ou calibrar a skill. Documenta regras de material,
sistemas, lógica de cálculo e aprendizados de projetos reais.

---

## Skill ativa: Lavinia — Orçamentista Estratégico

Agente unificado em `.claude/skills/orcamentista-marcenaria/`. Três fases:
1. **Olhar** — lê o projeto visualmente e monta o quantitativo (sem medidas: Lavinia infere).
2. **Preço** — aplica custo de material + MC% e fecha o orçamento.
3. **Estratégia** — otimizações, propostas alternativas, handoff para o Rodrigo.

Ferramenta principal: `ferramentas/validacao-orcamento.html`.

---

## Metas de MC (calibradas com o Rodrigo — jun/2026)

| Situação | MC mínima aceita | Referência |
|---|---|---|
| Caixa crítico | 25% | exceção — só para não ficar ocioso |
| Caixa ruim | 30% | exceção consciente |
| Caixa normal | 37% | piso operacional |
| **Piso de break-even real** | **~43%** | custo fixo R$67k ÷ fat. R$162k |
| **Alvo saudável** | **48–50%** | gera lucro + amortiza dívidas atuais |

> O "ideal 35–40%" do método original fica **abaixo do break-even** e gera prejuízo
> estrutural. Cada +1 ponto de MC% = +R$1,62k de lucro/mês. Ver auditoria completa
> em `estrategia-financeira-precificacao/referencias/auditoria-metodo.md`.

---

## Material padrão

- **MDF Melamínico** é o padrão da Valvic (não MDP, não aglomerado simples).
- Espessuras: **18mm** estrutural, **15mm** interno, **6mm** fundo/gaveta.
- **Prateleira longa (> 70cm em roupeiro):** usar **18mm** (não 15mm) para evitar
  flambagem.
- Cor padrão: cliente define; Branco TX é o mais comum. Cristallo, Acetinato e
  laminado prensado são upgrades com custo maior.

---

## Fita de borda (laminação)

**Regra geral: toda aresta exposta leva fita.**

| Situação | Tipo |
|---|---|
| Interno / não visto | Branco TX (mesmo se a peça for colorida) |
| Externo / visto / mesma cor | Fita cor correspondente |
| Aresta de porta ou face nobre | Fita cor ou perfil usinado |

- **Colagem máquina** (coladeira): 2,5 mt/linear — peças retas longas.
- **Colagem manual**: 4,0 mt/linear — peças curvas, ripados, detalhes.
- Gaveta 4 peças: frente + fundo + 2 laterais → ~3–4 mt de fita máquina + cola.
- Gaveta padrão = **6 peças** (frente, fundo, 2 laterais, frente falsa, guia inferior
  se telescópica); fita nas 4 faces internas.

---

## Roupeiros

### Sistemas de porta

| Sistema | Uso |
|---|---|
| **RO65** (Rometal) | Deslizante de embutir — padrão residencial. Kit R$60 + trilho. |
| **SS150** | Deslizante robusto — vãos maiores ou projetos de alto padrão. |
| **Dominus** | Premium. Trilho superior robusto. |
| **Multi** | Rack/suspenso. |
| **Linea** | Suspenso, 1 ou 2 portas. |

- **Desempenador:** sempre cotar quando a porta deslizante for alta (evita empenamento).
  Sobrepor R$100/par · embutido R$150/par.
- Trilho: medir o vão corrido e cotar o trilho correto (2mt ou 3mt). Não esquecer
  trilho superior E inferior (quando aplicável).

### Checklist roupeiro (antes de fechar o orçamento)

- [ ] Sistema de porta definido (deslizante / articulada / sem porta)
- [ ] Trilho(s) cotados (superior + inferior se deslizante)
- [ ] Desempenador cotado (portas altas)
- [ ] Tipo de corrediça das gavetas (telescópica / oculta Hardt / Hettich)
- [ ] Prateleiras > 70cm → 18mm
- [ ] Fita de borda por metro calculada (incluir gavetas)
- [ ] Iluminação LED (se solicitada)
- [ ] Tábua de passar (Outros 1 — R$500 kit)
- [ ] Espelho (vidros e espelhos m²)

### Roupeiro em L

Tratar como **dois ambientes separados no app** (aba por módulo) para rastrear
material por trecho. O fechamento consolida tudo.

---

## Gavetas

Estrutura padrão (6 peças de MDF):
1. Frente (face visível)
2. Fundo
3. Lateral esquerda
4. Lateral direita
5. Frente falsa (se o projeto tiver frente de MDF separada do sistema)
6. Base (quando não é fundo do próprio caixote)

Corrediças:
- **Telescópica** (R$40) — padrão / econômico.
- **Oculta Hardt** (R$70) — intermediário.
- **Oculta Quadro Hettich** (R$120) — alto padrão com amortecimento.
- **Oculta Actro Hettich** (R$400) / **Blum** (R$300) — premium.

---

## Ripado

Dois tipos principais:

| Tipo | Material | Cálculo |
|---|---|---|
| Ripado MDF | Tiras de MDF cortadas na CNC | mt² de área coberta × espessura |
| Ripado em madeira maciça | Pinus, Eucalipto, etc. | por mt linear de ripa + acabamento |

- Contar fita de borda em **todas** as faces expostas das ripas.
- Colagem manual (não máquina) para ripas curtas/curvas.

---

## Portas frisadas / com detalhe

- Portas com **friso vazado** (recorte na CNC): a abertura no MDF é real — não é só
  estética. Calcular a perda de material no recorte se o friso for grande.
- Portas com **friso embutido** (rebaixo): sem perda de material, mas custo de
  usinagem na CNC.
- **Porta com vidro**: cotar vidraceiro separado (terceirizado do ambiente).

---

## Portas de espelho — REGRA (Kenia & Fábio, jun/2026)

⚠️ **Quando o projeto não especifica como é a porta de espelho, PERGUNTAR ao
Jonathan** (espelho colado no MDF? esquadria de alumínio?). São custos diferentes.

### Caso 1 — espelho colado no MDF
- O espelho é **insumo de material**, **NÃO** mão de obra de vidraceiro.
- Lançar pela **base de custo por m²** (categoria *Vidros e espelhos*: Espelho
  prata / Espelho bronze).
- **Somar custo logístico do item: R$150** (frete do espelho até a fábrica) —
  lançar como item de logística/especial daquele ambiente.

### Caso 2 — porta com esquadria de alumínio
- Envolve **fornecedor terceirizado** — **NÃO** o vidraceiro.
- É o **mesmo fornecedor que cotou a porta de vidro reflecta**; a calibração de
  valor segue a **mesma dinâmica** daquele orçamento.

### Valores de referência cravados (jun/2026)
Calibrados com o Jonathan e gravados na biblioteca (`Vidros e espelhos (m²)`):
- **Vidro reflecta bronze 6mm: R$350/m²** · **8mm: R$450/m²**
- Espelho prata R$600 · Espelho bronze R$900 (já existiam)
- Logística do espelho colado: **R$150** (categoria *Especiais › Logística específica*)
- *Especiais*: Estrutura de serralheria R$150 · Gaveta especial R$900
- Removidos placeholders zerados (Especial 2, mini fix, Outros, Item especial, Bandeja).

> Regra geral aprendida: "porta de espelho" não é sinônimo de vidraceiro. Definir
> primeiro a construção (colado no MDF × esquadria de alumínio) e só então o custo.

---

## Terceirizados — por ambiente, não global

Cada ambiente tem seu próprio bloco de terceirizados:
- Vidraceiro, Serralheiro, Pintor, Estofador, Laqueamento.
- Alocar ao ambiente onde o serviço ocorre (não em um bolo global).
- O fechamento consolida todos os ambientes.

---

## Parâmetros financeiros padrão (app)

| Parâmetro | Valor padrão | Notas |
|---|---|---|
| NF % | 4% | sobre investimento bruto |
| Parcelamento % | 8% | custo financeiro do prazo |
| Comissão vendedor % | 3% | |
| RT % (s/ líquido) | 10% | responsabilidade técnica |
| Visitas R$ | R$250 | |
| Programador % | 0,8% | s/ líquido |
| Coordenador % | 1,0% | s/ líquido |
| Marceneiros % | 2,5% | s/ líquido |
| Desg. serra/fresa % | 0,5% | s/ bruto |
| Margem de erro % | 2% | s/ bruto |

Estes são os padrões; o app permite editar por orçamento.

---

## Prazo de entrega — SEMPRE perguntar ao Jonathan (regra, jun/2026)

O **prazo de entrega proposto ao cliente está diretamente ligado à produção** —
a Lavinia **não arbitra prazo sozinha**. Antes de fechar/propor, **perguntar ao
Jonathan** o prazo a propor e repassá-lo ao Vitor. Se a Lavinia não informar, o
Vitor **pergunta antes de pôr na proposta** (nunca cravar prazo sem validação).

## Harmonia informacional (gargalo central do Jonathan)

**O que está no projeto · o que foi entendido · o que foi vendido · o que será
produzido — tudo precisa estar em perfeita harmonia.** Toda decisão de material/
composição que destrava o orçamento vira registro (painel de dúvidas) e segue
idêntica até a produção. Na dúvida, **perguntar** — nunca assumir.
> Ex. real (Regina): o **interno dos nichos é Blush (cor)**; só o **contorno dos 4
> lados é branco**. Não descrever o interno como branco em lugar nenhum.

## Organização no Drive — pasta única por cliente

- **Uma pasta por cliente** em `CLIENTES VALVIC` (ex.: "Regina Godinho"). **Evitar
  muitas subpastas** — dificulta o acesso rápido. Orçamento (JSON) + proposta + docs
  ficam soltos na mesma pasta.
- A Lavinia cria a pasta e deposita o **orçamento (JSON)**; o **Vitor** adiciona a
  **parte dele** (proposta/links) na mesma pasta.

## Fluxo de orçamento

1. **Receber o briefing** (planta, fotos, referências do cliente).
2. **Lavinia analisa visualmente** → monta quantitativo (sem pedir medidas: infere
   da planta ou descrição, ou pede apenas o necessário).
3. **Preencher o app**: criar um ambiente por cômodo/módulo, lançar quantidades.
4. **Informar o Investimento Bruto** (preço ao cliente) → app calcula MC%.
5. **Verificar MC% vs situação de caixa** (pedir ao Jonathan antes de fechar).
6. **Usar "Sugerir preço"** quando precisar partir do custo para chegar no preço
   com MC alvo.
7. **Handoff para o Rodrigo** quando a decisão for estratégica (aceitar MC abaixo
   do normal, projeto grande, dúvida sobre caixa).
8. **Exportar JSON** → salvar no Drive: `Orçamentos Valvic / Em aberto / [cliente] /
   Versão N`.

---

## Preços de referência (biblioteca — atualizar quando o fornecedor mudar)

Os preços estão na biblioteca do app (editável por orçamento, compartilhada).
Principais a revisar periodicamente:

- MDF melamínico (variação de chapa)
- Sistemas de deslizante (RO65, SS150, Dominus)
- Corrediças (Hettich, Blum — importados sofrem câmbio)
- Vidros e espelhos (m²)

Ao alterar o preço de um item no app e exportar JSON, o JSON carrega o preço
atualizado. A biblioteca default (código) deve ser atualizada no HTML quando o
preço mudar permanentemente.

---

## Aprendizados de projetos reais

### Camila (Closet + Ilha)
- Roupeiro em L: dois ambientes no app (trecho 1 + trecho 2).
- Ilha com tampo de granito: granito é por conta da marmoraria (não entra no MDF).
- Portas deslizantes no closet: RO65 + trilho RO65 2mt ou 3mt conforme o vão.

### Kenia & Fábio (Banheiro)
- Portas de vidro temperado: cotar vidraceiro como terceirizado do ambiente.
- Armário espelho: espelho prata (m²) + estrutura MDF 18mm.
- Aço inox em detalhes: serralheiro como terceirizado.

### Regina Godinho (Home office — arq. Carolina Godinho, jun/2026)
- Bancada em L suspensa + gaveteiro (3 gav + 1 porta) + bandejas guarda-folhas; painel de 14 nichos aéreo.
- Material Blush (Duratex) = **MDF cor (R$500)**. Projeto inteiro em **15mm** (ver método bancada).
- Nicho: **interno todo na cor, contorno dos 4 lados em branco** (gargalo de material — ver regra abaixo).
- Sem RT de arquiteto. Custo R$7.442 → preço MC 43% = R$13.100.

### Regra geral aprendida
Sempre perguntar ao Jonathan **situação de caixa** antes de fechar qualquer
proposta. A MC mínima aceitável muda conforme o mês — é o Rodrigo quem define o
piso estratégico.

---

## Método Valvic — bancada/tampo suspenso (REGRA, jun/2026)

Tampo flutuante grande (ex.: escrivaninha em L) **flete só com MDF**. Forma usual da Valvic:
1. Tampo em **MDF 15mm** (não 18mm).
2. **Enchimento com sobras de material** até dar ~**50mm de espessura livre** (usa retalho, custo zero de chapa).
3. **Estrutura de serralheria em metalon 30×50mm** para sustentar → terceirizado, **~R$350 + logística dedicada (~R$150)**.
4. **Chapa de 6mm embaixo** para fechar = "bancada toda acabada", sem estrutura aparente.

> Consequência de orçamento: projetos com esse tampo saem **todos em 15mm** (+ 6mm de acabamento), nunca 18mm.

---

## Medida: o que prevalece

A **tabela de mapeamento** do projeto é só **referência de apoio** (para dar andamento
quando falta info). **A medida cotada no projeto SEMPRE prevalece** sobre a tabela.
Quando houver divergência, seguir o desenho técnico.

---

## Composição de material (gargalo crítico) — perguntar face a face

"Tudo na cor" × "branco por fora, cor por dentro" **inverte o plano de corte, a
metragem de cada chapa e a laminação**. Se vazar errado pro programador, vira peça
refeita. **Sempre confirmar a composição descrevendo a peça superfície por superfície**
(ex.: "moldura externa branca, interior e frente dos nichos na cor — é isso?"). Essa
decisão tem que ficar **registrada no painel de dúvidas** e seguir até a produção.

---

## Estratégia de proposta (alinhado com o Rodrigo)

- **Ancoramos na proposta o que está sendo vendido.** Orça-se o que o projeto especifica
  (ex.: todas as corrediças ocultas Hardt) — **sem "otimização escondida"**.
- **Downgrade é carta de negociação**, usada só **quando o cliente chora preço** — não é
  premissa de orçamento. Ex.: trocar bandejas de oculta Hardt → telescópica.
- Proposta ancorada no **piso real de MC (~43%)**; abaixo disso, só com aval do Rodrigo
  (caixa baixo pode aceitar 37%).
