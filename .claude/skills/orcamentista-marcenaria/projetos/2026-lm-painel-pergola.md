# Orçamento — LM / SPE Nova Lima 1 (Painéis + Pérgola) — comercial

**Cliente:** SPE Nova Lima 1 · **Projeto:** arq. Lodi Motta / JBA Arquitetura · **Local:** Nova Lima–MG · **Etapa:** Executivo
**Pranchas:** MOB 01 (Painel Corretores/Pilar, R01) + MOB 02 (Painel/Pérgula Gourmet-Lounge, R00)
\+ **[07/08] MO 03 (Sala/Cozinha) · DET 05 (Quarto) · DET 06 (Suíte)** — o apartamento decorado.
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


---

# ESCOPO NOVO — APARTAMENTO DECORADO [07/08/2026]

Chegaram três pranchas **executivas** do Lodi Motta, R00 de 05–06/08/2026:

| Prancha | Conteúdo | Formato |
|---|---|---|
| **MO 03** | Mobiliário Sala / Cozinha — 4 elevações + 2 plantas | A2 79,3×42 |
| **DET 05** | Quarto — 4 elevações + planta, 9,00 m² | A2 59,4×42 |
| **DET 06** | Suíte — 3 elevações + planta | A2 59,4×42 |

**Não há sobreposição com a proposta vigente.** Os R$ 88.200 cobrem MOB 01 + MOB 02 —
painéis, pérgola e móveis das **áreas comerciais do stand**. Isto é o **apartamento
decorado**. É escopo somado, não revisado.

## Acabamentos (legenda das pranchas)
- **Sala/Cozinha e Suíte:** MDF Arauco **Anis Matt** + **Frapé Matt**
- **Quarto:** MDF **Ciliegio Poro** + **laca brilhante Sayerlack M072**
- **Rodapé sala/cozinha:** perfil de **inox escovado 5×0,5, h=5** (DET.02)
- **Rodapé quarto/suíte:** h=7
- **Puxador da cozinha:** perfil embutido 1,5+1,5, prof. 8 (DET.03) — é **cava**

## Quantitativo — `corte-spe-decorado.py`

| Material | Área | Chapas |
|---|--:|--:|
| Branco 15 · 18 · 6 (caixaria e fundos) | 100,9 m² | 29 |
| Anis Matt 15 · 18 | 25,6 m² | 8 |
| Frapé Matt 15 · 18 | 6,9 m² | 3 |
| Ciliegio Poro 15 · 18 | 12,6 m² | 5 |
| **Total** | **145,85 m²** | **45** · 64% |

Terceirizados **R$ 5.950,69** — espelho prata 5,34 m², laca Sayerlack 3,16 m²,
cabeceiras estofadas 3,64 m², rodapé inox 10,6 m, LED 9,9 m.
Ferragens **R$ 2.860,50** — 22 dobradiças, 8 articuladores, 3 conjuntos de correr,
8,95 m de cava.

**CUSTO DIRETO: R$ 37.808,82**

## Preço

### FECHADO [Jonathan 07/08]: **sem RT · MC 35%** · *"sem mexer nos valores na proposta inicial"*

Divisor 0,45016. Rateio por ambiente — chapa por área dentro de cada material,
fita e filetagem por área, **terceiros e ferragens atribuídos exatos**.

| Ambiente | Área | Custo direto | Investimento |
|---|--:|--:|--:|
| Cozinha | 54,5 m² | 11.671,12 | **25.900** |
| Sala | 19,2 m² | 6.306,83 | **14.000** |
| Quarto | 29,9 m² | 9.178,30 | **20.400** |
| Suíte | 42,2 m² | 10.652,57 | **23.700** |
| **Decorado** | **145,9 m²** | **37.808,82** | **84.000** |

MC conferida **35,0%**.

| | |
|---|--:|
| Stand — MOB 01 + MOB 02 · **inalterado** | R$ 88.200 |
| Decorado — MO 03 + DET 05 + DET 06 | R$ 84.000 |
| **TOTAL** | **R$ 172.200** |

Escada: −3% 167.000 · −5% 163.600 · −7% **160.100**.

> ⚠️ **O contrato passa a ter duas margens.** O stand fechou a **40%**, o decorado
> sai a **35%**. A MC combinada fica em **~37,6%** — ainda na faixa boa. Mas se a
> negociação puxar desconto sobre o total, ela corrói a etapa nova, não a antiga.

O decorado quase empata com o stand — quatro ambientes mobiliados contra
painelaria e pérgola.

## Proposta — `build-spe-nova-lima.py` → `proposta-spe-nova-lima.pdf`

4 páginas no layout premium da casa: capa · **o que muda** (duas caixas opondo
contratado × entra agora, mais o decorado em números) · os quatro ambientes ·
investimento com o stand em faixa cinza marcado *"valor inalterado"*.

Condições: **60 a 75 dias úteis** para o decorado, a alinhar com a inauguração do
stand · garantia **2 anos** (mesma da etapa contratada) · validade 7 dias.
⚠️ O prazo é assumido por mim, não ditado.

## ⚠️ Flags
1. **Chapa Arauco MATT** — usei a base "cor" (R$ 500/580). Matt é linha premium;
   a R$ 800/chapa o custo sobe ~R$ 11.250 e o preço ~R$ 28.100. **É o maior risco
   aberto**, e é o mesmo flag que ficou pendente na proposta vigente.
2. **RT** — projeto do Lodi Motta. Se houver, o decorado vai de 94.500 para 121.100.
3. **Interno branco assumido** — as pranchas só especificam o acabamento aparente.
4. **Fita pelo fator 2,6 m/m²**, não apurada peça a peça.
5. **Divisão interna dos módulos** lida das elevações; as plantas cotam o
   desenvolvimento, não a divisão de gavetas.
6. **Fora do escopo:** caixa de gypsum, pintura, cortinas, tapetes, eletros,
   bancadas de pedra.
