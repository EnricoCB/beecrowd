a, b = input().split(' ')
a = int(a)
b = int(b)
m = (b / a) 
m = str(m)
if a/b % 2 == 0 or b/a % 2 == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')