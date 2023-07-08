n = int(input())
a1 = f = 0
a2 = 1
print(a1, a2, end=' ')
for c in range(0, n-2):
    f = a1 + a2
    if c == n-3:
        print(f)
    else:
        print(f,end=' ')
    a1 = a2
    a2 = f