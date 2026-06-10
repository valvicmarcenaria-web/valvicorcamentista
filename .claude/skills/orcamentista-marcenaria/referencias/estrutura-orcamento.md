# Estrutura do orçamento (modelo de dados Valvic OS)

Hierarquia do orçamento no Valvic OS (`fontes/valvic_os.html`, objeto `OS`):

```
Projeto
└── Ambiente            (toggle ativo/inativo · setup · logística · descarga)
    └── Item            (CX · descrição · embalagem · imposto · preço manual)
        └── Componente  (categoria · produto · variação · preço · qtd)
```

## Componente

Cada componente referencia um produto da **biblioteca** por:
`{ cat, produto, variacao, preco, qtd }`.

Categorias e unidades (ver `chapas.md`, `ferragens.md`):

| Categoria               | Unidade |
|-------------------------|---------|
| Chapas                  | chapa   |
| Portas de Vidro         | folha   |
| Portas de Passagem      | un      |
| Ferragens               | un      |
| Acabamentos             | m       |
| Serviços Terceirizados  | serv    |

### Serviços Terceirizados (preços de referência)
Serralheiro (padrão 800 · complexo 1400) · Vidraceiro (600 · 1100) ·
Eletricista (ponto 350 · completa 900) · Laca/Pintura (peça 180 · projeto 1200) ·
Estofador (cabeceira 650 · completo 1800) · Outros (avulso 500).

## Taxonomia técnica (escopo de venda — sem valores)

**Materiais (acabamento aparente):** Melamínico · Laca · Lâmina Natural ·
Serralheria · Espelho · Vidro · Tecido/Estofado · Iluminação.

**Flags de item** (sinalizam risco/atenção no escopo):
- ⚠ Medida a validar · 📐 Alteração de layout · 🟡 Material especial ·
  💡 Ponto elétrico · 🔧 Usinagem especial · 🔴 Serviço terceirizado.

**Tipos de ambiente:** Cozinha · Área de Serviço · Sala de Estar ·
Sala de Jantar · Quarto/Suíte · Closet/Roupeiro · Home Office ·
Banheiro Social · Banho Suíte · Área Gourmet · Varanda · Garagem · Outro.

**Checklists de conferência em obra** existem por tipo de ambiente
(ex.: Cozinha confere pontos de gás, hidráulicos, nicho de geladeira;
Closet confere sapateira, passador de calça, cabideiro). Ver o objeto
`checksPorTipo` na fonte.

## Ciclo do pedido (workflow)

`Escopo → Conferência em obra → Programação → Lista de compra`, seguido dos
status de Pedido (Aguardando produção → Em produção → Pronto → Entregue →
Encerrado) e de PCP (Fila de corte → Em corte → Fabricação → Qualidade →
Liberado → Instalação → Concluído).

## Funil comercial (CRM)

Atração → Qualificação → Briefing/Visita → Proposta → Follow-up →
Fechamento → Pós-venda. Origens típicas: Arquiteto, Indicação, Instagram, Site.

## Ferramentas e pipeline ATUAIS (estado real hoje)

A Valvic gerencia orçamentos hoje em três peças (o Valvic OS é o app em
construção que pretende unificá-las):

1. **CalcMe** (`app.calcme.com.br/orcamento`) — front-end de pipeline/CRM dos
   orçamentos. Lista com colunas: `# · Status · Data · Cliente · Entrega ·
   Relacionamento · Valor · Ações`. Entrega normalmente "À Combinar";
   relacionamento por WhatsApp/e-mail.
2. **Planilha de validação** (`fontes/validacao_de_orcamentos.xlsx`) — cálculo
   de custo/MC% por ambiente (ver `validacao-orcamento.md`).
3. **Proposta em PDF** (Gold/Silver) — saída ao cliente (ver
   `proposta-comercial.md`).

### Status reais do orçamento no CalcMe

`Novo Orçamento → Apresentação → Em negociação → Follow-up → Contrato →
Produção`.

> Volume de referência (jun/2026): orçamentos com ticket de ~R$4,5 mil a
> R$400 mil, a maioria de alto padrão. Esse é o funil real que o agente
> orçamentista alimenta.

> Esta estrutura é o "esqueleto" que o agente preenche ao orçar: identifica o
> ambiente (tipo), decompõe em itens, atribui CX e componentes da biblioteca,
> marca flags e segue para o quantitativo e o custo (`custos.md`).
