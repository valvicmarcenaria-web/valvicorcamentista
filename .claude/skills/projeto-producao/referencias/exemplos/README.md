# Exemplos de campo — biblioteca de aprendizado do Téo

> Aqui mora a **verdade de campo**: arquivos reais do Aspire/CNC que o **Paulo**
> manda. Cada caso vira uma **regra escrita** (no `aspire-cortes-especiais.md`,
> `modelo-construtivo.md` ou `dobra-de-mdf.md`) e fica registrado no
> `diario-de-bordo.md`. **Aprendo o jeito Valvic vendo o que já funcionou.**

## O que mandar (o que o Téo consegue aprender)

| Formato | O Téo lê? | O que aprendo |
|---|---|---|
| **DXF** | ✅ leio a geometria | como o desenho é montado (linhas, círculos, camadas) |
| **`.tap` / `.nc`** | ✅ leio o G-code | como o Aspire virou movimento de máquina (Z, ordem, ferramenta) |
| **PDF** (relatório/lista) | ✅ | ferramentas, tempos, lista de corte |
| **Print da tela** (PNG/JPG) | ✅ vejo a imagem | preview 3D, config da ferramenta, simulação do percurso |
| **`.crv3d`** (nativo Aspire) | ❌ binário, não abro | guardo como **gabarito** — mandar junto o DXF/`.tap` + print |

## Receita por modelo (3 coisas)
1. **O arquivo** — DXF e/ou `.tap` exportado.
2. **1–2 prints** — o 3D e a config da(s) ferramenta(s).
3. **Uma frase** — "isso é um X, o truque foi Y, o que dá errado é Z".

## Como guardar
Para cada caso novo, copie `_FICHA-MODELO.md`, renomeie para
`AAAA-MM-DD_nome-do-caso.md`, preencha, e jogue os arquivos do caso ao lado
(mesmo prefixo de nome). Quando o caso virar regra consolidada, anote em qual
referência ela foi parar.

## Casos mais valiosos (pedido do Téo)
- **Retrabalho do Paulo** — cada erro vira uma regra que mata o retrabalho. 🥇
- Encaixes diferentes (além do osso de cão / abas).
- Cortes especiais: friso de LED, friso de dobra, corte curvo.
- Configurações de ferramenta (T1, T3–T6, T8–T10 ainda não documentadas).

## Índice de exemplos
<!-- preencher conforme chegam: data — nome — formato — regra gerada -->
- `jrg-exemplo-corte-passante-15mm.tap` — corte passante simples (Z = esp.+0,1).
- `jrg-exemplo-dobra-mdf-kerf.tap` — dobra por vincos (kerf bending).
- `jrg-exemplo-dobra-completa-grooves-mais-corte.tap` — dobra + corte na mesma peça.
- `jrg-exemplo-corte-curvo-6mm.tap` — corte curvo em 6mm.
- `jrg-exemplo-curva-completa-estrutura-mais-painel.tap` — curva: estrutura + painel.
- `jrg-exemplo-cambota-base-teto-reguas.tap` — cambota (base/teto/réguas).
- `cilindro-ajustado-encaixe-dogbone.crv3d` — gabarito do encaixe com osso de cão (binário).
