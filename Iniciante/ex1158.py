t = int(input())
for c in range(0, t):
    v = 0
    s = 0
    x, y = input().split(' ')
    x = int(x)
    y = int(y)
    while True:
        if x % 2 == 1:
            s += x
            v += 1
        x += 1
        if v == y:
            break
    print(s)