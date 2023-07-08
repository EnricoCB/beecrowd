cha = int(input())
qntd = 0
tentativa = input().split(' ')
for num in tentativa:
    if int(num) == cha:
        qntd += 1

print(qntd)
