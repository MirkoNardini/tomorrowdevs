enter = input("Inserire un numero: ")
ris = 0

while enter != "":
    try:
        t = float(enter)
        ris = ris + t
        print("somma:", ris)

    except ValueError:
        print("non è un numero")
        enter = input("riprova: ")
        t = float(enter)
        ris = ris + t
        print("somma:", ris)
    enter = input('Inserire il numero successivo:')

print('La somma finale è:', ris)
