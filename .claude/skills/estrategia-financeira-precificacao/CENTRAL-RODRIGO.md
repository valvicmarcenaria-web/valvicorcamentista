# Central Financeira — Rodrigo (Valvic Marcenaria)

> **Leia este arquivo PRIMEIRO ao iniciar qualquer sessão com o Rodrigo.**
> É a fonte de verdade do estado financeiro atual + pipeline + pendências.
> Atualizar sempre que houver mudança relevante (novo projeto, dívida, caixa).

---

## 1. Quem é o Rodrigo

**Consultor de finanças e precificação estratégica da Valvic.** Eleva a decisão
de preço do tático (MC% por projeto, feito pela Lavinia) para o estratégico
(saúde financeira da empresa). Método baseado em Rodrigo Almeida (@rodrigofinancas).

> **Lema:** *"Faturamento é vaidade — aumente o lucro com os preços certos."*
> O problema da Valvic **não é venda** — é **ciclo de caixa e pipeline futuro**.
> A empresa cresce (+18% projetado 2026), mas o caixa não acompanhou o crescimento.

Ver método completo: `referencias/metodo-rodrigo.md`

---

## 2. Quadro financeiro real — ATUALIZADO 16/06/2026

### ⚠️ BREAK-EVEN REAL (custo-operacao.html — fonte de verdade)

> Fonte: JSON exportado do `custo-operacao.html` em 16/06/2026.
> Faturamento de referência configurado pelo Jonathan: **R$ 246.000/mês**

| Indicador | Valor |
|---|---|
| **Custo fixo total (fixoBE)** | **R$ 83.518/mês** |
| → do qual: dívidas/parcelas | R$ 20.700/mês |
| → do qual: folha + encargos | R$ 43.456/mês |
| Comissões em % (variáveis) | **9,5%** do faturamento |
| **MC líquida disponível p/ fixo** | **34%** (43,5% MC − 9,5% comissões) |
| **BREAK-EVEN FATURAMENTO** | **R$ 245.642/mês (~R$ 246k)** |
| Lucro no break-even | R$ 122/mês (literalmente zero) |

### Custo por centro (mensal, no faturamento de R$ 246k)

| Centro | R$/mês |
|---|---|
| Sócios (pró-labore + ajuda custo) | R$ 15.400 |
| Folha produção (PJ + CLT + encargos) | R$ 23.256 |
| Benefícios CLT (VT, EPIs) | R$ 2.650 |
| Comissões produção (5+0,5+1%+vendedor 3%) | R$ 23.370 |
| Máquinas e ferramentas (manutenção + depreç.) | R$ 3.933 |
| Instalações (aluguel + util. + conservação) | R$ 8.280 |
| Comercial (assistente + marketing) | R$ 5.449 |
| Logística / veículos | R$ 5.050 |
| Administrativo (contador, jurídico, sistemas, IA) | R$ 4.950 |
| Tributos (Simples Nacional) | R$ 1.500 |
| **Financeiro / Dívidas (parcelas)** | **R$ 20.700** |
| **TOTAL** | **~R$ 114.538** |

### Dívidas ativas — LEVANTADAS

| Dívida | Total | Parcelas | R$/mês |
|---|---|---|---|
| Financiamento de máquinas | R$ 24.000 | 5x | **R$ 4.800** |
| Capital de giro / empréstimo | R$ 37.000 | 4x | **R$ 9.250** |
| Empréstimo Paulo (devolução) | R$ 30.000 | 5x | **R$ 6.000** |
| Aporte Paulo — compra CNC | R$ 65.000 | 100x | **R$ 650** |
| **TOTAL DÍVIDAS** | **R$ 156.000** | — | **R$ 20.700/mês** |

### Simulação de resultado por faturamento

