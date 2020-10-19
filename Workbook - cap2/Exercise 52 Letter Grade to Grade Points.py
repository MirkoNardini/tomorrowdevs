lettera = input("Inserire un grado in lettera: ")
lettera = lettera.upper()

A = 4.0
A_MENO = 3.7
B_PIU = 3.3
B = 3.0
B_MENO = 2.7
C_PIU = 2.3
C = 2.0
C_MENO = 1.7
D_PIU = 1.3
D = 1.0
F = 0
NON_VALIDO = -1

if lettera == "A+" or lettera == "A":
    Punti = A
elif lettera == "A-":
    Punti = A_MENO
elif lettera == "B+":
    Punti = B_PIU
elif lettera == "B":
    Punti = B
elif lettera == "B-":
    Punti = B_MENO
elif lettera == "C+":
    Punti = C_PIU
elif lettera == "C":
    Punti = C
elif lettera == "C-":
    Punti = C_MENO
elif lettera == "D+":
    Punti = D_PIU
elif lettera == "D":
    Punti = D
elif lettera == "F":
    Punti = F
else:
    Punti = NON_VALIDO

if Punti == NON_VALIDO:
    print("Non è un voto valido per le lettere")
else:
    print("A(n)", lettera, "è uguale a", Punti, "punti di valutazione.")
