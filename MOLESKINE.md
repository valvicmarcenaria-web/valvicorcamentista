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

### [2026-07-17] Orçamento + Proposta — LM / SPE Nova Lima 1 (comercial: painéis + pérgola) — Lavinia
**Solicitante:** Jonathan · **Projeto:** arq. **Lodi Motta / JBA** · **Status:** 🟢 Proposta entregue
Stand de vendas comercial (2 pranchas executivas CAD): **MOB 01** Painel Corretores/Pilar + **MOB 02** Painel/Pérgula Gourmet-Lounge.
- **Leitura do VETOR do CAD** (não OCR/olho): cotas exatas de planta/elevações. Alturas painel 2,62 m.
- **PÉRGOLA cravada:** cadeia de cotas = **28 faces de 8** → **28 ripas** de metalon #10×5 × **3,09 m** (projeção). Barra 6 m, 2×3,09>6 → **1 ripa/barra = 28 barras** × R$150 + R$150 frete dedicado = **R$ 4.350**. (Cliente já sabia que não dá 2 numa barra — bateu.)
- **Painéis Cravo Trend** parede a parede: MOB02 62,9 m² + MOB01 ~35,8 m² + porta ripada + armário ext = **107,5 m² → 25 chapas**. Móveis Moscada Matt (móvel lounge 300×60×35 + armário gourmet 97,5×248×42). MDF madeirado (pérgola+forro) 11 chapas. **39 chapas**, custo material **~R$ 34.900**.
- **Preço:** chapa Arauco Realce R$ 500 · **sem RT** · **MC 40%** → **R$ 91.300**. Pagto 40/40/20, prazo 45–60 úteis, garantia 2a. Proposta comercial config única (sem linhas de ferragem), capa tipográfica (sem render, é CAD).
- **Não inclusos:** forro gypsum (gesseiro), pontos elétr./hidr., obra civil.
- **Rev. (Jonathan revisou):** tirei **veneziana** (a "porta ripada" da Elev.2 = veneziana, terceiro) e **vidro jateado** do pilar (vidraceiro) → **R$ 91.300 → R$ 88.200**. Corretor **não é balcão** — é backdrop + **caixa em marcenaria** (nicho recuado). **Inox** = rodapé perfil inox escovado 5cm (DET.02, serralheria). ⚠️ Lição: não rotular "ripado/balcão" no olho — conferir se é veneziana/nicho; e itens escritos na prancha (vidro) podem ser terceiro/existente, sempre confirmar escopo.
- **Aprendizado:** ler cota do vetor (`get_text('words')`) é o método exato pra prancha CAD — clusterizar cadeias horizontais/verticais dá comprimento de parede e contagem de ripas sem erro. Coordenada do vetor = pt; imagem 2,2x = ×2,2.
- **Arquivos:** `2026-lm-painel-pergola.md` · `corte-lm.py` · `build-lm.py` · `proposta-lm.html/.pdf`.

### [2026-07-16] Orçamento + Proposta — Graça (despensa + lavanderia + tanque) — Lavinia
**Solicitante:** Jonathan · **Projeto:** arq. **Lais Teles** (RT 10% líq.) · **Status:** 🟢 Proposta entregue
3 ambientes, 4 conjuntos de marcenaria, **projeto 100% MDF Azul Petróleo Guararapes** (25 pranchas, "Detalhamento").
- **CÁLCULO peça-a-peça** (`corte-graca.py`, 57 peças) → **9 chapas R$ 4.000**. Despensa = armário superior **revestido** (existente) + bancada em L (2 gavetões, nichos, **3 cestos aramados**, LED 3000 K). Lavanderia = torre da máq. de lavar (puxador cava passante). Tanque = balcão 2 portas. **Tampos (bancada despensa + tanque) = pedra/marmorista, fora.**
- **Preço (motor COM cartão, RT 10%):** **Essencial (telescópica/2a, MC 32%) R$ 20.100** · **Essencial Prime (oculta alemã Hardt/5a, MC 37%) R$ 24.000.** Alocação: Despensa 64,4% · Lavanderia 29,1% · Tanque 6,5%.
- **Rev. 16/07 (tarde) — ajustes do Jonathan:** (1) **100% Azul** (nada de Branco TX na caixaria); (2) **tampo é pedra** (fora); (3) **nesting unificado** (tudo uma cor → pilhas somadas), efeito **11→9 chapas** (unificar cor −1, tampo pedra −1); (4) **2ª linha +5% de MC** (32→37%) → gap ~R$ 3.900. ⚠️ Essencial a 32% abaixo do piso do Rodrigo (exceção 37%) — decisão do Jonathan.
- **Layout:** 1ª versão ficou "pesada" (blocos sólidos empilhados) → refeita **leve/editorial** (fios finos, tinta petróleo suave na Prime, pill "Recomendada"). **Bug pego:** `min-height:297mm` no WeasyPrint não enche a folha → rodapé `absolute` colava no conteúdo; corrigido com **`height:297mm`**.
- **Aprendizado:** projeto de cor única otimiza chapa (sem pilha Branca vs cor com sobra separada). Diferenciação por modelo/garantia, não por marca (regra da casa). **Pagto:** escala padrão. **Prazo 60–90 dias.** Proposta **enxuta (3 págs)**.
- **Flags:** nº de folhas do armário existente · larg. bancada 136 vs 154 (adotado 154) · puxador despensa/tanque.
- **Arquivos:** `2026-graca-marcenaria.md` · `orcamento-graca.json` · `corte-graca.py` · `build-graca.py` · `proposta-graca.html/.pdf` · `img-graca-*.png`.

