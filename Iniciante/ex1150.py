x = int(input())
z = x
while z <= x:
    z = int(input())
qntd = 1
v = x
while True:
    if v < z:
        v += x + 1
        x += 1
        qntd += 1
    else:
        print(qntd)
        break