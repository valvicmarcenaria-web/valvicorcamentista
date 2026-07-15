# Moleskine Digital — Valvic

Arquivo central de conhecimento, decisões e pendências entre sessões. Qualquer agente
(Lavinia, Rodrigo, Vitor, Stefan…) pode ler e escrever aqui. Formato livre — marcar
data e agente responsável.

---

# 🚀 CENTRO DE START — LEIA ANTES DE TODO ORÇAMENTO

> **Bootstrap único da Valvic.** Comece SEMPRE por aqui (economiza tokens e evita
> refazer o já decidido). Se algo mudar, atualize aqui primeiro. Detalhe fica nas
> referências apontadas — só abra o que o projeto exigir.

### ① Modelo de preço (decorar)
- **Preço (sem RT) = custo_direto ÷ ((1 − encargos%) − MC%)**. Depois **RT por cima**:
  **Preço_final = Preço_semRT ÷ (1 − 0,093)**. ⛔ **RT/repasse NUNCA no divisor.**
- **Encargos ≈ 22%** (NF 7 · parcelamento 7 · produção 5 · coordenador 1 · erro 2 —
  *sem vendedor*). Divisor padrão MC 37% → **0,41**. **À vista = −8%** (tira o cartão).
- **MC:** meta ideal ~43,5%; **piso pela situação de caixa** (perguntar SEMPRE). Pode ser
  **por ambiente** (ex. Mônica: banheiros 37 · closet 33 · cozinha 35). Projeto >R$80k:
  MC ≥ 40% + entrada 40%.

### ② Regras inegociáveis (cravadas — não repetir erro)
1. **NUNCA chutar quantitativo** — cut list peça a peça das cotas do desenho.
2. **Acabamento é lido POR AMBIENTE** — laca/LED/vidro/puxador só onde o desenho daquele
   móvel mostra; **nunca herdar** de outro ambiente. *(erro closet Mônica: laca+LED que não existiam)*
3. **Puxador abaulado/chanfro curvo → topo em LACA** (fita não acompanha a curva). Item
   próprio ~R$3.500/ambiente.
4. **Marmoraria/pedra + drywall/gesso + louças/metais → NUNCA são Valvic** (não perguntar).
5. **Ripado sempre régua a régua** (nunca multiplicador de área). **Porta de passagem = item próprio.**
6. **LED embutido na nossa marcenaria = escopo Valvic** (fornecemos E instalamos).
7. **RT/repasse fora do divisor** (regra ①). **Prazo: confirmar com Jonathan antes de cravar.**

### ③ Números de referência
- Chapa útil **5,0875 m²** (2750×1850); aproveitamento **15/18mm ≈ 0,82 · 6mm ≈ 0,55**;
  **cada cor ≥1 chapa**; fita **×1,15**; gaveta = 6 peças; filetagem máquina ~R$2,50/m,
  manual/6mm ~R$4/m; logística **por ambiente**.
- Ferragem → garantia: **Telescópica/padrão 2a · Hardt 5a · Hettich 10a · Blum vitalícia**
  (conjunto segue o elo mais fraco).

### ④ Ferramentas e modelos (não reinventar)
- **Orçamento:** `orcamentista-marcenaria/ferramentas/validacao-orcamento.html` (app oficial —
  biblioteca, ambientes, MC, import/export JSON). Fonte de preço: `dados/materiais.json`.
- **Proposta:** clonar **`closer-vendas/ferramentas/MODELO-proposta-essencial-prime.md`**
  (layout claro, 2 cenários Essencial/Prime). Instância pronta: `proposta-monica-premium.html`.
- **Descritivo da skill:** `closer-vendas/ferramentas/descritivo-lavinia.html`.

### ⑤ Fluxo e handoff
- **Lavinia** (quantitativo+preço por MC) → **Rodrigo** (piso de caixa) → **Vitor** (proposta+fechamento).
- Projetos resolvidos = `orcamentista-marcenaria/projetos/*.md` (consultar análogo antes de orçar).
- Ambiente: imagens **coladas no chat** viram base64 → embutíveis no PDF; **link de Drive não** renderiza.
- ⛔ **Drive WRITE não flui aqui:** `create_file`/upload exige aprovação que o ambiente headless não
  entrega (erro "requires approval"). Não insistir. Entregar via **SendUserFile** + **commit na branch**;
  o **Jonathan sobe no Drive** do lado dele. Drive **READ/search** funciona (metadados/IDs).

