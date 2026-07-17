# Orçamento — LM / SPE Nova Lima 1 (Painéis + Pérgola) — comercial

**Cliente:** SPE Nova Lima 1 · **Projeto:** arq. Lodi Motta / JBA Arquitetura · **Local:** Nova Lima–MG · **Etapa:** Executivo
**Pranchas:** MOB 01 (Painel Corretores/Pilar, R01) + MOB 02 (Painel/Pérgula Gourmet-Lounge, R00).
**Acabamentos:** MDF Arauco Realce **Cravo Trend** (painéis/aparente) · **Moscada Matt** (móveis/caixa interna) · **MDF madeirado** (revestimento da pérgola + forro).

## Método
Cotas lidas do **vetor do CAD** (planta + elevações + cortes) — calcular, não estimar. Alturas de painel **2,62 m** (confirmado). `corte-lm.py`.

## PÉRGOLA (metalon #10×5) — exato
- Cadeia de cotas da planta: **28 faces de 8 cm** (17×12 + 9×13 + 1×14 de vão) → **28 ripas**; vão total 563 cm.
- Comprimento de cada ripa = projeção da pérgola = **309 cm**. 2×3,09 = 6,18 > 6 m → **1 barra por ripa**.
- **28 barras** de 6 m × R$ 150 + **R$ 150 frete dedicado** (1 entrega) = **R$ 4.350**.
- Revestimento das ripas em MDF madeirado (perfil acabado ~15×8): ~40 m².

## PAINÉIS (Cravo Trend) — parede a parede
**MOB 02:** E05 4,27 + Topo 2,946 + Copa 3,384 (2 portas + painel) + Corredor pérgola 5,63 + E03 1,42 + Hall 1,57 + IS frente 1,86 + retornos/faces IS 2,937 = **24,0 m × 2,62 = 62,9 m²**.
**MOB 01:** Corretor backdrop 8,175 × 3,85 (faixa 4×204,4 h=125 + STAND/caixa 260) ≈ 31,5 m² · Pilar 0,445 × 3,85 × ~2,5 faces ≈ 4,3 m².
\+ porta ripada (0,90×2,10) + armário gourmet exterior. **Total Cravo Trend ≈ 107,5 m² → 25 chapas (15 mm).**

## MÓVEIS (Moscada Matt)
- **Móvel Lounge:** 300 L × 60 A (40 corpo + 20 pé metálico) × 35 P — 2 nichos + 4 gavetas, sobre pés metálicos.
- **Armário Gourmet:** 97,5 L × 248 A × 42 P — ext. Cravo Trend, caixa/nicho Moscada; 2 portas 42,3 + nicho 85,5 + compart. 56.
→ Moscada ~6,2 m² (15) + 1,8 m² (6) → 3 chapas.

## RESUMO — chapas & custo
| Item | m² | Chapas | R$ |
|---|---|---|---|
| Cravo Trend 15 | 107,5 | 25 | 12.500 |
| Moscada 15 | 6,2 | 2 | 1.000 |
| Moscada 6 | 1,8 | 1 | 300 |
| MDF madeirado 15 | 45,8 | 11 | 5.500 |
| **Chapas** | | **39** | **19.300** |
| Metalon pérgola (28 barras + frete) | | | 4.350 |
| Terceiros (inox, pés, vidro jateado, sanca LED, moldura hidrante, poliestireno) | | | ~3.234 |
| Insumos (fita, cola/parafuso, usinagem) | | | ~6.660 |
| Visitas + logística | | | 1.350 |
| **CUSTO MATERIAL** | | | **≈ R$ 34.900** |

## Portas (destacadas na proposta) — CORRIGIDO
2 portas de **giro** na copa (+ painel entre elas) · 2 portas do **armário gourmet** (42,3) · 1 porta de **acesso ao QG** embutida no painel.
**FORA (terceiros, correção do Jonathan):** a porta com lâminas horizontais da Elev.2 é **veneziana** (não marcenaria Valvic); a portinhola 30×20 do pilar (*"vidro temperado c/ película jateada"*, acesso hidrante) é **vidraceiro**. Ambas removidas do escopo/preço.

## Corretor & Inox (esclarecimentos)
- **Corretores** = Painel Corretor (MOB 01): backdrop 8,17×3,85 em Cravo Trend — faixa sup. 4×204,4 (h=125) + **caixa em marcenaria** central recuada (h=260). Não é balcão.
- **Inox** = rodapé em perfil de **inox escovado 5×0,5, h=5cm** (DET.02), na base dos painéis. Serralheria (incluso, coordenado pela Valvic).

## Fechamento (confirmado): chapa R$ 500 · sem RT · MC 40% → **R$ 88.200**
*(era R$ 91.300; −R$ 3.100 ao remover veneziana + vidro jateado, ambos terceiros.)* Material R$ 33.694.
Breakdown: Painéis R$ 45.700 · **Pérgola R$ 18.000** · **Portas (giro+acesso) R$ 5.500** · Móveis + complementos R$ 19.000. Pagto 40/40/20 · prazo 45–60 úteis · garantia 2 anos.

## Preço (motor comercial) — sensibilidade
denom = 1 − 0,18 − 0,88·b − MC. **MC 40% · sem RT → R$ 91.300** · **MC 40% · RT 10% → R$ 118.600** · MC 43%/RT10 → R$ 132.100.

## FLAGS p/ travar a proposta
1. **Preço da chapa Arauco Realce** — usei base R$ 500/chapa (cor). Realce é linha premium; se ~R$ 700–900, o material sobe.
2. **RT** — projeto de escritório de arquitetura (Lodi Motta). Tem RT (10%)? Muda ~R$ 27 mil.
3. **MC** — recomendo 40% (piso caixa Rodrigo é 37%).
4. **Forro em gypsum** — assumido por conta do gesseiro (fora do escopo Valvic). Confirmar.
5. Espessura do painel de parede: assumi 15 mm.
