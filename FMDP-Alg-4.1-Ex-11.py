'''11. Faça um programa Python que calcule o valor de A, dado pela expressão abaixo, onde N é um
número inteiro positivo fornecido pelo usuário.'''

# Solicita os dados

n = int(input("Insira um número inteiro positivo: "))

# Define variáveis

e = 1
soma = 0
x = 1

while True:
    soma += (1/e)*x
    x *= -1
    e += 1
    if e > n:
        break

print(f"O resultado da soma é: {soma}.")