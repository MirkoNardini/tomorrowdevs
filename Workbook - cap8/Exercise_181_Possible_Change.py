from itertools import combinations_with_replacement

def number_coins(imp, t, i = 0):
    coins = [0.25, 0.10, 0.05, 0.01]
    combinations = list(combinations_with_replacement(coins, t))
    if imp != round(sum(combinations[i]), 4):
        i += 1
        if i >= len(list(combinations)):
            return False
        else:
            return numbers_coins(imp, t, i)
    else:
        return True
def main():
    imp = float(input("Inserire una somma di denaro: "))
    num_coins = int(input("Inserire un numero di monete: "))
    print(number_coins(imp, num_coins))

main()
