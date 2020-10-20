def window(s,w):
    ns = ' '
    if len(s) >= w:
        ns = s
    elif len(s)<= w:
        a = (w -len(s)) // 2
        ns = (ns*a)+ s

    return ns

def main():
    width= 10
    string= str(input('Inserire una stringa:'))
    print(window(string,width))

if __name__ == "__main__":
        main()
