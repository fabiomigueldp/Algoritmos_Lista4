l = []
while True:
    n = int(input("Digite um númeroi (0 sai): "))
    if n == 0:
        break
    l.append(n)
x = 0
while x < len(l):
    print(l[x])
    x += 1