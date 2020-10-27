def split(i):
    p = 5
    list = []
    cont = 0  
    cont2 = 0 

    for a in i:
        if 'a' < a < 'z' or 'A' < a < 'Z' :
            p = 0

        elif a == ' ' or a == ',' or a == '?' or a == '-' or a == '_' or a == '\'' or a == '!' or a == '.' or a == ':':
            p = 1
            cont2 = cont - cont2
            
            if a == '\'':
                c = cont + 1
                b = i[d:c]
                if b != ' ':
                    p = 0
        
        if p == 1:
            parola = i[cont2:cont]
            d2 = len(parola)
            list.append(parola)
            cont2 = cont - cont2 - cont - 1
            p = 0

        cont += 1
        cont2 += 1

        if len(i) == cont:
            cont2 = cont - cont2
            parola = i[cont2:cont]
            list.append(parola)

            p = 0

    for i in list:
        if i == '':
            list.remove(i)

    return list


def main():
    string = str(input('Inserisci una stringa:'))
    print(split(string))

if __name__ == "__main__":
    main()
