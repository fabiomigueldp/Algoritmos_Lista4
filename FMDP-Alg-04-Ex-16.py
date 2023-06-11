'''16. Cara ou coroa. Qual é o menor número de vezes que você precisa sortear uma moeda para
ter três resultados consecutivos iguais de cara ou de coroa? Qual é o número máximo de
sorteios necessários? Quantos sorteios precisamos em média? Neste exercício vamos
explorar estas questões criando um programa que simula várias séries de sorteios de cara ou
coroa.
Crie um programa que utilize o gerador de números randômicos do Python para simular o
sorteio de uma moeda várias vezes. A moeda simulada deve ser justa, ou seja, deve ter a
mesma probabilidade de gerar cara e coroa. Seu programa deve continuar simulando sorteios
até que ocorra uma sequencia de 3 caras ou de 3 coroas consecutivas. Exiba A para cada vez
que ocorrer cara e O para cada vez que ocorrer coroa, com todos os resultados sendo
exibidos na mesma linha. Então exiba a quantidade de sorteios que levou para chegar a três
resultados iguais consecutivos. Quando seu programa executar, ele deve fazer esta simulação
10 vezes e, ao final, mostrar a quantidade média de sorteios necessária. Abaixo segue um
exemplo de saída do programa:
A O O O (4 sorteios)
A A O O A O A O O A A O A O O A O O O (19 sorteios)
O O O (3 sorteios)
O A A A (4 sorteios)
A A A (3 sorteios)
O A O O A O A A O O A A O A O A A A (18 sorteios)
A O O A A A (6 sorteios)
A O A A A (5 sorteios)
O O A O O A O A O A A A (12 sorteios)
O A O O O (5 sorteios)
Na média, foram necessários 7.9 sorteios.'''

import random

def cara_ou_coroa():
    if random.random() < 0.5:
        return "A"
    else:
        return "O"
    
x = 0
y = 100000
tentativas_totais = 0
s = ""

while x < y:
    while len(s) < 3:
        s += cara_ou_coroa()
    s_total = s
    tentativas = 3
    while s != "AAA" and s != "OOO":
        novo_sorteio = cara_ou_coroa()
        s += novo_sorteio
        s_total += novo_sorteio
        s = s[1:]
        tentativas += 1
    s_total = ' '.join(list(s_total))
    tentativas_totais += tentativas
    print(f"{s_total} ({tentativas} sorteios.)")
    s = ""
    x += 1

print(f"Na média, foram necessários {tentativas_totais/y} sorteios.")
