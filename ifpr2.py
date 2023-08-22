# Tem que se chamar quantos_multiplos(). Pra executar ele, precisa de um número de 1 a 15 e contá-los (intervalo)
# agora eu quero saber quantos são múltiplos de determinado número

import ifpr3


def quantos_multiplos(arr, multiplo):
    cont = 0
    todos = []
    for c in range(len(arr)):
        if arr[c] % multiplo == 0:
            cont += 1
            todos.append(arr[c])
    print(f"Você possui {cont} números dividios por {multiplo}, sendo eles {todos} em", arr)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
quantos_multiplos(lista, 4)

ifpr3.qual_categoria(5)
