# Aspire + dialeto G-code do JRG (Degrau 4)

> Como o Téo gera **cortes especiais** que o Marcenária Diferente não entrega
> (friso de LED, friso de dobra/V-groove, curva, peça em ângulo) e também cortes
> de contorno para a **Raizen Solid TAF**. Inclui o **dialeto de G-code do
> controlador JRG**, decodificado de arquivos `.tap` reais, comprovados na máquina.

## Caminho seguro (sempre)

1. **DXF primeiro.** Téo gera o vetor (DXF/SVG); o operador importa no Aspire,
   aplica o toolpath e posta. Toda a segurança do Aspire (simulação) fica no fluxo.
2. **G-code direto** (`.tap`) só **depois de simular no Aspire + air-cut** (sem
   material). Post errado ou Z trocado bate o spindle / estraga a chapa.
3. **Nunca inventar os M-codes próprios do JRG** (ver abaixo) — copiar verbatim.

## ⭐ Referência de Z — a regra que muda tudo (CONFIRMADO pelo Paulo)

Na mesa há uma **chapa de sacrifício**; o **eixo Z é sempre zerado sobre ela**
(Z-zero = topo do sacrifício). A chapa a cortar fica **em cima** do sacrifício.

### 🚨 INVARIANTE DE SEGURANÇA — Z NUNCA passa de −0,100
O ponto mais fundo de **qualquer** toolpath é **Z = −0,100** (0,1mm dentro do
sacrifício). **Nunca mais que isso**, seja qual for a espessura. Furar o
sacrifício além de 0,1 = estraga a chapa de sacrifício, a fresa e arrisca a mesa.

- **Topo da chapa** fica em `Z = +espessura` (chapa 15mm → topo em Z+15).
- **Corte passante** = descer até **Z−0,100**. Descida total = espessura + 0,1:
  - 15mm → 15,1 · 18mm → 18,1 · 6mm → 6,1 (sempre terminando em Z−0,1).
- **Corte parcial** (friso, V-groove, rebaixo, **vinco de dobra**) =
  `Z = espessura − profundidade` (ex.: friso de 5mm numa chapa de 15mm → fundo em
  **Z+10**; dobra deixando pele de 1mm em 15mm → **Z+1**). Nunca passar de −0,1.
  Validado no exemplo de dobra — ver `dobra-de-mdf.md`.
- **Altura de segurança (clearance)** = topo da chapa + **5,08mm** (0,2", padrão
  Aspire). ⇒ **conferir a espessura:** `espessura = clearanceZ − 5,08`.
  - Exemplos reais: clearance 11,080 → 6mm · clearance 20,080 → 15mm.

> **Caça-erro / trava do Téo:** ao gerar ou conferir qualquer `.tap`, validar que
> **nenhum Z < −0,1**. Se a clearance não bater com a espessura declarada, ou um
> "corte passante" não terminar em Z=−0,1, **parar e perguntar** — provável erro
> de Z-zero/espessura (a causa clássica de furar o sacrifício ou cortar raso).

## Ferramentas (magazine de 10)

Por ora, testes só com **T2** e **T7**. As outras 8 (finalidade, offsets/descontos)
o Paulo informa depois.

| Posição | Ferramenta | Raio | Usada em | Status |
|---|---|---|---|---|
| **T2** | **Fresa reta 6mm** | 3mm | contorno/corte passante (os dois exemplos) | em uso |
| **T7** | **Fresa reta 3mm** | 1,5mm | cortes finos/detalhe (a detalhar) | em uso |
| T1, T3–T6, T8–T10 | a informar | | (V-bit p/ dobra, friso LED, etc.) | pendente |

> O `M6T<n>` + `G43 H<n>` sempre casam o nº da ferramenta com o nº do offset (H).
> Em contorno externo com fresa de 6mm, os cantos saem com **arco de raio 3mm**
> (= raio da fresa rolando no canto). É o offset do toolpath, não um chanfro.

## Dialeto "JRG CNC SOLID TAF" (decodificado de `.tap` reais)

Exemplos comprovados em `exemplos/`: `jrg-exemplo-corte-passante-15mm.tap`
(quadrado 500×500, chapa 15mm, fresa 6mm/T2) e `jrg-exemplo-corte-curvo-6mm.tap`
(peça curva, chapa ~6mm).

### Convenções gerais
- **Unidades:** milímetros. **Absoluto** (G90 implícito — *não* é emitido; sem
  G20/G21). Coordenadas com **3 casas**; avanços com **1 casa**.
- **Numeração:** `N` + número, incremento de 1. No **cabeçalho/rodapé** há espaço
  após o N (`N5 M158`); no **corpo** não há (`N10G00X...`). Mimetizar.
