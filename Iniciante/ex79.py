qntd = int(input())
for c in range(0, qntd):
    media = 0.0
    nota1, nota2, nota3 = input('').split(' ')
    nota1 = float(nota1)
    nota2 = float(nota2)
    nota3 = float(nota3)
    print(f'Notas: 1° {nota1}   2° {nota2}   3°{nota3}')
    media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10
    media = round(media, 1)
    print(media)