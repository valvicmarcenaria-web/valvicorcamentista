# Home office sob a escada — Lirriet Libório

**Lead** · WhatsApp 31/07/2026, 13:21 · primeiro contato
**Entrada:** um moodboard ("PROJETO DEBAIXO DA ESCADA"), com render, foto do ANTES e
paleta. **Nenhuma cota.** Não é executivo.
**Motor:** `corte-escada-lirriet.py`

## O que o moodboard pede

> Home office funcional · prateleiras com iluminação · organização e aproveitamento ·
> estilo moderno e acolhedor
> Paleta: madeira clara (carvalho) · bege/areia · off-white · preto fosco · ripado amadeirado

Escopo de marcenaria lido no render:

| # | Item | Observação |
|---|---|---|
| 1 | Painel de fundo amadeirado | acompanha a diagonal da escada |
| 2 | Bancada com engrossamento de borda | h 75 · prof 55 |
| 3 | Gaveteiro de 3 gavetas | puxador cava usinado — não há puxador aparente no render |
| 4 | Painel ripado fechando a frente sob a bancada | ripas de 2 cm |
| 5 | 2 prateleiras com LED embutido em cava | escalonadas pela escada |
| 6 | Lateral direita | fecha o vão junto à porta |
| 7 | 3 linhas de LED | sob cada prateleira + sob a bancada |

Fora do escopo (do moodboard, mas não é marcenaria): cadeira, plantas, objetos de
decoração, pintura das paredes.

## ⚠️ O problema: não há uma medida

Escalei o render por duas referências confiáveis:

- **altura da bancada 75 cm** — padrão de projeto, e confere no render;
- **porta ao lado 210 cm** — no render, o topo da porta coincide exatamente com o
  ponto em que a escada encontra a parede → **altura máxima do móvel 210 cm**.

Com isso a vertical toda fecha: prateleiras a 116 e 161 cm, e a inclinação da escada
dá 0,719 cm de queda por cm na horizontal.

**O comprimento da bancada não fecha.** Dois caminhos independentes divergem:

| método | resultado |
|---|--:|
| pela largura da folha da porta (90 cm) | ~236 cm |
| pela inclinação da escada × altura de 210 cm | ~268 cm |

A diferença é distorção de perspectiva do render — o ponto de fuga está à direita, e
a parte esquerda da cena está comprimida. **Não dá para cravar**, então o motor roda a
mesma composição em 200 / 250 / 300 cm.

## Achado de produção

**Acima de 275 cm a bancada não sai de uma chapa.** A chapa tem 2,75 m; uma bancada de
3 m precisa de emenda ou de chapa de comprimento especial. É por isso que o custo dá um
salto entre 250 e 300 cm (mais uma chapa inteira de 15 mm), e não sobe de forma suave.
Vale avisar a cliente: **se o vão der até 2,75 m, o tampo é inteiriço.**

## Números — MC 37%

| bancada | ASSINADA custo | investimento | à vista | ENXUTA custo | investimento | à vista |
|---|--:|--:|--:|--:|--:|--:|
| 200 cm | 4.527 | 10.500 | 9.500 | 3.520 | 8.200 | 7.400 |
| **250 cm** | **4.730** | **11.000** | **9.900** | **4.062** | **9.400** | **8.500** |
| 300 cm | 5.985 | 13.900 | 12.500 | 4.603 | 10.700 | 9.600 |

**ENXUTA** = painel frontal liso no lugar do ripado + LED só nas duas prateleiras
(sai a linha sob a bancada). No comprimento de referência vale **R$ 1.600 (15%)**.

### Onde está o custo do ripado

51 ripas de 2 × 65 cm consomem **67 m de fita** — quase três vezes a fita de todo o
resto do móvel junto (24 m). E ripa de 2 cm não entra em pé na coladeira: a filetagem
é **manual, R$ 4/m** contra R$ 2,50/m na máquina. O ripado quase não pesa em chapa;
pesa em hora de bancada. É o ponto caro clássico, e o alvo certo da versão enxuta.

## Medidas a pedir para a Lirriet

Com estas cinco o orçamento vira exato:

1. **Comprimento do vão** sob a escada, no chão, da parede do fundo até onde a escada
   encosta no piso — é a medida que falta de verdade.
2. **Altura livre** no ponto mais alto (junto à porta), do piso à laje da escada.
3. **Profundidade** disponível (da parede do fundo até a frente do vão).
4. **Largura da folha da porta** ao lado — fecha a conferência de escala do render.
5. **Foto do vão vazio**, de frente e com uma trena aberta apoiada no chão.

## Pendências

- Situação de caixa não perguntada — MC 37% é o padrão; caixa apertado aceitaria menos.
- Confirmar se a cliente quer **corrediça oculta com amortecimento** (orçada, Hardt
  R$ 70/par) ou telescópica comum (R$ 40/par) — diferença pequena no total.
- Confirmar a **cor exata** do amadeirado (a paleta diz "madeira clara / carvalho";
  o custo de chapa de cor é o mesmo em qualquer padrão da linha fosca).
