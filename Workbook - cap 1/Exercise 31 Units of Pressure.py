pressione = float(input("inserisci pressione (kilopascal): "))

libbre =  6.895
millimetri = 7.501
atmosfere = 101

equi_libbre = pressione / libbre
equi_millimetri = pressione / millimetri
equi_atmosfera = pressione / atmosfere

print("Equivalente in libre: ", equi_libbre)
print("Equivalente in millimetri di mercurio: ", equi_millimetri)
print("Equivalente in atmosfere: ", equi_atmosfera)



