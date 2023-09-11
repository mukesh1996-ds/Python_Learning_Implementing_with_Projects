def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y

while True:
    try:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        choice = int(input("Enter choice (1/2/3/4/5): "))

        if choice == 5:
            print("Calculator is quitting. Goodbye!")
            break

        if choice < 1 or choice > 5:
            raise ValueError("Invalid choice. Please select a valid operation.")

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)

        print("Result:", result)

    except ValueError as ve:
        print("ValueError:", ve)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print("An unexpected error occurred:", e)
