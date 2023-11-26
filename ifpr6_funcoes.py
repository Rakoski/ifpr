def menu():
    while True:
        print("""
1. Inserir dados
2. Listar todos dados
3. Buscar dados
4. Listar emails
5. Listar pessoas por ano de nascimento
6. Listar pessoas com salários acima
7. Somar salários (todos)
8. Relatório da soma dos salários por ano de nascimento
9. Relatório da soma de salários por nome
10. Relatório de média de salários por idade
11. Sair""")
        opcao = int(input("Digite sua escolha: "))
        if not (0 < opcao <= 11):
            print("Por favor, escolha outra opção.")
            continue
        return opcao


def inserir_dados(arq, dicionario):
    arquivo = open(arq, "a")
    dicionario_como_lista = list(dicionario.values())
    for i, valores in enumerate(dicionario_como_lista):
        if i < (len(dicionario_como_lista) - 1):
            arquivo.write(str(valores) + ";")
        else:
            arquivo.write(str(valores) + "\n")
    arq.close()



