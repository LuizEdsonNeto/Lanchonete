import csv
import os
import re
def Clientes():
    while True:
        print("----------------------------------------\n")
        opcao = int(input("Digite uma opção do MENU CLIENTES: "))
        print("\n")
        if opcao == 1:
            while True:
                nome = input("Digite o nome do cliente: ")
                numero = input("Digite o numero de celular do cliente (no formato (XX) 9XXXX-XXXX): ")
                if re.match(r'^\(\d{2}\) 9\d{4}-\d{4}$', numero):
                    data = input("Digite a data de nascimento do cliente (no formato DD/MM/AAAA): ")
                    if re.match(r'^\d{2}/\d{2}/\d{4}$', data):
                        dados = [nome, numero, data, '0']

                        if os.path.exists("Arquivos/Clientes.csv"):
                            with open('Arquivos/Clientes.csv', 'r', newline='', encoding='utf-8') as arquivo:
                                r = csv.reader(arquivo)

                                dados_antigos = [x for x in r]

                            encontrado = False
                            for x in dados_antigos:
                                if x[0] == nome and x[1] == numero:
                                    encontrado = True

                            if encontrado == False:
                                with open('Arquivos/Clientes.csv', 'a', newline='', encoding='utf-8') as arquivo:
                                    dado = csv.writer(arquivo)
                                    dado.writerow(dados)
                            else:
                                print("\nJá há cliente cadastrado com esse nome e número!")
                        else:
                            with open('Arquivos/Clientes.csv', 'w', newline='', encoding='utf-8') as arquivo:
                                dado = csv.writer(arquivo)
                                dado.writerow(dados)
                    else:
                        print("\nFormato de data inválido!")
                else:
                    print("\nFormato de número inválido!")

                continuar = input("\nDeseja continuar (S ou N): ")
                print("")
                if continuar == 'N':
                    break
            print("Inclusão feita com sucesso!\n")
        elif opcao == 2:
            if os.path.exists("Arquivos/Clientes.csv"):
                while True:
                    with open('Arquivos/Clientes.csv', 'r', newline='', encoding='utf-8') as arquivo:
                        r = csv.reader(arquivo)

                        dados = [x for x in r]

                    nome = input("Digite o nome do cliente que terá os dados alterados: ")
                    numero = input("Digite o número do cliente que terá os dados alterados: ")

                    encontrado = False
                    for x in dados:
                        if x[0] == nome and x[1] == numero:
                            encontrado = True
                            x[0] = input("\nDigite o novo dado de nome do cliente: ")
                            x[1] = input("Digite o novo dado de número de celular do cliente (no formato (XX) 9XXXX-XXXX): ")
                            if re.match(r'^\(\d{2}\) 9\d{4}-\d{4}$', x[1]):
                                x[2] = input("Digite o novo dado de data de nascimento do cliente (no formato DD/MM/AAAA): ")
                                if re.match(r'^\d{2}/\d{2}/\d{4}$', x[2]):
                                    with open('Arquivos/Clientes.csv', 'w', newline='', encoding='utf-8') as arquivo:
                                        w = csv.writer(arquivo)
                                        w.writerows(dados)
                                    print("\nAlteração feita com sucesso!\n")
                                else:
                                    print("\nFormato de data inválido!\n")
                            else:
                                print("\nFormato de número inválido!\n")

                    if encontrado == False:
                        print("\nNão há cliente cadastrado com esse nome e número!\n")

                    continuar = input("Deseja continuar (S ou N): ")
                    print("")
                    if continuar == 'N':
                        break
            else:
                print("Nenhum cliente cadastrado!\n")
        elif opcao == 3:
            if os.path.exists("Arquivos/Clientes.csv"):
                with open('Arquivos/Clientes.csv', 'r', newline='', encoding='utf-8') as arquivo:
                    dados = csv.reader(arquivo)

                    for x in dados:
                        print(f"Nome: {x[0]}, Número: {x[1]}, Nascimento: {x[2]}, Valor gasto: R$ {x[3]}\n")
            else:
                print("Nenhum cliente cadastrado!\n")
        elif opcao == 4:
            if os.path.exists("Arquivos/Clientes.csv"):
                while True:
                    nome = input("Digite o nome do cliente que terá os dados apagados: ")
                    numero = input("Digite o número do cliente que terá os dados apagados: ")

                    dados = []
                    encontrado = False

                    with open('Arquivos/Clientes.csv', 'r', newline='', encoding='utf-8') as arquivo:
                        r = csv.reader(arquivo)
                        for x in r:
                            if x[0] == nome and x[1] == numero:
                                encontrado = True
                            else:
                                dados.append(x)
                    if not encontrado:
                        print("\nPessoa não cadastrada!\n")
                    else:
                        with open('Arquivos/Clientes.csv', 'w', newline='', encoding='utf-8') as arquivo:
                            w = csv.writer(arquivo)
                            w.writerows(dados)
                        print("\nExclusão feita com sucesso!\n")

                    continuar = input("Deseja continuar (S ou N): ")
                    print("")
                    if continuar == 'N':
                        break
            else:
                print("Nenhum cliente cadastrado!\n")
        elif opcao == 5:
            print("SAINDO DO MENU CLIENTES\n")
            break
        else:
            print("Opção inválida!\n")

