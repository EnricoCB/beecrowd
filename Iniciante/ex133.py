x = int(input())
y = int(input())

if x < y:
    for c in range(x+1, y):
        if c % 5 == 2 or c % 5 == 3:
            print(c)
else:
    for c in range(y+1, x):
        if c % 5 == 2 or c % 5 == 3:
            print(c)