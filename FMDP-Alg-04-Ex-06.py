'''6. Bits de paridade. Um bit de paridade é um mecanismo para detecção de erros em dados
transmitidos por uma conexão não confiável, como linha telefônica por exemplo. A idéia básica
é que, a cada grupo de 8 bits, seja acrescentado um bit adicional de forma que erros em bits
individuais possam ser detectados.
Os bit de paridade podem ser computados para paridade par ou paridade ímpar. Se for usada
paridade par, então o bit de paridade a ser transmitido deve ser tal que o número total de bits
“1” transmitidos (8 bits de dados + 1 bit de paridade) é par. Se for utilizada paridade ímpar, o
número total de bits “1” transmitidos deve ser ímpar.
Escreva um programa Python que compute o bit de paridade para grupos de 8 bits fornecidos
pelo usuário utilizando paridade par. Seu programa deve ler strings contendo 8 bits (portanto
as strings vai ser sequencias de 8 caracteres 0 ou 1) até que o usuário entre com uma linha
em branco. Logo após o usuário fornecer cada string, seu programa deve exibir uma
mensagem informando se o bit de paridade deve ser 0 ou 1. O programa também deve exibir
uma mensagem de erro caso o usuário entre com algo que não seja a sequência de 8 bits
Dica: você deve ler o impute do usuário como uma string. Então, você pode usar o método
count do tipo string para determinar a quantidade de "zeros" e "uns" na string. Você pode
encontrar informação sobre o método count na internet.'''

import sys

while True:
    # Solicita ao usuário uma sequência de 8 bits
    string = str(input("Insira uma sequência de 8 bits para calcular o bit de paridade, ou uma linha vazia para sair: "))
    
    # Conta o número de ocorrências de "0" na string
    n0 = string.count("0") 

    # Conta o número de ocorrências de "1" na string
    n1 = string.count("1")

    # Verifica se o usuário inseriu uma linha vazia para sair do programa
    if string == "":
        print("Programa encerrado.")
        sys.exit()

    try:
        # Tenta converter a string para um número inteiro
        string = int(string)
    except ValueError:
        print("\n\nERRO\nO dado inserido deve ser uma sequência de 8 bits.\n\n")

    # Verifica se a sequência de bits possui 8 caracteres
    if (n0 + n1) != 8:
        print("\n\nERRO\nO dado inserido deve ser uma sequência de 8 bits.\n\n")

    else:
        # Verifica se o bit de paridade é 0 ou 1
        if n1 % 2 == 0:
            print("O bit de paridade desta string é 0.\n")
        else:
            print("O bit de paridade desta string é 1.\n")
