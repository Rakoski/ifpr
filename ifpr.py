# Leia 3 numeros e mostre qual o maior

def maior_numero(num1, num2, num3):
    if num1 > num2 and num1 > num2:
        print(f"{num1} é o maior")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} é o maior")
    elif num3 > num2 and num3 > num1:
        print(f"{num3} é o maior")
    else:
        print(num1, num2, num3, "são iguais")


maior_numero(9, 9, 9)
