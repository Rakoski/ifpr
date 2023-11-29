# Chaves padrão do dicionário pessoas: nome, email, sal, nasc
import ifpr6_funcoes as ifpr

while True:
    opcao_escolhida = ifpr.menu()

    if opcao_escolhida == 1:
        pessoa = ifpr.perguntar_dados()
        ifpr.inserir_dados("ifpr6", pessoa)

    elif opcao_escolhida == 2:
        print(ifpr.ler_arquivo("ifpr6"))

    elif opcao_escolhida == 3:
        nome_pra_achar = input("Digite o nome pra buscarmos os dados: ")
        print(ifpr.acessar_onde_tem_n("ifpr6", nome_pra_achar))

    elif opcao_escolhida == 4:
        dicionario = ifpr.ler_arquivo("ifpr6")
        print(ifpr.listar_emails(dicionario))

    elif opcao_escolhida == 5:
        print(ifpr.listar_por_ano_nascimento("ifpr6", 2004))

