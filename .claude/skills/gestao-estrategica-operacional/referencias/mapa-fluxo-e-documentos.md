# Mapa de Fluxo & Registro de Documentos / POPs — Valvic

> A "fonte única" da Helena para o **fluxo de trabalho** da Valvic e o **inventário de
> documentos** (o que já existe × o que criar). Base: leitura do Drive (ver
> `dados/valvic-conhecimento-drive.md`). **A refinar com o export do fluxograma do Miro**
> — o Miro dá a sequência exata e a ordem-fim das etapas/POPs.
> Legenda: ✓ existe · ☐ criar · ⚑ prioridade alta.

## O fluxo de trabalho, ponta a ponta (CONFIRMADO pelo fluxograma do Miro)

Cadeia de **5 macro-etapas** encadeadas por handoffs (o "Fim" de uma = o "Início" da próxima).
Entre `[colchetes]` está o **artefato que o Miro anota em cada passo** — é daqui que sai o checklist.

**1 · COMERCIAL / VENDA** — *Jonathan / SDR / vendedor*
Contato (WhatsApp/redes/parceiros) → Qualificação `[check list]` → «projeto aprovado?» —
(não: Visita `[check list]` → Projeta → «validou?»/ajuste no esboço) · (sim: «visita prévia?» →
Realizar visita `[relatório Calcme]`) → **Elaborar orçamento** `[POP + proposta]` → Agendamento de
apresentação `[relatório Calcme]` → «orçamento aprovado?» — (não: «negociação possível?» → Negociar /
Encerrar `[relatório Calcme]`) → **Contrato e Financeiro** `[cadastro completo Calcme + PDP]` →
Inserção no quadro de entrega → **Etapa 1: Escopo de venda + projeto atualizado**.

**2 · ENGENHARIA / PROJETO** — *Paulo, Deivson, programadores, Jonathan*
Conferência técnica `[fotos+medição no Drive · check list / PDP]` → «tudo apto p/ produção?»
(sim / parcial / não → **realinhamento de cronograma formalizado c/ cliente** `[documentação formal
visual+textual]`) → Planejamento de produção `[plano de ações]` → Análise técnica (olhar de produção) →
«validou?» / adequação (formaliza alteração c/ cliente) → Engenharia de produto → Programação (software) →
conferência → «validou?» / correção → upload de arquivos no Drive → encaminha p/ Aquisição.

**3 · AQUISIÇÃO DE COMPRAS** — *Paulo / ADM · Jonathan / ADM*
Listagem de insumos `[lista]` → «insumos disponíveis?» — (não/parcial: lista de compra → Cotação →
Demandar fornecedores → Validar pagamento c/ financeiro → Requisição → Faturamento `[lançar Calcme]`) ·
(sim: separar no box do cliente → baixa no sistema) → aguarda recepção.

**4 · RECEPÇÃO / CONFERÊNCIA / ARMAZENAGEM** — *Deivson / Joelson / ADM*
Receber insumos `[Mapa de produção + Nota fiscal]` → «tudo correto?» — (não: acionar responsável `[POP]` →
«resolvido?» → sinalizar pendência / notificar comprador+financeiro) → Separação → «pertence a projeto?» —
(sim: alocação no projeto → baixa no pedido) · (não: almoxarifado → atualização de estoque no Calcme).

**5 · PRODUÇÃO** — *Deivson · Paulo/Jonathan · Jomar · Samuel*
Execução de fabricação `[Mapa de produção + POP]` → «cabível de pré-montagem?» → pré-montagem →
Conferência `[check list]` → «validou?»/correções → **Execução POP de qualidade** `[check list]` →
«validou?»/correções → Embalagem `[POP]` → Envio para entrega → Fim.

> **Sistemas no fluxo:** o **Calcme** é o transacional recorrente (relatório de visita/agendamento/
> encerramento, cadastro completo, faturamento, estoque) + **Drive** (fotos/medição, upload de arquivos).
> O Miro **não** cita Canva/Autentique/SketchUp/Upmob — esses aparecem no relato do processo *atual*
> (base histórica). O Miro é o **processo-alvo**, centrado em **Calcme + POPs + check lists + Mapa de produção**.
> **Termos a confirmar:** **PDP** (aparece em Contrato/Financeiro e Conferência técnica — plano/pedido de
> produção?); a fase de "Programação (software)" não nomeia o software; e há a caixa "Est.2" na conferência técnica.

