# optimize-windows-performance

- Categoria: **Sistema e Agentes** (`sistema-agentes`)
- Nome declarado: `optimize-windows-performance`
- Pacote instalavel: `packages/sistema-agentes/optimize-windows-performance.zip`
- Pasta copiada: `skills/sistema-agentes/optimize-windows-performance`
- Fonte original: `C:\Users\filip\.codex\skills\optimize-windows-performance`
- Hash do `SKILL.md`: `14996765f5362749d7ccf1db985ad57b7ebdeee598eda7ffb301afe563bbe320`

## Resumo

Use when a Windows PC is slow, overloaded, low on disk space, unstable, burdened by startup apps or background services, or needs evidence-based performance tuning, debloating, maintenance, benchmarking, driver or firmware review, and rollback.

## Instalacao individual

```powershell
$zip = "packages/sistema-agentes/optimize-windows-performance.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `optimize-windows-performance` |
| Skill name | `optimize-windows-performance` |
| Categoria | `sistema-agentes` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\optimize-windows-performance` |
| Pasta no repositorio | `skills/sistema-agentes/optimize-windows-performance` |
| Arquivo principal | `skills/sistema-agentes/optimize-windows-performance/SKILL.md` |
| Zip | `packages/sistema-agentes/optimize-windows-performance.zip` |
| Tamanho do zip | 24,6 KB |
| Duplicatas consolidadas | 1 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | optimize-windows-performance |
| `description` | Use when a Windows PC is slow, overloaded, low on disk space, unstable, burdened by startup apps or background services, or needs evidence-based performance tuning, debloating, maintenance, benchmarking, driver or firmware review, and rollback. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 9 |
| Diretorios | 4 |
| Tamanho copiado | 80,1 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 226 B |
| `references` | 4 | 11,2 KB |
| `scripts` | 2 | 51,3 KB |
| `tests` | 1 | 13,5 KB |

## Secoes internas detectadas

- Optimize Windows Performance
-   Overview
-   Workflow obrigatório
-   Perfis
-   Guardrails não negociáveis
-   Quick reference
- Somente leitura
- Prévia sem mutação
- Aplicação e verificação
- Rollback
-   Exemplo
-   Erros comuns

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/sistema-agentes/optimize-windows-performance/agents/openai.yaml` | 226 B |
| `skills/sistema-agentes/optimize-windows-performance/references/diagnosis-and-measurement.md` | 2,6 KB |
| `skills/sistema-agentes/optimize-windows-performance/references/oem-drivers-and-firmware.md` | 2,6 KB |
| `skills/sistema-agentes/optimize-windows-performance/references/optimization-catalog.md` | 3,0 KB |
| `skills/sistema-agentes/optimize-windows-performance/references/safety-and-rollback.md` | 2,9 KB |
| `skills/sistema-agentes/optimize-windows-performance/scripts/Invoke-WindowsOptimization.ps1` | 7,1 KB |
| `skills/sistema-agentes/optimize-windows-performance/scripts/WindowsOptimization.Core.psm1` | 44,3 KB |
| `skills/sistema-agentes/optimize-windows-performance/SKILL.md` | 3,9 KB |
| `skills/sistema-agentes/optimize-windows-performance/tests/Optimizer.Tests.ps1` | 13,5 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\optimize-windows-performance`

## Conteudo integral do SKILL.md

````
markdown
---
name: optimize-windows-performance
description: Use when a Windows PC is slow, overloaded, low on disk space, unstable, burdened by startup apps or background services, or needs evidence-based performance tuning, debloating, maintenance, benchmarking, driver or firmware review, and rollback.
---

# Optimize Windows Performance

## Overview

Otimizar por evidências, nunca por receita de outro PC. Medir, criar backup,
aplicar por fases e restaurar regressões.

## Workflow obrigatório

