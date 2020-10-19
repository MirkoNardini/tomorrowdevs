month = input("inserisci il nome di un mese: ")
day = int(input("inserisci il nome di un giorno: "))

primavera =  "20 marzo"
estate = "21 giugno"
autunno = "22 settembre"
inverno = "21 dicembre"

if month == "Giugno" or month == "Febraio":
    stagione = "inverno"
elif month == "Marzo":
    if day < 20:
        stagione = "Inverno"
    else:
        stagione = "Primavera"
elif month == "Aprile" or month == "Maggio":
        stagione = "Primavera"
elif month == "Giugno":
    if day < 21:
        stagione = "Primavera"
    else:
        stagione = "Estate"
elif month == "Luglio" or month == "Agosto":
        stagione = "Estate"
elif month == "Settembre":
    if day < 22:
        stagione = "Estate"
    else:
        stagione = "Autunno"
elif month == "Ottobre" or month == "Novembre":
        stagione = "Autunno"
elif month == "Dicembre":
    if day < 21:
        stagione = "Autunno"
    else:
        stagione = "Inverno"

print(day, month, "è in ", stagione)
    
    
        
