# Que formato usar, e como cada um se estrutura

Escolher errado o formato é o erro mais caro da Academy: uma política escrita como aula não
obriga ninguém, e um POP escrito como política não ensina ninguém a executar.

## A escolha

| Se a necessidade é… | O formato é | Tamanho típico |
|---|---|---|
| Ensinar um assunto do ofício | **Aula / módulo de apostila** | 2 a 6 páginas A4 |
| Padronizar como se executa uma tarefa | **POP** | 1 a 2 páginas A4 |
| Definir uma regra de conduta ou obrigação | **Política interna** | 1 a 3 páginas A4 |
| Mostrar o caminho de crescimento de um cargo | **Trilha de formação** | 2 a 4 páginas A4 |
| Lembrar na hora de fazer | **Guia rápido de parede** | 1 página A4 ou A3 |
| Conferir se foi feito | **Checklist** | 1 página, com coluna de marcar |
| Verificar se a pessoa aprendeu | **Avaliação / prova prática** | 1 página |
| Integrar quem entrou hoje | **Kit de integração** | conjunto de peças |
| Gravar em vídeo | **Roteiro de vídeo** | 1 a 2 páginas |

## Estruturas

### Aula / módulo
Ver a estrutura de 7 blocos em `metodo-didatico.md`. Modelo pronto:
`ferramentas/modelo-aula-a4.html`.

Uma apostila é um conjunto de módulos com capa, sumário e numeração — não um texto corrido
gigante. Módulo que cabe numa sessão de 20 minutos é módulo que a pessoa termina.

### POP
Ver `pop-e-processo.md`. Modelo: `ferramentas/modelo-pop-a4.html`.

### Política interna
Ver `politicas-internas.md`.

### Trilha de formação
Ver `trilhas-e-avaliacao.md`. O modelo da casa já existe e funciona:
`painel/trilha-formacao-marceneiro.html`.

### Guia rápido de parede
Uma folha, para ficar colada na máquina ou na bancada. Regras:
- **Um assunto.** "Como regular a coladeira", não "cuidados com máquinas".
- **Passo numerado, frase de no máximo uma linha.**
- **Fonte grande** — vai ser lido a um metro, com a máquina ligada.
- **O que NÃO fazer**, em vermelho, no máximo três itens.
- **Quem chamar** se não resolver.

### Checklist
- **Uma linha = uma ação verificável.** "Conferir cor da chapa contra o pedido" é
  verificável; "atenção ao material" não é.
- **Coluna para marcar**, sempre. Checklist sem lugar de riscar é lembrete.
- **Quem confere e quando** no cabeçalho.
- Se houver item crítico, marque-o — mas não mais que dois ou três, senão todos viram
  críticos e nenhum é.

### Avaliação
Três tipos, em ordem de valor:
1. **Prática** — "monte esta gaveta e regule a porta". É a que a Valvic usa na trilha e é
   a que vale. A régua é o que a pessoa sabe fazer.
2. **Situação** — "chegou chapa na cor errada e a montagem é amanhã. O que você faz?"
   Testa julgamento, não memória.
3. **Objetiva** — múltipla escolha. Serve para verificar leitura, não competência. Use
   pouco, e nunca sozinha.

Evite pergunta de decorar número que a pessoa pode consultar. O que importa é saber **que
existe o critério** e **onde encontrar**.

### Roteiro de vídeo
```
Título · Duração alvo · Quem grava · O que precisa estar em cena
[00:00] Gancho — o erro ou o resultado, em 10 segundos
[00:10] O que você vai aprender
[00:20] Passo a passo — uma ação por bloco, com o que a câmera mostra
[--:--] Erro comum — mostrar o errado e o certo lado a lado
[--:--] Como conferir
[--:--] Fechamento — a frase que fica
```
Vídeo de fábrica funciona melhor em 2 a 4 minutos, gravado no local real, com barulho de
oficina mesmo. Produção demais afasta.

## Produzir o arquivo

1. Copiar `ferramentas/modelo-aula-a4.html` ou `ferramentas/modelo-pop-a4.html`
2. Escrever o conteúdo
3. `python3 ferramentas/gerar-pdf.py painel/arquivo.html` — tem de dar `over_sheet: 0`
4. Salvar o HTML em `painel/` (nome minúsculo com hífen) e o PDF ao lado
   (`Valvic_Nome_Do_Doc.pdf`)

Se o conteúdo estourou a página: **reduza o preenchimento das caixas e encurte o texto** —
nunca diminua a fonte. Material de fábrica ilegível não é material.

## Nomenclatura da Academy

- Aula ou módulo: `academy-modulo-01-substratos.html`
- POP: `pop-conferencia-de-peca.html`
- Política: `politica-uso-de-ferramentas.html`
- Trilha: `trilha-formacao-<cargo>.html`
- Guia de parede: `guia-parede-<assunto>.html`

O prefixo faz o `ls painel/` já mostrar o acervo agrupado.
