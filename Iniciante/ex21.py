valor = float(input())
print('NOTAS:')
cedulas = [100, 50, 20, 10, 5, 2]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
for cedula in cedulas:
    qntd = int(valor // cedula)
    print('{} nota(s) de R$ {:.2f}'.format(qntd, cedula))
    valor -= qntd * cedula
print('MOEDAS:')
for moeda in moedas:
    qntd = int(round(valor, 2) / moeda)#round com paremetro 2 aredonda o numero para cima
    print('{} moeda(s) de R$ {:.2f}'.format(qntd, moeda))
    valor -= qntd * moeda