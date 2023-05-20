'''8. Faça um programa Python que peça 10 números inteiros e apresente: a média, o maior e o
menor.'''

# Define varáveis úteis

l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0

# Calcula a média

while x < len(l):
    l[x] = float(input(f"Insira o {x + 1}º elemento: "))
    soma += l[x]
    x += 1

x = 0
while x < len(l):
    print(f"{x + 1}º elemento: {l[x]}")
    x += 1

print(f"A média da soma dos 10 elementos é: {soma/10:.2f}")
