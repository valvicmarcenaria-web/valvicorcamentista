# Gestão de Documentos da Valvic

Todo documento serve a uma **decisão** ou a uma **cobrança**. A Helena sabe onde cada um
está, cria os novos no padrão da casa, e mantém o ecossistema organizado.

## Onde vive cada coisa
- **Documentos institucionais / apresentações / relatórios** → pasta `painel/` do repo
  (HTML + PDF gerado). É a "gráfica" da Valvic. Inventário em `dados/mapa-documentos.md`.
- **Projetos de cliente, contratos, orçamentos** → Google Drive, **uma pasta por cliente**
  (padrão: criar a pasta em até 24h após o fechamento — responsabilidade da Assistente
  Operacional). ERP **Calcme** guarda o cadastro e os marcos do projeto (ver
  `referencias/sistema-calcme.md`).
- **Escopos e gestão de equipe** → apostila (`painel/apostila-escopos-funcao.html`).
- **Skills (conhecimento da empresa)** → `.claude/skills/` (Rodrigo, Lavinia, Closer, Helena).

## Padrão visual Valvic (para todo documento novo)
Já consolidado em `painel/*.html`. Reusar sempre:
- Cores: `--navy:#0E2038 · --gold:#C2A05A · --cream:#FBFAF7`; fontes **Cormorant Garamond**
  (títulos serifados) + **Inter** (texto). Cabeçalho navy com selo "V" e faixa dourada.
- **Print-ready:** `@page { size: A4/A3; margin:0 }`, `print-color-adjust:exact`; folha
  `.sheet` = 210×297 mm (A4) ou 420×297 mm (A3 paisagem).
- **Gerar PDF** via Playwright/Chromium (`executable_path` do chromium do ambiente,
  `--no-sandbox`, `page.pdf(prefer_css_page_size=True, print_background=True)`), conferindo
  cada página por screenshot antes de entregar.
- Rodapé: "Uso interno · Valvic Marcenaria — Vargas Decor Ltda · <mês>/<ano>".

## Nomenclatura (arquivos e PDFs)
- HTML no repo: kebab-case, descritivo — `apresentacao-walton-visual.html`.
- PDF de entrega: `Valvic_<Assunto>_<Ano>.pdf` (Title_Case) — `Valvic_Apostila_Escopos_Funcao.pdf`.
- Versões: sufixo `-vN` quando houver revisão significativa; a versão entregue é a que vale.

## Ciclo de um documento
1. **Briefing** — para quem é, que decisão apoia, o que precisa comunicar, tom (interno,
   cliente, investidor), formato (A4 leitura / A3 impressão).
2. **Rascunho** no padrão Valvic → **revisão** (números fecham? sigilo ok? tom certo?).
3. **PDF + conferência visual** → **entrega** ao destinatário certo.
4. **Registro** no `dados/mapa-documentos.md` e, se gerar tarefas, na CENTRAL.

## Confidencialidade — regra de ouro
Classificar antes de compartilhar:
- **Restrito** (financeiro, folha, proposta a investidor, contratos) → só sócios / destinatário.
- **Interno** (apostila, rotinas) → equipe conforme a necessidade.
- **Externo** (proposta comercial, portfólio) → cliente/parceiro.
Nunca misturar dado financeiro sensível em documento de circulação ampla (ex.: a apostila
é deliberadamente **sem remuneração**). Na dúvida sobre destinatário, **perguntar antes de enviar**.

## Boas práticas de organização do Drive
- Uma pasta por cliente; subpastas fixas (Contrato · Projeto · Orçamento · Fotos · Pós-venda).
- Nome do cliente + código do projeto; nada de "final_final_2".
- O que é canônico fica no lugar canônico; cópias soltas viram fonte de erro.
