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
### 2.3.1 Botão Nova Reserva
- Botão Localizado na parte superior direita, logo abaixo do Painel Superior, ao clicar a Janela de Escolha de ambiente para cadastrar reserva é aberta. Esta janela possui:
    - 1. Botão "X": Localizado na parte superior direita da janela, ao clicar a janela é fechada.
    - 2. Botão "Cancelar": Localizado na parte inferior direita da janela, ao clicar a janela é fechada.
    - 3. Seletor "Ambiente": Localizado no centro da janela, ao clicar aparece uma lista de ambientes dos quais apenas um pode ser selecionado.
    - 4. Botão "Reservar": Localizado na parte inferior direita da janela, existem 2 comportamentos ao clicar:
        - 1. Seletor "Ambiente" não selecionado: É exibida uma janela de erro na tela
        - 2. Seletor de "Ambiente" selecionado: A janela "Reserva Geral (Confirmação)" é aberta.

### 2.3.2 Caixa de Informações Recepção
- Localizada no centro da página, logo abaixo do botão nova reserva, possui orientações sobre o painel de recepção, as quais são:
    - 1. "Como funciona o Painel de Recepção
    - 2. Nova Reserva Presencial: Use quando alguém chegar presencialmente para reservar um espaço
    - 3. Check-in: Clique em "Compareceu" quando o responsável chegar no horário agendado
    - 4. Ausência: Clique em "Não Compareceu" se a pessoa não aparecer - isso libera o espaço automaticamente
    - 5. Check-out: Libere o espaço antecipadamente quando a reunião terminar antes do previsto"

### 2.3.3. Filtros Recepção
- Localizados centralizados na tela, logo abaixo da Caixa de Informações Recepção, possui 4 caixas de filtros, com o o layout de o número de reservas referentes à aquele filtro e logo abaixo o nome do filtro, sendo elas:
    - 1. Total de Reservas: Localizado na primeira posição da esquerda, ao ser clicado filtra as reservas do dia para todas, mostra o resultado da união de todos os outros filtros.
    - 2. Aguardando Check-in: Localizado na segunda posição da esquerda para a direita, ao ser clicado mostra as reservas que possuem status "Aguardando Check-in".
    - 3. Em uso: Localizado na terceira posição da esquerda para a direita, ao ser clicado mostra as reservas que possuem status "Em uso".
    - 4. Finalizadas: Localizado na quarta posição da esquerda para a direita, ao ser clicado mostra as reservas que possuem status "Finalizadas".
- Logo abaixo das 4 caixas na parte direita existe um filtro seletor que por padrão possui o nome "Todos os ambientes", ao ser clicado mostra uma lista de ambientes para ser selecionado, ao selecionar a página mostra as reservas relacionadas apenas à aquele ambiente. Este filtro pode ser combinado com as caixas de filtro.


# 3. Fluxos de Uso do Sistema
## 3.1. Usuário no total de Reservas
- Usuário abre o sistema, clica no botão painel superior Recepção e é redirecionado para a página de Recepção, na página são exibidas todas as reservas do dia, usuário clica na caixa do filtro "Total de Reservas", a página exibe todas as reservas do dia.

## 3.2 Usuário clica no Aguardando Check-in
- Usuário abre o sistema, clica no botão painel superior Recepção e é redirecionado para a página de Recepção, na página são exibidas todas as reservas do dia, usuário clica na caixa do filtro "Aguardando Check-in", a página exibe todas as reservas do dia com status "Aguardando Check-in".

## 3.3 Usuário clica no Em uso
- Usuário abre o sistema, clica no botão painel superior Recepção e é redirecionado para a página de Recepção, na página são exibidas todas as reservas do dia, usuário clica na caixa do filtro "Em uso", a página exibe todas as reservas do dia com status "Em uso".

## 3.4 Usuário clica no Finalizadas
- Usuário abre o sistema, clica no botão painel superior Recepção e é redirecionado para a página de Recepção, na página são exibidas todas as reservas do dia, usuário clica na caixa do filtro "Finalizadas", a página exibe todas as reservas do dia com status "Finalizadas".

## 3.5 Usuário clica no Filtro de todos os ambientes
- Usuário abre o sistema, clica no botão painel superior Recepção e é redirecionado para a página de Recepção, na página são exibidas todas as reservas do dia, usuário clica no filtro seletor "Todos os ambientes" e seleciona um ambiente, a página exibe todas as reservas relacionadas à aquele ambiente.