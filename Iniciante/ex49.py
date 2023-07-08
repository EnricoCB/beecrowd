t1 = input()
t2 = input()
t3 = input()
if t1 == 'vertebrado':
    if t2 == 'ave':
        if t3 == 'carnivoro':
            a = 'aguia'
        if t3 == 'onivoro':
            a = 'pomba'
    if t2 == 'mamifero':
        if t3 == 'onivoro':
            a = 'homem'
        if t3 == 'herbivero':
            a = 'vaca'
if t1 == 'invertebrado':
    if t2 == 'inseto':
        if t3 == 'hematofago':
            a = 'pulga'
        if t3 == 'herbivoro':
            a = 'largarta'
    if t2 == 'anelideo':
        if t3 == 'hematofago':
            a = 'sangessuga'
        if t3 == 'onivoro':
            a = 'minhoca'
print(a)