# *Sistema de Controle de Estoque Simplificado (SCES)*
## ~Controle de saída e entrada de almoxarifados.~ 

O Sistema de Controle de Estoque Simplificado (SCES), é um programa de computador feito para ajudar a organizar as mercadorias de um negócio de forma totalmente digital. Ele funciona como uma lista inteligente que roda direto na tela do computador, substituindo os cadernos de papel e as anotações que se perdem facilmente. 
O objetivo principal do sistema é garantir que você nunca mais se perca nas contas do que tem guardado no depósito. Com ele, fica muito fácil saber o nome do produto, o código de identificação (ID), a quantidade exata de cada produto, além de registrar em qual setor cada item está localizado (Setor - n°). 
Outra grande utilidade é o seu sistema de alerta automático, que avisa o usuário se alguma mercadoria estiver acabando, ou seja, com menos de cinco unidades disponíveis, o que evita que o negócio fique sem produtos essenciais para os clientes. 
Para usar o programa é muito simples, pois ele funciona através de um menu interativo com perguntas e respostas diretas na tela. Assim que o usuário abre o sistema, ele é recebido por uma mensagem de boas-vindas e seis opções numeradas. 
Ao digitar:
 + 1- Mostrar Status do Estoque: o programa mostra na tela o status atual de tudo o que está cadastrado;
 + 2- Adicionar Produtos no Estoque: serve para adicionar um produto novo, bastando digitar o código, o nome, a quantidade e o setor dele;
 + 3- Buscar Produto por ID: permite buscar um item específico digitando apenas o seu número de identificação (ID);
 + 4- Atualizar Quantidade do Produto: alterar a quantidade de peças porque chegou mais mercadoria ou porque algo foi vendido;
 + 5- Verificar Quantidade de Produtos no Estoque: faz uma varredura automática para avisar se o estoque está perigosamente baixo (menos de 5 quantidades no estoque);
 + 6- Sair do Menu: fecha o programa com segurança.
O sistema é feito para ser prático, por isso, toda vez que uma tarefa termina, ele pede para o usuário apertar a tecla <Enter> antes de liberar o menu novamente, garantindo que dê tempo de ler todas as informações com calma.

Como funciona cada Função:

A função (adicionar_produto) serve para colocar novos itens na lista, pedindo para o usuário digitar o código de identificação (ID), o nome, a quantidade atual e o setor onde a mercadoria ficará guardada (Setor - n°). 
Para visualizar tudo o que está armazenado, a função (listar_produtos) exibe na tela o relatório completo com todos os itens cadastrados até o momento. 
Quando o estoque fica muito grande, a função (buscar_produto) facilita a localização de um item específico, bastando digitar o número do ID para que o sistema mostre o nome e o setor onde ele está. 
Se houver alguma venda ou chegada de novas mercadorias, a função (atualizar_produto) permite alterar a quantidade exata de um item de forma rápida a partir do seu código. 
Para garantir a segurança das vendas, a função (estoque_minimo) faz uma varredura automática e avisa se algum produto está com menos de cinco unidades, evitando que o estoque zere. 
Por fim, a função (travar_menu) cria uma pausa estratégica no sistema, fazendo o programa esperar que o usuário aperte a tecla Enter para que ele consiga ler as informações na tela com calma antes de voltar ao menu principal. 