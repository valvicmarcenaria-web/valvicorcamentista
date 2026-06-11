# Notas do Marcos — aprendizados da planilha real (teste Camila)

Anotações tiradas da planilha de validação atualizada (`teste_lavinea`, projeto
Closet da Camila = Roupeiro em L + Ilha). Servem para precificar com cada vez
mais eficiência.

## Estrutura da planilha (modelo de validação)

```
Investimento bruto R$   = preço de venda (input)
Inv. líquido            = Inv − NF − Parcelamento          (base de comissão prod. e RT)
Custo total             = Operacional + Venda + Material + Margem de erro (+ Terceirizados*)
MC R$                   = Investimento − Custo total
MC %                    = MC / Investimento                → IDEAL 35–40%
```

## Percentuais REAIS desta versão da planilha

| Encargo                 | %        | Base            | Obs |
|-------------------------|----------|-----------------|-----|
| Comissão produção       | **4,3%** | líquido         | programador 0,8% + coordenador 1,0% + marceneiros 2,5% |
| Desgaste serra/fresa    | 0,5%     | bruto           | |
| Manutenção máquinas     | 0,5%     | bruto           | |
| Comissão vendedor       | **3%**   | bruto           | (às vezes 5%) |
| Nota fiscal             | **4%**   | bruto           | nesta versão veio 4% (antes 7%) — confirmar caso a caso |
| RT                      | **10%**  | líquido         | parceiro/arquiteto |
| Parcelamento máquina    | **8%**   | bruto           | vira desconto à vista |
| Margem de erro          | **2%**   | bruto           | |
| Visitas                 | R$ 250   | fixo            | |

> Fórmula de preço p/ MC alvo:
> `Inv = fixedR / (1 − a − liqF·b − mc)`
> onde `fixedR` = material + terceirizados + logística + visitas;
> `a` = soma dos % sobre o bruto (NF+parc+vend+erro+serra+manut);
> `liqF` = (1 − NF − parc); `b` = % sobre o líquido (com. produção + RT);
> `mc` = MC alvo. (Implementada no app `validacao-orcamento.html`.)

## Catálogo — divergências e correções flagradas

- **RO65 (Rometal):** custo correto **R$ 250** (kit unitário). Na seção
  Roupeiro da planilha veio **R$ 60** (provável erro) — corrigido no preenchido.
- **Custo material do topo (B17)** só somava o Roupeiro (B52); a Ilha (B191)
  ficava de fora. **Corrigido para `=B52+B191`** no arquivo preenchido.
- **Terceirizados** (vidraceiro/serralheiro/pintor/estofador/laqueamento) estão
  listados mas **não tinham fórmula somando ao custo total**. No app eles entram
  como categoria própria que **soma** ao custo. Confirmar com Jonathan se quer
  manter assim na planilha.
- **Colagem (filetagem)** aparece como linha de material à parte da fita:
  máquina **R$ 2,5/m** e manual **R$ 4/m** — confirma o que treinamos com a
  Lavinia (custo de aplicação ≠ custo da fita-insumo).
- Puxador **Especial 1 = "Traço Metal/Couro Enlevo" R$ 60** — já está na planilha.
- **Desempenador**: sobrepor (par) R$ 100 · embutido (par) R$ 150.
- **Multi** (rack/suspenso): 2 portas R$ 300 · 3 portas R$ 380 · trilho 3m R$ 200.

## Itens da planilha que viram TERCEIRIZADO (não material)

- Estrutura de serralheria / base metalon laca champagne → **Serralheiro + Pintor**.
- Bandeja e divisória forrada em veludo → **Estofador**.
- Visor/portas de vidro, espelho → **Vidraceiro** (ou material em m² se comprado
  pronto). Laqueamento de peça lisa → **Laqueamento/Pintor**.

> **Estado:** notas v1 da planilha real. Calibrar contra o preenchido do Jonathan.
