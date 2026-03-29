def calculator():
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("1.Add  2.Subtract  3.Multiply  4.Divide")
    choice = input("Choose operation: ")

    if choice == '1':
        print("Result:", a + b)
    elif choice == '2':
        print("Result:", a - b)
    elif choice == '3':
        print("Result:", a * b)
    elif choice == '4':
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid choice")

calculator()