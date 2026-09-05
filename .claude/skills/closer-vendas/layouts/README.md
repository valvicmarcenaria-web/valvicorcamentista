# Linha Family — layout de proposta (referência)

> Layout-referência nascido da proposta real da **Samara — Quarto dos Irmãos**
> (jun/2026). É a opção de proposta para **projetos residenciais / perfil
> consultivo** (baixo-médio, indicação de parceiro), e resolve o que o
> template-mestre do Canva **não** comporta: **comparação de duas versões num só
> arquivo** e **números redondos**.

## Quando usar a Linha Family
- Projeto residencial/familiar (quarto, dormitório infantil, ambiente único ou poucos).
- Cliente de perfil **consultivo/caloroso** (não premium-institucional).
- Sempre que precisar mostrar **duas versões lado a lado** (Essencial × Conforto).
- Quando o cliente reduz o escopo (ex.: só bancada + guarda-roupa) — é só tirar linhas.

> Para casa inteira / premium com cases e linha do tempo, usar o template Canva
> (`proposta-e-identidade.md` → MODELO `DAHMsJxsuhE`). A Family é o irmão enxuto e
> caloroso, gerado em HTML→PDF (sem depender de Canva pago).

## Arquivos
| Arquivo | O que é |
|---|---|
| `linha-family.html` | **Template** genérico com `{{CAMPOS}}` — copiar e preencher. |
| `../propostas/proposta-samara.html` | Exemplo real (4 ambientes, 2 versões). |
| `../propostas/proposta-samara-bancada-guardaroupa.html` | Exemplo real (escopo reduzido). |
| `../propostas/Proposta-Samara-*.pdf` | PDFs gerados (referência visual). |

## Estrutura (4 páginas A4)
1. **Capa** — faixa mostarda topo/base, sparkles, nome do cliente (serifa grande), subtítulo, wordmark `valvic`.
2. **Conexão + O que entregamos** — 2 parágrafos personalizados do projeto + cards por ambiente (feature→valor; vende EXECUÇÃO, não o projeto).
3. **Investimento** — tabela por ambiente (Linha Essencial) + **duas versões** (Conforto recomendada × Essencial) + prazo/validade/atendimento.
4. **Pagamento (escada) + Garantia + CTA**.

## Identidade (tokens)
- Mostarda `#E0A521` · Ouro `#B8860B` · Creme `#FDF6E3` · Preto `#1A1A1A`.
- Display/títulos em **serifa** (Georgia/Cormorant); corpo em **sans**. Muito respiro.

## Regras de conteúdo (não negociáveis)
- **Números redondos** — nada de quebrado (arredondar à centena/milhar).
- **Duas versões com spread proporcional ao benefício** — a diferença de preço tem
  que acompanhar o salto de garantia/ferragem (no piloto Samara: gap **R$ 3.000**
  para 2→5 anos + Hardt soft-close). Spread pequeno demais desvaloriza o upsell.
- **Garantia derivada da ferragem** (telescópica/padrão 2 anos · Hardt 5 · Hettich 10 ·
  Blum vitalícia — ver `../referencias/garantia.md`).
- **Prazo SEMPRE confirmado** com o Jonathan antes de cravar.
- **QA** (nome em todas as páginas, sem cliente/marca antigos, termos técnicos corretos) —
  ver checklist no `SKILL.md`.

## Como gerar o PDF
```bash
pip install weasyprint
python3 -c "from weasyprint import HTML; HTML('linha-family.html').write_pdf('Proposta.pdf')"
```
Conferir visualmente (4 páginas) antes de enviar. Quebra de página: pagamento+CTA
ficam na pág. 4 (a seção de pagamento é uma `.page` própria — não deixar título órfão).
