power = 1
fraction = 0.5
cumulativeSum = 0

print("Power    Fraction  Sum")

while fraction > 0.000001:
    cumulativeSum += fraction
    print(f"{power:<9} {fraction:<9} {cumulativeSum:<9}")
    power += 1
    fraction = 1 / (2 ** power)

if fraction <= 0.000001:
    print(f"Final fraction: {fraction} is less than or equal to 0.000001. Terminating the program.")