| Faturamento | MC (43,5%) | − Comissões (9,5%) | MC Líquida | − Fixo R$83,5k | **Resultado** |
|---|---|---|---|---|---|
| R$ 82k (DRE atual) | R$ 35,7k | −R$ 7,8k | R$ 27,9k | −R$ 83,5k | 🔴 **−R$ 55,6k/mês** |
| R$ 148k (planilha H1) | R$ 64,4k | −R$ 14,1k | R$ 50,3k | −R$ 83,5k | 🔴 **−R$ 33,2k/mês** |
| R$ 180k | R$ 78,3k | −R$ 17,1k | R$ 61,2k | −R$ 83,5k | 🔴 **−R$ 22,3k/mês** |
| R$ 200k | R$ 87,0k | −R$ 19,0k | R$ 68,0k | −R$ 83,5k | 🔴 **−R$ 15,5k/mês** |
| **R$ 246k** | **R$ 107,0k** | **−R$ 23,4k** | **R$ 83,6k** | **−R$ 83,5k** | ✅ **ZERO (break-even)** |

> **DIAGNÓSTICO DEFINITIVO:** O problema NÃO é MC%. É VOLUME.
> A empresa precisa de R$ 246k/mês para quebrar o zero. Qualquer faturamento
> abaixo disso gera prejuízo estrutural — independentemente da MC%.
> Dezembro/2025 (−R$ 54k acumulado) e Junho/2026 (−R$ 33k) são CONSEQUÊNCIA
> direta de meses com faturamento muito abaixo de R$ 246k.

### Equipe atual (10 pessoas)
| Pessoa | Função | Contratação | R$/mês |
|---|---|---|---|
| Jonathan | Sócio | — | R$ 7.700 (pró-labore + ajuda) |
| Paulo | Sócio | — | R$ 7.700 (pró-labore + ajuda) |
| Jackson | Marceneiro | PJ | R$ 3.600 |
| Samuel | Marceneiro | PJ | R$ 3.900 |
| Joelson | Operador CNC/coladeira | CLT | R$ 2.500 + enc. |
| Deivson | Coordenador | PJ | R$ 4.000 |
| Filipe | Programador | PJ | R$ 3.600 |
| Jomar | Marceneiro Jr | CLT | R$ 1.950 + enc. |
| Davi | Ajudante | CLT | R$ 1.950 + enc. |
| (Assistente admin) | Administrativo | CLT | R$ 2.000 + enc. |

### Comissões ativas (9,5% total sobre faturamento)
| Comissão | % | Tipo |
|---|---|---|
| Marceneiros | 5,0% | Variável |
| Programador | 0,5% | Variável |
| Coordenador | 1,0% | Variável |
| Vendedor | 3,0% | Fixo (classificado) |
| **TOTAL** | **9,5%** | — |

### Dados DRE Jan–Jun/2026 (Calcme — visão contábil)

| Indicador | 6 meses | Média/mês |
|---|---|---|
| Receita Bruta reconhecida | R$ 493.029 | R$ 82.171 |
| Receita Líquida | R$ 470.017 | R$ 78.336 |
| CPV (materiais) | −R$ 166.719 | −R$ 27.786 |
| Despesas Operacionais | −R$ 283.315 | −R$ 47.219 |
| Lucro Operacional | R$ 19.983 | R$ 3.330 (4%) |
| **Resultado Final** | **−R$ 34.340** | **−R$ 5.723/mês** |

> Nota: DRE mostra despesas menores (R$ 47k) que o custo-operacao (R$ 83,5k)
> porque: (1) parcelas de dívidas passam por contas não totalmente registradas;
> (2) alguns pagamentos saem pelo conta-sócios; (3) comissões em % calculadas
> sobre faturamento contratado (R$ 246k referência), não sobre o reconhecido.
> Usar o custo-operacao.html como fonte de verdade para decisões estratégicas.

### Status de caixa (Fluxo Mensal Jul/2025–Jun/2026)

| Mês | Recebimentos | Pagamentos | Saldo |
|---|---|---|---|
| Jul/2025 | R$ 0 | R$ 33.491 | R$ 39.844 |
| Ago/2025 | R$ 0 | R$ 13.200 | R$ 26.644 |
| Set/2025 | R$ 58.445 | R$ 63.309 | R$ 21.781 |
| Out/2025 | R$ 91.050 | R$ 97.906 | R$ 14.924 |
| Nov/2025 🔴 | R$ 0 | R$ 29.043 | -R$ 14.119 |
| Dez/2025 🔴 | R$ 66.850 | R$ 107.165 | -R$ 54.434 |
| Jan/2026 | R$ 88.100 | R$ 78.874 | -R$ 45.207 |
| Fev/2026 | R$ 139.390 | R$ 107.511 | -R$ 13.328 |
| Mar/2026 ✅ | R$ 189.689 | R$ 151.182 | +R$ 25.179 |
| Abr/2026 | R$ 104.180 | R$ 126.229 | +R$ 3.130 |
| Mai/2026 🔴 | R$ 86.550 | R$ 95.936 | -R$ 6.256 |
| Jun/2026 🔴 (prev.) | R$ 46.830 | R$ 101.827 | -R$ 33.554 |

