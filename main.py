divisor = int(input("What number do you want to know its divisors?: "))

for x in range(1, divisor +1):
    if divisor % x == 0:
        print(x, end = " ")