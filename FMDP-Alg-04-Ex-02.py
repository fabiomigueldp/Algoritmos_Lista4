'''2. Tabela de descontos. Uma loja está oferecendo uma liquidação com descontos de 60% em
uma variedade de produtos em final de estoque. O vendedor gostaria de ajudar seus clientes a
determinar o preço reduzido (com desconto) de seus produtos. Ele quer criar uma tabela que
mostra os preços originais e os preços após o desconto ser aplicado. Escreva um programa
Python usando laço de repetição que gere esta tabela mostrando o preço original, o valor de
desconto e o novo valor com desconto aplicado para produtos com os seguintes valores:
R$ 4.95, R$ 9.95, R$ 14.95, R$ 19.95 e R$ 24.95. Certifique-se que todos os valores são
mostrados com duas casas decimais.'''

# Cabeçalho

print("Preço\t\tDesconto\tPreço c/ desconto")

# Lista de preços

l = [4.95, 9.95, 14.95, 19.95, 24.95]

# Itera sobre os elementos da lista

for e in l:
    # Preço original
    n = e 

    # Porcentagem de desconto
    q = "60%"

    # Cálculo do preço com desconto
    c = e*0.4

    # Imprime os resultados formatados
    print(f"R$ {n: .2f}\t{q}\t\tR$ {c: .2f}")


'''
# Cabeçalho
print("Preço\t\tDesconto\tPreço c/ desconto")

# Lista de preços
l = [4.95, 9.95, 14.95, 19.95, 24.95]

# Itera sobre os elementos da lista
for e in l:
    # Preço original
    preco_original = e

    # Porcentagem de desconto
    desconto = "60%"

    # Cálculo do preço com desconto
    preco_com_desconto = e * 0.4

    # Imprime os resultados formatados
    print(f"R$ {preco_original:.2f}\t{desconto}\t\tR$ {preco_com_desconto:.2f}")
    '''