def Carnes():
    while True:
        print("----------------------------------------\n")
        opcao = int(input("Digite uma opção do MENU CARNES: "))
        print("\n")
        if opcao == 1:
            while True:
                nome = input("Digite o nome da carne: ")
                preco = input("Digite o preco da carne: ")

                if os.path.exists("Arquivos/Carnes.csv"):
                    with open('Arquivos/Carnes.csv', 'r', newline='', encoding='utf-8') as arquivo:
                        dados = csv.reader(arquivo)

                        encontrado = False
                        for x in dados:
                            if x[0] == nome:
                                encontrado = True
                                break

                    if encontrado == True:
                        print("\nCarne já cadastrada!")
                    else:
                        dados = [nome, preco]
                        with open('Arquivos/Carnes.csv', 'a', newline='', encoding='utf-8') as arquivo:
                            dado = csv.writer(arquivo)
                            dado.writerow(dados)
                else:
                    dados = [nome, preco]
                    with open('Arquivos/Carnes.csv', 'w', newline='', encoding='utf-8') as arquivo:
                        dado = csv.writer(arquivo)
                        dado.writerow(dados)

                continuar = input("\nDeseja continuar (S ou N): ")
                print("")
                if continuar == 'N':
                    break
            print("Inclusão feita com sucesso!\n")
        elif opcao == 2:
            if os.path.exists("Arquivos/Carnes.csv"):
                while True:
                    with open('Arquivos/Carnes.csv', 'r', newline='', encoding='utf-8') as arquivo:
                        r = csv.reader(arquivo)

                        dados = [x for x in r]

                    nome = input("Digite o nome da carne que terá o preço alterado: ")

                    encontrado = False
                    for x in dados:
                        if x[0] == nome:
                            x[1] = input("\nDigite o novo preço da carne: ")
                            encontrado = True

                    if encontrado != True:
                        print("\nCarne não cadastrada!\n")
                    else:
                        with open('Arquivos/Carnes.csv', 'w', newline='', encoding='utf-8') as arquivo:
                            w = csv.writer(arquivo)
                            w.writerows(dados)
                        print("\nAlteração feita com sucesso!\n")

                    continuar = input("Deseja continuar (S ou N): ")
                    print("")
                    if continuar == 'N':
                        break
            else:
                print("Nenhuma carne e preço cadastrados!\n")
        elif opcao == 3:
            if os.path.exists("Arquivos/Carnes.csv"):
                with open('Arquivos/Carnes.csv', 'r', newline='', encoding='utf-8') as arquivo:
                    dados = csv.reader(arquivo)

                    for x in dados:
                        print(f"Carne: {x[0]}, Preço: R$ {x[1]}\n")
            else:
                print("Nenhuma carne e preço cadastrados!\n")
        elif opcao == 4:
            if os.path.exists("Arquivos/Carnes.csv"):
                while True:
                    nome = input("Digite o nome da carne que será apagada: ")

                    dados = []
                    encontrado = False

                    with open('Arquivos/Carnes.csv', 'r', newline='', encoding='utf-8') as arquivo:
                        r = csv.reader(arquivo)
                        for x in r:
                            if x[0] == nome:
                                encontrado = True
                            else:
                                dados.append(x)
                    if not encontrado:
                        print("\nCarne não cadastrada!\n")
                    else:
                        with open('Arquivos/Carnes.csv', 'w', newline='', encoding='utf-8') as arquivo:
                            w = csv.writer(arquivo)
                            w.writerows(dados)
                        print("\nExclusão feita com sucesso!\n")

                    continuar = input("Deseja continuar (S ou N): ")
                    print("")
                    if continuar == 'N':
                        break
            else:
                print("Nenhuma carne e preço cadastrados!\n")
        elif opcao == 5:
            print("SAINDO DO MENU CARNES\n")
            break
        else:
            print("Opção inválida!\n")

