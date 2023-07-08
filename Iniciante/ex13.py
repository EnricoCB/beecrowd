lista = input().split(' ')
a = int(lista[0])
b = int(lista[1])
c = int(lista[2])
maiorab = (a + b + abs(a - b)) / 2
maiorab = int(maiorab)
if c > maiorab:
    print('{} eh o maior'.format(c))
else:
    print('{} eh o maior'.format(maiorab))
