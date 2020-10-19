numero = int(input("Enter a number: "))

print(numero)

while numero != 1:
    if numero %2 == 0:
        numero = numero /2
    else:
        numero =(numero * 3)+1
    print(numero)
