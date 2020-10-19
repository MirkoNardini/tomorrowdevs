numero_b = input("Inserire un numero binario: ")

lunghezza = len(numero_b)-1
contatore = 0
i=0

while lunghezza>=0:
    contatore = contatore + int(numero_b[lunghezza])*(2**i)
    lunghezza -= 1
    i += 1

num_b = contatore

print(numero_b ,"corrisponde a ", numero_b)
