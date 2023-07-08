numeros = input().split(' ')
for c, numero in enumerate(numeros):
    if c == 0:
        a = int(numero)
        s = 0
    else:
        if int(numero) > 0:
            n = int(numero)

for i in range(0, n):
    s += a + i

print(s)