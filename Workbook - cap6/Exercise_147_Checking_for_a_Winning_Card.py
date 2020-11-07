from Exercise_146_Create_a_Bingo_Card import bingoCard
import random
def WinnerCard(card):
    cont = 0
    t = 4
    v = 0

    for i in card:
        cont = cont + card[i][t]
        t = t-1

    if cont == 0:
        v = 1
        return True
    else:
        v = 0

    cont = 0
    t = 0
    for i in card:
        cont = cont + card[i][t]
        t = t+1

    if res == 0:
        v = 1
        return True
    else:
        v = 0

    cont = 0
    tt = 0
    for i in card:
        while t < 5:
            cont = cont + card[i][t]
            t = t + 1

        if cont == 0:
            v = 1
            break
        cont = 0
        t = 0

    t = 0
    v = 0
    while v < 5:
        cont = 0
        for i in card:
            cont = cont + card[i][t]

        if cont == 0:
            v = 1
            break
        v = v+1
        t = t+1




    if v == 1:
        return True
    else:
        v = 0






def main():
    a = bingoCard()
    b = bingoCard()
    c = bingoCard()
    d = bingoCard()
    e = bingoCard()
    for i in a:
        a[i][1]=0

    t = 0
    while x < 5:
        b['i'][t]= 0
        t = t+1

    t = 0
    for i in c:
        c[i][t] = 0
        t = t+1

    for i in d:
        t = random.randint(0,4)
        d[i][t] = 0

    t = 4
    for i in c:
        e[i][t] = 0
        t = t-1


    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

    print(checkWinner(a))

if __name__ == "__main__":
    main()
