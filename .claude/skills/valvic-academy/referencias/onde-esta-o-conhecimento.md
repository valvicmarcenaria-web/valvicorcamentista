# O mapa do conhecimento da Valvic

**Ler antes de escrever qualquer coisa.** O conteúdo da Academy sai daqui — não da teoria
geral de marcenaria. Material genérico não ensina o jeito Valvic de fazer, e é exatamente o
jeito Valvic que precisa sair da cabeça das pessoas e virar documento.

**Repositório:** `~/valvicorcamentista`
Se não estiver aí: `find ~ -name "apostila-escopos-funcao.html" 2>/dev/null`

---

## 1 · O acervo técnico mais fundo da casa

Está na skill da **Lavinia** (orçamentista). É a melhor fonte de conteúdo técnico que
existe no repositório — foi escrita para orçar, mas descreve material, construção e
ferragem com profundidade de quem faz.

`.claude/skills/orcamentista-marcenaria/referencias/`

| Arquivo | O que ensina |
|---|---|
| `chapas.md` | Substratos, espessuras, cores, rendimento de chapa |
| `ferragens.md` | Corrediças, dobradiças, articuladores, o que é homologado na casa |
| `laminacao-e-construcao.md` | Laminação, construção do móvel, o que define o padrão premium |
| `roupeiros.md` · `movel-roupeiro.md` | O móvel mais complexo da casa, detalhado |
| `quantitativo.md` | Como se levanta o que um móvel consome |
| `custos.md` · `otimizacao-custos.md` | O custo por trás de cada escolha técnica |
| `processo-orcamento.md` · `estrutura-orcamento.md` | O processo comercial-técnico |
| `parametros-orcamento.md` · `validacao-orcamento.md` | Os parâmetros e a conferência |
| `logistica.md` | Transporte e montagem |
| `posicionamento.md` · `metodo-e-missao.md` | Por que a Valvic faz do jeito que faz |
| `metodo-aprendizado.md` | Como a Lavinia aprende — útil para desenhar avaliação |
| `notas-marcos-planilha.md` | Notas de campo sobre a planilha de orçamento |

E os **projetos reais** em `projetos/` — casos completos que valem ouro como estudo de caso
numa aula (`2026-kenia-e-fabio-casa-completa.md`, `2025-lucas-e-ana-apto101.md`, e a pasta
`treino/` com calibrações).

> Regra: o Lucas **usa** esse acervo para ensinar. Se a dúvida for de número ou de spec para
> precificar, a bola é da Lavinia.

---

## 2 · O fluxo de produção e a linguagem da fábrica

`.claude/skills/gestao-estrategica-operacional/referencias/vivencia-marcenaria.md`

Traz o **fluxo de 10 etapas** (medição → projeto → compra → corte → coladeira/filetagem →
furação → laminação → montagem → expedição/montagem → pós-venda), o **vocabulário
essencial** e — o mais valioso para a Academy — **onde estão os gargalos reais**: a coladeira
SCM ME25 que não finaliza 100% e exige acabamento manual, o retrabalho de acabamento, a falta
de material provisionado.

`.claude/skills/gestao-estrategica-operacional/referencias/mapa-fluxo-e-documentos.md` —
o fluxo ponta a ponta com o registro de **quais documentos e POPs existem × quais faltam**.
É o inventário de buracos da padronização.

---

## 3 · A base absorvida do Google Drive

`.claude/skills/gestao-estrategica-operacional/dados/valvic-conhecimento-drive.md`

O arquivo mais denso de contexto histórico. Seções que interessam à Academy:

- **§6 Academy & estágio** — o **Guia Técnico Módulo I** (substratos: MDF caixa 18 mm,
  fundos 9/15 mm · acabamentos: BP, lâmina, laca, fita PVC/ABS · ferragens: Hardt, Häfele,
  Hettich, Rometal, com corrediça oculta soft-close como **padrão Gold, parte da garantia de
  10 anos** · glossário). O **Módulo II previsto**: leitura de projeto, cotas, montagem. E o
  **Plano de Estágio** (Analista de Projetos / Suporte Comercial).
