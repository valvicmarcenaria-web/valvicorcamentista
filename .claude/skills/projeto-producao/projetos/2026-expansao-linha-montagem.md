# Plano de Expansão — Linha de Montagem (portfólio investidor)

> Documento de trabalho do Téo p/ montar o portfólio de apresentação ao sócio
> investidor. Acumula os dados conforme o Paulo manda. Vira PDF no final.
> Iniciado 24/06/2026.

## Objetivo
**Dobrar a produção: R$200 mil/mês → R$400 mil/mês**, com estrutura robusta
(máquinas + veículos + pessoal + espaço).

## Estado atual (CONFIRMADO pelo Paulo)
- **Faturamento:** ~R$200 mil/mês · **Margem de contribuição:** ~30% (→ R$60 mil/mês).
- **Aporte pretendido:** ~R$1,55 milhão (a confirmar valor exato e contrapartida).
- **Turno:** 1 só.
- **Time produção:** 1 operador (CNC+coladeira) · 1 encarregado (também produz) ·
  2 ajudantes · 2 marceneiros · (+Paulo às vezes — quer sair da produção).
- **Apoio/gestão:** Felipe (programação CNC) · Jonathan, sócio (comercial) ·
  Paulo, sócio (gestão, hoje preso na produção).
- **Máquinas atuais:** Raizen Solid TAF (CNC nesting+especiais) · SCM minimax me 25
  (coladeira) · Raizen RZN 3200P (esquadrejadeira) · tupia · serra esquadria.
  (detalhe em `dados/maquinas.json`)
- **Veículos:** 1 Chevrolet Montana 2020 (caçamba pequena) — insuficiente p/ dobrar.

## Decisões de arquitetura da linha (CONFIRMADO 24/06)
- **Não desfazer de NENHUMA máquina atual.** Todas continuam, com papel novo.
- **CNC nova (a adquirir):** nesting principal.
- **Raizen Solid TAF (atual):** passa a ser **só usinagens especiais** (Aspire).
- **Coladeira nova/maior (a adquirir):** filetagem principal.
- **SCM me 25 (atual):** vira **backup** (entra quando a principal parar/manutenção).
- Ganhos p/ o deck: fim do gargalo (Solid TAF não briga mais entre nesting×especiais)
  + **redundância/uptime** (sem ponto único de falha).

## Conta de retorno (modelo)
- Ganho-teto ao dobrar = +R$60 mil/mês (MC 30% sobre +R$200 mil).
- Lucro novo = R$60 mil − **custo fixo incremental** (folha nova + veículo + energia…).
- **Payback = aporte ÷ lucro novo.** (Ex.: fixo novo R$25k → sobra R$35k → ~44 meses.)
- Alavancas a favor: alavancagem operacional (fixos atuais já pagos) + MC sobe na
  escala (compra de chapa em volume).

## Fichas de máquina (para o portfólio)

### [ATUAL] Raizen Solid TAF — Centro de Usinagem (→ vira especiais)
- Área útil **Y 2800 × X 1900 × Z 200 mm** (cabe chapa inteira 1850×2750).
- **Capacidade: 35 chapas/dia · 660 chapas/mês** (~26 peças/chapa).
- Spindle 9 kW (12 CV) 24.000 RPM ISO30 · vácuo 11,7 CV (4 câmaras) · guias lineares ·
  servo Leadshine · redutor Shimpo · 40 m/min · ATC 10 ferramentas · ~1720 kg · 380V tri.
- **Papel na linha nova:** usinagens especiais (Aspire). Valor: ativo já existente.

> Benchmark p/ a conta: a CNC atual sozinha faz até **660 chapas/mês**. Hoje ela
> divide tempo entre nesting e especiais. Com a CNC nova só pro nesting + esta só
> pros especiais, a capacidade de nesting dá um salto (base do "dobrar produção").

### [NOVA — NESTING] Opção A: Raizen Vision One Nesting Plus
- **Centro de usinagem nesting industrial.** Área útil 2.800 × 1.900 mm (cabe chapa inteira).
- **Capacidade: 65 chapas/dia · 1.430 chapas/mês** (~26 peças/chapa).
- Comando **CNC Syntec** · spindle 9 kW (12 CV) 24.000 RPM · **60 m/min** ·
  precisão ±0,06 mm/2000 mm · monobloco aço.
