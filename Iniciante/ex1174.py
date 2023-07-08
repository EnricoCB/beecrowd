n = []
for c in range(0, 100):
    n.append(float(input()))

for i in range(0, 100):
    if n[i] <= 10:
        print(f'A[{i}] = {n[i]}')