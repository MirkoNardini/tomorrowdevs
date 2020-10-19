r = 8.324

t = float(input("inserisci il valore della temperatura in kevlvin: "))
v = float(input("inserisci il valore del volume in litri: "))
p = float(input("inserisci il valore della pressione in pascals: "))

n = (p*v)/(r*t)

print("numero di moli del ga equivale a", n)