### ⑥ Antes de entregar (trava)
Rodar a **Checklist de Completude Final** (SKILL). Proposta: QA de nome único + **mensagem de
acompanhamento** pronta pro Jonathan. Nada sai sem material entre 30–40% do preço conferido.

> Abaixo: status dos projetos · aprendizados cravados (detalhe) · backlog por dono · furos.

> **Última auditoria completa do branch:** 18/06/2026 (Lavinia) — varredura dos 85
> arquivos das 3 skills (orçamentista, closer, financeiro) + docs de raiz + fontes.
> O que a varredura achou está consolidado abaixo (estado dos projetos, aprendizados
> cravados, backlog por dono, furos/contradições).

---

## 🗂️ Estado dos projetos (status board)

| Projeto | Status | Valor / MC | Pendência principal |
|---|---|---|---|
| **Mônica Cristina** (banheiros + closet + cozinha) | ✅ Orçado + proposta (modelo Essencial Prime) | Essencial R$ 83.550 / Prime R$ 107.600 · MC banh.37 · closet 33 · coz 35 | Confirmar **prazo** c/ Jonathan; subir renders reais se houver |
| **Júnior — Lagoa Santa** (casa completa, 9 amb.) | ✅ Orçado + proposta entregue | A R$ 395k (~38%) / B R$ 370k (~36%) | Refinar quantitativo Fase-1 (±25%) com cotas reais antes da produção |
| **Kênia & Fábio — casa completa** (15 amb., ~60 mód.) | ✅ Orçado (Fase 2) | R$ 481.000 / MC 42% | 4 dúvidas abertas (ver backlog); ⚠️ status contraditório no `.md` (header "orçado" vs "próximos passos A FAZER" — reconciliar) |
| **Lucas e Ana — Apto 101** | 📘 Referência resolvida | Gold R$ 181.800 / Silver R$ 169.950 | 🔴 TODO: completar quantitativo dos demais ambientes + fechar regra "peças → nº de chapas" |
| **Camila — Closet** (treino/calibração) | 🧪 Calibração | Material Lavinia R$ 12.858 vs Jonathan R$ 13.793 (+7%) | Base das lições de calibração (ver aprendizados) |
| **Treino** (aline / luiz / camila) | 🧪 Parado | — | 🔴 Conectar renders 3D às peças + Marcos calibrar manual vs. real |
| **Refs Valvic OS** (Marcelo&Simony · Roberto Lima R$128k/MC31,4% · Horizonte) | 📄 A desenvolver | — | Desenvolver exemplos detalhados com o Jonathan |

---

## ⭐ Aprendizados cravados (NÃO apagar)

### Precificação / margem
- **[17/06] RT e todo REPASSE NUNCA entram no divisor de margem.** Fecha-se o preço na
  MC-alvo **sem RT** e soma-se por cima: `Preço_final = Preço_semRT / (1 − 0,093)` (RT
  10% do líquido ≈ 9,3% do bruto). Erro real evitado: +R$ 100k num projeto de R$ 324k.
  A MC em R$ da Valvic não muda com/sem RT. Detalhe em `validacao-orcamento.md`.
- **Meta de MC = ~43,5%** (regra Rodrigo/SKILL), com **piso pela situação de caixa**.
  Projeto grande (>R$ 80k): **MC ≥ 40% + entrada de 40%** antes de produzir.
  ⚠️ Vários arquivos antigos ainda dizem "35–40%" — ver Furos.
- **Regra de bolso:** variáveis ≈ 56,5% → MC ~43,5%; **material 30–40% do preço** (se
  passar de 40%, sinalizar). Âncora rápida: `Preço ≈ custo material ÷ 0,35`.

### Quantitativo / construção
- **Ripado NUNCA por multiplicador de área — sempre régua a régua** (cravado 17/06):
  `nº réguas = largura útil ÷ passo` → `fita = nº réguas × comprimento` + filetagem +
  chapa das ripas + colagem. É o **maior gargalo de fita** (caso Junior: 1 painel
  3,50×2,73 = 78 réguas = 213 m de fita ≈ R$ 1.170 só nele).
- **Porta de passagem = ITEM PRÓPRIO** (cravado 17/06), nunca diluída em m² de painel:
  folha ~4 cm = **2× MDF 15 mm + 2 barras de metalon** (R$ 100/barra = R$ 200/porta) +
  marco/alizar + pivô/trilho + puxador + tranca. ~R$ 1,5–2,5k/porta.