def Acompanhamentos():
    while True:
        print("----------------------------------------\n")
        opcao = int(input("Digite uma opção do MENU ACOMPANHAMENTOS: "))
        print("\n")
        if opcao == 1:
            while True:
                nome = input("Digite o nome do acompanhamento: ")
                preco = input("Digite o preco do acompanhamento: ")

                if os.path.exists("Arquivos/Acompanhamentos.csv"):
                    with open('Arquivos/Acompanhamentos.csv', 'r', newline='', encoding='utf-8') as arquivo:
                        dados = csv.reader(arquivo)

                        encontrado = False
                        for x in dados:
                            if x[0] == nome:
                                encontrado = True
                                break

                    if encontrado == True:
                        print("\nAcompanhamento já cadastrado!")
                    else:
                        dados = [nome, preco]
                        with open('Arquivos/Acompanhamentos.csv', 'a', newline='', encoding='utf-8') as arquivo:
                            dado = csv.writer(arquivo)
                            dado.writerow(dados)
                else:
                    dados = [nome, preco]
                    with open('Arquivos/Acompanhamentos.csv', 'w', newline='', encoding='utf-8') as arquivo:
                        dado = csv.writer(arquivo)
                        dado.writerow(dados)

                continuar = input("\nDeseja continuar (S ou N): ")
                print("")
                if continuar == 'N':
                    break
            print("Inclusão feita com sucesso!\n")
        elif opcao == 2:
            if os.path.exists("Arquivos/Acompanhamentos.csv"):
                while True:
                    with open('Arquivos/Acompanhamentos.csv', 'r', newline='', encoding='utf-8') as arquivo:
                        r = csv.reader(arquivo)

                        dados = [x for x in r]

                    nome = input("Digite o nome do acompanhamento que terá o preço alterado: ")

                    encontrado = False
                    for x in dados:
                        if x[0] == nome:
                            x[1] = input("\nDigite o novo preço do acompanhamento: ")
                            encontrado = True

                    if encontrado != True:
                        print("\nAcompanhamento não cadastrado!\n")
                    else:
                        with open('Arquivos/Acompanhamentos.csv', 'w', newline='', encoding='utf-8') as arquivo:
                            w = csv.writer(arquivo)
                            w.writerows(dados)
                        print("\nAlteração feita com sucesso!\n")

                    continuar = input("Deseja continuar (S ou N): ")
                    print("")
                    if continuar == 'N':
                        break
            else:
                print("Nenhum acompanhamento e preço cadastrados!\n")
        elif opcao == 3:
            if os.path.exists("Arquivos/Acompanhamentos.csv"):
                with open('Arquivos/Acompanhamentos.csv', 'r', newline='', encoding='utf-8') as arquivo:
                    dados = csv.reader(arquivo)

                    for x in dados:
                        print(f"Acompanhamento: {x[0]}, Preço: R$ {x[1]}\n")
            else:
                print("Nenhum acompanhamento e preço cadastrados!\n")
        elif opcao == 4:
            if os.path.exists("Arquivos/Acompanhamentos.csv"):
                while True:
                    nome = input("Digite o nome do acompanhamento que será apagado: ")

                    dados = []
                    encontrado = False

                    with open('Arquivos/Acompanhamentos.csv', 'r', newline='', encoding='utf-8') as arquivo:
                        r = csv.reader(arquivo)
                        for x in r:
                            if x[0] == nome:
                                encontrado = True
                            else:
                                dados.append(x)
                    if not encontrado:
                        print("\nAcompanhamento não cadastrado!\n")
                    else:
                        with open('Arquivos/Acompanhamentos.csv', 'w', newline='', encoding='utf-8') as arquivo:
                            w = csv.writer(arquivo)
                            w.writerows(dados)
                        print("\nExclusão feita com sucesso!\n")

                    continuar = input("Deseja continuar (S ou N): ")
                    print("")
                    if continuar == 'N':
                        break
            else:
                print("Nenhum acompanhamento e preço cadastrados!\n")
        elif opcao == 5:
            print("SAINDO DO MENU ACOMPANHAMENTOS\n")
            break
        else:
            print("Opção inválida!\n")

