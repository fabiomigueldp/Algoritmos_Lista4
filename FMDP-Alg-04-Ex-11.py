'''11. Palíndromos com múltiplas palavras. O conceito de palíndromo também pode ser aplicado
a frases, por exemplo: “A base do teto desaba”. Faça um novo programa Python que
modifique o programa do exercício anterior para verificar se frases são palíndromos. Seu
programa vai precisar ignorar os espaços em brando das frases. Como desafio adicional,
amplie sua solução para que também ignore sinais de pontuação e trate letras maiúsculas e
minúsculas como equivalentes.'''

mensagem = input("Insira uma mensagem: ")  # Solicita ao usuário que insira uma mensagem.
mensagem = mensagem.lower()  # Converte a mensagem para minúsculas.
mensagem = "".join(mensagem.split())  # Remove os espaços em branco da mensagem.
mensagemx = ""

# Remove caracteres diferentes de letras da mensagem.
for letra in mensagem:
    if letra.isalpha():
        mensagemx += letra

mensagem = mensagemx  # Atribui a versão filtrada da mensagem à variável "mensagem".

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