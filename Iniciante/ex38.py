c, qntd = input().split(' ')
c = int(c)
qntd = int(qntd)
if c == 1:
    p = qntd * 4
if c == 2:
    p = qntd * 4.50
if c == 3:
    p = qntd * 5
if c == 4:
    p = qntd * 2
if c == 5:
    p = qntd * 1.50
print('Total: R$ {:.2f}'.format(p))
