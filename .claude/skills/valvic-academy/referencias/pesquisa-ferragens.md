# Pesquisa verificada — ferragens (base do Volume 2)

Levantamento de setembro/2026 para o piloto da apostila. **Todo número aqui foi conferido
entre no mínimo duas fontes**, e onde as fontes divergem está dito por quê. Fontes ao final.

> Regra que rege este arquivo: quando o valor depende do modelo, registramos **onde
> encontrar** e **o que a medida significa** — nunca cravamos um número que a bancada vai
> desmentir. Número inventado em apostila é pior que apostila nenhuma: parece autoridade.

---

## 1 · A separação que resolve metade da confusão

Duas coisas independentes são misturadas o tempo todo:

| | O que diz | Valores |
|---|---|---|
| **Curvatura do braço** | **Onde a porta pousa** em relação à lateral | 0 · 9,5 · 16 mm |
| **Ângulo de abertura** | **Quanto a porta abre** | 95° a 175° |

Existe reta de 110° e existe super curva de 110°. São eixos separados.

## 2 · Curvatura do braço — e a conta que explica os números

| Dobradiça | Curvatura | Posição da porta | Nomenclatura Hettich |
|---|---|---|---|
| Reta | **0 mm** | Sobreposta total — cobre a lateral inteira | Montagem **Baixa** |
| Curva | **9,5 mm** | Parcialmente sobreposta — para no meio da lateral | Montagem **Alta** |
| Super curva | **16 mm** | Embutida — fica dentro do vão, faces alinhadas | Montagem **Super alta** |

**A curvatura é a distância entre a borda da porta e a face interna da lateral.**
Numa lateral de 18 mm: reta cobre os 18 (curvatura 0) · curva para nos 9 (braço 9,5) ·
super curva não cobre nada (braço 16, um pouco menos que 18 por causa da folga).

Isso transforma decoreba em conta — e é o ponto didático central do capítulo 1.

## 3 · Furação e caneco

| Dado | Valor | Observação |
|---|---|---|
| Diâmetro do caneco | **35 mm** padrão | Existem 26 e 40 mm; 35 é o de linha em planejado |
| Distância do furo à borda | **3 a 5 mm** | Definida pela tabela do modelo, junto com o calço |
| Centro do caneco à borda | **21 a 23 mm** | = 17,5 mm (raio) + a distância acima |
| Padrão de furação da base | **48/6** | Furos a 48 mm entre si, deslocados 6 mm do centro do caneco |
| Espessura de porta | **15 a 22 mm** (Sensys 8645i) · até 24 mm (Blum 110°) | Nossa chapa de 18 mm fica no meio da faixa |

## 4 · Regulagem e comportamento

- Recobrimento: **±2 mm** · Profundidade: **+3 / −2 mm** (Blum e Hettich publicam iguais).
- Fecho automático a partir de **35°** de abertura (Sensys).
- Sensys segue **DIN EN 15570**; pistão de gel pressurizado opera de 5 °C a 45 °C.

## 5 · Ângulo — escolhe-se pelo que está ATRÁS da porta

| Ângulo | Para quê | Atenção |
|---|---|---|
| **95°–110°** | Porta comum de armário e cozinha | Padrão. **Não serve com gaveta interna** |
| **155°** | Módulo com **gaveta interna** ou prateleira extraível | É o "grande ângulo", especificado para isso |
| **165°–175°** | Armário de canto, canto de 90°, móvel em L | Conferir o vão livre antes |
| 45° · 90° · 270° | Aplicações especiais e móvel em ângulo | Encomenda, não estoque |

## 6 · Quantidade por porta

| Altura da porta | Dobradiças |
|---|---|
| ≤ 900 mm | **2** |
| ~1600 mm | **3** |
| ~2000 mm | **4** |
| ~2400 mm | **5** |

Porta pesada (maciço) ou larga: soma uma.

## 7 · Calços — não são intercambiáveis entre marcas

- **Hettich:** 0,0 · 1,5 · 3,0 mm
- **Outras linhas:** 0 · 3 · 6 · 9 mm

Isso é armadilha real de bancada: calço de uma marca em dobradiça de outra muda o
recobrimento e desregula a porta. 🟡 **Falta definir qual a Valvic usa.**

