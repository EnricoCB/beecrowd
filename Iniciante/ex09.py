nome = input()
salariofixo =  float(input())
vendas = float(input())
salarionovo = salariofixo + vendas * 0.15
print('TOTAL = R$ {:.2f}'.format(salarionovo))