n = int(input())
f = n
for c in range(n-1, 1, -1):
    f *= c
print(f)