- **Eixos:** Y é o **eixo longo** (~2800mm), X o **curto** (~1900mm). Origem
  **0,0 no canto** da chapa/mesa (coordenadas em torno do zero). *Datum exato a
  confirmar.* Z-zero na mesa (ver acima).

### Cabeçalho (ligar)
```
(JrgCnC - Vision V1.01 - by Aspire)
(######## Troca de ferramentas ########)
(   NUMERO DA FERRAMENTA:<n>)

N5 M158            ; M-code JRG — LIGA (par com M159) — NÃO ALTERAR
N6 M162            ; M-code JRG — LIGA (par com M163) — NÃO ALTERAR
N7 M6T<n>          ; troca para ferramenta n
N8 M3S<rpm>        ; spindle horário (ex.: 24000)
N9 G0 G43 H<n>     ; rápido + compensação de comprimento (H = nº da ferramenta)
```

### Corpo (movimentos)
- `G00 X.. Y..` rápido (posiciona) → `G00 X.. Y.. Z<clearance>` sobe/desce em rápido
  à altura de segurança (espessura + 5,08).
- **Mergulho:** `G1 X.. Y.. Z<final> F2500.0` — plonge direto até a profundidade
  final (corte passante: Z-0,100). *Observado: passada única em cheio até 15mm.*
- **Corte:** `G1 X.. Y.. Z<final> F10000.0`; depois **F é modal** (omitido).
- **Arcos:** `G2` (horário) / `G3` (anti-horário) com **I/J** (offset do centro,
  relativo ao ponto inicial). **Z e F modais** nos arcos (omitidos na linha).
- **Avanços observados (6mm em MDF/compensado):** mergulho **F2500**, corte
  **F10000** (mm/min). Vêm do toolpath — ajustar por material/ferramenta/passada.

### Rodapé (desligar)
```
N.. M159           ; desliga o par de M158 — NÃO ALTERAR
N.. M163           ; desliga o par de M162 — NÃO ALTERAR
N.. M5             ; para o spindle
N.. G0 Y2840 X51 Z50   ; estaciona
N.. M30
N.. M30
%
```

### Regra de ouro
Os M-codes **M158/M162** (liga) e **M159/M163** (desliga) são do JRG (provável
vácuo da mesa + aspiração). **Sempre em par, sempre presentes, nunca inventados.**

## 🔩 Regras de ENCAIXE e NESTING (obrigatórias)

> Definidas pelo Paulo (16/06). Valem para **todo** projeto com encaixe/nesting.
> Referência visual: `exemplos/cilindro-ajustado-encaixe-dogbone.crv3d` (projeto
> Aspire corrigido — arquivo binário, não editável por mim, guardado como gabarito).

### 1. Osso de cão (dogbone) em encaixe — em UM lado só
A fresa é redonda → deixa o **canto interno arredondado** (raio = raio da fresa),
e a aba de **canto vivo NÃO entra até o fundo**. Solução: **osso de cão** =
sobrecorte circular no canto.
- **Raio do osso de cão = raio da fresa** usada no encaixe (T2 → 3mm; T7 → 1,5mm).
- 🚨 **Fazer em APENAS UMA das duas peças do par** — ou na **estrutura** (a peça que
  encaixa / a aba) **ou** no **buraco** que a recebe. **NUNCA nas duas** (senão tira
  material a mais e o encaixe fica frouxo).
- **Padrão Valvic / neste caso: na ESTRUTURA** (nos ombros das abas das réguas), e o
  **buraco/rasgo sai LIMPO** (ex.: tampo redondo / discos sem osso de cão).
- Implementado em `gerados/gen_dxf4.py`: osso de cão nos 4 ombros de cada régua
  (índices 1,4,7,10 do contorno); rasgos dos discos sem osso de cão.

### 2. Folga de 7mm também na BORDA da chapa
A mesma folga de **7mm entre peças** vale **da borda da chapa**: nenhuma peça a
menos de **7mm da borda**. ⇒ no nesting, **margem = 7mm** (não 10mm).

### 3. Ranhuras de dobra: AVANÇO + ZIGZAG contínuo
🚨 Erro pego pelo Paulo (DXF v2): ranhuras desenhadas como linhas soltas fazem
a fresa **sair da peça entre passadas → quebra/lasca as quinas** do MDF.
- As ranhuras **avançam 10mm para fora da peça** em CIMA e EMBAIXO (passam da borda
  do painel) — dobra limpa até a extremidade.
- Devem ser **ligadas num ÚNICO ZIGZAG** (serpentina): a fresa entra **1 vez**,
  percorre tudo e sai **1 vez**. As voltas do zigzag ficam na sobra (fora da peça).
- ⚠️ Nesting: o avanço de 10mm precisa de **folga ≥10mm** nas pontas ranhuradas
  (não basta 7mm). Posicionar o painel com ~12mm livres nas extremidades.
