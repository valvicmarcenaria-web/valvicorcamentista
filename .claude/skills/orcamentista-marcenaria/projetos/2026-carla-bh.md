# CARLA · BH 2026 — apartamento completo

**Cliente:** Carla · **Local:** Belo Horizonte
**Pasta:** `drive.google.com/drive/folders/1E7MrtwTS3YEuHt9m_-ti8WA54jvkpr87`
**Levantamento:** Lavinia, 24/08/2026 · `projetos/corte-carla.py`
**Entregável:** `projetos/proposta-carla.pdf` — 9 páginas

---

## ⭐ O melhor insumo que a casa já recebeu

As sete pranchas são **caso A** (têm camada de texto, lidas pelo conector) **e
trazem QUADRO DE PEÇAS** — código, quantidade, espessura e dimensão de cada
peça, com memorial de materiais e ferragens.

> **O levantamento foi transcrição, não interpretação.** Não medi nada em pixel,
> não arredondei por metro quadrado, não chutei modulação. Comparar com a
> Luciana (só larguras, sem coordenadas) e com o Carol e Vinícius (texto em
> curvas, leitura visual) mostra o salto.

Onde a prancha escreve "preliminar", ela avisa que as cotas de **corte** ainda
descontam folga e ferragem — as cotas de **projeto** estão fechadas.

| Prancha | Conteúdo |
|---|---|
| `ARQ_CARLA BH_2026_LAYOUT_V01` | layout — cozinha · sala · 2 banhos · suíte · 2 quartos |
| `Detalhamento_Cozinha` | cozinha linear 3890 com torre de geladeira |
| `Detalhamento_Painel` | painel amadeirado 6570 × 2450 com porta integrada |
| `Detalhamento_Rack` | rack suspenso 3580 × 400, 4 básculas |
| `Detalhamento_Cristaleira` | cristaleira 920 × 400 × 2450 |
| `Detalhamento_Guarda roupa 3P` | roupeiro 2550 × 640 × 2680, 3 folhas de correr |
| `Detalhamento_Guarda roupa L` | roupeiro em L 1970 + retorno com cabeceira |
| `Detalhamento_Escada` | marcenaria sob escada 2390 × 400 — **duplicado na pasta** |

⚠ **A pasta contém `contrato_eliuton-compactado.pdf`** — contrato de OUTRO
cliente. Ignorei, mas vale avisar: pasta de cliente com contrato de terceiro é
risco de vazamento.

---

## Decisões do Jonathan · 24/08

1. **COM RT** de 10 %.
2. **Ferragem Hettich** — uma linha só, MC 38 %, garantia de 10 anos.
3. **Interno em Branco TX onde pertinente** + **upgrade de tudo na cor**.

---

## Números

| | |
|---|---|
| Área de chapa | **132,94 m²** |
| Chapas | 37 (aproveitamento médio 71 %) |
| Fita de borda | 345,65 m |
| Cava e frisos usinados | 57,12 m |
| LED | 16,56 m |
| Ferragem | 46 dobradiças Novisys · 13 corrediças Quadro · 4 Blum HK-xs |
| Custo direto | **R$ 36.379** |

### Preço

| | |
|---|--:|
| **Investimento (interior branco)** | **R$ 109.300** |
| + Upgrade · tudo na cor | + R$ 18.500 |
| **Com o upgrade** | **R$ 127.800** |
| *sem RT, referência interna* | *R$ 86.400 · MC 38,0 %* |

**Sanidade:** R$/m² de chapa **650 sem RT** — dentro da faixa da casa
(626 Rizzi · 647 · 739 SPE · 834 Honda · 624 Eliuton). Com RT sobe para 822, o
que é esperado: RT é comissão, não material.

### Por ambiente

| Conjunto | Chapa | Investimento |
|---|--:|--:|
| Cozinha linear com torre de geladeira | 27,05 m² | 22.200 |
| Painel amadeirado até o forro | 18,85 m² | 15.500 |
| Rack suspenso de 3,58 m | 6,29 m² | 5.200 |
| Cristaleira até o forro | 5,94 m² | 4.900 |
| Guarda-roupa de três portas de correr | 33,46 m² | 27.500 |
| Guarda-roupa em L com cabeceira | 31,45 m² | 25.900 |
| Marcenaria sob a escada | 9,91 m² | 8.100 |
| **TOTAL** | **132,94 m²** | **109.300** |

---

## O upgrade de tudo na cor

Mesmo mecanismo do Carol e Vinícius: a caixaria interna é lançada como
`I:AM` / `I:PT` / `I:OW` e resolve para Branco TX ou para a cor do próprio
módulo. **Integral** — caixaria, prateleiras, fundos e caixa de gaveta.

| | Branco TX | Tudo na cor |
|---|--:|--:|
| Chapa | 37 ch. · R$ 14.910 | 39 ch. · R$ 20.700 |

São **85,5 m²** de interior. Aqui o upgrade **acrescenta duas chapas** — ao
contrário do Carol e Vinícius, onde tirava uma. A diferença é que lá havia uma
única cor de frente absorvendo o interior; aqui são **três** (amadeirado, preto
fosco e off-white), e cor nenhuma divide chapa com outra. Está explicado na
página 6 da proposta, que é o argumento de por que ele custa o que custa.

