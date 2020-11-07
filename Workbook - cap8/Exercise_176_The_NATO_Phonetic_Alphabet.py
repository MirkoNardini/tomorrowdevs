def spelling(t):
    dict = {'a':'Alpha', 'b':'Bravo', 'c':'Charlie', 'd':'Delta', 'e':'Echo', 'f':'Foxtrot', 'g':'Golf', 'h':'Hotel', 'i':'India', 'j':'Juliet', 'k':'Kilo', 'l':'Lima', 'm':'Mike', 'n':'November','o':'Oscar', 'p':'Papa', 'q':'Quebec', 'r':'Romeo', 's':'Sierra', 't':'Tango', 'u':'Uniform', 'v':'Victor', 'w':'Whiskey', 'x':'Xray', 'y':'Yankee', 'z':'Zulu'}
    if len(t) == 0:
        return t
    else:
        if t[0] in dict:
            ris = dict[t[0]] + ' ' + spell(t[1:])
            return ris

def main():
    t = str(input('Inserisci messaggio: '))
    print(spell(t))

main()
