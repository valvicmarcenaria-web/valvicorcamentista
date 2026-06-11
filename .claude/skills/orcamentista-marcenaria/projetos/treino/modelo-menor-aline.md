# Treino — Modelo MENOR (cliente aline · cód. 261074)

Projeto real da **Marcenária Diferente** (Ambiente 2). Composição enxuta:
aéreos + balcão com **portas de giro** (sem gavetas/corrediças), portas em
Pau Ferro Natural. Ground truth para calibrar a estimativa de móveis pequenos.

## Chapas (6 no total) — por cor/espessura

| Chapa (cor) | Esp. | Qtd |
|-------------|------|-----|
| Gianduia Linha Trama | 15mm | 3 |
| Gianduia Linha Trama | 6mm | 2 |
| Pau Ferro Natural Linha Cristallo | 15mm | 1 |

> **Aproveitamento (real):** 6mm → 70% e 31%; Gianduia 15mm → 93 · 87 · 77%;
> Pau Ferro 15mm (só portas) → 68%. Mesmo padrão: cor com poucas peças = chapa
> de baixo aproveitamento.

## Fita de borda (22×0,45 +10%)

Gianduia Trama 40m · Pau Ferro Natural Cristallo 60m. (Filetamento-serviço = 85,46m.)

## Ferragens e acessórios

- **Dobradiças:** Reta c/ amortecedor ×14 · Curva c/ amortecedor ×10 → **24**
  (sem corrediças — é tudo porta de giro).
- **Puxador Cava 45° Parcial 15mm:** **1,92 m**.
- **Suportes de prateleira:** Pino Pitão metal (PCT 100) ×1 pacote + VB Zamac
  Uniblock (furo 18mm) ×12.
- **Cantoneira reforçada 3 furos c/ capa:** 8.
- **Dispositivo de montagem:** Cavilha M8×30 (madeira) ×1 pacote.
- **Parafusos:** 4×16mm 1pct · 4×40mm 1pct.
- **Tapa-furo:** Gianduia ×3 · Pau Ferro ×1.

## Serviços de produção

Filetamento **85,46 m** · Rasgo **18,51 m** · Furação **190** · Marcação **108**
· Peças Cortadas **56** · Embalagem **6**.

## Calibração v1 (motor × real) — 11/06/2026

Rodando o núcleo do motor (peça→chapa) sobre as áreas reais:

| Material | Área real | Real | Motor (0,80) | Aproveit. real |
|---|---|---|---|---|
| Gianduia 15mm | 13,06 m² | 3 | 4 | **85,6%** |
| Gianduia 6mm (fundos) | 5,14 m² | 2 | 2 | **50,5%** |
| Pau Ferro 15mm | 3,46 m² | 1 | 1 | 68,0% |
| **Total** | | **6** | **7** | |

**Aprendizado → motor v1.1:**
- Aproveitamento **por espessura**: 15/18mm ≈ **0,82** · 6mm (fundos) ≈ **0,55**
  (peças grandes encaixam mal — sem isso o motor subestima fundos).
- Cor de "cauda" (poucas peças) rende ~68% — cada cor distinta puxa desperdício.
- Fita: real 85,46m de filetamento → 100m comprada (**buffer ≈ ×1,15**, não ×1,10).
- O erro do motor foi **para cima (seguro)**: melhor superestimar 1 chapa que faltar.
