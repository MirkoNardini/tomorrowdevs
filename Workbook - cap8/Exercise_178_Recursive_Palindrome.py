def palindrome(t):
    ris = ''
    if len(t)<=1:
        return True
    elif t[0] == t[len(t)-1]:

        t = t[1:len(t)-1]
        palindrome(t)
        return True
    else:
        return False



def main():
    x = str(input('Inserisci stringa:'))
    print('Questa stringa è un palidromo?',palindrome(t))

main()
