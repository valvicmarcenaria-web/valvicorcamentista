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
- [ ] Tipo de corrediça das gavetas (telescópica / oculta Hartt / Hettich)
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
- **Oculta Hartt** (R$70) — intermediário.
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

### Regra geral aprendida
Sempre perguntar ao Jonathan **situação de caixa** antes de fechar qualquer
proposta. A MC mínima aceitável muda conforme o mês — é o Rodrigo quem define o
piso estratégico.
