# Valvic — Orçamentista de Marcenaria

Repositório do agente especialista em **orçamento de marcenaria da Valvic**.
O objetivo é destilar a metodologia de cálculo de quantitativo de materiais em
uma **Skill reutilizável** do Claude Code.

## Estrutura

```
.claude/skills/orcamentista-marcenaria/
├── SKILL.md                 # definição do agente e fluxo de orçamento
├── referencias/
│   ├── chapas.md            # MDF melamínico, espessuras, fita de borda
│   ├── ferragens.md         # dobradiças, corrediças, puxadores, acessórios
│   └── custos.md            # composição de custo e precificação por demanda
└── projetos/
    ├── README.md            # índice dos projetos resolvidos
    └── TEMPLATE.md          # formato padrão de um projeto de treino
```

## Premissas atuais

- **Material base:** MDF melamínico (BP).
- **Precificação:** por demanda específica (sem tabela fixa universal).
- **Estado:** metodologia e exemplos em construção colaborativa; trechos
  marcados com `TODO` aguardam definição da Valvic.
