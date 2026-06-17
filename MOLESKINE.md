# Moleskine Digital — Valvic

Arquivo de tarefas e recados entre sessões. Qualquer agente (Lavinia, Rodrigo, Vitor…)
pode ler e escrever aqui. Formato livre — marcar data e agente responsável.

---

## Tarefas abertas

### [2026-06-16] Redesenho dos templates de proposta — Stefan
**Solicitante:** Jonathan  
**Agente:** Stefan (designer-grafico)  
**Status:** 🟡 Em andamento — v1 do redesign entregue, aguardando aprovação de Jonathan

**Contexto:**  
O Template Excellence (HTML) feito pelo Vitor foi **reprovado** por Jonathan:
"não conversa com o público; as páginas estão fracas". Só a **página de
Investimento** foi aprovada. Criada a skill **Stefan** (diretor de arte
especialista em marcenaria) para redesenhar as propostas do zero, com padrão de
grife (Ornare/Florense), antes de retomar o Vitor.

**O que fazer:**  
- Diagnóstico de design do Excellence atual (o que não funciona e por quê)
- Redesenhar os 4 templates por perfil (Signature/Excellence/Essencial/Family)
  usando o sistema visual de Stefan (`designer-grafico/referencias/sistema-visual.md`)
- Reaproveitar o conteúdo já definido (8 etapas da linha do tempo, social links)
- Manter o conteúdo da página de Investimento (aprovado), elevar o visual

**Arquivos:**  
- Skill: `.claude/skills/designer-grafico/`
- Template reprovado: `.claude/skills/closer-vendas/ferramentas/proposta-excellence.html`
- Conteúdo da linha do tempo: `closer-vendas/referencias/linha-do-tempo.md`
- **Acervo de imagens Valvic (projetos executados):** `https://drive.google.com/drive/folders/1eUnLV1GsOo4X5SSxNzbVLVfL4Wgjf2OM`

**Versão Canva (editável por Jonathan) — 2026-06-16:**  
A proposta foi levada ao Canva via **import de PDF** (o import de HTML achata o
layout; o de PDF preserva A4 e converte texto em caixas editáveis). Fonte:
`proposta-excellence.pdf` (gerado do HTML, commitado no repo).
- ✅ **Design bom (6 págs A4, texto editável):** `DAHMxT1mbIE` — editar: https://www.canva.com/d/ZAvl9HRyLSu9_p-
- ⚠️ **Import quebrado (ignorar/excluir):** `DAHMxR1GnbQ` (HTML achatou em 1 pág paisagem)
- Limite técnico confirmado: a API de edição do Canva só EDITA elementos
  existentes (texto/cor/imagem) — não CRIA caixas/formas do zero. Por isso o
  caminho é PDF→import, não construção nativa via MCP.
- Fluxo de atualização: editar texto no HTML → gerar PDF → reimportar no Canva.

**Modelo ESSENCIAL (Hardt) — 2026-06-17:**  
Criado `proposta-essencial.html` (variante do Excellence). Território visual
"Confiança limpa": fundo branco quente `#FBF8F2`, acento **terracota `#B07A56`**,
header de investimento em **espresso `#3D2A1C`**. Capa e linha do tempo CLARAS
(onde o Excellence é grafite escuro) — "premium sem peso". Badge "Essencial ·
Hardt", garantia 5 anos, ferragem Hardt, 1º diferencial adaptado (Hardt soft-
close, sem citar Hettich). Storage key `valvic_essencial_modelo`.

