class Calculate():

    def __init__(self):
        pass

    # Add methods to add, subtract, divide and multiply two numbers
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError
        return round((num1 / num2), 3)

calc = Calculate()
while True:
    num1 = int(input("give me the first number!"))
    num2 = int(input("give me the second number!"))
    print ("adding them gives me {}".format(int(calc.add(num1, num2))))
    print ("subtracting them gives me {}".format(int(calc.subtract(num1, num2))))
    print ("multiplying them gives me {}".format(int(calc.multiply(num1, num2))))
    try:
        print ("dividing them gives me {}".format(calc.divide(num1, num2)))
    except ZeroDivisionError:
        print ("stop trying to break the universe!")
