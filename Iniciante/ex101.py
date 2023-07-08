while True:
    s = 0
    a, b = input().split(' ')
    a = int(a)
    b = int(b)
    if a <= 0 or b <= 0:
        break
    if a < b:
        for c in range(a, b + 1):
            print(f'{c} ',end='')
            s += c
    else:
        for c in range(b, a + 1):
            print(f'{c} ', end='')
            s += c
    print(f'Sum={s}')
