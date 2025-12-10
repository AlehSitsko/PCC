# storage for all employees
employees = []
# function to create a new employee
def create_employee():
    name = input("Enter employee name: ")
    age = input("Enter employee age: ")
    position = input("Enter employee position: ")

    employee = {
        "name": name,
        "age": age,
        "position": position
    }

    employees.append(employee)

    print("Employee created:")
    print(employee)
# main loop
while True:
    create_employee()

    while True:
        another = input("Do you want to add another employee? (yes/no): ").lower()
        
        if another == "yes":
            break
        elif another == "no":
            print("\nAll employees:")
            print(employees)
            exit()
        else:
            print("Invalid input, please enter 'yes' or 'no'.")
