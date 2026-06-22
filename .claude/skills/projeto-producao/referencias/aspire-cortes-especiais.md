# Aspire + dialeto G-code do JRG (Degrau 4)

> Como o Téo gera **cortes especiais** que o Marcenária Diferente não entrega
> (friso de LED, friso de dobra/V-groove, curva, peça em ângulo) para a **Raizen
> Solid TAF**. Inclui o **dialeto de G-code do controlador JRG**, decodificado de
> um arquivo `.tap` real, comprovado na máquina.

## Caminho seguro (sempre)

1. **DXF primeiro.** Téo gera o vetor (DXF/SVG); o operador importa no Aspire,
   aplica o toolpath e posta. Toda a segurança do Aspire (simulação) fica no fluxo.
2. **G-code direto** (`.tap`) só **depois de simular no Aspire + air-cut** (sem
   material). Post errado ou Z trocado bate o spindle / estraga a chapa.
3. **Nunca inventar os M-codes próprios do JRG** (ver abaixo) — copiar verbatim.

## Dialeto "JRG CNC SOLID TAF" (decodificado de `.tap` real)

Referência: `exemplos/jrg-exemplo-marcacao.tap` (peça "pé da mesa", compensado
flex 200×91cm — uma passada de **marcação**, Z-0,1mm).

### Convenções gerais
- **Unidades:** milímetros. **Absoluto** (G90 implícito — *não* é emitido; também
  não há G20/G21). Coordenadas com **3 casas decimais**; avanços com **1 casa**.
- **Numeração de linha:** `N` + número, incremento de 1. No **cabeçalho/rodapé** há
  espaço após o N (`N5 M158`); no **corpo** não há (`N10G00X...`). Mimetizar.
- **Eixos:** Y é o **eixo longo** (~2800mm), X o **curto** (~1900mm). Origem no
  canto (coordenadas positivas). *Datum exato (0,0) e Z-zero a confirmar.*

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
- `G00 X.. Y..` rápido (posicionamento); `G00 X.. Y.. Z..` rápido até a altura de
  segurança (no exemplo Z≈11.08).
- **Mergulho:** `G1 X.. Y.. Z<corte> F2500.0` (avanço de mergulho).
- **Corte:** `G1 X.. Y.. Z<corte> F10000.0`; depois **F é modal** (omitido).
- **Arcos:** `G2` (horário) / `G3` (anti-horário) com **I/J** (offset do centro,
  relativo ao ponto inicial). **Z e F modais** nos arcos (omitidos na linha).
- Os avanços (F2500 mergulho / F10000 corte) vêm do **toolpath**, não do post —
  ajustar por material/ferramenta. Os do exemplo são de **marcação**.

### Rodapé (desligar)
```
N.. M159           ; desliga o par de M158 — NÃO ALTERAR
N.. M163           ; desliga o par de M162 — NÃO ALTERAR
N.. M5             ; para o spindle
N.. G0 Y2840 X51 Z50   ; estaciona (canto/fundo)
N.. M30
N.. M30
%
```

### Regra de ouro
Os M-codes **M158/M162** (liga) e **M159/M163** (desliga) são específicos do JRG
(provável vácuo da mesa + aspiração). **Sempre presentes, sempre em par, nunca
inventados.** Se faltar, a chapa não prende / não aspira.

## A confirmar (para gerar com segurança total)
- **Datum (0,0)** na mesa e referência do **Z-zero** (topo da peça × mesa).
- O que cada M-code (M158/M159/M162/M163) realmente aciona.
- Avanços/rotação reais por operação: **corte passante**, **friso LED**, **V-groove**
  de dobra (ângulo da fresa V), profundidade por passada.
- Diâmetro/tipo das fresas disponíveis (ver `maquinas.md`).

> **Status:** dialeto decodificado de 1 arquivo de **marcação**. Para corte
> passante e cortes especiais, calibrar com mais 1–2 `.tap` reais (um de corte
> passante e um de friso/V-groove) antes de gerar G-code para a máquina.
