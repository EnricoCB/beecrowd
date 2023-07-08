from math import pow, sqrt
a, b, c = input().split(' ')
a = float(a)
b = float(b)
c = float(c)
op = -4 * a * c
delta = b ** 2 + op
if delta <= 0 or a == 0:
    print('Impossivel calcular')
else:
    r1 = (-b + sqrt(delta)) / (2 * a)
    r2 = (-b - sqrt(delta)) / (2 * a)
    print('R1 = {:.5f}'.format(r1))
    print('R2 = {:.5f}'.format(r2))