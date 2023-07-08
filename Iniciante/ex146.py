while True:
    l = int(input())
    if l == 0:
        break
    for c in range(1, l+1):
        if c == l:
            print(c, end='')
        else:
            print(c, end=' ')
    print()