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


def inserir_dados(arq, dicionario) -> None:
    arquivo = open(arq, "a")
    dicionario_como_lista = list(dicionario.values())
    for i, valores in enumerate(dicionario_como_lista):
        if i < (len(dicionario_como_lista) - 1):
            arquivo.write(str(valores) + ";")
        else:
            arquivo.write(str(valores) + "\n")
    arquivo.close()
    return None


def ler_arquivo(arq):
    arquivo = open(arq, "r")
    pra_guardar_os_dados = []
    dados_do_arquivo = arquivo.readlines()
    for dado in dados_do_arquivo:
        pra_guardar_os_dados.append(dado.replace("\n", ""))
    arquivo.close()
    return pra_guardar_os_dados


# Tarefa: Acessar e devolver todos os dados que contém o nome N em um arquivo
def acessar_onde_tem_n(arq, nome):
    arquivo = open(arq, "r")
    pra_guardar_os_nomes = []
    dados_do_arquivo = arquivo.readlines()
    for dado in dados_do_arquivo:
        splitado = dado.split(";")
        if nome == splitado[0]:
            pra_guardar_os_nomes.append(dado)
    arquivo.close()
    return pra_guardar_os_nomes



