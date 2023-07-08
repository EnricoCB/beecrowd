t = int(input())
for c in range(0, t):
    s = 0
    n = int(input())
    for i in range(1, n):
        if n % i == 0:
            s += i
    msg = f'{n} eh perfeito' if s == n else f'{n} nao eh perfeito'
    print(msg)