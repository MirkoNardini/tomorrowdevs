# Scrivi i numeri in inglese
from random import *

numeri = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
          0: "zero", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
          16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
          40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

mille = 1000

def nEnglish(v):
    if v < 20:
        return numeri[v]

    if v < 100:
        if v % 10 == 0:
            return numeri[v]
        else:
            return numeri[v // 10 * 10] + " " + numeri[v % 10]

    if v < mille:
        if v % 100 == 0:
            return numeri[v // 100] + " cento"
        else:
            return numeri[v // 100] + " cento " + nEnglish(v % 100)

def main():
    scelta = int(randint(1, 999))
    print(nEnglish(scelta))
    for x in range(1, 999):
        print(nEnglish(x))


main()
