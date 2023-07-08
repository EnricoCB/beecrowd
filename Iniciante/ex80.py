for c in range(1, 101):
    valor = int(input())
    if c == 1:
        maior = valor
        posiçao = c
    if valor > maior:
        maior = valor
        posiçao = c


print(maior)
print(posiçao)