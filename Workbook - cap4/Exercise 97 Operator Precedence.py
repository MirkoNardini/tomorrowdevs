def precedence(x):
    if x=='-' or x =='+':
        res = 1
    elif x=='*' or x=='/':
        res = 2
    elif x=='ˆ':
        res=3
    else:
        res='Quello che hai inserito non è un operatore'

    return res

def main():
    a = str(input('Inserire un operatore matematico:'))
    print(precedence(a))

if __name__ == "__main__":
        main()
