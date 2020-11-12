enter = str(input('Inserire un grado:'))
while enter != '':
    try:
        if enter == 'A+':
            t = 4.0
        elif enter == 'A':
            t = 4.0
        elif enter == 'A-':
            t = 3.7
        elif enter == 'B+':
            t = 3.3
        elif enter == 'B':
            t = 3.0
        elif enter == 'B-':
            t = 2.7
        elif enter == 'C+':
            t = 2.3
        elif enter == 'C':
            t = 2.0
        elif enter == 'C-':
            g = 1.7
        elif enter == 'D+':
            t = 1.3
        elif enter == 'D':
            t = 1.0
        elif enter == 'F':
            t = 0
        else:
            try:
                enter = int(enter)
                enter = round(x, 1)
                if enter >= 4.0:
                    t = 'A+'
                elif 0 >= round(enter - 4, 1) >= -0.1:
                    t = 'A'
                elif -0.2 >= round(enter - 4, 1) >= -0.5:
                    t = 'A-'
                elif 0.4 >= round(enter - 3, 1) >= 0.2:
                    t = 'B+'
                elif 0.1 >= round(enter - 3, 1) >= -0.1:
                    t = 'B'
                elif -0.2 >= round(enter - 3, 1) >= -0.5:
                    t = 'B-'
                elif 0.4 >= round(enter - 2, 1) >= 0.2:
                    t = 'C+'
                elif 0.1 >= round(enter - 2, 1) >= -0.1:
                    t = 'C'
                elif -0.2 >= round(enter - 2, 1) >= -0.5:
                    t = 'C-'
                elif 0.4 >= round(enter - 1, 1) >= 0.2:
                    t = 'D+'
                elif 0.1 >= round(enter - 1, 1) >= -0.1:
                    t = 'D'
                elif -0.2 >= round(enter - 1, 1):
                    t = 'F'
            except ValueError:
                print('Ops, qualcosa è andato storto, riprova')
                t = ''
        print(t)
    except ValueError:
        print('Ops, qualcosa è andato storto, riprova')
    enter = str(input('Inserire un grado:'))
