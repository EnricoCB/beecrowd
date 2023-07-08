x = int(input())
y = int(input())
s = 0
if x < y:
    for c in range(x, y + 1):
        if c % 13 != 0:
            s += c
else:
    for c in range(x, y - 1, -1):
        if c % 13 != 0:
            s += c
print(s)