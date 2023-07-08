a,b,c = input().split(' ')
a = float(a)
b = float(b)
c = float(c)
o = [a, b, c]
o.sort(reverse=True)
a = o[0]
b = o[1]
c = o[2]
if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
    if a**2 == b**2 + c**2:
        print('TRIANGULO RETANGULO')
    if a**2 > b**2 + c**2:
        print('TRIANGULO OBTUSANGULO')
    if a**2 < b**2 + c**2:
        print('TRIANGULO ACUTANGULO')
    if a == b and a == c and b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or a == c or b == c:
        print('TRIANGULO ISOSCELES')