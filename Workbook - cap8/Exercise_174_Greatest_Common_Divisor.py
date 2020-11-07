def Euclide(a,b):
    if b == 0:
        return a
    else:
        c = a % b
        return Euclide(b,c)

def main():
    print(Euclide(2570,8394720))

main()
