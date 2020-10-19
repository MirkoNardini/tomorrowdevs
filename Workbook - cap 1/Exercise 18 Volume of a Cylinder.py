import math

raggio = float(input("inserisci il raggio: "))
altezza = float(input("inserisci l'altezza: "))

area = raggio * raggio * math.pi
volume = area *  altezza
round(volume)

print("il volume del cilindro è: ", volume) 
