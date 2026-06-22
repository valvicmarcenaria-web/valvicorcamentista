# Dobra de MDF por vincos (kerf bending) — técnica Valvic

> Como a Valvic curva chapa de MDF: ranhuras (fendas) paralelas que removem quase
> toda a espessura, deixando uma **pele fina** que dobra. Decodificado de `.tap`
> real (`exemplos/jrg-exemplo-dobra-mdf-kerf.tap`) + explicação do Jonathan.
> Técnica construtiva **e** parametrizável para gerar G-code (Degrau 4).

## Princípio
Fresa reta abre ranhuras paralelas no **lado interno** da curva, removendo material
até sobrar uma **pele** contínua. A chapa dobra fechando as ranhuras; a pele fica
na face **externa** (convexa). A curva é **facetada** (cada costela cheia fica reta;
a dobra acontece nas peles finas entre elas) — quanto mais ranhuras, mais lisa.

## Parâmetros do exemplo real (CONFIRMADOS)
- **Ferramenta:** T2, **fresa reta 6mm**. (Não é V-bit — é fenda de fundo chato.)
- **Chapa:** 15mm. **Pele deixada: 1mm.** → profundidade de corte **14mm**.
- **Z de corte = +1,000** (`Z = espessura − profundidade = 15 − 14 = 1`). Z-zero no
  sacrifício; respeita a trava (Z nunca < −0,1).
- **Espaçamento das ranhuras: 12mm** (centro a centro).
- **Largura da ranhura:** 6mm (= diâmetro da fresa). **Costela cheia entre elas:** 6mm.
- **Sentido:** ranhuras ao longo de Y (~575mm); avanço passo a passo em X de 12mm,
  em **serpentina** (corta sobe, anda 12mm no Z de corte, corta desce…).
- Avanços: mergulho **F2500**, corte **F10000** (padrão observado p/ 6mm).
- Clearance Z20,080 = 15 + 5,08 (confere a espessura).

## Fórmula para o Téo gerar (parametrizável)
Dado: largura do painel `W`, comprimento `L`, espessura `e`, pele `p` (ex.: 1mm),
espaçamento `s` (ex.: 12mm), fresa Ø`d`:
- **Z de corte** = `e − (e − p)` = **`p`** (= deixa a pele). Ex.: 15mm, pele 1 → Z+1.
- **Nº de ranhuras** ≈ `W / s` (centradas no painel).
- Cada ranhura é um corte reto de comprimento `L` no Z da pele; transição de `s` em
  X entre ranhuras; **sempre validar Z ≥ −0,1**.

## Fluxo completo da peça curva (a "cambota")

A dobra não vive sozinha — ela **veste uma estrutura**. O conjunto de teste
(`exemplos/jrg-exemplo-curva-completa-estrutura-mais-painel.tap`) mostra tudo num
arquivo só, em 3 operações na ordem certa:

1. **Estrutura** (contornos passantes Z−0,1): **base + teto** (dois painéis ~900mm
   de largura com uma **quina curva de R203mm**) + **4 réguas** (~55×353mm) que
   unem base e teto. As bordas têm pequenos **encaixes/abas** (os detalhes em
   G2/G3) para montagem por encaixe.
2. **Ranhuras de dobra** (parcial, Z+1) no **painel de revestimento**.
3. **Corte de separação** (passante Z−0,1) que **solta o painel** por último.

A **cambota** = a estrutura curva (base/teto + réguas) que dá a forma; o **painel
ranhurado** é o MDF curvado que a veste. O painel tem **parte plana + parte
ranhurada**: a plana cobre os trechos retos, a ranhurada (~324mm) abraça a quina
de R203.

## ⭐ Calibração raio ↔ espaçamento (DADO REAL deste conjunto)

- **Quina da cambota: R203mm** (arco de 90° → comprimento ≈ **318,8mm**).
- **Zona ranhurada do painel: ~324mm**, espaçamento **12mm**, pele **1mm**, 15mm.
- **Nº de ranhuras ≈ comprimento do arco ÷ espaçamento** → 318,8 ÷ 12 ≈ **27** ✓
  (bate com as ~27 ranhuras do arquivo).

> **Regra emergente (a generalizar):** a zona ranhurada = comprimento do arco
> (`ângulo × raio`); nº de vincos ≈ arco ÷ espaçamento. Para esta receita
> (12mm / pele 1mm / 15mm) o raio fechado é **R≈203mm**. Falta confirmar se o
> espaçamento muda o raio mínimo, ou se o raio é definido só pela cambota e o
> espaçamento é fixo (12mm) por suavidade.

## A confirmar / calibrar
- **Raio mínimo:** R203 funcionou com folga? Qual o menor raio sem quebrar a pele
  de 1mm? O espaçamento de 12mm muda esse limite?
- **Espaçamento é sempre 12mm** ou varia conforme o raio/acabamento?
- **Pele por espessura:** 1mm vale para 15mm. E para 18mm? E 6mm? (provável manter
  ~1mm, confirmar.)
- **Lado da pele:** confirmar que a pele (face lisa) vai sempre para **fora** da
  curva e a ranhurada para dentro.
- **Acabamento:** a face ranhurada some (vai colada/escondida) ou precisa de
  preenchimento/forramento? Lâmina/laca por cima da curva?
- **Limite de raio:** menor raio possível sem quebrar a pele.

> **Status:** técnica capturada e parametrizável. Falta a **relação raio↔espaçamento**
> (a calibrar com casos reais) para o Téo projetar uma dobra a partir do raio desejado.
