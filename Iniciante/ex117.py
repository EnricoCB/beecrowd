m = qntd = 0
while True:
    n = float(input())
    if n < 0 or n > 10:
        print('nota invalida')
    else:
        qntd += 1
        m += n
    if qntd == 2:
        m /= qntd
        break

print(f'media = {m:.2f}')
