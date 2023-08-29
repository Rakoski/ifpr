class Fatorial:
    def __init__(self, numero):
        self.numero = numero

    def fatorial(self, numero: int):
        if numero == 1:
            return 1
        else:
            return numero * self.fatorial(numero - 1)


fatorial = Fatorial("uai")
classe = fatorial.fatorial(5)
print(classe)


