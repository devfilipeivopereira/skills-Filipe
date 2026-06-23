# Platform Integrations

Este diretório documenta como o `kdp-notion-agent` é adaptado para operar como agente dedicado em diferentes ambientes, mantendo o core intacto.

## Objetivo

Permitir que Claude, Gemini, Cursor e Windsurf usem o mesmo núcleo editorial e determinístico do projeto, mas com instruções de entrada específicas para cada plataforma.

## Estratégia

- manter `kdp-notion-agent` como fonte única de verdade
- instalar uma cópia local da skill em cada plataforma
- criar wrappers de agente por plataforma
- adicionar instruções globais de priorização quando a plataforma já tiver arquivo de comportamento global

## Plataformas

- `claude-agent-wrapper.md`
- `gemini-agent-wrapper.md`
- `cursor-agent-wrapper.md`
- `windsurf-agent-wrapper.md`

## Regra de manutenção

Sempre que o core mudar:

1. atualizar o repositório principal
2. sincronizar a skill instalada em cada plataforma
3. revisar se os wrappers ainda estão coerentes com o fluxo atual
