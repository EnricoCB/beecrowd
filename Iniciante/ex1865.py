n = int(input())

for c in range(0, n):
    nome, f = input().split(' ')
    msg = 'Y' if nome.lower() == 'thor' else 'N'
    print(msg)