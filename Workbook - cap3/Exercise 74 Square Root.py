x = int(input("Insetisci un numero: "))

guess = x/2
print("Approssimazione:",guess)
error = abs((guess**2)-x)
print("Errore assoluto:",error)

while error>(10**(-12)):
    guess=(guess+(x/guess))/2
    error=abs((guess**2)-x)
    print("Approssimazione:",guess)
    print("Errore assoluto:",error)
