# Contrato de Informação de Produção (Degrau 1)

> **O objetivo é matar a dor #1 da Valvic: retrabalho por informação que chega
> incompleta ou errada à modelagem.** Este é o **portão**: um móvel só segue para
> a modelagem no Marcenária Diferente quando TODOS os campos obrigatórios estão
> preenchidos com dado real (não "assumido"). Onde falta, o agente **pergunta** —
> nunca chuta.

## Regra do portão

- Cada bloco abaixo tem campos **🔴 obrigatórios** e **🟡 condicionais** (só
  obrigatórios se aplicável ao móvel).
- **Status do dossiê:** `COMPLETO` (libera modelagem) · `INCOMPLETO` (lista o que
  falta) · `EM CONFERÊNCIA` (aguardando medida de obra).
- Todo campo "assumido por padrão" deve ser **marcado como suposição** e
  confirmado. Suposição não confirmada = dossiê INCOMPLETO.

---

## Bloco 0 — Identificação 🔴
- Cliente · Ambiente · Código do projeto · Data da conferência · Responsável pela
  medida · Vínculo com o orçamento da Lavinia (versão fechada).

## Bloco 1 — Medida de obra (conferência) 🔴
A medida real, não a do projeto. **A peça é feita sobre a parede que existe.**
- **Vão de cada nicho/parede:** Largura × Altura × Profundidade — medir em **3
  pontos** (topo/meio/base e esquerda/centro/direita) e registrar o **menor**.
- **Prumo e esquadro:** parede fora de prumo? Cantos fora de 90°? Quanto (mm)?
- **Desníveis:** piso e teto nivelados? Diferença ponta a ponta (mm).
- **Pé-direito** e **rodapé existente** (altura/profundidade) que interfiram.
- **Teto:** laje, gesso, sanca? Altura livre real.

## Bloco 2 — Interferências 🔴
O que está na parede e o móvel tem que desviar/acomodar. **Causa clássica de
retrabalho.**
- Tomadas, interruptores, pontos de TV/rede — posição (do piso e da lateral).
- Pontos de **água, gás, esgoto, registro**; quadro de luz/disjuntores.
- **Tubulação/eletroduto aparente**, vigas, pilares, quinas fora de esquadro.
- Janelas/portas/peitoris e o **sentido de abertura** que conflite com o móvel.
- Eletrodomésticos a embutir: medida real **do produto** (cooktop, forno,
  coifa, geladeira, micro-ondas) — marca/modelo + ficha (nicho exigido).

## Bloco 3 — Definição do móvel (escopo) 🔴
- Lista de módulos do ambiente (balcão, aéreo, torre, ilha, roupeiro…).
- Por módulo: nº de **portas** (e tipo: giro / correr / basculante), nº de
  **gavetas**, nº de **prateleiras** (fixas/reguláveis), **nichos** abertos.
- **Iluminação:** LED onde? (perfil, fita, sensor) — ⚠️ friso de LED → Aspire.
- Itens de conforto/acessório (cabideiro, sapateira, lixeira, divisória).

## Bloco 4 — Acabamento por face 🔴
A causa de "cor trocada". **Definir cor/linha por FACE, não só por móvel.**
- Cor + linha + acabamento de cada **face aparente** (frentes, laterais à vista,
  tamponamentos).
- O que é **interno** (padrão branco) × **externo** (cor) — explicitar.
- **Fita de borda:** onde leva (regras em
  `orcamentista-marcenaria/referencias/laminacao-e-construcao.md`), por cor.
- Sentido do veio (amadeirados) quando importa.

## Bloco 5 — Ferragens definidas 🔴
Vêm da especificação (não do nesting). Sem isso, modela-se errado.
- **Corrediça** (linha + comprimento por gaveta), **dobradiça** (reta/curva,
  c/ amortecedor), **sistema de correr** (Dominus/SS150/Multi/RO65 — ver
  `dados/materiais.json`), **pistão/articulador**, **puxador** (tipo, perfil,
  cava usinada × aplicado).
- Quantidades conferíveis pelas regras observadas em
  `orcamentista-marcenaria/referencias/quantitativo.md`.

## Bloco 6 — Especiais / terceirizados 🟡
- Vidro/espelho (tipo, medida), perfil de alumínio, porta de vidro (Renolfh).
- **Friso de LED, friso de dobra de MDF (V-groove), corte curvo → Aspire**
  (Degrau 4): registrar parâmetros (largura, profundidade, ângulo, raio).
- Laca/pintura, serralheria, veludo — confirmar custo/terceirizado por projeto.

## Bloco 7 — Montagem e logística 🟡
- Acesso à obra (elevador, escada, medida da porta de entrada — peça grande passa?).
- Sequência/ordem de montagem desejada; prazo; data de entrega.

---

## Saída do Degrau 1

Um **dossiê de produção** com status `COMPLETO`/`INCOMPLETO`. Se INCOMPLETO, o
agente devolve a **lista exata do que falta** — para o vendedor/medidor buscar a
informação **antes** de a chapa ser cortada, e não depois.

> **A calibrar com um caso real:** ao receber 1 conferência de obra vivida +
> o que deu retrabalho nela, extrair quais campos faltaram e **promover** esses
> campos a obrigatórios. É assim que o contrato aprende a pegar o erro da Valvic.
