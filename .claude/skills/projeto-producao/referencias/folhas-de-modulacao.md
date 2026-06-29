# Folhas de Modulação — família de formulários (a lapidar com o tempo)

Folhas que o **marceneiro preenche à mão** antes de passar pro programador (modelagem).
Cada tipo de módulo tem a sua. Projeto vivo: o Paulo vai ajustando ao longo do tempo.

> ⚠️ Reproduzir: todos os geradores usam caminho RELATIVO ao próprio arquivo
> (`_B=os.path.dirname(os.path.abspath(__file__))`). O logo fica em
> `ferramentas/logo_clean.png` (render limpo do `gerados/logo_valvic_oficial.dxf`).
> Para regenerar um PDF: `python3 ferramentas/gen_folha_XXX.py`.

## Arquivos (em `ferramentas/`)
| Módulo | Gerador | PDF | Layout |
|---|---|---|---|
| Armário inferior | `gen_folha_4up.py` | `folha_modulacao_4up.pdf` | 4 por folha |
| Torre (compacta) | `gen_folha_torre_4up.py` | `folha_modulacao_torre_4up.pdf` | 4 por folha |
| Torre (espaçosa) | `gen_folha_torre_2up.py` | `folha_modulacao_torre_2up.pdf` | 2 por folha |
| Painel | `gen_folha_painel_2up.py` | `folha_modulacao_painel_2up.pdf` | 2 por folha |
| Armário de canto | `gen_folha_canto_2up.py` | `folha_modulacao_canto_2up.pdf` | 2 por folha |
| (legado) Folha única grande | `gen_folha_modulacao.py` | `folha_modulacao_marceneiro.pdf` | 1 por folha |
| Checklist interativo (web) | — | `checklist-modulacao.html` | HTML c/ abas |

## Padrão visual (convenções)
- **Cabeçalho:** logo Valvic (lw=36mm no 2-up / 28mm no 4-up) + título "FOLHA DE
  MODULAÇÃO — <TIPO>" (curto: TORRE, PAINEL, CANTO) à direita; depois Pedido / Módulo.
- **Helpers** nos geradores: `chk()` checkbox, `fline()` linha de preenchimento,
  `lab()` rótulo negrito, `unit()` "mm", `quad()` face 3D.
- **2-up** (preferido p/ legibilidade): `cw,ch=W/2,H` (lado a lado, folha inteira na
  altura); fontes maiores (rótulo 7.6 / checkbox 7.0); espaçamento `g≈14mm`; guia de
  corte tracejada vertical no meio.
- **4-up:** `cw,ch=W/2,H/2`; fontes 6.8/6.5; `g≈8.6mm`; guias de corte em cruz.
- Largura útil de cada cartão ≈ 93mm (p=6mm de margem) — cuidado com linhas de muitos
  checkboxes (Porta, Acabamento) que chegam perto da borda.

## Desenho por tipo
- **Inferior / Torre:** caixa 3D isométrica ABERTA, paredes finas (contorno externo +
  interno deslocado pela espessura) = "parece MDF". Torre = caixa alta vertical.
- **Painel:** **chapa de MDF LISA** (retângulo plano, tom MDF) — o marceneiro desenha a
  ripa à mão. (Versão antiga tinha ripas desenhadas; Paulo preferiu liso e maior.)
- **Canto:** **planta (vista de cima) em "L"** com hachura nas 2 paredes (topo+esquerda)
  e diagonal tracejada (laranja) indicando a opção de frente diagonal.

## Campos por folha (estado atual)
**Inferior (4up):** Alt/Larg/Prof · Tamponam.(L,C,☐15☐6☐18) · Acabam.(idem) ·
Porta(linha + ☐15☐18☐Provençal☐Vidro) · Fundo(☐Sim☐Não)+LED(☐Sim☐Não) ·
Prat/Div(☐15☐18) · Puxador · Ferragens · Obs(2 linhas).

**Torre (2up — a mais completa):** Alt/Larg/Prof · Tamponam. · Acabam. ·
Base(☐Sim☐Não)+Recuo(☐Sim☐Não)+mm · Acab. base(linha) · Porta(linha + ☐15☐18☐
Provençal☐Vidro☐Correr) · Vão Forno(mm) · Vão Microond.(mm) · Gaveteiro(☐Sim☐Não +
Qtd gav.) · Sapateira(☐Sim☐Não + Qtd) · Fundo+LED · Prat/Div(☐15☐18 + Qtd) ·
Puxador · Ferragens · Obs.
  - Torre **4up** = versão compacta anterior (sem Base; Sapateira ainda dividia linha
    com Fundo; sem LED). Quando estabilizar, alinhar as duas.

**Painel (2up):** Alt/Larg/Esp. · Ripado(☐Sim☐Não) · Larg.ripa/Friso/Prof.ripa (lado a
lado, mm) · Acabam.(☐Lâmina☐Melamínico☐Laca) · Material(linha) · Rodapé(☐Alumínio☐MDF
Ultra + Alt + Recuo) · Arremate(☐Sim☐Não + Alt + Recuo) · Encaixe/Fixação(linha) ·
Usinagem esp.(☐Sim☐Não) · Qual usinagem(linha) · LED(☐Sim☐Não) · Obs.
  - Conhecimento de painel ripado em `referencias/painel-ripado.md`.

**Canto (2up):** Altura/Profund. · Lado A/Lado B · Tipo(☐Reto(L)☐Diagonal☐Giratório) ·
Tamponam. · Acabam. · Porta(idem torre) · Prat/Div(☐15☐18 + Qtd) · Fundo+LED ·
Puxador · Ferragens · Obs.

## Preferências do Paulo já aprendidas (não repetir os erros)
- Desenho **simples, não "embolado"**; sem rótulos "lateral/testeira" escritos.
- Representação **fina** (parede de MDF), nada de traço grosso.
- Caber vários por folha (começou 4up); depois pediu **2up** p/ desenho maior + mais
  espaço entre campos (caminho atual p/ os tipos novos).
- Painel: **liso e grande** (ele desenha a ripa). Sem Fundo, sem Ferragens.
- Fala em **CM** quando dá medida (atenção ao converter).

## Pendências / próximos passos
- [ ] Folha de **armário superior / aéreo** (no padrão 2up).
- [ ] Folha de **gaveteiro** (nº e altura de cada gaveta; corrediça oculta + folga 1,8).
- [ ] Propagar **Base/LED** e revisão p/ inferior 4up e torre 4up (alinhar com a 2up).
- [ ] Eventual: trocar "Encaixe/Fixação" e "Tipo de canto" por checkboxes; campo de
      medida da frente diagonal no canto.
- [ ] (Ideia do Paulo) arte mais bonita no padrão Valvic com a Lavinia.
- 🔄 **Método:** continuar lapidando essas folhas com o tempo, conforme o uso no chão.
