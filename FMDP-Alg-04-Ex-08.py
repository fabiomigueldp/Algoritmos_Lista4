'''8. Cifra de César. Um dos primeiros exemplos conhecidos de criptografia foi utilizado pelo
imperador romano Julio César. César precisava fornecer instruções por escrito para seus
generais, mas não queria que seus inimigos descobrissem suas estratégias caso as
mensagens com as instruções fossem extraviadas. Com isso, ele acabou desenvolvendo o
que mais tarde ficou conhecido como a “cifra de César”.
A idéia por trás desta cifra é simples (e portanto não oferece proteção contra as técnicas
modernas de quebra de códigos). Cada letra da mensagem original é deslocada em 3
posições. Com isso, a letra A se torna letra D, B se torna E, C se torna F, e assim por diante. A
ultimas 3 letras do alfabeto são transformadas nas primeiras. X se torna A, Y se torna B e Z se
torna C. Caracteres que não são letras não são convertidos.
Escreva um program Python que implemente a cifra de César. Permita que o usuário forneça a
mensagem e a distância de deslocamento de letras (portanto não será o valor fixo de
deslocamento de 3 letras no alfabeto). Certifique-se que seu programa codifique corretamente
tanto letras maiúsculas quanto minúsculas. Seu programa também deve suportar valores
negativos de deslocamento de letras, assim ele pode ser usado tanto para codificar quanto
para decodificar mensagens.
Dica: você pode usar as funções ord(c) e chr(n) do Python. A função ord(c) retorna um
número inteiro que representa o caracter Unicode c. A função chr(n) retorna o caracter
Unicode representado pelo número inteiro n.'''

def cifra_de_cesar(mensagem, deslocamento):
    """
    Aplica a cifra de César em uma mensagem, deslocando as letras do alfabeto
    de acordo com o valor fornecido.

    Args:
        mensagem (str): A mensagem a ser cifrada.
        deslocamento (int): O valor de deslocamento das letras.

    Returns:
        str: A mensagem cifrada.

    """

    resultado = ""
    for letra in mensagem:
        if letra.isalpha():
            if letra.isupper():
                codigo = ord('A')
            else:
                codigo = ord('a')
            deslocado = (ord(letra) - codigo + deslocamento) % 26 + codigo
            resultado += chr(deslocado)
        else:
            resultado += letra
    return resultado


# Entrada de dados
mensagem = input("Digite a mensagem: ")
deslocamento = int(input("Digite a distância de deslocamento: "))

# Cifrar mensagem
mensagem_codificada = cifra_de_cesar(mensagem, deslocamento)
print("Mensagem codificada:", mensagem_codificada)

# Decifrar mensagem
mensagem_decodificada = cifra_de_cesar(mensagem_codificada, -deslocamento)
print("Mensagem decodificada:", mensagem_decodificada)
