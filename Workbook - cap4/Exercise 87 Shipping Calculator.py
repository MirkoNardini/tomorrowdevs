def order(n):
    next_rate = 2.95
    first_rate = 10.95
    if n>1:
        cost=first_rate+(n-1)*next_rate
    else:
        cost=first_rate
    return cost

def main():
    num = int(input("Inserire il numero di articoli: "))

print("Le spese di spedizione per",num,"gli ordini è: $",order(num))

main()
