
def anagrams(v):
    risultato = {}
    for i in v:
        if i in risultato != "!?,.:":
            if i in risultato:
                risultato[i] += 1
            else:
                risultato[i] = 1
    return risultato


def main():
    s1 = input("Inserire la prima stringa: ").lower().replace(" ", "")
    s2 = input("Inserire la seconda stringa: ").lower().replace(" ", "")

    ris1 = anagrams(v1)
    ris2 = anagrams(v2)
    if ris1 == ris2:
        print("Le stringhe sono anagrammi")
    else:
        print("Le stringhe non sono anagrammi")


main()
