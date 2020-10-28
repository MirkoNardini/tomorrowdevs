from Exercise_129_Tokenizing_a_String import token_list

def binary(tok):
    x = []

    for i in range(len(tok)):

        if i == 0 and (tok[i] == "+" or tok[i] == "-"):
            x.append("u" + tok[i])

        elif i>0 and (tok[i] == "+" or tok[i] == "-") and (tok[i-1] == "+" or tok[i-1] == "-" or tok[i-1] == "*" or tok[i-1] == "/" or tok[i-1] == "("):
            x.append("u" + tok[i])

        else:
            x.append(tok[i])

    return x

def main():

    exp = input("Inserire un'espressione matematica: ")
    tok = tk(exp)
    new_tok = binary(tok)
    print("Con operatori unari contrassegnati: ", new_tok)

if __name__ == "__main__":
    main()
