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
3. **Corrigir termos:** "Premiun"→Premium, "harth"→**Hartt**.
4. **Abrir no cliente** (conexão), não na empresa.
5. **Versões nomeadas por valor** e ordenadas cara→barata.
6. **Validade por perfil** (premium 5–7 dias / rápido 48h).
7. **Personalização** com frase específica do projeto.

## Ativos pendentes (do Jonathan / Drive)

- **Proposta-mestre** a designar (qual vira o Brand Template).
- **Documento de garantia** (só o de **10 anos** está desenhado — Drive). Criar as
  variações 2/5 anos e vitalícia a partir dele (muda só o tempo).
- **Logo, paleta exata e fontes** oficiais (confirmar com o Jonathan para fixar o
  brand system; hoje inferido das propostas).
