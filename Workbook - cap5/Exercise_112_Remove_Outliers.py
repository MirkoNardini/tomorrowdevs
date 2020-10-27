def cleanData(na,x):

    if len(na) < 4:
        res = ('Devi inserire più elementi nella tua lista')

    na.sort()
    for a in range(x):
        na.pop(0)
        na.pop(len(na) - 1)

    return na

def main():
    list =[]
    orlist=[]
    while 0<1:
       a = int(input('Inserire un numero intero positivo: '))
       if a == 0:
           break
       list.append(a)

    for i in list:
        orlist.append(i)

    n = int(input('Inserire il valore di pulizia:'))
    print(cleanData(list,n),end = " ")
    print(orlist, end = " ")


main()
