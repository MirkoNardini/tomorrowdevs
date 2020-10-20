import random
sum =0
z = 0
while z < 10:
    n = 0 
    q=0 
    w=0 
    tot ='' 
    while q !=3 and w!=3:
        a = random.randint(0, 1)
        if a == 1:
            x = ' H'
            tot = tot + x
            q = q+1
            w = 0
        else:
            x = ' T'
            tot = tot + x
            w = w+1
            q =0
        n = n + 1

    print(tot,'(',n,'flips necessari)')
    sum = sum+n
    z = z+1

av = sum/10
print('In media',av,'flips necessari')
