c = a = d = g = 0
while c != 4:
    c = int(input())

    if c == 1:
        a += 1
    elif c == 2:
        g += 1
    elif c == 3:
        d += 1

print('MUITO OBRIGADO')
print(f'Alcool: {a}\nGasolina: {g}\nDiesel: {d}')