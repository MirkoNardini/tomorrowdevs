import random
try:
    input = open('C:\\Users\\Mirco\\Desktop\\es python\\Files\\Words.txt')
    input = input.read()
    input = input.split()

    for t in input:
        if len(t)>=3:
            pass
        else:
            input.remove(t)
    print(input)
    password = ''
    while password == '':
        element = random.choices(input, k=2)
        element[0] = element[0].title()
        element[1] = element[1].title()
        password = element[0] + element[1]
        if len(password)>=8:
            pass
        else:
            password = ''
    print(password)

except ValueError:
    print('Ops.... qualcosa è andato storto, il programma si interromperà')
