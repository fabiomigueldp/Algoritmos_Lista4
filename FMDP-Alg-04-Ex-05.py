'''5. Valor das entradas. Um determinado zoológico estipula o valor da entrada baseado na idade
do visitante. Visitantes com até dois anos de idade não precisam pagar. Crianças entre 3 e 12
anos de idade pagam R$ 14.00. Idosos com 65 anos ou mais pagam R$ 18.00. Todos os
demais pagam R$ 23.00. Crie um programa que inicia lendo as idades, uma por uma, de um
grupo de pessoas. O usuário deve entrar uma linha em branco para indicar que não há mais
pessoas no grupo. Depois disso, seu programa deve exibir uma mensagem informando o
preço total de todas as entradas para o grupo. O valor deve ser exibido com duas casas
decimais.'''

# Cria uma lista vazia

l = []

# Solicita e insere os dados na lista

while True:
    n = input("Informe a(s) idade(s) do(s) cliente(s), pressione <ENTER> sem inserir nenhum valor para finalizar: ")
    try:
        
        n = float(n)
    except ValueError:
        
        break
    l.append(n)
    print(l)

# Define variáveis

valor = 0
k = 1
uvalor = 0

# Itera sobre cada valor da lista, cálcula o débito e imprime a lista de clientes

for e in l:
    if e < 3:
        valor += 0
    if 3 <= e < 13:
        valor += 14
    if 13 <= e < 65:
        valor += 23
    if e >= 65:
        valor += 18
    print(f"A idade do {k}º cliente é {e}ano(s), ele pagará R${valor - uvalor:.2f}.")
    k += 1
    uvalor = valor

# Imprime o resultado

print("\n")
print(f"O valor total devido é R${valor:.2f}.")