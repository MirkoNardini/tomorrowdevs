import random


def bingoCard():
    Card = {'b': [], 'i': [], 'n': [], 'g': [], 'o': []}

    t = 0

    while t < 5:
        v = random.randint(1, 15)
        if v not in Card['b']:
            Card['b'].append(v)
            t = t + 1
    t = 0
    while t < 5:
        i = random.randint(16, 30)
        if i not in Card['i']:
            card['i'].append(i)
            t = t + 1
    t = 0
    while t < 5:
        n = random.randint(31, 45)
        if n not in Card['n']:
            Card['n'].append(n)
            t = t + 1
    t = 0
    while t < 5:
        a = random.randint(46, 60)
        if a not in Card['g']:
            Card['g'].append(a)
            t = t + 1
    t = 0
    while t < 5:
        o = random.randint(61, 75)
        if o not in Card['o']:
            Card['o'].append(o)
            t = t + 1

    return Card

def main():
    print(bingoCard())

if __name__ == "__main__":
    main()
