numero = float(input("inserisci un volto numerico: "))

A_PIU = 4.5
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

if numero == A_PIU:
     Punti = "A+"
elif numero == A:
     Punti = "A"
elif numero == A_MENO:
    Punti = "A-"
elif numero == B_PIU:
    Punti = "B+"
elif numero == B:
    Punti = "B"
elif numero == B_MENO:
    Punti = "B-"
elif numero == C_PIU:
    Punti = "C+"
elif numero == C:
    Punti = "C"
elif numero == C_MENO:
    Punti = "C-"
elif numero == D:
    Punti = "D+"
elif numero == D:
    Punti = "D"
elif numero == F:
    Punti = "F"
else:
    Punti = NON_VALIDO

if Punti == NON_VALIDO:
    print("Non è un voto valido in numeri")
else:
    print("A(n)", numero, "è uguale a", Punti, "punti di valutazione.")
