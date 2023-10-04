class Fatorial:
    def fatorial(self, numero: int):
        if numero == 1:
            return 1
        else:
            return numero * self.fatorial(numero - 1)


fatorial = Fatorial()
classe = fatorial.fatorial(5)
print(classe)


