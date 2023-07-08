q, l = input().split(' ')
q = int(q)
l = int(l)
n = 1
for c in range(1, l+1, q):
    for x in range(1, q+1):       
        if x == q:
            print(n, end='')
        else:
            print(n, end=' ')
        if n == l:
            break
        n += 1
    print()