def menu():
    print("1.  inserir dados")
    print("2.  listar dados")
    print("3.  buscar dados")
    print("4.  listar todos emails")
    print("5.  Listar pessoas por ano de nascimento")
    print("6.  Listar pessoas com salários acima")
    print("7.  Somar salários (todos)")
    print("8.  Relatório da soma dos salários por ano de nascimento")
    print("9.  Relatório da soma de salários por nome")
    print("10.  Relatório de média de salários por idade")
    print("11.  Sair")


# 1
def inserir_dados(arquivo, pessoas):
    arquivo = open(arquivo + ".txt", "a")
    arquivo.write(pessoas["nome"] + ";")
    arquivo.write(pessoas["email"] + ";")
    arquivo.write(str(pessoas["salario"]) + ";")
    arquivo.write(pessoas["nasc"] + "\n")
    arquivo.close()


# 2
def listar_dados(arquivo):
    arquivo = open(arquivo + ".txt", "r")
    linhas = arquivo.readlines()
    pessoas = [""] * len(linhas)
    for i in range(0, len(linhas)):
        dados = linhas[i].replace("\n", "").split(";")
        pessoas[i] = {}
        pessoas[i]["nome"] = dados[0]
        pessoas[i]["email"] = dados[1]
        pessoas[i]["salario"] = float(dados[2])
        pessoas[i]["nasc"] = dados[3]

    arquivo.close()
    return pessoas

# 3
def buscar_dados(arquivo, nome):
    pessoas = listar_dados(arquivo)

    cont = 0
    for i in range(0, len(pessoas)):
        if (nome.upper() in pessoas[i]["nome"].upper()):
            cont += 1
    vetor = [""] * cont
    posi = 0
    for j in range(0, len(pessoas)):
        if (nome.upper() in pessoas[j]["nome"].upper()):
            vetor[j] = pessoas[j]
            posi += 1

    return vetor

# 4
def listar_emails(pessoas):
    emails = [""] * len(pessoas)
    for i in range(0, len(pessoas)):
        emails[i] = pessoas[i]["email"]

    return emails


# 5
def listarPorAno(arquivo, ano):
    pessoas = listar_dados(arquivo)
    cont = 0
    anoNasc = 0
    for i in range(0, len(pessoas)):
        ano = pessoas[i]["nasc"].split("/")
        if (ano[2] == str(anoNasc)):
            cont += 1
    vetor = [""] * cont
    index = 0
    for i in range(0, len(pessoas)):
        ano = pessoas[i]["nasc"].split("/")
        if (ano[2] == (anoNasc)):
            vetor[index] = pessoas[i]
            index += 1
    return vetor


"""
Listar pessoas com salários acima


Tarefa: Acessar e devolver todos os dados de pessoas com salário acima de XXXX em um arquivo
Parâmetros: arquivo, salário mínimo
Retorno: vetor de dicionários de pessoas
"""


# 6
def listarAcimaDoSalario(arquivo, salarioMinimo):
    pessoas = listar_dados(arquivo)
    cont = 0

    for i in range(0, len(pessoas)):
        salario = pessoas[i]["salario"]
        if (salario > salarioMinimo):
            cont += 1

    vetor = [""] * cont
    index = 0
    for j in range(0, len(pessoas)):
        salario = pessoas[j]["salario"]
        if (salario > salarioMinimo):
            vetor[index] = pessoas[j]
            index += 1
    return vetor


# 7
def somarSalario(pessoas):
    total = 0.0
    for i in range(0, len(pessoas)):
        total += pessoas[i]["salario"]

    return total


# 8
"""
Relatório da soma dos salários por ano de nascimento
Tarefa: somar todos os salários de pessoas nascidas em XXXX
Parâmetro: vetor de dicionário de pessoas (obter por meio da função 2), ano de nascimento
Retorno: Valor da soma dos salários
"""


# RESUMO DO 8: variavel total pra soma de salarios
#  achar as pessoas nascidas no ano digitado
#  achar os salarios
#  somar os salarios
#  retornar a soma
def soma_salario_ano(ano, pessoas):
    total = 0.0
    cont = 0
    for i in range(0, len(pessoas)):
        ano = pessoas[i]["nasc"].split("/")
        if (str(pessoas[i]["nasc"]) == ano[2]):
            cont += 1

    vetor = [""] * cont

    index = 0
    for j in range(0, len(vetor)):
        ano = pessoas[j]["nasc"].split("/")
        if (str(pessoas[j]["nasc"]) == ano[2]):
            vetor[index] = pessoas[j]
            index += 1

    for k in range(0, len(vetor)):
        total += vetor[k]["salario"]

    return total


# 10
def mediaSalIdade(pessoas, idade):
    total = 0.0
    data = str
    ano = data.today().year
    cont = 0
    for i in range(0, len(pessoas)):
        data = pessoas[i]["nasc"].split("/")
        idadePessoa = ano - int(data[2])

        if (idade == idadePessoa):
            cont += 1
            total += pessoas[i]["sal"]

    if (cont == 0):
        return 0


    else:
        media = total / cont
    return media