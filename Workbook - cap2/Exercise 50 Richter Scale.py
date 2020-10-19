import math

a = float(input("insersci valore A:" ))
b = float(input("insersci valore B:" ))
c = float(input("insersci valore C:" ))

disco = (b**2)-4 *a*c
if disco < 0:
    print("non ci sono vere radici")
elif disc == 0:
    radici = (-b+math.sqrt((b**2)-4*a*c))/2*a
    print("ci sono vere e proprie radici: ", radici)
elif disc > 0:
    radici = (-b+math.sqrt((b**2)-4*a*c))/2*a
    radici2 = (-b-math.sqrt((b**2)-4*a*c))/2*a
    print("ci sono due vere radici: ", radici, radici2)
    
    
