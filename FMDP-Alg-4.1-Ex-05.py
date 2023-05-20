'''5. Faça um programa Python que calcule o valor de A, dado pela expressão abaixo, onde N é um
número inteiro positivo fornecido pelo usuário.'''

# Solicita os dados

n = int(input("Insira um número inteiro positivo: "))

# Define soma

soma = 0

# Repetição for

for e in range(1, n + 1):
    soma += (e-(e-1))/e
    print (soma)