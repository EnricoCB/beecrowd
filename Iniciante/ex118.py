m = qntd = 0
while True:
    n = float(input())
    if n < 0 or n > 10:
        print('nota invalida')
    else:
        qntd += 1
        m += n
    if qntd == 2:
        op = ' '
        m /= qntd
        qntd = 0
        print(f'media = {m:.2f}')
        m = 0
        while op != 1 and op != 2:
            print('novo calculo (1-sim 2-nao)')
            op = int(input())
        if op == 2:
            break
