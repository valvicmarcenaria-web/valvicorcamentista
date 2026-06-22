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

## A confirmar / calibrar
- **Raio × espaçamento:** que **raio de curva** esse padrão (12mm, pele 1mm, 15mm)
  produz? A relação raio→espaçamento é o que falta para o Téo projetar uma curva
  de raio-alvo. (Regra prática a levantar com o Paulo: "pra raio X, uso espaçamento Y".)
- **Pele por espessura:** 1mm vale para 15mm. E para 18mm? E 6mm? (provável manter
  ~1mm, confirmar.)
- **Lado da pele:** confirmar que a pele (face lisa) vai sempre para **fora** da
  curva e a ranhurada para dentro.
- **Acabamento:** a face ranhurada some (vai colada/escondida) ou precisa de
  preenchimento/forramento? Lâmina/laca por cima da curva?
- **Limite de raio:** menor raio possível sem quebrar a pele.

> **Status:** técnica capturada e parametrizável. Falta a **relação raio↔espaçamento**
> (a calibrar com casos reais) para o Téo projetar uma dobra a partir do raio desejado.
