# 1. Descrição Geral do Sistema
- O sistema, SisAmbiente, tem como objetivo gerenciar as reservas de espaços dentro do Tribunal de Contas da União, dando possibilidade para que os usuários verifiquem a disponibilidade e façam a reserva de diferentes tipos de espaços como auditórios, salas de aula, salas de reunião e etc. Cada espaço pode ou não possuir regras de uso próprias.

# 2. Localização de Itens no Sistema
-----
## 2.1. Painel Superior
- Painel localizado na parte superior presente em todas as páginas do sistema, logo abaixo da logo do TCU e do nome do sistema (SisAmbiente), o painel possui 5 botões, sendo eles os seguintes:
    - 1. Painel de Reservas:
        - 
    - 2. Consulta Avançada:
        - 
    - 3. Minhas reservas:
        - 
    - 4. Recepção:
        - O botão redireciona para a página Recepção, acessível apenas pelo perfil de recepcionista.
    - 5. Configurações:
        - 

## 2.2. Itens da Página Inicial
### 2.2.1. Botões da Região Inferior
- 2 Botões localizados no inferior da tela, sendo eles:
    - 1. Regras de uso:
        - O botão redireciona para uma página que descreve as regras gerais que cada ambiente do sistema possui.
    - 2. -> Acesso rápido:
        - O botão redireciona para a página de consulta e reserva de ambientes geral do sistema, acessível para todos os perfis de usuário.

## 2.3. Itens da Página Recepção

### 2.3.1 Botão Nova Reserva Presencial
- Botão Localizado na parte superior direita com o horário e data do dia ao lado, logo abaixo do Painel Superior, ao clicar a Janela de Escolha de ambiente para cadastrar reserva é aberta. Esta janela possui:
    - 1. Botão "X": Localizado na parte superior direita da janela, ao clicar a janela é fechada.
    - 2. Botão "Cancelar": Localizado na parte inferior direita da janela, ao clicar a janela é fechada.
    - 3. Seletor "Ambiente": Localizado no centro da janela, ao clicar aparece uma lista de ambientes dos quais apenas um pode ser selecionado.
    - 4. Botão "Reservar": Localizado na parte inferior direita da janela, existem 2 comportamentos ao clicar:
        - 1. Seletor "Ambiente" não selecionado: É exibida uma janela de erro na tela
        - 2. Seletor de "Ambiente" selecionado: A janela "Reserva Geral (Confirmação)" é aberta.
### 2.3.2. Seletor de Calendário e Tabela
- Localizado na lateral superior Esquerda, abaixo do título "Painel de Recepção", é um botão do tipo Toggle (Alternar) onde se pode escolher entre "Tabela" ou "Calendário".
    - 1. Tabela: A tela segue sem alteração da visualização inicial.
    - 2. Calendário: Aparece na tela um calendário com as reservas da semana.
    
#### 2.3.2.1 Calendário de Reservas da Semana:
- 

### 2.3.3. Busca de Reserva:
- Localizado no lado direito superior, logo abaixo do botão Nova Reserva Presencial, possui 2 campos que podem ou não ser preenchidos:
    - 1. Buscar por responsável: Deve ser digitado o nome do responsável pela reserva.
    - 2. Filtro por ambiente, ao clicar se abre uma seleção onde se deve escolher o ambiente pelo qual se quer filtrar.

### 2.3.4. Filtros Recepção
- Localizados centralizados na tela, logo abaixo da Caixa de Informações Recepção, possui 4 caixas de filtros, com o o layout de o número de reservas referentes à aquele filtro e logo abaixo o nome do filtro, sendo elas:
    - 1. Total de Reservas: Localizado na primeira posição da esquerda, ao ser clicado filtra as reservas do dia para todas, mostra o resultado da união de todos os outros filtros.
    - 2. Aguardando Check-in: Localizado na segunda posição da esquerda para a direita, ao ser clicado mostra as reservas que possuem status "Aguardando Check-in".
    - 3. Em uso: Localizado na terceira posição da esquerda para a direita, ao ser clicado mostra as reservas que possuem status "Em uso".
    - 4. Finalizadas: Localizado na quarta posição da esquerda para a direita, ao ser clicado mostra as reservas que possuem status "Finalizadas".

### 2.3.5. Caixa de Cards de Reserva:
- Localizado no centro da página, logo abaixo dos filtros, possui um título com a data atual + "Todas as Reservas" e o número de reservas do dia e logo abaixo do mesmo diversos cards que representam cada reserva. Os cards são divididos em 3 colunas:
    - 1. Reserva: Possui o nome do ambiente reservado, nome e foto do teams do responsável pela reserva, horário reservado e, caso exista, horário do check-in e check-out.
    - 2. Status: Possui um dos seguintes status relacionado a reserva: Check-in Confirmado (Fundo do card fica verde), Aguardando Check-in (Fundo do card branco) e Finalizado (Fundo do card fica cinza).
    - 3. Ações: Possui 3 ou 2 botões clicáveis pelo usuário, variando pelo status da reserva.

