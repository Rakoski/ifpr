from time import sleep

import prog_arq_simples as programa

while True:
    opcao = programa.mostrar_menu()

    if opcao == 1:
        programa.inserir_dados()

    elif opcao == 2:
        programa.ler_arq("nome.txt")

    elif opcao == 3:
        programa.buscar_dados_pelo_nome("nome.txt")

    elif opcao == 4:
        print(programa.relatorio_soma_salarios("nome.txt"))

    elif opcao == 5:
        print(programa.relatorio_soma_salarios_por_ano_nascimento("nome.txt"))

    elif opcao == 6:
        print(programa.relatorio_soma_salarios_por_nome("nome.txt"))

    elif opcao == 7:
        print(programa.relatorio_soma_salarios_por_idade('nome.txt'))

    else:
        print("finalizando...")
        sleep(0.5)
        break






