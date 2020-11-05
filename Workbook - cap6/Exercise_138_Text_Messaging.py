#Creo un dizionario contenente tutti i valori

k = {
    "1": ["", ".", ",", "?", "!", ":"],
    "2": ["", "A", "B", "C"],
    "3": ["", "D", "E", "F"],
    "4": ["", "G", "H", "I"],
    "5": ["", "J", "K", "L"],
    "6": ["", "M", "N", "O"],
    "7": ["", "P", "Q", "R", "S"],
    "8": ["", "T", "U", "V"],
    "9": ["", "W", "X", "Y", "Z"],
    "0": ["", " "]
    }

r = input("Inserisci un frase e ti diro a quali tasti corrisponde sul Nokia 3310: ").upper()
risultato = ""
for i in r:
    for key, value in k.items():
        if i in value:
            for v in range(value.index(i)):
                risultato += key

print("risultato: {}".format(risultato))
