# Nova Estrutura — Mapa da Expansão da Valvic Marcenaria

> **Documento-mapa da nova estrutura** — fonte detalhada e atualizada:
> [`2026-expansao-linha-montagem.md`](2026-expansao-linha-montagem.md).
> Este arquivo é o resumo organizado para futuras sessões. Em caso de divergência,
> o `2026-expansao-linha-montagem.md` prevalece.

---

## 1. Visão / Tese

- **Objetivo imediato:** dobrar a produção — **R$ 200 mil/mês → R$ 400 mil/mês**, com
  estrutura robusta (máquinas + veículos + pessoal + espaço).
- **Visão de longo prazo:** com tudo rodando, chegar a **R$ 1 milhão/mês** — a
  capacidade das máquinas novas comporta.
- **Estado atual confirmado:** faturamento ~R$ 200 mil/mês · margem de contribuição (MC)
  ~30% (→ R$ 60 mil/mês) · 1 turno.

### Faseamento (confirmado Paulo 25/06)
- **Fase 1 — JÁ:** começar a girar com o essencial — **coladeira + compressor +
  camionete usada + equipe inicial**. Start do negócio.
- **Fase 2:** montar a estrutura completa no **galpão novo** rodando todas as máquinas.

---

## 2. Máquinas

### Princípio de arquitetura
**Não desfazer de NENHUMA máquina atual.** Todas continuam com papel novo. Ganhos para
o deck: fim do gargalo (a Solid TAF deixa de brigar entre nesting × especiais) +
**redundância / uptime** (sem ponto único de falha).

### Máquinas ATUAIS (já existentes)
| Máquina | Hoje | Papel na nova linha |
|---|---|---|
| **Raizen Solid TAF** (centro de usinagem) | CNC nesting + especiais | Passa a fazer **só usinagens especiais (Aspire)** |
| **SCM minimax me 25** (coladeira) | Coladeira principal | Vira **backup** (entra quando a principal parar/manutenção) |
| **Raizen RZN 3200P** | Esquadrejadeira | Mantém — cluster de corte |
| **Tupia** | — | Mantém — auxiliar |
| **Serra esquadria** | — | Mantém — auxiliar |

> Solid TAF: área útil Y 2800 × X 1900 × Z 200 mm (cabe chapa inteira 1850×2750) ·
> capacidade 35 chapas/dia · 660 chapas/mês · spindle 9 kW 24.000 RPM ISO30 · 380V tri.
> Specs completas em `dados/maquinas.json` e `referencias/maquinas.md`.

### Máquinas NOVAS a adquirir (à vista — o aporte compra à vista)
| Máquina | Escolha recomendada | Preço à vista | Alternativa |
|---|---|---|---|
| **CNC Nesting** | **Giben** (palete inteiro) | **R$ 490.000** *(confirmar à vista)* | Raizen Vision One Nesting Plus — R$ 468.000 |
| **Coladeira de borda** | **Giben KG268** (arredondador) | **~R$ 162.000** *(à vista a confirmar; prazo R$ 180k)* | Raizen Spectra 7GT — R$ 162.000 à vista |
| **Furação horizontal** | **Raizen CNC Horizontal 3S** | **R$ 82.000** | — |
| **Compressor** | **Techto Autentic AT 10HP** | **R$ 21.310** | — |
| **Subtotal máquinas** | | **≈ R$ 755.000** | (100% Raizen ≈ R$ 733.000) |

### Por quê das decisões
- **CNC Nesting = Giben:** capacidade (~1.430 chapas/mês), automação (etiquetagem +
  furação + 9 brocas), procedência (China) e suporte/garantia no Brasil **empataram** com
  a Raizen Vision One. O desempate é a **carga de PALETE INTEIRO** (só a Giben; as outras
  carregam meio palete) → metade das paradas para reabastecer + menos mão de obra
  carregando chapa + ganho de ergonomia/uptime. O prêmio de ~R$ 22k (4,7%) é pequeno
  perto disso. ⚠️ Confirmar se R$ 490k é à vista.
- **Coladeira = Giben KG268:** decidido usar **fita de 1 mm** → exige **grupo
  arredondador**. A 6GT (sem arredondador) saiu. 7GT × Giben KG268 empatam em
  arredondador, velocidade e preço. Desempate = **suporte local em BH** (a KG268 é a mais
  usada pelas madeireiras da região → peça/técnico/operador fáceis = menos máquina
  parada, crítico numa coladeira que é gargalo). ⚠️ Única pendência: preço à vista da
  Giben (recomendado só se ≤ ~R$ 165k; senão reabrir vs 7GT).
