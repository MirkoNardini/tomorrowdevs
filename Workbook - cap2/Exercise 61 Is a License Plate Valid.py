targa = input("Inserire la targa: ")

if len(targa) == 6 and \
    targa[0] >= "A" and targa[0] <= "Z" and \
    targa[1] >= "A" and targa[1] <= "Z" and \
    targa[2] >= "A" and targa[2] <= "Z" and \
    targa[3] >= "0" and targa[3] <= "9" and \
    targa[4] >= "0" and targa[4] <= "9" and \
    targa[5] >= "0" and targa[5] <= "9":
    print("La targa è una valida targa di stile più vecchio.")
elif len(targa) == 7 and \
    targa[0] >= "0" and targa[0] <= "9" and \
    targa[1] >= "0" and targa[1] <= "9" and \
    targa[2] >= "0" and targa[2] <= "9" and \
    targa[3] >= "0" and targa[3] <= "9" and \
    targa[4] >= "A" and targa[4] <= "Z" and \
    targa[5] >= "A" and targa[5] <= "Z" and \
    targa[6] >= "A" and targa[6] <= "Z":
    print("La targa è una targa valida più recente.")
else:
    print("La targa non è valida.")
