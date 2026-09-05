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

---

## ⛔ Rateio do preço por item — é por CUSTO, nunca por área de chapa

**Corrigido pelo Jonathan em 29/08/2026**, no job da Flaviana e Igor: *"a
precificação do gabinete inferior ficou superfaturada."*

Os motores da casa vinham repartindo o investimento entre os itens pela
**área de chapa** de cada um. Está errado, e o erro é grande sempre que os
itens do job são de naturezas diferentes:

| | m² de chapa | custo direto | por área | por custo |
|---|--:|--:|--:|--:|
| Armário aéreo (espelho, LED, drivers, 56 suportes) | 5,61 | R$ 3.503 | R$ 7.100 | **R$ 11.300** |
| Gabinete inferior (caixa de madeira e gavetas) | 8,15 | R$ 1.784 | R$ 10.200 | **R$ 5.700** |
| Porta de correr | 2,94 | R$ 1.415 | R$ 3.700 | **R$ 4.500** |

Área de chapa não é custo: espelho, LED, drivers, ferragem e suportes não
entram nela. O item de mais chapa e menos acessório fica caro, e o item que
carrega os acessórios fica barato — o cliente compara com o mercado e o
inferior parece superfaturado, porque **estava**.

**A regra:** o preço de cada item é `INV × custo_direto_do_item / CD`, com a
sobra de arredondamento indo para o item de maior custo. Dentro do custo
direto:

- **chapa** — dentro de cada grupo (material, espessura), a chapa comprada é
  rateada pela área que cada item ocupa **naquele grupo**. É como ela é gasta.
- **fita e filetagem** — pelo metro explícito do item; se o piso de 2,6 m/m²
  valeu, o metro é do job inteiro e aí sim só a área explica.
- **usinagem, LED, terceirizados e ferragem** — já são por item, entram direto.
- **consumíveis e logística** — não têm dono: acompanham o resto,
  proporcionalmente.

Implementado como bloco `cd_amb` em `corte-flaviana.py` e `corte-giza.py`,
com `assert abs(sum(cd_amb.values()) - CD) < 0.01` — se algum custo novo
entrar no CD e ninguém colocar no rateio, o motor quebra na hora.

> Onde os itens são irmãos (dois armários iguais, dois quartos parecidos), os
> dois rateios dão quase o mesmo número — foi o caso da Giza e Renato, que não
> se moveu. Isso não é motivo para manter o rateio por área: é só a coincidência
> de um job homogêneo.
