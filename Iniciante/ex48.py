s = float(input())
if s <= 400:
    r = s * 0.15
    p = 15
elif s <= 800:
    r = s * 0.12
    p = 12
elif s <= 1200:
    r = s * 0.10
    p = 10
elif s <= 2000:
    r = s * 0.07
    p = 7
else:
    r = s * 0.04
    p = 4
print('Novo salario: {:.2f}'.format(s + r))
print('Reajuste ganho: {:.2f}'.format(r))
print('Em percentual: {} %'.format(p)) 