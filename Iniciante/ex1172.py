n = []
for c in range(0, 10):
    n.append(int(input()))
    if n[c] <= 0:
        n[c] = 1

for c in range(0, 10):
    print(f'X[{c}] = {n[c]}')