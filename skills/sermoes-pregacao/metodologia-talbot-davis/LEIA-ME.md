# 🎙️ Metodologia Talbot Davis — Skill para Múltiplas IAs

> Baseada no livro *Simplify the Message, Multiply the Impact* (Talbot Davis, Abingdon Press, 2020) e na análise empírica de **276 sermões** pregados na Good Shepherd United Methodist Church, Charlotte, NC.

---

## 📌 O que é esta Skill?

Esta skill ensina qualquer IA a criar sermões, séries e esboços homiléticos com a precisão, profundidade e impacto de **Talbot Davis** — um dos pregadores metodistas mais influentes dos EUA, especialista no **sermão expositivo de 1 Ponto**.

### Princípios Centrais:
- **1 Bottom Line por sermão** — memorável, rítmica, que uma criança de 11 anos repete à mesa
- **3 Movimentos:** Envolver → Encontrar → Capacitar (*Engage → Encounter → Empower*)
- **Exegese como Sherlock Holmes** — notar o detalhe surpreendente antes de abrir comentários
- **Wordsmithing rigoroso** — escrever para o ouvido, não para os olhos
- **Apelo cristocêntrico** culminando em *"JESUS. É. SENHOR."* proclamado em uníssono
- **Pregação sem notas** por internalização em 9 etapas semanais
- **Funerais:** A Pessoa antes da Promessa (nunca abrir com João 3:16)

---

## 📂 Estrutura do Repositório

```
metodologia-talbot-davis/
│
├── LEIA-ME.md                          ← Este arquivo (guia de instalação)
│
├── gemini-antigravity/                 ← Skill para Gemini / Antigravity IDE
│   ├── SKILL.md                        ← Arquivo principal (frontmatter YAML)
│   ├── references/
│   │   ├── 01-fundamentos-e-movimentos.md
│   │   ├── 02-exegese-sherlock-holmes.md
│   │   ├── 03-wordsmithing-e-oralidade.md
│   │   ├── 04-arquitetura-de-series.md
│   │   ├── 05-pregacao-cristocentrica-e-apelo.md
│   │   ├── 06-funerais-e-ocasiao-especial.md
│   │   ├── 07-internalizacao-sem-notas.md
│   │   └── 08-corpus-analitico-276-sermoes.md
│   └── examples/
│       ├── exemplo-manuscrito-completo.md
│       └── exemplo-serie-completa.md
│
├── claude-desktop/
│   └── system-prompt.md                ← System Prompt completo para Claude Desktop
│
└── chatgpt-desktop/
    └── custom-instructions.md          ← Custom Instructions (Bloco A + Bloco B)
```

---

## 🚀 Instalação por Plataforma

### 🔵 Gemini / Antigravity IDE

```powershell
# Windows — PowerShell
Copy-Item -Path ".\gemini-antigravity\*" `
  -Destination "$env:USERPROFILE\.gemini\config\skills\metodologia-talbot-davis\" `
  -Recurse -Force
```

```bash
# Linux / Mac — Terminal
cp -r ./gemini-antigravity/* ~/.gemini/config/skills/metodologia-talbot-davis/
```

A skill será detectada automaticamente na próxima conversa. Não é necessário reiniciar.

---

### 🟣 Claude Desktop

1. Abra o **Claude Desktop**
2. Vá em **Settings → System Prompt** (ou **Custom Instructions**)
3. Copie TODO o conteúdo de `claude-desktop/system-prompt.md`
4. Cole no campo e salve
5. Reinicie a conversa — a metodologia estará ativa ✅

> **Dica:** O Claude aceita system prompts longos sem truncar. Cole o arquivo inteiro sem cortar.

---

### 🟢 ChatGPT Desktop

1. Clique no seu perfil → **Customize ChatGPT → Custom Instructions**
2. Abra o arquivo `chatgpt-desktop/custom-instructions.md`
3. Cole o **BLOCO A** no campo *"What would you like ChatGPT to know about you?"*
4. Cole o **BLOCO B** no campo *"How would you like ChatGPT to respond?"*
5. Clique em **Save** ✅

> **Atenção:** Os blocos foram calibrados para caber dentro do limite de ~1.500 caracteres por campo.

---

### 🌐 Qualquer outra IA (Gemini Web, Perplexity, Copilot, etc.)

Cole o conteúdo de `claude-desktop/system-prompt.md` como **primeira mensagem** da conversa, precedido de:

> *"A partir de agora, siga rigorosamente estas instruções em todas as suas respostas desta conversa:"*

---

## 🧪 Exemplos de Uso

Após instalar a skill em qualquer IA, experimente:

**Sermão:**
> "Crie um sermão completo no estilo Talbot Davis sobre [texto bíblico ou tema]"

**Série:**
> "Planeje uma série de 4 semanas sobre [livro/tema] no estilo Talbot Davis"

**Lapidação de frase:**
> "Lapide esta Bottom Line no estilo Talbot Davis: [frase bruta]"

**Funeral:**
> "Crie um esboço fúnebre no estilo Talbot Davis para [situação pastoral]"

---

## 📚 Base Teórica

| Fonte | Relevância |
|---|---|
| *Simplify the Message, Multiply the Impact* — Talbot Davis (Abingdon, 2020) | Livro base da skill (9 capítulos cobertos) |
| *Methodical Bible Study* — Robert Traina | Ferramentas exegéticas (Repetição, Interrogação, Contraste) |
| *Just Say the Word* — Robert Jacks | Escrita para o ouvido (*"Fale enquanto digita"*) |
| *Preaching* — Timothy Keller | *"Jesus em Tudo"* — a regra do encerramento cristocêntrico |
| *Preaching without Notes* — Joseph Webb | Fundamento da pregação por internalização |
| 276 sermões da Good Shepherd UMC (corpus analisado) | Padrões empíricos de estrutura, léxico e apelo |

---

## 🏷️ Tags

`homilética` `pregação` `sermão` `talbot-davis` `1-ponto` `bottom-line` `série` `expositivo` `metodista` `pt-br` `skill` `gemini` `claude` `chatgpt`