#### 2.3.5.1. Cards de Reserva
- Localizado dentro da Caixa de Cards de Reserva, os cards ficam empilhados um em cima do outro, em formato de lista, entre as colunas Status e Ações existe uma caixa azul de Observação que pode ou não aparecer, dependendo se foi cadastrada uma observação ou não na reserva, os botões de Ações se modificam a depender do status da reserva da seguinte forma:
##### 2.3.5.1.1. Botões Card de Reserva com Status Aguardando Check-in
- 1. Check-in: Botão possui o ícone de um usuário, o fundo verde e um ícone de check, ao clicar o status da reserva e alterado para Check-in Confirmado.
- 2. Não compareceu: Botão possui o ícone de um usuário, fundo vermelho e um ícone de check, ao clicar a reserva é cancelada.
- 3. Observação: Botão possui o ícone de um balão de fala com fundo cinza, ao clicar se abre uma caixa para adicionar ou editar uma observação feita à respeito da reserva, caso exista uma observação já feita uma bolinha azul aparece em cima do ícone.
##### 2.3.5.1.2. Botões Card de Reserva com Status Check-in Confirmado
- 1. Check-out: Botão possui o ícone de uma porta de saída e o fundo azul, ao clicar o status da reserva e alterado para Finalizado.
- 2. Desfazer: Botão possui o ícone de uma seta circular e fundo laranja, ao clicar o status da reserva volta para Aguardando Check-in.
- 3. Observação: Botão possui o ícone de um balão de fala com fundo cinza, ao clicar se abre uma caixa para adicionar ou editar uma observação feita à respeito da reserva, caso exista uma observação já feita uma bolinha azul aparece em cima do ícone.
##### 2.3.5.1.3. Botões Card de Reserva com Status Finalizado
- 1. Desfazer: Botão possui o ícone de uma seta circular e fundo laranja, ao clicar o status da reserva volta para Check-in Confirmado.
- 2. Observação: Botão possui o ícone de um balão de fala com fundo cinza, ao clicar se abre uma caixa para adicionar ou editar uma observação feita à respeito da reserva, caso exista uma observação já feita uma bolinha azul aparece em cima do ícone.


### 2.3.6. Caixa de Informações Recepção
- Localizada no centro da página, logo abaixo dos cards de reserva, possui orientações sobre o painel de recepção, as quais são:
    - 1. • O sistema envia notificação automática via Teams 30 minutos antes da reserva
    - 2. • Clique em "Compareceu" quando o responsável chegar na recepção para confirmar o check-in
    - 3. • Clique em "Não Compareceu" se a pessoa não aparecer no horário - isso libera o espaço
    - 4. • O botão "Check-out" permite liberar o espaço antecipadamente quando a reunião terminar antes
    - 5. • Espaços liberados antecipadamente ficam disponíveis imediatamente para novas reservas

### 2.3.7. Reserva Geral (Confirmação)
- É uma janela que possui as informações para uma nova reserva, existem informações estáticas e informações para serem preechidas, são elas:
    - 1. Cabeçalho: Possui o tipo de ambiente, a data da reserva e o status "Confirmação Imediata".
    - 2. Ambiente Selecionado: Possui as informações detalhadas do ambiente, Localização, nome e capacidade máxima.
    - 3. Informações da Reserva: Unidade Demandante, Colaborador Responsável, E-mail do Responsável, Telefone do Responsável, onde todos os dados do responsável são transferidos para o usuário que está criando a reserva.
    - 4. Data e Horário: Informações à serem preenchidas, os campos são: Data Início, Hora Início e Hora Fim, variando com o tipo de regras de cada ambiente. São campos obrigatórios
    - 5. Detalhes da Resreva: Informações à serem preenchidas, Finalidade da Reserva e Observações. São Campos Opcionais.
    - 6. Alguns outros campos podem aparecer, à depender do tipo de ambiente sendo obrigatórios ou opcionais.
- Logo abaixo estão 2 botões:
    - 1. Cancelar: Cancela a criação da reserva.
    - 2. Prosseguir para a confirmação: Abre a janela de Confirmar Reserva.