def Bebidas():
    while True:
        print("----------------------------------------\n")
        opcao = int(input("Digite uma opção do MENU BEBIDAS: "))
        print("\n")
        if opcao == 1:
            while True:
                nome = input("Digite o nome da bebida: ")
                preco = input("Digite o preco da bebida: ")

                if os.path.exists("Arquivos/Bebidas.csv"):
                    with open('Arquivos/Bebidas.csv', 'r', newline='', encoding='utf-8') as arquivo:
                        dados = csv.reader(arquivo)

                        encontrado = False
                        for x in dados:
                            if x[0] == nome:
                                encontrado = True
                                break

                    if encontrado == True:
                        print("\nBebida já cadastrada!")
                    else:
                        dados = [nome, preco]
                        with open('Arquivos/Bebidas.csv', 'a', newline='', encoding='utf-8') as arquivo:
                            dado = csv.writer(arquivo)
                            dado.writerow(dados)
                else:
                    dados = [nome, preco]
                    with open('Arquivos/Bebidas.csv', 'w', newline='', encoding='utf-8') as arquivo:
                        dado = csv.writer(arquivo)
                        dado.writerow(dados)

                continuar = input("\nDeseja continuar (S ou N): ")
                print("")
                if continuar == 'N':
                    break
            print("Inclusão feita com sucesso!\n")
        elif opcao == 2:
            if os.path.exists("Arquivos/Bebidas.csv"):
                while True:
                    with open('Arquivos/Bebidas.csv', 'r', newline='', encoding='utf-8') as arquivo:
                        r = csv.reader(arquivo)

                        dados = [x for x in r]

                    nome = input("Digite o nome da bebida que terá o preço alterado: ")

                    encontrado = False
                    for x in dados:
                        if x[0] == nome:
                            x[1] = input("\nDigite o novo preço da bebida: ")
                            encontrado = True

                    if encontrado != True:
                        print("\nBebida não cadastrada!\n")
                    else:
                        with open('Arquivos/Bebidas.csv', 'w', newline='', encoding='utf-8') as arquivo:
                            w = csv.writer(arquivo)
                            w.writerows(dados)
                        print("\nAlteração feita com sucesso!\n")

                    continuar = input("Deseja continuar (S ou N): ")
                    print("")
                    if continuar == 'N':
                        break
            else:
                print("Nenhuma bebida e preço cadastrados!\n")
        elif opcao == 3:
            if os.path.exists("Arquivos/Bebidas.csv"):
                with open('Arquivos/Bebidas.csv', 'r', newline='', encoding='utf-8') as arquivo:
                    dados = csv.reader(arquivo)

                    for x in dados:
                        print(f"Bebida: {x[0]}, Preço: R$ {x[1]}\n")
            else:
                print("Nenhuma bebida e preço cadastrados!\n")
        elif opcao == 4:
            if os.path.exists("Arquivos/Bebidas.csv"):
                while True:
                    nome = input("Digite o nome da bebida que será apagada: ")

                    dados = []
                    encontrado = False

                    with open('Arquivos/Bebidas.csv', 'r', newline='', encoding='utf-8') as arquivo:
                        r = csv.reader(arquivo)
                        for x in r:
                            if x[0] == nome:
                                encontrado = True
                            else:
                                dados.append(x)
                    if not encontrado:
                        print("\nBebida não cadastrada!\n")
                    else:
                        with open('Arquivos/Bebidas.csv', 'w', newline='', encoding='utf-8') as arquivo:
                            w = csv.writer(arquivo)
                            w.writerows(dados)
                        print("\nExclusão feita com sucesso!\n")

                    continuar = input("Deseja continuar (S ou N): ")
                    print("")
                    if continuar == 'N':
                        break
            else:
                print("Nenhuma bebida e preço cadastrados!\n")
        elif opcao == 5:
            print("SAINDO DO MENU BEBIDAS\n")
            break
        else:
            print("Opção inválida!\n")

