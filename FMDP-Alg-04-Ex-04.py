'''4. Perímetro de um polígono. Crie um programa Python para calcular o perímetro de um
polígono sendo fornecidas as coordenadas x e y de cada um de seus vértices. Inicie lendo x e
y do primeiro vértice. Depois disso continue lendo x e y dos próximos vértices até que o
usuário entre com uma linha em branco para o valor da coordenada x (ou seja, quando ele
digitar “Enter" ou “Return" sem fornecer um valor). Cada vez que você ler as coordenadas de
um novo vértice, você deve calcular a distância em relação ao vértice anterior e acrescentá-la
ao valor do perímetro. A figura abaixo ilustra como se calcula a distância entre dois pontos
sendo dadas suas coordenadas x e y.
Quando o usuário entrar com a linha em branco na coordenada x, seu programa deve
adicionar ao perímetro a distância do último ponto até o primeiro. Depois disso, deve exibir o
valor do perímetro. Um exemplo de entrada é mostrado abaixo (o valores digitados pelo
usuário estão em negrito.
Digite a coordenada x de um ponto: 0
Digite a coordenada y de um ponto: 0
Digite a coordenada x de um ponto (enter para sair): 1
Digite a coordenada y de um ponto: 0
Digite a coordenada x de um ponto (enter para sair): 0
Digite a coordenada y de um ponto: 1
Digite a coordenada x de um ponto (enter para sair):
O perímetro deste polígono é igual a 3.41421356237309'''

import math
import sys

# Variável para armazenar o valor do perímetro do polígono
perimetro = 0

# Coordenadas do primeiro ponto
x1 = float(input("Insira a coordenada x de um ponto: "))
y1 = float(input("Insira a coordenada y de um ponto: "))

# Variáveis para manter as coordenadas do ponto anterior
xx = x1
yy = y1

while True:
    # Solicitar ao usuário as coordenadas x e y do próximo ponto
    x = input("Insira a coordenada x de um ponto (<enter> para sair): ")
    
    # Verificar se o usuário deseja encerrar a repetição
    if x == "":
        break
    
    try:
        # Converter o valor de x para float
        x = float(x)
    except ValueError:
        # Se o valor inserido não puder ser convertido em float, encerrar a repetição
        break

    y = input("Insira a coordenada y de um ponto: ")
    
    if y == "":
        # Se nenhuma coordenada y for fornecida, definir o valor de y como 0
        print("ERRO: é necessário inserir alguma coordenada y para um ponto, y será gravado como 0.")
        y = 0
    
    try:
        # Converter o valor de y para float
        y = float(y)
    except ValueError:
        # Se o valor inserido não puder ser convertido em float, encerrar o programa
        print("Dado inválido, fim da execução.")
        sys.exit()

    # Calcular a distância entre o ponto atual e o ponto anterior usando a fórmula da distância Euclidiana
    distancia = math.sqrt((x - xx) ** 2 + (y - yy) ** 2)

    # Adicionar a distância ao perímetro total do polígono
    perimetro += distancia

    # Atualizar as coordenadas do ponto anterior para o ponto atual
    xx = x
    yy = y

# Calcular a distância entre o último ponto e o primeiro ponto para fechar o polígono
distancia = math.sqrt((x1 - xx) ** 2 + (y1 - yy) ** 2)

# Adicionar a distância ao perímetro total do polígono
perimetro += distancia

# Exibir o resultado do perímetro do polígono
print(f"O perímetro deste polígono é igual a {perimetro}.")


