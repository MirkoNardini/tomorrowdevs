ins =int(input('''inserisci tutti i valori che desideri
ricorda solo che inserendo lo 0 terminerai il programma

inserisci il valore desiderato:  '''))

valori = []
valori.append(ins)

for cont in valori:
    ins = int(input('inserisci un altro valore: '))
    if ins == 0:
        break
    valori.append(ins)

valori.sort()
for cont in valori:
    print(cont)
