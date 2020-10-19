Pennies_Per_Nickel = 5
Nickel = 0.05

total = 0.00

line = input("Inserire il prezzo dell'articolo (vuoto per uscire): ")

while line != "":
    total = total + float(line)
    line = input("Inserire il prezzo dell'articolo (vuoto per uscire): ")
    print("L'importo esatto da pagare è %.02f" % total)

rounding_indicator = total * 100 % Pennies_Per_Nickel

if rounding_indicator < Pennies_Per_Nickel / 2:
    cash_total = total - rounding_indicator / 100
else:
    cash_total = total + Nickel - rounding_indicator / 100

print("L'importo da pagare è %.02f" % cash_total)