- **§7 Produção** — o fluxo declarado, a linha **Gold** (a Basic foi descontinuada), os
  padrões de caixa e fundo, e a lista dos **apps já construídos** que operam etapas como
  checklist digital.
- **§8 "Valvic OS"** — a arquitetura de ~15 documentos. **POPs são o Doc 12; a Academy é o
  Doc 13.** E o **gargalo-raiz** declarado, que é a razão de existir de tudo isto.
- **§5 Gestão de pessoas** — matriz de decisão do Deivison, reconhecimento de R$ 200/mês por
  conquista, e a regra cultural: *ninguém avança de nível sem ter ensinado algo ao nível
  abaixo*.
- **§9 História & cultura** — inclusive o acidente do RJ, que é material real para uma aula
  de segurança em transporte.

---

## 4 · O que a empresa já publicou — a pasta `painel/`

58 documentos em HTML, cada um com PDF ao lado. Os que mais servem à Academy:

### Formação e cargos
| Arquivo | O que é |
|---|---|
| `trilha-formacao-marceneiro.html` | **A trilha de Ajudante a Marceneiro** — o modelo de trilha da casa: 4 etapas, avaliação a cada 3 meses, incremento salarial por validação, régua pelo que sabe fazer e não pelo tempo de casa. **Copiar essa lógica ao criar trilha de outro cargo** |
| `apostila-escopos-funcao.html` | Escopo e critério de avaliação de **cada cargo** (10 blocos) |
| `escopo-marceneiro.html` · `escopo-ajudante-marcenaria.html` · `escopo-arquiteta-engenharia-produto.html` · `escopo-de-venda.html` | Escopos detalhados por função |
| `proposta-contratacao-marceneiro-pleno.html` | O perfil que a casa busca |

### Processo e qualidade — a matéria-prima dos POPs
| Arquivo | O que é |
|---|---|
| `ficha-conferencia-producao.html` | Conferência de peça antes de sair da fábrica |
| `ficha-recebimento-material.html` | Conferência de material recebido do fornecedor |
| `ficha-medicao.html` | Medição do ambiente |
| `matriz-conferencia.html` | A matriz de conferência |
| `checklist-insumos-ferramentas.html` | Insumos e ferramentas |
| `kit-montador-relatorios.html` | O kit e os relatórios do montador |
| `ocorrencia-reparo-maria-valdenir.html` | Registro de ocorrência — modelo real |
| `painel-producao-a3.html` | O painel semanal de produção |

### Conduta, feedback e casos reais — ouro para aula
| Arquivo | Por que serve |
|---|---|
| `feedback-deivison-obra.html` | **21 erros reais** de uma cozinha, classificados. Cada um é um exemplo concreto para aula de acabamento |
| `feedback-samuel-obra.html` | **16 pontos** de uma obra, por ambiente. Mostra o que é falta de preparo × falta de técnica |
| `advertencia-jomar.html` | Caso disciplinar real |
| `controle-veiculos-termo*.html` · `controle-veiculos-ficha-*.html` | Termos e fichas de veículo, com a base legal por vínculo |
| `folha-cobranca-karla.html` | Como a casa cobra rotina |

> Os dois documentos de feedback são a melhor fonte de **erro real** que existe aqui. Aula
> de acabamento feita em cima de erro que aconteceu de verdade nesta fábrica ensina muito
> mais que teoria — e a equipe reconhece o caso.

### Marca, produto e comercial
`escopo-de-venda.html` · `vaga-*-story.html` (o tom da marca em peça visual) ·
`caderno-empresarial-valvic.html` (o documento-mãe de 30 páginas, **restrito**).

### Estrutura e infraestrutura
`layout-fase1-galpao-atual.html` (o layout da fábrica — útil para aula de fluxo e
organização) · `patrimonio-valvic-2026.html` (o parque de máquinas).

### Financeiro e investidor — **restritos**
Todos os `walton-*.html`, `custos-*`, `estrutura-*`, `memoria-custos-*`,
`modelo-economico-investidor.html`, `parcelamentos-*`, `contas-receber-pagar-*`. Contêm
remuneração nominal e dado de investidor. **Não viram material de aula** e não se citam em
documento que circula na fábrica.

