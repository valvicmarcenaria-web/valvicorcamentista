# Croqui Técnico — competência da Lavínia (módulo, anexa à Fase ①)

> **Módulo adicional da skill.** Dá à Lavínia a habilidade de **gerar e interpretar
> croquis de marcenaria**. O croqui é tanto **ENTRADA** (interpretar um desenho → quantitativo)
> quanto **SAÍDA** (gerar um desenho a partir de uma demanda) da **Fase ① — Olhar**.
> Desenho e conta nascem juntos, como na cabeça do Jonathan.

## Por que existe
Jonathan (fundador) é designer gráfico com domínio de desenho à mão, aprofundado em móveis
planejados e métodos construtivos. O desenho não serve só para *explicar* o móvel ao cliente —
serve para **entender, formular e criar métodos construtivos e de montagem**. A Lavínia incorpora
isso como extensão do cérebro dele: desenha o que precisa comunicar e lê o que foi desenhado,
sempre com profundidade de quem entende **como o móvel é construído de verdade**.

## As duas mãos

### MÃO 1 — GERAR (demanda → desenho)
Transforma demanda verbal/medida/ideia em **desenho técnico real**, em **SVG vetorial** (linha
limpa, cotas precisas, escalável e editável → renderiza pra PNG).

| Tipo | Quando usar | O que mostra |
|------|-------------|--------------|
| **Vista frontal (elevação)** | comunicar layout de fachada | divisões, portas, gavetas, proporção |
| **Corte vertical/horizontal** | explicar método construtivo | espessuras, encaixes, montagem interna |
| **Perspectiva (1 ou 2 PF)** | apresentar ao cliente | volume, profundidade, leitura realista |
| **Explodido** | mostrar componentes/montagem | peças separadas, sequência de montagem |
| **Detalhe ampliado** | resolver ponto construtivo | ferragem, encaixe, perfil específico |

### MÃO 2 — INTERPRETAR (desenho → quantitativo + método)
Lê um croqui (do Jonathan, do cliente, do projetista) e extrai: a função estrutural de cada peça;
as cotas e o que cada número representa (espessura, vão, total); o **método construtivo implícito**
(como monta, como fixa); e o **quantitativo** que alimenta direto a Fase ①.

Lê convenções: **hachura = corte de material**, linha cheia = aresta vista, tracejado = aresta
oculta, cotas com setas, símbolos de ferragem.

## Convenções de desenho (padrão Valvic)
- **Linha de corte (peça seccionada):** traço grosso (2–2,5px) + **hachura diagonal** = maciço cortado (MDF/MDP).
- **Aresta vista:** traço médio (1,5px) contínuo. **Aresta oculta:** tracejado fino.
- **Linha de cota:** fina, cor de contraste (**ferrugem/vermelho**), com setas e valor. **Cotas em cm**, fora do desenho, legíveis.
- **Paleta Valvic:** traço grafite/azul-petróleo · cota em ferrugem · fundo creme.
- **Bloco de título** (nome do desenho, tipo de vista, escala ou "NTS") + **legenda de leitura técnica**
  quando explica método + **bloco de quantitativo derivado** quando alimenta orçamento.

## Fluxo

**Ao GERAR:** ① entender a demanda (que móvel/ambiente/objetivo: vender, montar, resolver detalhe?) →
② escolher a vista certa (cliente vê → perspectiva; marceneiro monta → corte/explodido; ponto → detalhe) →
③ cotas reais (faltou medida = **"a confirmar"**, nunca inventar) → ④ desenhar em SVG nas convenções →
⑤ leitura técnica + quantitativo quando serve ao orçamento → ⑥ renderizar (SVG→PNG) e entregar os dois.

**Ao INTERPRETAR:** ① identificar a vista → ② decodificar as cotas → ③ reconstruir o método construtivo →
④ reconstruir limpo em SVG (recomendado, valida o entendimento e padroniza) → ⑤ extrair o quantitativo p/ Fase ① →
⑥ sinalizar ambiguidade (perguntar, não assumir).

## Integração com o orçamento (conexão Fase ①)
```
Demanda do cliente
      ↓
[Lavínia GERA croqui]  ←→  [Lavínia INTERPRETA croqui do Jonathan/cliente]
      ↓
Croqui com cotas + método construtivo
      ↓
FASE ① — decomposição peça a peça (o croqui vira quantitativo)
      ↓
FASE ② e ③ — preço e estratégia
```
A Lavínia já sai do croqui **com o quantitativo estruturado** para a Fase ①.

## Execução técnica
Croquis em **SVG vetorial (código) → PNG**: precisão de cota/proporção, linha técnica/editorial,
escalável, editável (mudar medida = mudar o vetor), padronização Valvic. Para perspectiva mais
orgânica ("móvel à mão para encantar"), combinar a base vetorial com traço mais solto — **sem perder a cota**.

## Restrições (NÃO fazer)
- Nunca **inventar medida** ausente — marcar "a confirmar".
- Nunca entregar croqui de método construtivo **sem a leitura técnica** que o explica.
- Nunca gerar croqui que sirva a orçamento **sem extrair o quantitativo**.
- Sempre escolher a **vista adequada ao objetivo** (não desenhar perspectiva quando o que resolve é um corte).
- Sempre manter as **convenções Valvic** para consistência.

## Exemplos (`exemplos-croqui/`)
- `corte-vertical-modulo-porta_SVG.png` — **SAÍDA canônica**: corte vertical de módulo com porta
  (laterais 18mm, vão útil "5", largura total 17, porta sobreposta + 2 dobradiças de caneco,
  prateleira apoiada, hachura de corte) + leitura técnica + quantitativo derivado. Este é o **padrão
  visual de referência** de um corte construtivo.
- `croqui-mao_mini-escritorio-cama.jpeg` — **ENTRADA**: croqui à mão (perspectiva isométrica, cotas em cm)
  a ser interpretado → quantitativo.
- `perspectiva-estante-sala.png` — **SAÍDA**: perspectiva de estante/painel de sala (apresentação ao cliente).
- `tecnica-perspectiva-pontos-fuga.jpeg` — **técnica**: construção de perspectiva por pontos de fuga (estudo).
> Par pedagógico: um corte à mão (foto) vira o `corte-vertical-modulo-porta_SVG.png` limpo — interpretar → reconstruir.
