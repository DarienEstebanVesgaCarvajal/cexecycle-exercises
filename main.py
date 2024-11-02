def collatzSequence(x):
    sequence = []
    while x != 1:
        sequence.append(x)
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
    sequence.append(1)
    return sequence

def printCollatzSequence(x):
    sequence = collatzSequence(x)
    print(" ".join(map(str, sequence)))

def collatzLengthsUpTo(x):
    lengths = []
    for y in range(1, x + 1):
        lengths.append(len(collatzSequence(y)))
    return lengths

def printCollatzLengths(x):
    lengths = collatzLengthsUpTo(x)
    for y in range(x):
        print(f"{y + 1} {'*' * lengths[y]}")

x = int(input("Enter a positive integer: "))
print(f"Collatz sequence for {x}:")
printCollatzSequence(x)
print(f"\nCollatz lengths for numbers up to {x}:")
printCollatzLengths(x)