### Índice
`painel/index.html` — a página-índice. E o inventário comentado, documento a documento, em
`.claude/skills/gestao-estrategica-operacional/dados/mapa-documentos.md` — **esse arquivo
descreve o que tem dentro de cada documento**, e é a forma mais rápida de achar a fonte certa.

---

## 5 · Identidade, valor e garantia — a base do conteúdo institucional

`.claude/skills/closer-vendas/referencias/`

| Arquivo | O que tem |
|---|---|
| `identidade-marca.md` | Paleta, tipografia, tom visual, estrutura da proposta-mestre |
| `valor-do-produto.md` | **Por que o produto Valvic vale o que vale** — a fonte de qualquer aula sobre padrão de qualidade |
| `garantia.md` | O Termo de Garantia Gold — o que a empresa promete e por quanto tempo |
| `objecoes.md` · `metodo-vendas.md` | Base para o conteúdo de formação comercial |

Uma aula de acabamento fica muito mais forte quando começa por *"a garantia é de 10 anos,
e é por isso que a corrediça é essa e não outra"*.

---

## 6 · O Moleskine — o caderno vivo

`MOLESKINE.md`, na raiz do repositório.

É onde os agentes e o Jonathan deixam recado entre sessões: **tarefas abertas, decisões,
bases de dados atualizadas e correções**. Formato livre, com data e agente responsável.

Para a Academy ele serve de três formas:
1. **Saber o que está em aberto** antes de propor conteúdo novo.
2. **Achar decisões e números atualizados** que ainda não entraram em documento formal.
3. **Deixar registrado** o que a Academy produziu e o que ficou pendente — quando o Lucas
   terminar algo relevante ou identificar um buraco, ele **anota no Moleskine**, com data,
   para a próxima sessão encontrar.

O método de trabalho com ele está em
`.claude/skills/gestao-estrategica-operacional/referencias/caderno-moleskine.md`.

---

## 7 · Guias de operação na raiz

| Arquivo | O que é |
|---|---|
| `GUIA-APPS-E-FERRAMENTAS.md` | Os apps e ferramentas da casa — cada um deveria ter POP e aula |
| `GUIA-ORCAMENTOS.md` | O guia de orçamento |
| `COMO-OPERAR.md` | Como operar o repositório e as skills |
| `README.md` | Visão geral |

---

## 8 · O ERP e as ferramentas — conteúdo de treinamento administrativo

`.claude/skills/gestao-estrategica-operacional/referencias/sistema-calcme.md` — módulos e
rotinas do ERP Calcme. É a base de qualquer treinamento de sistema.
Na mesma pasta: `operacoes-drive.md`, `planilhas-e-relatorios.md`,
`rotinas-cadencia.md` e `gestao-equipe.md`.

E o dia a dia administrativo já escrito, na skill da Alice:
`.claude/skills/alice-assistente-operacional/referencias/` — atendimento, compras,
financeiro operacional, produção, RH. Serve de base para o material de integração do
administrativo.

---

## Como buscar rápido

```bash
# procurar um assunto em tudo que é texto
grep -ril "coladeira" --include="*.md" --include="*.html" .

# ver o que um documento do painel diz, sem o HTML
python3 -c "
import re,html,sys
s=open(sys.argv[1],encoding='utf-8').read()
t=re.sub(r'<(style|script).*?</\1>','',s,flags=re.S)
t=re.sub(r'<[^>]+>','\n',t)
print('\n'.join(l.strip() for l in html.unescape(t).split('\n') if l.strip()))
" painel/trilha-formacao-marceneiro.html

# inventário comentado de todos os documentos
less .claude/skills/gestao-estrategica-operacional/dados/mapa-documentos.md
```

## Quando não achar

Não invente. Pergunte — e pergunte **bem**: o Jonathan e o Paulo têm o conhecimento, mas
não têm tempo de escrever. O jeito de extrair está em `metodo-didatico.md`, seção
"Extrair o que está na cabeça".
