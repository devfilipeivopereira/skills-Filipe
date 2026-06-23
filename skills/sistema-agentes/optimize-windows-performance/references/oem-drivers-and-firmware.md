# OEM, drivers e firmware

## Regra central

Firmware e drivers de plataforma são específicos do equipamento. “Mais novo” de
outro fabricante não significa compatível.

## Identificação

Confirmar:

- fabricante;
- modelo comercial;
- `SystemSKUNumber`;
- revisão de placa quando disponível;
- versão e data do BIOS;
- versão, provedor, data e INF do driver instalado;
- alimentação externa e bateria suficiente para firmware.

Se página e hardware divergirem, confiar primeiro no SKU reportado pelo sistema
e reconciliar com a etiqueta/documentação.

## Fontes permitidas

Usar nesta ordem:

1. aplicativo ou portal oficial do fabricante para o SKU;
2. Windows Update, incluindo atualizações opcionais;
3. Microsoft Update Catalog quando o hardware ID e o pacote forem confirmados;
4. fabricante do componente somente quando o OEM autorizar a rota genérica.

Não usar agregadores de drivers.

## Verificação de pacote

Antes de executar:

- verificar URL de origem;
- validar assinatura Authenticode;
- conferir publicador;
- comparar modelo/SKU e hardware IDs;
- determinar se o executável atualiza firmware ou apenas configura o BIOS;
- localizar instruções oficiais e requisitos;
- criar ponto de recuperação quando aplicável;
- fechar cargas e manter alimentação.

Uma ferramenta chamada “BIOS Tools” não é automaticamente um atualizador.

## BIOS

Não:

- gravar BIOS de modelo semelhante;
- forçar downgrade ou cross-flash;
- executar utilitário sem conhecer a função;
- interromper alimentação;
- prometer rollback automático.

Se não houver firmware oferecido pelo OEM ou Windows Update, registrar que
nenhuma atualização compatível foi comprovada.

## Plataforma térmica e energia

Preservar Intel DTT/IPF, AMD platform management, ACPI, sensores e serviços
térmicos OEM. Não instalar pacote de outro notebook para “liberar potência”.

Eventos `Kernel-Processor-Power 37` podem indicar limitação pelo firmware.
Investigar BIOS, perfil OEM, temperatura e drivers oficiais; não desativar
proteções térmicas.

## Ordem de atualização

Quando o fabricante recomendar:

1. BIOS/firmware;
2. chipset e plataforma térmica;
3. gráficos;
4. armazenamento;
5. rede e Bluetooth;
6. sensores, câmera, biometria e áudio.

Reiniciar nos pontos exigidos. Reavaliar eventos, estabilidade e desempenho após
cada grupo; não instalar tudo de uma vez quando for necessário isolar regressão.

## Relatório

Registrar:

- versão anterior e posterior;
- fonte e URL;
- assinatura;
- hardware ID ou SKU;
- necessidade de reboot;
- resultado;
- eventos novos;
- rota de recuperação fornecida pelo fabricante.
