# Orçamento — Armário superior de cozinha (3,02 m)

> **Status:** 🟡 Levantado em 07/08/2026. Aguarda confirmação de medidas.
> Fontes: render do projeto + foto da parede real com medição de **3,02 m**.
> Script: `corte-armario-superior-cozinha.py`

## Premissas (Jonathan, 07/08/2026)
- **Interno branco · externo cor**
- **Linha básica** (Hardt)
- **Puxadores passantes** — perfil embutido em usinagem passante
- **Custo do LED apresentado separado**
- Profundidades dadas: **armário mais alto 50 cm · mais estreito 35 cm**

## Leitura da geometria

O render mostra **dois planos de profundidade**, e é isso que os 50 e os 35 cm
descrevem: o plano de cima avança 50 e corre a parede inteira, **passando por
cima da geladeira**; o plano de trabalho recua para 35 e para onde a geladeira
começa. Por isso o módulo da geladeira "desce" mais que o resto no render — ele
é do plano de 50, não do de 35.

| Plano | Trecho | Medidas | Portas |
|---|---|---|--:|
| **50 cm** | sobre a bancada | 230 × 50 alt | 6 |
| **50 cm** | sobre a geladeira | 72 × 70 alt | 2 |
| **35 cm** | cristaleira | 72 × 60 alt | 2 (vidro) |
| **35 cm** | vão da coifa (recuo de 15) | 83 × 60 alt | 2 |
| **35 cm** | nicho do micro | 75 × 60 alt | 1 (báscula) |

Parede 302 = geladeira 72 + bancada 230. Pé-direito **2,60** e fundo do aéreo a
**1,50** — ambos estimados, ambos mexem na altura das portas.

## Quantitativo

| Material | Área | Chapas | Aproveitamento |
|---|--:|--:|--:|
| Branco 15 (caixaria) | 7,18 m² | 2 | 71% |
| Branco 18 (prateleiras) | 2,11 m² | 1 | 42% |
| Branco 6 (fundos) | 3,03 m² | 1 | 60% |
| **Cor 18** (portas e acabamentos) | 2,67 m² | 1 | 53% |
| **Total** | **15,00 m²** | **5** | **59%** |

Fita 46,22 m (22,25 cor + 23,97 branco). Ferragens R$ 1.450 — dentro delas as
**2 portas de vidro com perfil pesam R$ 560**, o item mais caro da lista.

## Custo e preço — MC 35%, sem RT

| | Custo direto | Tabela |
|---|--:|--:|
| Marcenaria | R$ 4.752,88 | **R$ 10.550** |
| Iluminação LED | R$ 1.120,00 | **R$ 2.500** |
| **Total** | **R$ 5.872,88** | **R$ 13.050** |

Escada padrão: −3% **12.650** · −5% **12.400** · −7% **12.150** (MC cai a 31,7%).

## Decisões que mexem no preço
1. **Nicho do micro na cor** (é nicho aberto, o interior aparece): +R$ 100.
   O render mostra na cor; a especificação diz interno branco. Não mudei.
2. **Portas cegas no lugar do vidro:** −R$ 1.300 (12% do custo da marcenaria).
3. **LED sem o interno da cristaleira:** R$ 2.500 → R$ 1.900.

## ⚠️ A confirmar antes de fechar
- Pé-direito e altura do fundo do aéreo (usei 2,60 / 1,50).
- Largura do vão da geladeira (usei 72) — o resto da parede é consequência.
- Porta de vidro com perfil: usei **R$ 280/folha**, cotar com o vidraceiro.
- **Fora do escopo:** coifa, micro-ondas, pontos elétricos.

## APRENDIZADO — o empacotador guloso depende da ordem de entrada

O branco 15 fechou em **3 chapas com 47%** na primeira rodada. Sub-50% é
sintoma, e aqui era do método, não do móvel: ordenando só por largura
decrescente, as 3 verticais de 50×50 ocupavam a primeira faixa e empurravam os
tampos de 230 para outra chapa. Empacotado à mão, tudo cabia em **2 chapas**.

Correção aplicada em `nest()`: varrer **quatro ordens** (largura · largura+
comprimento · comprimento · área) e ficar com a menor contagem. O branco 15
virou **2 chapas com 71%**, e o custo caiu R$ 250 — R$ 555 de preço ao cliente.

> Os 42% do branco 18 e os 53% da cor **não** são o mesmo caso: são pouca área
> contra o mínimo de 1 chapa por cor × espessura. Piso, não desperdício.
