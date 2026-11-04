# Orçamento — Armário superior de cozinha (3,02 m)

> **Status:** 🔴 **FECHADO em R$ 9.700** [Jonathan 07/08] — contexto atípico, **não é referência**. Aguarda confirmação de medidas.
> Fontes: render do projeto + foto da parede real com medição de **3,02 m**.
> Scripts: `corte-armario-superior-cozinha.py` (levantamento) ·
> `build-armario-superior-cozinha.py` → `proposta-armario-superior-cozinha.pdf` (3 páginas)

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

## Proposta — 3 páginas [07/08/2026]

`build-armario-superior-cozinha.py`: escopo · **elevação frontal desenhada** · investimento.

A p.2 é o coração: uma **elevação em SVG** feita a partir do próprio levantamento, com os
dois planos em tons diferentes, as fitas de LED em dourado, a geladeira em tracejado (fora
do escopo) e as cotas por módulo. Não é ilustração — é **o que precisa ser aprovado**, já
que as alturas são estimadas e a medição final ainda vai acontecer.

Duas correções feitas no desenho depois de olhar o render:
- as etiquetas *PLANO 50/35* caíam **dentro de um módulo** e liam como nome dele → viraram
  **legenda** no rodapé da figura;
- o vazio sob o módulo da geladeira não se explicava → entrou a **geladeira em tracejado**.

Condições: **45 dias corridos** · garantia **10 anos** em estrutura e ferragens (linha
Silver: 10 anos, com 2 anos em corrediças — que este móvel **não tem**) · validade 7 dias.

> ⚠️ Prazo e validade foram **assumidos por mim**, não ditados. O padrão da casa em
> `proposta-comercial.md` é 45–60 dias úteis para projeto completo; aqui é um ambiente só.

## FECHAMENTO — R$ 9.700 [Jonathan 07/08/2026]

> ⚠️ **Contexto atípico, declarado pelo Jonathan. Não usar como referência de preço.**

Divisor calibrado: `5.872,88 ÷ 9.700 = 0,60545` → **MC 19,5%** no cartão.
Contra 35,0% da tabela de R$ 13.050. Cai na faixa **Crítico** (até 25%) da
`validacao-orcamento.md` — a que existe só para gerar caixa urgente.

| | Preço | MC |
|---|--:|--:|
| Tabela calculada | 13.050 | 35,0% · R$ 4.569 |
| **Fechado — cartão** | **9.700** | **19,5% · R$ 1.889** |
| **Fechado — transferência/PIX** | **9.700** | **26,7% · R$ 2.587** |

### A forma de pagamento virou a variável principal

A taxa de maquininha (~7,2%) mora dentro do `a = 0,162`. A R$ 9.700 ela vale
**R$ 698** — **37% de toda a MC do cartão**. Por isso a proposta **não traz a
escada de pagamento**: o −7% levaria a MC a 14,8%. Entrou no lugar um bloco de
**condição fechada** com 50% + 50% em transferência ou PIX.

### Alavancas, se precisar recuperar margem sem mexer no preço

| Alavanca | Custo | MC |
|---|--:|--:|
| Portas cegas na cor no lugar do vidro | −R$ 591 | 25,6% |
| LED sem o trecho da cristaleira | −R$ 273 | 22,3% |
| As duas | −R$ 864 | 28,4% |
| As duas + transferência | | **35,6%** |

> A alternativa de porta cega **saiu da p.2**: ela prometia "R$ 1.300 mais barato",
> número que existia contra a tabela. A R$ 9.700 aplicar aquele desconto levaria a
> MC a 17,1%. Virou nota técnica sobre o vidro e o LED interno, sem promessa de preço.

### Rateio apresentado
Marcenaria **R$ 7.850** · LED **R$ 1.850** — proporcional à tabela (80,8% / 19,2%),
para o LED continuar em linha própria como pedido. **Sem desconto riscado**: o
cliente nunca viu os R$ 13.050, então não há por que expor uma redução de 25,7%.