### [2026-07-16] Orçamento + Proposta — Resolve Consórcio (comercial, 14 amb.) — Lavinia + Vitor
**Solicitante:** Jonathan · **Parceira:** Jéssica Sollero (RT 10%) · **Eng.:** Corsino Soares · **Status:** 🟢 Proposta entregue
Escritório corporativo completo (14 ambientes, 54 pranchas) — recepção, salas, convivência, coffe point, refeitório,
jurídico, compliance, **63 lockers**, comercial, CEO, CALL + **7 cabines**. **Refeito do zero** (v1/v2 estimativas erradas).
- **CÁLCULO peça-a-peça** (`corte-resolve-consorcio.py`, 257 peças) → **79 chapas R$ 29.770** (v1 estimava 106, v2 49 — as duas erradas).
  **Ripado = produto Eucatex RU Freijó Brasil** (0,75 m²/cx, R$ 166,50/cx, ref. web). Material Valvic ~R$ 61k (Hardt).
- **Preço (motor sem cartão, RT 10%):** **Essencial (Hardt/5a/MC35%) R$ 147.800** · **Essencial Prime (Hettich/10a/MC38%) R$ 174.800.**
  Alocação por ambiente **proporcional ao material** (lockers 16,9%). Pagto **40/40/20**, prazo **90–100 dias corridos**.
- **Escopo:** inclui estofado dos bancos + pés metálicos + escorredor cromado. **FORA:** blindex, espuma acústica, fechaduras dos lockers.
- **Lição cravada na skill:** *CALCULAR, nunca ESTIMAR* (princípio nº 1). ⚠️ MC 35/38% abaixo do piso 40% do Rodrigo p/ >R$80k — decisão do Jonathan.
- **Arquivos:** `2026-resolve-consorcio-marcenaria.md` · `orcamento-resolve-consorcio.json` · `corte-resolve-consorcio.py` · `proposta-resolve-consorcio.html/.pdf`.

### [2026-07-14] Orçamento + Proposta — Jairo Samuel (apto completo) — Lavinia + Vitor
**Solicitante:** Jonathan · **Parceira:** Jéssica Sollero (RT 10%) · **Status:** 🟢 Proposta entregue (v002)
Marcenaria completa do apto (projeto Jéssica Sollero, 27 pranchas). **9 móveis MDF:** cristaleira (Sala,
Carvalho Hanover) · cozinha completa (superiores Cinza Cristal Chess + inferiores Lord + prateleiras) ·
cabeceira + roupeiro (Hóspede, Beige Matt) · roupeiro + painel/prateleiras + mesa (Suíte, Lord).
- **2 linhas pela ferragem, nomeadas pelo MODELO Valvic** (a pedido — sem citar marca):
  **"Essencial"** (Hardt · 5 anos · MC **32%** · **R$ 70.400**) · **"Essencial Prime"** (Hettich Sensys+Quadro ·
  10 anos · MC **35%** · **R$ 83.900**). Premium evidencia **engenharia alemã** (ciclagem 100k, ajuste 3D) e garantia superior.
  (nomes v1 "Assinatura/Assinatura Alemã" trocados por Essencial/Essencial Prime a pedido do Jonathan.)
