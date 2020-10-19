rumore = int(input(" inserire il valore in db di un rumore: "))

if rumore == 130:
    print("il rumore corrisponde al martello pneumatico")
elif rumore == 106:
    print("il rumore corrisponde al tosaerba a gas")
elif rumore == 70
    print("il rumore corrisponde alla sveglia")
elif rumore == 40
    print("il rumore corrisponde a una stanza sienziosa")
elif rumore > 106 and rumore < 130:
    print("il rumore corrisponde a una via di mezzo tra un tosaerba a gas e \
           un martello pneumatico")
elif rumore > 70 and < 106:
    print("rumore corrisponde al rumore intermedio tra una sveglia e \
           un tosaerba a gas")
elif rumore > 40 and < 70:
    print("rumore corrisponde al rumore intermedio tra una stanza silensiosa \
           e una sveglia")
elif rummore < 40:
    print("rumore è più silensioso di quello di una stanza silensiosa")
