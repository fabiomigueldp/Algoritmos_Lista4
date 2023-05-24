'''1. Média aritmética. Escreva um programa Python que calcula a média aritmética de um
conjunto de valores fornecidos pelo usuário. O usuário deve entrar com o valor 0 indicando
que não serão mais fornecidos novos valores. Seu programa deve exibir uma mensagem de
erro se o primeiro valor fornecido pelo usuário for 0.
Dica: o número 0 não deve ser incluído no cálculo da média, pois ele só serve para sinalizar
o final da entrada de dados.'''

# Cria uma lista vazia
l = []

# Solicita números ao usuário até que seja inserido o número 0
while True:
    n = float(input("Insira um número (0 sai): "))
    if n == 0:
        break
    l.append(n)

# Verifica se a lista está vazia
if len(l) == 0:
    print("ERRO: O primeiro valor não pode ser 0.")

x = 0

# Imprime os elementos da lista
while x < len(l):
    print(f"{x+1}º Elemento = {l[x]}")
    x += 1

soma = 0

# Calcula a soma dos números fornecidos
for e in l:
    soma += e

# Calcula e imprime a média dos números fornecidos
print(f"A média dos números fornecidos é: {soma / len(l)}.")