### 2.3.8. Janela de Confirmar Reserva
- É uma janela com as informações da reserva, possui as informações de local, capacidade máxima, detalhes da reserva e colaborador responsável. Logo abaixo existem 3 botões:
    - 1. Voltar e Editar (Botão branco): Volta para a tela anterior, "Reserva Geral (Confirmação)" para editar a reserva.
    - 2. Voltar para a consulta e reserva (Botão branco): Fecha a janela e volta para  tela de "Painel de Reservas".
    - 3. Confirmar (Botão Azul): Finaliza a reserva e redireciona para a tela de "Minhas Reservas"


# 3. Fluxos de Uso do Sistema

-----

## 3.1. Fluxos Recepcionista 
- Usuário abre o sistema, clica no botão painel superior Recepção e é redirecionado para a página de Recepção, a partir daqui os fluxos subsequentes se iniciam. Ressalatando que os diferentes os filtros e as buscas podem ser utilizados em conjunto. Nesta seção entende-se por usuário os recepcionistas que utilizam o sistema.

### 3.1.1. Recepcionista clica no filtro total de Reservas
- São exibidas todas as reservas do dia, usuário clica na caixa do filtro "Total de Reservas", a página exibe todas as reservas do dia.

### 3.1.2. Recepcionista clica no filtro Aguardando Check-in
- São exibidas todas as reservas do dia, usuário clica na caixa do filtro "Aguardando Check-in", a página exibe todas as reservas do dia com status "Aguardando Check-in".

### 3.1.3. Recepcionista clica no filtro Em uso
- São exibidas todas as reservas do dia, usuário clica na caixa do filtro "Em uso", a página exibe todas as reservas do dia com status "Em uso".

### 3.1.4. Recepcionista clica no filtro Finalizadas
- São exibidas todas as reservas do dia, usuário clica na caixa do filtro "Finalizadas", a página exibe todas as reservas do dia com status "Finalizadas".

### 3.1.5. Recepcionista clica na Busca de todos os ambientes
- São exibidas todas as reservas do dia, usuário clica no filtro seletor "Todos os ambientes" e seleciona um ambiente, a página exibe todas as reservas relacionadas à aquele ambiente.

### 3.1.6. Recepcionista clica na Busca por responsável
- São exbidas todas as reservas do dia, usuário clica no campo "Buscar por Responsável" e digita o nome da pessoa que ele deseja saber sobre as reservas, a página exibe as reservas relacionadas à aquele usuário.

### 3.1.7. Recepcionista faz Check-in na reserva
- Dentro da caixa de cards de reserva são exibidos os cards de reserva do dia, o usuário verifica as reservas com status "Aguardando Check-in", localiza a reserva que deseja modificar, clica no botão de Check-in, o usuário entrega a chave para o responsável pela reserva e o sistema atualiza o status da reserva para "Check-in confirmado".

### 3.1.8. Recepcionista faz Check-out na reserva
- Dentro da caixa de cards de reserva são exibidos os cards de reserva do dia, o usuário verifica as reservas com status "Check-in confirmado", localiza a reserva que deseja modificar, clica no botão de Check-out, o usuário recebe a chave do responsável pela reserva e o sistema atualiza o status da reserva para "Finalizado".

### 3.1.9. Recepcionista Registra Ausência na reserva
- Dentro da caixa de cards de reserva são exibidos os cards de reserva do dia, o usuário verifica as reservas com status "Aguardando Check-in" cujo o horário já passou, a depender das regras definidas pelo gestor do ambiente o tempo de tolerância pode mudar isto fica a cargo de cada gestor, usuário clica no botão de Não Compareceu, o sistema atualiza o status da reserva para "Finalizado" e cancela a reserva.

### 3.1.10. Recepcionista Desfaz Check-in na reserva
- Dentro da caixa de cards de reserva são exibidos os cards de reserva do dia, o usuário verifica as reservas com status "Check-in confirmado", localiza a reserva que deseja modificar, clica no botão de Desfazer, o sistema altera o status da reserva para "Aguardando Check-in"

### 3.1.11. Recepcionista Desfaz Check-out na reserva
- Dentro da caixa de cards de reserva são exibidos os cards de reserva do dia, o usuário verifica as reservas com status "Finalizado", localiza a reserva que deseja modificar, clica no botão de Desfazer, o sistema altera o status da reserva para "Check-in Confirmado"

### 3.1.12. Recepcionista Adiciona Observação na reserva
- Dentro da caixa de cards de reserva são exibidos os cards de reserva do dia, localiza a reserva que deseja adicionar observação, clica no botão de Observação, uma janela com um campo texto para adicionar a observação é aberta, o usuário digita a observação que deseja adicionar e clica em (Botão para salvar Observação), o sistema salva a observação e passa a exibir entre as colunas de Status e Ações um caixa de texto com o fundo azul descrevendo a observação.

