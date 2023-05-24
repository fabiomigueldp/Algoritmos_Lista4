'''8. Aproximação do valor de pi. O valor aproximado de pi pode ser calculado pela série infinita
apresentada abaixo:
Escreva um programa Python que exiba 15 aproximações de pi. A primeira aproximação deve
ter apenas o primeiro termo da série (ou seja, o valor resultante vai ser somente 3). Cada nova
aproximação de mostrada pelo seu programa deve incluir mais um termo da série, sendo
cada vez uma aproximação mais precisa do que a anterior.'''

import math

a = 2
b = 3
c = 4
l = range(15)
pi = 0
m = 1

for e in l:
    if e == 0:
        pi += 3
        print(f"{pi:.{e}f}")
    else:
        pi += (4/(a*b*c))*m
        m *= -1
        pi = str(pi)
        print(f"{pi:.{e+2}s}")
        pi = float(pi)
        a += 2
        b += 2
        c += 2

print(f"math.pi = {math.pi}")
