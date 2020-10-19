banconota = int(input("Inserire taglio banconota: "))

George_Washington = 1
Thomas_Jefferson = 2
Abraham_Lincoln = 5
Alexander_Hamilton = 10
Andrew_Jackson = 20
Ulysses_S_Grant = 50
Benjamin_Franklin = 100

if banconota == George_Washington:
    print("La banconota è da 1$ e raffigura George Washington")
elif banconota == Thomas_Jefferson:
    print("La banconota è da 2$ e raffigura Thomas Jefferson")
elif banconota == Abraham_Lincoln:
    print("La banconota è da 5$ e raffigura Abraham Lincoln")
elif banconota == Alexander_Hamilton:
    print("La banconota è da 10$ e raffigura Alexander Hamilton")
elif banconota == Andrew_Jackson:
    print("La banconota è da 20$ e raffigura Andrew Jackson")
elif banconota == Ulysses_S_Grant:
    print("La banconota è da 50$ e raffigura Ulysses S. Grant")
elif banconota == Benjamin_Franklin:
    print("La banconota è da 100$ e raffigura Benjamin Franklin")
else:
    print("BANCONOTANON RICONOSCIUTA")
