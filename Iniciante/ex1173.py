n = []
n.append(int(input()))
v = n[0]
for c in range(0, 9):
    v *= 2
    n.append(v)

for c in range(0, 10):
    print(f'N[{c}] = {n[c]}')