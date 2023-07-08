qntd = int(input())
for c in range(0, qntd):
    n = int(input())
    v = 0
    for i in range(1, n+1):
        if n % i == 0:
            v += 1
    msg = f'{n} eh primo' if v == 2 else f'{n} nao eh primo'
    print(msg)