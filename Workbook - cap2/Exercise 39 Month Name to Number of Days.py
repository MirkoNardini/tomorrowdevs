mese = input("inserisci il nome di un mese: ")

giorni = 31

if mese == "Aprile" or mese == "Giugno" or \
   mese == "Settembre" or mese == "Novembre":
    girorni = 30

elif mese == "Febraio":
    giorni = "28 o 29"

print(mese, "ha", giorni ,"giorni")
