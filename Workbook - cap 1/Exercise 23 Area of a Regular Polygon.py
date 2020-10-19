from math import tan, pi

s = float(input("Lunghezza di un lato: "))
n = float(input("Numero di lati: "))

area = (n * s ** 2) / (4 * tan (pi/n))

print("l'area del poligono è: ", area)