- Implementado em `gerados/gen_dxf3.py` (v3): polilinha aberta serpentina na camada
  RANHURAS, `OVER=10`.

## Estrutura multi-operação (vários cortes num arquivo)

Um `.tap` pode ter **vários cortes/operações** em sequência, com **um único
cabeçalho e rodapé**. Cada operação:
1. é separada por um comentário `(Corte N)` + `()`;
2. faz: `G00` posiciona → `G00 Z<clearance>` → `G1 Z<prof> F2500` mergulho →
   contorno (G1/G2/G3) no Z da operação → `G00 Z<clearance>` retrai;
3. **pode ter Z diferente** entre operações (ex.: contornos passantes em Z−0,1 e
   ranhuras de dobra em Z+1 no mesmo arquivo).
4. troca de ferramenta (`M6T<n>`) só aparece se a operação seguinte mudar de
   fresa — nos exemplos atuais é tudo T2.

### 🔑 Regra de sequência (ordem das operações)
**Operações parciais/internas primeiro (peça ainda presa à chapa = firme); o corte
passante que SOLTA a peça vem por ÚLTIMO.** Visto no exemplo completo de curva:
1º os contornos da estrutura, 2º as **ranhuras de dobra** (parcial, Z+1) no painel,
3º o **contorno que solta** o painel (Z−0,1). Se soltasse antes, a peça se mexeria
e estragaria. (Vácuo M158/M162 segura as peças já soltas.)

> Exemplo de referência: `exemplos/jrg-exemplo-curva-completa-estrutura-mais-painel.tap`
> (estrutura + ranhuras + corte de separação, 3 operações, tudo T2).

## A confirmar (para gerar corte com segurança total)
- ✅ **Z-zero na chapa de sacrifício** — CONFIRMADO. Z mín. = −0,1 (ver acima).
- **Datum 0,0** na chapa (onde fica o canto de referência na mesa).
- **Passada única × múltiplas:** até que espessura corta em cheio numa passada só?
  Acima disso, de quanto é o passo em Z?
- O que cada M-code (M158/M159/M162/M163) realmente aciona.
- Demais **ferramentas do magazine** (V-bit e ângulo, fresa de friso LED).
- Lead-in/rampa: os exemplos mergulham reto no canto — confirmar se há rampa em
  peças maiores.

> **Status:** dialeto calibrado com 2 cortes passantes reais (6mm e 15mm). Falta
> 1 exemplo de **friso/V-groove** (corte parcial em profundidade) para fechar a
> lógica de cortes especiais e múltiplas passadas em Z.

---

## ⭐ Fresa de 45° — chanfro / bisel  (Paulo, 26/06)
> 🚨 **Paulo fala/desenha em CENTÍMETROS.** "50,6" = 50,6 cm = **506 mm**. (Erro meu
> anterior: tinha lido como 0,6 mm — era 6 mm na medida = 3 mm/lado.)
- **Ferramenta:** **T7 = fresa de 45°** (CONFIRMADO Paulo + `.tap` `M6T7`, 26/06).
  A anotação antiga "T7 = fresa reta 3 mm" estava **ERRADA** — corrigida. Lição: o que
  sai no `.tap` é a verdade; confiar nele.
- **Método:** desenhar uma **LINHA** e mandar a 45° **correr sobre a linha** (sem offset).
- **Z = espessura + 0,1** p/ **chanfro completo** (atravessa): peça 18→**18,1**; 15→**15,1**.
  (No `.tap` o Z foi **8,900** = chanfro PARCIAL; falta a espessura da chapa do teste.)
- **Compensação = a 45° "come" por lado ≈ a PROFUNDIDADE do chanfro** (45° → horizontal =
  vertical). **NÃO é número fixo:**
  - **Quadrado do `.tap`:** desenhado **506×506** → final **500×500** = **3 mm/lado**.
  - **Tampo redondo:** Ø303 → Ø300 = **1,5 mm/lado** (chanfro mais raso).
  - **Regra:** 4 lados → desenhar **+2×come** em cada medida; 1 lado → **+come** só nela.
- **Fluxo do chanfro em 1 lado só:**
  1. Desenha o retângulo (com a compensação no lado a chanfrar) **+ uma linha extra** sobre ele.
  2. Passa a 45° **só nessa linha**.
  3. Troca pela **T2 (fresa 6 mm)** e corta o **contorno por fora** do retângulo.
- **Dados do `.tap`:** T7 · S13500 · 1 passe **Z8,900** · mergulho F2000 / corte F4000 ·
  quadrado 506×506 (X39,24/Y46,39 → X545,24/Y552,39) · clearance Z20,08.
- **A CONFIRMAR:** (1) T7 ou T8? (2) espessura da chapa do teste → fecha
  **come/lado = profundidade = espessura − Z**.
