lista = input().split(' ')
n1 = float(lista[0])
n2 = float(lista[1])
n3 = float(lista[2])
n4 = float(lista[3])
m = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10
print('Media: {:.1f}'.format(m))
if m >= 7:
    print('Aluno aprovado.')
elif m < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.') 
    n = float(input())
    print('Nota do exame: {}'.format(n))
    nf = (n + m) / 2
    if nf >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado')
    print('Media final: {:.1f}'.format(nf))