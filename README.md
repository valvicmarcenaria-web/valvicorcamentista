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
│   ├── validacao-orcamento.md    # BASE REAL atual (planilha): MC%, % e preços
│   ├── chapas.md                 # chapas, espessuras padrão, vidros, acabamentos
│   ├── ferragens.md              # ferragens, marcas (Hettich/Rometal/Blum), config
│   ├── custos.md                 # motor do app Valvic OS: CX, markup, MC
│   └── proposta-comercial.md     # saída ao cliente: Gold/Silver, garantia, RT
├── projetos/
│   ├── README.md                 # índice dos projetos resolvidos
│   ├── TEMPLATE.md               # formato padrão de um projeto de treino
│   └── 2025-lucas-e-ana-apto101.md  # exemplo: pipeline executivo→planilha→proposta
└── fontes/                       # arquivos originais da Valvic (fonte de verdade)
    ├── validacao_de_orcamentos.xlsx
    ├── valvic_os.html · valvic_painel_ferragens.html
    ├── valvic_garantia_comercial.pdf · valvic_parceria_rt_arquitetos.pdf
    └── exemplo_proposta_lucas_e_ana_v2.pdf · exemplo_projeto_executivo_apto101.pdf
```

## Premissas atuais

- **Material base:** MDF melamínico (classificado em branco / cor / especial).
- **Validação:** orçamento aprovado quando a **MC% fica entre 35% e 40%**.
- **Encargos reais (% do investimento):** NF 7% · parcelamento de máquina 7–8% ·
  comissão vendedor 5% · comissão produção 5% · RT 7–8% (com parceiro) ·
  margem de erro 2%.
- **Fonte de verdade:** planilha de validação (custos atuais) + biblioteca do
  Valvic OS (app em construção).
- **Estado:** taxonomia e metodologia destiladas das fontes da Valvic; trechos
  marcados com `TODO` aguardam confirmação de percentuais/regras.
