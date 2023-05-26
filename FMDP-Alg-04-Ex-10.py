'''10. Palíndromo. Uma string é considerada um palíndromo se, de trás para frente, ela for idêntica
à string original. Por exemplo: “arara”, “osso”, “radar”. Escreva um programa Python usando
laço de repetição para determinar se uma palavra fornecida pelo usuário é ou não é um
palíndromo. Seu programa deve exibir uma mensagem informando o resultado.'''

mensagem = input("Insira uma mensagem: ")

"""
Verifica se a mensagem é um palíndromo.
Divide a mensagem em duas metades e verifica se a primeira metade é igual à segunda metade invertida.
"""

if len(mensagem) % 2 == 0:
    metade1 = mensagem[0:(len(mensagem)//2)]
    metade2 = mensagem[(len(mensagem)//2):]
    imetade2 = metade2[::-1]

    # Converte as letras da primeira metade em códigos Unicode
    for letra in metade1:
        codigo_metade1 = ord(letra)

    # Converte as letras da segunda metade invertida em códigos Unicode
    for letra in imetade2:
        codigo_imetade2 = ord(letra)

    # Verifica se os códigos Unicode das metades são iguais
    if codigo_metade1 == codigo_imetade2:
        print("Sua mensagem é um palíndromo.")
    else:
        print("Sua mensagem não é um palíndromo.")

else:
    metade1 = mensagem[0:(len(mensagem)//2)]
    meio = mensagem[(len(mensagem)//2)]
    metade2 = mensagem[(len(mensagem)//2)+1:]
    imetade2 = metade2[::-1]

    # Converte as letras da primeira metade em códigos Unicode
    for letra in metade1:
        codigo_metade1 = ord(letra)

    # Converte as letras da segunda metade invertida em códigos Unicode
    for letra in imetade2:
        codigo_imetade2 = ord(letra)

    # Verifica se os códigos Unicode das metades são iguais
    if codigo_metade1 == codigo_imetade2:
        print("Sua mensagem é um palíndromo.")
    else:
        print("Sua mensagem não é um palíndromo.")
