class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1*num2

    def division(self,num1,num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero!")
        else:
            return num1/num2
    print("select operator 1:ADD 2:SUBTRACT 3:MULTIPLY 4:DIVISION")

while True:
    choice = input("enter choice")
    try:
        num1 = float(input("enter first number:"))
        num2 = float(input("enter second number"))
    except ValueError:
        print("invalid input")
    calc = Calculator(num1, num2)
    if choice == '1':
        print(calc.add(num1,num2))
    elif choice == '2':
        print(calc.sub(num1, num2))
    elif choice == '3':
        print(calc.multiply(num1, num2))
    elif choice == '4':
        if num1 and num2 !=0:
            print(calc.division(num1,num2))
        else:
            print("error")
    else:
        print("invalid")
