def ordinalDate(d,m,y):
    if y % 400 == 0:
        bis = 1
    elif y % 100 == 0:
        bis = 0
    elif y % 4 == 0:
        bis = 1
    else:
        bis = 0


    if bis == 1:
        months = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        months=[31,28,31,30,31,30,31,31,30,31,30,31]
    x = 1
    days = 0
    days_before=0
    if 2 <= m <= 12 and d<=months[m-1]:
        while x < m:
            days_before= months[m-2] + days_before
            m = m-1
        days = days_before+d
    elif m==1 and d<=31:
        days=d
    else:
        print('La data inserita non è corretta')

    return days

def main():
    datey = int(input('Inserisci anno:'))
    datem = int(input('Inserisci mese:'))
    dated = int(input('Inserisci giorno:'))

    print(datey,ordinalDate(dated, datem, datey))

if __name__ == "__main__":
        main()
