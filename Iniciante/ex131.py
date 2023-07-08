vitoGremio = vitoInter = empate = qntd = 0
while True:
    qntd += 1
    op = 0
    golInter, golGremio = input().split(' ')
    golInter = int(golInter)
    golGremio = int(golGremio)
    if golGremio > golInter:
        vitoGremio += 1
    elif golInter > golGremio:
        vitoInter += 1
    else:
        empate += 1

    print('Novo grenal (1-sim 2-nao)')
    op = int(input())
    if op == 2:
        vencedor = 'Inter venceu mais' if vitoInter > vitoGremio else 'Gremio venceu mais'
        break

print(f'{qntd} grenais')
print(f'Inter:{vitoInter}')
print(f'Gremio:{vitoGremio}')
print(f'Empates:{empate}')
print(vencedor)
