'''14. Binário para decimal. Escreva um programa Python que converte um número binário (base 2) para
decimal (base 10). Seu programa deve iniciar lendo um número binário como uma string. Então, ele
deve computar o número decimal equivalente processando cada dígito do número binário. Finalmente
seu programa deve exibir uma mensagem informando o número decimal calculado.'''

while True:

    n = input("Insira um número binário: ")
    n = n[::-1]
    x = 1
    soma = 0

    for i in n:
        i = int(i)
        if i == 1:
            soma += x
        x *= 2

    x = 1

    print(f"O número binário inserido é o decimal: {soma}.")