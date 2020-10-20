def prime(x):
    y = 1
    z = 0
    while y < x:
        if x % y == 0:
            z = z + 1
        else:
            z = z
        y = y + 1

    if z == 1:
        res = True
    else:
        res = False

    return res

def main():
    a = int(input("Inserisci un int:"))
    print(prime(a))

if __name__ == "__main__":
        main()
