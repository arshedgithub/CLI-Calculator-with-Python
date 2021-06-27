from functions import Operands

print("Welcome to My Python Calculator")

while True:
    print("\nEnter\t'a' for Addition\t's' for Substitution\t'm' for Multiplication\t'd' for Division")
    print("Enter q for Quit")

    c = input("Enter the Letter : ")

    a = float(input("Enter the First Operand : "))
    b = float(input("Enter the Second Operand : "))

    operands = Operands(a, b)

    if c == 'a':
        operands.addition()

    elif c == 's':
        operands.substitution()

    elif c == 'm':
        operands.multiplication()

    elif c == 'd':
        operands.division()

    elif c == 'q':
        break

    else:
        print("Sorry, Invalid Input\n")
