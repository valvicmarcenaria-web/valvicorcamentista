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

> ✅ **Confirmado pelo cliente:** altura do **aéreo do M3 = 70 cm**; **tampo da
> bancada (M2) = chapa dupla (~4 cm)**; forramento dos nichos do M3 = **caixa em
> Savana recuada 2 cm**. Estes parâmetros são o **build Gold (cheio)**.

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

Caixa/estratégia: projeto pequeno. **RT = 10% sobre o líquido** (acordo com a
arq. Ionah Pinho — **confirmado**). Percentuais calibrados (planilha recente):
NF 4% · parcelamento 8% · vendedor 3% · comissão produção 4,3% (prog 0,8 + coord
1,0 + marc 2,5) · serra 0,5% · manut. 0,5% · erro 2% · visita R$250.

| Componente | Gold (cheio) | Silver (enxuto) |
|------------|------|------|
| Material (chapas + fita + filetagem + ferragens + LED) | ~6.560 | ~5.910 |
| Consumíveis/fixação (~2%) | 200 | 200 |
| Logística (BH/Funcionários) | 600 | 600 |
| Embalagem + Visitas | 300 | 300 |
| **fixedR** | **~8.400** | **~7.750** |
| Terceirizados | 0 | 0 |

**Fórmula:** MC = (Inv − custo total)/Inv, com a = encargos s/ bruto (18%),
b = encargos s/ líquido (4,3% + **RT 10% = 14,3%**), liqF = 1 − NF − parc (0,88).

→ **Preços fechados** (MC subida +4 pts em cada versão) e MC% real **com RT**:

| Linha | Preço | MC% real (c/ RT) |
|-------|-------|------------------|
| **Gold** (build cheio) | **R$ 21.500** | **30,4%** |
| **Silver** (build enxuto) | **R$ 17.500** | **25,1%** |

> **Leitura:** com RT, o Gold a R$21.500 recompõe a MC saudável (**30,4%**,
> dentro da faixa ideal); o Silver a R$17.500 fica em **25,1%** (piso "ruim" —
> aceitável como versão de entrada/indicação). O RT (~10% do líquido) é repassado
> à arquiteta. Subir +4 pts custou ~R$2.000 no Gold e ~R$1.500 no Silver de preço.

## 7. Proposta (preço ao cliente)

| Linha | Descrição | Preço |
|-------|-----------|-------|
| **Gold** | Build cheio: corrediça **oculta Hardt**, tampo em chapa dupla, nichos forrados em Savana, LED na prateleira e nos nichos. Garantia **5 anos (Hardt)**. | **R$ 21.500** |
| **Silver** | Build enxuto: corrediça **telescópica** (garantia 2 anos na corrediça), tampo **18 mm c/ engrossamento de borda**, nichos **só com fundo Savana**. **LED na prateleira E nos nichos** (igual ao Gold — exigência do projeto). | **R$ 17.500** |

Diferença Gold↔Silver: **R$ 4.000 (−19%)** — justificada por escopo real, não só margem.

**Pagamento** (tabela Valvic): 30% entrada + 10× cartão · 50%+8× (−3%) · 70%+6×
(−5%) · **70% à vista + transferência (−7%)** → Gold ≈ **R$ 20.000**.
**Prazo:** **60–70 dias úteis**. **Garantia:** **até 5 anos** (Hardt, na Completa) /
2 anos (telescópica, na Essencial) — política escalonada por ferragem.
**Validade:** 7 dias. **RT** repassada à arquiteta conforme cronograma.

## 8. Diferença construtiva Gold × Silver (o que muda o custo)

| Item | Gold (cheio) | Silver (enxuto) | Economia |
|------|--------------|-----------------|----------|
| Corrediça (3 gavetas M1) | Oculta Hardt | Telescópica | ~R$90 |
| Tampo da bancada (M2) | Chapa dupla (~4 cm) | 18 mm + engrossamento de borda | ~½ chapa |
| Forro dos nichos (M3) | Caixa forrada em Savana recuada | Só fundo em Savana | ~1 chapa Savana 15 + fita |

> **LED igual nas duas versões** (prateleira + nichos) — está no escopo de ambas, não é
> diferencial (correção: o projeto exige LED também nos nichos). Já estava no custo do Silver,
> então a MC de 25,1% não muda.

## 9. Notas de metodologia

- **Dois amadeirados de cores diferentes** (Linho Belga + Savana) → cada cor puxa
  suas chapas; a Savana, mesmo com pouca área, abre chapa própria por cor (regra
  "cada cor ≥ 1 chapa") e ainda sofre **cauda** por serem muitas peças pequenas
  (forro de nicho) → no Gold arredondei a Savana 15 mm para 2 chapas; o Silver
  (nicho só com fundo) volta a 1 chapa.
- **Pegas integradas (cava/chanfro)** zeram o custo de puxador-ferragem, mas são
  **usinagem CNC** — hoje dentro da margem operacional (lancei só a cava usinada
  do M1 como referência).
- **RT em projeto pequeno corrói MC.** O RT (10% do líquido ≈ R$2 mil) derrubaria
  a MC de ~30% para ~26% (Gold) se o preço ficasse em R$19.500. Decisão: **subir o
  preço** para recompor a margem (Gold R$21.500 → MC 30,4%; Silver R$17.500 → MC
  25,1%). Aprendizado: em projeto pequeno com RT, repassar o RT no preço — não
  absorver na margem.
- **Build Gold vs Silver como alavanca de gap:** abrir a diferença de preço entre
  versões fica saudável quando o Silver é **realmente** mais enxuto (escopo), não
  só desconto — senão a MC do Silver desaba (17,5% no mesmo build vs 21,0% enxuto).
