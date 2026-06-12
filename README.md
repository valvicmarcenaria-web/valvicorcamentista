# Valvic — Orçamentista Estratégico de Marcenaria

Repositório da **Skill** do Claude Code que destila a metodologia de orçamento da
**Valvic Marcenaria**. É um **agente único e estratégico** que cobre o ciclo
completo, em 3 fases:

1. **Olhar** — lê o projeto (executivo, render, SketchUp, Marcenária Diferente,
   fotos) e levanta o **quantitativo** (chapas por cor/espessura, fita, ferragens,
   iluminação, terceirizados).
2. **Preço** — precifica com a base de custos e fecha por **MC%** (ideal 35–40%).
3. **Estratégia** — situação de caixa, versões mais enxutas (assinada × inteligente)
   e proposta.

> Convergência das antigas personas *Lavinia* (o olhar) + *Marcos* (o preço) numa
> só skill. **Skill ≠ agente:** aqui é um playbook de conhecimento; um subagente
> (execução em lote/paralelo) é uma camada opcional para o futuro.

## Estrutura

```
.claude/skills/orcamentista-marcenaria/
├── SKILL.md                      # agente estratégico, 3 fases (Olhar→Preço→Estratégia)
├── referencias/                  # método, leitura, custos, otimização, proposta
│   ├── roupeiros.md              # modulação, sistemas deslizantes, checklist
│   ├── laminacao-e-construcao.md # fita por peça, gaveta (6 peças), ripado, filetagem
│   ├── otimizacao-custos.md      # gerar versões enxutas (atacar mão de obra)
│   ├── validacao-orcamento.md    # modelo MC%, % reais, situação de caixa
│   ├── notas-marcos-planilha.md  # aprendizados da planilha real
│   └── (chapas, ferragens, custos, proposta-comercial, posicionamento, ...)
├── dados/materiais.json          # base de preços de compra (fonte de verdade)
├── ferramentas/
│   ├── validacao-orcamento.html  # O APP oficial (MC%, caixa, biblioteca editável)
│   └── (motor-orcamento, base-materiais, tabela-de-valores — apoio/legado)
├── projetos/                     # resolvidos + treino (Lucas&Ana, Camila, calibrações)
└── fontes/                       # originais da Valvic (planilha, OS, painel, PDFs)
```

## Premissas atuais

- **Material base:** MDF melamínico (categorias por acabamento, não cor exata).
- **Validação por MC%** (de trás para frente): material + operacional +
  terceirizados + venda + margem de erro → MC. **Ideal 35–40%**, ajustável pela
  **situação de caixa** (crítico ≤25 · ruim ≤30 · normal 30–37 · bom 37–45 · ótimo >45).
- **Ferramenta oficial:** o app `ferramentas/validacao-orcamento.html`.
- **Calibração contínua** contra projetos reais (ver `projetos/treino/`).
- **Fronteira aberta:** custo/m de corte na CNC (frisos vazados/usinagem) — hoje
  dentro da margem operacional.

## Instalar na base global

```bash
bash install-skills.sh   # copia a skill para ~/.claude/skills (exclui fontes/)
```
