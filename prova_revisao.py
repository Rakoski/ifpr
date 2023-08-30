import random
from time import sleep

# soma = subtracao = multiplicacao = divisao = 0
#
# print("MENU DE OPCOES")
# print("""Gerar 10 exercícios de soma
# Gerar 10 exercícios de subtração
# Gerar 10 exercícios de multiplicação
# Gerar 10 exercícios de divisão
# Sair""")
#
# while (True):
#     i = 0
#     opcao = int(input("Digite sua opção: "))
#
#     # Operacoes de soma
#     if (opcao == 1):
#         while i < 10:
#             aleatorio1 = random.randint(0, 100)
#             aleatorio2 = random.randint(0, 100)
#             soma = aleatorio1 + aleatorio2
#             print(f"{aleatorio1} + {aleatorio2} = {soma} | ", end="")
#             i += 1
#
#     # Operacoes de subtracao
#     elif (opcao == 2):
#         while i < 10:
#             aleatorio1 = random.randint(0, 100)
#             aleatorio2 = random.randint(0, 100)
#             subtracao = aleatorio1 - aleatorio2
#
#             if (subtracao >= 0):
#                 print(f"{aleatorio1} - {aleatorio2} = {subtracao} | ", end="")
#                 i += 1
#
#     # multiplicacao
#     elif (opcao == 3):
#         while i < 10:
#             aleatorio1 = random.randint(0, 100)
#             aleatorio2 = random.randint(0, 100)
#             multiplicacao = aleatorio1 * aleatorio2
#
#             if (multiplicacao < 1000):
#                 print(f"{aleatorio1} * {aleatorio2} = {multiplicacao} | ", end="")
#                 i += 1
#
#     elif (opcao == 4):
#         while i < 10:
#             n1 = random.randint(1, 100)
#             n2 = random.randint(1, n1)
#
#             if n1 % n2 == 0:
#                 print(f"{n1} / {n2} = {n1 / n2}")
#                 i += 1
#
#     elif (opcao == 5):
#         print("Desligando...")
#         sleep(0.5)
#         break
#
#     else:
#         print("Por favor, digite uma opcao correta")

vetor_a = int(input("digite o tamanho do seu vetor: "))

A = [0] * vetor_a
for c in range(0, vetor_a):
    A[c] = int(input(f"Digite a {c + 1}° parte do seu arr: "))
print(A)

B = [0] * random.randint(1, 30)
for c in range(len(B)):
    aleat = random.randint(1, 30)
    if B[c] < len(B):
        B[c] = aleat

C = [0] * len(A)
soma = [0] * len(C)
pares = []
soma_pares = cont = 0


for i in range(0, len(A)):
    C[i] = A[i] + B[i]
    if C[i] > 15:
        cont += 1

for c in range(len(C)):
    if(C[c] % 2 == 0 and C[c] != 0):
        pares.append(C[c])

for a in range(len(pares)):
    soma_pares += pares[a]

print(B)
print(C)
print(f"Seus números pares em C são {pares}")
print(f"Você tem {soma_pares} na soma de todos os números pares")
print(f"Você tem {cont} números maiores que quinze")
