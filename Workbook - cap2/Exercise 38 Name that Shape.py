lati = int(input("Inserisci il numero di lati: "))

name = ""
if lati == 3:
  name = "triangolo"
elif lati == 4:
  name = "quadrilatero"
elif lati == 5:
  name = "pentagono"
elif lati == 6:
  name = "esagono"
elif lati == 7:
  name = "ettagono"
elif lati == 8:
  name = "ottagono"
elif lati == 9:
  name = "ennagono"
elif lati == 10:
  name = "decagono"

if name == "":
  print("Il numero dei lati non è supportato dal programma.")
else:
  print("la forma è", name)
