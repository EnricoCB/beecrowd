n = float(input())
if n <= 2000:
    print('Isento')
elif n <= 3000:
    n -= 2000
    r = n * 8 / 100
    print('R$ {:.2f}'.format(r))
elif n <= 4500:
    n = n - 3000
    i = 1000 * 8 / 100
    n = n * 18 / 100
    r = n + i
    print('R$ {:.2f}'.format(r))
else:
    n = n - 4500
    i = 1000 * 8 / 100
    p = 1500 * 18 / 100
    n = n * 28 / 100
    r = n + i + p
    print('R$ {:.2f}'.format(r))

