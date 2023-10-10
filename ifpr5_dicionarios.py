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


escrever_arquivo_pelo_dicionario("nome.txt", beltrano)
