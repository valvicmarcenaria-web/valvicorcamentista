# Diário de bordo do Téo — onde paramos

> Para a próxima sessão (eu começo sem memória — leio isto primeiro). Registro o
> estado, o que está pendente e as perguntas em aberto. Atualizar ao fim de cada
> sessão de trabalho.

## 👥 COM QUEM EU FALO (a conta do Gmail é compartilhada — ler sempre)
A mesma conta (`valvicmarcenaria@gmail.com`) é usada por mais de uma pessoa. Quem
está digitando muda. Para não trocar os nomes:
- **Paulo** = sócio, marceneiro 20 anos. **TODA programação de Aspire e conversa de
  chão de fábrica é com o Paulo.** Se o assunto é Aspire/CNC/corte/encaixe/ferramenta
  /máquina e a pessoa não disse quem é → **é o Paulo**.
- **Jonathan** = quando for ele, **ele avisa** ("aqui é o Jonathan").
- **Lavinia** = orçamento · **Rodrigo** = finanças (outros skills).
- Na dúvida sobre quem está falando num assunto de produção, assumir **Paulo**.

📌 Plano da NOVA ESTRUTURA (expansão) consolidado em `projetos/Nova-estrutura.md`.

## Última sessão: 2026-06-24

### Caso real: criado-mudo curvo (dobra por BOLSO contínuo) ✅ aprendido
- Paulo mandou imagem + `.crv3d` + **`.tap`** (G-code). O `.tap` é ouro — leio a
  geometria real. Guardado em `exemplos/2026-06-24_criado-mudo-curvo*`.
- **Técnica nova:** dobra por **bolso contínuo até a pele** (≠ vincos do cilindro).
  Acabamento liso. Ranhuras com **passo < Ø da fresa** (5,7 < 6) → sobrepõem → fundo
  liso. T2 (6mm), ossos de cão R3, Z+1 dobra / Z−0,1 passante. Ver `dobra-de-mdf.md`.
- 🚨 **Lição (erro meu):** confundi raio×diâmetro. O `.tap` provou raio **R60** (=Ø120);
  o "120" era diâmetro. A zona de dobra do Paulo (9,5cm) estava CERTA. **Fórmula:
  zona de dobra = arco = R × ângulo(rad); usar sempre o RAIO.**
- **Téo gerou** a lateral parametrizada de teste 2 (`lateral_criado_r80_teste_teo.dxf`):
  R80 (Ø160), 90°, alt 350, aba 600 + retorno 200, chapa 15mm — tudo CONFIRMADO.
  **AGUARDANDO** Paulo importar no Aspire e validar.

## Última sessão: 2026-06-23

### Técnica: bisel de 45° mais grosso que a fresa alcança 🪚
- **Problema:** fresa de 45° corta no máx **18mm** de profundidade. Bisel de 45°
  atravessando **30mm** precisaria de 30mm de profundidade → não alcança.
- **Solução:** dividir em **2 chapas de 15mm**, biselar cada uma e empilhar. Como
  45° = **1:1**, cada 15mm de profundidade anda 15mm no raio → as duas faces de 45°
  ficam na mesma reta = **um cone contínuo**, sem degrau.
- 🎯 **A regra que importa:** a **diferença de RAIO entre os dois círculos = a
  espessura da chapa** (15mm). Isso garante o cone contínuo **mesmo se a calibração
  do kerf variar** (o kerf é da mesma fresa nas 2 peças → se cancela; só muda o Ø
  final em ~1mm). Geral: dif. de raio = espessura da chapa de cima.
- **Kerf do Paulo:** fresa de 45° "come" **+3mm no diâmetro** → desenhar Ø+3 pra
  sobrar o tamanho certo.
- **Risco único = alinhamento.** Colar torto cria degrau no bisel na linha da emenda.
  Solução: **furo de centro Ø8 nas 2 peças** (mesma origem na CNC) + **cavilha** pra
  centralizar. Sempre fazer **corte de teste** numa sobra pra conferir o +3mm.
- **Caso real (tampo Ø300, 23/06):** desenhar **cima Ø303 / baixo Ø273**; final =
  topo 300 → emenda 270 → base 240. Gerador: `gerados/gen_tampo_redondo_300_bisel45.py`,
  saída `gerados/tampo_redondo_300_bisel45_teo.dxf`.

### Regra NOVA do Paulo (gravar pra não esquecer mais) 🚨
- 🔩 **Osso de cão (dogbone) em APENAS UMA peça do par** — ou na **estrutura** (a
  aba/peça que encaixa) **ou** no **buraco** que a recebe. **NUNCA nas duas**, senão
  tira material a mais e o encaixe fica frouxo.
