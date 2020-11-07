def decimalRecurs(t):

    if t == 0 or t == 1:
        return t
    if t < 0:
        return print('The entered value is not a positive integer')
    elif t >= 0:
        c = t % 2
        v = t // 2
        decimalRecurs(v)
        res = str(c) + str(decimalRecurs(v))
        return res

def main():
    t = int(input('Enter a positive integer:'))
    res = decimalRecurs(t)
    c = len(res)
    count = -1
    ris = ''
    for x in res:
        counter = count + 1
        d = c - count
        e = c - count - 1
        g = r[e:d]
        ris = ris + g

    print(ris)
main()
