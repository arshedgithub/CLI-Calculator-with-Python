class Operands():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print("Addition")
        print(self.a + self.b)

    def substitution(self):
        print("Substitution")
        print(self.a - self.b)

    def multiplication(self):
        print("Multiplication")
        print(self.a * self.b)

    def division(self):
        print("Division")

        try:
            print(self.a / self.b)
        except ZeroDivisionError:
            print("Cannot Divide by Zero")


# a = float(input("Enter the First Operand : "))
# b = float(input("Enter the Second Operand : "))

# operands = Operands(a, b)