- **Painel apoiado no chão → perfil de alumínio de proteção na base, R$ 15/m linear**
  (regra Jonathan, handoff Juninho 18/06). Quantidade = largura do painel.
- **Interior dos closets NA COR das portas** (padrão alto-padrão) — não assumir branco.
- **Ler a espessura no desenho** (não assumir 15 mm). Prateleira larga >70 cm → 18 mm.
  *Caso Júnior:* prateleiras e montantes de louçaria em **30 mm** (estética + carga) —
  **caso específico, NÃO é regra geral.**
- **Calibração do olhar (projeto Camila):** subestimo **fita de cor e ripado** (~1,7–2,7×;
  o maior furo) e o **nº de prateleiras/suportes**; superestimo **chapa branca e LED**
  (LED só no trecho real; o "L" não dobra tudo); **sempre lançar consumíveis** (baseline
  de limpeza+embalagem+fixadores ≈ 2%, nunca zero).
- **Números de referência:** chapa útil **5,0875 m²** (2750×1850); aproveitamento
  **15/18 mm ≈ 0,82 · 6 mm ≈ 0,55**; **cada cor distinta puxa ≥1 chapa** (cauda ~68%);
  fita ×**1,15**; gaveta = **6 peças**; dobradiças por altura (≤900=2 · 900-1600=3 ·
  1600-2000=4 · >2000=5+); filetagem máquina ~R$ 2,50/m, manual/6 mm ~R$ 4/m.
- **Logística por AMBIENTE, não por projeto** (carreto ~R$ 300 ida+volta; equipe de
  montagem 2–3 dias tem que entrar — antes era esquecida = subprecificação).
- **Pedra / marmoraria = SEMPRE do cliente** (regra Jonathan), em qualquer projeto.

### Acabamento / proposta (cravado 14/07 — projeto Mônica)
- **Acabamento especial é LIDO POR AMBIENTE — nunca herdado nem assumido.** *Erro real:*
  lancei **laca (+R$3.500) e LED** num closet que só tinha **puxador alça Phenix preto** →
  inflou ~R$12k. Antes de precificar: *este móvel tem laca? tem LED? qual o puxador exato?*
- **Puxador abaulado/chanfro curvo → topo em LACA** (fita não acompanha a curva: emenda,
  quebra, descola). Laca PU = selagem → primer → cabine → polimento. Item próprio (~R$3.500).
  Vender com a **promessa de AMOSTRA física na aprovação**, antes da produção.
- **MC por ambiente** é válido (Mônica: banheiros 37 · closet 33 · cozinha 35) — não forçar MC única.
- **LED = escopo Valvic** (fornecemos **e** instalamos) → argumento de praticidade na proposta.
- **Modelo de proposta oficial = "Essencial Prime"** (2 cenários de ferragem/garantia; layout
  claro). Registro: `closer-vendas/ferramentas/MODELO-proposta-essencial-prime.md`; instância:
  `proposta-monica-premium.html`. **Sistemas de porta:** Essencial **Rometal RO82 top** ·
  Prime **Siforma (italiana)**. **Sempre um detalhe visual distinto para o item premium.**
  Portas Valvic são **estruturadas com mecanismo anti-empeno** (citar como qualidade/durabilidade).

### Persona / método
- **Lavínia é sênior e pensa como o Jonathan.** Princípio supremo: "orçamento incompleto
  é pior que nenhum orçamento" → roda a **Trava de Completude Final** antes de entregar.
- **Handoff entre sessões:** instruções dadas na sessão errada (ex.: K&F) são revertidas
  e migradas para um arquivo de handoff do projeto certo (ver `HANDOFF-juninho-*`).

### Truque operacional (ambiente)
- **Imagens coladas no chat** (não como link de Drive) ficam no transcript da sessão em
  base64 → dá pra extrair por script e **embutir no PDF via WeasyPrint**. Imagens por
  **link do Google Drive NÃO** funcionam (rede do Google bloqueada no ambiente; PDF/base64
  grande demais para subir pelo conector). Para PDF com fotos: anexar no chat, OU abrir o
  HTML no Chrome → Imprimir → PDF.

---

## 🔴 Backlog / Pendências abertas (por dono)

### 👤 Jonathan (decisões / dados que só ele fecha)
- **K&F — 4 dúvidas abertas:** (1) corrediça telescópica reforçada vs oculta (custo+garantia);
  (2) prateleira despensa M12 = 18 ou 20 mm; (3) **RT da arquiteta Inédita/Flávia — há parceria
  de 10%?** (se não, MC +~4 pts); (4) painel estofado linho M44 = tapeçaria Valvic (markup) ou
  cliente.
