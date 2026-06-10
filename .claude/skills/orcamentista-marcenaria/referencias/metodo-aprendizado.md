# Como Marcos aprende: cruzar método manual × saída exata

Estratégia de calibração definida pelo fundador para tornar o orçamento
**rápido E exato**.

## As duas realidades a mesclar

1. **O jeito que o Jonathan aprendeu** (marcenaria tradicional, manual): olhar o
   móvel e estimar o quantitativo — a lógica de raciocínio para orçar
   (`metodo-e-missao.md`, `movel-roupeiro.md`, `laminacao-e-construcao.md`).
2. **Como sai na ponta, com exatidão:** o software de produção **"Marcenária
   Diferente"** programa o projeto para o router e dá **tudo exato** — lista de
   material e plano de corte completos.

> **Missão de Marcos:** mesclar as duas para **otimizar a produção de orçamento**
> — estimar em minutos, com precisão próxima da do software, sem modelar cada
> cotação no 3D.

## Material de treino que o fundador vai enviar

Por projeto (1–2 por vez), uma pasta com:

- **Render com as portas fechadas** → leitura externa (dimensões, nº de portas,
  acabamento aparente).
- **Render sem as portas** → estrutura interna (caixaria, gaveteiro, prateleiras,
  divisões) — as peças reais.
- **Lista de material completa** → ground truth de chapas, fita, ferragens,
  acessórios, serviços.
- **Plano de corte completo** → peças (C×L×qtd), nº de chapas, aproveitamento,
  filetamento.

## O que Marcos faz com cada projeto de treino

1. **Decompor pelo método manual** o móvel a partir dos renders (estimar peças,
   chapas, fita pelas regras de `laminacao-e-construcao.md`).
2. **Comparar** com a lista de material + plano de corte reais.
3. **Medir o erro** (chapas, metros de fita, ferragens) e **extrair regras de
   calibração** (ex.: fator de aproveitamento por tipo de peça, fita real por
   gaveta/porta, parafusos/cola por módulo).
4. **Registrar a regra** calibrada em `quantitativo.md` e nos móveis-padrão.

> Os projetos de treino e a calibração ficam em `projetos/treino/`.
