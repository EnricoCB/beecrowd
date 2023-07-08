n = list()
for c in range(0, 6):
    x = float(input())
    if x >= 0:
        n.append(x)

s = sum(n)
s = s / len(n)
print(f'{len(n)} valores positivos')
print(f'{s:.1f}')