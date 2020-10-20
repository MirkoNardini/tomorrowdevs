from ex100 import randomPass
from ex102 import goodpass

def main():
    b = False
    a = ''
    x = 0
    while b == False:
        a = randomPass()
        b = goodpass(a)
        x = x+1
        print(a,b)

    print('Trova un buon pass ha preso',x,'tentativi')

if __name__ == "__main__":
        main()