- **Magazine 18 ferramentas** no pórtico · **cabeçote de furação 9 brocas verticais**.
- **2 bombas de vácuo 11,7 CV.**
- **Automação:** alimentação de chapas + **etiquetamento** + **descarga automática**.
- **Preço:** R$ 520.000 a prazo · **R$ 468.000 à vista**.
- Mesma marca da atual (Raizen) → sinergia de treino do Felipe.
- **Fabricada na China** (confirmado Paulo 25/06) — igual à Giben/KDT.
- ⚠️ Comando **Syntec** (≠ JRG da Solid TAF) → meu conhecimento de G-code JRG não
  transfere direto; a programação da nova usa post Syntec.

### [NOVA — NESTING] Opção B: Giben G2 1929 / KDT (premium)
- Vista nos vídeos (**Giben G2 1929** real + animação **KDT**).
- **Paulo (25/06):** **KDT = a mesma Giben, fábrica na China**; corta o **mesmo volume
  de chapa da Raizen** (~1.430 chapas/mês). → Giben (Itália) e KDT (China) = mesma linha,
  procedências diferentes.
- **Marca melhor posicionada** (durabilidade/precisão).
- **Diferencial:** carrega **PALETE INTEIRO** na mesa de abastecimento (as outras só
  meio palete) → menos paradas p/ reabastecer, menos mão de obra na chapa.
- **Preço:** R$ 490.000. ⚠️ **CONFIRMAR:** esse valor é da Giben (Itália) ou da KDT
  (China)? Há diferença de preço entre as duas procedências?
- ❗ **SEM ficha técnica ainda** — pedir (furação múltipla? etiquetamento/descarga
  automática? comando? vácuo?) p/ comparar maçã com maçã com a Vision One.

### Comparação (25/06 — máquinas quase equivalentes)
EMPATARAM: **capacidade** (~1.430 chapas/mês), **automação** (etiquetagem + furação +
9 brocas iguais nas duas) e **procedência** (ambas China). Sobram 3 fatores de decisão:
- **Preço:** Vision One **R$ 468k à vista** (520k a prazo) × Giben/KDT **R$ 490k**.
  → Raizen ~R$ 22k mais barata à vista.
- **Carga de chapa:** Giben carrega **palete inteiro** × Raizen **meio palete** (CONFIRMAR
  se ainda vale). Vale uptime/menos mão de obra — pesar contra os R$ 22k.
- **Suporte/garantia no Brasil:** TODAS têm suporte e garantia no Brasil (confirmado
  Paulo 25/06) → fator EMPATADO.

### ✅ RECOMENDAÇÃO (25/06): Giben
Como capacidade, automação, procedência e suporte/garantia EMPATARAM, sobram 2 fatores:
preço (Raizen ~R$22k mais barata à vista) × **carga de palete inteiro (só a Giben)**.
- **Recomendo a Giben.** O prêmio de ~R$22k (4,7%) é pequeno perto do ganho de
  **palete inteiro**: metade das paradas p/ reabastecer + menos mão de obra carregando
  chapa — exatamente o que a tese ("dobrar com equipe enxuta") precisa. Também é ganho
  de **ergonomia/segurança** (menos peso manual) e **uptime** (bom argumento p/ investidor).
- A favor da Raizen ficaria só o preço; a "mesma marca da atual" pesa pouco (a Solid TAF
  é JRG e a Vision One é Syntec — comando diferente de qualquer jeito).
- ⚠️ CONFIRMAR antes de bater o martelo: o **R$490k da Giben é à vista**? (comparar
  à vista × à vista, já que o aporte deve comprar à vista). Pedir desconto à vista na Giben.

> **Capacidade × tese:** ~1.430 chapas/mês já é >2× a Solid TAF (660). Com a nova só no
> nesting + Solid TAF só nos especiais, capacidade de corte deixa de ser o gargalo.
> O limite passa a ser **coladeira / pessoal / espaço / capital de giro**.

## Coladeira de borda nova (3 opções) — a me 25 vira backup

Comum às Spectra (Raizen): fita **0,4–3,0 mm** (hoje a Valvic só usa 0,4 → ganho de
poder colar fita grossa PVC/ABS), painel esp. 10–45 mm, colas **EVA/PO/PUR** (PUR =
linha de cola invisível, premium), 4 rolos pressores, tela Delta 7", coleiro híbrido
móvel c/ 2 reservatórios, copiador nesting, lubrificação automática, 380V trifásica.

