n1 = int(input("Inserisci 1 numeri desiderati: "))
n2 = int(input("Inserisci 2 numeri desiderati: "))
n3 = int(input("Inserisci 3 numeri desiderati: "))

minimo = min( n1, n2, n3)
massimo = max (n1, n2, n3)
mezzo = n1 + n2 + n3 - minimo - massimo

print("numero più piccolo", minimo)
print("numero di mezzo", mezzo)
print("numero più grande", massimo)

