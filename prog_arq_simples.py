import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")


def escrever_arq(cam_arq: str, *nome) -> None:
    with open(cam_arq, 'a+') as arquivo:
        arquivo.writelines(nome)


def ler_arq(cam_arq: str) -> None:
    print("Mostrando: ")
    print()
    with open(cam_arq, 'r+') as arquivo:
        linha = arquivo.readlines()
        for c in range(len(linha)):
            dados = linha[c].replace("\n", '').split(';')
            print("Nome: ", dados[0])
            print("Email: ", dados[1])
            print("Salário: ", dados[2])
            print("Data: ", dados[3])
            print()


def mostrar_menu() -> int:
    print("""
1. INSERIR DADOS
2. LISTAR DADOS
3. BUSCAR DADOS
4. RELATÓRIO DE SOMA DE SALÁRIOS
5. RELATÓRIO DA SOMA DOS SALÁRIOS POR ANO DE NASCIMENTO
6. RELATÓRIO DA SOMA DE SALÁRIOS POR NOME
7. RELATÓRIO DA MÉDIA DE SALÁRIOS POR IDADE
    """)
    opcao = int(input("Digite sua opção: "))
    return opcao


def inserir_dados() -> None:
    nome_completo = str(input("Digite seu nome completo: "))
    email = str(input("Digite seu email: "))
    salario = float(input("Digite seu salário: "))
    data_nascimento = str(input("Digite sua data de nascimento [xx/xx/xxxx]: "))

    escrever_arq(f"nome.txt", f"{nome_completo};", f"{email};", f"{salario};", f"{data_nascimento};", "\n")


def buscar_dados_pelo_nome(cam_arq: str) -> None:
    nome = str(input("Digite seu nome: "))
    with open(cam_arq, 'r+') as arquivo:
        linha = arquivo.readlines()
        for c in range(len(linha)):
            dados = linha[c].replace("\n", '').split(';')
            if nome == dados[0]:
                print(nome)


def relatorio_soma_salarios(cam_arq):
    salarios = []
    with open(cam_arq, "r+") as arquivo:
        linha = arquivo.readlines()
        for item in range(len(linha)):
            splitado = linha[item].split(';')
            salario_pra_colocar = splitado[2]
            salarios.append(int(salario_pra_colocar))
    return sum(salarios)


def relatorio_soma_salarios_por_ano_nascimento(cam_arq: str):
    salarios = []
    ano_nascimento = float(input("Digite seu ano de nascimento: "))
    with open(cam_arq, 'r') as arquivo:
        linha = arquivo.readlines()
        for item in range(len(linha)):
            splitado = linha[item].split(";")
            if str(ano_nascimento) in splitado[3]:
                salario_pra_colocar = splitado[2]
                salarios.append(float(salario_pra_colocar))
    return sum(salarios)


def relatorio_soma_salarios_por_nome(cam_arq: str):
    salarios = []
    nome = str(input("Digite seu nome: "))
    with open(cam_arq, 'r') as arquivo:
        linha = arquivo.readlines()
        for item in range(len(linha)):
            splitado = linha[item].split(";")
            if nome in splitado[0]:
                salario_pra_colocar = splitado[2]
                salarios.append(float(salario_pra_colocar))
    return sum(salarios)


def ler_arquivo(cam_arq):
    with open(cam_arq, 'r') as arquivo:
        return arquivo.readlines()


def calcular_idade(data_de_nascimento, idade):
    data_de_nascimento_splitada = data_de_nascimento.split("/")
    ano_de_nascimento_no_arquivo = int(data_de_nascimento_splitada[2])
    ano_nascimento = int(year) - idade
    return ano_de_nascimento_no_arquivo, ano_nascimento


def calcular_medias_salarios_por_idade(linhas, idade):
    cont_maior_que_idade = cont_menor_que_idade = 0
    salarios_maior_que_idade = []
    salarios_menor_que_idade = []

    for linha in linhas:
        splitado = linha.split(";")
        data_de_nascimento_do_arquivo = splitado[3]
        ano_de_nascimento_no_arquivo, ano_nascimento = calcular_idade(data_de_nascimento_do_arquivo, idade)

        if ano_nascimento <= ano_de_nascimento_no_arquivo:
            cont_menor_que_idade += 1
            salario_pra_colocar = splitado[2]
            salarios_menor_que_idade.append(float(salario_pra_colocar))
        else:
            cont_maior_que_idade += 1
            salario_pra_colocar = splitado[2]
            salarios_maior_que_idade.append(float(salario_pra_colocar))

    if cont_maior_que_idade != 0:
        media_maior_que_idade = sum(salarios_maior_que_idade) / cont_maior_que_idade
    else:
        media_maior_que_idade = 0
    if cont_menor_que_idade != 0:
        media_menor_que_idade = sum(salarios_menor_que_idade) / cont_menor_que_idade
    else:
        media_menor_que_idade = 0

    return media_maior_que_idade, media_menor_que_idade


def relatorio_soma_salarios_por_idade(cam_arq: str):
    try:
        linhas = ler_arquivo(cam_arq)
        idade = int(input("Qual sua idade? "))
        media_maior_que_idade, media_menor_que_idade = calcular_medias_salarios_por_idade(linhas, idade)
        return media_maior_que_idade, media_menor_que_idade
    except ZeroDivisionError:
        print(f"A média menor que a idade deu 0 e a média maior que"
              f" a idade deu 0 ")


