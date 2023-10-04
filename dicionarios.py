rafael = {}
rafael["nome"] = "Rafael Zottesso"
rafael["salario"] = 20000.99
rafael["nascimento"] = "01/02/1988"
rafael["email"] = "rafael.zottesso@ifpr.edu.br"

hudson = {}
hudson["nome"] = "Hudson de Souza"
hudson["salario"] = "15123.99"
hudson["nascimento"] = "02/10/2000"
hudson["email"] = "hudson.souza@ifpr.edu.br"

ciclano = {}
ciclano["nome"] = "Ciclano"
ciclano["salario"] = "3211.99"
ciclano["nascimento"] = "12/11/2003"
ciclano["email"] = "ciclano@ifpr.edu.br"

beltrano = {}
beltrano["nome"] = "Beltrano"
beltrano["salario"] = "1050.01"
beltrano["nascimento"] = "30/05/1995"
beltrano["email"] = "beltrano@ifpr.edu.br"

# fulano = {}
# fulano["nome"] = input("Nome: ")
# fulano["salario"] = float(input("Salário: R$"))
# fulano["nascimento"] = input("Nascimento: ")
# fulano["email"] = input("E-mail: ")

# Acessando as posições do dicionário diretamente
print("Dados do dicionário:")
print("Nome:", hudson["nome"])
print("Salário:", hudson["salario"])
print("Data de Nascimento:", hudson["nascimento"])
print("E-mail:", hudson["email"])

# Acessando um dicionário com laço de repetição
for chave in rafael:
    print(chave, ": ", rafael[chave])

# Cria um vetor "comum" de str
pessoas = [""] * 5

# Preencher o vetor com dicionários
# for i in range(0, len(pessoas)):
#     pessoas[i] = {}
#     pessoas[i]["nome"] = input("Nome: ")
#     pessoas[i]["idade"] = int(input("Idade: "))
#     pessoas[i]["email"] = input("E-mail: ")
#     print("-----------------")

# Armazenar dicionários no vetor "na mão"
# pessoas[0] = rafael
# pessoas[1] = hudson
# pessoas[2] = fulano
# pessoas[3] = ciclano
# pessoas[4] = beltrano

# Percorrer um vetor de dicionários
# Que eu conheço as chaves
# for i in range(0, len(pessoas)):
#     print("Nome:", pessoas[i]["nome"])
#     print("E-mail: ", pessoas[i]["email"])
#     print("Data de Nasc:", pessoas[i]["nascimento"])
#     print("Faturamento: R$", pessoas[i]["salario"])
#     print("---------------------------")

# Percorrendo um vetor de dicionários
# que eu NÃO CONHEÇO as chaves
for i in range(0, len(pessoas)):
    # percorrer o dicionário em cada posição do vetor
    for chave in pessoas[i]:
        print(chave, ":", pessoas[i][chave])

    print("-------------")
