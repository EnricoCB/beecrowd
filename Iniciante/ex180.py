t = int(input())
v = []
c = 0
n = input('').split(' ')
for num in n:
    v.append(int(num))

for e in v:
    if c == 0:
        menor = e
        posicao = c
    if menor > e:
        menor = e
        posicao = c
    c += 1
print('Menor valor:', menor)
print('Posicao:',posicao)
