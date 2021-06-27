import functions

print("Welcome to My Python Calculator")

while True:
    print("\nEnter\t'a' for Addition\t's' for Substitution\t'm' for Multiplication\t'd' for Division")
    print("Enter q for Quit")

    c = input("Enter the Letter : ")

    if c == 'a':
        functions.addition()

    elif c == 's':
        functions.substitution()

    elif c == 'm':
        functions.multiplication()

    elif c == 'd':
        functions.division()

    elif c == 'q':
        break

    else:
        print("Sorry, Invalid Input\n")
