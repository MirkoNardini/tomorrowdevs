from ex89 import ord

def song(a):
    print("On the", ord(a), "day of christmas")
    print("My true love sent to me:")
    if a >= 12:
        print("Twelve drummers drumming,")
    if a >= 11:
        print("Eleven pipers piping,")
    if a >= 10:
        print("Ten lords a-leaping,")
    if a >= 9:
        print("Nine ladies dancing,")
    if a >= 8:
        print("Eight maids a-milking,")
    if a >= 7:
        print("Seven swans a-swimming,")
    if a >= 6:
        print("Six geese a-laying,")
    if a >= 5:
        print("Five golden rings,")
    if a >= 4:
        print("Four calling birds,")
    if a >= 3:
        print("Three French hens,")
    if a >= 2:
        print("Two turtle doves,")
    if a == 1:
        print("A", end=" ")
    else:
        print("And a", end=" ")
    print("partridge in a pear tree.")
    print()

def main():
    for x in range(1, 13):
        song(x)

main()
