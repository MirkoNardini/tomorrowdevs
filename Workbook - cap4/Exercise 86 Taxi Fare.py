def distance(d):
    base_fare = 4.00
    every_140 = 0.25
    if d<140:
        cost=d*base_fare
    else:
        q=d//140
        cost=d*base_fare+q*every_140
    return cost

def main():
    dis = int(input("Inserire la distanza in Km: "))

print("La",dis,"Km da percorrere è: $",distance(dis))

main()
