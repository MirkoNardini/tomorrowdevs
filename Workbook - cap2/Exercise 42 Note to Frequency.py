nome = input("Inserire il nome della nota a due caratteri: ")

C4_FREQ = 261.63
D4_FREQ = 293.66
E4_FREQ = 329.63
F4_FREQ = 349.23
G4_FREQ = 392.00
A4_FREQ = 440.00
B4_FREQ = 493.88

note = nome[0]
ottave = int(nome[1])

if note == "C":
frequenza = C4_FREQ
elif note == "D":
frequenza = D4_FREQ
elif note == "E":
frequenza = E4_FREQ
elif note == "F":
frequenza = F4_FREQ
elif note == "G":
frequenza = G4_FREQ
elif note == "A":
frequenza = A4_FREQ
elif note == "B":
frequenza = B4_FREQ

frequenza = frequenza / 2 ** (4 - ottave)

print("La frequenza di", nome, "è", frequenza)
