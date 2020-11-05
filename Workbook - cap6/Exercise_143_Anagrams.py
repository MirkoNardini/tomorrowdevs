#definisco funzione anagrammi

def anagrammi(t):
    risultato = {}
    for i in t:
        if i in risultato:
            risultato[i] += 1
        else:
            risultato[i] = 1
    return risultato


def main():
    t1 = input("Inserire la prima stringa: ")
    t2 = input("Inserire la seconda stringa: ")

    cont1 = anagrams(t1)
    cont2 = anagrams(t2)
    if cont1 == cont2:
        print("Le stringhe sono anagrammi")
    else:
        print("Ops, Le stringhe non sono anagrammi")


main()
