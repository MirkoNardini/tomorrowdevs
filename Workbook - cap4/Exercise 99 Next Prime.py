from ex98 import prime

def nextPrime(x):
    a = False
    if x>0:
        while a == False:
            x = x + 1
            a = prime(x)

    return x

def main():
    n = int(input('Inserisci un int'))
    print(nextPrime(n))

if __name__ == "__main__":
        main()
