# ELIUTON — Residência Brisas da Pampulha

**Data:** 13/08/2026 · **Status:** ⛔ **projeto NÃO lido** — ver "O bloqueio" abaixo.
**Pasta no Drive:** `1L1y1ZSq1bIpLVSc-Znjm_14ECRreaBAo` — 19 arquivos, todos PDF,
subidos em 13/08/2026 por `valvicmarcenaria@gmail.com`.
**Autoria:** Arq. **Luciana Beatriz Simplício** — Núcleo SC Arquitetura ·
tel. (31) 3004-3387.

---

## Inventário da pasta

### Documentos-mestre (2)
| Arquivo | Tam. | Leitura |
|---|--:|---|
| `PROJ. ELTN_A3_ÁREAS MOLHADAS-AS E BANHEIROS.pdf` | 3,1 MB | ✅ **legível** — export de PowerPoint |
| `PLANTAS COTADAS - Executivo[1]_…-Model.pdf` | 1,8 MB | ❌ só devolve *"PÉ DIREITO DUPLO"* |

### Série PR NN — cozinha e gourmet (8 arquivos)
`PR 01` a `PR 05` **COZINHA** · `PR 06` e `PR 07` **A. GOURMET**
⚠️ ~~`PR 05_COZINHA` duplicado~~ — **NÃO são duplicatas** [Jonathan 13/08]. Mesmo nome,
conteúdos diferentes. Eu tinha julgado pelo nome do arquivo. O leitor do Drive devolve
os dois idênticos porque só faz OCR do **carimbo**, que é igual nos dois.

### Série PR NN-10 — áreas molhadas (9 arquivos)
`01-10` ÁREA SERVIÇO · `03-10` LAVABO EXTERNO · `04-10` BANHEIRO SOCIAL TÉRREO ·
`05-10` e `06-10` BANHEIRO MASTER · `07-10` e `08-10` BANHEIRO SOCIAL 1º PAV ·
`09-10` e `10-10` BANHEIRO 04

> ⚠️ **`PR 02-10` NÃO ESTÁ NA PASTA.** A sequência é 01, _(02 faltando)_, 03…10.
> Pedir ao cliente ou à arquiteta.

---

## O que o documento legível diz — e por que ele não resolve

O A3 compilado é o **pacote de acabamentos das áreas molhadas**, não de marcenaria:

| Ambiente | Piso | Parede |
|---|--:|--:|
| Lavanderia | 5,42 m² | 23,00 m² |
| Lavabo externo | 2,55 m² | 7,90 m² + 4,80 m² de destaque |
| *(sem nome no extrato)* | 4,34 m² | 12,75 m² + 5,71 m² de destaque |
| Banheiro social térreo | 4,06 m² | 13,50 m² + 8,12 m² de destaque |
| Banheiro suíte 02 | 4,20 m² | 16,14 m² + 7,22 m² de destaque |
| Banheiro suíte master | 9,20 m² | 21,70 m² + 5,20 + 6,65 m² de destaque |

Especifica **porcelanato** (Portinari York / Sense Travertino / Ritual, Embramaco Gran
Ônix, Ceusa Traços Mônaco), **mármore travertino** e tijolete, **azulejo Portobello
Gouache Nuage**, e **louças e metais Deca** (Axis, Level, Black Matte, Red Gold).

**Nada disso é nosso.** É revestimento, louça e metal — o escopo do revestimentista e
do hidráulico. Não há uma linha de marcenaria no arquivo que consegui ler.

**E a marcenaria está exatamente onde não consigo ler:** as 5 pranchas da COZINHA e as
2 da ÁREA GOURMET.

---

## ⛔ O bloqueio

As 17 pranchas PR são **PDFs de CAD**. O leitor do conector do Drive devolve apenas o
carimbo, OCR-ado e com erro:

```
"Model \n\nNÚCLEO\n\nBC ARQUITETERA\n\nLUCIANA BEATRIZ SIMPLICIO\n\nGOUTAL STA…"
```

Sem cota, sem elevação, sem legenda. **Não dá para orçar a partir disso.**

E `drive.google.com` está **bloqueado pela política de rede** deste ambiente — a tentativa
de baixar direto morre no gateway:

```
connect_rejected · gateway answered 403 to CONNECT · host: drive.google.com:443
```

### O caminho que funciona
**Subir os PDFs no chat**, como foi feito com a prancha AR-18 da Honda. Ali eu extraio a
geometria vetor a vetor — escala aferida no próprio desenho, cada linha lida em
coordenada — e o levantamento sai das cotas, não de estimativa.

**Prioridade, se for para subir aos poucos:** as 5 da COZINHA, depois as 2 da GOURMET,
depois `PLANTAS COTADAS`. As 9 de banheiro provavelmente só têm marcenaria se houver
gabinete/nicho — conferir.

---

## A confirmar
1. **Qual é o escopo de marcenaria** neste projeto. O único arquivo legível é de
   revestimento. Cozinha e gourmet podem ou não ter marcenaria nossa.
2. **`PR 02-10`** — falta na pasta.
3. ~~`PR 05_COZINHA` duplicado~~ — resolvido: são duas pranchas diferentes.
4. **Situação de caixa e MC** — quando houver escopo.


---

## 13/08 — segunda tentativa de leitura, e o motor montado

Testei o `read_file_content` em **quatro** pranchas da cozinha (PR 01, 02, 05 e
PR 05 (1)). Todas devolvem o mesmo carimbo OCR-ado, com grafias diferentes a cada
leitura — `SC ARBUITETURA`, `BC ARQUITETERA`, `BC ARBUITETURA`, `ROUTETAANSA`,
`GOUTAL STA`. Grafia instável na mesma origem é **assinatura de OCR sobre imagem**:
as pranchas são **raster**, não vetoriais.

Consequências, já registradas:
1. Mesmo com o arquivo em mãos, **a leitura será visual**, não vetor a vetor como na
   prancha AR-18 da Honda. Resolução importa.
2. Baixar pelo conector **não fecha a conta**: a menor prancha da cozinha (182 KB)
   vira ~243 mil caracteres em base64 para chegar, e o mesmo tanto para gravar em
   disco. ~120 mil tokens **por prancha**, e são cinco. Estoura antes da terceira.
3. `drive.google.com` segue bloqueado na política de rede (403 no CONNECT).

**Entregue mesmo assim:** `2026-eliuton-duvidas-tecnicas.md` (o levantamento de
dúvidas, que o Jonathan pediu para vir antes) e `corte-eliuton.py` (o motor com os
três cenários e a regra do ripado já calibrados — falta só a geometria).
