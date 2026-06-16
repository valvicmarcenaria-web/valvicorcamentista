# Pesquisa de Satisfação — Nível 1 (Google Forms)

Dois formulários enviados por WhatsApp no momento certo do projeto.
Respostas vão automaticamente para uma Planilha Google no Drive.

---

## FORMULÁRIO 1 — Checkpoint de Obra

**Quando enviar:** após a Conferência Técnica (antes da montagem)  
**Quem envia:** Jonathan  
**Canal:** WhatsApp Business — mensagem template (ver abaixo)  
**Duração para o cliente:** ~2 minutos

### Configuração no Google Forms

**Título:** Checkpoint Valvic — [Nome do Cliente]  
**Descrição:**
> Seu projeto está em produção e queremos garantir que tudo está exatamente como você idealizou.
> São só 3 perguntas rápidas. Obrigado por confiar na Valvic! ✦

**Pergunta 1**
- Tipo: Escala linear (1 a 5)
- Pergunta: *Como você avalia a comunicação com a nossa equipe até agora?*
- Rótulo 1: "Poderia melhorar"
- Rótulo 5: "Excelente"

**Pergunta 2**
- Tipo: Parágrafo (texto longo)
- Pergunta: *Tem alguma dúvida ou preocupação sobre o projeto que ainda não foi respondida?*
- Obrigatório: Não

**Pergunta 3**
- Tipo: Parágrafo (texto longo)
- Pergunta: *Tem alguma sugestão de como poderíamos melhorar o processo?*
- Obrigatório: Não

**Confirmação (mensagem ao final):**
> Obrigado pelo seu feedback! Nossa equipe irá revisar e, se houver alguma pendência, entraremos em contato em até 24h. Estamos comprometidos em entregar exatamente o que você idealizou. ✦

---

### Mensagem WhatsApp — Checkpoint

```
Oi, [Nome]! Tudo bem? Aqui é o Jonathan da Valvic. 😊

Seu projeto está em produção e está ficando incrível!

Antes da entrega, criei uma pesquisa rápida com 3 perguntas — leva menos de 2 minutos.
É pra garantir que tudo está exatamente como você idealizou:

👇 [LINK DO FORMULÁRIO]

Qualquer dúvida, estou aqui!
```

---

## FORMULÁRIO 2 — Pesquisa de Entrega

**Quando enviar:** D+7 após a montagem  
**Quem envia:** Jonathan  
**Canal:** WhatsApp Business — mensagem template (ver abaixo)  
**Duração para o cliente:** ~3 minutos

### Configuração no Google Forms

**Título:** Como ficou seu projeto? — Valvic Marcenaria  
**Descrição:**
> Seu projeto foi entregue há uma semana! 🎉
> Queremos saber como está sendo a experiência de viver com ele no dia a dia.
> São 5 perguntas rápidas — e sua opinião faz toda a diferença para a gente continuar melhorando.

**Pergunta 1 — NPS**
- Tipo: Escala linear (0 a 10)
- Pergunta: *Em uma escala de 0 a 10, qual a probabilidade de você recomendar a Valvic para um amigo ou familiar?*
- Rótulo 0: "Jamais recomendaria"
- Rótulo 10: "Com certeza recomendaria"
- Obrigatório: Sim

**Pergunta 2**
- Tipo: Parágrafo
- Pergunta: *O que mais te surpreendeu positivamente no projeto ou na experiência com a Valvic?*
- Obrigatório: Não

**Pergunta 3**
- Tipo: Parágrafo
- Pergunta: *Tem algo que poderíamos ter feito melhor?*
- Obrigatório: Não

**Pergunta 4**
- Tipo: Parágrafo
- Pergunta: *Se quiser deixar um depoimento sobre sua experiência, fique à vontade! Podemos usar nas nossas redes e materiais.*
- Placeholder: "Ex: Adorei o resultado, o processo foi muito organizado e a equipe super atenciosa..."
- Obrigatório: Não

**Pergunta 5**
- Tipo: Múltipla escolha (checkboxes)
- Pergunta: *Autorizo a Valvic a usar meu depoimento e/ou fotos do projeto nas redes sociais e materiais de divulgação.*
- Opções:
  - ✅ Sim, autorizo com meu nome
  - ✅ Sim, autorizo de forma anônima
  - ❌ Prefiro não autorizar

