from operands import Operands

print("Welcome to My Python Calculator")

while True:
    print("\nEnter\t'a' for Addition\t's' for Substitution\t'm' for Multiplication\t'd' for Division")
    print("Enter q for Quit")

    c = input("Enter the Letter : ")

    if c.strip() == '':
        continue

    elif c == 'q':
        break

    try:
        a = float(input("Enter the First Operand : "))
        b = float(input("Enter the Second Operand : "))

    except ValueError:
        print("Error : Invalid input")

    operands = Operands(a, b)

    if c == 'a':
        operands.addition()

    elif c == 's':
        operands.substitution()

    elif c == 'm':
        operands.multiplication()

    elif c == 'd':
        operands.division()

    else:
        print("Sorry, Invalid Input\n")
