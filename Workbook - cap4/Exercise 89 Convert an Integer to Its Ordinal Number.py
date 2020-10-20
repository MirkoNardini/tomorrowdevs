def integer(n):
    if n==1:
        name="Primo"
    elif n==2:
        name="Secondo"
    elif n==3:
        name="Terzo"
    elif n==4:
        name="Quarto"
    elif n==5:
        name="Quinto"
    elif n==6:
        name="Sesto"
    elif n==7:
        name="Settimo"
    elif n==8:
        name="Ottavo"
    elif n==9:
        name="Nono"
    elif n==10:
        name="Decimo"
    elif n==11:
        name="Undicesio"
    elif n==12:
        name="Dodicesimo"
    return name
    if n<1 or n>12:
        return ""

def main():
    for i in range(1,12+1):
        print(integer(i))

if __name__ == "__main__":
    main()
