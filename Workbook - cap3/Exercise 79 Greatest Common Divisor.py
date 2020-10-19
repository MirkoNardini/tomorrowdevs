n = int(input("inserisci un numero intero positivo: "))
m = int(input("inserisci un numero intero positivo: "))

d = min(n, m)

while n % d != 0 or m % d != 0:
    d-=1

print("Il più grande divisore comune di", n, "e", m, "è", d)
