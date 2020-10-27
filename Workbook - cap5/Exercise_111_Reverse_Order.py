ins = int(input('''questo programma ti permette di inserire diversi vaori
se desideri terminare il programma inserisci 0

inserisci il primo valore:  '''))

valore = []
valore.append(ins)

for i in valore:
    ins = int(input('inserisci altro valore: '''))
    if ins == 0:
        break
    valore.append(ins)

valore.reverse()
for i in valore:
    print(i)
    
