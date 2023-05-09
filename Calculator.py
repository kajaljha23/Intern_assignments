class Calculator:
    def __init__(self):
        """"""

    @staticmethod
    def add(num1, num2):
        return num1 + num2

    @staticmethod
    def sub(num1, num2):
        return num1 - num2

    @staticmethod
    def multiply(num1, num2):
        return num1 * num2

    @staticmethod
    def division(num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero!")
        else:
            return num1 / num2

    print("select operator 1:ADD 2:SUBTRACT 3:MULTIPLY 4:DIVISION")


while True:
    choice = input("enter choice")
    try:
        value_1 = float(input("enter first number:"))
        value_2 = float(input("enter second number"))
    except ValueError:
        print("invalid input")
        exit()
    calc = Calculator()
    if choice == '1':
        print(calc.add(value_1, value_2))
    elif choice == '2':
        print(calc.sub(value_1, value_2))
    elif choice == '3':
        print(calc.multiply(value_1, value_2))
    elif choice == '4':
        if value_1 and value_2 != 0:
            print(calc.division(value_1, value_2))
        else:
            print("error")
    else:
        print("invalid")
