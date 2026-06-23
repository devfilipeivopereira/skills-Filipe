# Diagnóstico e medição

## Ordem de investigação

1. Confirmar Windows, arquitetura, fabricante, modelo e SKU.
2. Capturar BIOS, CPU, RAM, armazenamento, saúde e espaço livre.
3. Medir CPU ociosa, memória disponível, processos e atividade do disco.
4. Inspecionar startup, tarefas, serviços, Appx e aplicativos persistentes.
5. Identificar sincronizadores, acesso remoto, software de segurança e OEM.
6. Inspecionar eventos recentes.
7. Verificar WSL, Hyper-V, Docker e cargas de desenvolvimento.
8. Consultar integridade e atualizações oficiais quando a evidência justificar.

## Métricas

Medir em condição comparável, preferencialmente dez minutos após login e com os
mesmos aplicativos abertos:

- CPU média e pico;
- memória disponível e comprometida;
- quantidade de processos;
- espaço livre e percentual;
- atividade e fila do disco;
- benchmark sustentado em pelo menos três rodadas;
- latência, DNS e rota padrão em experimentos de rede;
- eventos críticos novos;
- saúde do disco e TRIM;
- tempo de boot quando o log Diagnostics-Performance estiver disponível.

## Interpretação

### CPU

CPU ociosa alta exige descobrir o processo, serviço, tarefa ou driver causador.
Não reduzir serviços aleatoriamente. Frequência maior não prova throughput maior;
comparar mediana sustentada.

### Memória

Memória usada por cache não é automaticamente desperdício. Investigar
commit, paginação, working set persistente, VMs, WSL e aplicativos de login.

### Armazenamento

Menos de 12% livre merece ação; menos de 8% é crítico. Priorizar caches
regeneráveis, versões antigas verificadas e hibernação consentida. Nunca
desfragmentar SSD como HDD; usar TRIM/ReTrim.

### Processos

Contagem é indicador, não objetivo absoluto. Preservar segurança, drivers,
hotkeys, acesso remoto e funções aprovadas.

### Eventos

Priorizar:

- bugcheck e Kernel-Power 41;
- disco 7/51/55/129/153;
- Kernel-Processor-Power 37;
- WUDFRd 219 quando ligado a dispositivo funcional;
- Service Control Manager 7000/7009/7011/7031/7034.

Não “corrigir” DCOM 10016 automaticamente.

## Comparação

Calcular mudança percentual:

```text
(depois - antes) / antes * 100
```

Considerar regressão:

- benchmark abaixo do limite configurado;
- latência mais de 50% pior;
- evento crítico novo;
- perda funcional.

Melhora em uma métrica não compensa automaticamente regressão grave em outra.

## Evidência final

Produzir JSON para auditoria e Markdown para leitura. Separar:

- observado;
- planejado;
- aplicado;
- recusado ou não encontrado;
- pendente de reboot;
- verificado;
- restaurado.
