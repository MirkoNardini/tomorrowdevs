from Exercise_117_Only_the_Words import split

ins = str(input('inserisci una stringa: '))
ins = ins.lower()
list = split(ins)
t = split(ins)
t.reverse()

a = False

if list == t:
    a = True
else:
    a = False
    print(a, t, list)
