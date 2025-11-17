# Basic calculation functions based on user input

def calculate():
    while True:  # Cycle to allow multiple calculations

        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("x. Exit")

        choice = input("Enter choice (1/2/3/4/x): ")

        if choice.lower() == 'x':
            print("Exiting the calculator.")
            break  

        if choice not in ['1', '2', '3', '4']:
            print("Invalid input.")
            continue  # go back to menu

        # Only ask for numbers if operation is valid
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            print(f"{a} + {b} = {a + b}")

        elif choice == '2':
            print(f"{a} - {b} = {a - b}")

        elif choice == '3':
            print(f"{a} * {b} = {a * b}")

        elif choice == '4':
            if b != 0:
                print(f"{a} / {b} = {a / b}")
            else:
                print("Error: Division by zero is not allowed.")


# Call the calculation function
calculate()
