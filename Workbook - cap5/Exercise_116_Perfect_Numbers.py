from Exercise_115_List_of_Proper_Divisors import divisore

def numPerf(i):
    p = 0
    list = divisore(i)
    res = False
    for ins in list:
        p = p + ins
        if p == i:
            res = True
        else:
            res = False

    return res

def main():
    num_magic=[]
    for i in range(1,10000,1):
        a = numPerf(i)
        if a == True:
            num_magic.append(i)

    print(num_magic)

main()
