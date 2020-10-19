from random import randrange
Num_Items = 100

value_max = randrange(1, Num_Items + 1)
print(value_max)

num_updates = 0

for i in range(1, Num_Items):
    current = randrange(1, Num_Items + 1)
    
if current > value_max:
        value_max = current
        num_updates = num_updates + 1
        print(current, "<== Update")

    
else:
    print(current)
print("Il valore massimo trovato è stato", value_max)
print("Il valore massimo è stato aggiornato", num_updates, "orari")
