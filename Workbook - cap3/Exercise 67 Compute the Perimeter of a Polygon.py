import math
x1 = float(input('Inserire la prima coordinata x:'))
y1 = float(input('Inserire la prima coordinata y:'))
check = str(x1)
p = 0
while check != '' :
    x2s = str(input('Inserire la successiva coordinata x (vuoto per uscire):'))
    if x2s != '':
        x2 = float(x2s)
        y2 = float(input('Inserire la coordinata y successiva :'))
        d = math.sqrt((x2-x1)**2+(y2-y1)**2)
        p = p + d
        x1 = x2
        y1 = y2
        check = x2s
    else:
        check=x2s
print(p)
