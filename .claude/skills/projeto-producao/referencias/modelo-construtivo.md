# Modelo Construtivo da Valvic (Degrau 2 — em construção)

> Como o móvel Valvic vira **peças de MDF**. É o conhecimento que, destilado,
> permitirá à skill traduzir **medida de obra → lista de peças** (Degrau 3).
> **Não duplicar** o que já existe em `orcamentista-marcenaria` — referenciar e
> estender com o olhar de *produção* (folgas, encaixes, furação).

## Já destilado (na skill de orçamento — herdar)
- **Taxonomia de peças** `Função-Grupo-Módulo` e regras de espessura por peça:
  `orcamentista-marcenaria/referencias/quantitativo.md`.
- **Chapas / espessuras padrão** (estrutura 15mm · fundos 6mm · porta de correr
  18mm · prateleira de roupeiro >70cm 18mm): `.../chapas.md`.
- **Fita por face / filetagem / gaveta de 6 peças / ripado:**
  `.../laminacao-e-construcao.md`.
- **Rasgo de fundo por encaixe** (não parafusado) — confirmado nos planos de corte
  reais (modelo maior luiz: 43 m de rasgo).

## A destilar com casos reais (o que falta para MODELAR)
- **Folgas e tolerâncias:** vão de obra → medida da peça (folga de porta, de
  gaveta, recuo de fundo, junta entre módulos, ajuste para parede fora de prumo).
- **Modulação:** quando quebrar um vão grande em mais de um módulo (limite de
  chapa 2750×1850, transporte, montagem).
- **Furação e marcação:** padrão de furos (dobradiça, prateleira regulável,
  Minifix/cavilha) — base para o DXF do router.
- **Passante × apoiado:** quando a base/lateral é passante (visto nos planos:
  "Base (passante)").

> **Método de aprendizado** (igual ao da Lavinia): pegar projeto real do MD
> (lista + plano de corte + DXF + medida de obra), reconstruir a lógica peça a
> peça e registrar a regra aqui. Fonte de treino: pasta Drive "modelo maior/menor".
