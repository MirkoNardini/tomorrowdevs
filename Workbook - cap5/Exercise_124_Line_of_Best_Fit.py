x = str(input("Inserire la coordinata x del primo punto: \n"))
y = str(input("Inserire la coordinata y del primo punto:\n"))
points = []
points.append(x)
points.append(y)
z = 0
m1 = 0 #sommatorio di x*y
mx2 = 0 #sommatorio di x
my2 = 0 #sommatorio di y
m2 = 0  # prodotto di sommatoria x e sommatoria y diviso per 0
m3 = 0 #sommatorio di x**2
m4 = 0 # ((sommatorio di x)**2)/n
sy = 0 # sommatorio di y
sx = 0 # sommatorio di x
yv = 0 # valore medio y
xv = 0 # valore medio x

while points[z]!='':
    x = str(input('Inserire la coordinata x di un altro punto:\n'))
    if x == '':
        break
    y = str(input('Inserire la coordinata y di un altro punto:\n'))
    points.append(x)
    points.append(y)
    z = z+2

z = 0
while len(points)>z:
    points[z]=float(points[z])
    z = z+1

z = 0
while len(points) > z:
    a = points[z]*points[z+1]
    m1 = m1 + a
    z = z+2

z = 0

while len(points) > z:
    mx2 = mx2 + points[z]
    my2 = my2 +points[z+1]
    z = z+2

m2 = (mx2*my2)/(len(points)/2)
z = 0
while len(points) > z:
    m3 = m3 + points[z]**2
    z = z+2

m4 = ((mx2)**2)/(len(points)/2)

m = (m1 - m2)/(m3-m4)

z = 0
while len(points)>z:
    sx = sx + points[z]
    sy = sy + points[z+1]
    z = z+2

xv = sx/(len(points)/2)
yv = sy/(len(points)/2)

b = sy - m*sx

print( 'Con i vostri dati y=',m,'* x +',b)
