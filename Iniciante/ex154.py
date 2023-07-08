m = c = 0
while True:
    i = int(input())
    if i < 0:
        break
    c += 1
    m += i

m /= c
print(f'{m:.2f}')