iva = 0.22
mancia = 0.18

costo = float(input("Costo del pasto: "))

Iva = costo * iva
Mancia = costo * mancia
totale = costo + Iva + Mancia

print("La tassa è di %.2f e la mancia è di %.2f, e il totale %.2f" % (Iva, Mancia, totale))
