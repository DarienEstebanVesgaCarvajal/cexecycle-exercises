size = 10

for x in range(1, size + 1):
    for y in range (1, size + 1):
        print(str(x * y).rjust(5), end="")
    print()