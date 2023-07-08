n = int(input())
cont = 0
a = b = c = 1
acre = 2 
for contador in range(1, n*2 + 1):
    if contador == 0:
        a = b = c = 1
    elif cont == 1:
        b += 1
        c += 1
    elif cont == 2:
        cont = 0
        a += 1
        b += acre
        acre += 2
        c = a * b
    print(a, b, c)
    cont +=1