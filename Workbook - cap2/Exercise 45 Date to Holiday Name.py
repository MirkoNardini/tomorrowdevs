mese = (input("Inserisci il numero del mese dell'anno: "))


festa1 = "1 Gennaio"
festa2 = "1 Luglio"
festa3 = "25 Dicembre"

if mese == festa1:
    print("il 1 Gennaio è Capodanno")
elif mese == festa2:
    print("il 1 Luglio è il giorno dell'Indipendenza")
elif mese == festa3:
    print("il 25 Dicembre è Natale")
else:
    print("giorno non corrisponde a un giorno festivo")
            
