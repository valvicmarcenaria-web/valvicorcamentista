---
name: leitor-projetos-marcenaria
description: >-
  Olhar de marceneiro — lê projetos de móveis planejados (SketchUp, Marcenária
  Diferente, AutoCAD, renders, PDFs executivos, fotos) e levanta o QUANTITATIVO
  de material e insumos (chapas por cor/espessura, fita de borda, ferragens,
  iluminação, terceirizados), sem precisar digitar medidas uma a uma. Use quando
  chegar um projeto/imagem de móvel e for preciso estimar o material para
  orçamento. A saída alimenta o motor de orçamento (skill orcamentista-marcenaria
  / Marcos), que faz a precificação e a MC%.
---

# Olhar de Marceneiro — leitura de projetos para quantitativo

Skill especializada em **olhar um projeto de móvel e enxergar o material**, do
jeito que um marceneiro experiente faz "riscando na régua" — só que de forma
analítica e rápida. **Não pede medida item a item**: lê o desenho/render,
identifica os módulos e devolve o **quantitativo** pronto para o motor de
orçamento (Marcos) precificar.

> Complementa a skill `orcamentista-marcenaria` (Marcos). Esta levanta o
> **quantitativo**; o Marcos faz o **preço e a MC%**.

## Entradas que sei ler

- **Marcenária Diferente** (3D): render com portas / sem portas, lista de
  material, plano de corte.
- **SketchUp**: vistas 3D, cenas, prints.
- **AutoCAD / executivo**: plantas, vistas, cortes, detalhamento (PDF/imagem).
- **Renders, fotos, croquis**.

Quando houver **cotas no desenho**, usar as cotas. Quando não houver, usar as
**profundidades padrão** (cozinha inf 60 / sup 35 · roupeiro 65 · bancada 50 cm)
e estimar largura/altura pela escala/proporção, sinalizando como estimativa.

## Procedimento de leitura (o olhar)

1. **Mapear ambientes e itens.** Separar o projeto por ambiente e listar os
   móveis (itens) de cada um — como no Valvic OS (Ambiente → Itens).
2. **Para cada móvel, ler duas vistas:**
   - **Fechado** → nº e tipo de portas, acabamento aparente (linha/cor de chapa),
     puxador (perfil/cava/pulsador), frente (L×A).
   - **Aberto/sem portas** → estrutura interna: laterais, base, teto, fundo,
     **prateleiras**, **gaveteiro** (nº de gavetas), divisões, nichos, cabideiro.
3. **Classificar o acabamento** em categoria da base (Branco TX / Melamínico
   Fosco / Cristallo / Acetinato / lâmina natural…) — não a cor exata.
4. **Decompor em peças** (vocabulário: lateral, base, teto, fundo, prateleira,
   porta, frente/contra-frente/lateral/fundo de gaveta, tamponamento, painel,
   batedor) e somar **área por cor × espessura**.
5. **Converter área → chapas** (regra calibrada):
   - chapas = arredonda p/ cima de `Σárea ÷ (5,0875 m² × aproveitamento)`;
   - **aproveitamento por espessura: 15/18mm ≈ 0,82 · 6mm (fundos) ≈ 0,55**;
   - **cada cor distinta puxa ≥ 1 chapa** (cor de pouca peça rende ~68% → cauda).
6. **Fita de borda** pelas regras de faces (ver `laminacao-e-construcao.md` da
   skill Marcos), por cor, **× 1,15** de buffer.
7. **Ferragens (por contagem, sem variável):**
   - dobradiças = nº portas de giro × (altura: ≤900→2, ≤1600→3, ≤2000→4, +→5);
   - corrediças = 1 par por gaveta;
   - sistema de correr = por nº de portas (roupeiro); pistão/articulador por
     báscula; pulsador se abertura touch; puxador (perfil em m ou cava usinada).
8. **Terceirizados / outros:** porta de espelho, espelho/vidro (m²), serralheria,
   laca (m²), LED (m linear, fita+perfil).
9. **Flags de atenção:** medida a validar, ponto elétrico, usinagem especial,
   **painel ripado** (atenção redobrada à fita — fonte histórica de prejuízo).

> **Roupeiro:** seguir o checklist de `referencias/roupeiros.md` (skill Marcos)
> — sistema deslizante (RO-65 = caixaria aparente / Multi = slim, kit 2-3 portas
> / regra de ≥50cm senão vira giro), corrediça oculta (perguntar se não
> especificado), puxador SMP7000 (central 2 / extremidades 1), desempenador em
> toda porta deslizante, LED acompanha o **L** (somar as duas vistas → ~1m/prat).
> **Ripado:** calcular régua a régua (`laminacao-e-construcao.md`) — é onde mais
> se perde dinheiro. Filetagem tem custo de aplicação à parte (máquina ~R$2,50/m,
> manual ~R$4/m).

## Saída — quantitativo (formato que o motor consome)

Para cada item, produzir:

```json
{
  "ambiente": "Cozinha",
  "item": "Balcão inferior",
  "acabamento": "MDF Melamínico Fosco",
  "chapas": [ {"linha":"MDF Branco TX","espessura":"15mm","qtd":3},
              {"linha":"MDF Branco TX","espessura":"6mm","qtd":1},
              {"linha":"MDF Melamínico Fosco","espessura":"18mm","qtd":2} ],
  "fita": { "tipo":"Cor", "metros": 28 },
  "ferragens": { "dobradicas":{"linha":"Hartt","qtd":8},
                 "corredicas":{"linha":"Oculta Hartt","pares":3},
                 "sistema":null, "pulsador":{"qtd":4} },
  "iluminacao": { "led_m": 2 },
  "terceirizados": { "porta_espelho":0, "espelho_m2":0, "serralheria":0, "laca_m2":0 },
  "flags": ["usinagem cava"]
}
```

> O **Marcos** (skill `orcamentista-marcenaria`) recebe esse quantitativo, puxa
> os custos de `dados/materiais.json`, soma especulação (2%), logística e
> visitas, aplica os % do motor e devolve **preço sugerido + MC% (35–40%)**.

## Calibração e honestidade

- Estimativa rápida **erra para cima de propósito** (melhor sobrar 1 chapa que
  faltar). Sempre declarar o que é cota lida vs. estimativa.
- Calibrar continuamente contra projetos reais (`projetos/treino/` da skill
  Marcos): modelo menor (aline) e maior (luiz) são as referências atuais.

> **Estado:** v1 — método definido. A acurácia do "olhar" sobre imagens será
> afinada com projetos reais enviados pela Valvic.
