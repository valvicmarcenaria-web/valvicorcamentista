# Projeto: Karina Ramos — Escritório (Home Office)

> Orçamento Valvic (Lavinia). Projeto de interiores **IONAH PINHO arquitetura &
> interiores** (CAU 29.315-6). Cliente **Karina Ramos** — Rua Sergipe, 440,
> ap.101, Funcionários, BH/MG. Conteúdo: **MARCENARIA**. Folha JUN/2026, rev. 0.
> Fonte: `projeto-karina-ramos-escritorio.pdf` (9 pranchas, esc. 1/20).

## 1. Demanda

- **Ambiente:** escritório / home office em **L**.
- **Descrição:** aparador-bancada baixo com baú + gavetas + porta de correr (M1);
  bancada de trabalho apoiada no aparador e num pé lateral (M2); armário aéreo
  com torre de nichos piso-teto e prateleira iluminada (M3); armário suspenso
  com nicho lateral (M4).
- **Acabamento:** **dois amadeirados foscos** — **MDF Linho Belga (Duratex)** na
  estrutura/portas e **MDF Savana (Guararapes)** nos nichos, tampo e prateleiras.
  Ambos classificados como **MDF cor** na base de custos.
- **Pegas:** sem puxador aparente — **cava esculpida no próprio MDF** (M1) e
  **chanfro no topo da porta** (M3/M4). Usinagem CNC.
- **Observações do projeto:** transferir a tomada atrás do M1 para o tampo (caixa
  de tomada com tampa articulada); levar energia da torre de nichos para a
  iluminação LED embutida (perfil metálico + tampa acrílica); +1 tomada na
  lateral da bancada.

## 2. Módulos e medidas

Medidas em **cm** (L × A × P). Lidas das elevações/cortes (esc. 1/20).

| # | Módulo | L | A | P | Acabamento | Composição |
|---|--------|----|----|----|-----------|-----------|
| M1 | Aparador baixo (bancada-baú) | 255 | 72 | 48 | Linho Belga | baú c/ tampa basculante (115) + 3 gavetas + 1 porta de correr s/ prateleira |
| M2 | Bancada de trabalho | 140 | 76 | 50 | Savana | tampo grosso (~4 cm) apoiado no M1 + 1 pé de apoio lateral |
| M3 | Aéreo + torre de nichos | 140 + 55 | até 255 | 36 | LB (estrutura/portas) + Savana (nichos/prateleira) | aéreo 4 portas de giro + prateleira c/ LED + torre de nichos piso-teto (4 nichos) + armário embaixo (1 porta) |
| M4 | Armário suspenso + nicho | 150 + 50 | 85 | 42 | LB (armário) + Savana (nicho) | 3 portas de giro + nicho lateral (2 vãos) |

> ⚠ **Confirmar (não trava o orçamento, ajusta ±1 chapa):** altura do **aéreo do
> M3** — as cotas do corte se sobrepõem ao 76 da bancada; adotei **70 cm**.
> Forramento dos nichos do M3 adotado como **caixa em Savana recuada 2 cm**
> (interpretação de "nichos recuados 2 cm em relação à estrutura").

## 3. Quantitativo de chapas (estimativa de orçamento)

Chapa **2750 × 1850 mm** (5,0875 m²). Aproveitamento 15/18 mm ≈ 0,82 · 6 mm ≈
0,55. Cada cor×espessura puxa ≥ 1 chapa. Decomposição peça a peça em
`/quantitativo` (script). Erra para cima.

| Cor / espessura | Área peças (m²) | Chapas |
|-----------------|-----------------|--------|
| Linho Belga 6 mm (fundos) | 6,3 | 3 |
| Linho Belga 15 mm (estrutura, portas de giro, gavetas) | 16,3 | 4 |
| Linho Belga 18 mm (porta de correr, prateleiras) | 1,8 | 1 |
| Savana 6 mm (fundo nicho M4) | 0,4 | 1 |
| Savana 15 mm (forros dos nichos M3) | 3,9 | 2 |
| Savana 18 mm (tampo bancada, prateleira LED) | 2,3 | 1 |
| **Total** | | **12 chapas** |

Custo chapas (MDF cor): 4×R$300 (6mm) + 6×R$500 (15mm) + 2×R$600 (18mm) = **R$ 5.400**.

## 4. Fita de borda

| Cor | Metros (já ×1,15) |
|-----|-------------------|
| Cor (Linho Belga + Savana) | ~110 m |

Fita-material: 110 × R$3 = **R$ 330** · Filetagem (máquina, R$2,5/m): **R$ 275**.

## 5. Ferragens e acessórios