- **Louçaria 30 mm (Júnior)** — confirmar se vira regra ou fica caso específico (hoje: caso).
- **Meta de MC oficial** — cravar 43,5% e corrigir os arquivos que ainda dizem 35–40% (ver Furos).
- **Garantia Hardt: 5 ou 10 anos?** (política nova por ferragem vs Termo Gold vigente).
- Prazo de entrega — **validar sempre com Jonathan** antes de cravar (referência ~60 dias úteis).

### 💰 Rodrigo (financeiro) — fonte: `CENTRAL-RODRIGO.md`
- 🔴 **PIPELINE H2/2026 ZERADO** (jul–dez = R$ 0) — emergência; 6 meses × R$ 47k ≈ −R$ 280k.
- 🔴 **Recebíveis em aberto ≈ R$ 330.859** — cobrar Cristiane (79.200), **Andre Alphaville
  (70.800 — não pagou nada)**, Maria (58.869), **Marcelo e Simony (34.850 — não pagou nada)**,
  Augusto (27k), Rejane (21.360).
- 🔴 Levantar com Jonathan: parcelas das dívidas (máquinas + empréstimo do Paulo), composição
  dos R$ 107k (dez/2025) e R$ 101k (jun/2026) → break-even de caixa real.
- 🟠 **Painel HTML financeiro** (Demanda 2, Jonathan 16/06) + integração Google Sheets — em construção.
- 🟠 Recalibrar a régua de MC no app (piso 43%, alvo 48–50%) + **linha de break-even visível
  por orçamento**. Meta 2026 de R$ 3M = inalcançável → recalibrar p/ ~R$ 1,8M.
- 🟡 Reserva de emergência R$ 70k; política de entrada ≥40% em contrato; parar ativo fixo.
- ⚠️ `dados/custo-fixo.md` está **desatualizado** (base 2025) vs DRE jun/2026 do CENTRAL — reconciliar.

### 🤝 Vitor (comercial / proposta)
- 🔴 **Novo layout de proposta** (Jonathan, 16/06): nova linha do tempo visual + links IG/YouTube
  + demais seções a confirmar. **Bloqueado** aguardando specs do Jonathan **e** o **Canva MCP não
  autenticado** nesta sessão.
- 🔴 **MODELO ENXUTO (Canva `DAHMsEfQNas`):** aparar a tabela para 1–2 linhas (ajuste manual único —
  o Canva MCP não adiciona/remove linhas de tabela).
- 🔴 **Documento de garantia:** só o de 10 anos existe; criar variações **2 / 5 / vitalícia** por tier.
- QA de nome único em todas as páginas (histórico de vazar "Vargas Decor"/"Vargas Decor").
- Toda proposta acompanha **mensagem pronta** para o Jonathan enviar ao cliente.
- Fechar **Kênia & Fábio** (P1 do Rodrigo) e conduzir o **Júnior** (âncora "Tudo na cor").

### 📐 Lavinia (método / orçamento)
- 🔴 **Método de quebra do móvel em peças "à mão"** (`quantitativo.md` = "A SER ENSINADO pela Valvic")
  — a habilidade central da skill está **vazia**: folgas, critérios de dimensão, como anota, e a
  **regra de estimativa rápida** (por ambiente/m²/tipo) não estão registradas.
- 🔴 **Júnior:** refinar quantitativo Fase-1 (±25%) com as cotas reais (DET.MARCENARIA pág. 3–46);
  conferir **SKUs/preços Hettich**; rodar a revisão de completude ambiente a ambiente (HANDOFF item 7).
- 🔴 **Custo/m de corte na CNC** (frisos vazados/usinagem) — hoje jogado "na margem operacional" sem número.
- 🟡 K&F: refinar plano de corte com cotas de baixa confiança (M55 ILEGÍVEL, sapateiras/prateleiras
  aproximadas); cotar prateleiras de vidro iluminadas da cristaleira + puxador "sotille".
- 🟡 Lucas e Ana: completar quantitativo dos demais ambientes + fechar regra peças→chapas.

---

## ⚠️ Furos e contradições a resolver (achados na auditoria)

