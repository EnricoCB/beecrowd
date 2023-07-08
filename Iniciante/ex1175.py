n = []
for c in range(0, 10):
    n.append(int(input()))

a = len(n) - 1
aux = 0
li = len(n) / 2
for i in range(0, len(n)):
    aux = n[i]
    n[i] = n[a]
    n[a] = aux
    a -= 1
    print(f'N[{i}] = {n[i]}')