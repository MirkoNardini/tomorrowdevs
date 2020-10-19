conto = float(input("Inserire l'importo: $"))
ta = float(input("Inserire il tasso di interesse annuale %"))
a = float(input("Inserire il numero di volte all'anno che l'interesse è aumentato:"))
t = float(input('Inserire il numero di anni che il conto sarà lasciato per guadagnare interessi: '))

ta /= 100 
A = conto * ((1 + (ta / a))**(a * t))

print('Dopo ', t, ' anno, $', format(A, ',.2f'), ' sarà nel conto. ', sep='')
