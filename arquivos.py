BASE_DIR = '/home/mateus/PycharmProjects/ifpr/sim.txt'

v = ["Maria\n", 'Lucas\n', 'Arthur\n']

with open(BASE_DIR, "a+") as arquivo:
    arquivo.write("sim2\n".replace("\n", ""))

with open(BASE_DIR, "r") as arquivo:
    linha = arquivo.readlines()
    for c in range(len(linha)):
        print(linha[c].replace("\n", ''), end=' ' )

with open(BASE_DIR, "w+") as arquivo:
    arquivo.writelines(v)