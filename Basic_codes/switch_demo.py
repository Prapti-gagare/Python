a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

match op:
    case '+':
        print("Result:", a + b)
    case '-':
        print("Result:", a - b)
    case '*':
        print("Result:", a * b)
    case '/':
        if b != 0:
            print("Result:", a / b)
        else:
            print("Division by zero not allowed")
    case _:
        print("Invalid operator")
