try:
    t = open('C:\\Users\\Mirco\\Desktop\\es python\\Files\\TestFile.txt', "r")
    v = t.read()
    spli = v.split()
    print(spli)
    Long_Word = 0
    Word = 0
    for i in spl:
        if len(i) > Long_Word:
            Long_Word = len(i)
            ins = i
        elif len(i) == Long_Word:
            Word += 1
        elif len(i) < Long_Word:
            pass
    print('La parola più lunga è', ins,'con', Long_Word,' caratteri. \n Ci sono anche altri', Word,'con questa lunghezza.')

except FileNotFoundError:
    print("Non è stato possibile aprire il file. Uscire...")
    quit()
