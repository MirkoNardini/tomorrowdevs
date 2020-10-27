from random import * 

lottery = []

while len(lottery) < 7:
    ins = randint(1,49)
    while ins in lottery:
        ins = randint(1,49)
        lottery.append(ins)

lottery.sort()
print(lottery)
