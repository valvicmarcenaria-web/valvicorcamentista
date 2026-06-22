# Diário de bordo do Téo — onde paramos

> Para a próxima sessão (eu começo sem memória — leio isto primeiro). Registro o
> estado, o que está pendente e as perguntas em aberto. Atualizar ao fim de cada
> sessão de trabalho.

## Última sessão: 2026-06-16

### O que já está consolidado (✅)
- **Persona Téo** definida: marceneiro raiz 25 anos + programador.
- **Parque de máquinas** mapeado: Raizen **Solid TAF** (mesa 2800×1900, Z200, ATC
  10 ferramentas, controlador **JRG**), coladeira **SCM minimax me 25** (fita 0,4mm,
  7 m/min, cola EVA ~180–190°C), esquadrejadeira RZN 3200P, tupia, serra esquadria.
- **Dialeto G-code JRG** decodificado de `.tap` reais (`aspire-cortes-especiais.md`).
- 🚨 **Trava de Z:** Z-zero na chapa de sacrifício; **nunca Z < −0,1**. Passante =
  espessura+0,1; parcial = espessura − profundidade.
- **Ferramentas em uso:** T2 (fresa 6mm), T7 (fresa 3mm). Magazine tem 10.
- **Dobra de MDF (kerf bending)** capturada (`dobra-de-mdf.md`): vincos 12mm, pele
  1mm, Z+1 em chapa 15mm; fluxo estrutura→ranhuras→separação (multi-operação).
- **Calibração:** quina cambota **R203** ↔ espaçamento **12mm** (≈27 vincos/90°).
- **Téo gerou**: `.tap` do cilindro + **DXF v2 com encaixe** (cruz, abas, nesting
  7mm, chapa 1850×2750). Ver `gerados/`.

### EM ANDAMENTO — Teste do cilindro R200 × H500
- Entreguei o **DXF v2 com encaixe** (`cilindro_r200_h500_encaixe_teo.dxf`).
- **AGUARDANDO:** Jonathan importar no Aspire e dizer se a geometria bate (2 discos
  com "+" de rasgos, 4 réguas com abas, painel com 105 vincos).
- **Decisões minhas a confirmar:** aba 30×15mm (ombro 10mm); rasgos a 70mm do
  centro; réguas como 4 aletas radiais separadas (≠ entrelaçadas com meia-madeira).

### Regras novas gravadas (16/06, fim do dia)
- 🔩 **Osso de cão (dogbone) em TODA quina de encaixe** (raio = raio da fresa).
  Sem ele, aba de canto vivo não assenta. Ver `aspire-cortes-especiais.md`.
- 📐 **Folga de 7mm também da borda da chapa** (margem de nesting = 7mm, não 10).
- Gabarito recebido: `exemplos/cilindro-ajustado-encaixe-dogbone.crv3d` (Aspire,
  binário — não editável por mim, guardado como referência do encaixe correto).
- ⚠️ **Pendência de implementação:** atualizar geradores para (a) margem 7mm e
  (b) gerar dogbones automáticos nos rasgos de encaixe.

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
