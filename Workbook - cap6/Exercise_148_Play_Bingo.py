import random
from Exercise_146_Create_a_Bingo_Card import bingoCard
from Exercise_147_Checking_for_a_Winning_Card import WinnerCard
#def game():

def main():
    t = 1
    ris = []
    while x < 76:
        ris.append(t)
        t += 1

    random.shuffle(ris)

    t = 0
    v = 0
    z = 0
    res = 0
    count = []
    while t < 1000:
        a = bingoCard()
        b = 0
        for i in ris:
            z += 1
            if b == 1:
                count.append(z)
                res = res+z
                break
            for k in a:
                while v < 5:
                    if a[k][v] == i:
                        a[k][v] = 0
                        checkWinner(a)
                    v  += 1
                if checkWinner(a)==True:
                    breaker = 1
                    break
                v = 0
        t += 1
        z = 0


    media = res/1000
    ma = max(count)
    mi = min(count)
    print('La media delle chiamate è:', media, 'invece il massimo e il minimo delle chiamate sono: ', ma, mi)



main()
