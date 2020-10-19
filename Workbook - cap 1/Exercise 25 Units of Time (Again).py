secondi = float(input("Insersci il numero di secondi: "))

giorni = secondi / 86400
secondi = secondi % 86400
ore = secondi / 3600
secondi = secondi % 3600
minuti = secondi / 60
secondi = secondi % 60

print("L'equivalente è","%d:%02d:%02d:%02d." % (giorni, ore, minuti, secondi))
