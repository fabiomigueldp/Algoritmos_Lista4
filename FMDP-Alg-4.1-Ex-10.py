'''10. Faça um programa Python que calcule o valor de A, dado pela expressão abaixo, onde N é um
número inteiro positivo fornecido pelo usuário.'''

# Solicita os dados

n = int(input("Insira um número inteiro positivo: "))

# Define soma

soma = 0

# Repetição while

for e in range(1, n + 1):
    soma += 1/(2*e-1)
    print(soma)


e = 1
soma = 0

while True:
    soma += 1/(2*e-1)
    e += 1
    if e > n:
        break

print(f"O resultado da soma é: {soma}.")
