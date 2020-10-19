n = int(input("Inserire un numero intero non negativo: "))

nuova_base = 2
risultato = ""

r = n % nuova_base
risultato = str(r) + risultato
n = n // nuova_base

while n > 0:
    r = n % nuova_base
    risultato = str(r) + risultato
    n = n // nuova_base

print(n, "in decimale è", risultato, "in binario.")