## Artefatos exigidos pelo próprio fluxo (Miro) × status
Cada linha é um documento que o processo **explicitamente pede**. Onde já há um app na pasta `apps`, o
que falta é o **POP escrito / template que o rege**.
| Artefato (etapa) | Já existe? | O que falta criar |
|---|---|---|
| **Check list de Qualificação** (com score) | ✓ (comercial) | — (validar contra o Miro) |
| **Check list de Visita** | parcial | Formulário de visita padrão |
| **Proposta / Orçamento** | ✓ template Lavinia (custeio) | **Template de proposta (Gold/Prime)** + **POP de elaboração de orçamento** |
| **Relatório no Calcme** (visita/agend./encerr.) | ✓ (campos no Calcme) | Padrão do que registrar em cada ponto |
| **Escopo de venda + projeto atualizado** (Etapa 1) | ✓ app | ⚑ **POP do Escopo de Venda** (contrato de informação) |
| **PDP** (contrato/financeiro e conf. técnica) | ? | Definir o que é e o **template do PDP** |
| **Check list de Conferência técnica** (Est.2) | ✓ app | POP + check list impresso |
| **Documentação de realinhamento de cronograma** | ✓ modelo (doc de ocorrência já feito serve de base) | Template de comunicação formal c/ cliente |
| **Plano de ações / Planejamento de produção** | ? | Template do plano de produção |
| **Mapa de produção** (recepção→envio) | ? (central no fluxo) | ⚑ **Template do Mapa de Produção** (documento que atravessa 4 etapas) |
| **POP de recepção / acionar responsável** | ☐ | ⚑ POP de recebimento + tratativa de não conformidade |
| **POP de execução de fabricação** | ☐ | ⚑ POP de fabricação |
| **Check list de Conferência (produção)** | ✓ app conferência fabricação | check list impresso + POP |
| **POP de Qualidade** ("Execução POP de qualidade") | ☐ | ⚑ POP + check list de qualidade |
| **POP de Embalagem** | ☐ | POP de embalagem |
| **Check list / relatório de Envio-Entrega** | ☐ | Relatório de entrega + vistoria-aceite |
| **Listas** (insumos / compra / pendências) | parcial | Templates de lista |

## Registro de documentos — o que JÁ EXISTE (✓)
**Comercial:** Funil de Vendas 2026 · Checklists de qualificação (Lead Direto / Via Arquiteto, com score) ·
Compromisso de Garantia (Gold) · Painel de Ferragens · Política/Programa de Parceria RT · Scripts de SDR ·
Mapeamento de Objeções · Arsenal de Vendas · Caixa de Ferramentas (jornada + cadência de follow-up) ·
Manual de Comportamento do Setor Financeiro (protocolos de contato/cobrança/NF).
**Precificação:** Template de custeio/validação de orçamento (Lavinia, MC%).
**Pessoas/RH:** Matriz de Crescimento v2 (organograma + trilhas + salários) · Manifestos individuais (7+) ·
Atas de alinhamento (CLT/PJ) · Advertência (modelo) · Plano de Estágio/Trilha · Sistema de reconhecimento R$200.
**Academy:** Guia Técnico Módulo I.
**Apps-checklist (pasta apps):** Escopo de Venda · Conferência Técnica · Conferência de Programação ·
Lista de Materiais · Conferência de Fabricação · Briefing de Visita · Demandas · Reconhecimento ·
Matriz de Crescimento · academia de vendas · validação de orçamento · custo da operação · tabela de valores.

## Documentos & POPs a CRIAR (☐) — o checklist

### A · Produção / chão de fábrica (maior lacuna de padronização)
- ☐⚑ **POP — Escopo de Venda completo** (contrato de informação): regra "não entra em produção sem
  material, cor, medida, ferragem e prazo 100% definidos". *Ataca o gargalo-raiz.*
- ☐⚑ **Checklist de qualidade / não conformidade** antes da expedição (rege o app de conferência de fabricação).
- ☐⚑ **POP de montagem em obra + Relatório/checklist de entrega** (vistoria-aceite + registro de ocorrências).
- ☐ **POP — recebimento e conferência de chapas MDF** (NF, quantidade, avarias).
- ☐ **POP — operação/troca de fresa da CNC e manutenção de máquinas** (coladeira, seccionadora, router).
- ☐ **POP — plano de corte / nesting + nomenclatura padrão de peças.**
- ☐ **Checklist de pré-montagem.**
- ☐ **POP — pós-venda / assistência técnica / acionamento da garantia (10 anos).**
- ☐⚑ **Manual do padrão construtivo Valvic (SketchUp + Upmob)** — tirar da cabeça do Paulo (tácito → escrito).
- ☐ **Tabela oficial de espessuras/ferragens por tipo de móvel + folgas e recuos padrão.**

