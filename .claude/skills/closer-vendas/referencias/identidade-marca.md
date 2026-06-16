# Identidade de marca Valvic (inferida — não há Brand Office formal)

> Jonathan (designer) não mantém um manual de marca. Esta é a identidade
> **consolidada a partir das propostas reais** (mestre: `proposta_bruna_ferreira`)
> e do Termo de Garantia Gold. Serve como brand system de referência do Vitor até
> existir um manual oficial.

## Logo
- Wordmark **"Valvic"** em caixa baixa, customizado, preto (versão sobre claro).
- Motivo gráfico: **estrelas/sparkles de 4 pontas** (usado na capa).

## Paleta (cravada dos arquivos)
| Uso | Cor |
|---|---|
| Dourado marca (faixa capa, títulos) | mostarda **#E0A521** (aprox.) |
| Dourado documento/detalhe | **#D4AF37** / **#B8860B** |
| Quase-preto (texto, rodapé) | **#1A1A1A** |
| Creme/fundo nobre | **#FDF6E3** |
| Texto sobre dourado | grafite escuro / branco |
| Fundo geral | branco |

## Tipografia (aproximação — confirmar fontes exatas com Jonathan)
- **Nome do cliente / display:** serifa elegante (estilo Cormorant Garamond / Playfair).
- **Títulos de seção:** sans geométrica em caixa alta (estilo Poppins / Century Gothic).
- **Corpo:** sans limpa e legível.
- Nas ferramentas internas espelhamos com **Cormorant Garamond + DM Sans** (Google Fonts).

## Tom visual
Premium, limpo, fotográfico. Render/foto ocupa grande área. Faixas douradas
marcam seções. Muito respiro. Páginas A4 retrato.

---

# Proposta-mestre (estrutura oficial — base: Bruna Ferreira)

Projeto completo de casa (multi-ambiente). Estrutura de 6+ páginas:

1. **Capa** — "PROPOSTA ESPECIAL PARA" + **[Nome do cliente]** (serifa) sobre faixa
   dourada + sparkles; render(s) grande(s); logo Valvic no rodapé.
2. **Quem somos** — foto dos sócios + headline "Não desenvolvemos apenas móveis,
   mas soluções…" + texto institucional + 5 diferenciais (faixa dourada com ícones:
   ética, qualidade, foco, inovação, relacionamento).
3. **Configuração técnica dos móveis** — grid 3×3 de cards (Corrediças, Dobradiças,
   Articuladores, Sist. deslizante roupeiro, Sist. portas de passagem, Iluminação,
   Espessuras, Laminação, Suportes/montagem) — feature → benefício, com foto.
4. **Cases** — 3 cases (foto + storytelling de desafio técnico).
5. **Linha do tempo do projeto** (8 etapas) + "Por que a Valvic?" + fotos da equipe.
6. **Investimento** — tabela `serviço | descrição | investimento` por ambiente;
   **GARANTIA** (selo) + **INVESTIMENTO TOTAL** + prazo + validade + formas de
   pagamento (escada de antecipação com desconto).

## Campos de autofill (o que o Vitor injeta) — mapa para o template
- `cliente_nome` (capa) · `render_capa` (+ secundários)
- `conexao_texto` (parágrafo personalizado do projeto — MELHORIA: hoje é genérico)
- `itens[]` = linhas da tabela: { ambiente, descrição (em valor), investimento }
- `investimento_total`
- `garantia_tempo` (selo) — **derivado da ferragem** (ver garantia.md)
- `prazo` · `validade` (por perfil) · `condicoes[]` (escada de pagamento)
- A seção técnica/cases/linha do tempo é **fixa** (muda pouco); personalização entra
  na capa, conexão e tabela.

## Melhorias a aplicar no template (já acordadas)
1. QA de nome em todas as páginas (já vazou "Vargas Decor" em outra proposta).
2. Garantia dinâmica (não fixar "10 anos" no template).
3. Corrigir typos técnicos: "Premiun"→Premium, "harth"/"Hardt"→**Hardt**.
4. Abrir a pág. 2 no cliente (conexão) antes do institucional.
5. Versões/ambientes nomeados por valor; ancorar do maior para o menor.
6. Validade por perfil (premium 5–7 dias / rápido 48h).

## Ativos
- **Master:** `proposta_bruna_ferreira` (Canva).
- **Logo/fontes exatas:** não há manual — confirmar fontes com Jonathan quando possível.

## Acervo de imagens de serviços (Drive) — fonte para as propostas

Pasta-raiz do acervo (fotos reais de projetos executados, para compor propostas):
**https://drive.google.com/drive/folders/1eUnLV1GsOo4X5SSxNzbVLVfL4Wgjf2OM**
(ID `1eUnLV1GsOo4X5SSxNzbVLVfL4Wgjf2OM`)

Subpastas úteis (ambiente → onde buscar):
- **Home office / escritório:** `leyde_contagem` (apto Contagem, ~20 fotos), `Escritório Marco Túlio`, `Mesas corporativas`, `marco_tulio`
- **Equipe / institucional:** `Fotos _equipe`, `insititucionais`, `Bastidores`
- **Casas completas (cases):** `casa_richard_fazendas_da_serra`, `Casa graciane`, etc.

> Imagens são `image/jpeg`. O `read_file_content` **não descreve** fotos (volta vazio);
> para escolher visualmente, baixar via `download_file_content` (base64) e abrir, ou
> pedir ao Jonathan o nº da foto. Para inserir no Canva: `upload-asset-from-url` com
> URL direta `https://drive.google.com/uc?export=download&id=<FILE_ID>` → `update_fill`.
