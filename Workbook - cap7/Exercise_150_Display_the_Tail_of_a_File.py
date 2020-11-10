import sys

if len(sys.argv) != 2:
    print("Fornire il nome del file come argomento della riga di comando.")
    quit()
try:
    t = open(sys.argv[1], "r")
    line = t.readlines()
    a = len(line)
    b = len(line)-10
    if b >= 1:
        v = 0
        while v < b:
            line.pop(0)
            v = v+1
    print(line)
    t.close()

except IOError:
    print("Si è verificato un errore durante l'accesso al file.")
