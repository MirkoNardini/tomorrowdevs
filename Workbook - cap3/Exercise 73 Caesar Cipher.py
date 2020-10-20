m = str(input('Inserisci il tuo messaggio:'))
s = int(input('Inserire il valore di spostamento:'))
nm = str('') 
if s>26 or s<-26: 
    s= s%26

for x in m:
    if 'a' <= x <= 'z' or 'A' <= x <= 'Z':
        x1 = (chr(ord(x)+s))
        if 'a' <= x1 <= 'z' or 'A' <= x1 <= 'Z':
            x1 = x1
        else: 
            x1 = (chr(ord(x)-26+s))
    else: 
        x1 = x
    nm = nm + x1

print(nm)
