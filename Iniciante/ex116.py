n = int(input())
for c in range(0, n):
    a, b = input().split(' ')
    a = int(a)
    b = int(b)
    try:
        r = a / b
    except ZeroDivisionError:
        print('divisao impossivel')
    else:
        print(r)
