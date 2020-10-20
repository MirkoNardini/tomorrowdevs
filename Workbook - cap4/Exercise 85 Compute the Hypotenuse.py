import math

def triangle(l1,l2):
    h=math.sqrt(l1**2+l2**2)
    return h

def main():
    q1 = float(input("Inserire la prima lunghezza: "))
    q2 = float(input("Inserire la seconda lunghezza: "))

print("Un triangolo con le lunghezze dei due lati più corti: ",q1 ,\
    "e",q2,"ha l'ipotenusa: %.2f" %(triangle(q1,q2)))