## 8 · Corrediças

| | Telescópica | Oculta (sob o fundo) |
|---|---|---|
| Fixação | Na lateral da gaveta | Sob o fundo — lateral fica limpa |
| Folga lateral | **12,5 a 13 mm por lado** | **Depende do modelo** — fontes vão de 6,5 a 11 mm |
| Carga | Até 25 kg (simples), até 45 kg (reforçada) | Hardt 450 mm: 35 kg |
| Durabilidade | Menor — perde óleo, acumula sujeira | ~100 mil ciclos |

> **Os 13 mm da telescópica não são folga arbitrada: são a espessura do corpo da
> corrediça**, que fica entre a caixa e a lateral. Entender isso é o que impede o erro de
> aplicar o mesmo número na oculta.

## 9 · Pistão a gás — comum × força inversa

| | Pistão comum | Força inversa |
|---|---|---|
| A porta abre | **Para cima** — pivô no topo (báscula de aéreo) | **Para baixo** — pivô embaixo, a porta gira **para fora e para baixo** |
| O pistão | **Empurra** — vence o peso e sustenta aberta | **Segura** — trabalha contra a queda, liberando aos poucos |

| Força | Peso de porta |
|---|---|
| 60 N | até ~6 kg |
| 80 N | até ~8 kg |
| 100 N | até ~10 kg |
| 120 N | até ~12 kg |

Porta com **60 cm ou mais de largura: dois pistões**.
Fórmula citada pelos fornecedores: `Peso (kg) × (Baricentro mm ÷ Curso útil mm) × 1,25`.

---

## 10 · Divergências encontradas, e o que se conclui

**"Dobradiça reta não abre mais que 90°" — falso.** Afirmado por um portal grande de
material de construção. Blum e Hettich vendem reta de 110° como item de linha, e o varejo
brasileiro lista "reta 110° com Blumotion". A origem do erro é misturar curvatura com
ângulo (ver §1).

**Folga da corrediça oculta — sem consenso.** Uma fonte de instalação diz 6,5 mm por lado;
outra atribui 9 a 11 mm ao catálogo FGVTN; uma página de fabricante fala em "folga não
significativa". A divergência é real porque **o valor é do modelo**. Conclusão para a
apostila: ensinar a consultar a tabela, não um número.

---

## 11 · Pendências — só a produção responde

1. **Pistão: comum ou inversa?** O `orcamentista-marcenaria/referencias/ferragens.md`
   registra "Pistão a gás força inversa: 60N e 100N (básculas/aéreos)". Báscula de aéreo
   abre para cima, e isso pede pistão **comum**. Ou a nota está mal rotulada, ou aplicamos
   inversa em portas de abrir para baixo e o registro generalizou. **Não corrigir sem
   confirmar** — é compra real.
2. **Qual calço a Valvic usa** (ver §7).
3. **Distância do furo à borda na nossa furação padrão** de 18 mm — define o recobrimento de
   todo projeto.
4. **Hardt, Hettich ou Blum no capítulo.** O `ferragens.md` diz que **Hardt é ~70% da compra
   real**, mas Hettich e Blum são as marcas de projeto e de garantia. A apostila ensina o que
   usamos ou o que existe no mercado? Muda o índice do Volume 2.

---

## Fontes

Fabricante: Hettich Brasil (Sensys 8645i, 8657i; comparativo corrediça invisível ×
telescópica) · Blum (CLIP top BLUMOTION; catálogo 2022/2023; dobradiça 155° grande ângulo) ·
FGVTN (corrediças ocultas) · Soprano (escolha de dobradiça; escolha de pistão) ·
Häfele Brasil (corrediça telescópica).

Técnico e de montador: Portal do Montador de Móveis (calços, curvaturas 0 / 9,5 / 16) ·
Guia do Marceneiro (padrão 48/6) · Guia da Marcenaria (gaveta com corrediça oculta) ·
Edem Marceneiro (funcionamento do pistão força inversa) · Completa (instalação de
telescópicas; escolha de pistão) · Canal da Marcenaria.

Varejo e agregadores, usados só para confirmar disponibilidade de linha: Leroy Merlin,
Leo Madeiras, Madeiras Gasômetro, Maxave.
