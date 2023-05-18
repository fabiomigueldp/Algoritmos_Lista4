'''3. Faça um programa Python que calcule os quadrados e cubos dos números de 0 a 10 e
imprima os valores resultantes no formato de tabela, como segue:
Número Quadrado Cubo
0 0 0
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
6 36 216
7 49 343
8 64 512
9 81 729
10 100 1000
Observação: para imprimir com espaços tabulados (tecla “tab”), coloque o caracter “\t” dentro
da string a ser impressa. Por exemplo: print(“Número\t\tQuadrado\t\tCubo”)'''

# Header

print("Número\t\tQuadrado\tCubo")

# Repetição for

for e in range(11):
    n = e
    q = e**2
    c = e**3
    print(f"{n}\t\t{q}\t\t{c}")
