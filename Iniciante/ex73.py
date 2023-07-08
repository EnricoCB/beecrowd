n = int(input())
m = 2
for c in range(2, n+1):
    if c % 2 == 0:
        print(f'{c}^{m} = {c**m}')