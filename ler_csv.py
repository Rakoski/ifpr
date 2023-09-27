from time import sleep

import prog_arq_simples

while True:
    opcao = prog_arq_simples.mostrar_menu()

    if opcao == 1:
        prog_arq_simples.inserir_dados()

    elif opcao == 2:
        prog_arq_simples.ler_arq("nome.txt")

    elif opcao == 3:
        prog_arq_simples.buscar_dados_pelo_nome("nome.txt", "Mateus")

    elif opcao == 4:
        print(prog_arq_simples.relatorio_soma_salarios("nome.txt"))

    elif opcao == 5:
        print(prog_arq_simples.relatorio_soma_salarios_por_ano_nascimento("nome.txt", 2005))

    elif opcao == 6:
        print(prog_arq_simples.relatorio_soma_salarios_por_nome("nome.txt", "neymar jr"))

    elif opcao == 7:
        print(prog_arq_simples.relatorio_soma_salarios_por_idade("nome.txt", 18))

    else:
        print("finalizando...")
        sleep(0.5)
        break






