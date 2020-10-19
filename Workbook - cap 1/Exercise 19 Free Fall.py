from math import sqrt

gravità= 9.8
altezza = float(input("Altezza: "))
vf = sqrt(2 *gravità * altezza)
print("colpirà il terreno a %.2f m/s." % vf)
