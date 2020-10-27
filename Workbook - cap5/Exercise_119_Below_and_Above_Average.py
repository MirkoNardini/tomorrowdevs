t = []
giu = []
su = []
uguale = []
count = 0

num = input("Immettere i numeri fino a una linea nera: ")

while num!="":
    n = int(num)
    t +=[n]
    count +=1
    num = input("Immettere i numeri fino a una linea nera: ")

m =sum(t)/count

for n in t:
    if n<m:
        giu.append(n)
    elif n==m:
        uguale.append(n)
    else:
       su.append(n)

print("I valori medi sono:", m)

print("Tutti i valori sotto la media:", end="")
print(giu)
print("Tutti i valori medi:", end="")
print(uguale)
print("Tutti i valori sopra la media:", end="")
print(su)
