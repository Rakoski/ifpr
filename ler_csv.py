from time import sleep

import prog_arq_simples

while True:
    opcao = prog_arq_simples.mostrar_menu()

    if opcao == 1:
        prog_arq_simples.inserir_dados()

    elif opcao == 2:
        prog_arq_simples.ler_arq("nome.txt")

    elif opcao == 3:
        nome = str(input("Qual nome quer pesquisar? "))
        prog_arq_simples.buscar_dados_pelo_nome("nome.txt", nome)

    elif opcao == 4:
        print(prog_arq_simples.relatorio_soma_salarios("nome.txt"))

    elif opcao == 5:
        ano_nascimento = int(input("Qual ano quer pesquisar? "))
        print(prog_arq_simples.relatorio_soma_salarios_por_ano_nascimento("nome.txt", ano_nascimento))

    elif opcao == 6:
        nome = str(input("Qual nome quer pesquisar? "))
        print(prog_arq_simples.relatorio_soma_salarios_por_nome("nome.txt", nome))

    elif opcao == 7:
        idade = int(input("Qual idade quer pesquisar? "))
        print(prog_arq_simples.relatorio_soma_salarios_por_idade("nome.txt", idade))

    else:
        print("finalizando...")
        sleep(0.5)
        break