### [NOVA — COLADEIRA] Opção A: Raizen Spectra 6GT
- **6 grupos:** tupia entrada · coleiro · destopador · refilador · raspador · polidor.
- **Velocidade:** 14 m/min (fixa). Potência 18 kW · 1.200 kg.
- **Preço:** R$ 142.000 a prazo · **R$ 127.000 à vista**.

### [NOVA — COLADEIRA] Opção B: Raizen Spectra 7GT
- **7 grupos:** os 6 acima **+ grupo ARREDONDADOR** (arredonda o canto da fita —
  acabamento premium, essencial p/ fita grossa PVC/ABS).
- **Velocidade:** **14-16-20 m/min** (selecionável → ~43% mais rápida que a 6GT).
  Potência 20 kW · 1.300 kg.
- **Preço:** R$ 180.000 a prazo · **R$ 162.000 à vista**.

### [NOVA — COLADEIRA] Opção C: Giben KG268 (KG 268J)
- Vista no vídeo (coladeira branca, touchscreen, bobina de fita).
- **"A mais usada pelas madeireiras de BH"** → proven, **suporte/peças/operadores
  abundantes na região** (baixo risco, fácil achar técnico que conhece).
- **Preço:** R$ 180.000 (⚠️ confirmar se à vista ou a prazo).
- ❗ **SEM ficha técnica ainda** — pedir grupos, velocidade, arredondador?, fita máx, colas.

### ✅ DECISÃO COLADEIRA (25/06) — DECIDIDO usar fita de 1 mm
Fita 1 mm → **arredondador necessário**. Confirmado pelo Paulo: Giben KG268 **tem
arredondador**, **velocidade ~igual** à 7GT, e os **R$ 180k são a PRAZO**.
- **6GT — fora** (sem arredondador, não serve p/ fita de 1 mm).
- **7GT × Giben KG268 — EMPATAM** em arredondador, velocidade e preço (a prazo as duas
  = R$ 180k; à vista 7GT = R$ 162k, Giben a confirmar mas ~próximo).
- **Desempate = suporte local.** A **Giben KG268 é a mais usada pelas madeireiras de
  BH** → peça/técnico/operador fáceis na região = **menos máquina parada**. Pra uma
  coladeira que vira **gargalo** numa operação dobrando, uptime é o que mais vale.
- **➡️ RECOMENDAÇÃO: Giben KG268**, desde que o **preço à vista** fique ≈ o da 7GT
  (≤ ~R$ 165k). Se a Giben à vista vier bem acima de 162k, reabrir vs 7GT.
- **Única pendência:** preço **à vista** da Giben KG268.

## Centro de furação HORIZONTAL (4ª máquina a adquirir)
- **Função:** furar o **topo/borda** do MDF — furo de **dispositivo** (cavilha/minifix),
  **furo de fechadura** e **dobradiça** em porta de passagem, etc.
- **Por quê:** a CNC fura na vertical (face); o **topo** é horizontal → a CNC NÃO faz.
  Hoje provavelmente é manual/gabarito (lento, sujeito a erro). Máquina destrava também
  **produção de portas de passagem** internamente.
- Valor p/ o deck: + capacidade interna, − retrabalho, − terceirização.
- ❗ **Ficha técnica + preço: A RECEBER** (modelo, nº de mandris/brocas, eixos,
  comando, capacidade).

## A RECEBER do Paulo (pendências)
- [ ] Máquinas a adquirir (foto + modelo + valor + função/capacidade).
- [ ] Pessoal a contratar (cargos + salários estimados) → custo fixo incremental.
- [ ] 2º turno entra no plano? (S/N)
- [ ] Espaço: galpão atual cabe ou precisa área nova? (m² atuais)
- [ ] Confirmar aporte (R$1,55 mi?) e contrapartida ao investidor (% / empréstimo).

## A FAZER (Téo)
- [ ] Dimensionar galpão (footprints + fluxo + estoque) quando vier a lista.
- [ ] Layout da linha de montagem (recebimento → nesting → coladeira → marcenaria →
      montagem → expedição).
- [ ] Plano de veículos (somar baú/furgão).
- [ ] Organograma atual × futuro.
- [ ] Conta de payback final (puxar Rodrigo/financeiro).
- [ ] Montar o PDF do portfólio.
