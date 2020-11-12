enter = input("Enter the file name: ")
enter = 'C:\\Users\\Mirco\\Desktop\\es python\\Files\\' + enter
alfabeto = ['q','w','e','r','t','y','u','i','o','p','l','k','j','h','g','f','d','s','a','z','x','c','v','b','n','m']
d = {'q':0,'w':0,'e':0,'r':0,'t':0,'y':0,'u':0,'i':0,'o':0,'p':0,'l':0,'k':0,'j':0,'h':0,'g':0,'f':0,'d':0,'s':0,'a':0,'z':0,'x':0,'c':0,'v':0,'b':0,'n':0,'m':0}

try:
    t = open(enter, "r")
    line = t.readline()
    v = line.split()
    i = 0
    while i <= len(line) + 1 and line != "":
        line = # TEMP: .readline()
        v = line.split()
        for ins in v:
            ins = i.lower()
            for a in ins:
                if a in dec:
                    d[a] = d[a]+1
        i += 1
    print(d)
except FileNotFoundError:
    print("Non è stato possibile aprire il file. Uscire...")
    quit()