### 3.1.13. Recepcionista Edita Observação na reserva
- Dentro da caixa de cards de reserva são exibidos os cards de reserva do dia, localiza a reserva que deseja editar a observação, clica no botão de Observação, uma janela com um campo texto para adicionar a observação é aberta, o usuário altera a observação e clica em (Botão para salvar Observação), o sistema salva a observação e passa a exibir entre as colunas de Status e Ações um caixa de texto com o fundo azul descrevendo a observação já alterada.

### 3.1.13. Recepcionista Cria Reserva no Balcão, Fluxo Completo
- O usuário precisa fazer uma reserva com alguém presencialmente, usuário clica no botão "Nova Reserva(Presencial)", janela com opção de "Escolha o ambiente para cadastrar reserva" aparece, o usuário seleciona um ambiente, clica no botão "Reservar (Azul)", janela "Reserva Geral (Confirmação)" é aberta, o usuário preenche os campos obrigatórios e/ou opcionais, clica no botão "Prosseguir para Confirmação (Azul)", Janela de "Confirmar Reserva" é aberta, usuário clica no botão "Confirmar Reserva (Azul)", o sistema salva a reserva e redireciona o usuário para a página de Minhas Reservas.

### 3.1.14. Recepcionista Cria Reserva no Balcão, Fluxo Cancelar etapa 1
- O usuário precisa fazer uma reserva com alguém presencialmente, usuário clica no botão "Nova Reserva(Presencial)", janela com opção de "Escolha o ambiente para cadastrar reserva" aparece, o usuário seleciona um ambiente, clica no botão "Cancelar (Branco)", a janela é fechada e retorna ao painel de recepção.

### 3.1.15. Recepcionista Cria Reserva no Balcão, Fluxo Cancelar etapa 2
- O usuário precisa fazer uma reserva com alguém presencialmente, usuário clica no botão "Nova Reserva(Presencial)", janela com opção de "Escolha o ambiente para cadastrar reserva" aparece, o usuário seleciona um ambiente, clica no botão "Reservar (Azul)", janela "Reserva Geral (Confirmação)" é aberta, o usuário preenche ou não os campos obrigatórios e/ou opcionais, clica no botão "Cancelar (Branco)", a janela é fechada e retorna ao painel de recepção.

### 3.1.16. Recepcionista Cria Reserva no Balcão, Fluxo Cancelar etapa 3
- O usuário precisa fazer uma reserva com alguém presencialmente, usuário clica no botão "Nova Reserva(Presencial)", janela com opção de "Escolha o ambiente para cadastrar reserva" aparece, o usuário seleciona um ambiente, clica no botão "Reservar (Azul)", janela "Reserva Geral (Confirmação)" é aberta, o usuário preenche os campos obrigatórios e/ou opcionais, clica no botão "Prosseguir para Confirmação (Azul)", o usuário clica no botão "Voltar para a consulta e reserva (Branco)", a janela é fechada e retorna ao painel de recepção.

### 3.1.16. Recepcionista Cria Reserva no Balcão, Fluxo Editar etapa 3
- O usuário precisa fazer uma reserva com alguém presencialmente, usuário clica no botão "Nova Reserva(Presencial)", janela com opção de "Escolha o ambiente para cadastrar reserva" aparece, o usuário seleciona um ambiente, clica no botão "Reservar (Azul)", janela "Reserva Geral (Confirmação)" é aberta, o usuário preenche os campos obrigatórios e/ou opcionais, clica no botão "Prosseguir para Confirmação (Azul)", o usuário clica no botão "Voltar e Editar (Branco)", o sistema redireciona para a janela "Reserva Geral (Confirmarção)" e a partir daqui outros fluxos que envolvam esta tela podem acontecer, incluindo este próprio.

### 3.1.17. Recepcionista Alterna Para Visualização em Calendário.
- O usuário clica no seletor de Tabela ou Calendário e seleciona calendário, o botão ficará azul e com a bolinha na direita, o sistema exibirá o Calendário de Reservas da Semana, exibindo todas as reservas da semana logo acima dos cards de reserva.

### 3.1.17.1. Recepcionista Navega Pelo Calendário.
- O usuário clica nas setas do calendário, para a esquerda ele volta uma semana e para direita ele avança uma semana no tempo.

### 3.1.17.2. Recepcionista Navega Pelo Calendário e Retorna Para a Data Atual.
- O usuário clica nas setas do calendário, em algum ponto ele resolve ver as reservas do dia atual, usuário clica no botão "Semana Atual (Branco), o sistema exibe o calendário mostrando a data atual.

### 3.1.17.3. Recepcionista Alterna Para Visualização em Tabela.
- Com o seletor de Tabela ou Calendário em calendário, o usuáro clica novamente e alterna para modo tabela, o sistema deixará de exibir o Calendário de Reservas da Semana.