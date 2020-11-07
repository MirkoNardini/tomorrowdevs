def numbersRom(t):
    dict = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    res = 0
    if t == '':
        return t
    else:
        if t[0] in dict and len(t)>1:
            if dict[t[0]] >= dict[t[1]]:
                ris = dict[t[0]] + numbersRom(t[1:])
            elif dict[t[0]] < dict[t[1]]:
                ris = numbersRom(t[1:]) - dict[t[0]]
        else:
            ris = ris + dict[t[0]]

        return ris



def main():
    t = str(input('Inserisci numero romano:'))
    print(numbersRom(t))
main()
