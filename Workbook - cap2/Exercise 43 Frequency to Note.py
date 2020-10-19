frequenza = float(input("Inserire una frequenza (Hz): "))

C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88
limite = 1

if frequenza >= C4 - limite and frequenza <= C4 + limite:
    nota = "C4"
elif frequenza >= D4 - limite and frequenza <= D4 + limite:
    nota = "D4"
elif frequenza >= E4 - limite and frequenza <= E4 + limite:
    nota = "E4"
elif frequenza >= F4 - limite and frequenza <= F4 + limite:
    nota = "F4
elif frequenza >= G4 - limite and frequenza <= G4 + limite:
    nota = "G4"
elif frequenza >= A4 - limite and frequenza <= A4 + limite:
    nota = "A4"
elif frequenza >= B4 - limite and frequenza <= B4 + limite:
    nota = "B4"
else:
    nota = ""

if nota == "":
print("Non c'è nessuna nota che corrisponda a quella frequenza.")
else:
print("Quella frequenza è", nota)
