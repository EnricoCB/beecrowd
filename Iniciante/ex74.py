qntd = int(input())
for c in range(0, qntd):
    n = int(input())
    if n % 2 == 0:
        if n > 0:
            print('EVEN POSITIVE')
        if n < 0:
            print('EVEN NEGATIVE')
    else:
        if n > 0:
            print('ODD POSITIVE')
        if n < 0:
            print('ODD NEGATIVE')
    if n == 0:
        print('NULL')