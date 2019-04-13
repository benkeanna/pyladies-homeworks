from random import randrange

body = 0

while body < 21:
    print('Máš ', body,' bodů')
    odpoved = input('Otočit kartu?')
    if odpoved == 'ano':
        karta = randrange(2,11)
        print('Otočila jsi',body)
        body = body + karta
    elif odpoved == 'ne':
        break
    else:
        print ('Odpovídej "ano" nebo "ne".')

if body == 21:
    print('Vyhrála jsi!')
elif body > 21:
    print('Prohrála jsi.')
else:
    print('Škoda, chybělo ti jen', 21 - body,'bodů.')
