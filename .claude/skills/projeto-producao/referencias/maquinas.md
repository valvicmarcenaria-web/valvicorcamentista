# Parque de máquinas da Valvic

> Define o que a fábrica **consegue** fazer e seus **limites** — toda regra de
> modelagem e de corte depende disso. Identificado por fotos (jun/2026); specs
> detalhadas a confirmar. Dados estruturados em `dados/maquinas.json`.

## Inventário (v1 — identificado por fotos IMG_7611..7615)

| Máquina | Marca / modelo | Função |
|---|---|---|
| **Router CNC de nesting** | Raizen (modelo a confirmar) | Corta as chapas a partir dos **DXF do MD** (1 por chapa). Mesa a vácuo + gantry. |
| **Coladeira de borda** | **SCM me 25** | Filetagem automática (~R$2,5/m). |
| **Esquadrejadeira** | **Raizen RZN 3200P** | Corte esquadrejado; carro ~3200mm. |
| **Tupia / fresadora** | a confirmar | Usinagem de perfis/cavas (cabeçotes de fresa). |
| **Serra de esquadria** | inversor Razi | Destopo; discos de grande diâmetro. |
| **CNC via Aspire** | a confirmar (mesmo router?) | Frisos de LED, friso de dobra (V-groove), curvas. |

## A confirmar (specs que governam modelagem e corte)
- **Router CNC:** modelo, **área útil da mesa**, software de comando (entra o
  DXF do MD), potência/ferramentas do spindle, espessura máx.
- **Aspire:** roda no mesmo router Raizen ou em outra máquina? Raio mínimo de
  curva, fresas disponíveis (V para dobra, reta para friso LED).
- **Coladeira SCM me 25:** espessura de fita suportada; faz pré-fresa/raspagem/lixa?
- **Esquadrejadeira / serra de esquadria:** diâmetro dos discos, altura de corte.
- **Tupia:** marca/modelo e cabeçotes (ex.: cava 45° de puxador).

> **Implicação para a skill:** o fluxo de corte é **MD → DXF → router Raizen**
> (nesting) e **filetagem na SCM me 25**. O Aspire é o track paralelo de cortes
> especiais (Degrau 4).
