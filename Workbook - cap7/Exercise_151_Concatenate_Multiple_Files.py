import sys

if len(sys.argv) < 2:
    print("Fornire altri nomi di file come argomenti da riga di comando.")
    quit()
try:
    for i in range(len(sys.argv)):
        if i > 0:
            t = open(sys.argv[i], "r")
            line = t.readlines()
            print(line)
            t.close()

except IOError:
    print("Si è verificato un errore durante l'accesso al file.")
