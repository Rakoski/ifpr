class Fatorial:
    def __init__(self, numero):
        self.numero = numero

    def fatorial(self, numero):
        if numero == 1:
            return 1
        else:
            return numero * self.fatorial(numero - 1)


numero = Fatorial(5)
classe = numero.fatorial(5)
print(classe)


