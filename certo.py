import certo_funcoes as f
import os

arq = input("Digite o nome de um arquivo: ")

while (True):
    f.menu()
    op = input("\nDigite a opção desejada: ")
    # 1
    if (op == "1"):
        pessoas = {}
        pessoas["nome"] = input("Nome: ")
        pessoas["email"] = input("Email: ")
        pessoas["salario"] = float(input("Salario: "))
        pessoas["nasc"] = input("Data de nascimento: ")

        f.inserir_dados(arq, pessoas)
    # 2
    elif (op == "2"):
        pessoas = f.listar_dados(arq)

        for i in range(0, len(pessoas)):
            print("Nome: ", pessoas[i]["nome"])
            print("Email: ", pessoas[i]["email"])
            print("Salario: ", pessoas[i]["salario"])
            print("Data de Nascimento: ", pessoas[i]["nasc"])
            print("-" * 40)


    # 3
    elif (op == "3"):
        nome = input("\nNome: ")
        vetor = f.buscar_dados(arq, nome)


    # 4
    elif (op == "4"):
        pessoas = f.listar_dados(arq)
        emails = f.listar_emails(pessoas)
        for i in range(0, len(pessoas)):
            print(pessoas[i]["email"])

    # 5
    elif (op == "5"):
        ano = int(input("\nDigite um ano para listar as pessoas nascidas nele:  \n"))

        pessoas = f.listar_dados(arq)
        vetor = f.listarPorAno(arq, ano)
        for i in range(0, len(pessoas)):
            print("")
            print("Data de Nascimento: ", pessoas[i]["nasc"])


    # 6
    elif (op == "6"):
        salarioMinimo = float(input("Digite um salário base: "))
        pessoas = f.listar_dados(arq)
        salarios = f.listarAcimaDoSalario(arq, salarioMinimo)
        for i in range(0, len(pessoas)):
            if (salarios > salarioMinimo):
                print("Salarios: ", pessoas[i]["salario"])


    # 7
    elif (op == "7"):
        pessoas = f.listar_dados(arq)
        total = f.somarSalario(pessoas)
        print("\nSoma total de salários: R$", total)


    # 8
    elif (op == "8"):
        ano = int(input("Digite o ano para somar os salarios das pessoas nascidas nele: "))
        pessoas = f.listar_dados(arq)
        soma = f.soma_salario_ano(ano, pessoas)


    # 10
    elif (op == 10):
        pessoas = f.listar_dados(arq)
        idade = int(input("Idade: "))
        media = f.mediaSalIdade(pessoas, idade)

    input("\nAperte ENTER para voltar ao Menu: ")