'''13. Fatoração numérica. A fatoração de um número inteiro n pode ser feita por meio de números
primos de acordo com o procedimento descrito abaixo:
Inicialize fator com valor 2
Enquanto fator for menor ou igual a n, faça
Se n for divisível por fator então
Concluímos que fator faz parte da fatoração de n
Faça divisão inteira de n por fator
Senão
Incremente fator em uma unidade
Escreva um programa Python que lê um número inteiro do usuário. Se o valor fornecido pelo
usuário é menor do que 2, seu programa deve exibir uma mensagem de erro. Caso contrário,
seu programa deve exibir os números primos que podem ser multiplicados para formar o
número n, com um fator exibido em cada linha. Por exemplo:
Digite um número inteiro (maior ou igual a 2): 72 36 18 9 3 1
2
2
2
3
3'''
while True:
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    n = int(input("Insira um número inteiro: "))

    divisor = 2

    while n != 1 or is_prime(n):
        if n % divisor == 0:
            n /= divisor
            print(divisor)
        elif n % divisor != 0:
            divisor += 1
            if is_prime(divisor) == False:
                divisor += 1