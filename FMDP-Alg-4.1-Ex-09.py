'''9. Adapte seu programa da questão anterior para que ele receba uma quantidade indefinida de
notas até que o usuário pressione <enter> sem fornecer nenhuma nota.'''

l = []
soma = 0
x = 0

# Entrada das notas
while True:
    entrada = input(f"Insira o {x + 1}º elemento (pressione <enter> para encerrar): ")
    if entrada == '':
        break  # Sai do loop se o usuário pressionar <enter> sem fornecer uma nota
    nota = float(entrada)
    l.append(nota)
    soma += nota
    x += 1

# Imprime os elementos
x = 0
while x < len(l):
    print(f"{x + 1}º elemento: {l[x]}")
    x += 1

# Calcula e imprime a média
media = soma / len(l)
print(f"A média da soma dos elementos é: {media:.2f}")

# Encontra o maior número
x = 0
maior = l[0]

while x < len(l):
    if l[x] > maior:
        maior = l[x]
    x += 1

print(f"O maior número inserido é {maior}.")

# Encontra o menor número
x = 0
menor = l[0]

while x < len(l):
    if l[x] < menor:
        menor = l[x]
    x += 1

print(f"O menor número inserido é {menor}.")
