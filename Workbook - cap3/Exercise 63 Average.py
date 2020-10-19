numero = int(input("inserisci un numero: "))
sm = 0.00
count = 0

if numero == 0:
    print("Messaggio di errore: il primo numero non può essere 0")
else:
    while numero != 0:
        count = count+1
        sm = sm + numero 
        numero = int(input("inserisci un numero: "))

media = sm/count

print("La media è :", media)