> **Status jun/2026:** 🔴 CRÍTICO — saldo projetado -R$ 33.554. 7 de 12 meses
> com saldo negativo. Causa raiz: meses de zero recebimento (jul, ago, nov/2025)
> + dezembro catastrófico (R$ 107k pagamentos — investigar composição) +
> investimento em máquinas (R$ 34.966) durante crise de caixa.

---

## 3. Pipeline de projetos (planilha backup + Calcme)

### Projetos 2026 — valor contratado por mês (ATUALIZADO 22/06/2026 — planilha atualizada.xlsx)

| Mês | Contratado | Projetos | Situação |
|---|---|---|---|
| Janeiro | R$ 110.280 | Luiz (casa R$87,7k), Raquel (quarto R$22,6k) | ✅ Concluído |
| Fevereiro | R$ 201.675 | Matheus (painel), Bibiane (casa R$68k), Bruna, Augusto (apt R$90k), Sylvia | ✅ Em andamento |
| Março | R$ 216.198 | Rosemary, Matheus (cozinha), Isaias/Nubia, Reginaldo, Marcelo Maciel, **Maria Casa VDC R$117.738** | ✅ Em andamento |
| Abril | R$ 264.390 | Gisele, **Andre Alphaville R$70,8k (investimento dos sócios)**, Yasmin, **Cristiane casa R$101,7k**, Rejane, Leyde | ⚠️ Recebíveis críticos |
| Maio | R$ 89.650 | Daniel, Marina Borges, Maria VDC hall, Marcelo+Simony (apt) | ✅ Em andamento |
| Junho | R$ 99.600 | Fábio, Alexandrina, Bernardo, Carla (coz R$27k), **Lucas Mello casa R$46k** | ✅ Em andamento |
| **TOTAL H1** | **R$ 981.793** | **28 projetos** | |
| Julho–Dezembro | **R$ 0,00** | — | 🔴 **PIPELINE ZERADO** |

> **ALERTA CRÍTICO:** H2/2026 sem nenhum projeto vendido. Break-even R$246k/mês ×
> 6 meses = R$1,47M em custo. Com pipeline zero, a empresa perde R$83k/mês (custo
> fixo puro). Ação comercial imediata é questão de sobrevivência.

> **Meta 2026:** R$3.000.000 (declarada na planilha) | Meta lucro: R$600.000
> **Realidade:** R$981.793 em 6 meses = média R$163,6k/mês
> **Projeção H2 mantendo ritmo:** +R$981k → Total 2026 ≈ R$1,96M (65% da meta)
> **Para atingir R$3M:** precisa R$2.018.207 em Jul–Dez = R$336k/mês (impossível sem Walton ou projeto âncora)

### Recebíveis em aberto — R$ 366.709 (planilha 22/06/2026)

**Maiores pendências (a cobrar com urgência):**

| Cliente | Projeto | Valor Aberto | Observação |
|---|---|---|---|
| Cristiane | Casa completa | **R$ 79.200** | Abr/2026 — parcela única de R$22,5k recebida |
| **Andre Alphaville** | **Casa** | **R$ 70.800** | Abr/2026 — **projeto de investimento dos sócios** (não é venda a cliente — recebimento retorna conforme o investimento se realizar) |
| Maria - Vale dos Cristais | Casa | **R$ 58.869** | Mar/2026 — 2ª parcela pendente |
| Lucas Mello | Casa | **R$ 22.000** | Jun/2026 — parcela futura |
| Marcelo e Simony | Apt novo | **R$ 21.700** | Mai/2026 — zero recebido registrado |
| Rejane | Cozinha | **R$ 21.360** | Abr/2026 |
| Augusto | Apt | **R$ 27.000** | Fev/2026 |
| Marina Borges | Casa nova | **R$ 10.000** | Mai/2026 |
| Maria VDC hall | Painel hall garagem | **R$ 9.050** | Mai/2026 |

