month = input("inserisci mese del tuo compleanno: ")
day = int(input("inserisci la da del tuo compleanno: "))


if (month == "Dicembre" and day >= 22) or (month == "Gennaio" and day <= 19):
    segno = "Capricorno"
elif (month == "Gennaio" and day >= 20) or (month == "Febraio" and day <= 18):
    segno = "Acquario"
elif (month == "Febraio" and day >= 19) or (month == "Marzo" and day <= 20):
    segno = "Pesci"
elif (month == "Marzo" and day >= 21) or (month == "Aprile" and day <= 19):
    segno = "Ariete"
elif (month == "Ariete" and day >= 20) or (month == "Maggio" and day <= 20):
    segno = "Toro"
elif (month == "Maggio" and day >= 21) or (month == "Giugno" and day <= 20):
    segno = "Gemelli"
elif (month == "Giugno" and day >= 21) or (month == "Luglio" and day <= 22):
    segno = "Cancro"
elif (month == "Luglio" and day >= 23) or (month == "Agosto" and day <= 22):
    segno = "Leone"
elif (month == "Agosto" and day >= 23) or (month == "Settembre" and day <= 22):
    segno = "Vergine"
elif (month == "Settembre" and day >= 23) or (month == "Ottobre" and day <= 21):
    segno = "Bilancia"
elif (month == "Ottobre" and day >= 22) or (month == "Novembre" and day <= 21):
    segno = "Scorpione"
elif (month == "Novembre" and day >= 22) or (month == "Dicembre" and day <= 21):
    segno = "Saggitario"

print("Il tuo segno è: ", segno)
    


