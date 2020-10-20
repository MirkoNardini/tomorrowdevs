def Median_function(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)

def main():
    x = float(input("Inserire il primo valore: "))
    y = float(input("Inserire il secondo valore: "))
    z = float(input("Inserire il terzo valore: "))

    print("Il valore mediano è:", Median_function(x, y, z))

main()
