from re import split


def sequenza(inizio, parola):
    if inizio == "":
        return []
        seq = []
    lettere = inizio[len(inizio) - 1].lower()
    for i in range(0, len(parola)):
        p_lettere = parola[i][0].lower()
        if p_lettere == lettere:
            t = sequenza(parola[i], parola[0: i] + parola[i + 1: len(parola)])
            if len(t) > len(seq):
                    seq = t
    return [inizio] + seq


def nome_elemento():
    elemento = open("elements.txt")
    nome = []
    for line in elemento:
        line = line.replace("\n", "")
        line = split(",", line)
        names.append(line[2])
    elemento.close()
    return nome


def main():
    nome = nome_elemento()
    inizio = input("Inserire il nome di un elemento: ").capitalize()
    print("-" * 50)
    if inizio not in nome:
        print("Non era un nome di elemento valido")
    else:
        nome.remove(inizio)
        seq = sequenza(inizio, nome)
        print("La sequenza più lunga che inizia con {} è:".format(inizio))
        for elemento in seq:
            print(" ", elemento)
        print("-" * 50)
        print("La lunghezza della sequenza è: {}".format(len(seq)))


main()
