while True:
    n = int(input())
    v = 0
    qntd = 0
    if n == 0:
        break
    while True:
        if n % 2 == 0:
            v += n
            qntd += 1
        n += 1
        if qntd == 5:
            break
    print(v)