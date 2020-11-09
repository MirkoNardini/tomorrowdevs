def tras(v,t):
    if len(v)== 0:
        return len(t)
    elif len(t)== 0:
        return len(v)
    else:
        cost = 0
        if v [len(v)-1]!=t[len(t)-1]:
            cost = 1
        tras1 = tras(v[0: len(v) - 1], t) + 1
        tras2 = tras(v, t[0: len(t) - 1]) + 1
        tras3 = tras(v[0: len(s) - 1], t[0: len(t) - 1]) + cost
        return min(tras1,tras2,tras3)

def main():
    v = str(input('Inserisci la stringa da trasformare:'))
    t = str(input('Inserisci la stringa finale:'))
    print(tras(v,t))

main()