1. **Auditar antes de propor.** Executar:

   ```powershell
   powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts\Invoke-WindowsOptimization.ps1 -Mode Audit
   ```

   Ler [diagnosis-and-measurement.md](references/diagnosis-and-measurement.md)
   para interpretar métricas, startup, serviços, eventos e integridade.

2. **Separar evidência de preferência.** Perguntar antes de remover funções como
   sincronização, acesso remoto, hibernação, biometria, WSL ou integrações OEM.
   Elevação administrativa não equivale a consentimento funcional.

3. **Gerar e revisar o plano.** Usar `-Mode Plan -Profile <perfil>`. Ler
   [optimization-catalog.md](references/optimization-catalog.md). Rejeitar plano
   com alvo copiado, ação sem evidência, restauração indefinida ou componente
   protegido.

4. **Simular.** Executar `-Mode Apply -Profile <perfil> -WhatIf`. Confirmar que
   `Audit`, `Plan` e `-WhatIf` não criaram estado nem alteraram o Windows.

5. **Aplicar por fases.** Ler
   [safety-and-rollback.md](references/safety-and-rollback.md). Aprovar cada
   `ActionId` consentido. Criar estado em
   `%ProgramData%\CodexWindowsOptimizer` antes da primeira mutação.

6. **Reiniciar e verificar.** Coordenar o reboot. Executar
   `-Mode Verify -StatePath <pasta>`. Comparar baseline, benchmark, rede e
   eventos. Restaurar experimentos acima do limite de regressão (`regression`).

7. **Restaurar se preciso.** Executar `-Mode Restore -StatePath <pasta>`.
   Recusar estado incompleto salvo quando o usuário revisar e autorizar uma
   restauração parcial.

## Perfis

| Perfil | Uso |
|---|---|
| `Safe` | Integridade, espaço e startup dispensável |
| `Performance` | Redução ampla de carga com escolhas funcionais explícitas |
| `Extreme` | Experimentos medidos de energia, rede e OEM com rollback |

`Extreme` não autoriza desativar segurança ou limites térmicos.

## Guardrails não negociáveis

- Preservar Defender, Update, UAC, mitigações, pagefile, logs e Prefetch.
- Não desativar Search ou SysMain sem evidência específica.
- Não remover Edge ou componentes centrais do shell por padrão.
- Usar allowlist; nunca matar processos genéricos.
- Respeitar ACLs OEM; nunca tomar posse para forçar serviço protegido.
- Não instalar firmware ou driver de outro OEM.
- Não chamar pico de frequência de ganho: comparar desempenho sustentado.
- Não limpar dados pessoais, modelos ou volumes sem classificação e consentimento.

Para BIOS e drivers, ler obrigatoriamente
[oem-drivers-and-firmware.md](references/oem-drivers-and-firmware.md).

## Quick reference

```powershell
# Somente leitura
.\scripts\Invoke-WindowsOptimization.ps1 -Mode Audit
.\scripts\Invoke-WindowsOptimization.ps1 -Mode Plan -Profile Performance

# Prévia sem mutação
.\scripts\Invoke-WindowsOptimization.ps1 -Mode Apply -Profile Performance -WhatIf

# Aplicação e verificação
.\scripts\Invoke-WindowsOptimization.ps1 -Mode Apply -Profile Performance -ApprovedActionId <id>
.\scripts\Invoke-WindowsOptimization.ps1 -Mode Verify -StatePath <pasta>

# Rollback
.\scripts\Invoke-WindowsOptimization.ps1 -Mode Restore -StatePath <pasta>
```

## Exemplo

Pedido: “Deixe este notebook extremamente rápido.”

Resposta: auditar, medir, simular, aplicar ações aprovadas e manter ganhos
comprovados.

## Erros comuns

- Executar debloater sem revisar origem.
- Ocultar UAC ou alterar o HKCU errado.
- Contornar ACL OEM.
- Confundir comando bem-sucedido com melhoria medida.
````
