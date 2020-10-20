def cap(x):
    a = 0
    b=0 
    c= 0
    d = 0 
    e = 0
    z =''
    for y in x:
     
        if y != ' ' and a == 0:
            y = y.upper()
            
            a = 1
            b = 0
            c = 0
            e = 0
            z = z+y

        elif y == '.' or y == '!' or y == '?':
            a = 0
            e = 1
            z = z + y
        elif y =='i':
            c=1
            z = z+y
        elif y ==' ':
            b = 1
            e = 1
            z = z+y
        elif y == '\'':
            e = 1
        elif b ==1 and c ==1 and e==1:
            ls1 = d-1
            z = z[:ls1]
            z = z+'I'+y
            b = 0
            c = 0
            e = 0

        else:
            z = z+y
            b = 0
            c = 0
            e = 0

    d = d+1
    print(z)


def main():
    string=str(input('Inserire una stringa:'))
    cap(string)

if __name__ == "__main__":
        main()
