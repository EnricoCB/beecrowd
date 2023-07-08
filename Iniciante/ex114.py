senha = 2002
while True:
    n = int(input())
    if n == senha:
        print('Acesso Permitido')
        break
    else:
        print('Senha Invalida')