> ⚠️ **Cristiane R$79,2k pendente** — maior risco individual. Contrato assinado?
> ℹ️ **Andre Alphaville** permanece no faturamento e no total a receber. Não é
> inadimplência — é recebível de investimento dos próprios sócios.

### Nota interna: análise de comissões de marceneiros (planilha)
Jonathan está analisando reajuste na base de cálculo da comissão dos marceneiros:
- Atual: 5% sobre faturamento bruto → R$150k/ano sobre meta de R$3M
- Proposta: 5% sobre (faturamento − custos de venda: NF 7,5% + vendedor 4% + RT 5% = 16,5%)
  → base reduzida para R$2.505.000 → comissão R$125.250
  → **economia de R$24.750/ano = R$2.062/mês**
- Impacto: moderado (−2k/mês), mas alinha incentivo (marceneiro ganha mais quando custo de venda é menor)

### Crescimento histórico

| Ano | Faturamento | Crescimento |
|---|---|---|
| 2023 | R$ 645.614 | — |
| 2024 | R$ 1.035.980 | +60% |
| 2025 | R$ 1.504.141 | +45% |
| 2026 (projeção realista) | ~R$ 1.780.000 | +18% |
| Meta oficial 2026 | R$ 3.000.000 | inalcançável |

---

## 4. Metas calibradas (Rodrigo, jun/2026)

| Situação de caixa | MC mínima | Observação |
|---|---|---|
| **Caixa crítico (atual)** | **37%** | Exceção máxima — só com capacidade ociosa |
| Caixa ruim | 30% | Exceção consciente e raríssima |
| Caixa normal | 43% | Piso operacional padrão |
| **Alvo saudável** | **48–50%** | Gera lucro real + amortiza dívidas |

> Meta de MC mensal: min 43% para projetos regulares. Para projetos grandes
> (>R$ 80k), mínimo 40% COM ENTRADA de 40% antes de iniciar.

### Política obrigatória de entrada (a implementar)
- **Todos os projetos**: entrada ≥ 40% antes de iniciar produção
- **Projetos grandes**: parcelas vinculadas a etapas de entrega
- **Zero projetos com pagamento total no final** — é o que causa meses de zero recebimento

---

## 5. Plano de ação vigente (jun/2026)

### 🔴 URGENTE — Esta semana
1. Cobrar os R$ 295.909 em aberto de clientes (prioridade: Cristiane R$79,2k, Maria VDC R$58,9k, Augusto R$27k — Andre Alphaville R$70,8k é investimento dos sócios, não cobrança a cliente)
2. Investigar composição dos R$ 107k de pagamentos em dez/2025
3. Investigar R$ 101k de pagamentos previstos em jun/2026 — o que é postergável?
4. Fechar Kênia & Fábio (casa completa): MC ≥ 40%, entrada 40% obrigatória

### 🟠 30 dias
5. Vitor ativar pipeline H2/2026 — reativar orçamentos parados (90 dias)
6. Levantar break-even de CAIXA real: serviço das dívidas (máquinas + Paulo)
7. Revisar e recalibrar meta 2026 para R$ 1.8M (realista, ainda seria recorde)

### 🟡 90 dias
8. Constituir reserva de emergência: R$ 70k (45 dias de custo fixo)
9. Implementar política de entrada ≥ 40% em contrato
10. Parar investimentos em ativo fixo até caixa positivo consolidado

---

## 6. Handoffs com os outros agentes

| De / Para | O que passa | Formato |
|---|---|---|
| **Lavinia → Rodrigo** | MC% + MC R$ + custo total por projeto | JSON do app ou briefing |
| **Rodrigo → Lavinia** | Piso de MC + situação de caixa | "caixa CRÍTICO, piso 37%, ideal 43%+" |
| **Rodrigo → Vitor** | Margem de negociação + estratégia de fechamento | "sem desconto de preço, entrada 40% obrigatória, prioridade H2" |
| **Jonathan → Rodrigo** | Projeção de caixa + dados de dívidas | Texto livre ou planilha |