- **Padrão Valvic / cilindro:** osso de cão **na ESTRUTURA** (nos ombros das abas das
  4 réguas — 16 ossos no total) e o **buraco/rasgo sai LIMPO** (discos do tampo
  redondo sem dogbone). Ver `aspire-cortes-especiais.md` §1.
- Outro erro corrigido nesta sessão (v3): **ranhuras de dobra eram linhas soltas** →
  a fresa saía da peça entre passadas e quebrava as quinas. Agora **zigzag contínuo**
  (1 entrada / 1 saída), avanço de **10mm fora da peça** em cima e embaixo.
- **Entregue hoje:** `gerados/cilindro_r200_h500_encaixe_v4_teo.dxf` (gerador
  `gen_dxf4.py`). Estilo do osso de cão deixado como está, a pedido do Paulo.
- **AGUARDANDO:** Paulo importar o **v4** no Aspire e dizer se o encaixe bate.

## Sessão anterior: 2026-06-16

### O que já está consolidado (✅)
- **Persona Téo** definida: marceneiro raiz 25 anos + programador.
- **Parque de máquinas** mapeado: Raizen **Solid TAF** (mesa 2800×1900, Z200, ATC
  10 ferramentas, controlador **JRG**), coladeira **SCM minimax me 25** (fita 0,4mm,
  7 m/min, cola EVA ~180–190°C), esquadrejadeira RZN 3200P, tupia, serra esquadria.
- **Dialeto G-code JRG** decodificado de `.tap` reais (`aspire-cortes-especiais.md`).
- 🚨 **Trava de Z:** Z-zero na chapa de sacrifício; **nunca Z < −0,1**. Passante =
  espessura+0,1; parcial = espessura − profundidade.
- **Ferramentas em uso:** T2 (fresa reta 6mm), **T7 (fresa 45° — CORRIGIDO 26/06**, antes
  estava errado como "reta 3mm"). Magazine tem 10. (45° = chanfro; ver aspire-cortes-especiais.)
- **Dobra de MDF (kerf bending)** capturada (`dobra-de-mdf.md`): vincos 12mm, pele
  1mm, Z+1 em chapa 15mm; fluxo estrutura→ranhuras→separação (multi-operação).
- **Calibração:** quina cambota **R203** ↔ espaçamento **12mm** (≈27 vincos/90°).
- **Téo gerou**: `.tap` do cilindro + **DXF v2 com encaixe** (cruz, abas, nesting
  7mm, chapa 1850×2750). Ver `gerados/`.

### EM ANDAMENTO — Teste do cilindro R200 × H500
- Entreguei o **DXF v2 com encaixe** (`cilindro_r200_h500_encaixe_teo.dxf`).
- **AGUARDANDO:** Paulo importar no Aspire e dizer se a geometria bate (2 discos
  com "+" de rasgos, 4 réguas com abas, painel com 105 vincos).
- **Decisões minhas a confirmar:** aba 30×15mm (ombro 10mm); rasgos a 70mm do
  centro; réguas como 4 aletas radiais separadas (≠ entrelaçadas com meia-madeira).

### Regras novas gravadas (16/06, fim do dia)
- 🔩 **Osso de cão (dogbone) em TODA quina de encaixe** (raio = raio da fresa).
  Sem ele, aba de canto vivo não assenta. Ver `aspire-cortes-especiais.md`.
- 📐 **Folga de 7mm também da borda da chapa** (margem de nesting = 7mm, não 10).
- Gabarito recebido: `exemplos/cilindro-ajustado-encaixe-dogbone.crv3d` (Aspire,
  binário — não editável por mim, guardado como referência do encaixe correto).
- ✅ **RESOLVIDO em 23/06 (v3/v4):** geradores atualizados com (a) margem 7mm e
  (b) dogbones — agora só na estrutura (réguas), não nos discos. Ver topo do arquivo.

### Perguntas em aberto (puxar quando der)
1. **Caso real de retrabalho do Paulo** — o maior combustível (modos de falha →
   regras). Ainda não veio.
2. **Dobra:** R203 fechou com folga? Qual o **raio mínimo** sem quebrar a pele de
   1mm? O espaçamento muda com o raio?
3. **Máquina:** onde fica o **0,0** na mesa? **Passada única** corta até quantos mm
   (acima disso, passo em Z)?
4. **Ferramentas:** documentar T1, T3–T6, T8–T10 (finalidade, offsets/descontos).
5. **Regra do suporte espada** (do 1º teste) ainda não registrada no
   `modelo-construtivo.md`.

### Lembrete de método
Cada caso real / arquivo / resposta do Paulo → vira regra escrita aqui. Arquivos
`.tap` reais guardados em `referencias/exemplos/` como verdade de campo. Saídas
geradas pelo Téo em `gerados/`.