**Confirmação (mensagem ao final):**
> Muito obrigado pelo seu tempo e pela confiança! 💛
> Seu feedback é o que nos move a entregar cada vez melhor.
> Em breve entraremos em contato. — Equipe Valvic ✦

---

### Mensagem WhatsApp — Entrega

```
Oi, [Nome]! Aqui é o Jonathan da Valvic. 😊

Já faz uma semana desde a entrega do seu projeto — e adoraria saber como está sendo!

Preparei uma pesquisa rápida com 5 perguntas. Leva 3 minutinhos:

👇 [LINK DO FORMULÁRIO]

Sua opinião é muito importante pra gente continuar evoluindo. Obrigado de coração! 🙏
```

---

## Planilha Google — Estrutura recomendada

Quando conectar o formulário à planilha (automático pelo Google Forms),
crie uma segunda aba manualmente chamada **"Dashboard"** com estas fórmulas:

### Aba: Dashboard

| Campo | Fórmula |
|---|---|
| Total de respostas | `=COUNTA(Respostas!A:A)-1` |
| NPS médio | `=AVERAGE(Respostas!B:B)` *(coluna do NPS)* |
| % Promotores (9–10) | `=COUNTIF(Respostas!B:B,">=9")/COUNTA(Respostas!B:B)-1` |
| % Neutros (7–8) | `=COUNTIFS(Respostas!B:B,">=7",Respostas!B:B,"<=8")/COUNTA(Respostas!B:B)-1` |
| % Detratores (0–6) | `=COUNTIF(Respostas!B:B,"<=6")/COUNTA(Respostas!B:B)-1` |
| NPS Score | `=% Promotores - % Detratores` |

### Aba: Depoimentos Aprovados

Filtro manual: Jonathan revisa as respostas semanalmente e cola os
depoimentos com autorização nessa aba. Campos:
- Data
- Nome (ou "Anônimo")
- Depoimento
- Perfil do projeto (Premium / Excellence / Essencial)
- Usou na proposta? (Sim / Não)
- Usou no Instagram? (Sim / Não)

---

## Gatilhos manuais (Nível 1)

Jonathan confere as respostas **1x por semana** na planilha e age:

| Score NPS | Ação |
|---|---|
| 9–10 (Promotor) | Enviar mensagem pedindo foto + tag no Instagram. Copiar depoimento para "Depoimentos Aprovados". Considerar pedir indicação. |
| 7–8 (Neutro) | Agradecer. Investigar o que faltou para virar 9. |
| 0–6 (Detrator) | Contato imediato (24h). Entender o problema. Registrar na Academia (Histórico > Atenção). |

---

### Mensagem WhatsApp — Pedir foto/indicação (para Promotores)

```
[Nome], muito obrigado pelo seu feedback incrível! 💛

Fico muito feliz que o projeto superou as expectativas.

Teria uma fotinho do ambiente pronto que você pudesse compartilhar?
Adoraríamos mostrar o resultado nas nossas redes (sempre com seu aval, claro!).

E se você conhecer alguém que esteja pensando em fazer uma marcenaria, 
pode nos indicar à vontade — vai ser um prazer cuidar de mais um projeto assim. 😊
```

---

## Setup completo — passo a passo (20 minutos)

1. Criar Formulário 1 no Google Forms (Checkpoint) — 5 min
2. Criar Formulário 2 no Google Forms (Entrega) — 8 min
3. Em cada formulário: clicar em "Respostas" → ícone do Sheets → criar planilha vinculada — 2 min
4. Na planilha do Formulário 2: criar aba "Dashboard" com as fórmulas — 3 min
5. Criar aba "Depoimentos Aprovados" na mesma planilha — 2 min
6. Salvar os links dos formulários como mensagens salvas no WhatsApp Business — 5 min

**Pronto. Processo rodando.**

---

## Evolução futura (Nível 2)

Quando o volume crescer e o envio manual virar gargalo:
- **Tally** (formulário mais bonito) + **Make** (automação)
- Nota ≥ 8 → WhatsApp automático de depoimento
- Nota ≤ 6 → alerta para Jonathan no WhatsApp
- Depoimentos aprovados → alimentam a academia automaticamente
