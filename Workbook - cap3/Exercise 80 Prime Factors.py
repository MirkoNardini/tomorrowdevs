n = int(input("Inserire un numero intero (2 o superiore): "))

fattore = 2

if n >= 2:
    print("I fattori principali di",n,"sono:")
    while fattore <= n:
        if n% fattore == 0:
            print(fattore)
            n=n / fattore
        else:
            fattore += 1
else:
    print("Il numero inserito è inferiore a 2.")
