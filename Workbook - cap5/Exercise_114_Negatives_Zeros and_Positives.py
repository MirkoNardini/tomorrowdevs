def divisore(numeri):
    div = []
    for i in range(numeri):
        if numeri % (i + 1) == 0:
            div.append(i + 1)
            
    div.remove(numeri)
    return div

def main():
    ins = int(input('inserisci numero positivo:'))
    print(divisor(ins))

if __name__ == "__main__":
    main()
