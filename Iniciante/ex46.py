h1, h2 = input().split(' ')
h1 = int(h1)
h2 = int(h2)
if h1 >= h2:
    r = (24 - h1) + h2
else:
    r = h2 - h1
print('O JOGO DUROU {} HORA(S)'.format(r))