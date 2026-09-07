# Ilustrações técnicas da Academy

SVG vetorial, escrito à mão, sem dependência de biblioteca. Escala sem perder, imprime limpo
e se corrige quando a medida mudar — que é o que foto de catálogo não faz.

## Convenções do desenho Valvic

Fixadas em setembro/2026 a partir da referência aprovada pelo Jonathan.

| Elemento | Como se desenha | Por quê |
|---|---|---|
| **Fundo** | **Branco, sempre** — nos dois temas e na impressão. Grade técnica a 16 px, opacidade 0,07 | Ar de prancheta sem disputar com o traço |
| **Madeira** | Bege `#ECE0C8`, contorno `#A89A78` | É MDF: quente e neutro |
| **Ferragem** | Cinza-metal `#6E737A`, contorno `#3F444B` | Lê como aço. **Dourado sobre bege embaralha** — duas cores quentes de valor parecido |
| **Peça vizinha** | Bege claro `#F6F1E6`, contorno tracejado `#C4B998` | É contexto: existe, não é o assunto |
| **Cota e alerta** | Vermelho `#B0413F`, linha fina, seta nas duas pontas, chamada tracejada | Só onde a medida é obrigação |
| **Confirmação** | Verde `#2F7D4F` | Para o que está certo. Nunca decorativo |
| **Rótulo** | **Dentro da peça**, girado −90° nas verticais | Dispensa legenda — é o que a referência faz |
| **Detalhe** | Moldura circular isolando a peça | Um círculo por coluna, nunca mais |
| **Divisória** | Filete `#D8D2C4` entre colunas | Separa sem pesar |

Tipografia: Inter para rótulo e legenda, JetBrains Mono para cota e medida.
Nada de texto explicativo dentro do desenho — isso é da legenda.

> **O dourado da marca não entra no desenho técnico.** Ele segue no texto, nos títulos e nas
> caixas, onde funciona. Dentro do desenho, ferragem é cinza-metal.

## Arquivos

| Arquivo | Figura | O que mostra |
|---|---|---|
| `fig-1-3-dobradicas-reta-curva-supercurva.svg` | **1.3** | Três colunas: esquema do canto (lateral, dobradiça e porta rotuladas por dentro) com a cota de quanto da lateral a porta cobre — 18 / 9 / 0 mm — e o perfil de cada dobradiça em moldura circular, com o braço cada vez mais desviado |
| `fig-2-5-corredica-telescopica-x-oculta.svg` | **2.5** | Corte frontal: a telescópica com os 13 mm do corpo entre a caixa e a lateral; a oculta sob o fundo, lateral limpa, folga dependente do modelo |
| `fig-3-1-pistao-comum-x-forca-inversa.svg` | **3.1** | O comum empurrando a porta que abre para cima; o de força inversa segurando a que abre para baixo |

Base técnica de todas: `referencias/pesquisa-ferragens.md`.

## Como usar

Cole o conteúdo do `.svg` direto no HTML da aula (o `viewBox` já escala), ou referencie como
imagem. No modelo A4 a figura ocupa a largura inteira do texto — **171 mm** — conforme o
`plano-editorial.md`.

## Como criar uma nova

1. Leia a convenção acima e siga à risca. Desenho fora do padrão custa mais caro que desenho
   nenhum: quebra a leitura de todo o volume.
2. `viewBox` proporcional ao espaço da apostila. Largura 640 dá boa resolução de traço.
3. **Três leituras sempre que couber:** o corte, a cota que explica e a peça isolada.
4. Rótulo dentro da peça; explicação na legenda, fora do desenho.
5. `role="img"` e `aria-label` descrevendo o que a figura mostra — a versão digital é lida por
   quem não enxerga o desenho.
