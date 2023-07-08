n1 = int(input())
s = 0
n2 = int(input())
if n1 < n2:
    for c in range(n1+1, n2):
        if c % 2 == 1:
            s += c
else:
    for c in range(n1-1, n2, -1):
        if c % 2 == 1:
            s += c

print(s)