qntd = int(input())
total = qntdSapo = qntdCoelho = qntdRato = 0
for c in range(0, qntd):
    qntdCobaias = input().split(' ')
    qntdCobaias[0] = int(qntdCobaias[0])
    total += qntdCobaias[0]
    if qntdCobaias[1] == 'S':
        qntdSapo += qntdCobaias[0]
    elif qntdCobaias[1] == 'C':
        qntdCoelho += qntdCobaias[0]
    elif qntdCobaias[1] == 'R':
        qntdRato += qntdCobaias[0]

porcentCoelho = qntdCoelho * 100 / total
porcentSapo = qntdSapo * 100 / total
porcentRato = qntdRato * 100 / total

print(f'Total: {total} cobaias')
print('Total de coelhos:', qntdCoelho)
print('Total de ratos:', qntdRato)
print('Total de sapos:', qntdSapo)
print(f'Percentual de coelhos: {porcentCoelho:.2f} %')
print(f'Percentual de ratos: {porcentRato:.2f} %')
print(f'Percentual de sapos: {porcentSapo:.2f} %')
