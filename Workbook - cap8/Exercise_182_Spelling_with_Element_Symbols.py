from re import split


def elemDaControllare(parola, t, i=0, risultato=""):
    if parola[i].capitalize() in t:
        risultato += parola[i].capitalize()
        i += 1

        if i == len(parola):
            return risultato
        else:
            return elemDaControllare(parola, t, i, risultato)

    if i < len(parola) - 1:
        if parola[i].capitalize() + parola[i + 1] in t:
            risultato += parola[i].capitalize() + parola[i + 1]
            i += 2

            if i == len(parola):
                return risultato
            else:
                return elemDaControllare(parola, t, i, risultato)
    else:
        return False


element = open("elements.txt")
s = []
e = []


def main():
    for line in elements:
        line = line.replace("\n", "")
        line = split(",", line)

        s.append(line[1])
        e.append(line[2])

    enter = input("Inserire una parola da scrivere utilizzando solo i simboli degli elementi: ")
    print()
    if check_element(enter, s):
        print("{} può essere scritto come: ".format(enter), check_element(enter, s))
    else:
        print("La tua parola non può essere scritta usando solo i simboli degli elementi")

    print("-" * 70)
    print("I nomi degli elementi che possono essere scritti usando solo i simboli degli elementi sono:")
    print()
    for v in range(len(e)):
        if check_element(e[v], s):
            print("{} can be spelled as: ".format(e[v]), check_element(e[v], s))
            print()


main()
