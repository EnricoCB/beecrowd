qntd = int(input())
for c in range(0, qntd):
    soma = 0
    a, b = input().split(' ')
    a = int(a)
    b = int(b)
    if a < b:
        for num in range(a + 1, b):
            if num % 2 == 1:
                soma += num
    else:
        for num in range(b + 1, a):
            if num % 2 == 1:
                soma += num
    print(soma)