### B · Financeiro (lacuna mais crítica — handoff ao Rodrigo)
- ☐⚑ **DRE mensal** (modelo).
- ☐⚑ **Fluxo de caixa projetado** (entradas × saídas).
- ☐⚑ **Contas a pagar** (fornecedores, folha, impostos, financiamentos).
- ☐⚑ **Mapa de custo fixo mensal + cálculo de break-even.**
- ☐ **Controle de dívidas/financiamentos** (máquinas, aportes do Paulo).
- ☐ **Política de precificação documentada** (MC mínima por canal/perfil, descontos, gatilhos) — texto, não só planilha.
- ☐ **Dashboard de margem por projeto/mês** (usar `ferramentas/painel-gestao-template.html`).
- ☐ **Conciliação bancária + consolidação de comissões pagas por colaborador/mês.**

### C · Comercial
- ☐⚑ **Template de Proposta padrão** (2 versões Gold/Prime) — o arquivo-modelo.
- ☐⚑ **Contrato-modelo + Termo de Garantia** (arquivos-modelo prontos p/ Autentique).
- ☐ **Tabela de preços / piso de margem** documentada.
- ☐ **POP de CRM/pipeline** (ferramenta, campos, cadência de atualização do funil).
- ☐⚑ **POP de handoff Comercial → Produção** (checklist do que o comercial entrega no fechamento).
- ☐ **Roteiro/checklist da visita técnica + da reunião de fechamento presencial.**
- ☐ **Metas comerciais quantificadas por etapa** (leads/mês, conversão-alvo, meta por closer).

### D · Pessoas / gestão
- ☐ **Escopos formais dos sócios** (Jonathan e Paulo) como documento próprio.
- ☐ **Manifestos dos cargos-vaga** (Especialista em Acabamento, Técnico de Montagem).
- ☐⚑ **Formulário de avaliação de 90 dias** (instrumento preenchível a partir dos indicadores dos manifestos).
- ☐ **POP de admissão/onboarding operacional** (montador, auxiliar) — hoje só a estagiária tem trilha.
- ☐ **Guia Técnico Módulo II** (leitura de projeto, cotas, montagem).
- ☐ **Rito documentado de reuniões/cadência** (base já em `referencias/rotinas-cadencia.md` — formalizar).

## Melhorias sugeridas (a Helena recomenda)
1. **Atacar o gargalo-raiz primeiro:** o *Escopo de Venda como contrato de informação* — é o item de
   maior retorno (elimina retrabalho). Tornar obrigatório antes de qualquer início de produção.
2. **App executa, POP ensina:** os apps-checklist já existem; falta o **POP escrito que os rege** e liga
   à Academy (Doc 12 + Doc 13 do "Valvic OS"). Cada app deve ter seu POP e um vídeo/aula.
3. **Financeiro é o maior risco:** a pasta financeira tem **1 planilha de recebíveis** — subir para gestão
   real (DRE + fluxo de caixa + contas a pagar + break-even). *Handoff ao Rodrigo.*
4. **Padronizar a precificação em documento** (não só "feeling" + planilha): regras de MC mínima por
   perfil/canal, para virar método ensinável (dor declarada no processo comercial).
5. **Consolidar a marca:** substituir "Vargas Decor" por "Valvic / Linha Gold" em todo o material comercial
   (há inconsistência entre o doc estratégico e os PDFs novos).
6. **Fechar templates comerciais:** proposta-modelo, contrato e Termo de Garantia como arquivos prontos.
7. **Onboarding operacional + avaliação 90 dias** como instrumento (hoje o critério existe, o formulário não).
8. **Manter este registro como fonte única** (Helena): cada documento com **status + dono + prazo**;
   revisar na cadência mensal.

## Pendências deste mapa
- ✓ **Fluxograma do Miro** — obtido via 3 screenshots no Drive e transcrito; fluxo acima já é o do Miro.
- ⚑ **Confirmar com o Jonathan:** o que é **PDP**; o software da etapa "Programação"; e o que é o **Mapa de
  Produção** hoje (documento? planilha? app?) — é o artefato mais central do fluxo (atravessa 4 etapas).
- Próximo: escrever os POPs na **ordem do fluxo**, começando pelo **Escopo de Venda** (Etapa 1, o gargalo).
