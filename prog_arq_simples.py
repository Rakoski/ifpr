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


def buscar_dados_pelo_nome(cam_arq: str, nome: str) -> None:
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


def relatorio_soma_salarios_por_ano_nascimento(cam_arq: str, ano_nascimento: float):
    salarios = []
    with open(cam_arq, 'r') as arquivo:
        linha = arquivo.readlines()
        for item in range(len(linha)):
            splitado = linha[item].split(";")
            if str(ano_nascimento) in splitado[3]:
                salario_pra_colocar = splitado[2]
                salarios.append(float(salario_pra_colocar))
    return sum(salarios)


def relatorio_soma_salarios_por_nome(cam_arq: str, nome: str):
    salarios = []
    with open(cam_arq, 'r') as arquivo:
        linha = arquivo.readlines()
        for item in range(len(linha)):
            splitado = linha[item].split(";")
            if nome in splitado[0]:
                salario_pra_colocar = splitado[2]
                salarios.append(float(salario_pra_colocar))
    return sum(salarios)


def relatorio_soma_salarios_por_idade(cam_arq: str, idade: int):
    cont_maior_que_idade = cont_menor_que_idade = 0
    salarios_maior_que_idade = []
    salarios_menor_que_idade = []

    with open(cam_arq, 'r') as arquivo:
        linha = arquivo.readlines()

        for item in range(len(linha)):
            splitado = linha[item].split(";")
            data_de_nascimento_do_arquivo = splitado[3]
            data_de_nascimento_splitada = data_de_nascimento_do_arquivo.split("/")
            ano_de_nascimento_no_arquivo = data_de_nascimento_splitada[2]
            ano_nascimento = int(year) - idade

            # ele quer o maior igual ou o menor igual e falou isso explicitamente na explicação
            if ano_nascimento <= int(ano_de_nascimento_no_arquivo):
                cont_menor_que_idade += 1
                salario_pra_colocar = splitado[2]
                salarios_menor_que_idade.append(float(salario_pra_colocar))

            elif ano_nascimento >= int(ano_de_nascimento_no_arquivo):
                cont_maior_que_idade += 1
                salario_pra_colocar = splitado[2]
                salarios_maior_que_idade.append(float(salario_pra_colocar))

    media_maior_que_idade = sum(salarios_maior_que_idade)/cont_maior_que_idade
    media_menor_que_idade = sum(salarios_menor_que_idade)/cont_menor_que_idade

    return media_maior_que_idade, media_menor_que_idade
