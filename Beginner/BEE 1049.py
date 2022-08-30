i1 = str(input())
i2 = str(input())
i3 = str(input())
if i1 == 'vertebrado':
    if i2 == 'ave':
        if i3 == 'carnivoro':
            print('aguia')
        elif i3 == 'onivoro':
            print('pomba')
    elif i2 == 'mamifero':
        if i3 == 'onivoro':
            print('homem')
        elif i3 == 'herbivoro':
            print('vaca')
elif i1 == 'invertebrado':
    if i2 == 'inseto':
        if i3 == 'hematofago':
            print('pulga')
        elif i3 == 'herbivoro':
            print('lagarta')
    elif i2 == 'anelideo':
        if i3 == 'hematofago':
            print('sanguessuga')
        elif i3 == 'onivoro':
            print('minhoca')
