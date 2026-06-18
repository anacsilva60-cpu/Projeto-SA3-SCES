produtos = [
    [213, "Volante", 56, "Setor - 09"],
    [145, "Motor Parcial Man", 23, "Setor - 04"],
    [325, "Conjunto Filtro de Ar", 100, "Setor - 01"],
    [567, "Filtro de Combustível", 98, "Setor - 07"],
    [389, "Combustível", 1, "Setor - 12"],
    [101, "Martelo", 2, "Setor - 14"],
]

def adicionar_produto():  #Função de Adicionar Produtos
    global produtos
    id_item = int(input("\nDigite o ID do produto: "))
    nome = input("Digite o nome do produto: ")
    qtd = int(input("Digite a quantidade de produto que tem no estoque: "))
    local = input("Digite o localização do produto em Setor (ex: Setor - n°): ")
    produtos.append([id_item, nome, qtd, local])
    travar_menu()


def listar_produtos(): #Função para listar produtos
    for linha in produtos:
        print(linha)
    travar_menu()

def buscar_produto(): #Função para buscar o produto pelo ID
    global produtos
    buscar_id = int(input("\nDigite o ID do produto para encontrá-lo: "))
    for linha in produtos:
        if buscar_id == linha[0]:
            print(f"\nO Produto procurado é: {linha}")
            break
    else:
        print("\nO seu produto não contém no estoque!")
        print("Adicione um produto para procurá-lo!!")
    travar_menu()

def atualizar_produto(): #Função para Atualizar a Quantidade do Produto, buscando pelo ID
    global produtos
    alterar_Qtd = int(input("\nQual o ID do produto que quer atualizar?: "))
    for i in range(len(produtos)):
        if(produtos[i][0] == alterar_Qtd):
            linha_procurada = i
            print(f"\nO Produto procurado é: {produtos[i][1]}, com quantidade atual de: {produtos[i][2]}")
            nova_Qtd = int(input("Digite a nova quantidade do produto: "))
            produtos[i][2] = nova_Qtd 
            print("\nQuantidade atualizada com sucesso!")
            print(f"A nova quantidade do Produto {produtos[i][1]} é: {nova_Qtd}")
            break
    else:
        print("\nO Produto não foi encontrado!")
    travar_menu()

def travar_menu(): #Função para Travar o Menu
    input("\nPrecione <ENTER> para continuar... ")

def estoque_minimo():
    for linha in produtos:
        if linha[2] < 5:
            print(f"Alerta!! O(s) Produto(s) {linha}, está(ão) com baixa quantidade {linha[2]}")

    print("\nTodos os produtos estão em quantidade maior que 5. Prossiga com o Sistema...")
    travar_menu()

print("\n----> Bem Vindo ao Menu Interativo do Sistema de Controle de Estoque Simplificado (SCES)! Por Favor, selecione uma opção: ")
while True: ##Loop que faz funcionar o sistema de escolha do menu
    print("\n1- Mostrar Status do Estoque | 2- Adicionar Produtos no Estoque | 3- Buscar Produto por ID | 4- Atualizar Quantidade do Produto | 5- Verificar Quantidade de Produtos no Estoque |  6- Sair do Menu ")
    opção = input("Escolha: ")
    if(opção == "1"):
        listar_produtos()
    elif(opção == "2"):
        adicionar_produto()
    elif(opção == "3"):
        buscar_produto()
    elif(opção == "4"):
        atualizar_produto()
    elif(opção == "5"):
        estoque_minimo()
    elif(opção == "6"):
        print("\nSaindo...\n")
        break