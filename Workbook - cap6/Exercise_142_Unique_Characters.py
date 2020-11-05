enter = input("Inserisci stringa: ")

caratteri = {}

for i in enter:
    caratteri[i] = 0
print("La stringa contiene", len(caratteri), "caratteri unici")
