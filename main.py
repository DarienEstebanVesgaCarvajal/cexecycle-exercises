numberTerms = int(input("What's the number of terms?: "))

piEstimate = 0

for x in range(numberTerms):
    term = (-1) ** x / (2 * x + 1)
    piEstimate += term

piEstimate *= 4

print(piEstimate)
