# Proposta visual e identidade — Vitor

Entrega definida (jun/2026): **Brand Template no Canva + autofill**. A proposta sai
100% na identidade do Jonathan (designer); o Vitor preenche via dados.

## Leitura da identidade atual (das propostas do Jonathan no Canva)

- **Formato:** A4 retrato, multipágina (3–7 páginas conforme o porte).
- **Cor de marca:** faixa/destaque em **dourado mostarda**; fundo claro; texto escuro.
- **Tipografia:** **serifa elegante** para nomes/títulos (estilo Cormorant) + sans
  para corpo. (Espelhado nas ferramentas internas: Cormorant Garamond + DM Sans.)
- **Capa:** "proposta especial para [Nome]" + render grande + logo **Valvic** + ícone estrela.
- **Tom visual:** premium, limpo, fotográfico (render/foto ocupa muito espaço).

## Estrutura-mestre da proposta (páginas)

1. **Capa** — nome do cliente + render do projeto + logo.
2. **Conexão** — sonho do cliente + frase específica do projeto (personalização).
3. **Configuração técnica** — cards de ferragens/sistemas/espessuras (feature→valor).
4. **Cases** — desafios resolvidos com foto.
5. **Linha do tempo + "Por que a Valvic"**.
6. **Investimento** — versões (Completa→Essencial), prazo, condições (escada), garantia.

## Campos de autofill (o que o Vitor injeta no Brand Template)

Mapear estes campos no template do Canva (data fields):
- `cliente_nome`, `projeto_titulo`, `data`, `validade`
- `render_principal` (imagem), `renders_secundarios[]`
- `conexao_texto` (parágrafo personalizado do projeto)
- `itens[]` → { ambiente/peça, descrição em valor, versão, preço }
- `versoes[]` → { nome ("Completa"/"Essencial"), descrição, preço }
- `prazo`, `condicoes_pagamento` (escada), `garantia_tempo` (derivado da ferragem)

Origem dos dados: **JSON do validador da Lavinia** (escopo + preço + ferragem) +
briefing do cliente (nome, conceito, renders).

## Caminho operacional (como o Vitor gera)

1. Jonathan designa **uma proposta-mestre** (a melhor) → vira **Brand Template** no
   Canva com os campos acima. *(passo único de setup; pode exigir Canva Pro/Teams)*
2. Vitor recebe o JSON da Lavinia + briefing → monta o **dataset** (texto de valor,
   versões, condições, garantia derivada).
3. Vitor gera a proposta via **autofill / create-design-from-brand-template** (MCP Canva).
4. Jonathan dá o **acabamento final** (ajuste fino de imagem/layout) e exporta **PDF**.
5. **QA** (checklist do SKILL) antes de enviar.

> Ferramentas MCP Canva úteis: `search-brand-templates`, `get-brand-template-dataset`,
> `create-design-from-brand-template`, `export-design`. Fallback sem brand template:
> `start-editing-transaction` + `perform-editing-operations` para preencher campos
> numa cópia do design-mestre.

## Melhorias acordadas para a proposta-mestre (aplicar no template)

1. **QA de dados** — eliminar resíduos de template (já vazou "Vargas Decor"); um
   campo de nome único propagado em todas as páginas.
2. **Garantia dinâmica** por ferragem (2/5/10/vitalícia) — não fixar "10 anos".
3. **Corrigir termos:** "Premiun"→Premium, "harth"→**Hardt**.
4. **Abrir no cliente** (conexão), não na empresa.
5. **Versões nomeadas por valor** e ordenadas cara→barata.
6. **Validade por perfil** (premium 5–7 dias / rápido 48h).
7. **Personalização** com frase específica do projeto.

## Templates no Canva (criados jun/2026)

| Template | Canva ID | Uso |
|---|---|---|
| **MODELO — Proposta Valvic (Vitor)** | `DAHMsJxsuhE` ([ver](https://www.canva.com/d/DOc6GSXnxk33_kc)) | Projetos grandes / casa inteira |
| **MODELO ENXUTO — Proposta Valvic (Vitor)** | `DAHMsEfQNas` ([ver](https://www.canva.com/d/Z4tsP3oAXOpXLCb)) | Projetos pequenos (1–2 ambientes, ex.: Regina) |

Base: cópia da `proposta_bruna_ferreira` (`DAHKUR7n8Yo`). Ambos já têm placeholders
`{{NOME DO CLIENTE}}`, `garantia - {{ANOS}} anos`, `Investimento total - R$ {{TOTAL}}`
e typos corrigidos (Premium, Hardt, Laminação, Espessuras de painéis).

### Element IDs reutilizáveis (para autofill via MCP)
- Capa nome: `PB2PRdKRTQVKcmq8-LBRmKPSmH1SKzz2l`
- Garantia (selo): `PBxslyLM2wlZc8Yx-LBC987f5h8kznwRY`
- Investimento total: `PBxslyLM2wlZc8Yx-LBBLKCF5rH9q1YJd`
- Validade/prazo: `PBxslyLM2wlZc8Yx-LBQGXh0pwsSjBv2n`
- Tabela investimento (pág. 6): TABLE `PBxslyLM2wlZc8Yx-LBLlQw4sLNxvkzB0` (células via replace_text)

### LIMITAÇÃO conhecida (Canva MCP)
A API **não adiciona nem remove linhas de tabela** — só edita texto de célula. Logo:
- Gerar proposta = preencher células + nome/garantia/total/validade (automatizável).
- **Reduzir linhas** (master grande → 1 ambiente) exige ajuste manual único. Por isso
  o **MODELO ENXUTO**: o Jonathan apara as linhas extras **uma vez** (deixa 1–2), e o
  Vitor autofila projetos pequenos sem trabalho manual.

### Fluxo de geração (por cliente)
1. Escolher master (grande/enxuto) pelo porte → `copy-design` → "proposta_[cliente]".
2. `start-editing-transaction` → `perform-editing-operations` (nome, células, garantia
   derivada da ferragem, total, validade) → aprovação → `commit-editing-transaction`.
3. `export-design` (PDF) → QA → enviar.

## Ativos pendentes (do Jonathan / Drive)

- **MODELO ENXUTO:** aparar a tabela para 1–2 linhas (ajuste manual único no Canva).
- **Documento de garantia:** só o de **10 anos** (Gold) está desenhado. Criar as
  variações **2 / 5 anos / vitalícia** a partir dele (muda o tempo e a linha) — ver
  `garantia.md` (política escalonada por ferragem).
- **Logo, paleta exata e fontes** oficiais: não há Brand Office — identidade hoje
  inferida das propostas (`identidade-marca.md`).

## ⚠️ Gotcha ao reaproveitar o template Premium (cravado 08/07/2026 — Clínica Nura)

O HTML da proposta tem **JS** que, ao abrir no navegador, preenche os campos
(`.token[data-key]`, imagens) a partir de um objeto `DEFAULTS` **e** do
`localStorage` (chave `SK`). Isso **sobrescreve o texto estático** — então editar
só o HTML estático NÃO basta. Ao clonar o template para um novo cliente:

1. **Trocar a chave `SK`** para uma única por cliente (ex.: `valvic_nura_clinica`).
   Senão o navegador carrega os dados salvos de OUTRA proposta — bug real: abriu a
   proposta da Nura e apareceu Kênia & Fábio.
2. **Atualizar TODOS os `DEFAULTS`** (nome, projeto, data, ferragem, material,
   acabamento, depoimento/autor/projeto/caption, prazo, garantia, URLs das imagens) —
   não só o texto estático.
3. **Testar no navegador** (não só no WeasyPrint, que ignora o JS e mostra o estático).
