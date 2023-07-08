qntd = int(input())
dentro = 0
fora = 0
for c in range(0, qntd):
    n = int(input())
    if 10 <= n <= 20:
        dentro += 1
    else:
        fora += 1
    
print(f'{dentro} in')
print(f'{fora} out')