### Recado atual para a Lavinia:
> **CAIXA CRÍTICO** — piso de exceção: 37%. Piso ideal: 43%+.
> Para projetos grandes (>R$ 80k): mínimo 40%, entrada de 40% ANTES de iniciar.
> Não ceder abaixo de 40% em hipótese alguma nos próximos 30 dias.

### Recado atual para o Vitor:
> **Pipeline H2 zerado — emergência comercial.**
> Fechar Kênia & Fábio é prioridade 1. Reativar orçamentos parados, prioridade 2.
> Sem margem para desconto de preço. Alavanca: prazo, qualidade, referências.
> Todo projeto novo: entrada 40% obrigatória antes de iniciar.

---

## 9. FRENTE INVESTIDOR — Walton (aberta 11–17/06/2026)

> 📄 **Registro completo desta frente:** `dados/dossie-investidor-walton.md`
> (personagens, áudios, blocos de diligência, cenários de deal A–D, links de
> estudo, resposta-modelo ao teste de escala e roteiro da reunião de terça).
> O resumo abaixo é o essencial; o dossiê é a fonte completa.

### Personagens
- **Walton** — investidor. Multi-setorial (construtora, avião, gado, locadora de
  veículos). Da igreja do Otávio. Conhece donos de construtora — citou **Caparaó
  e Terraza**. Método: entra como **sócio investidor** em empresa que JÁ tem
  atuação no mercado, aporta **dinheiro + contatos** (ex.: entrou numa locadora
  pequena e escalou com contato + capital). Quer marcenaria focada em **luxo +
  construtora + incorporação**, galpão/escritório no Jardim Canadá. Lema dele:
  *"trabalhar com rico, com crise ou sem crise."* Está fazendo diligência séria
  (pediu levantamento das maiores marcas de marcenaria do Brasil/BH).
- **Otávio** — intermediário. Cliente antigo da Valvic (casa na Fazenda da Serra),
  demitido do laboratório em 01/abr, hoje trabalha com o Walton. Incentivo dele é
  FECHAR o negócio (novo emprego) — pode supervalorizar para os dois lados.
- **Alternativa do Walton:** um "menino de Governador Valadares" que cresceu em
  marcenaria (greenfield). Mas exige mudança de cidade/família — mais sensível.
  **Vantagem da Valvic:** já é empresa estabelecida — encaixa no método do Walton
  (entrar em quem já roda) melhor que começar do zero.

### ⚠️ INSIGHT CENTRAL — a ilusão de margem
Walton entrou na tese por um MAL-ENTENDIDO: viu um orçamento de R$ 280k onde
"R$ 80k era material e R$ 200k era margem". **Ele acha que marcenaria de luxo tem
~70% de margem.** Realidade Valvic: MC bruta 43,5%, MC líquida 34%, lucro ~2%,
break-even R$ 246k/mês. Risco: se entrar achando 70% e descobrir 2%, sai ou
aperta. Oportunidade: a tese dele está certa pelo motivo errado — a conta só
fecha em **VOLUME**, e ele traz volume. Reposicionar de "caçador de margem" para
"sócio de volume". **Postura decidida pelo Jonathan: na reunião 1, ESCUTAR
primeiro, não tocar em margem até ele pedir número.**

### A obsessão do Walton: ESCALA + CAPACIDADE PRODUTIVA
Roteiro de diligência que o Otávio mandou (os "blocos"):
- **Bloco 1 — Capacidade atual:** projetos/mês, ambientes/projeto, faturamento
  máximo num mês, quando a fábrica chegou no limite, maior volume entregue,
  capacidade ociosa.
- **Cadeia de valor:** quem mede / projeta / vende / instala; equipe própria ou
  terceirizada; gargalo; retrabalho; prazo médio; reclamações.
- **Bloco 8 — Teste de escala:** 10 aptos/mês? 20? construtora com 50/trimestre?
  Pegadinha explícita: *"observe se responde com NÚMEROS ou só com confiança.
  Empresário preparado responde: pessoas necessárias, investimento, prazo de
  adaptação, impacto no caixa."*

