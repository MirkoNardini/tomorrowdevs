def magic_date(c,m,y):
    m = m.lower()
    if m == 'gennaio':
        d = 1
    elif m == 'febbraio':
        d = 2
    elif m == 'marzo':
        d = 3
    elif m == 'aprile':
        d = 4
    elif m == 'maggio':
        d = 5
    elif m == 'giugno':
        d = 6
    elif m == 'luglio':
        d = 7
    elif m == 'agosto':
        d = 8
    elif m == 'settembre':
        d = 9
    elif m == 'ottobre':
        d = 10
    elif m == 'novembre':
        d = 11
    elif m == 'dicembre':
        d = 12

    y = str(y)
    y = y[2:4]
    y = int(y)

    md = d * c

    if y == md:
        e = True
    else:
        e = False

    return e

def main():
    y = int(input('Inserire un anno:'))
    m = str(input('Inserire un mese:'))
    d = int(input('Inserire un giorno:'))

    magicday = magic_date(d,m,y)

    if magicday==True:
        print('Cavolo sì, è un appuntamento magico)
    else:
        print('Nessun uomo, riprova')

main()
