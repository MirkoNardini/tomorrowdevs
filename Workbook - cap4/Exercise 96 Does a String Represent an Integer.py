def isInteger(x):
    z = ''
    counter=0
    for a in x:
        if a==' ':
            a=a
        else:
            z=z+a

    if len(z) > 0:
        if z[0] == '+' or z[0] == '-':
            counter = counter+1
            check = 1
        elif z[0] == '1' or z[0] == '2' or z[0] == '3' or z[0] == '4' or z[0] == '5' or z[
            0] == '6' or z[0] == '7' or z[0] == '8' or z[0] == '9' or z[0] == '0':
            check = 1

    if check ==1:
        for b in z:
            if b == '1' or b == '2' or b == '3' or b == '4' or b == '5' or b == '6' or b == '7' or b == '8' or b == '9' or b == '0':
                counter = counter + 1
            else:
                counter = counter

    print(counter)
    if counter == len(z):
        result= True
    else:
        result= False

    return result

def main():
    a = str(input("Inserisci una stringa, scopriremo se si tratta di una cifra o meno:"))
    print(isInteger(a))


if __name__ == "__main__":
        main()
