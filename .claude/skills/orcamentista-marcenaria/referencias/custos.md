# Composição de custo — motor Valvic OS

> **Para a base de custo ATUAL e REAL da Valvic, veja
> `validacao-orcamento.md`** (a planilha que a Valvic usa hoje, com preços de
> compra e percentuais reais). Este documento descreve o motor do **app Valvic
> OS** — o sistema em construção que formaliza a mesma lógica. As duas fontes
> são coerentes: validação por MC% no fim, custo por composição no início.

Metodologia destilada do motor de orçamento (`fontes/valvic_os.html`, funções
`calcItem` → `calcAmb` → `recalc`). O cálculo sobe em três níveis:
**Item → Ambiente → Projeto**.

## Princípio central

> **"CX define margem mínima, não custo."** (comentário literal do código)

A **complexidade (CX)** de um item **não muda o custo** — ela estabelece o
**piso de margem** daquele item. O preço ao cliente é formado por **markup
divisor** sobre o custo direto.

### Níveis de complexidade (CX)

| Nível    | Margem mínima (MC) |
|----------|--------------------|
| Baixo    | 52%                |
| Médio    | 58%                |
| Alto     | 63%                |
| Premium  | 68%                |

A margem aplicada ao item é sempre `max(margem mínima do CX, margem global)`.
A margem global padrão é **40%** (campo `margemPct`).

## Nível 1 — Item

```
mat        = Σ (preço_componente × qtd)          // custo de material do item
emb        = embalagem  (% sobre mat, ou valor fixo)
imp        = imposto    (% sobre mat, ou valor fixo)
markupVal  = mat × markup%                        // markup por categoria ou item
custoDir   = mat + emb + imp + markupVal
m          = max(CX_min, margem_global)
valorCliente = custoDir / (1 − m)                 // markup divisor
```

- **Preço manual** (`precoManual`) sobrescreve o cálculo por composição.
- Separa-se **material puro** de **serviços terceirizados** (categoria
  `Serviços Terceirizados`) para análise.

> A fórmula `custoDir / (1 − m)` significa que a margem é calculada **sobre o
> preço de venda**, não sobre o custo. Ex.: custo 1000 com m=40% → preço 1667.

## Nível 2 — Ambiente

```
Σ valorCliente dos itens ativos
+ setup_ambiente / (1 − margem_global)            // setup também leva markup
+ logística:
    logBase  = logEquipe + logMat
    logTotal = logBase + logBase × descarga        // multiplicador de descarga
```

## Nível 3 — Projeto (fechamento)

```
cheio    = Σ valorCliente dos ambientes (+ setups)
nf       = cheio × nf%                              // nota fiscal
liquido  = cheio − nf
rt       = base × rt%      (base = líquido ou bruto, configurável)  // RT/parceiro (arquiteto)

Comissões:
  venda        = (bruto ou líquido) × %venda
  programação  = líquido × %prog
  coordenação  = líquido × %coord
  marceneiro   = líquido × %marc
  corte chapa  = total_de_chapas × R$/chapa         // comissão do operador de corte
  totalCom     = soma das comissões

Máquinas:
  laminação = custo/ml × ml
  corte     = custo/ml × ml
  totalMaq  = laminação + corte

custoTotal = mat + setupProj + setupAmb + visitas + logTotal
           + nf + rt + totalCom + totalMaq

MC   = cheio − custoTotal          // margem de contribuição (R$)
MC%  = MC / cheio
estratégico = cheio − desconto_manual   // preço final negociado
```

### Outros custos de projeto
- **Setup por pessoa** (Jonathan, Paulo, Programador): `horas × custo/hora`.
- **Visitas**: validação (R$250) + conferência (R$300), por quantidade.

### Saúde da margem (MC% final)

| Faixa MC%   | Leitura                                                     |
|-------------|------------------------------------------------------------|
| < 28%       | ⚠ Abaixo do ideal — revisar margem ou encargos             |
| 28% – 38%   | ✓ Saudável — cobre overhead + lucro                        |
| > 38%       | ↑ Acima da faixa — verificar competitividade               |

> **Atenção à diferença:** o markup por item (52–68% via CX) é o *bruto* sobre
> custo direto. Depois de NF, RT, comissões, logística e máquinas, ele
> **deságua** numa MC% final saudável de ~28–38%. São métricas diferentes.

## Apresentação do orçamento

1. **Quantitativo** — chapas, fita, ferragens, com origem de cada quantidade.
2. **Composição** — material, terceirizados, embalagem, imposto, setup,
   visitas, logística, NF, RT, comissões, máquinas.
3. **Resultado** — valor cheio, MC% e preço estratégico (com desconto).

> TODO Valvic: registrar os percentuais que você usa hoje (margem global, NF%,
> RT%, % de cada comissão, R$/chapa do corte, custos de máquina) ou a fonte
> consultada a cada orçamento.
