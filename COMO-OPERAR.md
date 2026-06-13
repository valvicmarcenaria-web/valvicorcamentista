# Como operar a Lavinia (runbook — operação solo no Claude)

Guia rápido para usar a Lavinia (Orçamentista Estratégico) no dia a dia, dentro
do Claude Code (web). Operação **solo**, **privada**, **sem servidor**.

## Princípio
A skill mora em `.claude/skills/orcamentista-marcenaria/` **dentro deste repo**.
Logo: **toda sessão aberta neste repositório já vem com a Lavinia pronta** —
conhecimento, base de preços (`dados/materiais.json`) e histórico de projetos.

## Ritual de uma cotação (passo a passo)

1. **Abrir sessão** do Claude Code neste repo (`valvicorcamentista`).
2. **Mandar o projeto** — PDF executivo, render, foto ou descrição do móvel.
3. **Lavinia lê (Fase 1)** → levanta o quantitativo (chapas por cor/espessura,
   fita, ferragens, LED, terceirizados). Confirma medidas/dúvidas com você.
4. **Precifica (Fase 2)** → custo de material pela base + fechamento por MC%.
   Lavinia **pergunta a situação de caixa** (define a MC mínima).
5. **Estratégia (Fase 3)** → se houver ponto caro, propõe versão enxuta; se for
   pacote, aloca por peça; monta a proposta.
6. **Salvar:**
   - Registrar o orçamento no projeto (`projetos/<ano>-<cliente>.md`).
   - Exportar o JSON do app e subir no Drive (`Orçamentos Valvic / Em aberto /
     <cliente> / Versão N`).
   - **Commit + push** (o container é efêmero — sem push, perde-se).

## App de orçamento (privado)
- Arquivo: `ferramentas/validacao-orcamento.html`.
- **Uso solo:** guardar o HTML no seu PC/celular e abrir no navegador (funciona
  offline; salva no próprio navegador). **Não publicar** em link público — o app
  contém a base de preços e a fórmula de margem (exporia custo/markup).
- Pedir a versão atualizada à Lavinia sempre que a base/ferramenta evoluir.

## Higiene da operação
- **Fonte única de verdade:** `dados/materiais.json` (preços de compra). Atualizar
  num lugar só; o app importa.
- **Sempre commitar** ao fim da sessão (base, projetos, app).
- **Fornecedores:** preço novo (ex.: porta de vidro Renolfh) → gravar no projeto
  e no `materiais.json` como referência.

## Quando escalar (sinais para revisitar)
- Volume alto/recorrente → considerar o **subagente de lote** (orçar vários
  ambientes/projetos em paralelo).
- Mais de um operador → padronizar instalação da skill e a base compartilhada.

> Operação atual: **solo, dentro do Claude**, privada. Simples de propósito.
