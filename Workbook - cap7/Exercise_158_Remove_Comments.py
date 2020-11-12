input = open('C:\\Users\\Mirco\\Desktop\\es python\\prova.py', 'r')
    read = input.readlines()
    print(read)
    for line in read:
        print(line)
        if line[0] == '#':
            pass
        else:
            try:
                output = open('C:\\Users\\Mirco\\Desktop\\es python\\Files\\TestFileWrite.txt', 'a')
                output.write(line)


            except FileNotFoundError:
                print(' Ops... qualcosa con il vostro file di output è andato storto, il programma si chiude.')
                quit()


except FileNotFoundError:
    print('Ops... qualcosa con il vostro file di input è andato storto, il programma si chiude.')
    quit()
