anni_Uomo = float(input("inserisci gli anni umani: "))

anni2 = 10.5

if anni_Uomo <= 2 and anni_Uomo >= 0:
    anni_Canini = anni_Uomo * anni2

    print("L'età di un cane è:", anni_Canini)

elif anni_Uomo > 2:
    anni_Canini = 2 * anni2 + ((anni_Uomo - 2)* 4)

    print("L'eta di un cane è:", anni_Canini)
else:
    print("ERRORE: NUMERO NEGATIVO")
