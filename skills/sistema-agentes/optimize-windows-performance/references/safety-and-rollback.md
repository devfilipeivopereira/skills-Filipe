# Segurança, consentimento e rollback

## Princípio

Nenhuma mutação precede o inventário, o plano validado e o backup. O usuário
autoriza o objetivo; escolhas que removem funções continuam exigindo
consentimento explícito.

## Gates

### Gate de plataforma

- Aplicar automaticamente somente em Windows 11 x64.
- No Windows 10, limitar a ações cuja compatibilidade foi confirmada.
- Não aplicar em Windows Server, Windows ARM, WinPE ou máquina gerenciada pela
  organização sem revisar políticas.

### Gate funcional

Pedir decisão antes de alterar:

- sincronizadores;
- acesso remoto não assistido;
- hibernação e Fast Startup;
- Xbox/Game Bar;
- impressão, Bluetooth, câmera, biometria e localização;
- WSL, Hyper-V, Docker e ferramentas de desenvolvimento;
- serviços ou aplicativos OEM;
- modelos locais, caches grandes e dados que podem custar tempo ou banda para
  baixar novamente.

### Gate administrativo

- Usar elevação visível com `Start-Process -Verb RunAs -WindowStyle Normal`.
- Retornar `.ExitCode` do processo elevado.
- Não reduzir UAC nem alterar suas políticas para evitar prompts.
- Informar o usuário quando a janela do UAC precisar de interação.

## Ações proibidas

- Desativar Defender, Firewall, Windows Update ou UAC.
- Desativar DEP, ASLR, CFG, proteção de pilha ou mitigações equivalentes.
- Desativar pagefile.
- Apagar Prefetch, todos os eventos ou `SoftwareDistribution` como “limpeza”.
- Remover Edge ou componentes centrais do shell por padrão.
- Desativar Search ou SysMain sem evidência específica.
- Tomar posse de ACL de serviço, driver ou chave OEM.
- Instalar firmware ou driver térmico de outro modelo/OEM.
- Matar processos por padrões genéricos.
- Apagar dados pessoais sob o rótulo de cache.

## Estado mínimo

Antes da primeira alteração, exigir:

- `manifest.json`;
- `plan.json`;
- `inventory-before.json`;
- `baseline-before.json`;
- `services-before.json`;
- `tasks-before.json`;
- `packages-before.json`;
- `power-before.txt`;
- exportações de startup disponíveis;
- diretório de logs.

O manifesto deve listar artefatos obrigatórios e ações sem rollback automático.

## Aplicação

- Usar `ShouldProcess`.
- Aplicar uma categoria por vez.
- Registrar `Applied`, `NotFound`, `AccessDenied`, `ConsentRequired` ou
  `ManualReviewRequired`.
- Considerar acesso negado OEM um resultado, não uma falha a ser contornada.
- Validar tarefa agendada consultando-a após o registro.
- Usar nomes exatos e passes limitados para processos que reaparecem.

## Rollback

Restaurar quando houver:

- benchmark sustentado abaixo do limite;
- latência ou DNS significativamente piores;
- novos eventos críticos;
- perda de função aprovada como requisito;
- falha parcial que deixe estado inconsistente.

Não prometer rollback automático de:

- pacote Appx removido;
- driver atualizado;
- BIOS/firmware;
- dado apagado.

Para esses casos, explicar previamente a rota de reinstalação ou recuperação.