def Pedidos():
    while True:
        print("----------------------------------------\n")
        opcao = int(input("Escolha uma opção do MENU GARÇOM: "))
        print("")
        if opcao == 1:
            if os.path.exists("Arquivos/Carnes.csv") and os.path.exists("Arquivos/Acompanhamentos.csv") and os.path.exists("Arquivos/Bebidas.csv"):
                with open('Arquivos/Carnes.csv', 'r', newline='', encoding='utf-8') as arquivo1, \
                     open('Arquivos/Acompanhamentos.csv', 'r', newline='', encoding='utf-8') as arquivo2, \
                     open('Arquivos/Bebidas.csv', 'r', newline='', encoding='utf-8') as arquivo3:

                    r1 = csv.reader(arquivo1)
                    carnes = [x for x in r1]

                    r2 = csv.reader(arquivo2)
                    acompanhamentos = [x for x in r2]

                    r3 = csv.reader(arquivo3)
                    bebidas = [x for x in r3]

                    print("CARDÁPIO")
                    print("\nCARNES:")
                    for x in carnes:
                        print(f"Carne: {x[0]}, Preço: {x[1]}")
                    print("ACOMPANHAMENTOS:")
                    for x in acompanhamentos:
                        print(f"Acompanhamento: {x[0]}, Preço: {x[1]}")
                    print("BEBIDAS:")
                    for x in bebidas:
                        print(f"Bebida: {x[0]}, Preço: {x[1]}")
                    print("")
                    print("----------------------------------------\n")

                    while True:
                        nome = input("Digite o nome do cliente: ")
                        numero = input("Digite o numero de celular do cliente (no formato (XX) 9XXXX-XXXX): ")
                        if os.path.exists("Arquivos/Clientes.csv"):
                            with open('Arquivos/Clientes.csv', 'r', newline='', encoding='utf-8') as arquivo:
                                r = csv.reader(arquivo)

                                dados = [x for x in r]

                                encontrado = False
                                for x in dados:
                                    if x[0] == nome and x[1] == numero:
                                        encontrado = True
                                        break

                            if encontrado == True:
                                carne = input("Digite a carne escolhida: ")
                                encontrado = False
                                for x in carnes:
                                    if x[0] == carne:
                                        encontrado = True
                                if encontrado == True:
                                    acompanhamento = input("Digite o acompanhamento escolhido: ")
                                    encontrado = False
                                    for x in acompanhamentos:
                                        if x[0] == acompanhamento:
                                            encontrado = True

                                    if encontrado == True:
                                        bebida = input("Digite a bebida escolhida: ")
                                        encontrado = False
                                        for x in bebidas:
                                            if x[0] == bebida:
                                                encontrado = True

                                        if encontrado == True:
                                            for x in carnes:
                                                if x[0] == carne:
                                                    preco_carne = float(x[1].replace(",", "."))
                                            for x in acompanhamentos:
                                                if x[0] == acompanhamento:
                                                    preco_acompanhamento = float(x[1].replace(",", "."))
                                            for x in bebidas:
                                                if x[0] == bebida:
                                                    preco_bebida = float(x[1].replace(",", "."))

                                            for x in dados:
                                                if x[0] == nome and x[1] == numero:
                                                    valor_antigo = float(x[3].replace(",", "."))
                                                    valor_gasto = preco_carne + preco_acompanhamento + preco_bebida
                                                    valor_total = valor_antigo + valor_gasto
                                                    x[3] = str(valor_total).replace(".", ",")

                                            with open('Arquivos/Clientes.csv', 'w', newline='', encoding='utf-8') as arquivo:
                                                w = csv.writer(arquivo)
                                                w.writerows(dados)

                                            if os.path.exists("Arquivos/Caixa.csv"):
                                                with open('Arquivos/Caixa.csv', 'r', newline='', encoding='utf-8') as arquivo:
                                                    r = csv.reader(arquivo)
                                                    caixa_antigo = [x for x in r]

                                                for x in caixa_antigo:
                                                    preco_total1 = preco_carne + preco_acompanhamento + preco_bebida
                                                    preco_total2 = float(x[0].replace(",", "."))
                                                    preco_total3 = preco_total1 + preco_total2

                                                caixa_novo = []
                                                preco_total4 = str(preco_total3)
                                                caixa_novo.append(preco_total4.replace(".", ","))

                                                with open('Arquivos/Caixa.csv', 'w', newline='', encoding='utf-8') as arquivo:
                                                    dado = csv.writer(arquivo)
                                                    dado.writerow(caixa_novo)
                                            else:
                                                preco_total1 = str(preco_carne + preco_acompanhamento + preco_bebida)
                                                preco_total2 = []
                                                preco_total2.append(preco_total1.replace(".", ","))

                                                with open('Arquivos/Caixa.csv', 'w', newline='', encoding='utf-8') as arquivo:
                                                    dado = csv.writer(arquivo)
                                                    dado.writerow(preco_total2)

                                            print("\nPedido feito com sucesso!\n")
                                        else:
                                            print("\nBebida não cadastrada!\n")
                                    else:
                                        print("\nAcompanhamento não cadastrado!\n")
                                else:
                                    print("\nCarne não cadastrada!\n")
                            else:
                                print("\nCliente não cadastrado!\n")
                        else:
                            print("\nNão há clientes cadastrados!\n")

                        continuar = input("Deseja continuar (S ou N): ")
                        print("")
                        if continuar == 'N':
                            break
            else:
                print("\nMenu incompleto, cadastre todas as opções!\n")
        elif opcao == 2:
            print("\nSAINDO DO MENU GARÇOM\n\n----------------------------------------")
            break
        else:
            print("Opção inválida!\n")

def Caixa():
    while True:
        print("----------------------------------------\n")
        opcao = int(input("Digite uma opção do MENU CAIXA: "))
        print("\n")
        if opcao == 1:
            if os.path.exists("Arquivos/Caixa.csv"):
                with open('Arquivos/Caixa.csv', 'r', newline='', encoding='utf-8') as arquivo:
                    dado = csv.reader(arquivo)

                    caixa = tuple(dado)

                for x in caixa:
                    print(f"Caixa: R$ {caixa[0][0]}\n")
            else:
                print("Nenhum caixa cadastrado, é preciso que pedidos sejam anotados!\n")
        elif opcao == 2:
            print("SAINDO DO MENU CAIXA\n")
            break
        else:
            print("Opção inválida!\n")