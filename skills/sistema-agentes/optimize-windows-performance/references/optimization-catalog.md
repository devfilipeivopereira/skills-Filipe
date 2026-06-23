# Catálogo adaptativo de otimizações

## Inicialização

- Construir allowlist com segurança, acesso remoto e sincronização aprovados.
- Desativar itens por `StartupApproved`, tarefa ou configuração suportada.
- Manter aplicativo instalado quando o objetivo for uso sob demanda.
- Verificar o estado após novo login.

## Serviços

- Priorizar serviço opcional com falhas repetidas ou timeout comprovado.
- Preferir `Manual` a `Disabled` para recurso ocasional.
- Usar `Disabled` apenas quando o recurso foi removido ou rejeitado.
- Preservar RPC, Event Log, Defender, Firewall, Update, Search e serviços de
  driver/energia.
- Não inferir dispensabilidade somente pelo nome.

## Aplicativos e debloat

- Revisar origem, tag/commit, opções e logs de ferramentas de terceiros.
- Criar restore point quando suportado e sempre salvar estado próprio.
- Separar pacote do usuário, provisionamento e política.
- Preservar componentes centrais mesmo quando o nome contiver “AI”.
- Registrar como reinstalar pacotes removidos.

## Armazenamento

Allowlist típica:

- temporários antigos;
- npm, uv, pip e caches de compilação;
- D3DSCache;
- logs antigos de aplicativos;
- versões antigas confirmadas, preservando a versão atual;
- journals WSL acima do limite;
- caches de modelos somente com consentimento.

Preservar:

- Downloads, Documents e projetos;
- sessões, cookies, senhas e extensões;
- rascunhos e bancos locais;
- dumps recentes;
- imagens, volumes e ambientes de VM/containers sem autorização.

## Integridade e SSD

Usar conforme necessidade:

```powershell
DISM /Online /Cleanup-Image /CheckHealth
DISM /Online /Cleanup-Image /StartComponentCleanup
DISM /Online /Cleanup-Image /RestoreHealth
SFC /verifyonly
SFC /scannow
CHKDSK C: /scan
Optimize-Volume -DriveLetter C -ReTrim
```

Não executar todos por ritual. Registrar exit code e logs.

## Energia e CPU

- Manter máximo de CPU em 100% quando desempenho for requisito.
- Manter mínimo baixo o suficiente para ocioso eficiente.
- Preservar thermal throttling, estados ociosos e Hyper-Threading.
- Alterar EPP/boost somente como experimento com backup.
- Medir pelo menos três rodadas e restaurar regressão.
- Não copiar GUIDs ou valores de outro processador sem confirmar suporte.

## WSL e desenvolvimento

- Detectar distribuições e cargas ativas.
- Considerar `autoMemoryReclaim=gradual`.
- Usar `journalctl --vacuum-size` e `fstrim` quando apropriado.
- Encerrar WSL somente com coordenação.
- Não apagar ambientes, imagens, volumes ou modelos sem inventário.

## Background e OEM

- Preferir controles suportados de background e execução sob demanda.
- Preservar hotkeys, sensores, thermal framework e utilitário de configurações.
- Testar Quick Share, Find, Multi Control ou equivalentes após mudança.
- Se ACL protegida impedir ajuste, registrar e escolher outro ponto suportado.

## Navegadores

- Desativar Startup Boost e background apenas quando o usuário não depende deles.
- Limpar somente caches regeneráveis.
- Preservar perfis, histórico, cookies, senhas, extensões e sessões.
