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
