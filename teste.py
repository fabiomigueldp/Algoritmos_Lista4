l = []
while True:
    n = input("Digite um númeroi (0 sai): ")
    if n == None:
        break
    l.append(n)
x = 0
while x < len(l):
    print(l[x])
    x += 1