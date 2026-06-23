# figma-create-new-file

- Categoria: **Design, Figma e Frontend** (`design-figma-frontend`)
- Nome declarado: `figma-create-new-file`
- Pacote instalavel: `packages/design-figma-frontend/figma-create-new-file.zip`
- Pasta copiada: `skills/design-figma-frontend/figma-create-new-file`
- Fonte original: `C:\Users\filip\.codex\skills\figma-create-new-file`
- Hash do `SKILL.md`: `b3a45dfd8af628262311cfd0bac8dcbc19affc6b873a9c8421a58707b725e349`

## Resumo

Create a new blank Figma file. Use when the user wants to create a new Figma design or FigJam file, or when you need a new file before calling use_figma. Handles plan resolution via whoami if needed. Usage — /figma-create-new-file [editorType] [fileName] (e.g. /figma-create-new-file figjam My Whiteboard)

## Instalacao individual

```powershell
$zip = "packages/design-figma-frontend/figma-create-new-file.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `figma-create-new-file` |
| Skill name | `figma-create-new-file` |
| Categoria | `design-figma-frontend` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\figma-create-new-file` |
| Pasta no repositorio | `skills/design-figma-frontend/figma-create-new-file` |
| Arquivo principal | `skills/design-figma-frontend/figma-create-new-file/SKILL.md` |
| Zip | `packages/design-figma-frontend/figma-create-new-file.zip` |
| Tamanho do zip | 1,3 KB |
| Duplicatas consolidadas | 2 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | figma-create-new-file |
| `description` | Create a new blank Figma file. Use when the user wants to create a new Figma design or FigJam file, or when you need a new file before calling use_figma. Handles plan resolution via whoami if needed. Usage — /figma-create-new-file [editorType] [fileName] (e.g. /figma-create-new-file figjam My Whiteboard) |
| `disable-model-invocation` | true |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 1 |
| Diretorios | 0 |
| Tamanho copiado | 2,7 KB |

## Secoes internas detectadas

- create_new_file — Create a New Figma File
-   Skill Arguments
-   Workflow
-     Step 1: Resolve the planKey
-     Step 2: Call create_new_file
-     Step 3: Use the result
-   Important Notes

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/design-figma-frontend/figma-create-new-file/SKILL.md` | 2,7 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\figma-create-new-file`
- `C:\Users\filip\.claude\skills\figma-create-new-file`

## Conteudo integral do SKILL.md

````
markdown
---
name: figma-create-new-file
description: Create a new blank Figma file. Use when the user wants to create a new Figma design or FigJam file, or when you need a new file before calling use_figma. Handles plan resolution via whoami if needed. Usage — /figma-create-new-file [editorType] [fileName] (e.g. /figma-create-new-file figjam My Whiteboard)
disable-model-invocation: true
---

# create_new_file — Create a New Figma File

Use the `create_new_file` MCP tool to create a new blank Figma file in the user's drafts folder. This is typically used before `use_figma` when you need a fresh file to work with.

## Skill Arguments

This skill accepts optional arguments: `/figma-create-new-file [editorType] [fileName]`

- **editorType**: `design` (default) or `figjam`
- **fileName**: Name for the new file (defaults to "Untitled")

Examples:
- `/figma-create-new-file` — creates a design file named "Untitled"
- `/figma-create-new-file figjam My Whiteboard` — creates a FigJam file named "My Whiteboard"
- `/figma-create-new-file design My New Design` — creates a design file named "My New Design"

Parse the arguments from the skill invocation. If editorType is not provided, default to `"design"`. If fileName is not provided, default to `"Untitled"`.

## Workflow

### Step 1: Resolve the planKey

The `create_new_file` tool requires a `planKey` parameter. Follow this decision tree:

1. **User already provided a planKey** (e.g. from a previous `whoami` call or in their prompt) → use it directly, skip to Step 2.

2. **No planKey available** → call the `whoami` tool. The response contains a `plans` array. Each plan has a `key`, `name`, `seat`, and `tier`.

   - **Single plan**: use its `key` field automatically.
   - **Multiple plans**: ask the user which team or organization they want to create the file in, then use the corresponding plan's `key`.

### Step 2: Call create_new_file

Call the `create_new_file` tool with:

| Parameter    | Required | Description |
|-------------|----------|-------------|
| `planKey`   | Yes      | The plan key from Step 1 |
| `fileName`  | Yes      | Name for the new file |
| `editorType`| Yes      | `"design"` or `"figjam"` |

Example:
```json
{
  "planKey": "team:123456",
  "fileName": "My New Design",
  "editorType": "design"
}
```

### Step 3: Use the result

The tool returns:
- `file_key` — the key of the newly created file
- `file_url` — a direct URL to open the file in Figma

Use the `file_key` for subsequent tool calls like `use_figma`.

## Important Notes

- The file is created in the user's **drafts folder** for the selected plan.
- Only `"design"` and `"figjam"` editor types are supported.
- If `use_figma` is your next step, load the `figma-use` skill before calling it.
````
