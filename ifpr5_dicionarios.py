beltrano = {}
beltrano["nome"] = "Beltrano"
beltrano["salario"] = "1050.01"
beltrano["nascimento"] = "30/05/1995"
beltrano["email"] = "beltrano@ifpr.edu.br"


def escrever_arquivo_pelo_dicionario(cam_arq, dictio):
    arquivo = open(cam_arq, "a")
    arquivo.write(dictio["nome"] + ";")
    arquivo.write(dictio["email"] + ";")
    arquivo.write(dictio["nascimento"] + ";")
    arquivo.write(str(dictio["salario"] + ";" + "\n"))
    arquivo.close()


def acessar_arquivo(cam_arq):
    arquivo = open(cam_arq, "r")
    vet_linhas = arquivo.readlines()
    vet = [""] * len(vet_linhas)
    for i in range(0, len(vet)):
        conteudo = vet_linhas[i].replace("\n", "")
        dados = conteudo.split(";")
        vet[i] = {}
        vet[i]["nome"] = dados[0]
        vet[i]["email"] = dados[1]
        vet[i]["salario"] = dados[2]
        vet[i]["data"] = dados[3]
    arquivo.close()
    return vet


def procurar_pelo_nome(cam_arq, nome):
    pra_colocar = []
    arquivo = open(cam_arq, "r")
    vet_linhas = arquivo.readlines()
    vet = [""] * len(vet_linhas)
    for i in range(0, len(vet)):
        conteudo = vet_linhas[i].replace("\n", "")
        dados = conteudo.split(";")
        vet[i] = {}
        vet[i]["nome"] = dados[0]
        vet[i]["email"] = dados[1]
        vet[i]["salario"] = dados[2]
        vet[i]["data"] = dados[3]
        if nome in vet[i]["nome"]:
            pra_colocar.append(vet[i])
    arquivo.close()
    return pra_colocar


def listar_emails(dicionario):
    emails = []
    arquivo = open("nome.txt", "r")
    for i in range(len(dicionario)):
        linhas = dicionario[i]
        email_pra_colocar = linhas["email"]
        emails.append(email_pra_colocar)
    arquivo.close()
    return emails


print(procurar_pelo_nome("nome.txt", "Mateus"))
print(listar_emails(acessar_arquivo("nome.txt")))
