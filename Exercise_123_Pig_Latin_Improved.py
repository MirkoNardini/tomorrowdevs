n_str= str(input('Enter a string:'))
words= n_str.split()
x=0
y = 0
list = []
res = ''
z = 0
r = ''

for i in words:
    if i[0]!='a' and i[0]!='e' and i[0]!='i' and i[0]!='o' and i[0]!='u' and i[0]!='y' :
        for a in i:
            if a != 'a' and a != 'e' and a != 'i' and a != 'o' and a != 'u' and a != 'y':
                i = i[1:]
                i = i + a
                print(i)
            elif a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u' or a == 'y':
                break
        words[y] = i
        y = y + 1
    else:
        i = i+'way'
        words[y] = i


for i in words:
    if '.' in i:
        r= i.replace('.','')
        r = r + '.'
        words[z] = r
        z = z + 1
    elif '!' in i:
        r= i.replace('!','')
        r = r + '!'
        words[z] = r
        z = z + 1
    elif '?' in i:
        r = i.replace('?','')
        r = r + '?'
        words[z] = r
        z = z + 1
        print('te')
    elif ',' in i:
        r= i.replace(',','')
        r = r + ','
        words[z] = r
        z = z + 1
    else:
        z = z+1
    res = res + ' '+ r



print(res)
