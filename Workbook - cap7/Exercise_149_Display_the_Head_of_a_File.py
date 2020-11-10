import sys

if len(sys.argv) != 2:
    print("Fornire il nome del file come argomento della riga di comando.")
    quit()
try:
    t = open(sys.argv[1], "r")
    line = t.readline()
    count = 0
    while count < 10 and line != "":
        line = line.rstrip()
        count = count + 1
        print(line)
        line = t.readline()
    t.close()

except IOError:
    print("Si è verificato un errore durante l'accesso al file.")
