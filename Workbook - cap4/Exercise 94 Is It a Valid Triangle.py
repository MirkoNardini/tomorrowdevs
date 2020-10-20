def triangle(a,b,c):
    if a>= b+c:
        d = False
    elif b>= a+c:
        d = False
    elif c>= b+a:
        d = False
    else:
        d = True

    return d

def main():

    l1=int(input('Inserire il primo lato del triangolo:'))
    l2=int(input('Inserire il secondo lato del triangolo:'))
    l3=int(input('Inserire il terzo lato del triangolo:'))

    print(triangle(l1,l2,l3))

if __name__ == "__main__":
        main()
