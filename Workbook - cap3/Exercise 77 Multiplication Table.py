Min = 1
Max = 10

print("    ", end="")
for i in range(Min, Max + 1):
    print("%4d" % i, end="")
print()

for i in range(Min, Max + 1):
    print("%4d" % i, end="")
    for j in range(Min, Max + 1):
        print("%4d" % (i * j), end="")
    print()
