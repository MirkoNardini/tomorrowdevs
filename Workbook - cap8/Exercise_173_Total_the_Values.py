def ricursione():
    cont = 0
    valore = str(input('Inserire un intero:'))
    if valore != '':
        valore = int(valore)
        cont = valore + ricursione()
        print(cont)
    else:
        return cont

    return cont
def main():

    print(ricursione())


main()
