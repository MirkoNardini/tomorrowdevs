import math


anno = int(input("inserisci anni: "))

giorno_della_settimana = (anno + math.floor((anno - 1) / 4) - math.floor((anno - 1) / 100) +
math.floor((anno - 1) / 400)) % 7

if giorno_della_settimana ==0:
    giorno = "Domenica"
elif giorno_della_settimana ==1:
    giorno = "Lunedi"
elif giorno_della_settimana ==2:
    giorno = "Martedi"
elif giorno_della_settimana ==3:
    giorno = "Mercoledi"
elif giorno_della_settimana ==4:
    giorno = "Giovedi"
elif giorno_della_settimana ==5:
    giorno = "Venerdi"
elif giorno_della_settimana ==6:
    giorno = "Sabato"

print("%d-01-01 è nel giorno %d: %s" %(anno ,giorno_della_settimana, giorno))
