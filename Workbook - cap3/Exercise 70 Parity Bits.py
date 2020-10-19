
bit = input("insersici 8 bit: ")

while bit != "":

    if bit.count("0") + bit.count("1") != 8 or len(bit) != 8:
        print("Qualcosa è andato storto, non erano 8 bit")
    else:
        ok = bit.count("1")

    if ok % 2 == 0:
        print("Il bit di parità dovrebbe essere 0.")
    else:
        print("Il bit di parità dovrebbe essere 1.")

    bit = input("inserisci 8 bit: ")
