def token_list(x) :

    res = ''
    x = x.replace(" ", "")
    tokens = []
    i=0
    a = len(x)

    while i < a:
        if x[i] == "+" or x[i] == "-" or x[i] == "*" or x[i] == "/" or x[i] == "ˆ" or x[i] == "(" or x[i] == ")":
            tokens.append(x[i])
            i=i+1
        elif x[i] >= "0" and x[i] <= "9":
            y = ""
            while i < a and x[i] >= "0" and x[i] <= "9":
                y = y + x[i]
                i=i+1
                tokens.append(y)
        else:
            res = 'Qualcosa è andato storto'
            break

        res = tokens

    return res

def main():
    a = input("Inserire un'espressione: ")
    print(token_list(a))

if __name__ == "__main__":
    main()
