i = 0
j = 1
c = 0
while i != 2.2:
    c += 1
    j = round(j, 1)
    i = round(i, 1)

    if i == 1 or i == 0 or i == 2:
        print(f'I={i:.0f} J={j:.0f}')
    else:
        print(f'I={i} J={j}')
    if c == 3:         
        c = 0
        i += 0.2
        j += 0.2
        j -= 3
    j += 1
