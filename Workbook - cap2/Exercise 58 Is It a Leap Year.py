anni = int(input("inserisci un anno: "))

if anni % 400 == 0:
    anno_biestile = True
elif anni % 100 == 0:
    anno_bisestile = False
elif anni % 4 == 0:
    anno_bisestile = True
else:
    anno_bisestile = False


if anno_bisestile:
    print(anni, "è un anno bisestile.")
else:
    print(anni, "non è un anno bisestile.")
