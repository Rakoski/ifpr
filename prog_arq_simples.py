def escrever_arq(cam_arq: str, nome: str) -> None:
    with open(cam_arq, 'a+') as arquivo:
        arquivo.write(nome)


def ler_arq(cam_arq: str) -> None:
    print("Mostrando: ")
    print()
    with open(cam_arq, 'r+') as arquivo:
        linha = arquivo.readlines()
        for c in range(len(linha)):
            print(linha[c].replace("\n", ''))


escrever_arq("/home/mateus/PycharmProjects/ifpr/sim.txt", "\nArtur")

ler_arq("/home/mateus/PycharmProjects/ifpr/sim.txt")