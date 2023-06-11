'''15. Decimal para binário. Escreva um programa Python que converte um número decimal (base 10) para o
correspondente número binário (base 2). Leia o número decimal como um número inteiro fornecido pelo
usuário. Depois disso, use o algoritmo de divisão mostrado abaixo para fazer a conversão. Quando o
algoritmo terminar, a variável result contém a representação binária do número. Ao final exiba uma
mensagem informando o valor de result.
Inicialize result como uma string vazia
Seja q o número decimal a ser convertido
Repita
r recebe o resto da divisão de q por 2
converta r para uma string e adicione no início de result
faça a divisão inteira de q por 2 (descartando o resto) e guarde o resultado em q
Até que q seja igual a zero'''

n = int(input("Insira um número inteiro: "))


x = 0
soma = 0
b = 1


while n != 0:
    r = n % 2
    soma += r * (10**x)
    x += 1
    n = n//2
  


soma = str(soma)
print(f"O número decimal inserido corresponde ao binário {soma}.")
