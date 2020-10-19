giorni = float(input("numero di giorni: "))
ore = float(input("numero delle ore: "))
minuti = float(input("numero dei minuti: "))
secondi = float(input("numero dei secondi: "))

tot_giorni = giorni * 86400
tot_ore = ore / 3600
tot_minuti = minuti * 60

tot_secondi = tot_giorni + tot_ore + tot_minuti + secondi
round(tot_secondi)

print("il totale di secondi è: ", tot_secondi)
