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
        print()
        opcao = int(input("Digite sua escolha: "))
        if not (0 < opcao <= 11):
            print("Por favor, escolha outra opção.")
            continue
        return opcao

def perguntar_dados():
    pessoa = {}
    pessoa["nome"] = input("Nome: ")
    pessoa["email"] = input("Email: ")
    pessoa["salario"] = float(input("Salário: "))
    pessoa["data_nascimento"] = input("Data de nascimento: ")
    return pessoa


#1
def inserir_dados(arq, dicionario) -> None:
    arquivo = open(arq, "a")
    arquivo.write(f"{dicionario['nome']};{dicionario['email']};{dicionario['salario']};{dicionario['data_nascimento']}\n")
    arquivo.close()


#2
def ler_arquivo(arq):
    arquivo = open(arq, "r")
    linhas = arquivo.readlines()
    pessoas = [""] * len(linhas)
    for i in range(0, len(linhas)):
        dados = linhas[i].replace("\n", "").split(";")
        pessoas[i] = {}
        pessoas[i]["nome"] = dados[0]
        pessoas[i]["email"] = dados[1]
        pessoas[i]["salario"] = float(dados[2])
        pessoas[i]["data_nascimento"] = dados[3]
    arquivo.close()
    return pessoas


# 3
def acessar_onde_tem_n(arq, nome):
    arquivo = open(arq, "r")
    linhas = arquivo.readlines()
    pra_guardar_os_nomes = [""] * len(linhas)
    vet = [""] * len(linhas)
    for i in range(len(linhas)):
        dados = linhas[i].replace("\n", "").split(";")
        vet[i] = {}
        vet[i]["nome"] = dados[0]
        vet[i]["email"] = dados[1]
        vet[i]["salario"] = float(dados[2])
        vet[i]["data_nascimento"] = dados[3]
        if nome in vet[i]["nome"]:
            pra_guardar_os_nomes[i] = vet[i]
        else:
            continue
    arquivo.close()
    return pra_guardar_os_nomes


# 4
def listar_emails(dicionario):
    pra_guardar_os_emails = [""] * len(dicionario)
    vet = [""] * len(dicionario)
    for i in range(len(dicionario)):
        dados = dicionario[i]
        vet[i] = {}
        pra_guardar_os_emails[i] = dados["email"]
    return pra_guardar_os_emails


def listar_por_ano_nascimento(arq, ano_nasc):
    arquivo = open(arq, "r")
    linhas = arquivo.readlines()
    pra_guardar_as_pessoas = [""] * len(linhas)
    vet = [""] * len(linhas)
    for i in range(len(linhas)):
        dados = linhas[i].replace("\n", "").split(";")
        vet[i] = {}
        vet[i]["nome"] = dados[0]
        vet[i]["email"] = dados[1]
        vet[i]["salario"] = dados[2]
        vet[i]["data_nascimento"] = dados[3]
        if str(ano_nasc) in dados[3]:
            pra_guardar_as_pessoas[i] = dados[i]
        else:
            continue
    return pra_guardar_as_pessoas


