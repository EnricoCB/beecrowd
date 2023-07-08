a, b, c = input().split(' ')
a = float(a)
b = float(b)
c = float(c)
if c + a > b and a + b > c and c + b > a:
    p = c + a + b
    print('Perimetro = {:.1f}'.format(p))
else:
    p = ((a + b) * c) / 2
    print('Area = {:.1f}'.format(p))
