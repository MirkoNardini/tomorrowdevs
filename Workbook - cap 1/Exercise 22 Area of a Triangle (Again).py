s1 = float(input("primo lato del trinaglo con lunghezza: "))
s2 = float(input("secondo lato del trinaglo con lunghezza: "))
s3 = float(input("terzo lato del trinaglo con lunghezza: "))

s = (s1 + s2 + s3)/2
area = s*(s-s1)*(s-s2)*(s-s3)
print("l'area del tringolo è: ", area)
