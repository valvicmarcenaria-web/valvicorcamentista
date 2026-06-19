# Projeto: Condomínio Ed. Luxemburgo — Reforma dos Halls

> Reforma das modificações dos halls. Arq. **Rosana Miraglia**. Base: PDF
> `orcamento_igor` (10 pranchas: halls 2 aptos, halls 4 aptos, hall social A/B).
> Orçado em jun/2026 (Lavinia).

## 1. Demanda

- **Ambientes:** Hall de 2 apartamentos · Hall de 4 apartamentos · Hall social
  (Bloco A + Bloco B).
- **Descrição:** revestimento de paredes em **MDF amadeirado** (painéis), com
  portas de giro embutidas para acesso a quadros (imã de toque), frisos, fita de
  LED embutida; no hall social, **molduras dos espelhos** em amadeirado com
  espelho colado em MDF.
- **Acabamento:** MDF **melamínico fosco amadeirado** "a escolher" (painéis 15mm;
  moldura do social 18mm).
- **Decisões do cliente (Jonathan):** preço **unitário** (1 hall de cada tipo —
  os halls 2/4 apt se repetem por pavimento); **sem RT** (condomínio direto);
  **espelhos como linha separada com MC 37%**; **não orçar madeira maciça**
  (banco/aparador em madeira de demolição ficam fora); **MC alvo 37%**.

### Escopo — o que é e o que NÃO é Valvic

| ✅ Marcenaria Valvic | 🪞 À parte | ❌ Fora (outros fornecedores) |
|---|---|---|
| Painéis de revestimento em MDF amadeirado | Espelhos cristal prata | Granito preto S. Gabriel (pórtico, molduras, rodapé) |
| Portas de giro embutidas (quadros) + imã de toque | | Portas prontas pintadas cinza (apto/elevador) |
| Frisos (usinados CNC) | | Papel de parede, pintura, porcelanato 90×90 |
| Recuo + fita de LED embutida no painel | | Rodapé poliestireno preto, forro de gesso/sanca |
| Molduras dos espelhos (amadeirado) + MDF de fundo | | Porta blindex, arandelas, vidros fixos existentes |
| | | **Banco/aparador em madeira de demolição** (pedido: sem maciça) |

## 2. Quantitativo (por hall)

Áreas de painel obtidas por **medição de pixel** das elevações em escala 1:20
(isolando a cor do MDF amadeirado e convertendo px→m² com fator 1:20 @ 300dpi).
Conferido contra cálculo manual (parede dos elevadores do hall 2 apt = ~4,5 m²).

| Hall | Paredes revestidas | Área painel amadeirado | Portas de acesso |
|------|--------------------|------------------------|------------------|
| 2 aptos | parede dos elevadores + parede c/ painel de quadros | **~10,2 m²** | 2 |
| 4 aptos | idem, hall mais longo (+ retorno) | **~14 m²** | 3 |
| Social A+B | molduras dos espelhos (A: 152×225 + B ~2,5 m²) | molduras ~2 m² | — |

## 3. Quantitativo de chapas e insumos

| Hall | Amadeirado (mel. fosco) | Branco 15mm | Fita cor | Filetagem | LED | Ferragens |
|------|-------------------------|-------------|----------|-----------|-----|-----------|
| 2 aptos | 3 ch. 15mm | 1 ch. | ~25 m | ~25 m | ~6 m + sensor | 4 dobr. Sensys + 2 imã toque |
| 4 aptos | 4 ch. 15mm | 1,5 ch. | ~35 m | ~35 m | ~10 m + sensor | 6 dobr. Sensys + 3 imã toque |
| Social A+B | 1 ch. 18mm (moldura) | 2 ch. (fundo espelho) | ~30 m | ~30 m | — | — |

Espelho cristal prata (à parte): **~6 m²** (A 3,4 + B ~2,5 — *confirmar em obra*).

## 4. Composição de custo (custo de compra)

| | Hall 2 apt | Hall 4 apt | Social A+B | Espelhos |
|---|---:|---:|---:|---:|
| Material | 3.197 | 4.655 | 1.320 | 3.600 |
| Logística | 400 | 500 | 400 | — |
| Visitas | 250 | 250 | 250 | — |
| **Custo direto (fixedR)** | **3.847** | **5.405** | **1.970** | **3.600** |

## 5. Preço final — MC 37%, sem RT

Fórmula da planilha de validação: `Inv = fixedR / (1 − a − liqF·b − mc)`,
com `a`=18% (NF4+parc8+vend3+erro2+serra0,5+manut0,5), `liqF`=0,88,
`b`=4,3% (comissão produção; RT=0), `mc`=0,37 → divisor **0,41216**.

| Item | Preço (sem RT) | (referência com RT 10%) |
|------|---------------:|------------------------:|
| Hall 2 aptos | **R$ 9.334** | R$ 11.868 |
| Hall 4 aptos | **R$ 13.114** | R$ 16.674 |
| Hall social A+B (marcenaria) | **R$ 4.780** | R$ 6.077 |
| Espelhos (linha separada) | **R$ 8.734** | R$ 11.106 |
| **Total de 1 de cada + espelhos** | **R$ 35.962** | R$ 45.725 |

> MC verificada = **37,0%** em cada item e no total.
> **Para o total do prédio:** multiplicar hall 2 apt e hall 4 apt pelo nº de
> pavimentos de cada tipo; hall social é único (térreo A+B).

## 6. Notas de metodologia / pendências

- **Pré-medição.** Várias cotas no projeto são "confirmar no local"; fechar o
  m² de painel e de espelho na conferência em obra (erra-se para cima).
- **Frisos** são usinados na CNC — sem material extra, custo de corte hoje
  dentro da margem operacional (driver de tempo; reavaliar se vierem muitos).
- **LED embutido** incluído como Valvic (fita+perfil no recuo do painel); sai da
  conta se o ponto/fita ficar com o eletricista. A "entrada de energia" é do
  eletricista.
- **Repetição por pavimento** é o maior multiplicador: o preço aqui é por UM
  hall de cada tipo.
- Artefato app: `orcamento-ed-luxemburgo-halls.json` (carregável no
  `validacao-orcamento.html`; números autoritativos são os deste .md).
