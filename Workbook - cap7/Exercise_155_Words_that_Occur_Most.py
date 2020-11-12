from Exercise_117_Only_the_Words import split
enter = input("Inserire il nome del file: ")
enter = 'C:\\Users\\Mirco\\Desktop\\es python\\Files\\' + enter
ins = {}

try:
    t = open(enter, "r")
    line = t.readline()
    v = line.split()
    a = 0
    while a <= len(line) + 1 and line != "":
        line = t.readline()
        v = line.split()
        for i in v:
            i = i.lower()
            if i not in ins:
                ins[i] = 1
            else:
                ins[i] = ins[i]+1

        a += 1
    print(ins)
except FileNotFoundError:
    print("Non è stato possibile aprire il file. Uscire...")
    quit()
