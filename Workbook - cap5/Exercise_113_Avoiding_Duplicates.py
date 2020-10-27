ins = input('inserisci una parola: ')

valore = []
valore.append(ins)

while 0 < 1:
    if ins == '':
        break
    elif ins in valore:
        ins = ins
    else:
        valore.append(ins)

for i in ins:
    print(i)
    
