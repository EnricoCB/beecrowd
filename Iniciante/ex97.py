c = 0
i = 1
j = 7
while True:
    c += 1
    print(f'I={i} J={j}')
    j -= 1
    if c == 3:
        c = 0
        j += 5
        i += 2
    if i == 11:
        break
