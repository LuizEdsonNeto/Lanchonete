from functions import Clientes, Carnes, Acompanhamentos, Bebidas, Pedidos, Caixa

print("----------------------------------------")
while True:
    menu = {
        1: "Setor Administrativo",
        2: "Garçom",
        3: "sair"
    }
    print("")
    for x in menu:
        if x == 3:
            print(f"Digite '{x}' para {menu[x]}")
        else:
            print(f"Digite '{x}' para acessar a aba '{menu[x]}'")
    print("")

    print("----------------------------------------\n")
    opcao = int(input("Escolha uma opção: "))
    print("")

    if opcao == 1:
        while True:
            print("""----------------------------------------\n
(MENU SETOR ADMINISTRATIVO)
Digite '1' para acessar a aba 'Clientes'
Digite '2' para acessar a aba 'Carnes'
Digite '3' para acessar a aba 'Acompanhamentos'
Digite '4' para acessar a aba 'Bebidas'
Digite '5' para acessar a aba 'Caixa'
Digite '6' para sair
""")

            print("----------------------------------------\n")
            opcao_administrativo = int(input("Escolha uma opção do MENU SETOR ADMINISTRATIVO: "))
            print("")

            if opcao_administrativo == 1:
                print("""----------------------------------------\n
(MENU CLIENTES)
Digite '1' para cadastrar os dados de um cliente
Digite '2' para alterar os dados de um cliente
Digite '3' para consultar os dados dos clientes
Digite '4' para excluir os dados de um cliente
Digite '5' para sair do MENU CLIENTES
""")

                Clientes()
            elif opcao_administrativo == 2:
                print("""----------------------------------------\n
(MENU CADASTRAR CARNES)
Digite '1' para cadastrar uma carne e seu preço
Digite '2' para alterar o preço de uma carne
Digite '3' para consultar as carnes disponíveis e seus preços
Digite '4' para excluir uma carne e seu preço
Digite '5' para sair do MENU CARNES
""")
                Carnes()
            elif opcao_administrativo == 3:
                print("""----------------------------------------\n
(MENU CADASTRAR ACOMPANHAMENTOS)
Digite '1' para cadastrar um acompanhamento e seu preço
Digite '2' para alterar o preço de um acompanhamento
Digite '3' para consultar os acompanhamentos disponíveis e seus preços
Digite '4' para excluir um acompanhamento e seu preço
Digite '5' para sair do MENU ACOMPANHAMENTOS
""")
                Acompanhamentos()
            elif opcao_administrativo == 4:
                print("""----------------------------------------\n
(MENU CADASTRAR BEBIDAS)
Digite '1' para cadastrar uma bebida e seu preço
Digite '2' para alterar o preço de uma bebida
Digite '3' para consultar as bebidas disponíveis e seus preços
Digite '4' para excluir uma bebida e seu preço
Digite '5' para sair do MENU BEBIDAS
""")
                Bebidas()
            elif opcao_administrativo == 5:
                print("""----------------------------------------\n
(MENU CAIXA)
Digite '1' para consultar o caixa
Digite '2' para sair do MENU CAIXA
""")
                Caixa()
            elif opcao_administrativo == 6:
                print("\nSAINDO DO MENU SETOR ADMINISTRATIVO\n\n----------------------------------------")
                break
            else:
                print("\nOpção inválida!\n")
    elif opcao == 2:
            print("""----------------------------------------\n
(MENU GARÇOM)
Digite '1' para anotar o pedido
Digite '2' para sair        
""")

            Pedidos()
    elif opcao == 3:
        break
    else:
        print("\nOpção inválida!\n")