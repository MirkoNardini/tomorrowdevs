name1 = input("Inserire il nome del file: ")
name2 = input('Inserire un nome per il nuovo file:')
name1 = 'C:\\Users\\Mirco\\Desktop\\es python\\Files\\' + name1
name2 = 'C:\\Users\\Mirco\\Desktop\\es python\\Files\\' + name2

try:
    t = open(name1, "r")
    line = t.readline()
    count = 0
    TFile_res = open(name2, 'a')
    while count <= len(line)+1 and line != "":
        count = count + 1
        line = line.rstrip()
        line = str(count) + ': ' + line + ' ' + '\n'
        TFile_res.write(line)
        line = t.readline()
    inf.close()

except FileNotFoundError:
    print("Non è stato possibile aprire il file. Uscire...")
    quit()
