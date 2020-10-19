bread_Old = int(input("pane del giorno prima aquistato:"))

BREAD = 3.49
SCONTO = 0.60

prezzo = bread_Old * BREAD
sconto = prezzo * SCONTO
totale = prezzo - sconto


print("Old bread: %5.2f" % bread_Old)
print("bread: %5.2f" % BREAD)
print("Sconto: %5.2f" % SCONTO)
print("tot: %5.2f" % totale )





