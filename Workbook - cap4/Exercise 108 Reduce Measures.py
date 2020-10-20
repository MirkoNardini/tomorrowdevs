n = int(input('Numero di unità:'))
u = str(input('Unità di misurae:'))

if u == 'cucchiaini':
    cup = 0
    tab = 0
    teas = n
    if teas >= 3:
        at = teas // 3
        tab = tab + at
        teas = teas % 3

    if tab >= 16:
        tt = tab // 16
        cup = cup + tt
        tab = tab % 16
elif u == 'cucchiai':
    cup = 0
    tab = n
    teas = 0
    if tab >= 16:
        tt = tab // 16
        cup = cup + tt
        tab = tab % 16
elif u == 'tazza':
    cup = n
    tab = 0
    teas = 0
else:
    cup = 0
    tab = 0
    teas = 0

print(cup,'Tazze', tab,'Cucchiai da tavola', teas,'Cucchiaini da tè')
