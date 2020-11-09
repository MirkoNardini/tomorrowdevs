def quadrato(n,t):
    if 0 < n - t**2 < 10** - 12:
        return t
    else:
        t = quadrato(n,(t+(n/t))/2)
        return t



def main():
    n = 32
    t = 1
    print(quadrato(n,t))

main()
