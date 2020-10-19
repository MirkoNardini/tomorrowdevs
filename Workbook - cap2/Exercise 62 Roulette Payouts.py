from random import randrange

valore = randrange(0, 38)
if valore == 37:
    print("La rotazione ha portato a 00...")
else:
    print("La rotazione ha portato a %d..." % valore)

if valore == 37:
    print("Paga 00")
else:
    print("Paga", valore)

if valore % 2 == 1 and valore >= 1 and valore <= 9 or \
valore % 2 == 0 and valore >= 12 and valore <= 18 or \
valore % 2 == 1 and valore >= 19 and valore <= 27 or \
valore % 2 == 0 and valore >= 30 and valore <= 36:
    print("Paga Rosso")
elif valore == 0 or valore == 37:
    pass
else:
    print("Paga Nero")

if valore >= 1 and valore <= 36:
    if valore % 2 == 1:
        print("Paga dispari")
    else:
        print("Paga anche")

if valore >= 1 and valore <= 18:
    print("Pagare 1 a 18")
elif valore >= 19 and valore <= 36:
    print("Pagare 19 a 36")
