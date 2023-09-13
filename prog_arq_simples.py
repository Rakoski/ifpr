def escrever_arq(cam_arq, nome):
    with open(cam_arq, 'w+') as arquivo:
        arquivo.write(nome)


def ler_arq(cam_arq):
    print("Mostrando: ")
    print()
    with open(cam_arq, 'r+') as arquivo:
        linha = arquivo.readlines()
        for c in range(len(linha)):
            print(linha[c].replace("\n", ''))


escrever_arq("/home/mateus/PycharmProjects/ifpr/sim.txt", "Mateus")

ler_arq("/home/mateus/PycharmProjects/ifpr/sim.txt")