# Moleskine Digital — Valvic

Arquivo de tarefas e recados entre sessões. Qualquer agente (Lavinia, Rodrigo, Vitor…)
pode ler e escrever aqui. Formato livre — marcar data e agente responsável.

---

## Tarefas abertas

### [2026-06-16] Novo layout de proposta — Vitor
**Solicitante:** Jonathan  
**Agente:** Vitor  
**Status:** 🔴 Pendente

**O que foi pedido:**  
Criar um novo layout/template de proposta para o Vitor — diferente dos modelos atuais
no Canva (MODELO e MODELO ENXUTO). Jonathan quer um design novo com:
- Nova linha do tempo visual
- Links para Instagram e YouTube da Valvic
- (outros detalhes a confirmar com Jonathan na próxima sessão)

**Contexto:**  
A demanda surgiu na sessão de 2026-06-16 mas foi interrompida antes de Jonathan
especificar o design completo. Retomar perguntando: "Quais seções quer no novo
layout? Referência visual? Links exatos do IG e YouTube?"

**Arquivos relacionados:**  
- Templates atuais: MODELO `DAHMsJxsuhE` · MODELO ENXUTO `DAHMsEfQNas`  
- Referência de identidade: `.claude/skills/closer-vendas/referencias/identidade-marca.md`

---

## Tarefas concluídas

*(mover aqui quando feito, com data de conclusão)*

### [2026-06-19] Orçamento + Proposta — Halls Ed. Luxemburgo — Lavinia + Vitor
**Solicitante:** Jonathan · **Status:** 🟢 Concluído

Orçamento e proposta dos halls do **Condomínio Ed. Luxemburgo** (Arq. Rosana Miraglia).
Escopo Valvic = revestimento em **MDF amadeirado** (painéis dos halls de 2 e 4 apt +
molduras de espelho no hall social). Fora: granito, gesso, portas prontas, papel,
pintura, porcelanato, rodapé poliestireno, blindex, arandelas e **madeira de demolição**.
- Fechado: **versão única Hardt** (garantia 5 anos), **sem RT**, espelhos em linha
  separada, **MC 37%**, preço **unitário** (1 hall de cada).
- Preços: 2 apt **R$ 9.070** · 4 apt **R$ 12.710** · social A+B **R$ 4.780** ·
  espelhos **R$ 8.730** · total 1-de-cada **R$ 35.295**.
- Prazo 100–120 dias úteis · pagamento 40% entrada + 30% entrega + 30% boleto 30d ·
  validade 7 dias · cliente: Condomínio Ed. Luxemburgo (Igor, 31 98814-4127).
- **Arquivos:** `projetos/2026-ed-luxemburgo-halls.md` · `orcamento-ed-luxemburgo-halls.json` ·
  `proposta-ed-luxemburgo.html`/`.pdf`. Proposta subida ao Drive (pasta do cliente).
- **Pendências:** confirmar prazo do boleto (assumido 30 dias); ver recado p/ Rodrigo.

---

## Aprendizados

### [2026-06-19] Método e ferramentas (projeto Luxemburgo) — Lavinia/Vitor
- **Medir revestimento por PIXEL nas elevações 1:20.** Isolar a cor do MDF amadeirado
  na imagem e converter px→m² (fator linear = 2,54/dpi × escala; área = fator²).
  Ótimo p/ revestimento de parede sem cotas item-a-item; conferir contra 1 cálculo
  manual. (Halls: ~10,2 m² no 2 apt; ~14 m² no 4 apt.)
- **Escopo de hall de arquitetura:** separar SEMPRE a marcenaria (MDF amadeirado) do
  resto (granito, gesso/sanca, portas prontas, papel, pintura, porcelanato, rodapé
  poliestireno, blindex, arandelas). **Madeira de demolição = maciça → fora** quando
  o cliente pede "sem maciça".
- **Condomínio:** orçar por HALL (unitário) × nº de pavimentos; hall social é único (A+B).
- **Ferragem muda preço E garantia:** Hardt = 5 anos (dobradiça ~R$8) · Hettich Sensys
  = 10 anos (~R$35). Trocar ferragem → reprecificar e reajustar a garantia. Upsell de
  garantia = subir p/ Hettich (+R$264 no 2 apt, +R$393 no 4 apt).
- **Proposta HTML→PDF (weasyprint) — armadilhas:** (1) NÃO renderiza `background`
  multi-camada nem `var()` dentro de gradiente → o painel "some". Usar **divs sólidos**
  (slats) p/ o painel amadeirado/frisos; gradiente ÚNICO funciona (usei no LED).
  (2) `min-height:297mm` + página cheia estoura p/ uma página extra — deixar folga.
- **Canva:** brand-template **autofill exige plano pago** (bloqueado nesta conta).
  Fallback oficial = **HTML→PDF** (precedente K&F). A API do Canva **não adiciona/remove
  linhas de tabela** — limita reaproveitar os masters p/ nº de itens diferente.

---

## Recados rápidos

*(notas passageiras — podem ser apagadas após lidas)*

### [2026-06-16] Rodrigo → Lavinia
**CAIXA CRÍTICO.** Piso de exceção: 37%. Ideal: 43%+.
Projetos grandes (>R$ 80k): mínimo 40%, ENTRADA de 40% antes de iniciar produção.
Não fechar nenhum projeto sem entrada real. H2 está zerado — cada venda conta.

### [2026-06-16] Rodrigo → Vitor
**Pipeline H2/2026 zerado — emergência comercial.**
Prioridade 1: fechar Kênia & Fábio (casa completa, MC ≥ 40%, entrada 40%).
Prioridade 2: reativar orçamentos parados nos últimos 90 dias.
Sem margem para desconto de preço. Sem desconto = sem negociação de preço.
Cobrar Andre Alphaville (R$ 70.800 em aberto) e Marcelo e Simony (R$ 34.850).

### [2026-06-19] Vitor → Rodrigo / Jonathan
Luxemburgo fechou a **MC 37%** (seu piso de exceção do caixa crítico) com **entrada de
40%** — atende sua regra de entrada. ⚠️ **Atenção:** o preço é por hall; se o total do
prédio passar de **R$ 80k** (vários pavimentos), sua regra pede **MC mínima 40%**.
Avaliar subir a margem no fechamento do prédio inteiro ou manter 37% como exceção.

