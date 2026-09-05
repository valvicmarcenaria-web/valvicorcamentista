# Ficha do exemplo — Criado-mudo com cantos arredondados (curvo)

- **Data:** 2026-06-24
- **Quem mandou:** Paulo
- **Tipo:** modelo construtivo (curva + estrutura + painel) / dobra de MDF
- **Arquivos deste caso:**
  - `2026-06-24_criado-mudo-curvo.crv3d` (gabarito Aspire, binário)
  - imagem de referência (Pinterest) — criado com cantos arredondados, tampo de pedra

## 1. O que é
Criado-mudo (mesa de cabeceira) com **cantos arredondados**. O corpo amadeirado
faz a curva contínua na quina vertical; tampo de pedra por cima. Mesmo **modelo
construtivo do cilindro** (duas tampas + réguas de estrutura + painel que envolve),
num formato de criado com canto arredondado.

## 2. O truque (o que faz dar certo)
Peças no arquivo:
1. **Base + Teto** (2 peças horizontais com a curva na ponta) — fundo e tampa
   estrutural. Levam os **filetes / ossos de cão** onde a estrutura encaixa.
2. **4 réguas retas** (estrutura vertical) — unem base e teto, encaixando nos
   **ossos de cão** do teto e da base.
3. **1 painel grande = a lateral** — tem um **rebaixo deixado só na pele do MDF**;
   a pele dobra e **envolve a curva**, abraçando teto e base → vira a lateral curva.

Dobra aqui é por **rebaixo até a pele** (bolso) — diferente dos **vincos/zigzag**
usados na dobra do cilindro (`dobra-de-mdf.md`). [A CONFIRMAR — ver §3]

## 3. Resolvido pelo `.tap` (24/06) — fonte: `..._criado-mudo-curvo_teo.tap`
- ✅ **Raio real = R60 (Ø120).** O arco no G-code é R63 = R60 + 3mm da fresa. O "120"
  do projeto era o **DIÂMETRO** — daí a confusão de cálculo.
- ✅ **Canto de 90°.** Arco = 94,2 mm → bate com os **95 mm (9,5 cm)** da zona de
  dobra. **O 9,5 cm do Paulo estava certo;** quem errou foi o Téo (assumiu R120).
- ✅ **Bolso contínuo** feito por ranhuras a **~5,7 mm** (< Ø6 da fresa → sobrepõe →
  fundo liso). Pele **1 mm** (deformação 0,83% → ok).
- ✅ **T2 (6mm), ossos de cão R3, Z+1,0 dobra / Z−0,1 passante.** Um canto neste teste.

### Ainda em aberto
- **Espessura da chapa** (15 mm?) → profundidade do bolso (15−1 = 14 mm).
- Confirmar com o Paulo que **120 = diâmetro** (o `.tap` indica R60).

> **Achado-chave:** largura da zona de dobra = **ângulo(rad) × raio**. Registrado em
> `dobra-de-mdf.md` (Variante 2 — bolso contínuo fold-to-skin).

## 4. Ferramenta(s) e máquina
- Ferramenta lida do `.crv3d`: **"FRESA 6 MM CORTE"** (= T2, fresa 6 mm).
- Toolpaths no arquivo: **perfil (profile)** + **contorno (contour group)**.
- Z / profundidade / passadas: (a confirmar)

## 5. Regra que isso gerou
- [ ] Vira regra? Onde foi parar:
  - `modelo-construtivo.md` — criado-mudo curvo = tampas + réguas + painel envolvente.
  - `dobra-de-mdf.md` — variante "dobra por rebaixo até a pele" (se confirmado).
- Resumo da regra em 1 linha: (fechar após confirmação dos 4 pontos)

## Notas do Téo
Extraí do binário só: ferramenta "FRESA 6 MM CORTE" + toolpaths de perfil/contorno.
Dimensões não são legíveis no `.crv3d` (números binários). Regra final depende das
respostas do §3.
