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

<!-- próximas fichas: CNC nova, coladeira nova, veículo(s), etc. -->

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