1. **Meta de MC divergente:** SKILL.md + Rodrigo = **~43,5%**; mas `validacao-orcamento.md`,
   `parametros-orcamento.md`, `custos.md`, `metodo-e-missao.md`, `notas-marcos-planilha.md` e o
   **README** dizem **35–40%**. Duas metas convivendo sem reconciliação (auditoria do Rodrigo já
   apontou: o piso antigo está **abaixo do break-even** — "método calibrado para uma empresa que
   não existe").
2. **Preços de chapa em 3+ tabelas incompatíveis** (>2× no mesmo item): ex. Branco 15 mm —
   `chapas.md` (108/110) vs `materiais.json` (260) vs `validacao` (230/250) vs `movel-roupeiro` (220).
   Nomenclatura "branco/cor/especial" vs nomes comerciais não mapeada. **Definir fonte única de preço**
   (`materiais.json` × biblioteca dentro do HTML — os dois se dizem fonte de verdade).
3. **Sistema Dominus:** `ferragens.md` 2p **R$ 1.840** vs `materiais.json` 2p **R$ 700** — provável
   venda vs compra, mas **não está dito** (risco de erro grave). Confirmar Multi (custos `null`).
4. **Fita:** insumo R$ 2–3/m (materiais.json) vs R$ 2,8 (chapas.md) vs "R$ 100/rolo" (validacao);
   buffer **×1,15** (SKILL/laminacao) vs **+10%** (materiais.json/quantitativo). **Filetagem
   R$ 2,50/R$ 4,00 nunca confirmada** na planilha (3 arquivos dizem "a confirmar").
5. **Aproveitamento:** SKILL **0,82** (15/18) vs `quantitativo.md` **0,85**.
6. **NF%:** 7–7,5% (padrão) vs **4%** (versão Camila, "confirmar caso a caso"); parcelamento 7% vs 8%.
7. **Garantia Hardt:** política nova por ferragem = **5 anos** vs Termo Gold vigente = **10 anos**.
8. **Custo fixo:** R$ 67k (base 2025, `dados/custo-fixo.md`) vs R$ 47.219 (DRE jun/2026, CENTRAL) —
   break-even e faturamento base também divergem; só reconciliado no CENTRAL.
9. **Infra do repo:**
   - `install-skills.sh` instala **só** `orcamentista-marcenaria` (ignora `estrategia-financeira-precificacao`
     e `closer-vendas`).
   - `README.md` desatualizado: fala de "Lavinia + Marcos" (hoje é o trio **Lavinia / Rodrigo / Vitor**)
     e repete a meta de MC 35–40%.
   - `descritivo-lavinia.html` (nova) **não documentada** em nenhum guia.
   - Apps legado duplicados: `tabela-de-valores.html` **e** `tabela-valores.html` + `base-materiais` +
     `motor-orcamento` — só `validacao-orcamento.html` é oficial. Arquivar/limpar.
10. **K&F `.md`:** header diz "Fase 2 ✅ ORÇADO" mas "Próximos passos" ainda lista Fase 2 como 🔴 A FAZER
    (o JSON já foi gerado → seção desatualizada).

> Os itens de **preço/margem/garantia** (1–8) são decisões de negócio → Jonathan/Rodrigo.
> Os de **infra** (9–10) a Lavinia pode corrigir (mediante OK).

---

## ✅ Concluído nesta leva (18/06/2026)
- **Júnior — Lagoa Santa:** orçado (395/370), 2 JSONs no app, **proposta em PDF entregue** (layout
  Premium), registro em `projetos/2026-junior-lagoa-santa.md`, handoff aplicado, resumo salvo no Drive.
- **Skill Lavínia** auto-complementada (persona sênior + Trava de Completude + checklists), mantendo
  os valores/regras desta sessão (RT repasse, ripado, porta de passagem etc.).
- **Regras cravadas** promovidas às referências (RT, ripado, porta de passagem, perfil de base).
- Ferramenta `descritivo-lavinia.html` (botão copiar o descritivo da skill).

---

## 📮 Recados rápidos (passageiros — apagar após lidos)

### [16/06/2026] Rodrigo → Lavinia
**CAIXA CRÍTICO.** Piso de exceção: 37%. Ideal: 43%+. Projetos grandes (>R$ 80k): mínimo 40%,
ENTRADA de 40% antes de iniciar produção. Não fechar nenhum projeto sem entrada real. H2 zerado.

### [16/06/2026] Rodrigo → Vitor
**Pipeline H2/2026 zerado — emergência comercial.** P1: fechar Kênia & Fábio (MC ≥ 40%, entrada 40%).
P2: reativar orçamentos parados nos últimos 90 dias. Sem desconto de preço. Cobrar Andre Alphaville
(R$ 70.800) e Marcelo e Simony (R$ 34.850).
