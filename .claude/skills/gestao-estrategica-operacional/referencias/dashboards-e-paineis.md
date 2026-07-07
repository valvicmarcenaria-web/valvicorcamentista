# Dashboards & Painéis Informativos Inteligentes

A Helena cria painéis que **respondem uma pergunta de gestão** — não que despejam dados.
Um bom painel é lido em segundos e leva a uma ação. Base técnica: as boas práticas de
data-viz (form-first, cor por função, acessibilidade), aplicadas ao **sistema visual Valvic**.

## O que torna um painel "inteligente"
- **Uma pergunta por visão.** Cada bloco responde algo específico ("bati o break-even?",
  "onde estão os projetos?", "o caixa aguenta o mês?"). Sem "gráfico bonito à toa".
- **Hierarquia:** o número que decide vem primeiro e maior; o detalhe, depois e menor.
- **Do dado à ação:** todo indicador tem um **estado** (bom / atenção / crítico) e, de
  preferência, o **próximo passo** implícito.
- **Contexto, não só valor:** um número sozinho não diz nada — mostrar **meta, período
  anterior ou break-even** ao lado (ex.: "MC 38% · meta 40%").
- **Atualizável:** o painel nasce ligado a uma fonte (export do Calcme, planilha) para
  não virar foto velha.

## Regra de forma — escolher o tipo certo (a cor vem por último)
Primeiro pergunte **qual o trabalho do dado**:
- **Um número-herói** (faturamento do mês, caixa hoje) → **stat tile**, não gráfico.
- **Magnitude / comparar** (faturamento por mês, custo por categoria) → **barras**.
- **Mudança no tempo** (MC% ao longo dos meses, caixa projetado) → **linha**.
- **Estado / etapa** (projetos por fase, prazos) → **status** (chips/kanban com cor+ícone).
- **Parte do todo** (composição do custo) → barras (melhor que pizza acima de 3–4 fatias).
> Se um stat tile resolve, **não faça gráfico**. O melhor gráfico às vezes é um número grande.

## Cor por função — o sistema Valvic + a paleta validada
**Cromo (identidade) × dados (legibilidade) são camadas diferentes:**
- **Cromo do painel** = identidade **Valvic**: navy `#0E2038`, dourado `#C2A05A`, cream
  `#FBFAF7`, títulos Cormorant + Inter. É o que faz "parecer Valvic".
- **Marcas de dado** = **paleta validada** (CVD-safe), porque o navy/dourado da marca é
  bonito mas **reprova** nos critérios de gráfico (baixa saturação, contraste). Regra:
  - **Série única** (o mais comum num painel de gestão) → **navy** cheio (`#16314f`),
    alto contraste e on-brand. Dourado só para **acento/linha de meta**, nunca preenchimento.
  - **Multi-categoria** (≤ 5 fatias) → paleta categórica validada, **em ordem fixa**:
    `#2a78d6` azul · `#1baf7a` água · `#eda100` amarelo · `#008300` verde · `#4a3aa7` violeta.
    Sempre com **rótulo direto** (nunca só cor).
  - **Status** (reservado, com **ícone + rótulo**): bom `#0ca30c` · atenção `#fab219` ·
    sério `#ec835a` · crítico `#d03b3b`. Nunca usar essas cores como "série".
- **Texto veste cor de texto** (ink), nunca a cor da série.
- **Validar a paleta antes de publicar** — rodar o validador do skill `dataviz`
  (`scripts/validate_palette.js`), não confiar no olho. Categórica alvo: separação CVD ≥ 12.

## Especificação das marcas (o acabamento que faz parecer profissional)
- Barras/linhas **finas**; pontas de barra arredondadas 4px ancoradas na base; linhas 2px;
  marcadores ≥ 8px; **2px de respiro** entre preenchimentos vizinhos; grade e eixos **recessivos**.
- **Rótulo direto seletivo** (o valor no fim da barra/ponto-chave), não número em todo ponto.
- **Legenda** presente sempre que houver **≥ 2 séries** (série única dispensa — o título já nomeia).
- **Linha de referência** (meta, break-even) tracejada e discreta — o "contexto" do número.

## Acessibilidade & robustez (não-negociáveis)
- Identidade **nunca só por cor** — sempre rótulo/ícone junto.
- **Existe uma tabela** por trás dos gráficos (o dado cru, para conferência/leitor de tela).
- **Modo claro por padrão**; se fizer modo escuro, é uma paleta própria (não um "flip").
- Funciona **impresso e em tela** (o painel Valvic é print-ready A4/A3, como os documentos).

## Tipos de painel na Valvic (e quando usar)
| Painel | Pergunta que responde | Onde vive |
|---|---|---|
| **Painel executivo (1 tela)** | "Como está a empresa hoje?" — KPIs + tendência + status | reunião de sócios |
| **Painel financeiro** | break-even, MC, caixa, contas a pagar/receber | fechamento (com Rodrigo) |
| **Painel de produção** | projetos por etapa (Kanban), prazos, gargalos | acompanhamento (com Deivson) |
| **Painel de pipeline** | propostas em aberto, follow-ups, conversão | comercial (com Closer) |
| **Relatório-painel** | um tema a fundo, para decisão pontual | sob demanda |

## Pipeline de construção (como a Helena entrega)
1. **Pergunta** que o painel responde + público (sócio / equipe / investidor).
2. **Dado** da fonte (Calcme export / planilha) → validar o fechamento (ver `planilhas-e-relatorios.md`).
3. **Forma** por bloco (stat tile / barra / linha / status) — cor por último.
4. **Montar** em HTML/CSS/SVG **autocontido** (sem dependência externa), padrão Valvic,
   print-ready. **Ponto de partida:** `ferramentas/painel-gestao-template.html`.
5. **Validar a paleta** (validador do `dataviz`) e **olhar o resultado** (screenshot) —
   colisão de rótulo, geometria, overflow.
6. **Publicar** (tela e/ou PDF) e **registrar** em `dados/mapa-documentos.md`.

> **Ferramenta pronta:** `ferramentas/painel-gestao-template.html` — painel de gestão Valvic
> com stat tiles, barras (com linha de break-even), linha de MC% (com meta), status de
> produção e tabela de dados. Copiar, trocar os dados, publicar.
