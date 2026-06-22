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

## ⭐ Referência de Z — a regra que muda tudo (CONFIRMADO pelo Jonathan)

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
o Jonathan informa depois.

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