| Item | Qtd | Critério | R$ |
|------|-----|----------|----|
| Corrediça oculta Hardt | 3 pares | 1 par/gaveta (M1) | 210 |
| Pistão c/ amortecimento | 2 | tampa basculante do baú (M1) | 60 |
| Sistema de correr leve | 1 | porta de correr do M1 | ~200 |
| Dobradiças Hardt | 18 | 2/porta (4 M3 aéreo + 1 M3 base + 3 M4 = 8 portas) + folga | 144 |
| Cava usinada (pega) | 4 | frentes do M1 (gavetas + porta) | 200 |
| LED COB (fita+perfil) + sensor | 3 m + 1 | prateleira M3 + nicho topo | 500 |
| Suportes de prateleira | cj | prateleiras móveis | 20–30 |

> Padrão Linha Gold: corrediça **oculta Hardt** (slow-motion). Linha Silver troca
> por **telescópica** (garantia 2 anos na corrediça).

## 6. Composição de custo e fechamento (validação por MC%)

Caixa/estratégia: **projeto pequeno → MC alvo 30%** (decisão do Jonathan).
RT = **0** (sem acordo de RT com a arquiteta; ver nota). Percentuais calibrados
(planilha recente): NF 4% · parcelamento 8% · vendedor 3% · comissão produção
4,3% (prog 0,8 + coord 1,0 + marc 2,5) · serra 0,5% · manut. 0,5% · erro 2% ·
visita R$250.

| Componente | R$ |
|------------|----|
| Material (chapas + fita + filetagem + ferragens + LED) | ~6.560 |
| Consumíveis/fixação (~2%) | 200 |
| Logística (carretos + equipe, BH/Funcionários) | 600 |
| Embalagem | 50 |
| Visitas | 250 |
| **fixedR (base do markup)** | **~8.400** |
| Terceirizados (vidro/serralheria) | 0 |

**Fórmula:** `Inv = fixedR / (1 − a − liqF·b − mc)`, a = encargos s/ bruto (18%),
b = encargos s/ líquido (4,3%), liqF = 1 − NF − parc (0,88), mc = 0,30.

→ **Preço cheio (Gold) ≈ R$ 17.500 · MC 30,0%.**

## 7. Proposta (preço ao cliente)

| Linha | Descrição | Preço |
|-------|-----------|-------|
| **Gold** | Corrediça oculta Hardt, garantia 10 anos | **R$ 17.500** |
| **Silver** | Corrediça telescópica (garantia 2 anos na corrediça); demais igual | **~R$ 16.450** |

**Pagamento** (tabela Valvic): 30% entrada + 10× cartão · 50%+8× (−3%) · 70%+6×
(−5%) · **70% à vista + transferência (−7%) ≈ R$ 16.275**.
**Prazo:** 45–60 dias úteis. **Garantia:** 10 anos (estrutura + ferragens).
**Validade:** 2 dias úteis.

> **Cenário com RT 10% (se houver acordo com a IONAH PINHO):** preço cheio sobe
> para **≈ R$ 21.300** mantendo MC 30%.

## 8. Otimização (versão inteligente, se precisar baixar)

- **Tampo da bancada (M2):** 4 cm em dupla chapa → fazer **18 mm com
  engrossamento só na borda aparente** (economiza ~½ chapa Savana).
- **Forro dos nichos (M3):** nichos com **fundo em Savana** apenas (em vez de
  caixa forrada recuada) → economiza ~1 chapa Savana 15 mm + fita.
- **Porta de correr (M1):** manter; sistema leve já é econômico.
- LED: manter só na prateleira do M3 (corta o LED do nicho).

## 9. Notas de metodologia

- **Dois amadeirados de cores diferentes** (Linho Belga + Savana) → cada cor puxa
  suas chapas; a Savana, mesmo com pouca área, abre chapa própria por cor (regra
  "cada cor ≥ 1 chapa") e ainda sofre **cauda** por serem muitas peças pequenas
  (forro de nicho) → arredondei a Savana 15 mm para 2 chapas.
- **Pegas integradas (cava/chanfro)** zeram o custo de puxador-ferragem, mas são
  **usinagem CNC** — hoje dentro da margem operacional (lancei só a cava usinada
  do M1 como referência).
- **Projeto de arquiteta ≠ RT automático.** Precedente Ed. Luxemburgo (arq.
  envolvida, RT = 0). Tratar RT como decisão comercial, não premissa.
- **Tampo "4 cm" e baú basculante**: confirmar se o tampo é chapa dupla cheia ou
  engrossamento de borda — muda ~½ chapa.
