produtos = [
    [100, "Volante", 34, "Setor - 01"],
]

def adicionar_produto():
    global produtos
    id_item = int(input("Digite o ID do produto: "))
    nome = input("Digite o nome do produto: ")
    qtd = int(input("Digite a quantidade de produto que tem no estoque: "))
    local = input("Digite o localização do produto: ")
    produtos.append([id_item, nome, qtd, local])
    travar_menu()


def listar_produtos():
    for linha in produtos:
        print(linha)
    travar_menu()

def buscar_produto():
    global produtos
    buscar_id = int(input("Digite o ID do produto para encontrá-lo: "))
    for produto in produtos:
        if produto == buscar_id:
            print("A")
        else:
            print("O seu produto não contém no estoque!")
            print("Adicione um produto para pracurá-lo!!")

buscar_produto()

def travar_menu():
    input("\nPrecione <ENTER> para continuar... ")

print("\n----> Bem Vindo ao Menu Interativo do Sistema de Estoque! Por Favor, selecione uma opção: ")
while True: 
    print("\n1- Mostrar Status do Estoque | 2- Adicionar Produtos no Estoque | 3- Buscar Produto por ID ")
    opção = input("Escolha: ")
    if(opção == "1"):
        listar_produtos()
    elif(opção == "2"):
        adicionar_produto()
    elif(opção == "3"):
        buscar_produto()