- **Furação 3S:** fura o **topo/borda** do MDF (cavilha/minifix, fechadura, dobradiça) —
  a CNC de nesting só fura a face vertical. Destrava produção de portas internas, reduz
  retrabalho e terceirização.
- **Compressor Techto:** alimenta o ar comprimido de toda a linha (coladeira, furadeira,
  fixações, pistolas). 10 HP / 7,5 kW · 8,5 bar · 1,08 m³/min · cabine acústica. ⚠️
  Validar se a vazão atende a demanda somada com todas as máquinas rodando juntas.

> Capacidade × tese: a nova CNC (~1.430 chapas/mês) já é >2× a Solid TAF (660). Com a
> nova só no nesting e a Solid TAF só nos especiais, o corte deixa de ser gargalo — o
> limite passa a ser coladeira / pessoal / espaço / capital de giro.

---

## 3. Galpão

**Decidido (Paulo 25/06): galpão de 1.000 m² (40 × 25 m).** Layout em escala (v4):
[`Valvic_Layout_Galpao_1000m2.png`](Valvic_Layout_Galpao_1000m2.png) /
[`.pdf`](Valvic_Layout_Galpao_1000m2.pdf).

### Arranjo (máquinas todas EM LINHA no topo; bancadas no lado oposto)
1. Entrada de caminhão (esq) → **gaiola de chapas** (recebimento) → **CNC Nesting +
   Solid TAF ao lado** → **Coladeira (+ backup me25)** → **Furação 3S** → fim da linha:
   armazenagem de peças cortadas/prontas + carrinhos.
- **Esquadrejadeira** central, no cluster de corte (abaixo do nesting, junto da Solid TAF).
- **Corredor central:** trânsito dos **8 carrinhos** levando peças cortadas até as bancadas.
- **Lado oposto:** **7 bancadas** com área generosa de pré-montagem em volta de cada uma.
- **Expedição** (peças embaladas) no fim da linha de bancadas, perto do portão de saída.
- **Compressor:** **EXTERNO, coberto** (fora do galpão).
- **3 m entre TODAS as máquinas** (confirmado que cabe nos 40 m de comprimento).

### Medidas reais (C × L, em m)
- Máquinas: gaiola 3×4 · nesting 10×2,5 · Solid TAF 3×2 · esquadrejadeira 3×2 ·
  coladeira 4×1 · furação 3×1.
- **Bancadas:** 7 un. de 2,70 × 0,90 × 0,90 m (alt).
- **Carrinhos:** 8 un. de 2,00 × 0,50 × 0,90 m (alt).

### Requisitos de infra
- **Pé-direito ≥ 6 m** (estoque vertical de chapa + dutos de exaustão).
- **Piso industrial reforçado** (máquinas de 1–2 t).
- **Energia trifásica ~150 kVA** (soma das cargas: Giben CNC ~30 kW + coladeira ~20 +
  furação 9,6 + compressor 7,5 + Solid TAF ~20 + auxiliares + aspiração). Confirmar c/
  eletricista.
- **Aspiração central de pó** (CNC + coladeira + serras).
- **Rede de ar comprimido (anel)** a partir do compressor.
- **Doca / acesso de caminhão (baú)** + área de manobra; idealmente empilhadeira.
- **Layout em FLUXO:** recebimento → nesting → coladeira → furação → marcenaria →
  montagem → expedição. A peça nunca anda para trás.

---

## 4. Veículos

| Veículo | Quando | Custo | Função |
|---|---|---|---|
| **Chevrolet Montana 2020** | ATUAL | — | Caçamba pequena; corridas rápidas / pequenas entregas |
| **Camionete usada** | Fase 1 | R$ 50–60 mil | Reforço inicial de logística |
| **Kia Bongo (baú)** | Fase 2 | ~R$ 100 mil (R$ 80–120k usados) | Caminhão leve, carga ~1,5 t; entrega + montagem do volume dobrado, libera a Montana |

---

## 5. Pessoal

Organograma: [`Valvic_Organograma.png`](Valvic_Organograma.png).

**Time atual:** 1 operador (CNC+coladeira) · 1 encarregado (também produz) · 2 ajudantes ·
2 marceneiros · Paulo (quer sair da produção). Apoio: Felipe (programação CNC), Jonathan
(sócio, comercial), Paulo (sócio, gestão).