**Propostas Kênia & Fábio (Casa Completa) — GERADAS 2026-06-17:**  
Pasta Drive: `https://drive.google.com/drive/folders/1phUShb6q29uXp4vWzHQYM_TmBmtTs85a`
- ✅ `proposta-kenia-fabio-premium.html` (Excellence/Hettich): Tudo na cor R$359k · Branco interno R$345k · 10 anos
- ✅ `proposta-kenia-fabio-essencial.html` (Essencial/Hardt): Tudo na cor R$340k · Branco interno R$317k · 5 anos
- 9 págs cada: capa · diferenciais · **descritivo técnico (4 págs, 69 itens M## por ambiente)** · linha do tempo · depoimento (Graciene) · investimento
- Descritivo item-a-item com códigos M## da arquiteta, sem medidas (escolha do Jonathan)
- Investimento: 2 versões (cor/branco) + aviso reajuste julho/2026 + 40/30/30 sem cartão + 90–100 dias + sem assinatura
- Gerador versionado: `gerar-kenia-fabio.cjs` (dados do descritivo + monta os 2 docs a partir dos templates)
- ⏳ Pendentes: foto da capa (placeholder) · revisão do Jonathan · export PDF · salvar FINAL na pasta Drive

---

### [2026-06-16] Novo layout de proposta — Vitor
**Solicitante:** Jonathan  
**Agente:** Vitor  
**Status:** 🟡 Em andamento — brief definido, aguardando decisão de cor + execução no Canva

**O que foi pedido:**  
Criar um novo layout/template de proposta — diferente dos modelos atuais no Canva
(MODELO e MODELO ENXUTO). Jonathan quer:
- Nova linha do tempo visual (mais impactante, que transmita rigor e confiança)
- Links para Instagram e YouTube da Valvic
- Incorporar o processo real da Valvic (fluxogramas Miro) de forma estratégica

**Brief definido (Vitor, 2026-06-16):**

#### Linha do tempo — 8 etapas selecionadas estrategicamente

| # | Nome na proposta | Argumento de valor |
|---|---|---|
| ① | Visita & Escuta | Medição presencial para garantir precisão total |
| ② | Projeto & Orçamento | Transparência completa — sem surpresas no caminho |
| ③ | Engenharia de Produto | Seu projeto vira software especializado antes de virar móvel |
| ④ | Análise Técnica | Validação por toda a equipe antes do primeiro corte |
| ⑤ | Produção com Padrão | Cada peça produzida com protocolo documentado de qualidade |
| ⑥ | Conferência & Embalagem | Testado e protegido antes de sair da fábrica |
| ⑦ | Entrega & Montagem | Equipe própria do início ao fim — não terceirizamos |
| ⑧ | Garantia & Suporte | Estamos aqui depois da entrega (garantia por ferragem) |

**Critério de seleção:** cobrir os 3 medos do comprador (Clube dos Planejados):
"vão entregar o que prometeram?", "tem equipe própria?", "some depois da entrega?"

#### Conceito visual
- **Estilo:** linha diagonal ascendente (progresso) com marcos em círculos dourados
  — inspirado na Coffema Roadmap mas na identidade Valvic
- **Alternativa A4:** horizontal 4+4, ícones acima, texto abaixo, 2 linhas
- **Paleta:** fundo creme `#FDF6E3` ou navy escuro (decidir com Jonathan)
- **Ícones:** linha fina, minimalista
- **Rodapé da seção:** links IG + YouTube

#### Social links confirmados
- Instagram: https://www.instagram.com/valvic_marcenaria
- YouTube: https://www.youtube.com/@Valvic_Marcenaria

**Pendências antes de executar no Canva:**
- [ ] Jonathan decide: fundo claro (creme) ou escuro (navy)?
- [ ] Jonathan valida as 8 etapas e os nomes
- [ ] Executar no Canva (MCP disponível)

**Arquivos relacionados:**  
- Templates atuais: MODELO `DAHMsJxsuhE` · MODELO ENXUTO `DAHMsEfQNas`
- Referência identidade: `.claude/skills/closer-vendas/referencias/identidade-marca.md`
- Conteúdo detalhado: `.claude/skills/closer-vendas/referencias/linha-do-tempo.md`

---

### [2026-06-16] Academia de vendas — Vitor
**Solicitante:** Jonathan  
**Agente:** Vitor  
**Status:** 🔴 Pendente — estrutura definida, cresce gradualmente com o aprendizado

**O que foi pedido:**  
Criar uma "caixa de ferramentas de vendas" no repositório — academia completa
com scripts, cadências e filosofia de fechamento. Cresce com o tempo conforme
Vitor aprende o jeito do Jonathan.

**Estrutura planejada:**
```
.claude/skills/closer-vendas/academia/
├── README.md              ← índice da academia
├── filosofia.md           ← Flávio Augusto + Caio Carneiro + Jonas Pastore aplicados
├── perfil-comprador.md    ← inteligência do Clube dos Planejados
└── scripts/
    ├── 01-primeiro-contato.md
    ├── 02-qualificacao.md
    ├── 03-apresentacao-proposta.md
    ├── 04-tratamento-objecoes.md
    └── 05-fechamento.md
```

**Próximo passo:** Jonathan compartilha mais conversas reais / situações vividas
para Vitor calibrar o tom e o jeito dele.

---

## Tarefas concluídas

### [2026-06-16] Proposta Regina Godinho — Escritório ✅
- Proposta montada no Canva (MODELO ENXUTO)
- Mensagem de envio preparada
- Doc salvo no Drive: "Proposta Regina Godinho - Vitor (links + mensagem)"

---

## Regras permanentes de proposta

> Válido para todos os templates e todos os agentes. Não mudar sem OK do Jonathan.

- **NUNCA mencionar RT de arquiteto** nos valores: "RT da arquiteta inclusa nos preços" ou qualquer variação gera atrito sério entre cliente e arquiteta. Fora de toda proposta.
- **NUNCA dizer "sem cartão"** nas condições de pagamento: o cliente já vê que cartão não está listado. Mencionar cria objeção desnecessária. Usar apenas "Condições de pagamento" como título.

---

## Recados rápidos

*(notas passageiras — podem ser apagadas após lidas)*
