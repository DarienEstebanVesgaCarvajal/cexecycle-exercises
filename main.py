side = int(input("What's the side length?: "))

for x in range(2 * side - 1):
    if x < side:
        spaces = side - x - 1
        dots = side + 2 * x
    else:
        spaces = x - side + 1
        dots = side + 2 * (2 * side - x - 2)    

    print(' ' * spaces + '·' * dots)