### Contratações (confirmado Paulo 25/06)
| Cargo | Qtd | Salário base | Subtotal | Fase |
|---|---|---|---|---|
| Marceneiro | 2 | R$ 5.000 | R$ 10.000 | +1 Fase 1, +1 Fase 2 |
| Ajudante | 2 | R$ 2.500 | R$ 5.000 | +1 Fase 1, +1 Fase 2 |
| Auxiliar administrativo | 1 | R$ 4.000 | R$ 4.000 | Fase 1 |
| Projetista | 1 | R$ 5.000 | R$ 5.000 | Fase 2 |
| **Total novas contratações** | **6** | | **R$ 24.000/mês (base)** | |

- **Fase 1:** +1 marceneiro, +1 auxiliar administrativo, +1 ajudante.
- **Fase 2:** +1 marceneiro, +1 ajudante, +1 projetista.
- Com encargos (~70%: FGTS, INSS, 13º, férias, benefícios) → **~R$ 40.800/mês**
  (confirmar com contador).

---

## 6. Investimento

| Item | Valor |
|---|---|
| **Fase 1 — equipamentos** (coladeira + compressor + camionete + start) | **≈ R$ 235–261 mil** |
| **Fase 2 — estrutura completa no galpão novo** | **≈ R$ 872 mil** |
| → CNC Nesting (Giben) | R$ 490.000 |
| → Furação horizontal (Raizen 3S) | R$ 82.000 |
| → Kia Bongo (baú) | R$ 100.000 |
| → Infra do galpão novo | R$ 200.000 |
| **Total geral em estrutura** | **≈ R$ 1,1 milhão** (~R$ 1.055.000) |

- Composição geral: máquinas ~R$ 755k + veículo ~R$ 100k + infra do galpão R$ 200k
  (+ capital de giro a dimensionar).
- **APORTE: definido pelo investidor** — não fixar valor no deck. O aporte compra à vista.

---

## 7. Payback / Retorno

- **Ganho ao dobrar:** +R$ 200k/mês × MC 30% = **+R$ 60.000/mês** de margem de contribuição.
- **− folha nova** (com encargos) ≈ R$ 40.800 → **sobra ≈ R$ 19.000/mês** (antes de
  outros fixos novos: galpão, energia, combustível — a estimar).
- **Payback (cenário dobrar, só folha):** ~R$ 1.055M ÷ 19k ≈ **~55 meses (~4,6 anos)**.
- **🚀 Upside (R$ 1 mi/mês):** +R$ 800k/mês × MC 30% = **+R$ 240.000/mês** de MC. Com a
  capacidade instalada, o payback cai para menos de 1 ano no pico (alavancagem
  operacional + ganho de escala na MC).

---

## 8. Artefatos gerados

| Arquivo | Conteúdo |
|---|---|
| `projetos/Valvic_Portfolio_Investidor.pdf` | Portfólio completo de apresentação ao investidor |
| `projetos/Valvic_Plano_Fases_1e2.pdf` | Plano detalhado das Fases 1 e 2 |
| `projetos/Valvic_Fase1_Investimento_Inicial.pdf` | Investimento inicial da Fase 1 |
| `projetos/Valvic_Layout_Galpao_1000m2.png` / `.pdf` | Layout em escala do galpão de 1.000 m² (v4) |
| `projetos/Valvic_Organograma.png` | Organograma (atual × futuro) |
| `projetos/foto-giben-g2-1929.jpg` | Foto referência CNC Giben G2 1929 |
| `projetos/foto-giben-kg268.jpg` | Foto referência coladeira Giben KG268 |

---

## 9. Pendências

- [ ] Confirmar **preço à vista da Giben CNC** (R$ 490k é à vista?) e pedir desconto à vista.
- [ ] Confirmar **preço à vista da coladeira Giben KG268** (≤ ~R$ 165k; senão reabrir vs 7GT).
- [ ] Confirmar **aporte e contrapartida** ao investidor (% / empréstimo).
- [ ] Definir **aluguel / custo do galpão** novo (custo fixo mensal).
- [ ] Validar se o compressor (1,08 m³/min) atende a demanda somada das máquinas.
- [ ] Confirmar **~150 kVA** com eletricista.
- [ ] Fotos reais das máquinas e dos funcionários para o portfólio.
- [ ] 2º turno entra no plano? (S/N).
- [ ] Conta de payback final com outros fixos novos (galpão, energia, combustível) — puxar Rodrigo/financeiro.
- [ ] Confirmar encargos da folha com contador (~70%).
