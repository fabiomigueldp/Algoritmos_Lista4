'''12. Tabela de multiplicação. Neste exercício você deve criar uma tabela de multiplicação
mostrando os produtos de todos os inteiros de 1 vezes 1 até 10 vezes 10. Sua tabela deve
incluir uma linha de cabeçalho com números de 1 a 10, e também uma coluna com os
mesmos números. A saída esperada do programa deve ser semelhante ao mostrado abaixo:

Ao desenvolver seu programa, talvez você ache conveniente exibir um valor com print sem
mover para a próxima linha. Isso pode ser feito adicionando-se end="" como último parâmetro
da função print (Exemplo: print(x, end=“”)).'''

# Tabela de multiplicação

# Imprime a linha de cabeçalho
print("  ", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print()

# Imprime as linhas da tabela
for i in range(1, 11):
    print(f"{i:2}", end="")
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()
