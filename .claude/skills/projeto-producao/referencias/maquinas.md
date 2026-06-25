# Parque de máquinas da Valvic

> Define o que a fábrica **consegue** fazer e seus **limites** — toda regra de
> modelagem e de corte depende disso. Identificado por fotos (jun/2026); specs
> detalhadas a confirmar. Dados estruturados em `dados/maquinas.json`.

## Inventário (v2 — fotos IMG_7611..7615 + specs de fonte)

| Máquina | Marca / modelo | Função |
|---|---|---|
| **Router CNC** | **Raizen Solid TAF** | Nesting (DXF do MD) **e** cortes especiais (Aspire). Mesa 2800×1900, Z200. |
| **Coladeira de borda** | **SCM minimax me 25** | Filetagem automática, fita 0,4mm, avanço 7 m/min. |
| **Esquadrejadeira** | **Raizen RZN 3200P** | Corte esquadrejado; carro ~3200mm. |
| **Tupia / fresadora** | a confirmar | Usinagem de perfis/cavas (cabeçotes de fresa). |
| **Serra de esquadria** | inversor Razi | Destopo; discos de grande diâmetro. |

## Router Raizen Solid TAF (specs da FOLHA DO FABRICANTE — Paulo, 24/06)
- **Área útil:** **Y 2800 × X 1900** × Z 200 mm → **cabe chapa inteira** (1850×2750).
  (Y = eixo longo; correção: antes estava X/Y trocado.)
- **Capacidade:** **35 chapas/dia · 660 chapas/mês** (~26 peças/chapa de MDF).
- **Spindle:** 9 kW (12 CV), 24.000 RPM, cone ISO 30, pinça ER 32.
- **Vácuo:** bomba **11,7 CV**, mesa de **4 câmaras** (acionamento manual).
- **Movimentação:** guias lineares · lubrificação automática centralizada · redutor
  planetário Shimpo · servo Leadshine · **40 m/min** · anticolisão eletrônico.
- **Troca automática de ferramenta:** magazine linear, **10 ferramentas**.
- **Controlador:** **JRG** · post-processador Aspire = **"JRG CNC SOLID TAF"**.
  Dialeto pouco documentado publicamente → o **arquivo `.pp`** é a fonte da
  verdade para gerar G-code com segurança.
- Monobloco em aço, **~1720 kg** · 380V 60Hz trifásica.
- **Na expansão:** vira a máquina de **usinagens especiais** (nesting vai p/ CNC nova).

> **Descoberta importante:** com ATC de 10 ferramentas + Z200, **o nesting e os
> cortes especiais rodam na MESMA máquina**. O "Aspire" não é outra CNC — é o
> software que gera o toolpath especial (friso LED, V-groove, curva) para a
> Raizen. O fluxo normal usa o DXF do MD.

## Coladeira SCM minimax me 25 (specs confirmadas)
- **Fita hoje:** só **0,4mm** melamínica (a máquina aceita 0,4–3mm e tiras de
  madeira até 5mm — não usadas).
- **Painel:** espessura 12–50mm, comprimento mín. 190mm.
- **Avanço:** **7 m/min** → *tempo de passagem* = comprimento da peça ÷ 7 m/min.
- **Cola:** EVA hot-melt (pellets), pote teflonado; temperatura de trabalho
  20–190 °C (operação melamina ~180–190 °C).
- **Funções:** colagem + refile de topo + refile lateral; opcional raspador/escova.
- Produção 20–50 painéis/h; trifásico 220V.

## A confirmar
- **Router:** controlador/CAM que recebe o DXF do MD e o post do Aspire; fresas
  disponíveis (V para dobra, reta para friso LED), raio mínimo de curva.
- **Esquadrejadeira / serra de esquadria:** diâmetro dos discos, altura de corte.
- **Tupia:** marca/modelo e cabeçotes (ex.: cava 45° de puxador).

> **Fluxo de corte:** MD → DXF → **router Raizen Solid TAF** (nesting) ·
> especiais via **Aspire** na mesma Raizen · **filetagem na SCM me 25**.