- **Quantitativo com PLANO DE CORTE** (premissa nova da skill) → ~34 chapas · fita+filetagem · ~64 dobr. + 16 corr.
  ocultas · LED 9 m · terceirizados (vidros cristaleira + espelho + estofado cabeceira) · **insumos** (cola, parafusos,
  limpeza/embalagem) não esquecidos. Cliente **criterioso** → proposta puxa acabamento, garantia, pós-venda e a
  **parceria de anos com a Jéssica**. Prazo **60–70 dias úteis**.
- 🚫 **DIVISÓRIA de TV (Metalon + cachepots) FORA** (confirmado cliente) · toda serralheria/marmoraria fora do escopo
  (por fornecedor parceiro) — só a marcenaria MDF entrou.
- **Margens:** v001 era 37/42% (R$81k/105k); revistas p/ **32/35%** a pedido do Jonathan.
- **Arquivos:** `projetos/2026-jairo-samuel-marcenaria.md` · `orcamento-jairo-samuel.json` · `proposta-jairo-samuel.html`/`.pdf`.
- **Pendências:** ① confirmar coordenação da **serralheria** (Valvic gerencia ou fica com o serralheiro?) · ② **ripado dos
  banhos** sem cota · ③ cota "113" da cristaleira não fecha (conferir DWG p/ porta de vidro) · ④ prof. do roupeiro da suíte
  (adotei 55) · ⑤ refinar quantitativo no app após **medição no local** · ⑥ subir a proposta ao Drive (pasta do cliente).

### [2026-06-25] Orçamento + Proposta — Camila (Closet) — Lavinia + Vitor · rev. 10/07
**Solicitante:** Jonathan · **Status:** 🟢 Concluído
Closet = **Roupeiro em L (piso-teto) + Ilha**. Fechou em **config única** (evoluiu de 2
versões — correr ripado × básculas — que foram descartadas). **R$ 24.900** ·
RT **10%** embutido · ferragem **Hardt** → garantia 5 anos.
- **Roupeiro** (piso-teto, 2 cores cinza + Cumaru **USINADO**, não ripado): 3 portas de
  correr **RO-65 piso-teto** (trilho 3 m + desempenadores) + 2 portas menores (43 cm) de
  **giro** (dobradiças Hardt). Gavetas em corrediça oculta Hardt + puxador SP7000. LED +
  sensor. **Eliminados:** módulo superior, báscula/Multi, tábua de passar.
- **Ilha (rev. 10/07):** agora **marcenaria** — **estrutura com 4 gavetas** (corrediça oculta
  Hardt + puxador Enlevo), **base SEM serralheria**. Saiu a serralheria da base e o tampo de
  vidro. **R$ 4.200** (era R$ 6.800). Repreço a pedido do Jonathan.
- **Alocação:** Roupeiro **R$ 20.700** · Ilha **R$ 4.200** → **total R$ 24.900**.
- **Pagamento (rev. 10/07):** condição única **50% entrada + 50% na entrega** (transferência)
  com **8% de desconto → R$ 22.908**. (Saíram as opções de cartão/parcelamento.)
- **Arquivos:** `orcamento-camila-v3-mc32.json`, `orcamento-camila-closet.html/.pdf`,
  `proposta-camila.html/.pdf` (proposta de config única, **atualizada 10/07**).
- **Drive (pasta "Camila"):** Docs **ATUAL** (proposta + orçamento interno v3). ⚠️ Subir a
  proposta rev. 10/07 no lugar. Há **2 Docs antigos** (das versões 2-cenários) a **apagar**
  pelo Jonathan — o Drive MCP não deleta.
- **Pendências:** ① atualizar o **orçamento interno v3** (linha da ilha ainda com serralheria/vidro
  → recalcular MC com o novo custo da ilha em marcenaria); ② confirmar prazo (usei 60–70 dias
  úteis); ③ trocar render da capa por foto real.

