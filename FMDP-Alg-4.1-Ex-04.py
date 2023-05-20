'''4. Faça um programa Python que calcule o valor de A, dado pela expressão abaixo, onde N é um
número inteiro positivo fornecido pelo usuário.'''

# Solicita os dados

n = int(input("Insira um número inteiro positivo: "))

soma = 0

for e in range(1, n + 1):
    soma += 1 / e
    print (soma)