---

## 🐛 Um erro que eu quase deixei passar

Lancei a fita **peça a peça** e cheguei a 190,33 m para 132,94 m² — **1,43 m/m²**.
A faixa da casa é **2,6 m/m²** (fator validado em `corte-spe-decorado.py`).

Eu tinha fitado só a **borda aparente** — frente de porta, gaveta, topo de nicho
— e esquecido a borda de **caixaria**: todo topo de lateral, divisória,
prateleira e base leva fita, aparente ou não. Num job com 26 prateleiras e três
roupeiros, isso é muita fita.

O motor agora usa `max(explícito, 2,6 × área)` e **imprime os dois números**,
para que a diferença fique visível em vez de silenciosa. Efeito: +155 m de fita,
+R$ 900 de custo direto, **+R$ 2.800 de preço**.

> 🧠 **Para o moleskine:** fita lançada peça a peça é mais precisa que o fator
> da casa **só quando se lança TODA a peça**. Meia lista é pior que o fator.
> O teste é dividir pelo m² e comparar com a faixa — igual ao teste do R$/m².

---

## Dúvidas e conferências — 12 itens

**Para a arquiteta**

1. A cozinha diz "frentes em preto fosco e off-white conforme referência" sem
   dizer **qual módulo leva qual**. Adotei inferiores e torre em preto, aéreos
   em off-white.
2. Os **frisos do painel** podem ser usinados no MDF ou em perfil metálico
   preto (P07). Orcei usinados — perfil metálico é terceirizado e muda o valor.
3. O **fundo da cristaleira** pode ser MDF 6 mm ou espelho, "conforme acabamento
   final". Orcei MDF; espelho acrescenta ~R$ 900.

**Marcado pela própria prancha como "conferir em obra"**

4. Cota vertical do rack (piso até a face inferior) — está escrito
   "DEFINIR / CONFIRMAR EM OBRA".
5. Inclinação real da escada — a geometria dos nichos acompanha o intradorso.
6. Modelos definitivos dos eletrodomésticos — a modulação da cozinha é
   preliminar, baseada em aparelho padrão.

**Sem preço na base (★ no relatório) — R$ 4.085**

7. Sistema de correr de **3 folhas** — temos o Dominus de 2 folhas a R$ 1.840;
   escalei para R$ 2.760. Confirmar com a Rometal.
8. Batente oculto + dobradiça invisível da porta integrada — R$ 600.
9. Estrutura niveladora de sarrafo atrás do painel — R$ 402.
10. Barra metálica contínua de fixação do rack — R$ 322.

---

## Fora do escopo

- **Tampo e rodabanca da cozinha** — pedra de 20 mm, 2970 × 650. Marmoraria.
- Eletrodomésticos, louças e metais.
- Elétrica e hidráulica, inclusive os circuitos exclusivos dos eletros.
- Alvenaria, gesso, revestimento e pintura.
- Móveis soltos, cortinas e decoração.

---

## 🔁 24/08 — correções do Jonathan na proposta

1. **Saíram TODAS as cotas de móvel.** Era a segunda vez que ele pedia (a
   primeira foi no Carol e Vinícius, 21/08). Virou **regra da skill** —
   `referencias/proposta-comercial.md`, no topo, e resumida no `SKILL.md`.
   Onde a dimensão era o argumento, passou a ser dita em palavras: "do piso ao
   forro", "parede inteira revestida", "nicho contínuo sem divisória".
2. **Saiu toda a explicação de formação de preço.** A página do upgrade não fala
   mais de chapa, plano de corte nem aproveitamento. Passou a falar só de
   benefício: *"abrir a porta deixa de mostrar branco"* e *"marca de uso aparece
   muito menos em superfície colorida"*. Também virou regra.
3. **Imagens do projeto — BLOQUEADO, não feito.** Ver abaixo.

### ⛔ Por que a proposta ainda está sem imagem

Os renders do projeto estão em `Apresentação_Carla.pdf`, **39 MB**. Não consegui
trazer por nenhum dos dois caminhos:

| Caminho | Resultado |
|---|---|
| `curl` direto no Drive | **bloqueado pela política de rede** — o proxy devolve 403 no CONNECT para `drive.google.com` |
| conector do Drive (`download_file_content`) | devolve **base64 no contexto** — 39 MB viram ~52 MB de texto, inviável |

Testei o mecanismo com a imagem de 10 KB da pasta: funciona, mas é uma
miniatura de 300 × 300 px, sem resolução para impressão.

⚠ As "imagens de referência" que aparecem nos detalhamentos **não servem** — as
próprias pranchas as rotulam como *"referência estética fornecida pelo
cliente"*. É inspiração de terceiro, não o projeto da Carla, e usar na nossa
proposta é risco de direito de imagem. Está escrito na regra.

**O que destrava:** subir a `Apresentação_Carla.pdf` (ou só os renders) no chat,
como foi feito com o caderno do Vinícius. Com as imagens em mão, a proposta vira
o deck premium A4 paisagem, no padrão do Junior.
