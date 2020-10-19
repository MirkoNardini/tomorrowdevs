lato1 = float(input("Inserire la lunghezza del lato 1: "))
lato2 = float(input("Inserire la lunghezza del lato 2: "))
lato3 = float(input("Inserire la lunghezza del lato 3: "))

if lato1 == lato2 and lato2 == lato3:
    tri_type = "equilatero"
elif lato1 == lato2 or lato2 == lato3 or lato3 == lato1:
    tri_type = "isoscele"
else:
    tri_type = "scaleno"

print("è un triangolo ", tri_type)
