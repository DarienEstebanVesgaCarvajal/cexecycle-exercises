def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

eApproximation = 0.0
n = 0 

while True:
    currentTerm = 1 / factorial(n)
    eApproximation += currentTerm

    if n > 0 and abs(currentTerm) < 0.0001:
        break

    n += 1

print(f"Approximation of e: {eApproximation:.6f}")