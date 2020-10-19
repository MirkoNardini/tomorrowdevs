quarter = 25
toonie = 200
dime = 10
nickel = 5
loonie = 100

cents = int(input("Inserire il numero di centesimi: "))


print(" ", cents // quarter, "quarters")
cents = cents % quarter
print(" ", cents // toonie, "toonies")
cents = cents % toonie
print(" ", cents // dime, "dimes")
cents = cents % dime
print(" ", cents // nickel, "nickels")
cents = cents % nickel
print(" ", cents // loonie, "loonies")
cents = cents % loonie

print(" ", cents, "pennies")