### Decisão estratégica a alinhar Jonathan+Paulo ANTES da reunião
Tese do Walton (volume padronizado p/ construtora) ≠ modelo atual (bespoke, "a
marcenaria como ela é", projeto do arquiteto). Jonathan já sacou no áudio: *"não
sou uma Marcato"*. **Recomendação Rodrigo: MODELO DE DUAS PISTAS** — manter
bespoke premium (marca + margem) E criar linha incorporação modular/padronizada
(absorve o volume do Walton). É onde o capital dele faz sentido: financiar a
pista industrial sem trair a identidade. Conecta ao diagnóstico de sempre:
capacidade instalada já paga + ociosa + volume do investidor = projeto
incremental altamente lucrativo.

### Resposta-modelo ao teste de escala (terça)
Não responder sim/não. "Capacidade se mede em unidades de produção, não em aptos.
Me define o padrão (m², ambientes, laca/lâmina, complexidade) que eu te digo
capacidade, pessoas, investimento e prazo. Hoje entregamos ~R$150k/mês, pico de
R$260k. Para 10 aptos do padrão X: +N pessoas, +máquina Y, R$Z, W meses de
ramp-up + capital de giro (material compra antes de receber)." **Quem define a
unidade controla a conversa.**

### Apetite definido pelo Jonathan
- Formato: **ABERTO a sociedade (equity), COM PROTEÇÕES** — valuation justo +
  vesting atrelado ao pipeline + cláusulas de controle (tag/drag along, preferência).
- ⚠️ Não dar equity barato. Capital sem pipeline = revenue share, não sociedade.
- Valvic tem 2º pretendente (cliente da Fazenda da Serra, parado pq mãe adoeceu)
  = alavanca de "não dependo dessa mesa".

### Pendências desta frente
- 🔴 **Levantar com Paulo (operacional p/ reunião):** projetos produzidos/mês,
  ambientes/projeto, cadeia (medição/projeto/venda/instalação), própria×terceira,
  gargalo, retrabalho, prazo médio, reclamações, maior volume entregue.
- 🔴 Alinhar Jonathan+Paulo na tese "duas pistas" antes de terça.
- 🟠 Produzir material da reunião (deck visual e/ou roteiro de bolso) — pendente
  de definição do Jonathan.
- ⚖️ LEMBRAR: Rodrigo é consultor financeiro, NÃO advogado. Sociedade exige
  advogado societário antes de assinar.

---

## 10. Pendências abertas para o Rodrigo

### 🔴 Dados a levantar com Jonathan
- Composição dos R$ 107k de pagamentos em dez/2025 (o que causou o buraco?)
- Composição dos R$ 101k previstos em jun/2026
- Parcelas mensais das dívidas ativas: máquinas CNC/coladeira + empréstimo Paulo
- ~~Status de Andre Alphaville (R$ 70.800)~~ ✅ Esclarecido: é projeto de **investimento dos sócios**, não recebível de cliente.
- Status de Marcelo e Simony (R$ 21.700) — inadimplência ou parcela futura?

### 🟢 Concluído
- Painel HTML financeiro (Demanda 2) — entregue com resultado mês a mês,
  crescimento ano a ano e dados reais da planilha importados (offline + seed).

### 🟠 Em construção
- Integração planilha Google Sheets ↔ painel (Apps Script — setup em andamento)

---

## 11. Referências

| Arquivo | O que é |
|---|---|
| `referencias/metodo-rodrigo.md` | Método Rodrigo Almeida (4 pilares, sequência) |
| `referencias/auditoria-metodo.md` | Auditoria da meta de MC |
| `dados/custo-fixo.md` | Números reais — atualizar com DRE jun/2026 |
| `dados/faturamento-historico.md` | Faturamento mês a mês 2023–2026 (planilha) |
| `dados/dossie-investidor-walton.md` | Frente do investidor Walton — registro completo |
| `ferramentas/custo-operacao.html` | App de levantamento de custos operacionais |
| `SKILL.md` | Persona completa do Rodrigo |
| `../../GUIA-ORCAMENTOS.md` | Guia da Lavinia |
| `../../MOLESKINE.md` | Notas e tarefas entre sessões |