### [2026-06-27] Orçamento + Proposta — Raquel (Roupeiro Branco TX) — Lavinia + Vitor
**Solicitante:** Jonathan · **Status:** 🟢 Concluído
Roupeiro piso-teto de **6,30 m**, todo em **MDF Branco TX 15 mm**, **portas de giro** com
puxador **Liveri IL955 192 mm** (Italy Line), interior completo (cabideiros, prateleiras e
**até 25 gavetas/sapateiras deslizantes** — puxadores espaçados, sem cava). **Sem LED.**
- **Duas linhas de ferragem** (mesma estrutura/portas): **Premium** (corrediça oculta Hardt
  + dobradiça Hardt → 5 anos) **R$ 30.000** (MC **35,2%** — ÂNCORA) × **Essencial**
  (telescópica + dobradiça padrão → 2 anos) **R$ 25.000** (MC **30%**). RT 0. Gap = R$ 5.000.
- **Arquivos:** `orcamento-roupeiro-branco-tx.json` (v003), `proposta-roupeiro-branco-tx.html/.pdf`.
- **Proposta:** 5 páginas, 2 opções lado a lado · prazo **60 dias corridos** · validade
  **30/06/2026**. Drive: pasta **"Raquel"** criada + **Doc nativo** da proposta; PDF visual no chat.
- **Pendências:** confirmar custo de compra do **Liveri IL955** (usei R$ 40/un); confirmar
  nº de chapas na **elevação das portas** (~14 portas de giro; ±2-3 chapas no nesting).

---

## Painel de orçamentos (dashboard)

### [2026-07-16] Painel fixo de orçamentos — Lavinia
**Artifact (link fixo):** https://claude.ai/code/artifact/19b63c82-17d8-4b8c-a5b7-b95c63abb71d
**Fonte no repo:** `painel-orcamentos.html` (raiz) = **versão COMPACTA/widget** (o que está publicado — feito p/ ficar
fixo no painel lateral: hero de valor total, ticket, nº fechados, lista enxuta + status dot). A **versão detalhada**
(KPIs + gráfico de barras + tabela completa) está preservada em `painel-orcamentos-detalhado.html`.
- **Dados:** array `ORCAMENTOS` no `<script>` (KPIs recalculam sozinhos ao adicionar item). Também `PARADOS`.
  Atualizar `DATA_ATUALIZADA` a cada mudança. `dp` = pendências Drive (conta ausente+desatualizado).
- **Como atualizar:** editar `painel-orcamentos.html`, e republicar com a ferramenta Artifact **passando
  `url:` = o link acima** (senão cria um artifact novo). Na mesma conversa que publicou, basta republicar o mesmo caminho.
- Regra: **preencher o painel a cada orçamento que a Lavinia finaliza.**

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

### [2026-06-25] Proposta — clareza para o cliente (Vitor) — regra do Jonathan
- **Quanto mais conta o cliente tem que fazer sozinho, pior; quanto mais claro,
  organizado e objetivo, melhor.** Na proposta, mostrar SEMPRE o total que o cliente
  paga, pronto — nada de "some o roupeiro + a ilha". Cada cenário/opção já traz o
  conjunto COMPLETO num total único + o valor à vista.
- **Comparativo de versões na proposta:** quando há duas formas de executar (ex. módulo
  superior em correr ripado × báscula — closet da Camila), apresentar as duas como
  CENÁRIOS COMPLETOS lado a lado (roupeiro + ilha em cada), com a economia explícita —
  não só o item que muda.

### [2026-06-27] Ancoragem de preço por MC, não só por custo (Vitor/Lavinia) — Raquel
- **Diferenciar as versões pela MARGEM, não apenas pelo custo da ferragem.** No roupeiro da
  Raquel as duas linhas usam a mesma estrutura; a Premium custa só **+R$ 880** de ferragem
  (oculta Hardt vs telescópica). Precificada na mesma MC, o gap fica pequeno (~R$ 1.800).
  Subindo a **Premium para 35% de MC** (× Essencial 30%), o gap vira **R$ 5.000** — âncora
  forte que faz a Essencial parecer o "negócio certo".
- **Usar números redondos como âncora** (R$ 30.000 × R$ 25.000): mais memorável e o salto de
  qualidade (telescópica/2 anos → oculta Hardt/5 anos) fica nítido. Fechar o investimento na
  MC alvo e arredondar pra cima (motor confirma a MC realizada — Premium 35,2%).

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

