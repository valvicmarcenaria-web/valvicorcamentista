# POP — procedimento que a fábrica cumpre

POP é **Procedimento Operacional Padrão**: como se executa uma tarefa, do jeito Valvic, de
forma que qualquer pessoa treinada faça igual. Na arquitetura do "Valvic OS" é o **Doc 12**,
e é a peça que mais falta hoje.

## O teste do bom POP

> **Alguém que nunca fez consegue executar lendo, com o material na mão?**

Se a resposta for não, falta passo. Se a resposta for "só se alguém explicar junto", não é
POP — é anotação.

E o segundo teste, que a maioria dos POPs falha:

> **Se der errado no meio, o documento diz o que fazer?**

Procedimento que só descreve o caminho feliz não sobrevive à primeira quinta-feira.

## Estrutura

```
IDENTIFICAÇÃO      nome · código · versão · data · quem escreveu · quem aprovou
QUANDO SE APLICA   a situação exata que dispara este procedimento — e quando NÃO se aplica
QUEM EXECUTA       o cargo, não a pessoa
O QUE PRECISA      material, ferramenta, documento, informação — tudo antes de começar
PASSO A PASSO      numerado, uma ação por passo, verbo no imperativo
PONTOS DE CONFERÊNCIA   onde se para e se verifica, com o critério de "está certo"
SE DER ERRADO      o desvio mais provável e o que fazer — inclusive a quem recorrer
REGISTRO           o que fica escrito e onde
```

## Como escrever cada parte

**Quando se aplica.** Seja específico, e diga também o que fica de fora. "Recebimento de
chapa e ferragem de fornecedor" — não "recebimento de material", que abre discussão sobre
se vale para o carreto que trouxe peça de volta da obra.

**Passo a passo.** Uma ação por passo, verbo no imperativo, sem "deve-se" nem "é
recomendável". O passo tem que caber numa linha ou duas.

> ❌ *"Deve-se proceder à verificação da conformidade cromática do material."*
> ✅ *"3. Confira a cor da chapa contra o pedido. Cor errada = não descarregue."*

Quando o passo tem um número que importa, ele fica **no passo**, não numa observação lá
embaixo: *"Aperte o parafuso a 32 mm da borda"*.

**Pontos de conferência.** É aqui que o POP vira ferramenta de qualidade. Cada ponto precisa
de um **critério observável**:

> ❌ *"Conferir se o acabamento está bom."*
> ✅ *"Passe o dedo na borda: não pode haver ressalto nem filete de cola. Se pegar na unha,
> volta para a lixa."*

**Se der errado.** O bloco mais valioso e o mais esquecido. Liste os dois ou três desvios
mais prováveis, o que fazer em cada um, e **quem acionar**. É isso que evita a pessoa
improvisar sozinha ou parar e esperar.

## Os POPs que a Valvic precisa

Do fluxo declarado, cada etapa merece um. Em ordem de dor — a lista vem do gargalo real da
casa, que é retrabalho por informação faltando:

| Prioridade | POP | Por que |
|---|---|---|
| 1 | **Conferência de peça antes de sair da fábrica** | A ficha já existe; falta o procedimento. É o filtro que evita erro chegar na obra |
| 2 | **Recebimento de material** | Chapa na cor errada aceita no descarregamento vira prejuízo sem recurso |
| 3 | **Medição do ambiente** | Medida errada contamina tudo o que vem depois |
| 4 | **Conferência de programação (pré-CNC)** | Erro aqui gasta chapa, máquina, filetagem e montagem antes de aparecer |
| 5 | **Filetagem e acabamento de borda** | O gargalo conhecido: a coladeira não finaliza 100% e exige acabamento manual |
| 6 | **Montagem em obra** | Conduta no cliente + sequência de montagem |
| 7 | **Carga e transporte** | O que sobe no caminhão, como se protege, o que se confere |
| 8 | **Entrega e vistoria** | O aceite do cliente |

Antes de escrever qualquer um: **veja o que já existe**. Várias fichas e checklists estão
prontos em `painel/` (`ficha-conferencia-producao.html`, `ficha-recebimento-material.html`,
`ficha-medicao.html`, `matriz-conferencia.html`) — o POP é o texto que diz *como usar a
ficha*, não um documento paralelo que a contradiga.

## POP e treinamento andam juntos

Um POP publicado e nunca treinado não muda nada. Toda entrega de POP fecha com:
1. **Quem precisa conhecer** — os cargos.
2. **Como será apresentado** — 10 minutos na reunião da manhã, ou uma aula, ou a folha
   colada na parede.
3. **Como se verifica** — a primeira execução acompanhada, ou o checklist assinado.

## Versão e manutenção

Todo POP nasce com **versão e data**. Quando muda, muda o número da versão e diz o que
mudou, em uma linha. Sem isso, em seis meses existem três versões impressas circulando na
fábrica e ninguém sabe qual vale — que é exatamente o problema que o POP veio resolver.
