# Valvic — Orçamentista de Marcenaria

Repositório do agente especialista em **orçamento de marcenaria da Valvic**.
O objetivo é destilar a metodologia de cálculo de quantitativo de materiais em
uma **Skill reutilizável** do Claude Code.

## Estrutura

```
.claude/skills/orcamentista-marcenaria/
├── SKILL.md                      # definição do agente e fluxo de orçamento
├── referencias/
│   ├── estrutura-orcamento.md    # modelo de dados, categorias, flags, workflow
│   ├── chapas.md                 # chapas, vidros, acabamentos, fita (c/ preços)
│   ├── ferragens.md              # biblioteca do OS + painel Bigfer/Hettich
│   └── custos.md                 # motor de custo: CX, markup divisor, MC
├── projetos/
│   ├── README.md                 # índice dos projetos resolvidos
│   └── TEMPLATE.md               # formato padrão de um projeto de treino
└── fontes/                       # arquivos originais da Valvic (fonte de verdade)
    ├── valvic_os.html            # motor de orçamento + biblioteca
    └── valvic_painel_ferragens.html
```

## Premissas atuais

- **Material base:** MDF melamínico.
- **Motor de custo:** CX define margem mínima (não custo); preço por markup
  divisor `custoDir / (1 − margem)`; encargos (NF, RT, comissões, máquinas)
  deságuam numa MC% saudável de ~28–38%.
- **Fonte de verdade:** biblioteca do Valvic OS (catálogo + preços de compra).
- **Estado:** taxonomia e metodologia destiladas das fontes da Valvic; trechos
  marcados com `TODO` aguardam confirmação de percentuais/regras.
