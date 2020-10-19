import math

a = float(input("inserisci a: "))
b = float(input("inserisci b: "))
c = float(input("inserisci c: "))

dis = b**2-4*a*c

if dis < 0:
    print("il discriminante è negativo, quindi l'equazione quadratica non ha radici")
elif dis == 0:
    radici = (-b)/(2*a)
    print("la discriminante è 0 quindi l'equazione ha una radice: %.2f" %radice)
else:
    sqr = math.sqrt(dis)
    radice1 = (-b+sqr)/(2*a)
    radice2 = (-b-sqr)/(2*a)
    print("L'equazione ha due radici: %.2d e %.2f" %(radice1, radice2))
